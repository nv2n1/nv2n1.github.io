---
title: "grephistory(1)"
name: "grephistory"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grephistory/"
description: "grephistory – Query the INN history database"
---

<h2 class="name">NAME</h2>
<p> grephistory &#8211; Query the INN history database </p>
<h2>SYNOPSIS</h2>
<p> <code>grephistory</code> [<code>-eilnqsv</code>] [<code>-f</code> <i>db</i>] [<i>message-id</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>grephistory</code> queries the <font SIZE="-1">INN</font> history database for information about the specified message-ID. If no flags are given, the program prints the storage <font SIZE="-1">API</font> token of the corresponding article, or <tt>&quot;/dev/null&quot;</tt> if the article is listed in the history database but not stored on the server. If the message-ID cannot be found in the database, <code>grephistory</code> will print <tt>&quot;grephistory: not found&quot;</tt> and exit with a non-zero status. </p>
<p> Be sure to escape any special characters in the message <font SIZE="-1">ID</font> from the shell. Single quotes are recommended for this purpose since many message-IDs contain dollar signs.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code></p>
<dd> Only print the storage token if the article is stored on the system. (In other words, suppress the <tt>&quot;/dev/null&quot;</tt> or <tt>&quot;not found&quot;</tt> output for missing or remembered articles.)</p>
<dt><code>-f</code> <i>db</i></p>
<dd> Query the history database <i>db</i> rather than the default history database.</p>
<dt><code>-i</code></p>
<dd> Rather than expecting a message-ID on the command line, <code>grephistory</code> will read a list of message-IDs on standard input, one per line. Leading and trailing whitespace is ignored, as are any malformed lines. It will print on standard output those message-IDs which are not found in the history database. This is used when processing <tt>&quot;ihave&quot;</tt> control messages.</p>
<dt><code>-l</code></p>
<dd> Display the entire line from the history database, rather than just the storage <font SIZE="-1">API</font> token. If the message-ID is present in the history database but has no storage <font SIZE="-1">API</font> token, <code>grephistory</code> does not print anything.</p>
<dt><code>-n</code></p>
<dd> If the message-ID is present in the history database but has no storage <font SIZE="-1">API</font> token, print <tt>&quot;/dev/null&quot;</tt> and exit successfully. This can happen if an article has been cancelled or expired, but history information has still been retained. This is the default behavior.</p>
<dt><code>-q</code></p>
<dd> Don&#8217;t print any message, but still exit with the appropriate status.</p>
<dt><code>-s</code></p>
<dd> Rather than expecting a message-ID on the command line, <code>grephistory</code> will read a list of message-IDs on standard input, one per line. Leading and trailing whitespace is ignored, as are any malformed lines. It will print on standard output the storage <font SIZE="-1">API</font> tokens for any articles that are still available, one per line. This flag is used when processing <tt>&quot;sendme&quot;</tt> control messages.</p>
<dt><code>-v</code></p>
<dd> Print out the hash of the message-ID for diagnostic purposes, as well as any other requested information. This flag is not useful with <code>-i</code> or <code>-s</code>.</dl>
<h2>EXAMPLES</h2>
<p> In case the requested article is not listed in the history database: </p>
<pre><code>
% grephistory '&lt;unknown.article [at] news.example.com&gt;' grephistory : not found % grephistory - v '&lt;unknown.article [at] news.example.com&gt;' grephistory : not found(hash is 501C66C22932BA91131186D7218201EB)
</code></pre>
<p> In case the requested article is listed in the history database but not stored on the server: </p>
<pre>
    % grephistory '&lt;remembered.article [at] news.example.com&gt;'
    /dev/null
</pre>
<p> In case the requested article is stored on the server: </p>
<pre><code>
% grephistory '&lt;87fxeaay1z.fsf [at] windlord.stanford.edu&gt;' @02014A2DD6231FCC00000000000000000000 @ % grephistory - l '&lt;87fxeaay1z.fsf [at] windlord.stanford.edu&gt;'
                                                                                                                        [B6DDF69376E3CC199246CEC949B3ACAC] 1244517923 ~-~1244517912 @02014A2DD6231FCC00000000000000000000 @
</code></pre>
<p> With <code>sm</code>, we can retrieve the article, and get its posting date: </p>
<pre>
    % grephistory '&lt;87fxeaay1z.fsf [at] windlord.stanford.edu&gt;' | sm | grep Date
    Date: Mon, 08 Jun 2009 20:25:12 -0700
    % convdate -dc 1244517912
    Tue, 9 Jun 2009 03:25:12 +0000 (UTC)
</pre>
<p> It matches the number recorded in history as for its posting date.</p>
<h2>HISTORY</h2>
<p> Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> grephistory.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-history/">history</a></i>(5), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/1-sm/">sm</a></i>(1). </p>
<h2>Index</h2>
