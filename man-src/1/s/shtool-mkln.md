---
title: "shtool-mkln(1)"
name: "shtool-mkln"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-mkln/"
description: "shtool mkln – GNU shtool enhanced"
---

<h2 class="name">NAME</h2>
<p> shtool mkln &#8211; GNU shtool enhanced </p>
<p><a href="/docs/linux/man/1-ln/">ln</a>(1) replacement</p>
<h2>SYNOPSIS</h2>
<p> <code>shtool mkln</code> [<code>-t</code>|<code>&#8211;trace</code>] [<code>-f</code>|<code>&#8211;force</code>] [<code>-s</code>|<code>&#8211;symbolic</code>] <i>src-path</i> [<i>src-path</i> &#8230;] <i>dst-path</i></p>
<h2>DESCRIPTION</h2>
<p> This is a <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1) style command. It is enhanced to provide automatic calculation and usage of relative links with the shortest possible path, if possible. Usually if <i>src-path</i> and <i>dst-path</i> are not absolute paths or at least they share a common prefix except the root directory (&#8220;<tt>&quot;/&quot;</tt>&#8221;). When more than one <i>src-path</i> is specified, all of them are linked into <i>dst-path</i>.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-t</code>, <code>&#8211;trace</code></p>
<dd> Enable the output of the essential shell commands which are executed.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Force the creation of the link even if it exists. Default is to fail with error.</p>
<dt><code>-s</code>, <code>&#8211;symbolic</code></p>
<dd> Create a symbolic link instead of a hard-link.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   shell script
 shtool mkln -s foo/bar baz/quux
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>fixperm</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1998 for <i>ePerl</i>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1). </p>
<h2>Index</h2>
