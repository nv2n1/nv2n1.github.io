---
title: "usb_alloc_coherent(9)"
name: "usb_alloc_coherent"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_alloc_coherent/"
description: "usb_alloc_coherent – allocate dma-consistent buffer for URB_NO_xxx_DMA_MAP"
---

<p>usb_alloc_coherent &#8211; allocate dma-consistent buffer for URB_NO_xxx_DMA_MAP</p>
<h2>Synopsis</h2>
<pre><code>void *usb_alloc_coherent(struct usb_device *dev, size_t size, gfp_t mem_flags, dma_addr_t *dma);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device the buffer will be used with</dl>
<p> <i>size</i></p>
<dl>
<dd>requested buffer size</dl>
<p> <i>mem_flags</i></p>
<dl>
<dd>affect whether allocation may block</dl>
<p> <i>dma</i></p>
<dl>
<dd>used to return DMA address of buffer</dl>
<h2>Return</h2>
<p>Either null (indicating no buffer could be allocated), or the cpu-space pointer to a buffer that may be used to perform DMA to the specified device. Such cpu-space buffers are returned along with the DMA address (through the pointer provided).</p>
<h2>Note</h2>
<p>These buffers are used with URB_NO_xxx_DMA_MAP set in urb-&gt;transfer_flags to avoid behaviors like using &#8220;DMA bounce buffers&#8221;, or thrashing IOMMU hardware during URB completion/resubmit. The implementation varies between platforms, depending on details of how DMA will work to this device. Using these buffers also eliminates cacheline sharing problems on architectures where CPU caches are not DMA-coherent. On systems without bus-snooping caches, these buffers are uncached. </p>
<p> When the buffer is no longer used, free it with <code>usb_free_coherent</code>.</p>
<h2>Copyright</h2>
