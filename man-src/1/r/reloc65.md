---
title: "reloc65(1)"
name: "reloc65"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reloc65/"
description: "reloc65 – relocator for o65 object files"
---

<h2 class="name">NAME</h2>
<p> reloc65 &#8211; relocator for o65 object files</p>
<h2>SYNOPSIS</h2>
<p> <code>reloc65</code> [<i>OPTION</i>]&#8230; <i>FILE</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>reloc65</code> is a relocator for files in the <code>o65</code> object format. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o filename</code></p>
<dd> Set output filename. The default is <code>a.o65</code>.</p>
<dt><code>-b? addr</code></p>
<dd> Relocate segment <code>?</code> to <code>addr</code>. <code>?</code> should be t, d, b or z to represent the text, data, bss or zero segment respectively. See the <code><a href="/docs/linux/man/1-xa/">xa</a></code>(1) man page for an explanation.</p>
<dt><code>-x? </code></p>
<dd> Extract segment <code>?</code> from the file instead of writing back the whole file. Valid arguments are t and d for the text or data segment respectively. Not valid for bss or zero.</p>
<dt><code>-X </code></p>
<dd> Extract text and data segment together from the file instead of writing back the whole file. Relocating data segment to the end of the text segment (ignoring the -xd option) before extracting.</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of program. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-file65/">file65</a></code>(1), <code><a href="/docs/linux/man/1-ldo65/">ldo65</a></code>(1), <code><a href="/docs/linux/man/1-printcbm/">printcbm</a></code>(1), <code><a href="/docs/linux/man/1-uncpk/">uncpk</a></code>(1), <code><a href="/docs/linux/man/1-dxa/">dxa</a></code>(1), <code><a href="/docs/linux/man/1-xa/">xa</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by David Weinehall &lt;tao [at] acc.umu.se&gt; and Cameron Kaiser &lt;ckaiser [at] floodgap.com&gt;. Original xa package (C)1989-1997 Andre Fachat. Additional changes (C)1989-2006 Andre Fachat, Jolse Maginnis, David Weinehall and Cameron Kaiser. The current maintainer is Cameron Kaiser. </p>
<h2>WEBSITE</h2>
<p> <a rel="nofollow" href="http://www.floodgap.com/retrotech/xa/">http://www.floodgap.com/retrotech/xa/</a> </p>
<h2>Index</h2>
