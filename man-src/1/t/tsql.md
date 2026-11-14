---
title: "tsql(1)"
name: "tsql"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tsql/"
description: "tsql – utility to test FreeTDS connections and queries"
---

<h2>NAME</h2>
<p> <code>tsql</code> &#8211; utility to test FreeTDS connections and queries</p>
<h2>SYNOPSIS</h2>
<p> Br o &#8211;<code>S </code><i>servername</i> [-<code>I </code><i>interface</i> ] | &#8211;<code>H </code><i>hostname</i> [-<code>L</code> ] [-<code>p </code><i>port</i> ] Br c [-<code>D </code><i>dbname</i> ] [-<code>U </code><i>username</i> ] [-<code>P </code><i>password</i> ] [-<code>o </code><i>options</i> ]<br />
 &#8211;<code>C</code></p>
<h2>DESCRIPTION</h2>
<p> is a FreeTDS diagnostic tool. It uses the TDS protocol to connect to a Sybase or Microsoft SQL Server, and lets the user issue queries. does not use the FreeTDS client libraries. Instead, it uses only the lowest level library, libtds, to test the protocol implementation. </p>
<p> can be run in two ways, one which uses the freetds.conf and one which connects directly using the server&#8217;s hostname and port. The &#8211;<code>H</code> and &#8211;<code>p</code> parameters are provided to let the user verify a server is listening on the named host and port. These parameters override any configuration files and environment variables. Pl The &#8211;<code>S</code> parameter can be used to test the local configuration. FreeTDS will use freetds.conf (or equivalent) and environment variables in the normal way to determine the server&#8217;s IP address and port. You can use &#8211;<code>I</code> to specify a filename, overriding FreeTDS&#8217;s configuration file search algorithm.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-S </code><i>servername</i></p>
<dd> database server to which to connect.</p>
<dt><code>-D </code><i>dbname</i></p>
<dd> database to use.</p>
<dt><code>-I </code><i>interface</i></p>
<dd> freetds.conf or interfaces file describing servername.</p>
<dt><code>-H </code><i>hostname</i></p>
<dd> DNS hostname of the server.</p>
<dt><code>-p </code><i>port</i></p>
<dd> port at which SQL Server is listening.</p>
<dt><code>-U </code><i>username</i></p>
<dd> database login name. If username is not provided, a domain login is attempted for TDS 7+ connections.</p>
<dt><code>-P </code><i>password</i></p>
<dd> database password.</p>
<dt><code>-L</code></p>
<dd> list Microsoft server instances (with &#8211;<code>H ).</code></p>
<dt><code>-C</code></p>
<dd> print some of the compile-time configuration parameters.</p>
<dt><code>-o </code><i>options</i></p>
<dd> apply the options specified to every command.</p>
<dl>
<dt><code>-f</code></p>
<dd> No footer Bq result count</p>
<dt><code>-h</code></p>
<dd> No header Bq titles</p>
<dt><code>-t</code></p>
<dd> Print time</p>
<dt><code>-v</code></p>
<dd> Print version</p>
<dt><code>-q</code></p>
<dd> Quiet</dl>
<dt><code>-a </code><i>appname</i></p>
<dd> application name.</p>
<dt><code>-t </code><i>colterm</i></p>
<dd> column terminator.</p>
<dt><code>-r </code><i>rowterm</i></p>
<dd> row terminator.</p>
<dt><code>-r </code><i>rowterm</i></p>
<dd> row terminator.</p>
<dt><code>-J </code><i>charset</i></p>
<dd> character set.</p>
<dt><code>-v</code></p>
<dd> verbose mode.</dl>
<h2>NOTES</h2>
<p> If you can connect with `tsql&#8217; -S servername Ns , your basic FreeTDS installation is working. </p>
<p> Typing `exit&#8217; Ns , `quit&#8217; Ns , or `bye&#8217; (or <code>^D )</code> exits </p>
<p> Typing `version&#8217; displays the TDS protocol version. </p>
<p> Command batches may be separated with `go&#8217; or `GO&#8217; Ns . If `GO&#8217; the version string is reported before executing the batch. </p>
<p> After prompting for the password (if not provided with &#8211;<code>P ),</code> will attempt to connect to the remote server. displays a counter indicating the number of seconds elapsed during the connection attempt. Typically, immediately responds with a `1&gt;&#8217; prompt. If you see the counter (1, 2, 3, &#8230;), most likely is unable to connect to the indicated server. </p>
<p> is not a replacement for a complete isql such as sqsh (<a rel="nofollow" href="http://www.sqsh.org">www.sqsh.org</a>). If you have suggestions for ways to make more useful as a diagnostic tool, please post them to the FreeTDS mailing list for consideration.</p>
<h2>HISTORY</h2>
<p> first appeared in FreeTDS 0.60.</p>
<h2>AUTHORS</h2>
<p> The utility was written by An Brian Bruns Ns .</p>
<h2>BUGS</h2>
<p> Several, to be sure, now that it&#8217;s documented. :) </p>
<h2>Index</h2>
