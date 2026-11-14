---
title: "spi_getargtypeid(3)"
name: "spi_getargtypeid"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_getargtypeid/"
description: "SPI_getargtypeid – return the data type OID for an argument of a statement prepared by SPI_prepare"
---

<p>SPI_getargtypeid &#8211; return the data type OID for an argument of a statement prepared by <code>SPI_prepare</code> </p>
<h2>Synopsis</h2>
<pre>Oid SPI_getargtypeid(SPIPlanPtr <i>plan</i>, int <i>argIndex</i>)</pre>
<h2>Description</h2>
<p><code>SPI_getargtypeid</code> returns the OID representing the type for the <i>argIndex</i>&#8216;th argument of a statement prepared by <code>SPI_prepare</code>. First argument is at index zero.</p>
<h2>Arguments</h2>
<p>SPIPlanPtr <i>plan</i></p>
<dl COMPACT>
<dd>prepared statement (returned by <code>SPI_prepare</code>)</dl>
<p> int <i>argIndex</i></p>
<dl COMPACT>
<dd>zero based index of the argument</dl>
<h2>Return Value</h2>
<p>The type OID of the argument at the given index. If the <i>plan</i> is NULL or invalid, or <i>argIndex</i> is less than 0 or not less than the number of arguments declared for the <i>plan</i>, <i>SPI_result</i> is set to SPI_ERROR_ARGUMENT and InvalidOid is returned.</p>
