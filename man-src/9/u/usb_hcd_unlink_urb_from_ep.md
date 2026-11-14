---
title: "usb_hcd_unlink_urb_from_ep(9)"
name: "usb_hcd_unlink_urb_from_ep"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_hcd_unlink_urb_from_ep/"
description: "usb_hcd_unlink_urb_from_ep – remove an URB from its endpoint queue"
---

<p>usb_hcd_unlink_urb_from_ep &#8211; remove an URB from its endpoint queue</p>
<h2>Synopsis</h2>
<pre><code>void usb_hcd_unlink_urb_from_ep(struct usb_hcd *hcd, struct urb *urb);</code></pre>
<h2>Arguments</h2>
<p><i>hcd</i></p>
<dl>
<dd>
<dd>host controller to which <i>urb</i> was submitted</dl>
<p> <i>urb</i></p>
<dl>
<dd>URB being unlinked</dl>
<h2>Description</h2>
<p>Host controller drivers should call this routine before calling <code>usb_hcd_giveback_urb</code>. The HCD&#8217;s private spinlock must be held and interrupts must be disabled. The actions carried out here are required for URB completion.</p>
<h2>Copyright</h2>
