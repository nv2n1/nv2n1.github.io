---
title: "h5repart(1)"
name: "h5repart"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5repart/"
description: "h5repart – Repartitions a file or family of files."
---

<h2>NAME</h2>
<p> h5repart &#8211; Repartitions a file or family of files.</p>
<h2>SYNOPSIS</h2>
<p> <code>h5repart </code> <code>[-v] </code> <code>[-V] </code> <code>[-[b|m]N[g|m|k]] </code> source_file dest_file</p>
<h2>DESCRIPTION</h2>
<p> h5repart splits a single file into a family of files, joins a family of files into a single file, or copies one family of files to another while changing the size of the family members. h5repart can also be used to copy a single file to a single file with holes. </p>
<p> Sizes associated with the -b and -m options may be suffixed with g for gigabytes, m for megabytes, or k for kilobytes. </p>
<p> File family names include an integer printf format such as %d.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></dt>
<dd> Produce verbose output.</dd>
<dt><code>-V</code></dt>
<dd> Print a version number and exit.</dd>
<dt><code>-bN</code></dt>
<dd> The I/O block size, defaults to 1kB</dd>
<dt><code>-mN</code></dt>
<dd> The destination member size or 1GB</dd>
<dt>source_file</dt>
<dd> The name of the source file</dd>
<dt>dest_file</dt>
<dd> The name of the destination files</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-h5dump/">h5dump</a></i>(1), <i><a href="/docs/linux/man/1-h5ls/">h5ls</a></i>(1), <i><a href="/docs/linux/man/1-h5diff/">h5diff</a></i>(1), <i><a href="/docs/linux/man/1-h5import/">h5import</a></i>(1), <i><a href="/docs/linux/man/1-gif2h5/">gif2h5</a></i>(1), <i><a href="/docs/linux/man/1-h52gif/">h52gif</a></i>(1), <i>h5perf</i>(1) </p>
<h2>Index</h2>
