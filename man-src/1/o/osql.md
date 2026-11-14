---
title: "osql(1)"
name: "osql"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osql/"
description: "osql – utility to test FreeTDS connections and queries"
---

<h2 class="name">NAME</h2>
<p> <code>osql</code> &#8211; utility to test FreeTDS connections and queries </p>
<h2>SYNOPSIS</h2>
<p> &#8211;<code>S </code><i>dsn </i> &#8211;<code>U </code><i>username</i> &#8211;<code>P </code><i>password</i> [-<code>I ini_directory </code> ]</p>
<h2>DESCRIPTION</h2>
<p> is a diagnostic tool provided as part of FreeTDS. It is a Bourne shell script that checks and reports on your configuration files. If everything checks out OK, it invokes isql. </p>
<p> works only with the isql that comes with unixODBC.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-S </code><i>dsn</i></p>
<dd> the Data Source Name to which to connect, as known to odbc.ini</p>
<dt><code>-U </code><i>username</i></p>
<dd> database login name.</p>
<dt><code>-P </code><i>password</i></p>
<dd> database password.</p>
<dt><code>-I </code><i>ini_dir</i></p>
<dd> override odbc.ini file location.</dl>
<h2>EXAMPLE</h2>
<p> If you have an odbc.ini with a section like this: </p>
<blockquote>
<pre>
Bq myDSN
servername = myserver
TDS_Version = 5.0
</pre>
</blockquote>
<p> You would invoke as: </p>
<p> <code>osql -S myDSN </code> [&#8230;]</p>
<h2>FILES</h2>
<p> odbc.ini freetds.conf</p>
<h2>NOTES</h2>
<p> If you can connect with `osql&#8217; -S servername -U user -P passwd Ns , your FreeTDS ODBC installation is working. </p>
<p> guesses where unixODBC might look for its odbc.ini by examining the binary. This is not always an effective approach. If it doesn&#8217;t work, you&#8217;ll receive a report of candidate strings. Kindly pass along the output to help improve the guessing. </p>
<p> If cannot intuit your odbc.ini directory, you can force the issue with the &#8211;<code>I</code> option. However, you&#8217;re then instructing what to test, not where unixODBC will eventually look. Your override is therefore only as good as you are. Look carefully at the error output before overriding. </p>
<p> If you have suggestions for ways to make more useful as a diagnostic tool, please post them to the FreeTDS mailing list.</p>
<h2>HISTORY</h2>
<p> first appeared in FreeTDS 0.65.</p>
<h2>AUTHORS</h2>
<p> The utility was written by An James K. Lowden Ns . </p>
<h2>Index</h2>
