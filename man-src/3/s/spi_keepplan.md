---
title: "spi_keepplan(3)"
name: "spi_keepplan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_keepplan/"
description: "SPI_keepplan – save a prepared statement"
---

<p>SPI_keepplan &#8211; save a prepared statement </p>
<h2>Synopsis</h2>
<pre>int SPI_keepplan(SPIPlanPtr <i>plan</i>)</pre>
<h2>Description</h2>
<p><code>SPI_keepplan</code> saves a passed statement (prepared by <code>SPI_prepare</code>) so that it will not be freed by <code>SPI_finish</code> nor by the transaction manager. This gives you the ability to reuse prepared statements in the subsequent invocations of your procedure in the current session.</p>
<h2>Arguments</h2>
<p>SPIPlanPtr <i>plan</i></p>
<dl COMPACT>
<dd>the prepared statement to be saved</dl>
<h2>Return Value</h2>
<p>0 on success; SPI_ERROR_ARGUMENT if <i>plan</i> is NULL or invalid</p>
<h2>Notes</h2>
<p>The passed-in statement is relocated to permanent storage by means of pointer adjustment (no data copying is required). If you later wish to delete it, use <code>SPI_freeplan</code> on it.</p>
