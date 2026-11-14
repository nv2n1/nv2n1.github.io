---
title: "spi_freetuptable(3)"
name: "spi_freetuptable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_freetuptable/"
description: "SPI_freetuptable – free a row set created by SPI_execute or a similar function"
---

<p>SPI_freetuptable &#8211; free a row set created by <code>SPI_execute</code> or a similar function </p>
<h2>Synopsis</h2>
<pre>void SPI_freetuptable(SPITupleTable * <i>tuptable</i>)</pre>
<h2>Description</h2>
<p><code>SPI_freetuptable</code> frees a row set created by a prior SPI command execution function, such as <code>SPI_execute</code>. Therefore, this function is usually called with the global variable <i>SPI_tupletable</i> as argument. </p>
<p> This function is useful if a SPI procedure needs to execute multiple commands and does not want to keep the results of earlier commands around until it ends. Note that any unfreed row sets will be freed anyway at <code>SPI_finish</code>.</p>
<h2>Arguments</h2>
<p>SPITupleTable * <i>tuptable</i></p>
<dl COMPACT>
<dd>pointer to row set to free</dl>
