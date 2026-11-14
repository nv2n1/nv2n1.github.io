---
title: "spi_gettypeid(3)"
name: "spi_gettypeid"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_gettypeid/"
description: "SPI_gettypeid – return the data type OID of the specified column"
---

<p>SPI_gettypeid &#8211; return the data type OID of the specified column </p>
<h2>Synopsis</h2>
<pre>Oid SPI_gettypeid(TupleDesc <i>rowdesc</i>, int <i>colnumber</i>)</pre>
<h2>Description</h2>
<p><code>SPI_gettypeid</code> returns the OID of the data type of the specified column.</p>
<h2>Arguments</h2>
<p>TupleDesc <i>rowdesc</i></p>
<dl COMPACT>
<dd>input row description</dl>
<p> int <i>colnumber</i></p>
<dl COMPACT>
<dd>column number (count starts at 1)</dl>
<h2>Return Value</h2>
<p>The OID of the data type of the specified column or InvalidOid on error. On error, <i>SPI_result</i> is set to SPI_ERROR_NOATTRIBUTE.</p>
