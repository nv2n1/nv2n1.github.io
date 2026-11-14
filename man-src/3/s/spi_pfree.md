---
title: "spi_pfree(3)"
name: "spi_pfree"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_pfree/"
description: "SPI_pfree – free memory in the upper executor context"
---

<p>SPI_pfree &#8211; free memory in the upper executor context </p>
<h2>Synopsis</h2>
<pre>void SPI_pfree(void * <i>pointer</i>)</pre>
<h2>Description</h2>
<p><code>SPI_pfree</code> frees memory previously allocated using <code>SPI_palloc</code> or <code>SPI_repalloc</code>. </p>
<p> This function is no longer different from plain <code>pfree</code>. It&#8217;s kept just for backward compatibility of existing code.</p>
<h2>Arguments</h2>
<p>void * <i>pointer</i></p>
<dl COMPACT>
<dd>pointer to existing storage to free</dl>
