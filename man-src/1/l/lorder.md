---
title: "lorder(1)"
name: "lorder"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lorder/"
description: "lorder – list dependencies for object files"
---

<h2 class="name">NAME</h2>
<p> <code>lorder</code> &#8211; list dependencies for object files </p>
<h2>SYNOPSIS</h2>
<p> <i>file &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> The utility uses <a href="/docs/linux/man/1-nm/">nm</a>(1) to determine interdependencies in the list of object files and library archives specified on the command line. The utility outputs a list of file names where the first file contains a symbol which is defined by the second file. </p>
<p> The output is normally used with <a href="/docs/linux/man/1-tsort/">tsort</a>(1) when a library is created to determine the optimum ordering of the object modules so that all references may be resolved in a single pass of the loader. </p>
<p> When linking static binaries, and <a href="/docs/linux/man/1-tsort/">tsort</a>(1) can be used to properly order library archives automatically.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>NM</code></p>
<dd> Path to the <a href="/docs/linux/man/1-nm/">nm</a>(1) binary, defaults to &#8220;<code>nm</code> &#8221;</p>
<dt><code>NMFLAGS</code></p>
<dd> Flags to pass to <a href="/docs/linux/man/1-nm/">nm</a>(1).</dl>
<h2>EXAMPLES</h2>
<blockquote>
<pre><code>
ar cr library.a `lorder ${OBJS} | tsort` cc - o foo $
{
    OBJS
}
`lorder ${STATIC_LIBS} | tsort`
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ar/">ar</a>(1), <a href="/docs/linux/man/1-ld/">ld</a>(1), <a href="/docs/linux/man/1-nm/">nm</a>(1), <a href="/docs/linux/man/1-ranlib/">ranlib</a>(1), <a href="/docs/linux/man/1-tsort/">tsort</a>(1)</p>
<h2>HISTORY</h2>
<p> A utility appeared in AT&amp;T System v7 . </p>
<h2>Index</h2>
