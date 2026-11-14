---
title: "spi_execute_with_args(3)"
name: "spi_execute_with_args"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_execute_with_args/"
description: "SPI_execute_with_args – execute a command with out-of-line parameters"
---

<p>SPI_execute_with_args &#8211; execute a command with out-of-line parameters </p>
<h2>Synopsis</h2>
<pre>int SPI_execute_with_args(const char *<i>command</i>,
 int <i>nargs</i>, Oid *<i>argtypes</i>,
 Datum *<i>values</i>, const char *<i>nulls</i>,
 bool <i>read_only</i>, long <i>count</i>)</pre>
<h2>Description</h2>
<p><code>SPI_execute_with_args</code> executes a command that might include references to externally supplied parameters. The command text refers to a parameter as $<i>n</i>, and the call specifies data types and values for each such symbol. <i>read_only</i> and <i>count</i> have the same interpretation as in <code>SPI_execute</code>. </p>
<p> The main advantage of this routine compared to <code>SPI_execute</code> is that data values can be inserted into the command without tedious quoting/escaping, and thus with much less risk of SQL-injection attacks. </p>
<p> Similar results can be achieved with <code>SPI_prepare</code> followed by <code>SPI_execute_plan</code>; however, when using this function the query plan is always customized to the specific parameter values provided. For one-time query execution, this function should be preferred. If the same command is to be executed with many different parameters, either method might be faster, depending on the cost of re-planning versus the benefit of custom plans.</p>
<h2>Arguments</h2>
<p>const char * <i>command</i></p>
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
<p> If <i>nulls</i> is NULL then <code>SPI_execute_with_args</code> assumes that no parameters are null.</dl>
<p> bool <i>read_only</i></p>
<dl COMPACT>
<dd>true for read-only execution</dl>
<p> long <i>count</i></p>
<dl COMPACT>
<dd>maximum number of rows to return, or 0 for no limit</dl>
<h2>Return Value</h2>
<p>The return value is the same as for <code>SPI_execute</code>. </p>
<p> <i>SPI_processed</i> and <i>SPI_tuptable</i> are set as in <code>SPI_execute</code> if successful.</p>
