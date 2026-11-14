---
title: "shtool-move(1)"
name: "shtool-move"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-move/"
description: "shtool move – GNU shtool enhanced"
---

<h2 class="name">NAME</h2>
<p> shtool move &#8211; GNU shtool enhanced </p>
<p><a href="/docs/linux/man/1-mv/">mv</a>(1) replacement</p>
<h2>SYNOPSIS</h2>
<p> <code>shtool move</code> [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-t</code>|<code>&#8211;trace</code>] [<code>-e</code>|<code>&#8211;expand</code>] [<code>-p</code>|<code>&#8211;preserve</code>] <i>src-file</i> <i>dst-file</i></p>
<h2>DESCRIPTION</h2>
<p> This is a <i><a href="/docs/linux/man/1-mv/">mv</a></i>(1) style command enhanced with the ability to rename multiple files in a single operation and the ability to detect and not touch existing equal destinations files, thus preserving timestamps.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display some processing information.</p>
<dt><code>-t</code>, <code>&#8211;trace</code></p>
<dd> Enable the output of the essential shell commands which are executed.</p>
<dt><code>-e</code>, <code>&#8211;expand</code></p>
<dd> Expand asterisk in <i>src</i> to be used as &quot;<tt>&quot;%&quot;</tt><i>n</i>&quot; (where <i>n</i> is <tt>1</tt>,<tt>2</tt>,&#8230;) in <i>dst-file</i>. This is useful for renaming multiple files at once.</p>
<dt><code>-p</code>, <code>&#8211;preserve</code></p>
<dd> Detect <i>src-file</i> and <i>dst-file</i> having equal content and not touch existing destination files, thus perserving timestamps. This is useful for applications that monitor timestamps, i.e. suppress <a href="//www.systutorials.com/docs/linux/man/1L-make/">make</a>(1L) repeating actions for unchanged files.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   shell script
 shtool move -v -e '*.txt' %1.asc
 #   Makefile
 scanner.c: scanner.l
     lex scanner.l
     shtool move -t -p lex.yy.c scanner.c
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>move</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1999 for <font SIZE="-1"><code>GNU</code></font><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-mv/">mv</a></i>(1), <i><a href="/docs/linux/man/1-make/">make</a></i>(1). </p>
<h2>Index</h2>
