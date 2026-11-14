---
title: "bsqldb(1)"
name: "bsqldb"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bsqldb/"
description: "bsqldb – batch SQL script processor using DB-Library"
---

<h2 class="name">NAME</h2>
<p> <code>bsqldb</code> &#8211; batch SQL script processor using DB-Library </p>
<h2>SYNOPSIS</h2>
<p> [-<code>hqv</code> ] [-<code>S </code><i>servername</i> ] [-<code>D </code><i>database</i> ] [-<code>U </code><i>username</i> ] [-<code>P </code><i>password</i> ] [-<code>i </code><i>input_file</i> ] [-<code>o </code><i>output_file</i> ] [-<code>e </code><i>error_file</i> ] [-<code>H </code><i>hostname</i> ] [-<code>t </code><i>field_term</i> ] [-<code>R </code><i>pivot_description</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is a utility program distributed with FreeTDS. is a non-interactive equivalent of the &quot;isql&quot; utility programs distributed by Sybase and Microsoft. Like them, uses the command &quot;go&quot; on a line by itself as a separator between batches. The last batch need not be followed by &quot;go&quot;. makes use of the DB-Library API provided by FreeTDS. This API is of course also available to application developers. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-D </code><i>database</i></p>
<dd> Database to use.</p>
<dt><code>-H </code><i>hostname</i></p>
<dd> hostname Override name of client sent to server.</p>
<dt><code>-P </code><i>password</i></p>
<dd> Database server password.</p>
<dt><code>-S </code><i>servername</i></p>
<dd> Database server to which to connect.</p>
<dt><code>-U </code><i>username</i></p>
<dd> Database server login name. If username is not provided, a domain login is attempted for TDS 7+ connections.</p>
<dt><code>-e </code><i>error_file</i></p>
<dd> Name of file for errors.</p>
<dt><code>-h</code></p>
<dd> Print column headers with the data to the same file.</p>
<dt><code>-i </code><i>input_file</i></p>
<dd> Name of script file, containing SQL.</p>
<dt><code>-o </code><i>output_file</i></p>
<dd> Name of output file, holding result data.</p>
<dt><code>-q</code></p>
<dd> Do not print column metadata, return status, or rowcount. Overrides &#8211;<code>h </code></p>
<dt><code>-t </code><i>field_term</i></p>
<dd> Specifies the field terminator. Default is two spaces (&#8216; &#8216;). Recognized escape sequences are tab (&#8216;	&#8217;), carriage return (&#8216;&#8217;), newline (&#8216;
&#8217;), and backslash (&#8216;\&#8217;).</p>
<dt><code>-v</code></p>
<dd> Verbose mode, for more information about the DB-Library interaction. This also reports the result set metadata, including and return code. All verbose data are written to standard error (or &#8211;<code>e ), so as not to interfere with the data stream.</code></p>
<dt><code>-R </code><i>pivot_description</i></p>
<dd> Specify pivot trasformation. The format is Ao Ar down columns Ac Ao Ar across columns Ac Ao Ar function Ac Ao Ar value Ac . Columns are specified but numbers. The format of <i>down columns</i> and <i>across columns</i> is a comma separated list of columns. <i>function</i> is either count, sum, min or max.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>DSQUERY</code> default <i>servername</i></p>
<h2>NOTES</h2>
<p> is a filter; it reads from standard input, writes to standard output, and writes errors to standard error. The &#8211;<code>i , -o , and -e</code> options override these defaults. </p>
<p> The source code for is intended as a model for DB-Library users. DB-Library has a rich set of functions, and it can be hard sometimes to understand how to use them, particularly the first time. If you find something about the source code unclear, you are encouraged to email the author your comments.</p>
<h2>EXIT STATUS</h2>
<p> exits 0 on success, and &gt;0 if the server cannot process the query. </p>
<p> For messages with severity &gt; 10, calls <a href="/docs/linux/man/3-exit/">exit</a>(3) with the severity level. For example, if the severity level is 16, will return an exit status of 16 to the shell.</p>
<h2>HISTORY</h2>
<p> first appeared in FreeTDS 0.63.</p>
<h2>AUTHORS</h2>
<p> The utility was written by An James K. Lowden Aq jklowden [at] freetds.org .</p>
<h2>BUGS</h2>
<p> Microsoft servers as of SQL Server 7.0 SP 3 do not return output parameters unless the RPC functions are used. This means cannot return output parameters for stored procedures with these servers. </p>
<h2>Index</h2>
