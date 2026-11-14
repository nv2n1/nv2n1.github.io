---
title: "spi_fnumber(3)"
name: "spi_fnumber"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_fnumber/"
description: "SPI_fnumber – determine the column number for the specified column name"
---

<p>SPI_fnumber &#8211; determine the column number for the specified column name </p>
<h2>Synopsis</h2>
<pre>int SPI_fnumber(TupleDesc <i>rowdesc</i>, const char * <i>colname</i>)</pre>
<h2>Description</h2>
<p><code>SPI_fnumber</code> returns the column number for the column with the specified name. </p>
<p> If <i>colname</i> refers to a system column (e.g., oid) then the appropriate negative column number will be returned. The caller should be careful to test the return value for exact equality to SPI_ERROR_NOATTRIBUTE to detect an error; testing the result for less than or equal to 0 is not correct unless system columns should be rejected.</p>
<h2>Arguments</h2>
<p>TupleDesc <i>rowdesc</i></p>
<dl COMPACT>
<dd>input row description</dl>
<p> const char * <i>colname</i></p>
<dl COMPACT>
<dd>column name</dl>
<h2>Return Value</h2>
<p>Column number (count starts at 1), or SPI_ERROR_NOATTRIBUTE if the named column was not found.</p>
