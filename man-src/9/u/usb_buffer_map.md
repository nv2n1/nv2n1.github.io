---
title: "usb_buffer_map(9)"
name: "usb_buffer_map"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_buffer_map/"
description: "usb_buffer_map – create DMA mapping(s) for an urb"
---

<p>usb_buffer_map &#8211; create DMA mapping(s) for an urb</p>
<h2>Synopsis</h2>
<pre><code>struct urb *usb_buffer_map(struct urb *urb);</code></pre>
<h2>Arguments</h2>
<p><i>urb</i></p>
<dl>
<dd>
<dd>urb whose transfer_buffer/setup_packet will be mapped</dl>
<h2>Description</h2>
<p>URB_NO_TRANSFER_DMA_MAP is added to urb-&gt;transfer_flags if the operation succeeds. If the device is connected to this system through a non-DMA controller, this operation always succeeds. </p>
<p> This call would normally be used for an urb which is reused, perhaps as the target of a large periodic transfer, with <code>usb_buffer_dmasync</code> calls to synchronize memory and dma state. </p>
<p> Reverse the effect of this call with <code>usb_buffer_unmap</code>.</p>
<h2>Return</h2>
<p>Either <code>NULL</code> (indicating no buffer could be mapped), or <i>urb</i>.</p>
<h2>Copyright</h2>
