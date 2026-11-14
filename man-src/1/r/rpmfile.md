---
title: "rpmfile(1)"
name: "rpmfile"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmfile/"
description: "rpmfile – list file modes and types in RPM packages"
---

<h2 class="name">NAME</h2>
<p> rpmfile &#8211; list file modes and types in RPM packages </p>
<h2>SYNOPSIS</h2>
<p> <code>rpmfile</code> [<code>-h</code>] [<code>-a</code>] [<code>-p</code>] [<i></i><font SIZE="-1"><i>FILE</i></font><i></i>&#8230;] [<i></i><font SIZE="-1"><i>DIR</i></font><i></i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>rpmfile</code> produces three-column output: file name, file mode (octal), and file type, as determined by <i><a href="/docs/linux/man/1-file/">file</a></i>(1). When processing a directory, an additional column is prepended to the output, which is typically <font SIZE="-1">RPM</font> file basename.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Process all Sisyphus packages.</p>
<dt><code>-p</code></p>
<dd> When processing a directory, list package names, not file names; furthermore, enable special treatment of packages with the same name; that is, process only the one with the latest version.</p>
<dt><code>-h</code></p>
<dd> Display this help and exit.</dl>
<h2>AUTHOR</h2>
<p> Written by Alexey Tourbin &lt;at [at] altlinux.org&gt;.</p>
<h2>COPYING</h2>
<p> Copyright (c) 2005 Alexey Tourbin, <font SIZE="-1">ALT</font> Linux Team. </p>
<p> This is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rpmargs/">rpmargs</a></i>(1), <i><a href="/docs/linux/man/8-rpm/">rpm</a></i>(8), <i><a href="/docs/linux/man/8-rpm2cpio/">rpm2cpio</a></i>(8), <i><a href="/docs/linux/man/1-file/">file</a></i>(1) </p>
<h2>Index</h2>
