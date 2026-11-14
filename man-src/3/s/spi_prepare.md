---
title: "spi_prepare(3)"
name: "spi_prepare"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_prepare/"
description: "SPI_prepare – prepare a statement, without executing it yet"
---

<p>SPI_prepare &#8211; prepare a statement, without executing it yet </p>
<h2>Synopsis</h2>
<pre>SPIPlanPtr SPI_prepare(const char * <i>command</i>, int <i>nargs</i>, Oid * <i>argtypes</i>)</pre>
<h2>Description</h2>
<p><code>SPI_prepare</code> creates and returns a prepared statement for the specified command, but doesn&#8217;t execute the command. The prepared statement can later be executed repeatedly using <code>SPI_execute_plan</code>. </p>
<p> When the same or a similar command is to be executed repeatedly, it is generally advantageous to perform parse analysis only once, and might furthermore be advantageous to re-use an execution plan for the command. <code>SPI_prepare</code> converts a command string into a prepared statement that encapsulates the results of parse analysis. The prepared statement also provides a place for caching an execution plan if it is found that generating a custom plan for each execution is not helpful. </p>
<p> A prepared command can be generalized by writing parameters ($1, $2, etc.) in place of what would be constants in a normal command. The actual values of the parameters are then specified when <code>SPI_execute_plan</code> is called. This allows the prepared command to be used over a wider range of situations than would be possible without parameters. </p>
<p> The statement returned by <code>SPI_prepare</code> can be used only in the current invocation of the procedure, since <code>SPI_finish</code> frees memory allocated for such a statement. But the statement can be saved for longer using the functions <code>SPI_keepplan</code> or <code>SPI_saveplan</code>.</p>
<h2>Arguments</h2>
<p>const char * <i>command</i></p>
<dl COMPACT>
<dd>command string</dl>
<p> int <i>nargs</i></p>
<dl COMPACT>
<dd>number of input parameters ($1, $2, etc.)</dl>
<p> Oid * <i>argtypes</i></p>
<dl COMPACT>
<dd>pointer to an array containing the OIDs of the data types of the parameters</dl>
<h2>Return Value</h2>
<p><code>SPI_prepare</code> returns a non-null pointer to an SPIPlan, which is an opaque struct representing a prepared statement. On error, NULL will be returned, and <i>SPI_result</i> will be set to one of the same error codes used by <code>SPI_execute</code>, except that it is set to SPI_ERROR_ARGUMENT if <i>command</i> is NULL, or if <i>nargs</i> is less than 0, or if <i>nargs</i> is greater than 0 and <i>argtypes</i> is NULL.</p>
<h2>Notes</h2>
<p>If no parameters are defined, a generic plan will be created at the first use of <code>SPI_execute_plan</code>, and used for all subsequent executions as well. If there are parameters, the first few uses of <code>SPI_execute_plan</code> will generate custom plans that are specific to the supplied parameter values. After enough uses of the same prepared statement, <code>SPI_execute_plan</code> will build a generic plan, and if that is not too much more expensive than the custom plans, it will start using the generic plan instead of re-planning each time. If this default behavior is unsuitable, you can alter it by passing the CURSOR_OPT_GENERIC_PLAN or CURSOR_OPT_CUSTOM_PLAN flag to <code>SPI_prepare_cursor</code>, to force use of generic or custom plans respectively. </p>
<p> This function should only be called from a connected procedure. </p>
<p> SPIPlanPtr is declared as a pointer to an opaque struct type in spi.h. It is unwise to try to access its contents directly, as that makes your code much more likely to break in future revisions of PostgreSQL. </p>
<p> The name SPIPlanPtr is somewhat historical, since the data structure no longer necessarily contains an execution plan.</p>
