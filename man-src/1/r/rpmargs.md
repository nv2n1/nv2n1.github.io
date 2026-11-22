---

title: "rpmargs(1)"
name: "rpmargs"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmargs/"
description: "rpmargs – process RPM packages"
---

<p> rpmargs &#8211; process RPM packages </p>
<h2>SYNOPSIS</h2>
<p> <code>rpmargs</code> [<code>-h</code>] <code>-c</code> <i>command</i> [<code>-a</code>] [<code>-p</code>] [<i></i><i>FILE</i><i></i>&#8230;] [<i></i><i>DIR</i><i></i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>rpmargs</code> executes a <i>command</i> against each RPM package given on the command line. Extra word splitting is performed on the <i>command</i>. Each <i></i><i>FILE</i><i></i> is treated as RPM package. Each <i></i><i>DIR</i><i></i> is processed with <tt>&quot;*.rpm&quot;</tt> pattern, and RPM file basename is prepended to the <i>command</i> output.</p>
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
<p> This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
