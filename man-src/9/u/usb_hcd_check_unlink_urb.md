---
title: "usb_hcd_check_unlink_urb(9)"
name: "usb_hcd_check_unlink_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_hcd_check_unlink_urb/"
description: "usb_hcd_check_unlink_urb – check whether an URB may be unlinked"
---

<p>usb_hcd_check_unlink_urb &#8211; check whether an URB may be unlinked</p>
<h2>Synopsis</h2>
<pre><code>int usb_hcd_check_unlink_urb(struct usb_hcd *hcd, struct urb *urb, int status);</code></pre>
<h2>Arguments</h2>
<p><i>hcd</i></p>
<dl>
<dd>
<dd>host controller to which <i>urb</i> was submitted</dl>
<p> <i>urb</i></p>
<dl>
<dd>URB being checked for unlinkability</dl>
<p> <i>status</i></p>
<dl>
<dd>error code to store in <i>urb</i> if the unlink succeeds</dl>
<h2>Description</h2>
<p>Host controller drivers should call this routine in their <code>dequeue</code> method. The HCD&#8217;s private spinlock must be held and interrupts must be disabled. The actions carried out here are required for making sure than an unlink is valid.</p>
<h2>Return</h2>
<p>0 for no error, otherwise a negative error code (in which case the <code>dequeue</code> method must fail). The possible error codes are: </p>
<p> -EIDRM: <i>urb</i> was not submitted or has already completed. The completion function may not have been called yet. </p>
<p> -EBUSY: <i>urb</i> has already been unlinked.</p>
<h2>Copyright</h2>
