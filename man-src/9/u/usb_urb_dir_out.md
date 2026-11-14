---
title: "usb_urb_dir_out(9)"
name: "usb_urb_dir_out"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_urb_dir_out/"
---

usb_urb_dir_out - check if an URB describes an OUT transfer

<h2>Synopsis</h2>

<pre><code>int usb_urb_dir_out(struct urb *urb);</code></pre>

<h2>Arguments</h2>

<i>urb</i>
<dl><dd><dd>URB to be checked</dl>

<h2>Return</h2>

1 if <i>urb</i> describes an OUT transfer (host-to-device), otherwise 0.

<h2>Copyright</h2>


