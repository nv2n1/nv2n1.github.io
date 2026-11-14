---
title: "usb_hcd_giveback_urb(9)"
name: "usb_hcd_giveback_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_hcd_giveback_urb/"
description: "usb_hcd_giveback_urb – return URB from HCD to device driver"
---

<p>usb_hcd_giveback_urb &#8211; return URB from HCD to device driver</p>
<h2>Synopsis</h2>
<pre><code>void usb_hcd_giveback_urb(struct usb_hcd *hcd, struct urb *urb, int status);</code></pre>
<h2>Arguments</h2>
<p><i>hcd</i></p>
<dl>
<dd>
<dd>host controller returning the URB</dl>
<p> <i>urb</i></p>
<dl>
<dd>urb being returned to the USB device driver.</dl>
<p> <i>status</i></p>
<dl>
<dd>completion status code for the URB.</dl>
<h2>Context</h2>
<p><code>in_interrupt</code></p>
<h2>Description</h2>
<p>This hands the URB from HCD to its USB device driver, using its completion function. The HCD has freed all per-urb resources (and is done using urb-&gt;hcpriv). It also released all HCD locks; the device driver won&#8217;t cause problems if it frees, modifies, or resubmits this URB. </p>
<p> If <i>urb</i> was unlinked, the value of <i>status</i> will be overridden by <i>urb</i>-&gt;unlinked. Erroneous short transfers are detected in case the HCD hasn&#8217;t checked for them.</p>
<h2>Copyright</h2>
