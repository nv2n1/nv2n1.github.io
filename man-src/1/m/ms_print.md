---
title: "ms_print(1)"
name: "ms_print"
section: "1"
letter: "m"
url: "/docs/linux/man/1-ms_print/"
description: "ms_print – post-processing tool for Massif"
---

<h2 class="name">NAME</h2>
<p> ms_print &#8211; post-processing tool for Massif </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ms_print</code> [<i>options</i>] <i>massif-out-file</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>ms_print</code></p>
<dd>takes an output file produced by the Valgrind tool Massif and prints the information in an easy-to-read form.</p>
<h2>OPTIONS</h2>
<p> <code>-h &#8211;help </code></p>
<dl>
<dt>
<dd> Show the help message.</dl>
<p> <code>&#8211;version </code></p>
<dl>
<dt>
<dd> Show the version number.</dl>
<p> <code>&#8211;threshold=&lt;m.n&gt; [default: 1.0] </code></p>
<dl>
<dt>
<dd> Same as Massif&#8217;s <code>&#8211;threshold</code> option, but applied after profiling rather than during.</dl>
<p> <code>&#8211;x=&lt;4..1000&gt; [default: 72]</code></p>
<dl>
<dt>
<dd> Width of the graph, in columns.</dl>
<p> <code>&#8211;y=&lt;4..1000&gt; [default: 20] </code></p>
<dl>
<dt>
<dd> Height of the graph, in rows.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-valgrind/">valgrind</a>(1), $INSTALL/share/doc/valgrind/html/index.html or <a rel="nofollow" href="http://www.valgrind.org/docs/manual/index.html.">http://www.valgrind.org/docs/manual/index.html.</a></p>
<h2>AUTHOR</h2>
<p> Nicholas Nethercote. </p>
<h2>Index</h2>
