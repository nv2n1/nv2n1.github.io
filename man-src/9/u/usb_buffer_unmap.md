---
title: "usb_buffer_unmap(9)"
name: "usb_buffer_unmap"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_buffer_unmap/"
description: "usb_buffer_unmap – free DMA mapping(s) for an urb"
---

<p>usb_buffer_unmap &#8211; free DMA mapping(s) for an urb</p>
<h2>Synopsis</h2>
<pre><code>void usb_buffer_unmap(struct urb *urb);</code></pre>
<h2>Arguments</h2>
<p><i>urb</i></p>
<dl>
<dd>
<dd>urb whose transfer_buffer will be unmapped</dl>
<h2>Description</h2>
<p>Reverses the effect of <code>usb_buffer_map</code>.</p>
<h2>Copyright</h2>
