---
title: "usb_unlink_urb(9)"
name: "usb_unlink_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_unlink_urb/"
description: "usb_unlink_urb – abort/cancel a transfer request for an endpoint"
---

<p>usb_unlink_urb &#8211; abort/cancel a transfer request for an endpoint</p>
<h2>Synopsis</h2>
<pre><code>int usb_unlink_urb(struct urb *urb);</code></pre>
<h2>Arguments</h2>
<p><i>urb</i></p>
<dl>
<dd>
<dd>pointer to urb describing a previously submitted request, may be NULL</dl>
<h2>Description</h2>
<p>This routine cancels an in-progress request. URBs complete only once per submission, and may be canceled only once per submission. Successful cancellation means termination of <i>urb</i> will be expedited and the completion handler will be called with a status code indicating that the request has been canceled (rather than any other code). </p>
<p> Drivers should not call this routine or related routines, such as <code>usb_kill_urb</code> or <code>usb_unlink_anchored_urbs</code>, after their disconnect method has returned. The disconnect function should synchronize with a driver&#8217;s I/O routines to insure that all URB-related activity has completed before it returns. </p>
<p> This request is asynchronous, however the HCD might call the -&gt;<code>complete</code> callback during unlink. Therefore when drivers call <code>usb_unlink_urb</code>, they must not hold any locks that may be taken by the completion function. Success is indicated by returning -EINPROGRESS, at which time the URB will probably not yet have been given back to the device driver. When it is eventually called, the completion function will see <i>urb</i>-&gt;status == -ECONNRESET. Failure is indicated by <code>usb_unlink_urb</code> returning any other value. Unlinking will fail when <i>urb</i> is not currently &#8220;linked&#8221; (i.e., it was never submitted, or it was unlinked before, or the hardware is already finished with it), even if the completion handler has not yet run. </p>
<p> The URB must not be deallocated while this routine is running. In particular, when a driver calls this routine, it must insure that the completion handler cannot deallocate the URB.</p>
<h2>Return</h2>
<p>-EINPROGRESS on success. See description for other values on failure. </p>
<p> Unlinking and Endpoint Queues: </p>
<p> [The behaviors and guarantees described below do not apply to virtual root hubs but only to endpoint queues for physical USB devices.] </p>
<p> Host Controller Drivers (HCDs) place all the URBs for a particular endpoint in a queue. Normally the queue advances as the controller hardware processes each request. But when an URB terminates with an error its queue generally stops (see below), at least until that URB&#8217;s completion routine returns. It is guaranteed that a stopped queue will not restart until all its unlinked URBs have been fully retired, with their completion routines run, even if that&#8217;s not until some time after the original completion handler returns. The same behavior and guarantee apply when an URB terminates because it was unlinked. </p>
<p> Bulk and interrupt endpoint queues are guaranteed to stop whenever an URB terminates with any sort of error, including -ECONNRESET, -ENOENT, and -EREMOTEIO. Control endpoint queues behave the same way except that they are not guaranteed to stop for -EREMOTEIO errors. Queues for isochronous endpoints are treated differently, because they must advance at fixed rates. Such queues do not stop when an URB encounters an error or is unlinked. An unlinked isochronous URB may leave a gap in the stream of packets; it is undefined whether such gaps can be filled in. </p>
<p> Note that early termination of an URB because a short packet was received will generate a -EREMOTEIO error if and only if the URB_SHORT_NOT_OK flag is set. By setting this flag, USB device drivers can build deep queues for large or complex bulk transfers and clean them up reliably after any sort of aborted transfer by unlinking all pending URBs at the first fault. </p>
<p> When a control URB terminates with an error other than -EREMOTEIO, it is quite likely that the status stage of the transfer will not take place.</p>
<h2>Copyright</h2>
