---
title: "spi_getvalue(3)"
name: "spi_getvalue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_getvalue/"
description: "SPI_getvalue – return the string value of the specified column"
---

<p>SPI_getvalue &#8211; return the string value of the specified column </p>
<h2>Synopsis</h2>
<pre>char * SPI_getvalue(HeapTuple <i>row</i>, TupleDesc <i>rowdesc</i>, int <i>colnumber</i>)</pre>
<h2>Description</h2>
<p><code>SPI_getvalue</code> returns the string representation of the value of the specified column. </p>
<p> The result is returned in memory allocated using <code>palloc</code>. (You can use <code>pfree</code> to release the memory when you don&#8217;t need it anymore.)</p>
<h2>Arguments</h2>
<p>HeapTuple <i>row</i></p>
<dl COMPACT>
<dd>input row to be examined</dl>
<p> TupleDesc <i>rowdesc</i></p>
<dl COMPACT>
<dd>input row description</dl>
<p> int <i>colnumber</i></p>
<dl COMPACT>
<dd>column number (count starts at 1)</dl>
<h2>Return Value</h2>
<p>Column value, or NULL if the column is null, <i>colnumber</i> is out of range (<i>SPI_result</i> is set to SPI_ERROR_NOATTRIBUTE), or no output function is available (<i>SPI_result</i> is set to SPI_ERROR_NOOUTFUNC).</p>
