---
title: "spi_repalloc(3)"
name: "spi_repalloc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_repalloc/"
description: "SPI_repalloc – reallocate memory in the upper executor context"
---

<p>SPI_repalloc &#8211; reallocate memory in the upper executor context </p>
<h2>Synopsis</h2>
<pre>void * SPI_repalloc(void * <i>pointer</i>, Size <i>size</i>)</pre>
<h2>Description</h2>
<p><code>SPI_repalloc</code> changes the size of a memory segment previously allocated using <code>SPI_palloc</code>. </p>
<p> This function is no longer different from plain <code>repalloc</code>. It&#8217;s kept just for backward compatibility of existing code.</p>
<h2>Arguments</h2>
<p>void * <i>pointer</i></p>
<dl COMPACT>
<dd>pointer to existing storage to change</dl>
<p> Size <i>size</i></p>
<dl COMPACT>
<dd>size in bytes of storage to allocate</dl>
<h2>Return Value</h2>
<p>pointer to new storage space of specified size with the contents copied from the existing area</p>
