---
title: "usb_hcd_link_urb_to_ep(9)"
name: "usb_hcd_link_urb_to_ep"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_hcd_link_urb_to_ep/"
description: "usb_hcd_link_urb_to_ep – add an URB to its endpoint queue"
---

<p>usb_hcd_link_urb_to_ep &#8211; add an URB to its endpoint queue</p>
<h2>Synopsis</h2>
<pre><code>int usb_hcd_link_urb_to_ep(struct usb_hcd *hcd, struct urb *urb);</code></pre>
<h2>Arguments</h2>
<p><i>hcd</i></p>
<dl>
<dd>
<dd>host controller to which <i>urb</i> was submitted</dl>
<p> <i>urb</i></p>
<dl>
<dd>URB being submitted</dl>
<h2>Description</h2>
<p>Host controller drivers should call this routine in their <code>enqueue</code> method. The HCD&#8217;s private spinlock must be held and interrupts must be disabled. The actions carried out here are required for URB submission, as well as for endpoint shutdown and for usb_kill_urb.</p>
<h2>Return</h2>
<p>0 for no error, otherwise a negative error code (in which case the <code>enqueue</code> method must fail). If no error occurs but <code>enqueue</code> fails anyway, it must call <code>usb_hcd_unlink_urb_from_ep</code> before releasing the private spinlock and returning.</p>
<h2>Copyright</h2>
