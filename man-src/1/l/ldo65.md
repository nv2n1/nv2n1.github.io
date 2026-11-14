---
title: "ldo65(1)"
name: "ldo65"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldo65/"
description: "ldo65 – linker for o65 object files"
---

<h2 class="name">NAME</h2>
<p> ldo65 &#8211; linker for o65 object files</p>
<h2>SYNOPSIS</h2>
<p> <code>ldo65</code> [<i>OPTION</i>]&#8230; <i>FILE</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>ldo65</code> is a linker for files in the `o65&#8242; object format, formerly <code>ld65</code> but renamed to avoid conflicts with the <code>cc65</code> package (a separate product). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b? addr</code></p>
<dd> Relocate segment <code>?</code> to <code>addr</code>. <code>?</code> must be either t, d, b or z to indicate the text, data, bss or zero segment respectively. See the <code><a href="/docs/linux/man/1-xa/">xa</a></code>(1) man page for an explanation.</p>
<dt><code>-o filename</code></p>
<dd> Set output filename. The default is <code>a.o65</code>.</p>
<dt><code>-G</code></p>
<dd> Suppress writing of globals.</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of program. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-file65/">file65</a></code>(1), <code><a href="/docs/linux/man/1-printcbm/">printcbm</a></code>(1), <code><a href="/docs/linux/man/1-reloc65/">reloc65</a></code>(1), <code><a href="/docs/linux/man/1-uncpk/">uncpk</a></code>(1), <code><a href="/docs/linux/man/1-dxa/">dxa</a></code>(1), <code><a href="/docs/linux/man/1-xa/">xa</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by David Weinehall &lt;tao [at] acc.umu.se&gt; and Cameron Kaiser &lt;ckaiser [at] floodgap.com&gt;. Original xa package (C)1989-1997 Andre Fachat. Additional changes (C)1989-2006 Andre Fachat, Jolse Maginnis, David Weinehall and Cameron Kaiser. The current maintainer is Cameron Kaiser. </p>
<h2>WEBSITE</h2>
<p> <a rel="nofollow" href="http://www.floodgap.com/retrotech/xa/">http://www.floodgap.com/retrotech/xa/</a> </p>
<h2>Index</h2>
