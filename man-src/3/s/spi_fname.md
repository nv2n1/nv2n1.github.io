---
title: "spi_fname(3)"
name: "spi_fname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_fname/"
description: "SPI_fname – determine the column name for the specified column number"
---

<p>SPI_fname &#8211; determine the column name for the specified column number </p>
<h2>Synopsis</h2>
<pre>char * SPI_fname(TupleDesc <i>rowdesc</i>, int <i>colnumber</i>)</pre>
<h2>Description</h2>
<p><code>SPI_fname</code> returns a copy of the column name of the specified column. (You can use <code>pfree</code> to release the copy of the name when you don&#8217;t need it anymore.)</p>
<h2>Arguments</h2>
<p>TupleDesc <i>rowdesc</i></p>
<dl COMPACT>
<dd>input row description</dl>
<p> int <i>colnumber</i></p>
<dl COMPACT>
<dd>column number (count starts at 1)</dl>
<h2>Return Value</h2>
<p>The column name; NULL if <i>colnumber</i> is out of range. <i>SPI_result</i> set to SPI_ERROR_NOATTRIBUTE on error.</p>
