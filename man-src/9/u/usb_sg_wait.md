---
title: "usb_sg_wait(9)"
name: "usb_sg_wait"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_sg_wait/"
description: "usb_sg_wait – synchronously execute scatter/gather request"
---

<p>usb_sg_wait &#8211; synchronously execute scatter/gather request</p>
<h2>Synopsis</h2>
<pre><code>void usb_sg_wait(struct usb_sg_request *io);</code></pre>
<h2>Arguments</h2>
<p><i>io</i></p>
<dl>
<dd>
<dd>request block handle, as initialized with <code>usb_sg_init</code>. some fields become accessible when this call returns.</dl>
<h2>Context</h2>
<p>!in_interrupt ()</p>
<h2>Description</h2>
<p>This function blocks until the specified I/O operation completes. It leverages the grouping of the related I/O requests to get good transfer rates, by queueing the requests. At higher speeds, such queuing can significantly improve USB throughput. </p>
<p> There are three kinds of completion for this function. (1) success, where io-&gt;status is zero. The number of io-&gt;bytes transferred is as requested. (2) error, where io-&gt;status is a negative errno value. The number of io-&gt;bytes transferred before the error is usually less than requested, and can be nonzero. (3) cancellation, a type of error with status -ECONNRESET that is initiated by <code>usb_sg_cancel</code>. </p>
<p> When this function returns, all memory allocated through <code>usb_sg_init</code> or this call will have been freed. The request block parameter may still be passed to <code>usb_sg_cancel</code>, or it may be freed. It could also be reinitialized and then reused. </p>
<p> Data Transfer Rates: </p>
<p> Bulk transfers are valid for full or high speed endpoints. The best full speed data rate is 19 packets of 64 bytes each per frame, or 1216 bytes per millisecond. The best high speed data rate is 13 packets of 512 bytes each per microframe, or 52 KBytes per millisecond. </p>
<p> The reason to use interrupt transfers through this API would most likely be to reserve high speed bandwidth, where up to 24 KBytes per millisecond could be transferred. That capability is less useful for low or full speed interrupt endpoints, which allow at most one packet per millisecond, of at most 8 or 64 bytes (respectively). </p>
<p> It is not necessary to call this function to reserve bandwidth for devices under an xHCI host controller, as the bandwidth is reserved when the configuration or interface alt setting is selected.</p>
<h2>Copyright</h2>
