---
title: "rnews(1)"
name: "rnews"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rnews/"
description: "rnews – Inject individual articles and UUCP batches into INN"
---

<h2 class="name">NAME</h2>
<p> rnews &#8211; Inject individual articles and UUCP batches into INN </p>
<h2>SYNOPSIS</h2>
<p> <code>rnews</code> [<code>-NUv</code>] [<code>-h</code> <i>host</i>] [<code>-P</code> <i>port</i>] [<code>-rS</code> <i>server</i>] [<i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>rnews</code> injects either individual articles or UUCP-style article batches into an <font SIZE="-1">INN</font> server. It submits articles via <font SIZE="-1">IHAVE</font> and is suitable for injecting articles received from other sources; local postings should generally use <i><a href="/docs/linux/man/1-inews/">inews</a></i>(1) instead. It is also used to process spooled messages created by, for example, <code>nnrpd</code> while <code>innd</code> is not available. </p>
<p> The message is read from <i>file</i> if given, or standard input if no file is given. Articles are sent to the server given in the <code>-r</code> or <code>-S</code> command line options if given, otherwise to the server set via <i>nnrpdposthost</i> in <i>inn.conf</i>, otherwise to the local server. </p>
<p> When sent over <font SIZE="-1">UUCP</font>, Usenet articles are typically collected in a single batch to reduce the <font SIZE="-1">UUCP</font> overhead. Batches can also be compressed to reduce communication time. If the input to <code>rnews</code> does not begin with the characters <tt>&quot;#!&quot;</tt>, it is taken to be a single news article; otherwise, the first line of the input is interpreted as a batch command. </p>
<p> If the batch command is: </p>
<pre>
    #! rnews &lt;number&gt;
</pre>
<p> then the next &lt;number&gt; bytes (starting with the next line) are read as a news article. After that article is processed, the next line is again treated as a batch command. </p>
<p> If the command is: </p>
<pre>
    #! cunbatch
</pre>
<p> then the rest of the input is fed to <tt>&quot;gzip -d&quot;</tt> to uncompress it, and then the resulting uncompressed output is re-read as if it were the original input to <code>rnews</code>. A compressed batch should therefore start with this line and contain a batch of articles separated by <tt>&quot;#!&nbsp;<wbr>rnews&quot;</tt> lines and then compressed with <i><a href="/docs/linux/man/1-compress/">compress</a></i>(1). (Batches compressed with <i><a href="/docs/linux/man/1-gzip/">gzip</a></i>(1) should instead use <tt>&quot;gunbatch&quot;</tt> as the batch command; <font SIZE="-1">INN</font> just uses <code>gzip</code> rather than <code>compress</code> because it can handle <code>compress</code>-style compression but is more widely available, due to old patent issues, than <code>compress</code>.) </p>
<p> Otherwise, if the command is any other word, then <code>rnews</code> will try to execute a program with that name, looking for it in the directory <i>pathbin</i>/rnews.libexec. The rest of the batch will be fed to that program&#8217;s standard input, and the standard output from the program will be treated as if it were the original input to <code>rnews</code>. <font SIZE="-1">INN</font> comes with three such standard batch processors:</p>
<dl>
<dt><code>bunbatch</code></p>
<dd> It invokes <code>bzip2</code> and should be used for batches compressed with <code>bzip2</code>.</p>
<dt><code>c7unbatch</code></p>
<dd> It undoes an <font SIZE="-1">ASCII</font> encoding to recover the original binary compressed stream and then decompresses it as explained above.</p>
<dt><code>gunbatch</code></p>
<dd> It invokes <code>gzip</code> and should be used for batches compressed with <code>gzip</code>.</dl>
<p> By default, <code>rnews</code> will log and discard any articles that are rejected by the server or cannot be parsed by <code>rnews</code> for some reason (such as a missing header). This default can be changed when compiling <font SIZE="-1">INN</font> by setting <font SIZE="-1">DO_RNEWS_SAVE_BAD</font> in <i>include/inn/options.h</i>. There is no way to change it at runtime, unfortunately.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> <i>host</i></p>
<dd> If <code>-h</code> is given, <code>rnews</code> will log the message <font SIZE="-1">ID</font> and <i>host</i> via syslog for each article that it offers to the server. This is used in conjunction with a <font SIZE="-1">UUCP</font> feed to get a log of the messages received via that feed. This will also be done if the environment variable <font SIZE="-1">UU_MACHINE</font> is set, but will only be done if <i>host</i> is not an empty string. (You can therefore turn off logging even if <font SIZE="-1">UU_MACHINE</font> will be set by passing the flag <tt>&quot;-h ''&quot;</tt> to <code>rnews</code>.)</p>
<dt><code>-N</code></p>
<dd> Normally, if unpacking the input batch fails, it is re-spooled to <i>pathincoming</i> for another attempt later. If the <code>-N</code> flag is given, no such re-spooling is done and <code>rnews</code> will instead exit with status 9 if unpacking fails.</p>
<dt><code>-P</code> <i>port</i></p>
<dd> Use <i>port</i> as the server port to connect to rather than <i>nnrpdpostport</i> (as set in <i>inn.conf</i>). Note that this value is only used if <code>rnews</code> does not connect to the local server (in other words, when <code>-r</code> or <code>-S</code> is given or <i>nnrpdposthost</i> is set).</p>
<dt><code>-r</code> <i>server</i>, <code>-S</code> <i>server</i></p>
<dd> <code>-r</code> and <code>-S</code> are synonymous. If either is given, articles will be sent to <i>server</i> rather than using the local server, overriding also the setting of <i>nnrpdposthost</i> in <i>inn.conf</i>.</p>
<dt><code>-U</code></p>
<dd> If the server is not available, both <code>rnews</code> and <code>nnrpd</code> will spool posts to new files in the <i>pathincoming</i> directory (as specified in <i>inn.conf</i>). When <code>rnews</code> is invoked with the <code>-U</code> option, it scans that directory and processes all spooled messages found there whose filenames do not begin with <tt>&quot;.&quot;</tt>, attempting to send them to the server again. It&#8217;s a good idea to run this periodically out of cron to pick up any articles spooled due to temporary server unavailability.</dl>
<h2>BUGS</h2>
<p> <code>rnews</code> cannot process articles that have embedded nul characters in them. (Neither can the rest of <font SIZE="-1">INN</font> at present.)</p>
<h2>HISTORY</h2>
<p> Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> rnews.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-bzip2/">bzip2</a></i>(1), <i><a href="/docs/linux/man/1-compress/">compress</a></i>(1), <i><a href="/docs/linux/man/1-gzip/">gzip</a></i>(1), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8). </p>
<h2>Index</h2>
