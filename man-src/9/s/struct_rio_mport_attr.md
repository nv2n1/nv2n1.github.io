---
title: "struct_rio_mport_attr(9)"
name: "struct_rio_mport_attr"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rio_mport_attr/"
description: "struct_rio_mport_attr – RIO mport device attributes"
---

<p>struct_rio_mport_attr &#8211; RIO mport device attributes</p>
<h2>Synopsis</h2>
<pre><code>struct rio_mport_attr {
    int flags;
    int link_speed;
    int link_width;
    int dma_max_sge;
    int dma_max_size;
    int dma_align;
};</code></pre>
<h2>Members</h2>
<p>flags</p>
<dl>
<dd>mport device capability flags</dl>
<p> link_speed</p>
<dl>
<dd>SRIO link speed value (as defined by RapidIO specification)</dl>
<p> link_width</p>
<dl>
<dd>SRIO link width value (as defined by RapidIO specification)</dl>
<p> dma_max_sge</p>
<dl>
<dd>number of SG list entries that can be handled by DMA channel(s)</dl>
<p> dma_max_size</p>
<dl>
<dd>max number of bytes in single DMA transfer (SG entry)</dl>
<p> dma_align</p>
<dl>
<dd>alignment shift for DMA operations (as for other DMA operations)</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
