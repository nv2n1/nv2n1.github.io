---
title: "spi_execute_plan_with_paramlist(3)"
name: "spi_execute_plan_with_paramlist"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_execute_plan_with_paramlist/"
description: "SPI_execute_plan_with_paramlist – execute a statement prepared by SPI_prepare"
---

<p>SPI_execute_plan_with_paramlist &#8211; execute a statement prepared by <code>SPI_prepare</code> </p>
<h2>Synopsis</h2>
<pre>int SPI_execute_plan_with_paramlist(SPIPlanPtr <i>plan</i>,
 ParamListInfo <i>params</i>,
 bool <i>read_only</i>,
 long <i>count</i>)</pre>
<h2>Description</h2>
<p><code>SPI_execute_plan_with_paramlist</code> executes a statement prepared by <code>SPI_prepare</code>. This function is equivalent to <code>SPI_execute_plan</code> except that information about the parameter values to be passed to the query is presented differently. The ParamListInfo representation can be convenient for passing down values that are already available in that format. It also supports use of dynamic parameter sets via hook functions specified in ParamListInfo.</p>
<h2>Arguments</h2>
<p>SPIPlanPtr <i>plan</i></p>
<dl COMPACT>
<dd>prepared statement (returned by <code>SPI_prepare</code>)</dl>
<p> ParamListInfo <i>params</i></p>
<dl COMPACT>
<dd>data structure containing parameter types and values; NULL if none</dl>
<p> bool <i>read_only</i></p>
<dl COMPACT>
<dd>true for read-only execution</dl>
<p> long <i>count</i></p>
<dl COMPACT>
<dd>maximum number of rows to return, or 0 for no limit</dl>
<h2>Return Value</h2>
<p>The return value is the same as for <code>SPI_execute_plan</code>. </p>
<p> <i>SPI_processed</i> and <i>SPI_tuptable</i> are set as in <code>SPI_execute_plan</code> if successful.</p>
