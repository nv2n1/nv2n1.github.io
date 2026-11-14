---
title: "spi_cursor_open_with_args(3)"
name: "spi_cursor_open_with_args"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_cursor_open_with_args/"
description: "SPI_cursor_open_with_args – set up a cursor using a query and parameters"
---

<p>SPI_cursor_open_with_args &#8211; set up a cursor using a query and parameters </p>
<h2>Synopsis</h2>
<pre>Portal SPI_cursor_open_with_args(const char *<i>name</i>,
 const char *<i>command</i>,
 int <i>nargs</i>, Oid *<i>argtypes</i>,
 Datum *<i>values</i>, const char *<i>nulls</i>,
 bool <i>read_only</i>, int <i>cursorOptions</i>)</pre>
<h2>Description</h2>
<p><code>SPI_cursor_open_with_args</code> sets up a cursor (internally, a portal) that will execute the specified query. Most of the parameters have the same meanings as the corresponding parameters to <code>SPI_prepare_cursor</code> and <code>SPI_cursor_open</code>. </p>
<p> For one-time query execution, this function should be preferred over <code>SPI_prepare_cursor</code> followed by <code>SPI_cursor_open</code>. If the same command is to be executed with many different parameters, either method might be faster, depending on the cost of re-planning versus the benefit of custom plans. </p>
<p> The passed-in parameter data will be copied into the cursor&#8217;s portal, so it can be freed while the cursor still exists.</p>
<h2>Arguments</h2>
<p>const char * <i>name</i></p>
<dl COMPACT>
<dd>name for portal, or NULL to let the system select a name</dl>
<p> const char * <i>command</i></p>
<dl COMPACT>
<dd>command string</dl>
<p> int <i>nargs</i></p>
<dl COMPACT>
<dd>number of input parameters ($1, $2, etc.)</dl>
<p> Oid * <i>argtypes</i></p>
<dl COMPACT>
<dd>an array containing the OIDs of the data types of the parameters</dl>
<p> Datum * <i>values</i></p>
<dl COMPACT>
<dd>an array of actual parameter values</dl>
<p> const char * <i>nulls</i></p>
<dl COMPACT>
<dd>an array describing which parameters are null </p>
<p> If <i>nulls</i> is NULL then <code>SPI_cursor_open_with_args</code> assumes that no parameters are null.</dl>
<p> bool <i>read_only</i></p>
<dl COMPACT>
<dd>true for read-only execution</dl>
<p> int <i>cursorOptions</i></p>
<dl COMPACT>
<dd>integer bit mask of cursor options; zero produces default behavior</dl>
<h2>Return Value</h2>
<p>Pointer to portal containing the cursor. Note there is no error return convention; any error will be reported via <code>elog</code>.</p>
