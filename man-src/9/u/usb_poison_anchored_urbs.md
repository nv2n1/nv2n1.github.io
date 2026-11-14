---
title: "usb_poison_anchored_urbs(9)"
name: "usb_poison_anchored_urbs"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_poison_anchored_urbs/"
---

usb_poison_anchored_urbs - cease all traffic from an anchor

<h2>Synopsis</h2>

<pre><code>void usb_poison_anchored_urbs(struct usb_anchor *anchor);</code></pre>

<h2>Arguments</h2>

<i>anchor</i>
<dl><dd><dd>anchor the requests are bound to</dl>

<h2>Description</h2>

this allows all outstanding URBs to be poisoned starting from the back of the queue. Newly added URBs will also be poisoned 

 This routine should not be called by a driver after its disconnect method has returned.

<h2>Copyright</h2>


