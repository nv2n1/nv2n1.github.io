---
title: "spi_cursor_open_with_paramlist(3)"
name: "spi_cursor_open_with_paramlist"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_cursor_open_with_paramlist/"
description: "SPI_cursor_open_with_paramlist – set up a cursor using parameters"
---

<p>SPI_cursor_open_with_paramlist &#8211; set up a cursor using parameters </p>
<h2>Synopsis</h2>
<pre>Portal SPI_cursor_open_with_paramlist(const char *<i>name</i>,
 SPIPlanPtr <i>plan</i>,
 ParamListInfo <i>params</i>,
 bool <i>read_only</i>)</pre>
<h2>Description</h2>
<p><code>SPI_cursor_open_with_paramlist</code> sets up a cursor (internally, a portal) that will execute a statement prepared by <code>SPI_prepare</code>. This function is equivalent to <code>SPI_cursor_open</code> except that information about the parameter values to be passed to the query is presented differently. The ParamListInfo representation can be convenient for passing down values that are already available in that format. It also supports use of dynamic parameter sets via hook functions specified in ParamListInfo. </p>
<p> The passed-in parameter data will be copied into the cursor&#8217;s portal, so it can be freed while the cursor still exists.</p>
<h2>Arguments</h2>
<p>const char * <i>name</i></p>
<dl COMPACT>
<dd>name for portal, or NULL to let the system select a name</dl>
<p> SPIPlanPtr <i>plan</i></p>
<dl COMPACT>
<dd>prepared statement (returned by <code>SPI_prepare</code>)</dl>
<p> ParamListInfo <i>params</i></p>
<dl COMPACT>
<dd>data structure containing parameter types and values; NULL if none</dl>
<p> bool <i>read_only</i></p>
<dl COMPACT>
<dd>true for read-only execution</dl>
<h2>Return Value</h2>
<p>Pointer to portal containing the cursor. Note there is no error return convention; any error will be reported via <code>elog</code>.</p>
