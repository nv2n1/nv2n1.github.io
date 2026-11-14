---
title: "usb_clear_halt(9)"
name: "usb_clear_halt"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_clear_halt/"
description: "usb_clear_halt – tells device to clear endpoint halt/stall condition"
---

<p>usb_clear_halt &#8211; tells device to clear endpoint halt/stall condition</p>
<h2>Synopsis</h2>
<pre><code>int usb_clear_halt(struct usb_device *dev, int pipe);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device whose endpoint is halted</dl>
<p> <i>pipe</i></p>
<dl>
<dd>endpoint &#8220;pipe&#8221; being cleared</dl>
<h2>Context</h2>
<p>!in_interrupt ()</p>
<h2>Description</h2>
<p>This is used to clear halt conditions for bulk and interrupt endpoints, as reported by URB completion status. Endpoints that are halted are sometimes referred to as being &#8220;stalled&#8221;. Such endpoints are unable to transmit or receive data until the halt status is cleared. Any URBs queued for such an endpoint should normally be unlinked by the driver before clearing the halt condition, as described in sections 5.7.5 and 5.8.5 of the USB 2.0 spec. </p>
<p> Note that control and isochronous endpoints don&#8217;t halt, although control endpoints report &#8220;protocol stall&#8221; (for unsupported requests) using the same status code used to report a true stall. </p>
<p> This call is synchronous, and may not be used in an interrupt context.</p>
<h2>Return</h2>
<p>Zero on success, or else the status code returned by the underlying <code>usb_control_msg</code> call.</p>
<h2>Copyright</h2>
