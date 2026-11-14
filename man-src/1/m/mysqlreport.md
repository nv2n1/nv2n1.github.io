---
title: "mysqlreport(1)"
name: "mysqlreport"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlreport/"
description: "mysqlreport – Makes a friendly report of important MySQL status values"
---

<h2 class="name">NAME</h2>
<p> mysqlreport &#8211; Makes a friendly report of important MySQL status values </p>
<h2>SYNTAX</h2>
<p> mysqlreport [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> mysqlreport makes a friendly report of important MySQL status values. Actually, it makes a friendly report of nearly every status value from SHOW STATUS. Unlike SHOW STATUS which simply dumps over 100 values to screen in one long list, mysqlreport interprets and formats the values and presents the basic values and many more inferred values in a human-readable format. Numerous example reports are available at the mysqlreport web page at <a rel="nofollow" href="http://hackmysql.com/mysqlreport.">http://hackmysql.com/mysqlreport.</a> </p>
<p> The benefit of mysqlreport is that it allows you to very quickly see a wide array of performance indicators for your MySQL server which would otherwise need to be calculated by hand from all the various SHOW STATUS values. For example, the Index Read Ratio is an important value but it&#8217;s not present in SHOW STATUS; it&#8217;s an inferred value (the ratio of Key_reads to Key_read_requests). </p>
<p> This documentation outlines all the command line options in mysqlreport, most of which control which reports are printed. This document does not address how to interpret these reports; that topic is covered in the document Guide To Understanding mysqlreport at <a rel="nofollow" href="http://hackmysql.com/mysqlreportguide.">http://hackmysql.com/mysqlreportguide.</a> </p>
<h2>OPTIONS</h2>
<p> Technically, command line options are in the form &#8211;option, but -option works too. All options can be abbreviated if the abbreviation is unique. For example, option &#8211;host can be abbreviated &#8211;ho but not &#8211;h because &#8211;h is ambiguous: it could mean &#8211;host or &#8211;help. </p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Output help information and exit. </p>
<dt><code>&#8211;user USER</code></p>
<dd>
<dt><code>&#8211;password</code></p>
<dd> As of version 2.3 &#8211;password can take the password on the command line like &quot;&#8211;password FOO&quot;. Using &#8211;password alone without giving a password on the command line causes mysqlreport to prompt for a password. </p>
<dt><code>&#8211;host ADDRESS</code></p>
<dd>
<dt><code>&#8211;port PORT</code></p>
<dd>
<dt><code>&#8211;socket SOCKET</code></p>
<dd>
<dt><code>&#8211;no-mycnf</code></p>
<dd> &#8211;no-mycnf makes mysqlreport not read ~/.my.cnf which it does by default otherwise. &#8211;user and &#8211;password always override values from ~/.my.cnf. </p>
<dt><code>&#8211;dtq</code></p>
<dd> Print Distribution of Total Queries (DTQ) report (under Total in Questions report). Queries (or Questions) can be divided into four main areas: DMS (see &#8211;dms below), Com_ (see &#8211;com below), COM_QUIT (see COM_QUIT and Questions at <a rel="nofollow" href="http://hackmysql.com/com_quit">http://hackmysql.com/com_quit</a>), and Unknown. &#8211;dtq lists the number of queries in each of these areas in descending order. </p>
<dt><code>&#8211;dms</code></p>
<dd> Print Data Manipulation Statements (DMS) report (under DMS in Questions report). DMS are those from the MySQL manual section 13.2. Data Manipulation Statements. (Currently, mysqlreport considers only SELECT, INSERT, REPLACE, UPDATE, and DELETE.) Each DMS is listed in descending order by count. </p>
<dt><code>&#8211;com N</code></p>
<dd> Print top N number of non-DMS Com_ status values in descending order (after DMS in Questions report). If N is not given, default is 3. Such non-DMS Com_ values include Com_change_db, Com_show_tables, Com_rollback, etc. </p>
<dt><code>&#8211;sas</code></p>
<dd> Print report for Select_ and Sort_ status values (after Questions report). See MySQL Select and Sort Status Variables at <a rel="nofollow" href="http://hackmysql.com/selectandsort.">http://hackmysql.com/selectandsort.</a> </p>
<dt><code>&#8211;tab</code></p>
<dd> Print Threads, Aborted, and Bytes status reports (after Created temp report). As of mysqlreport v2.3 the Threads report reports on all Threads_ status values. </p>
<dt><code>&#8211;qcache</code></p>
<dd> Print Query Cache report.</p>
<dt><code>&#8211;all</code></p>
<dd> Equivalent to &quot;&#8211;dtq &#8211;dms &#8211;com 3 &#8211;sas &#8211;qcache&quot;. (Notice &#8211;tab is not invoked by &#8211;all.) </p>
<dt><code>&#8211;infile FILE</code></p>
<dd> Instead of getting SHOW STATUS values from MySQL, read values from FILE. FILE is often a copy of the output of SHOW STATUS including formatting characters (|, +, -). mysqlreport expects FILE to have the format &quot; value number &quot; where value is only alpha and underscore characters (A-Z and _) and number is a positive integer. Anything before, between, or after value and number is ignored. mysqlreport also needs the following MySQL server variables: version, table_cache, max_connections, key_buffer_size, query_cache_size. These values can be specified in INFILE in the format &quot;name = value&quot; where name is one of the aforementioned server variables and value is a positive integer with or without a trailing M and possible periods (for version). For example, to specify an 18M key_buffer_size: key_buffer_size = 18M. Or, a 256 table_cache: table_cache = 256. The M implies Megabytes not million, so 18M means 18,874,368 not 18,000,000. If these server variables are not specified the following defaults are used (respectively) which may cause strange values to be reported: 0.0.0, 64, 100, 8M, 0. </p>
<dt><code>&#8211;outfile FILE</code></p>
<dd> After printing the report to screen, print the report to FILE too. Internally, mysqlreport always writes the report to a temp file first: /tmp/mysqlreport.PID on *nix, c:mysqlreport.PID on Windows (PID is the script&#8217;s process ID). Then it prints the temp file to screen. Then if &#8211;outfile is specified, the temp file is copied to OUTFILE. After &#8211;email (below), the temp file is deleted. </p>
<dt><code>&#8211;email ADDRESS</code></p>
<dd> After printing the report to screen, email the report to ADDRESS. This option requires sendmail in /usr/sbin/, therefore it does not work on Windows. /usr/sbin/sendmail can be a sym link to qmail, for example, or any MTA that emulates sendmail&#8217;s -t command line option and operation. The FROM: field is &quot;mysqlreport&quot;, SUBJECT: is &quot;MySQL status report&quot;. </p>
<dt><code>&#8211;flush-status</code></p>
<dd> Execute a &quot;FLUSH STATUS;&quot; after generating the reports. If you do not have permissions in MySQL to do this an error from DBD::mysql::st will be printed after the reports. </p>
</dl>
<h2>AUTHORS</h2>
<p> Daniel Nichter </p>
<p> If mysqlreport breaks, send me a message from <a rel="nofollow" href="http://hackmysql.com/feedback">http://hackmysql.com/feedback</a> with the error. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mytop/">mytop</a>(1) </p>
<p> The comprehensive Guide To Understanding mysqlreport at <a rel="nofollow" href="http://hackmysql.com/mysqlreportguide.">http://hackmysql.com/mysqlreportguide.</a> </p>
<h2>Index</h2>
