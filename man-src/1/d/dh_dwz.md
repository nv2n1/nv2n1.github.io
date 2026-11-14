---
title: "dh_dwz(1)"
name: "dh_dwz"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_dwz/"
description: "dh_dwz – optimize DWARF debug information in ELF binaries via dwz"
---

<h2 class="name">NAME</h2>
<p> dh_dwz &#8211; optimize DWARF debug information in ELF binaries via dwz </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_dwz</code> [<i>debhelper options</i>] [<code>-X</code><i>item</i>] [<code>&#8212;</code> <i>params</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Caveat</code>: This tool is experimental and may disappear or change behaviour without any notice. </p>
<p> <code>dh_dwz</code> is a debhelper program that will optimize the (uncompressed) size of the <font SIZE="-1">DWARF</font> debug information in <font SIZE="-1">ELF</font> binaries. It does so by running <i><a href="/docs/linux/man/1-dwz/">dwz</a></i>(1) on all the <font SIZE="-1">ELF</font> binaries in the package.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain <i>item</i> anywhere in their filename from being stripped. You may use this option multiple times to build up a list of things to exclude.</p>
<dt><code>&#8212;</code> <i>params</i></p>
<dd> Pass <i>params</i> to <i><a href="/docs/linux/man/1-dwz/">dwz</a></i>(1) when it processes <font SIZE="-1">ELF</font> binaries. This is mostly useful for setting memory related parameters (e.g. -l and -L).</dl>
<h2>NOTES</h2>
<p> If the <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> environment variable contains <code>nostrip</code>, nothing will be stripped, in accordance with Debian policy (section 10.1 &#8220;Binaries&#8221;). </p>
<p> While this tool technically does not remove debug information from binaries, it is still skipped when the <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> environment variable contains <code>nostrip</code>. This is because <code>nostrip</code> is often used to optimize build times (e.g. for &#8220;build and test&#8221;-cycles) rather than optimizing for size.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Niels Thykier &lt;niels [at] thykier.net&gt; </p>
<h2>Index</h2>
