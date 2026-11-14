---
title: "usb_buffer_unmap_sg(9)"
name: "usb_buffer_unmap_sg"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_buffer_unmap_sg/"
description: "usb_buffer_unmap_sg – free DMA mapping(s) for a scatterlist"
---

<p>usb_buffer_unmap_sg &#8211; free DMA mapping(s) for a scatterlist</p>
<h2>Synopsis</h2>
<pre><code>void usb_buffer_unmap_sg(const struct usb_device *dev, int is_in, struct scatterlist *sg, int n_hw_ents);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device to which the scatterlist will be mapped</dl>
<p> <i>is_in</i></p>
<dl>
<dd>mapping transfer direction</dl>
<p> <i>sg</i></p>
<dl>
<dd>the scatterlist to unmap</dl>
<p> <i>n_hw_ents</i></p>
<dl>
<dd>the positive return value from usb_buffer_map_sg</dl>
<h2>Description</h2>
<p>Reverses the effect of <code>usb_buffer_map_sg</code>.</p>
<h2>Copyright</h2>
