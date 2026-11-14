---
title: "uncpk(1)"
name: "uncpk"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uncpk/"
description: "uncpk – manage c64 cpk archives"
---

<h2 class="name">NAME</h2>
<p> uncpk &#8211; manage c64 cpk archives</p>
<h2>SYNOPSIS</h2>
<p> <code>uncpk</code> [<i>OPTION</i>]&#8230; <i>FILE</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>uncpk</code> is an archive tool for Commodore 64 .cpk-format archives. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>c</code></p>
<dd> Create an archive.</p>
<dt><code>x</code></p>
<dd> Extract from an archive.</p>
<dt><code>l</code></p>
<dd> List contents of archive.</p>
<dt><code>a</code></p>
<dd> Add a file to the archive.</p>
<dt><code>v</code></p>
<dd> Verbose output.</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of program. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>uncpk c foo.cpk bar</code></p>
<dd> Create archive <code>foo.cpk</code> with the single file <code>bar</code> inside it.</p>
<dt><code>uncpk a foo.cpk bar</code></p>
<dd> Add file <code>bar</code> to archive <code>foo.cpk</code> (which must already exist).</p>
<dt><code>uncpk x foo.cpk</code></p>
<dd> Extract all files from archive <code>foo.cpk</code>.</p>
<dt><code>uncpk l foo.cpk</code></p>
<dd> List contents of archive <code>foo.cpk</code>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-file65/">file65</a></code>(1), <code><a href="/docs/linux/man/1-ldo65/">ldo65</a></code>(1), <code><a href="/docs/linux/man/1-printcbm/">printcbm</a></code>(1), <code><a href="/docs/linux/man/1-reloc65/">reloc65</a></code>(1), <code><a href="/docs/linux/man/1-dxa/">dxa</a></code>(1), <code><a href="/docs/linux/man/1-xa/">xa</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by David Weinehall &lt;tao [at] acc.umu.se&gt; and Cameron Kaiser &lt;ckaiser [at] floodgap.com&gt;. Original xa package (C)1989-1997 Andre Fachat. Additional changes (C)1989-2006 Andre Fachat, Jolse Maginnis, David Weinehall and Cameron Kaiser. The current maintainer is Cameron Kaiser. </p>
<h2>WEBSITE</h2>
<p> <a rel="nofollow" href="http://www.floodgap.com/retrotech/xa/">http://www.floodgap.com/retrotech/xa/</a> </p>
<h2>Index</h2>
