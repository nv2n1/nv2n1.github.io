---
title: "spi_copytuple(3)"
name: "spi_copytuple"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_copytuple/"
description: "SPI_copytuple – make a copy of a row in the upper executor context"
---

<p>SPI_copytuple &#8211; make a copy of a row in the upper executor context </p>
<h2>Synopsis</h2>
<pre>HeapTuple SPI_copytuple(HeapTuple <i>row</i>)</pre>
<h2>Description</h2>
<p><code>SPI_copytuple</code> makes a copy of a row in the upper executor context. This is normally used to return a modified row from a trigger. In a function declared to return a composite type, use <code>SPI_returntuple</code> instead.</p>
<h2>Arguments</h2>
<p>HeapTuple <i>row</i></p>
<dl COMPACT>
<dd>row to be copied</dl>
<h2>Return Value</h2>
<p>the copied row; NULL only if <i>tuple</i> is NULL</p>
