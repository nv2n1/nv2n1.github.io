---
title: "copy(7)"
name: "copy"
section: "7"
letter: "c"
url: "/docs/linux/man/7-copy/"
description: "COPY – copy data between a file and a table"
---

<p>COPY &#8211; copy data between a file and a table </p>
<h2>Synopsis</h2>
<pre>COPY <i>tablename</i> [ ( <i>column</i> [, ...] ) ]
 FROM { '<i>filename</i>' | STDIN }
 [ [ WITH ] 
 [ BINARY ]
 [ OIDS ]
 [ DELIMITER [ AS ] '<i>delimiter</i>' ]
 [ NULL [ AS ] '<i>null string</i>' ]
 [ CSV [ HEADER ]
 [ QUOTE [ AS ] '<i>quote</i>' ] 
 [ ESCAPE [ AS ] '<i>escape</i>' ]
 [ FORCE NOT NULL <i>column</i> [, ...] ]
COPY { <i>tablename</i> [ ( <i>column</i> [, ...] ) ] | ( <i>query</i> ) }
 TO { '<i>filename</i>' | STDOUT }
 [ [ WITH ] 
 [ BINARY ]
 [ OIDS ]
 [ DELIMITER [ AS ] '<i>delimiter</i>' ]
 [ NULL [ AS ] '<i>null string</i>' ]
 [ CSV [ HEADER ]
 [ QUOTE [ AS ] '<i>quote</i>' ] 
 [ ESCAPE [ AS ] '<i>escape</i>' ]
 [ FORCE QUOTE <i>column</i> [, ...] ]</pre>
<h2>Description</h2>
<p><code>COPY</code> moves data between PostgreSQL tables and standard file-system files. <code>COPY TO</code> copies the contents of a table <code>to</code> a file, while <code>COPY FROM</code> copies data <code>from</code> a file to a table (appending the data to whatever is in the table already). <code>COPY TO</code> can also copy the results of a <code>SELECT</code> query. </p>
<p> If a list of columns is specified, <code>COPY</code> will only copy the data in the specified columns to or from the file. If there are any columns in the table that are not in the column list, <code>COPY FROM</code> will insert the default values for those columns. </p>
<p> <code>COPY</code> with a file name instructs the PostgreSQL server to directly read from or write to a file. The file must be accessible to the server and the name must be specified from the viewpoint of the server. When STDIN or STDOUT is specified, data is transmitted via the connection between the client and the server.</p>
<h2>Parameters</h2>
<dl>
<dt><i>tablename</i></p>
<dd>The name (optionally schema-qualified) of an existing table.</p>
<dt><i>column</i></p>
<dd>An optional list of columns to be copied. If no column list is specified, all columns of the table will be copied.</p>
<dt><i>query</i></p>
<dd>A SELECT [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] or VALUES [<code><a href="/docs/linux/man/7-values/">values</a></code>(7)] command whose results are to be copied. Note that parentheses are required around the query.</p>
<dt><i>filename</i></p>
<dd>The absolute path name of the input or output file. Windows users might need to use an E&#8221; string and double backslashes used as path separators.</p>
<dt><code>STDIN</code></p>
<dd>Specifies that input comes from the client application.</p>
<dt><code>STDOUT</code></p>
<dd>Specifies that output goes to the client application.</p>
<dt><code>BINARY</code></p>
<dd>Causes all data to be stored or read in binary format rather than as text. You cannot specify the <code>DELIMITER</code>, <code>NULL</code>, or <code>CSV</code> options in binary mode.</p>
<dt><code>OIDS</code></p>
<dd>Specifies copying the OID for each row. (An error is raised if OIDS is specified for a table that does not have OIDs, or in the case of copying a <i>query</i>.)</p>
<dt><i>delimiter</i></p>
<dd>The single ASCII character that separates columns within each row (line) of the file. The default is a tab character in text mode, a comma in CSV mode.</p>
<dt><i>null string</i></p>
<dd>The string that represents a null value. The default is \N (backslash-N) in text mode, and an unquoted empty string in CSV mode. You might prefer an empty string even in text mode for cases where you don&#8217;t want to distinguish nulls from empty strings. </p>
<dl>
<dd><code>Note:</code> When using <code>COPY FROM</code>, any data item that matches this string will be stored as a null value, so you should make sure that you use the same string as you used with <code>COPY TO</code>.</dl>
<dt><code>CSV</code></p>
<dd>Selects Comma Separated Value (CSV) mode.</p>
<dt><code>HEADER</code></p>
<dd>Specifies that the file contains a header line with the names of each column in the file. On output, the first line contains the column names from the table, and on input, the first line is ignored.</p>
<dt><i>quote</i></p>
<dd>Specifies the ASCII quotation character in CSV mode. The default is double-quote.</p>
<dt><i>escape</i></p>
<dd>Specifies the ASCII character that should appear before a QUOTE data character value in CSV mode. The default is the QUOTE value (usually double-quote).</p>
<dt><code>FORCE QUOTE</code></p>
<dd>In CSV <code>COPY TO</code> mode, forces quoting to be used for all non-NULL values in each specified column. NULL output is never quoted.</p>
<dt><code>FORCE NOT NULL</code></p>
<dd>In CSV <code>COPY FROM</code> mode, process each specified column as though it were quoted and hence not a NULL value. For the default null string in CSV mode (&#8221;), this causes missing values to be input as zero-length strings.</dl>
<h2>Outputs</h2>
<p>On successful completion, a <code>COPY</code> command returns a command tag of the form </p>
<pre>COPY <i>count</i></pre>
<p>The <i>count</i> is the number of rows copied.</p>
<h2>Notes</h2>
<p><code>COPY</code> can only be used with plain tables, not with views. However, you can write COPY (SELECT * FROM <i>viewname</i>) TO &#8230;. </p>
<p> The BINARY key word causes all data to be stored/read as binary format rather than as text. It is somewhat faster than the normal text mode, but a binary-format file is less portable across machine architectures and PostgreSQL versions. Also, the binary format is very data type specific; for example it will not work to output binary data from a <code>smallint</code> column and read it into an <code>integer</code> column, even though that would work fine in text format. </p>
<p> You must have select privilege on the table whose values are read by <code>COPY TO</code>, and insert privilege on the table into which values are inserted by <code>COPY FROM</code>. It is sufficient to have column privileges on the column(s) listed in the command. </p>
<p> Files named in a <code>COPY</code> command are read or written directly by the server, not by the client application. Therefore, they must reside on or be accessible to the database server machine, not the client. They must be accessible to and readable or writable by the PostgreSQL user (the user ID the server runs as), not the client. <code>COPY</code> naming a file is only allowed to database superusers, since it allows reading or writing any file that the server has privileges to access. </p>
<p> Do not confuse <code>COPY</code> with the <code>psql</code> instruction <code>
