---
title: "usb_get_status(9)"
name: "usb_get_status"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_get_status/"
description: "usb_get_status – issues a GET_STATUS call"
---

<p>usb_get_status &#8211; issues a GET_STATUS call</p>
<h2>Synopsis</h2>
<pre><code>int usb_get_status(struct usb_device *dev, int type, int target, void *data);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the device whose status is being checked</dl>
<p> <i>type</i></p>
<dl>
<dd>USB_RECIP_*; for device, interface, or endpoint</dl>
<p> <i>target</i></p>
<dl>
<dd>zero (for device), else interface or endpoint number</dl>
<p> <i>data</i></p>
<dl>
<dd>pointer to two bytes of bitmap data</dl>
<h2>Context</h2>
<p>!in_interrupt ()</p>
<h2>Description</h2>
<p>Returns device, interface, or endpoint status. Normally only of interest to see if the device is self powered, or has enabled the remote wakeup facility; or whether a bulk or interrupt endpoint is halted (&#8220;stalled&#8221;). </p>
<p> Bits in these status bitmaps are set using the SET_FEATURE request, and cleared using the CLEAR_FEATURE request. The <code>usb_clear_halt</code> function should be used to clear halt (&#8220;stall&#8221;) status. </p>
<p> This call is synchronous, and may not be used in an interrupt context. </p>
<p> Returns 0 and the status value in *<i>data</i> (in host byte order) on success, or else the status code from the underlying <code>usb_control_msg</code> call.</p>
<h2>Copyright</h2>
