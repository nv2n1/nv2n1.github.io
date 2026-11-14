---
title: "p7zip(1)"
name: "p7zip"
section: "1"
letter: "p"
url: "/docs/linux/man/1-p7zip/"
description: "p7zip – Wrapper on 7-Zip file archiver with high compression ratio"
---

<h2 class="name">NAME</h2>
<p> p7zip &#8211; Wrapper on 7-Zip file archiver with high compression ratio </p>
<h2>SYNOPSIS</h2>
<p> <code>p7zip</code> [<code>-c</code>|<code>&#8211;stdout</code>|<code>&#8211;to-stdout</code>] [<code>-d</code>|<code>&#8211;decompress</code>|<code>&#8211;uncompress</code>] [<code>-f</code>|<code>&#8211;force</code>] [<code>-h</code>|<code>&#8211;help</code>] [<code>-k</code>|<code>&#8211;keep</code>] [<code>&#8212;</code>] [<i>file &#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> 7-Zip is a file archiver supporting 7z (that implements LZMA compression algorithm featuring very high compression ratio), LZMA2, XZ, ZIP, Zip64, CAB, RAR (if the non-free p7zip-rar package is installed), ARJ, GZIP, BZIP2, TAR, CPIO, RPM, ISO, most filesystem images and DEB formats. Compression ratio in the new 7z format is 30-50% better than ratio in ZIP format. </p>
<p> <code>p7zip</code> is a gzip-like CLI wrapper script for 7-Zip, and handles only the 7z format (the native format of 7-Zip), internally executing either <code><a href="/docs/linux/man/1-7za/">7za</a></code>(1) or <code><a href="/docs/linux/man/1-7zr/">7zr</a></code>(1) command. </p>
<p> With no switches passed in the command line, each given <i>file</i> argument is compressed into <i>file.7z</i>, and then removed. </p>
<p> With the <code>-d</code> switch each passed <i>file</i> needs to end with the <i>.7z</i> extension and is decompressed. After the decompression the original <i>file</i> is removed unless it contained more than one archived file. </p>
<p> When used without any <i>file</i> argument, <code>p7zip</code> reads data from the standard input and compresses (or decompresses in case of <code>-d</code>) it into the standard output.</p>
<h2>SWITCHES</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;stdout</code>, <code>&#8211;to-stdout</code></p>
<dd> Write output on standard output.</p>
<dt><code>-d</code>, <code>&#8211;decompress</code>, <code>&#8211;uncompress</code></p>
<dd> Decompress file.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Skip some checks and force compression or decompression.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print usage.</p>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> Do not delete input file.</p>
<dt><code>&#8212;</code></p>
<dd> Treat all subsequent arguments as file names, even if they start with a dash.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-7z/">7z</a></code>(1), <code><a href="/docs/linux/man/1-7za/">7za</a></code>(1), <code><a href="/docs/linux/man/1-7zr/">7zr</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-zip/">zip</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Written for Debian by Mohammed Adnene Trojette. Updated by Robert Luberda. </p>
<h2>Index</h2>
