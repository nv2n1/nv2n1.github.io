---
title: "spi_freeplan(3)"
name: "spi_freeplan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_freeplan/"
description: "SPI_freeplan – free a previously saved prepared statement"
---

<p>SPI_freeplan &#8211; free a previously saved prepared statement </p>
<h2>Synopsis</h2>
<pre>int SPI_freeplan(SPIPlanPtr <i>plan</i>)</pre>
<h2>Description</h2>
<p><code>SPI_freeplan</code> releases a prepared statement previously returned by <code>SPI_prepare</code> or saved by <code>SPI_keepplan</code> or <code>SPI_saveplan</code>.</p>
<h2>Arguments</h2>
<p>SPIPlanPtr <i>plan</i></p>
<dl COMPACT>
<dd>pointer to statement to free</dl>
<h2>Return Value</h2>
<p>0 on success; SPI_ERROR_ARGUMENT if <i>plan</i> is NULL or invalid</p>
