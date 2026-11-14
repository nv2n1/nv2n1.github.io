---
title: "bsqlodbc(1)"
name: "bsqlodbc"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bsqlodbc/"
description: "bsqlodbc – batch SQL script processor using ODBC"
---

<h2 class="name">NAME</h2>
<p> <code>bsqlodbc</code> &#8211; batch SQL script processor using ODBC </p>
<h2>SYNOPSIS</h2>
<p> [-<code>hqv</code> ] [-<code>U </code><i>username</i> ] [-<code>P </code><i>password</i> ] [-<code>S </code><i>server</i> ] [-<code>D </code><i>database</i> ] [-<code>i </code><i>input_file</i> ] [-<code>o </code><i>output_file</i> ] [-<code>e </code><i>error_file</i> ] [-<code>t </code><i>field_term</i> ] [-<code>V </code><i>odbc_version</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is a utility program distributed with FreeTDS. </p>
<p> is a non-interactive equivalent of the `isql&#8217; utility programs distributed by Sybase and Microsoft. Like them, uses the command `go&#8217; on a line by itself as a separator between batches. The last batch need not be followed by `go&#8217; </p>
<p> makes use of the ODBC API provided by FreeTDS. This API is of course also available to application developers.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-U </code><i>username</i></p>
<dd> Database server login name.</p>
<dt><code>-P </code><i>password</i></p>
<dd> Database server password.</p>
<dt><code>-S </code><i>server</i></p>
<dd> Database server to which to connect.</p>
<dt><code>-D </code><i>database</i></p>
<dd> Database to use.</p>
<dt><code>-i </code><i>input_file</i></p>
<dd> Name of script file, containing SQL.</p>
<dt><code>-o </code><i>output_file</i></p>
<dd> Name of output file, holding result data.</p>
<dt><code>-e </code><i>error_file</i></p>
<dd> Name of file for errors.</p>
<dt><code>-t </code><i>field_term</i></p>
<dd> Specifies the field terminator. Default is two spaces ( `&nbsp;<wbr>&#8216; <code>).</code> Recognized escape sequences are tab ( `	&#8217; <code>), </code> carriage return ( `&#8217; <code>), </code> newline ( `
&#8217; <code>),</code> and backslash ( `\&#8217; <code>).</code></p>
<dt><code>-h</code></p>
<dd> Print column headers with the data to the same file.</p>
<dt><code>-q </code></p>
<dd> Do not print column metadata, return status, or rowcount. Overrides &#8211;<code>h</code></p>
<dt><code>-v</code></p>
<dd> Verbose mode, for more information about the ODBC interaction. This also reports the result set metadata, including and return code. All verbose data are written to standard error (or &#8211;<code>e ),</code> so as not to interfere with the data stream.</p>
<dt><code>-V </code><i>odbc_version</i></p>
<dd> Specify ODBC version (2 or 3).</dl>
<h2>NOTES</h2>
<p> is a filter; it reads from standard input, writes to standard output, and writes errors to standard error. The &#8211;<code>i</code> &#8211;<code>o</code> and &#8211;<code>e</code> options override these defaults.</p>
<h2>EXIT STATUS</h2>
<p> exits 0 on success, and &gt;0 if the server cannot process the query.</p>
<h2>HISTORY</h2>
<p> first appeared in FreeTDS 0.65.</p>
<h2>AUTHORS</h2>
<p> The utility was written by An James K. Lowden Aq jklowden [at] freetds.org . </p>
<h2>Index</h2>
