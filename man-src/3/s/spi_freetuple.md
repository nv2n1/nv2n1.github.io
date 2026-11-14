---
title: "spi_freetuple(3)"
name: "spi_freetuple"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_freetuple/"
description: "SPI_freetuple – free a row allocated in the upper executor context"
---

<p>SPI_freetuple &#8211; free a row allocated in the upper executor context </p>
<h2>Synopsis</h2>
<pre>void SPI_freetuple(HeapTuple <i>row</i>)</pre>
<h2>Description</h2>
<p><code>SPI_freetuple</code> frees a row previously allocated in the upper executor context. </p>
<p> This function is no longer different from plain <code>heap_freetuple</code>. It&#8217;s kept just for backward compatibility of existing code.</p>
<h2>Arguments</h2>
<p>HeapTuple <i>row</i></p>
<dl COMPACT>
<dd>row to free</dl>
