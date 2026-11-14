---
title: "spi_getbinval(3)"
name: "spi_getbinval"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_getbinval/"
description: "SPI_getbinval – return the binary value of the specified column"
---

<p>SPI_getbinval &#8211; return the binary value of the specified column </p>
<h2>Synopsis</h2>
<pre>Datum SPI_getbinval(HeapTuple <i>row</i>, TupleDesc <i>rowdesc</i>, int <i>colnumber</i>,
 bool * <i>isnull</i>)</pre>
<h2>Description</h2>
<p><code>SPI_getbinval</code> returns the value of the specified column in the internal form (as type Datum). </p>
<p> This function does not allocate new space for the datum. In the case of a pass-by-reference data type, the return value will be a pointer into the passed row.</p>
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
<p> bool * <i>isnull</i></p>
<dl COMPACT>
<dd>flag for a null value in the column</dl>
<h2>Return Value</h2>
<p>The binary value of the column is returned. The variable pointed to by <i>isnull</i> is set to true if the column is null, else to false. </p>
<p> <i>SPI_result</i> is set to SPI_ERROR_NOATTRIBUTE on error.</p>
