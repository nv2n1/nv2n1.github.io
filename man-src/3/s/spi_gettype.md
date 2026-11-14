---
title: "spi_gettype(3)"
name: "spi_gettype"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_gettype/"
description: "SPI_gettype – return the data type name of the specified column"
---

<p>SPI_gettype &#8211; return the data type name of the specified column </p>
<h2>Synopsis</h2>
<pre>char * SPI_gettype(TupleDesc <i>rowdesc</i>, int <i>colnumber</i>)</pre>
<h2>Description</h2>
<p><code>SPI_gettype</code> returns a copy of the data type name of the specified column. (You can use <code>pfree</code> to release the copy of the name when you don&#8217;t need it anymore.)</p>
<h2>Arguments</h2>
<p>TupleDesc <i>rowdesc</i></p>
<dl COMPACT>
<dd>input row description</dl>
<p> int <i>colnumber</i></p>
<dl COMPACT>
<dd>column number (count starts at 1)</dl>
<h2>Return Value</h2>
<p>The data type name of the specified column, or NULL on error. <i>SPI_result</i> is set to SPI_ERROR_NOATTRIBUTE on error.</p>
