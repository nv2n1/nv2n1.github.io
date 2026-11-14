---
title: "spi_execp(3)"
name: "spi_execp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_execp/"
description: "SPI_execp – execute a statement in read/write mode"
---

<p>SPI_execp &#8211; execute a statement in read/write mode </p>
<h2>Synopsis</h2>
<pre>int SPI_execp(SPIPlanPtr <i>plan</i>, Datum * <i>values</i>, const char * <i>nulls</i>, long <i>count</i>)</pre>
<h2>Description</h2>
<p><code>SPI_execp</code> is the same as <code>SPI_execute_plan</code>, with the latter&#8217;s <i>read_only</i> parameter always taken as false.</p>
<h2>Arguments</h2>
<p>SPIPlanPtr <i>plan</i></p>
<dl COMPACT>
<dd>prepared statement (returned by <code>SPI_prepare</code>)</dl>
<p> Datum * <i>values</i></p>
<dl COMPACT>
<dd>An array of actual parameter values. Must have same length as the statement&#8217;s number of arguments.</dl>
<p> const char * <i>nulls</i></p>
<dl COMPACT>
<dd>An array describing which parameters are null. Must have same length as the statement&#8217;s number of arguments. n indicates a null value (entry in <i>values</i> will be ignored); a space indicates a nonnull value (entry in <i>values</i> is valid). </p>
<p> If <i>nulls</i> is NULL then <code>SPI_execp</code> assumes that no parameters are null.</dl>
<p> long <i>count</i></p>
<dl COMPACT>
<dd>maximum number of rows to return, or 0 for no limit</dl>
<h2>Return Value</h2>
<p>See <code>SPI_execute_plan</code>. </p>
<p> <i>SPI_processed</i> and <i>SPI_tuptable</i> are set as in <code>SPI_execute</code> if successful.</p>
