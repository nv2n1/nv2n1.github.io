---
title: "zstdgrep(1)"
name: "zstdgrep"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zstdgrep/"
description: "zstdgrep – print lines matching a pattern in zstandard-compressed files"
---

<h2 class="name">NAME</h2>
<p> <code>zstdgrep</code> &#8211; print lines matching a pattern in zstandard-compressed files </p>
<h2>SYNOPSIS</h2>
<p> <code>zstdgrep</code> [<i>grep-flags</i>] [&#8211;] <i>pattern</i> [<i>files</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>zstdgrep</code> runs <code>grep (1)</code> on files or stdin, if no files argument is given, after decompressing them with <code>zstdcat (1)</code>. </p>
<p> The grep-flags and pattern arguments are passed on to <code>grep (1)</code>. If an <code>-e</code> flag is found in the <code>grep-flags</code>, <code>zstdgrep</code> will not look for a pattern argument.</p>
<h2>EXIT STATUS</h2>
<p> In case of missing arguments or missing pattern, 1 will be returned, otherwise 0.</p>
<h2>SEE ALSO</h2>
<p> <code>zstd (1)</code></p>
<h2>AUTHORS</h2>
<p> Thomas Klausner <i>wiz [at] NetBSD.org</i> </p>
<h2>Index</h2>
