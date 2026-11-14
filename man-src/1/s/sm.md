---
title: "sm(1)"
name: "sm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sm/"
description: "sm – Command-line interface to the INN storage manager"
---

<h2 class="name">NAME</h2>
<p> sm &#8211; Command-line interface to the INN storage manager </p>
<h2>SYNOPSIS</h2>
<p> <code>sm</code> [<code>-cdHiqRrSs</code>] [<i>token</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <font SIZE="-1">INN</font> storage manager is the subsystem that stores and keeps track of all of the articles and what storage backend they&#8217;re in. All stored articles are assigned a storage <font SIZE="-1">API</font> token. <code>sm</code> is a command-line interface to that storage manager, primarily used to retrieve articles by those tokens but also to perform other operations on the storage subsystem. </p>
<p> <i>token</i> is the token of an article (the same thing that&#8217;s returned by <code>grephistory</code> or stored in the <i>history</i> file). It looks something like: </p>
<pre>
    @0502000005A4000000010000000000000000@
</pre>
<p> Any number of tokens can be given on the command-line for any function other than <code>-s</code>. If none are, <code>sm</code> normally reads tokens from standard input, one per line. The default operation is to retrieve and write to standard output the corresponding article for each token given. </p>
<p> If <code>-s</code> is given, <code>sm</code> instead stores the article given on standard input (in native format, not wire format) using the standard rules of the storage subsystem. If the article is stored successfully, the token of the article is printed to standard output. Please note that this does not make any attempt to write a history entry or any overview data, and is therefore only useful under very specific circumstances.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Show a clear, decoded form of the storage <font SIZE="-1">API</font> token. Each part of the token is explained, in a human-readable string. Amongst other elements, this command gives the path to where the corresponding article is supposed to be stored.</p>
<dt><code>-d</code>, <code>-r</code></p>
<dd> Rather than retrieving the specified article, remove the article. This will delete the article out of the news spool and it will not subsequently be retrievable by any part of <font SIZE="-1">INN</font>. It&#8217;s equivalent to <tt>&quot;ctlinnd cancel&quot;</tt> except it takes a storage <font SIZE="-1">API</font> token instead of a message-ID.</p>
<dt><code>-H</code></p>
<dd> Retrieve only the headers of the article rather than the entire article. This option cannot be used with <code>-d</code>, <code>-r</code>, <code>-i</code>, or <code>-S</code>.</p>
<dt><code>-i</code></p>
<dd> Show the newsgroup name and article number associated with the token rather than the article itself. Note that for crossposted articles, only the first newsgroup and article number to which the article is associated will be returned.</p>
<dt><code>-q</code></p>
<dd> Suppress all error messages except usage errors.</p>
<dt><code>-R</code></p>
<dd> Display the raw article. This means that line endings won&#8217;t be converted to native line endings and will be left as <font SIZE="-1">CRLF</font> sequences; leading periods will still be escaped for sending over <font SIZE="-1">NNTP</font>, and the article will end in a <font SIZE="-1">CRLF</font>.CRLF sequence.</p>
<dt><code>-S</code></p>
<dd> Write the article to standard output in the format used by <code>rnews</code> spool files. Multiple articles can be written in this format, and the resulting output can be fed to <code>rnews</code> (on another system, for example) to inject those articles into <font SIZE="-1">INN</font>. This option cannot be used with <code>-d</code>, <code>-r</code>, <code>-H</code>, <code>-i</code>, or <code>-R</code>.</p>
<dt><code>-s</code></p>
<dd> Store the article given on standard input using the normal storage rules for articles as configured in <i><a href="/docs/linux/man/5-storage-conf/">storage.conf</a></i>(5). Print the new token for the message to standard output if it is stored successfully. If this option is given, no other options except possibly <code>-q</code> should be given.</dl>
<h2>EXIT STATUS</h2>
<p> If all operations were successful, <code>sm</code> exits with status 0. If an operation on any of the provided tokens fails, <code>sm</code> will exit with status 1, even if the operations on other tokens were successful. In other words, if twenty tokens are fed to <tt>&quot;sm -r&quot;</tt> on stdin, 19 articles were successfully removed, but the sixth article couldn&#8217;t be found, <code>sm</code> will still exit with status 1. </p>
<p> This means that if you need to be sure whether a particular operation succeeded, you should run <code>sm</code> on one token at a time.</p>
<h2>HISTORY</h2>
<p> Written by Katsuhiro Kondou &lt;kondou [at] nec.co.jp&gt; for InterNetNews. Rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> sm.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/1-grephistory/">grephistory</a></i>(1), <i><a href="/docs/linux/man/5-history/">history</a></i>(5), <i><a href="/docs/linux/man/1-rnews/">rnews</a></i>(1), <i><a href="/docs/linux/man/5-storage-conf/">storage.conf</a></i>(5). </p>
<h2>Index</h2>
