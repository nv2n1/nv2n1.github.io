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
<dl>
<dt><code>-h</code></dt>
<dd> Display a short help message and exit.</dd>
<dt><code>-i</code></dt>
<dd> Compare names ignoring case distinctions.</dd>
<dt><code>-q</code></dt>
<dd> Quiet mode. Compare <code>-v</code>.</dd>
<dt><code>-v</code></dt>
<dd> Verbose mode. Print details about differences to stdout. (This is the default.)</dd>
<dt><code>-V</code></dt>
<dd> Display version information and exit.</dd></dl>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>zipcmp</code> exits 0 if the two zip archives contain the same files, 1 if they differ, and &gt;1 if an error occurred.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-zipmerge/">zipmerge</a>(1), <a href="/docs/linux/man/1-ziptorrent/">ziptorrent</a>(1), libzip(3)</p>
<h2>AUTHORS</h2>
<p> Dieter Baron &lt;dillo [at] giga.or.at&gt; and Thomas Klausner &lt;tk [at] giga.or.at&gt; </p>
