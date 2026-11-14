---
title: "mysql_embedded(1)"
name: "mysql_embedded"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysql_embedded/"
description: "mysql – the MySQL command-line client"
---

<h2 class="name">NAME</h2>
<p> mysql &#8211; the MySQL command-line client </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysql [</code><i>options</i><code>] </code><i>db_name</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysql</code></p>
<dd>is a simple SQL shell with input line editing capabilities. It supports interactive and noninteractive use. When used interactively, query results are presented in an ASCII-table format. When used noninteractively (for example, as a filter), the result is presented in tab-separated format. The output format can be changed using command options. </p>
<p> If you have problems due to insufficient memory for large result sets, use the <code>&#8211;quick</code> option. This forces <code>mysql</code> to retrieve results from the server a row at a time rather than retrieving the entire result set and buffering it in memory before displaying it. This is done by returning the result set using the mysql_use_result() C API function in the client/server library rather than mysql_store_result(). </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Alternatively, MySQL Shell offers access to the X DevAPI. For details, see m[blue]<code>MySQL Shell 8.0 (part of MySQL 8.0)</code>m[]<font SIZE="-2">[1]</font>. </p>
</dl>
<p> Using <code>mysql</code> is very easy. Invoke it from the prompt of your command interpreter as follows: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql </code><i>db_name</i>
</pre>
</dl>
<p> Or: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql --user=</code><i>user_name</i><code> --password </code><i>db_name</i>
Enter password: <i>your_password</i>
</pre>
</dl>
<p> Then type an SQL statement, end it with ;, \g, or \G and press Enter. </p>
<p> Typing Control+C interrupts the current statement if there is one, or cancels any partial input line otherwise. </p>
<p> You can execute SQL statements in a script file (batch file) like this: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>mysql </code><i>db_name</i><code> &lt; </code><i>script.sql</i><code> &gt; </code><i>output.tab</i>
</pre>
</dl>
<p> On Unix, the <code>mysql</code> client logs statements executed interactively to a history file. See the section called &#8220;MYSQL CLIENT LOGGING&#8221;.</p>
<h2>MYSQL CLIENT OPTIONS</h2>
<p> <code>mysql</code> supports the following options, which can be specified on the command line or in the [mysql] and [client] groups of an option file. For information about option files used by MySQL programs, see Section 4.2.2.2, &#8220;Using Option Files&#8221;. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code>, <code>-?</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;auto-rehash</code> </p>
<p> Enable automatic rehashing. This option is on by default, which enables database, table, and column name completion. Use <code>&#8211;disable-auto-rehash</code> to disable rehashing. That causes <code>mysql</code> to start faster, but you must issue the rehash command or its \# shortcut if you want to use name completion. </p>
<p> To complete a name, enter the first part and press Tab. If the name is unambiguous, <code>mysql</code> completes it. Otherwise, you can press Tab again to see the possible names that begin with what you have typed so far. Completion does not occur if there is no default database. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 This feature requires a MySQL client that is compiled with the <code>readline</code> library. Typically, the <code>readline</code> library is not available on Windows. </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;auto-vertical-output</code> </p>
<p> Cause result sets to be displayed vertically if they are too wide for the current window, and using normal tabular format otherwise. (This applies to statements terminated by ; or \G.)</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;batch</code>, <code>-B</code> </p>
<p> Print results using tab as the column separator, with each row on a new line. With this option, <code>mysql</code> does not use the history file. </p>
<p> Batch mode results in nontabular output format and escaping of special characters. Escaping may be disabled by using raw mode; see the description for the <code>&#8211;raw</code> option.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;binary-as-hex</code> </p>
<p> When this option is given, <code>mysql</code> displays binary data using hexadecimal notation (0x<i>value</i>). This occurs whether the overall output dislay format is tabular, vertical, HTML, or XML. </p>
<p> This option was added in MySQL 5.7.19.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;binary-mode</code> </p>
<p> This option helps when processing <code>mysqlbinlog</code> output that may contain BLOB values. By default, <code>mysql</code> translates 
 in statement strings to 
 and interprets 
