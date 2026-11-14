---
title: "usb_buffer_dmasync_sg(9)"
name: "usb_buffer_dmasync_sg"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_buffer_dmasync_sg/"
---

usb_buffer_dmasync_sg - synchronize DMA and CPU view of scatterlist buffer(s)

<h2>Synopsis</h2>

<pre><code>void usb_buffer_dmasync_sg(const struct usb_device *dev, int is_in, struct scatterlist *sg, int n_hw_ents);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device to which the scatterlist will be mapped</dl>
 

 <i>is_in</i>
<dl><dd>mapping transfer direction</dl>
 

 <i>sg</i>
<dl><dd>the scatterlist to synchronize</dl>
 

 <i>n_hw_ents</i>
<dl><dd>the positive return value from usb_buffer_map_sg</dl>

<h2>Description</h2>

Use this when you are re-using a scatterlist's data buffers for another USB request.

<h2>Copyright</h2>


