---
title: "usb_block_urb(9)"
name: "usb_block_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_block_urb/"
---

usb_block_urb - reliably prevent further use of an URB

<h2>Synopsis</h2>

<pre><code>void usb_block_urb(struct urb *urb);</code></pre>

<h2>Arguments</h2>

<i>urb</i>
<dl><dd><dd>pointer to URB to be blocked, may be NULL</dl>

<h2>Description</h2>

After the routine has run, attempts to resubmit the URB will fail with error -EPERM. Thus even if the URB's completion handler always tries to resubmit, it will not succeed and the URB will become idle. 

 The URB must not be deallocated while this routine is running. In particular, when a driver calls this routine, it must insure that the completion handler cannot deallocate the URB.

<h2>Copyright</h2>


