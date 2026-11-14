---
title: "fisql(1)"
name: "fisql"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fisql/"
description: "fisql – interactive SQL shell"
---

<h2 class="name">NAME</h2>
<p> <code>fisql</code> &#8211; interactive SQL shell </p>
<h2>SYNOPSIS</h2>
<p> [-<code>eFgpnvXY</code> ] [-<code>a </code><i>display_charset</i> ] [-<code>A </code><i>packet_size</i> ] [-<code>c </code><i>cmdend</i> ] [-<code>D </code><i>database</i> ] [-<code>E </code><i>editor</i> ] [-<code>h </code><i>headers</i> ] [-<code>H </code><i>hostname</i> ] [-<code>i </code><i>inputfile</i> ] [-<code>I </code><i>interfaces_file</i> ] [-<code>J </code><i>client_charset</i> ] [-<code>l </code><i>login_timeout</i> ] [-<code>m </code><i>errorlevel</i> ] [-<code>o </code><i>outputfile</i> ] [-<code>P </code><i>password</i> ] [-<code>s </code><i>colseparator</i> ] [-<code>S </code><i>server</i> ] [-<code>t </code><i>timeout</i> ] [-<code>U </code><i>username</i> ] [-<code>w </code><i>width</i> ] [-<code>y </code><i>sybase_dir</i> ] [-<code>z </code><i>language</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is very similar to the `isql&#8217; utility programs distributed by Sybase and Microsoft. Like them, uses the command `go&#8217; on a line by itself as a separator between batches.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a </code><i>display_charset</i></p>
<dd> The client charset name. Not implemented.</p>
<dt><code>-A </code><i>packet_size</i></p>
<dd> Set protocol packet size. You should not need to set this parameter.</p>
<dt><code>-c </code><i>cmdend</i></p>
<dd> Command terminator, defaults to `go&#8217; Ns .</p>
<dt><code>-D</code></p>
<dd> Database name on the server to use.</p>
<dt><code>-e</code></p>
<dd> Echo SQL input (usually in outputfile)</p>
<dt><code>-E </code><i>editor</i></p>
<dd> Specify an editor to invoke. Defaults to vi.</p>
<dt><code>-F</code></p>
<dd> FIPS mode ON. Server returns a message (but processes the query anyway) when it encounters a non-standard SQL command.</p>
<dt><code>-g</code></p>
<dd> Display a brief help message</p>
<dt><code>-h </code><i>headers</i></p>
<dd> Number of rows after which to repeat the column headers. Default is once per resultset.</p>
<dt><code>-H </code><i>hostname</i></p>
<dd> Hostname of the client machine as it will be told to the server.</p>
<dt><code>-I </code><i>interfaces_file</i></p>
<dd> Name of the interfaces or freetds.conf file to use.</p>
<dt><code>-i </code><i>inputfile</i></p>
<dd> Name of script file, containing SQL.</p>
<dt><code>-J </code><i>client_charset</i></p>
<dd> Not implemented.</p>
<dt><code>-l </code><i>login_timeout</i></p>
<dd> How long to wait for the server to acknowledge a login attempt.</p>
<dt><code>-m </code><i>errorlevel</i></p>
<dd> For errors of the severity level specified or higher, print only the message number, state, and error level. Below that level, print nothing.</p>
<dt><code>-n</code></p>
<dd> Suppress line numbers in echoed output.</p>
<dt><code>-o </code><i>outputfile</i></p>
<dd> Name of output file, holding result data.</p>
<dt><code>-p</code></p>
<dd> Prints performance statistics. Not implemented.</p>
<dt><code>-P </code><i>password</i></p>
<dd> Database server password.</p>
<dt><code>-s </code><i>colseparator</i></p>
<dd> The column separator. Default is space. Shell metacharacters require quoting.</p>
<dt><code>-S </code><i>server</i></p>
<dd> Database server to which to connect.</p>
<dt><code>-t </code><i>timeout</i></p>
<dd> The query timeout, in seconds. How long to wait for a query to be processed. The default is indefinitely, or as determined by freetds.conf.</p>
<dt><code>-U </code><i>username</i></p>
<dd> Database server login name.</p>
<dt><code>-v</code></p>
<dd> Display version and copyright.</p>
<dt><code>-w </code><i>width</i></p>
<dd> How many characters wide to print the output. Defaults to 80.</p>
<dt><code>-X</code></p>
<dd> Use encrypted login. Not implemented in FreeTDS.</p>
<dt><code>-y sybase_dir </code></p>
<dd> Sets the <code>SYBASE</code> environment variable. Not used by FreeTDS.</p>
<dt><code>-Y</code></p>
<dd> Use chained transactions.</p>
<dt><code>-z </code><i>language</i></p>
<dd> Name of a language for fisql&#8217;s prompts and messages. Cf. DBSETLNATLANG.</dl>
<h2>NOTES</h2>
<p> is a filter; it reads from standard input, writes to standard output, and writes errors to standard error. The &#8211;<code>i ,</code> and &#8211;<code>e</code> options override these defaults. </p>
<p> uses the DB-Library API provided by FreeTDS. It was first implemented using Sybase&#8217;s own library and continues to work with it. Before (and after) modifying it, it would be well to test it with Sybase&#8217;s library to assure compatibility between it and FreeTDS. EXIT STATUS </p>
<p> exits 0 on success, and &gt;0 if the server cannot process the query. </p>
<p> will report any errors returned by the server, but will continue processing. In a production environment, this behavior may be insufficiently stringent. To make it extremely intolerant of errors, change the message and error handlers to call <a href="/docs/linux/man/3-exit/">exit</a>(3).</p>
<h2>HISTORY</h2>
<p> first appeared in FreeTDS 0.65.</p>
<h2>AUTHORS</h2>
<p> The utility was written by An Nicholas S. Castellano Aq entropy [at] freetds.org Ns , who contributed it to the FreeTDS project under the terms of the GPL.</p>
<h2>BUGS</h2>
<p> Requires the GNU readline library. </p>
<h2>Index</h2>
