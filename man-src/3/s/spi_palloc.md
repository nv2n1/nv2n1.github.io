---
title: "spi_palloc(3)"
name: "spi_palloc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_palloc/"
description: "SPI_palloc – allocate memory in the upper executor context"
---

<p>SPI_palloc &#8211; allocate memory in the upper executor context </p>
<h2>Synopsis</h2>
<pre>void * SPI_palloc(Size <i>size</i>)</pre>
<h2>Description</h2>
<p><code>SPI_palloc</code> allocates memory in the upper executor context.</p>
<h2>Arguments</h2>
<p>Size <i>size</i></p>
<dl COMPACT>
<dd>size in bytes of storage to allocate</dl>
<h2>Return Value</h2>
<p>pointer to new storage space of the specified size</p>
