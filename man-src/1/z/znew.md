---
title: "znew(1)"
name: "znew"
section: "1"
letter: "z"
url: "/docs/linux/man/1-znew/"
description: "znew – recompress .Z files to .gz files"
---

<h2 class="name">NAME</h2>
<p> znew &#8211; recompress .Z files to .gz files </p>
<h2>SYNOPSIS</h2>
<p> <code>znew</code> [ -ftv9PK] [ name.Z &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Znew</i> recompresses files from .Z (compress) format to .gz (gzip) format. If you want to recompress a file already in gzip format, rename the file to force a .Z extension then apply znew.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Force recompression from .Z to .gz format even if a .gz file already exists.</p>
<dt><code>-t</code></p>
<dd> Tests the new files before deleting originals.</p>
<dt><code>-v</code></p>
<dd> Verbose. Display the name and percentage reduction for each file compressed.</p>
<dt><code>-9</code></p>
<dd> Use the slowest compression method (optimal compression).</p>
<dt><code>-P</code></p>
<dd> Use pipes for the conversion to reduce disk space usage.</p>
<dt><code>-K</code></p>
<dd> Keep a .Z file when it is smaller than the .gz file; implies <code>-t</code>.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gzip/">gzip</a>(1), <a href="/docs/linux/man/1-zmore/">zmore</a>(1), <a href="/docs/linux/man/1-zdiff/">zdiff</a>(1), <a href="/docs/linux/man/1-zgrep/">zgrep</a>(1), <a href="/docs/linux/man/1-zforce/">zforce</a>(1), <a href="/docs/linux/man/1-gzexe/">gzexe</a>(1), <a href="/docs/linux/man/1-compress/">compress</a>(1)</p>
<h2>BUGS</h2>
<p> If the <code>-P</code> option is used, <i>znew</i> does not maintain the timestamp if <i><a href="/docs/linux/man/1-touch/">touch</a></i>(1) does not support the <code>-r</code> option, and does not maintain permissions if <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1) does not support the <code>&#8211;reference</code> option. </p>
<h2>Index</h2>
