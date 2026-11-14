---
title: "spi_execute_plan(3)"
name: "spi_execute_plan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_execute_plan/"
description: "SPI_execute_plan – execute a statement prepared by SPI_prepare"
---

<p>SPI_execute_plan &#8211; execute a statement prepared by <code>SPI_prepare</code> </p>
<h2>Synopsis</h2>
<pre>int SPI_execute_plan(SPIPlanPtr <i>plan</i>, Datum * <i>values</i>, const char * <i>nulls</i>,
 bool <i>read_only</i>, long <i>count</i>)</pre>
<h2>Description</h2>
<p><code>SPI_execute_plan</code> executes a statement prepared by <code>SPI_prepare</code> or one of its siblings. <i>read_only</i> and <i>count</i> have the same interpretation as in <code>SPI_execute</code>.</p>
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
<p> If <i>nulls</i> is NULL then <code>SPI_execute_plan</code> assumes that no parameters are null.</dl>
<p> bool <i>read_only</i></p>
<dl COMPACT>
<dd>true for read-only execution</dl>
<p> long <i>count</i></p>
<dl COMPACT>
<dd>maximum number of rows to return, or 0 for no limit</dl>
<h2>Return Value</h2>
<p>The return value is the same as for <code>SPI_execute</code>, with the following additional possible error (negative) results: </p>
<p> SPI_ERROR_ARGUMENT</p>
<dl COMPACT>
<dd>if <i>plan</i> is NULL or invalid, or <i>count</i> is less than 0</dl>
<p> SPI_ERROR_PARAM</p>
<dl COMPACT>
<dd>if <i>values</i> is NULL and <i>plan</i> was prepared with some parameters</dl>
<p> <i>SPI_processed</i> and <i>SPI_tuptable</i> are set as in <code>SPI_execute</code> if successful.</p>
