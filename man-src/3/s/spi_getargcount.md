---
title: "spi_getargcount(3)"
name: "spi_getargcount"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_getargcount/"
description: "SPI_getargcount – return the number of arguments needed by a statement prepared by SPI_prepare"
---

<p>SPI_getargcount &#8211; return the number of arguments needed by a statement prepared by <code>SPI_prepare</code> </p>
<h2>Synopsis</h2>
<pre>int SPI_getargcount(SPIPlanPtr <i>plan</i>)</pre>
<h2>Description</h2>
<p><code>SPI_getargcount</code> returns the number of arguments needed to execute a statement prepared by <code>SPI_prepare</code>.</p>
<h2>Arguments</h2>
<p>SPIPlanPtr <i>plan</i></p>
<dl COMPACT>
<dd>prepared statement (returned by <code>SPI_prepare</code>)</dl>
<h2>Return Value</h2>
<p>The count of expected arguments for the <i>plan</i>. If the <i>plan</i> is NULL or invalid, <i>SPI_result</i> is set to SPI_ERROR_ARGUMENT and -1 is returned.</p>
