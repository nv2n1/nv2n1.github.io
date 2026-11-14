---
title: "freebcp(1)"
name: "freebcp"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freebcp/"
description: "freebcp – bulk loading utility for Sybase and Microsoft databases"
---

<h2>NAME</h2>
<p> <code>freebcp</code> &#8211; bulk loading utility for Sybase and Microsoft databases</p>
<h2>SYNOPSIS</h2>
<p> Bo Bo Ao Ar database Ac Ns . Bc Ns Ao Ar owner Ac Ns . Bc Ns Aq Ar object_name Br o <i>in</i> | <i>[query] </i><i>out</i> Br c <i>datafile</i> Br o &#8211;<code>c</code> | &#8211;<code>n</code> | &#8211;<code>f </code><i>formatfile</i> Br c [-<code>S </code><i>servername</i> ] [-<code>D </code><i>dbname</i> ] [-<code>U </code><i>username</i> ] [-<code>P </code><i>password</i> ] [-<code>b </code><i>batchsize</i> ] [-<code>F </code><i>firstrow</i> ] [-<code>L </code><i>lastrow</i> ] [-<code>e </code><i>errfile</i> ] [-<code>I </code><i>interfaces</i> ] [-<code>m </code><i>maxerror</i> ] [-<code>t </code><i>field_term</i> ] [-<code>r </code><i>row_term</i> ] [-<code>h </code><i>hints</i> ] [-<code>T </code><i>textsize</i> ] [-<code>A </code><i>packet_size</i> ] [-<code>O </code><i>options</i> ] [-<code>i </code><i>inputfile</i> ] [-<code>o </code><i>outputfile</i> ] [-<code>C </code><i>charset</i> ] [-<code>EdVv </code> ]</p>
<h2>DESCRIPTION</h2>
<p> is a utility program distributed with FreeTDS. replicates (in part at least) the functionality of the bcp utility programs distributed by Sybase and Microsoft. makes use of the DB-Library bcp API provided by FreeTDS. This API is also available to application developers. </p>
<p> The manual pages or online help for Sybase or SQL Server can be referenced for more detailed information on bcp functionality.</p>
<h2>TABLES AND FILES</h2>
<dl>
<dt><i>database</i></p>
<dd> The name of the database containing object to be copied. Optional if the table/view is in the default database for <i>username</i></p>
<dt><i>schema</i></p>
<dd> The schema of the object being copied. If not provided, the default schema for <i>username</i> is used.</p>
<dt><i>object</i></p>
<dd> The name of the database object you wish to access, typically a table. It can also be a view. All views can be read; some can be written, subject to constraints. With <i>queryout </i><code>, </code><i>object</i> can also be an SQL query.</p>
<dt><i>in</i></p>
<dd> Copy data from a host file to a database table.</p>
<dt><i>out</i></p>
<dd> Copy data from a database table to a host file.</p>
<dt><i>queryout</i></p>
<dd> indicates that <i>table_name</i> is in fact SQL, rather than a database object. will execute the query and write the results to a file. (It is a good idea to have the query return one and only one result set.)</p>
<dt><i>datafile</i></p>
<dd> The name of an operating system file.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A </code><i>packet_size</i></p>
<dd> Set the size of a TDS packet to packet_size. Not sure why you would want to do this, except as an experiment.</p>
<dt><code>-D </code><i>dbname</i></p>
<dd> The name of the default database to use. Overrides default database associated with the login account. Causes to issue a <code>USE </code><i>dbname </i> command immediately after logging in, before commencing BCP operations.</p>
<dt><code>-E</code></p>
<dd> Write the data in datafile to the table&#8217;s IDENTITY column. Without this flag, the identity data present in the datafile will be ignored, and new IDENTITY values will be generated for the imported rows.</p>
<dt><code>-F </code><i>firstrow</i></p>
<dd> The first row to copy from the input file or database table. The default is the first row, row 1.</p>
<dt><code>-I </code><i>interfaces</i></p>
<dd> The name and location of the interfaces file to search when connecting to servername. Overrides freetds.conf.</p>
<dt><code>-L </code><i>lastrow</i></p>
<dd> The last row to copy from an input file or database table. The default is the last row.</p>
<dt><code>-O </code><i>options</i></p>
<dd> SQL text to set connection options prior to the bcp operation. If <i>options</i> is a valid filename, the SQL is read from the file instead. Sometimes needed for <i>queryout</i> Example: <code>-O `SET QUOTED_IDENTIFIER ON&#8217; </code></p>
<dt><code>-P </code><i>password</i></p>
<dd> The password associated with <i>username</i></p>
<dt><code>-S </code><i>servername</i></p>
<dd> The name of the Database Server to which to connect.</p>
<dt><code>-T </code><i>textsize</i></p>
<dd> For text or image columns, set the maximum number of characters to request from the server. Defaults to the setting in freetds.conf If not specified anywhere, defaults to the full size of the data.</p>
<dt><code>-U </code><i>username</i></p>
<dd> A database login name. For TDS 7+ connections, a domain login is attempted if <i>username</i> is not provided.</p>
<dt><code>-b </code><i>batchsize</i></p>
<dd> The number of rows per batch of data copied. Batching applies only when you are bulk copying into the database. Each batch of data is effectively &#8220;committed&#8221; into the database. The default value for <i>batchsize</i> is 1000.</p>
<dt><code>-c</code></p>
<dd> The host data file is (or will be) in &quot;character&quot; format, i.e., a text file. Encoding is determined by the client charset attribute in freetds.conf</p>
<dt><code>-d</code></p>
<dd> Turn off any logging. (Unintuitive, perhaps.)</p>
<dt><code>-e </code><i>errfile</i></p>
<dd> Write errors to <i>errfile . </i> For uploads. Includes line and column information, and the row data.</p>
<dt><code>-f </code><i>formatfile</i></p>
<dd> The format of the host data file is described by <i>formatfile . </i> The layout of <i>formatfile</i> is identical to that understood by the Sybase and Microsoft bcp utilities, but is too complicated to describe here.</p>
<dt><code>-h </code><i>hints</i></p>
<dd> Set bcp hints. For valid values, cf. Fn bcp_options in the FreeTDS Reference Manual.</p>
<dt><code>-m </code><i>maxerror</i></p>
<dd> Stop after encountering <i>maxerror</i> errors. Default 10.</p>
<dt><code>-n</code></p>
<dd> The host data file is in &#8220;native&#8221; format. This is a format that will be able to process, but is not portable or readable.</p>
<dt><code>-r </code><i>row_term</i></p>
<dd> The row terminator for a character file. May be more than one character. Default is newline (&#8216;
&#8217;). Cf. &#8211;<code>c ,</code> above.</p>
<dt><code>-t </code><i>field_term</i></p>
<dd> The field terminator for character file. Also known as a column delimiter. May be more than one character. Default is tab (&#8216;	&#8217;). Cf. &#8211;<code>c , above.</code></p>
<dt><code>-v</code></p>
<dd>
<dt><code>-V</code></p>
<dd> Print the version information and exit.</p>
<dt><code>-i </code><i>inputfile</i></p>
<dd> Read input data from file specified.</p>
<dt><code>-o </code><i>outputfile</i></p>
<dd> Write output data to file specified.</p>
<dt><code>-C </code><i>charset</i></p>
<dd> Specify character set to use to talk to server.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>DSQUERY</code> default <i>servername</i></p>
<h2>NOTES</h2>
<p> When connecting to a Sybase database server, it is required that the TDS 5.0 protocol be used. When connecting to a Microsoft SQL Server 2000 database server, the TDS 7 (or later) protocol is required. </p>
<p> Sybase and Microsoft define different versions of the bcp portion of TDS 4.2. Because FreeTDS has no way of knowing which type of server it&#8217;s connected to, does not support version 4.2 of the TDS protocol.</p>
<h2>HISTORY</h2>
<p> first appeared in FreeTDS 0.60</p>
<h2>AUTHORS</h2>
<p> The utility was written by An Bill Thompson Aq thompbil [at] exchange.uk.ml.com</p>
<h2>BUGS</h2>
<p> Currently, there is no support for text data types in <code>, when</code> SQL Server 2000 is the target server. </p>
<h2>Index</h2>
