---
title: "usb_submit_urb(9)"
name: "usb_submit_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_submit_urb/"
description: "usb_submit_urb – issue an asynchronous transfer request for an endpoint"
---

<p>usb_submit_urb &#8211; issue an asynchronous transfer request for an endpoint</p>
<h2>Synopsis</h2>
<pre><code>int usb_submit_urb(struct urb *urb, gfp_t mem_flags);</code></pre>
<h2>Arguments</h2>
<p><i>urb</i></p>
<dl>
<dd>
<dd>pointer to the urb describing the request</dl>
<p> <i>mem_flags</i></p>
<dl>
<dd>the type of memory to allocate, see <code>kmalloc</code> for a list of valid options for this.</dl>
<h2>Description</h2>
<p>This submits a transfer request, and transfers control of the URB describing that request to the USB subsystem. Request completion will be indicated later, asynchronously, by calling the completion handler. The three types of completion are success, error, and unlink (a software-induced fault, also called &#8220;request cancellation&#8221;). </p>
<p> URBs may be submitted in interrupt context. </p>
<p> The caller must have correctly initialized the URB before submitting it. Functions such as <code>usb_fill_bulk_urb</code> and <code>usb_fill_control_urb</code> are available to ensure that most fields are correctly initialized, for the particular kind of transfer, although they will not initialize any transfer flags. </p>
<p> If the submission is successful, the <code>complete</code> callback from the URB will be called exactly once, when the USB core and Host Controller Driver (HCD) are finished with the URB. When the completion function is called, control of the URB is returned to the device driver which issued the request. The completion handler may then immediately free or reuse that URB. </p>
<p> With few exceptions, USB device drivers should never access URB fields provided by usbcore or the HCD until its <code>complete</code> is called. The exceptions relate to periodic transfer scheduling. For both interrupt and isochronous urbs, as part of successful URB submission urb-&gt;interval is modified to reflect the actual transfer period used (normally some power of two units). And for isochronous urbs, urb-&gt;start_frame is modified to reflect when the URB&#8217;s transfers were scheduled to start. </p>
<p> Not all isochronous transfer scheduling policies will work, but most host controller drivers should easily handle ISO queues going from now until 10-200 msec into the future. Drivers should try to keep at least one or two msec of data in the queue; many controllers require that new transfers start at least 1 msec in the future when they are added. If the driver is unable to keep up and the queue empties out, the behavior for new submissions is governed by the URB_ISO_ASAP flag. If the flag is set, or if the queue is idle, then the URB is always assigned to the first available (and not yet expired) slot in the endpoint&#8217;s schedule. If the flag is not set and the queue is active then the URB is always assigned to the next slot in the schedule following the end of the endpoint&#8217;s previous URB, even if that slot is in the past. When a packet is assigned in this way to a slot that has already expired, the packet is not transmitted and the corresponding usb_iso_packet_descriptor&#8217;s status field will return -EXDEV. If this would happen to all the packets in the URB, submission fails with a -EXDEV error code. </p>
<p> For control endpoints, the synchronous <code>usb_control_msg</code> call is often used (in non-interrupt context) instead of this call. That is often used through convenience wrappers, for the requests that are standardized in the USB 2.0 specification. For bulk endpoints, a synchronous <code>usb_bulk_msg</code> call is available.</p>
<h2>Return</h2>
<p>0 on successful submissions. A negative error number otherwise. </p>
<p> Request Queuing: </p>
<p> URBs may be submitted to endpoints before previous ones complete, to minimize the impact of interrupt latencies and system overhead on data throughput. With that queuing policy, an endpoint&#8217;s queue would never be empty. This is required for continuous isochronous data streams, and may also be required for some kinds of interrupt transfers. Such queuing also maximizes bandwidth utilization by letting USB controllers start work on later requests before driver software has finished the completion processing for earlier (successful) requests. </p>
<p> As of Linux 2.6, all USB endpoint transfer queues support depths greater than one. This was previously a HCD-specific behavior, except for ISO transfers. Non-isochronous endpoint queues are inactive during cleanup after faults (transfer errors or cancellation). </p>
<p> Reserved Bandwidth Transfers: </p>
<p> Periodic transfers (interrupt or isochronous) are performed repeatedly, using the interval specified in the urb. Submitting the first urb to the endpoint reserves the bandwidth necessary to make those transfers. If the USB subsystem can&#8217;t allocate sufficient bandwidth to perform the periodic request, submitting such a periodic request should fail. </p>
<p> For devices under xHCI, the bandwidth is reserved at configuration time, or when the alt setting is selected. If there is not enough bus bandwidth, the configuration/alt setting request will fail. Therefore, submissions to periodic endpoints on devices under xHCI should never fail due to bandwidth constraints. </p>
<p> Device drivers must explicitly request that repetition, by ensuring that some URB is always on the endpoint&#8217;s queue (except possibly for short periods during completion callbacks). When there is no longer an urb queued, the endpoint&#8217;s bandwidth reservation is canceled. This means drivers can use their completion handlers to ensure they keep bandwidth they need, by reinitializing and resubmitting the just-completed urb until the driver longer needs that periodic bandwidth. </p>
<p> Memory Flags: </p>
<p> The general rules for how to decide which mem_flags to use are the same as for kmalloc. There are four different possible values; GFP_KERNEL, GFP_NOFS, GFP_NOIO and GFP_ATOMIC. </p>
<p> GFP_NOFS is not ever used, as it has not been implemented yet. </p>
<p> GFP_ATOMIC is used when (a) you are inside a completion handler, an interrupt, bottom half, tasklet or timer, or (b) you are holding a spinlock or rwlock (does not apply to semaphores), or (c) current-&gt;state != TASK_RUNNING, this is the case only after you&#8217;ve changed it. </p>
<p> GFP_NOIO is used in the block io path and error handling of storage devices. </p>
<p> All other situations use GFP_KERNEL. </p>
<p> Some more specific rules for mem_flags can be inferred, such as (1) start_xmit, timeout, and receive methods of network drivers must use GFP_ATOMIC (they are called with a spinlock held); (2) queuecommand methods of scsi drivers must use GFP_ATOMIC (also called with a spinlock held); (3) If you use a kernel thread with a network driver you must use GFP_NOIO, unless (b) or (c) apply; (4) after you have done a <code>down</code> you can use GFP_KERNEL, unless (b) or (c) apply or your are in a storage driver&#8217;s block io path; (5) USB probe and disconnect can use GFP_KERNEL unless (b) or (c) apply; and (6) changing firmware on a running storage or net device uses GFP_NOIO, unless b) or c) apply</p>
<h2>Copyright</h2>
