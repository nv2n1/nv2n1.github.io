---
title: "usb_unanchor_urb(9)"
name: "usb_unanchor_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_unanchor_urb/"
---

usb_unanchor_urb - unanchors an URB

<h2>Synopsis</h2>

<pre><code>void usb_unanchor_urb(struct urb *urb);</code></pre>

<h2>Arguments</h2>

<i>urb</i>
<dl><dd><dd>pointer to the urb to anchor</dl>

<h2>Description</h2>

Call this to stop the system keeping track of this URB

<h2>Copyright</h2>


