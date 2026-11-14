---
title: "spi_saveplan(3)"
name: "spi_saveplan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_saveplan/"
description: "SPI_saveplan – save a prepared statement"
---

<p>SPI_saveplan &#8211; save a prepared statement </p>
<h2>Synopsis</h2>
<pre>SPIPlanPtr SPI_saveplan(SPIPlanPtr <i>plan</i>)</pre>
<h2>Description</h2>
<p><code>SPI_saveplan</code> copies a passed statement (prepared by <code>SPI_prepare</code>) into memory that will not be freed by <code>SPI_finish</code> nor by the transaction manager, and returns a pointer to the copied statement. This gives you the ability to reuse prepared statements in the subsequent invocations of your procedure in the current session.</p>
<h2>Arguments</h2>
<p>SPIPlanPtr <i>plan</i></p>
<dl COMPACT>
<dd>the prepared statement to be saved</dl>
<h2>Return Value</h2>
<p>Pointer to the copied statement; or NULL if unsuccessful. On error, <i>SPI_result</i> is set thus: </p>
<p> SPI_ERROR_ARGUMENT</p>
<dl COMPACT>
<dd>if <i>plan</i> is NULL or invalid</dl>
<p> SPI_ERROR_UNCONNECTED</p>
<dl COMPACT>
<dd>if called from an unconnected procedure</dl>
<h2>Notes</h2>
<p>The originally passed-in statement is not freed, so you might wish to do <code>SPI_freeplan</code> on it to avoid leaking memory until <code>SPI_finish</code>. </p>
<p> In most cases, <code>SPI_keepplan</code> is preferred to this function, since it accomplishes largely the same result without needing to physically copy the prepared statement&#8217;s data structures.</p>
