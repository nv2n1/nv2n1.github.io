---
title: "usb_free_coherent(9)"
name: "usb_free_coherent"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_free_coherent/"
description: "usb_free_coherent – free memory allocated with usb_alloc_coherent"
---

<p>usb_free_coherent &#8211; free memory allocated with <code>usb_alloc_coherent</code></p>
<h2>Synopsis</h2>
<pre><code>void usb_free_coherent(struct usb_device *dev, size_t size, void *addr, dma_addr_t dma);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device the buffer was used with</dl>
<p> <i>size</i></p>
<dl>
<dd>requested buffer size</dl>
<p> <i>addr</i></p>
<dl>
<dd>CPU address of buffer</dl>
<p> <i>dma</i></p>
<dl>
<dd>DMA address of buffer</dl>
<h2>Description</h2>
<p>This reclaims an I/O buffer, letting it be reused. The memory must have been allocated using <code>usb_alloc_coherent</code>, and the parameters must match those provided in that allocation request.</p>
<h2>Copyright</h2>
