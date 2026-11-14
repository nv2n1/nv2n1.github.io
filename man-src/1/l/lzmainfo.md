---
title: "lzmainfo(1)"
name: "lzmainfo"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lzmainfo/"
description: "lzmainfo – show information stored in the .lzma file header"
---

<h2 class="name">NAME</h2>
<p> lzmainfo &#8211; show information stored in the .lzma file header </p>
<h2>SYNOPSIS</h2>
<p> <code>lzmainfo</code> [<code>&#8211;help</code>] [<code>&#8211;version</code>] [<i>file&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lzmainfo</code> shows information stored in the <code>.lzma</code> file header. It reads the first 13 bytes from the specified <i>file</i>, decodes the header, and prints it to standard output in human readable format. If no <i>files</i> are given or <i>file</i> is <code>&#8211;</code>, standard input is read. </p>
<p> Usually the most interesting information is the uncompressed size and the dictionary size. Uncompressed size can be shown only if the file is in the non-streamed <code>.lzma</code> format variant. The amount of memory required to decompress the file is a few dozen kilobytes plus the dictionary size. </p>
<p> <code>lzmainfo</code> is included in XZ Utils primarily for backward compatibility with LZMA Utils.</p>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> All is good.</p>
<dt><code>1</code></p>
<dd> An error occurred.</dl>
<h2>BUGS</h2>
<p> <code>lzmainfo</code> uses <code>MB</code> while the correct suffix would be <code>MiB</code> (2^20 bytes). This is to keep the output compatible with LZMA Utils.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) </p>
<h2>Index</h2>
