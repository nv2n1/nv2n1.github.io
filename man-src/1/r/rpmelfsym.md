---

title: "rpmelfsym(1)"
name: "rpmelfsym"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmelfsym/"
description: "rpmelfsym – list symbols from object files in RPM packages"
---

<p> rpmelfsym &#8211; list symbols from object files in RPM packages </p>
<h2>SYNOPSIS</h2>
<p> <code>rpmelfsym</code> [<code>-h</code>] [<code>-a</code>] [<code>-p</code>] [<i></i><i>FILE</i><i></i>&#8230;] [<i></i><i>DIR</i><i></i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>rpmelfsym</code> produces three-column output: file name, symbol type, and symbol name, as determined by <i><a href="/docs/linux/man/1-nm/">nm</a></i>(1). Only dynamically linked executable files and shared libraries are processed, and only dynamic symbols are listed. When processing a directory, an additional column is prepended to the output, which is typically RPM file basename.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd> Process all Sisyphus packages.</dd>
<dt><code>-p</code></dt>
<dd> When processing a directory, list package names, not file names; furthermore, enable special treatment of packages with the same name; that is, process only the one with the latest version.</dd>
<dt><code>-h</code></dt>
<dd> Display this help and exit.</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Alexey Tourbin &lt;at [at] altlinux.org&gt;.</p>
<h2>COPYING</h2>
<p> Copyright (c) 2005 Alexey Tourbin, ALT Linux Team. </p>
<p> This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rpmfile/">rpmfile</a></i>(1), <i><a href="/docs/linux/man/1-rpmpeek/">rpmpeek</a></i>(1), <i><a href="/docs/linux/man/1-nm/">nm</a></i>(1) </p>
