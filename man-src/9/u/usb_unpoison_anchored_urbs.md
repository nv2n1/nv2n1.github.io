---
title: "usb_unpoison_anchored_urbs(9)"
name: "usb_unpoison_anchored_urbs"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_unpoison_anchored_urbs/"
---

usb_unpoison_anchored_urbs - let an anchor be used successfully again

<h2>Synopsis</h2>

<pre><code>void usb_unpoison_anchored_urbs(struct usb_anchor *anchor);</code></pre>

<h2>Arguments</h2>

<i>anchor</i>
<dl><dd><dd>anchor the requests are bound to</dl>

<h2>Description</h2>

Reverses the effect of usb_poison_anchored_urbs the anchor can be used normally after it returns

<h2>Copyright</h2>


