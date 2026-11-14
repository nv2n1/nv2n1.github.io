---
title: "spi_returntuple(3)"
name: "spi_returntuple"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_returntuple/"
description: "SPI_returntuple – prepare to return a tuple as a Datum"
---

<p>SPI_returntuple &#8211; prepare to return a tuple as a Datum </p>
<h2>Synopsis</h2>
<pre>HeapTupleHeader SPI_returntuple(HeapTuple <i>row</i>, TupleDesc <i>rowdesc</i>)</pre>
<h2>Description</h2>
<p><code>SPI_returntuple</code> makes a copy of a row in the upper executor context, returning it in the form of a row type Datum. The returned pointer need only be converted to Datum via <code>PointerGetDatum</code> before returning. </p>
<p> Note that this should be used for functions that are declared to return composite types. It is not used for triggers; use <code>SPI_copytuple</code> for returning a modified row in a trigger.</p>
<h2>Arguments</h2>
<p>HeapTuple <i>row</i></p>
<dl COMPACT>
<dd>row to be copied</dl>
<p> TupleDesc <i>rowdesc</i></p>
<dl COMPACT>
<dd>descriptor for row (pass the same descriptor each time for most effective caching)</dl>
<h2>Return Value</h2>
<p>HeapTupleHeader pointing to copied row; NULL only if <i>row</i> or <i>rowdesc</i> is NULL</p>
