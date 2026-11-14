---
title: "usb_anchor_urb(9)"
name: "usb_anchor_urb"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_anchor_urb/"
---

usb_anchor_urb - anchors an URB while it is processed

<h2>Synopsis</h2>

<pre><code>void usb_anchor_urb(struct urb *urb, struct usb_anchor *anchor);</code></pre>

<h2>Arguments</h2>

<i>urb</i>
<dl><dd><dd>pointer to the urb to anchor</dl>
 

 <i>anchor</i>
<dl><dd>pointer to the anchor</dl>

<h2>Description</h2>

This can be called to have access to URBs which are to be executed without bothering to track them

<h2>Copyright</h2>


