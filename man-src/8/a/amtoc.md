---
title: "amtoc(8)"
name: "amtoc"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amtoc/"
description: "amtoc – generate TOC (Table Of Contents) for an Amanda run"
---

<p>amtoc &#8211; generate TOC (Table Of Contents) for an Amanda run</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amtoc</code> [-a] [-i] [-t] [-f&nbsp;<wbr><i>file</i>] [-s&nbsp;<wbr><i>subs</i>] [-w] [&#8211;] <i>logfile</i></dl>
<h2>Description</h2>
<p><i>Amtoc</i></p>
<dd>generates a table of contents for an Amanda run. It&#8217;s a perl script (if you don&#8217;t have perl, install it first!).</p>
<h2>Options</h2>
<p><code>-a</code></p>
<dl>
<dd>The output file name will be <i>label-of-the-tape</i>.toc in the same directory as <i>logfile</i>.</dl>
<p> <code>-i</code></p>
<dl>
<dd>Display help about <code>amtoc</code>.</dl>
<p> <code>-t</code></p>
<dl>
<dd>Generate the output in tabular form.</dl>
<p> <code>-f file</code></p>
<dl>
<dd>Write the output to a file (&#8216;-&#8216; for stdout).</dl>
<p> <code>-s subs</code></p>
<dl>
<dd>Evaluate the output file name from <i>subs</i>, with $_ set to <i>label-of-the-tape</i>. The <code>-a</code> option is equivalent to <code>-s</code> <i>&#8216;s/$_/.toc/&#8217;</i>.</dl>
<p> <code>-w</code></p>
<dl>
<dd>Separate tapes with form-feeds and display blank lines before totals.</dl>
<p> <code>&#8212;</code></p>
<dl>
<dd>Marks the last option so the next parameter is the <i>logfile</i>.</dl>
<p> <code>logfile</code></p>
<dl>
<dd>(use &#8216;-&#8216; for stdin)</dl>
<h2>Output Format</h2>
<p>The standard output has five fields separated by two spaces: </p>
<pre># Server:/partition date level size[Kb]
0 daily-05: 19991005 - -
1 cuisun15:/cuisun15/home 19991005 1 96
2 cuinfs:/export/dentiste 19991005 1 96
 ...
103 cuisg11:/ 19991005 0 4139136
103 total: - - 16716288</pre>
<p>In tabular format (-t), this would look like: </p>
<pre> # Server:/partition date lev size[Kb]
 0 daily-05: 19991005 - -
 1 cuisun15:/cuisun15/home 19991005 1 96
 2 cuinfs:/export/dentiste 19991005 1 96
 ...
103 cuisg11:/ 19991005 0 4139136
103 total: - - 16716288</pre>
<h2>Usage</h2>
<p>The easiest way to use it is to run <code>amtoc</code> right after <i>amdump</i> in the <i>cron job:</i> </p>
<pre>amdump daily ; logdir=`amgetconf daily logdir` ; log=`ls -1t $logdir/log.*.[0-9] | head -1` ; amtoc -a $log</pre>
<p>which will generate /usr/local/etc/amanda//daily/<i>tape_label</i>.toc. You may also want to call <code>amtoc</code> after an <i>amflush</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8), <code><a href="/docs/linux/man/8-amflush/">amflush</a></code>(8), <code><a href="/docs/linux/man/8-amgetconf/">amgetconf</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Nicolas Mayencourt</code> &lt;Nicolas.Mayencourt [at] cui.unige.ch&gt;</p>
<dl>
<dd>University of Geneva/Switzerland</dl>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
