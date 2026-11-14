---
title: "zipcmp(1)"
name: "zipcmp"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zipcmp/"
description: "zipcmp – compare contents of zip archives"
---

<h2>NAME</h2>
<p> zipcmp &#8211; compare contents of zip archives</p>
<h2>SYNOPSIS</h2>
<p> <code>zipcmp</code> [<code>-hiqVv</code>] <code>zip1 zip2</code></p>
<h2>DESCRIPTION</h2>
<p> <code>zipcmp</code> compares the zip archives <code>zip1</code> and <code>zip2</code> and checks if they contain the same files, comparing their names, uncompressed sizes, and CRCs. File order and compressed size differences are ignored. </p>
<p> Supported options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-h</code></p>
<dd> Display a short help message and exit.</p>
<dt><code>-i</code></p>
<dd> Compare names ignoring case distinctions.</p>
<dt><code>-q</code></p>
<dd> Quiet mode. Compare <code>-v</code>.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. Print details about differences to stdout. (This is the default.)</p>
<dt><code>-V</code></p>
<dd> Display version information and exit.</dl>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>zipcmp</code> exits 0 if the two zip archives contain the same files, 1 if they differ, and &gt;1 if an error occurred.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-zipmerge/">zipmerge</a>(1), <a href="/docs/linux/man/1-ziptorrent/">ziptorrent</a>(1), <a href="/docs/linux/man/3-libzip/">libzip</a>(3)</p>
<h2>AUTHORS</h2>
<p> Dieter Baron &lt;dillo [at] giga.or.at&gt; and Thomas Klausner &lt;tk [at] giga.or.at&gt; </p>
<h2>Index</h2>
