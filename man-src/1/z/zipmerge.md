---
title: "zipmerge(1)"
name: "zipmerge"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zipmerge/"
description: "zipmerge – merge zip archives"
---

<h2>NAME</h2>
<p> zipmerge &#8211; merge zip archives</p>
<h2>SYNOPSIS</h2>
<p> <code>zipmerge</code> [<code>-DhIiSsV</code>] <code>target-zip</code> <code>source-zip Op source-zip &#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>zipmerge</code> merges the source zip archives <code>source-zip</code> into the target zip archive <code>target-zip.</code> By default, files in the source zip archives overwrite existing files of the same name in the target zip archive. </p>
<p> Supported options:</p>
<dl>
<dl>
<dt><code>-D</code></dt>
<dd> Ignore directory components in file name comparisons.</dd>
<dt><code>-h</code></dt>
<dd> Display a short help message and exit.</dd>
<dt><code>-I</code></dt>
<dd> Ignore case in file name comparisons</dd>
<dt><code>-i</code></dt>
<dd> Ask before overwriting files. See also <code>-s</code>.</dd>
<dt><code>-S</code></dt>
<dd> Do not overwrite files that have the same size and CRC32 in both the source and target archives.</dd>
<dt><code>-s</code></dt>
<dd> When <code>-i</code> is given, do not before overwriting files that have the same size and CRC32.</dd>
<dt><code>-V</code></dt>
<dd> Display version information and exit.</dd></dl>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>zipmerge</code> exits 0 on success and &gt;1 if an error occurred.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-zipcmp/">zipcmp</a>(1), <a href="/docs/linux/man/1-ziptorrent/">ziptorrent</a>(1), libzip(3)</p>
<h2>AUTHORS</h2>
<p> Dieter Baron &lt;dillo [at] giga.or.at&gt; and Thomas Klausner &lt;tk [at] giga.or.at&gt; </p>
