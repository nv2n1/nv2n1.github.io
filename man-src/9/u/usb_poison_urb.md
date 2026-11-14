---
title: "usb_poison_urb(9)"
name: "usb_poison_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_poison_urb/"
description: "usb_poison_urb – reliably kill a transfer and prevent further use of an URB"
---

<p>usb_poison_urb &#8211; reliably kill a transfer and prevent further use of an URB</p>
<h2>Synopsis</h2>
<pre><code>void usb_poison_urb(struct urb *urb);</code></pre>
<h2>Arguments</h2>
<p><i>urb</i></p>
<dl>
<dd>
<dd>pointer to URB describing a previously submitted request, may be NULL</dl>
<h2>Description</h2>
<p>This routine cancels an in-progress request. It is guaranteed that upon return all completion handlers will have finished and the URB will be totally idle and cannot be reused. These features make this an ideal way to stop I/O in a <code>disconnect</code> callback. If the request has not already finished or been unlinked the completion handler will see urb-&gt;status == -ENOENT. </p>
<p> After and while the routine runs, attempts to resubmit the URB will fail with error -EPERM. Thus even if the URB&#8217;s completion handler always tries to resubmit, it will not succeed and the URB will become idle. </p>
<p> The URB must not be deallocated while this routine is running. In particular, when a driver calls this routine, it must insure that the completion handler cannot deallocate the URB. </p>
<p> This routine may not be used in an interrupt context (such as a bottom half or a completion handler), or when holding a spinlock, or in other situations where the caller can&#8217;t <code>schedule</code>. </p>
<p> This routine should not be called by a driver after its disconnect method has returned.</p>
<h2>Copyright</h2>
