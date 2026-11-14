---
title: "heif-convert(1)"
name: "heif-convert"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heif-convert/"
description: "heif-convert – convert HEIC/HEIF image"
---

<h2 class="name">NAME</h2>
<p> heif-convert &#8211; convert HEIC/HEIF image </p>
<h2>SYNOPSIS</h2>
<p> <code>heif-convert</code> [<code>-q</code> <i>QUALITY</i>] <i>filename</i> <i>output[.jpg|.png|.y4m]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>heif-convert</code> Convert HEIC/HEIF image to a different image format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q</code>&nbsp;<i>QUALITY</i></p>
<dd> Defines quality level between 0 and 100 for the generated output file.</dl>
<h2>EXIT STATUS</h2>
<p> <code>0</code></p>
<dl>
<dt>
<dd> Success</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Failure (syntax or usage error; error while loading, converting or writing image).</dl>
<h2>NOTES</h2>
<p> The available output formats depend on the libraries that were available at compile time. Supported are JPEG, PNG and Y4M, the file type is determined based on the extension of the output file.</p>
<h2>BUGS</h2>
<p> Please reports bugs or issues at <a rel="nofollow" href="https://github.com/strukturag/libheif">https://github.com/strukturag/libheif</a></p>
<h2>AUTHORS</h2>
<p> Joachim Bauch, struktur AG<br />
 Dirk Farin, struktur AG</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2017 struktur AG </p>
<h2>Index</h2>
