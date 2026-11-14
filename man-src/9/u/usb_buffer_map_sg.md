---
title: "usb_buffer_map_sg(9)"
name: "usb_buffer_map_sg"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_buffer_map_sg/"
description: "usb_buffer_map_sg – create scatterlist DMA mapping(s) for an endpoint"
---

<p>usb_buffer_map_sg &#8211; create scatterlist DMA mapping(s) for an endpoint</p>
<h2>Synopsis</h2>
<pre><code>int usb_buffer_map_sg(const struct usb_device *dev, int is_in, struct scatterlist *sg, int nents);</code></pre>
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
<dd>the scatterlist to map</dl>
<p> <i>nents</i></p>
<dl>
<dd>the number of entries in the scatterlist</dl>
<h2>Return</h2>
<p>Either &lt; 0 (indicating no buffers could be mapped), or the number of DMA mapping array entries in the scatterlist.</p>
<h2>Note</h2>
<p>The caller is responsible for placing the resulting DMA addresses from the scatterlist into URB transfer buffer pointers, and for setting the URB_NO_TRANSFER_DMA_MAP transfer flag in each of those URBs. </p>
<p> Top I/O rates come from queuing URBs, instead of waiting for each one to complete before starting the next I/O. This is particularly easy to do with scatterlists. Just allocate and submit one URB for each DMA mapping entry returned, stopping on the first error or when all succeed. Better yet, use the usb_sg_*() calls, which do that (and more) for you. </p>
<p> This call would normally be used when translating scatterlist requests, rather than <code>usb_buffer_map</code>, since on some hardware (with IOMMUs) it may be able to coalesce mappings for improved I/O efficiency. </p>
<p> Reverse the effect of this call with <code>usb_buffer_unmap_sg</code>.</p>
<h2>Copyright</h2>
