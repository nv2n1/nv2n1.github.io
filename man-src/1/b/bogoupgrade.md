---
title: "bogoupgrade(1)"
name: "bogoupgrade"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bogoupgrade/"
description: "bogoupgrade – upgrades bogofilter database to current version"
---

<h2 class="name">NAME</h2>
<p> bogoupgrade &#8211; upgrades bogofilter database to current version </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bogoupgrade</code> [-h] -d&nbsp;<wbr><i>directory</i> [-i&nbsp;<wbr><i>input file</i>] [-o&nbsp;<wbr><i>output file</i>] [-b&nbsp;<wbr><i>path to bogoutil</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>bogoupgrade</code></p>
<dd>is a command to upgrade bogofilter&#8217;s databases from an old format to the current format. Since the format of the database changes once in a while, the utility is designed to make the upgrade easy.</p>
<h2>OPTIONS</h2>
<p> The <code>-h</code> option prints the help message and exits. </p>
<p> The <code>-d</code> specifies the directory with the wordlists for converting. This option is used when converting from multiple, separate wordlists (spamlist.db and goodlist.db &#8211; containing spam and ham tokens, respectively) to a combined wordlist (wordlist.db) which contains both spam and ham tokens. </p>
<p> The <code>-i</code> specifies the input file to be converted. It should be a text file containing message counts, and possibly data. If there is no data in the text file, there should be a Berkeley DB file in the same directory as the text file which contains the data. </p>
<p> The <code>-o</code> specifies the output Berkeley DB file. </p>
<p> The <code>-b</code> gives the path to the <code>bogoutil</code> command. It defaults to &#8216;bogoutil&#8217;, in the hopes that your shell will find it.</p>
<h2>UPGRADING</h2>
<p> Follow these instructions to upgrade bogofilter&#8217;s databases to the latest version. </p>
<dl>
<dt>
<dd> 1. Stop all instances of bogofilter. While the upgrade tools lock the database files, the upgrade may take a long time if you have a busy site. Don&#8217;t forget to stop cron jobs or daemons that fetch and process mail and could fire off bogofilter.</dl>
<dl>
<dt>
<dd> 2. Backup your data. Let&#8217;s assume that you said: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>mv ~/.bogofilter ~/.bogofilter.safe</code>
$ <code>mkdir ~/.bogofilter</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 3. If your bogofilter version is less than 0.7, say: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>bogoupgrade -i ~/.bogofilter.safe/goodlist -o ~/.bogofilter/goodlist.db</code>
$ <code>bogoupgrade -i ~/.bogofilter.safe/badlist -o ~/.bogofilter/spamlist.db</code>
</pre>
</dl>
<p> If your bogofilter version is 0.7 or greater, say: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>bogoupgrade -i ~/.bogofilter.safe/hamlist.count -o ~/.bogofilter/goodlist.db</code>
$ <code>bogoupgrade -i ~/.bogofilter.safe/spamlist.count -o ~/.bogofilter/spamlist.db</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 4. Current versions of bogofilter use a combined wordlist that holds both spam and non-spam tokens. It is named wordlist.db. If you&#8217;re updating from a version older than 0.14.0 that has separate wordlists (named goodlist.db and spamlist.db), use: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>bogoupgrade -d ~/.bogofilter.safe</code>
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 5. Done. Restart any stopped daemons, cron tasks, etc.</dl>
<h2>AUTHOR</h2>
<p> <code>bogoupgrade</code> was written by Gyepi Sam gyepi [at] praxis-sw.com and David Relson relson [at] osagesoftware.com. </p>
<p> For updates, see m[blue]<code>the bogofilter project page</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bogofilter/">bogofilter</a>(1), <a href="/docs/linux/man/1-bogolexer/">bogolexer</a>(1), <a href="/docs/linux/man/1-bogotune/">bogotune</a>(1), <a href="/docs/linux/man/1-bogoutil/">bogoutil</a>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> the bogofilter project page</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://bogofilter.sourceforge.net/">http://bogofilter.sourceforge.net/</a></dl>
</dl>
<h2>Index</h2>
