---
title: "usb_bulk_msg(9)"
name: "usb_bulk_msg"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_bulk_msg/"
description: "usb_bulk_msg – Builds a bulk urb, sends it off and waits for completion"
---

<p>usb_bulk_msg &#8211; Builds a bulk urb, sends it off and waits for completion</p>
<h2>Synopsis</h2>
<pre><code>int usb_bulk_msg(struct usb_device *usb_dev, unsigned int pipe, void *data, int len, int *actual_length, int timeout);</code></pre>
<h2>Arguments</h2>
<p><i>usb_dev</i></p>
<dl>
<dd>
<dd>pointer to the usb device to send the message to</dl>
<p> <i>pipe</i></p>
<dl>
<dd>endpoint &#8220;pipe&#8221; to send the message to</dl>
<p> <i>data</i></p>
<dl>
<dd>pointer to the data to send</dl>
<p> <i>len</i></p>
<dl>
<dd>length in bytes of the data to send</dl>
<p> <i>actual_length</i></p>
<dl>
<dd>pointer to a location to put the actual length transferred in bytes</dl>
<p> <i>timeout</i></p>
<dl>
<dd>time in msecs to wait for the message to complete before timing out (if 0 the wait is forever)</dl>
<h2>Context</h2>
<p>!in_interrupt ()</p>
<h2>Description</h2>
<p>This function sends a simple bulk message to a specified endpoint and waits for the message to complete, or timeout. </p>
<p> Don&#8217;t use this function from within an interrupt context, like a bottom half handler. If you need an asynchronous message, or need to send a message from within interrupt context, use <code>usb_submit_urb</code> If a thread in your driver uses this call, make sure your <code>disconnect</code> method can wait for it to complete. Since you don&#8217;t have a handle on the URB used, you can&#8217;t cancel the request. </p>
<p> Because there is no <code>usb_interrupt_msg</code> and no USBDEVFS_INTERRUPT ioctl, users are forced to abuse this routine by using it to submit URBs for interrupt endpoints. We will take the liberty of creating an interrupt URB (with the default interval) if the target is an interrupt endpoint.</p>
<h2>Return</h2>
<p>If successful, 0. Otherwise a negative error number. The number of actual bytes transferred will be stored in the <i>actual_length</i> parameter.</p>
<h2>Copyright</h2>
