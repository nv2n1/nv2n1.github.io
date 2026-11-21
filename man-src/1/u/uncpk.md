---
title: "uncpk(1)"
name: "uncpk"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uncpk/"
description: "uncpk – manage c64 cpk archives"
---

<h2>SYNOPSIS</h2>
<p> <code>uncpk</code> [<i>OPTION</i>]&#8230; <i>FILE</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>uncpk</code> is an archive tool for Commodore 64 .cpk-format archives. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>c</code></dt>
<dd> Create an archive.</dd>
<dt><code>x</code></dt>
<dd> Extract from an archive.</dd>
<dt><code>l</code></dt>
<dd> List contents of archive.</dd>
<dt><code>a</code></dt>
<dd> Add a file to the archive.</dd>
<dt><code>v</code></dt>
<dd> Verbose output.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version of program. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>uncpk c foo.cpk bar</code></dt>
<dd> Create archive <code>foo.cpk</code> with the single file <code>bar</code> inside it.</dd>
<dt><code>uncpk a foo.cpk bar</code></dt>
<dd> Add file <code>bar</code> to archive <code>foo.cpk</code> (which must already exist).</dd>
<dt><code>uncpk x foo.cpk</code></dt>
<dd> Extract all files from archive <code>foo.cpk</code>.</dd>
<dt><code>uncpk l foo.cpk</code></dt>
<dd> List contents of archive <code>foo.cpk</code>. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-file65/">file65</a></code>(1), <code><a href="/docs/linux/man/1-ldo65/">ldo65</a></code>(1), <code><a href="/docs/linux/man/1-printcbm/">printcbm</a></code>(1), <code><a href="/docs/linux/man/1-reloc65/">reloc65</a></code>(1), <code>dxa</code>(1), <code><a href="/docs/linux/man/1-xa/">xa</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by David Weinehall &lt;tao [at] acc.umu.se&gt; and Cameron Kaiser &lt;ckaiser [at] floodgap.com&gt;. Original xa package (C)1989-1997 Andre Fachat. Additional changes (C)1989-2006 Andre Fachat, Jolse Maginnis, David Weinehall and Cameron Kaiser. The current maintainer is Cameron Kaiser. </p>
<h2>WEBSITE</h2>
<p> <a rel="nofollow" href="http://www.floodgap.com/retrotech/xa/">http://www.floodgap.com/retrotech/xa/</a> </p>
