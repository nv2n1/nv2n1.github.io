---
title: "spi_cursor_open(3)"
name: "spi_cursor_open"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_cursor_open/"
description: "SPI_cursor_open – set up a cursor using a statement created with SPI_prepare"
---

<p>SPI_cursor_open &#8211; set up a cursor using a statement created with <code>SPI_prepare</code> </p>
<h2>Synopsis</h2>
<pre>Portal SPI_cursor_open(const char * <i>name</i>, SPIPlanPtr <i>plan</i>,
 Datum * <i>values</i>, const char * <i>nulls</i>,
 bool <i>read_only</i>)</pre>
<h2>Description</h2>
<p><code>SPI_cursor_open</code> sets up a cursor (internally, a portal) that will execute a statement prepared by <code>SPI_prepare</code>. The parameters have the same meanings as the corresponding parameters to <code>SPI_execute_plan</code>. </p>
<p> Using a cursor instead of executing the statement directly has two benefits. First, the result rows can be retrieved a few at a time, avoiding memory overrun for queries that return many rows. Second, a portal can outlive the current procedure (it can, in fact, live to the end of the current transaction). Returning the portal name to the procedure&#8217;s caller provides a way of returning a row set as result. </p>
<p> The passed-in parameter data will be copied into the cursor&#8217;s portal, so it can be freed while the cursor still exists.</p>
<h2>Arguments</h2>
<p>const char * <i>name</i></p>
<dl COMPACT>
<dd>name for portal, or NULL to let the system select a name</dl>
<p> SPIPlanPtr <i>plan</i></p>
<dl COMPACT>
<dd>prepared statement (returned by <code>SPI_prepare</code>)</dl>
<p> Datum * <i>values</i></p>
<dl COMPACT>
<dd>An array of actual parameter values. Must have same length as the statement&#8217;s number of arguments.</dl>
<p> const char * <i>nulls</i></p>
<dl COMPACT>
<dd>An array describing which parameters are null. Must have same length as the statement&#8217;s number of arguments. n indicates a null value (entry in <i>values</i> will be ignored); a space indicates a nonnull value (entry in <i>values</i> is valid). </p>
<p> If <i>nulls</i> is NULL then <code>SPI_cursor_open</code> assumes that no parameters are null.</dl>
<p> bool <i>read_only</i></p>
<dl COMPACT>
<dd>true for read-only execution</dl>
<h2>Return Value</h2>
<p>Pointer to portal containing the cursor. Note there is no error return convention; any error will be reported via <code>elog</code>.</p>
