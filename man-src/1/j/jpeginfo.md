---
title: "jpeginfo(1)"
name: "jpeginfo"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jpeginfo/"
description: "jpeginfo – prints information and tests integrity of JPEG/JFIF files."
---

<h2>NAME</h2>
<p> jpeginfo &#8211; prints information and tests integrity of JPEG/JFIF files. </p>
<h2>SYNOPSIS</h2>
<p> <code>jpeginfo </code> [ <code>options </code> ] [ <code>filenames </code> ] </p>
<h2>DESCRIPTION</h2>
<p> <i>jpeginfo</i> is used to generate informative listings of jpeg files, and also to check jpeg files for errors. Program also supports automatic deletion of broken jpegs. </p>
<h2>OPTIONS</h2>
<p> Options may be either the traditional POSIX one letter options, or the GNU style long options. POSIX style options start with a single &#8220;-&#8221;, while GNU long options start with &#8220;&#8211;&#8221;. </p>
<p> Options offered by <i>jpeginfo</i> are the following:</p>
<dl>
<dt><code>-c, &#8211;check</code></p>
<dd> Check files also for errors. (default is just to read the headers).</p>
<dt><code>-C, &#8211;comments</code></p>
<dd> Display file comments (from COM markers).</p>
<dt><code>-d, &#8211;delete</code></p>
<dd> Delete files that have errors. (default is not to delete any files).</p>
<dt><code>-f&lt;filename&gt;, &#8211;file&lt;filename&gt;</code></p>
<dd> Read filenames to process from given file. To use standard input (stdin) use &#8216;-&#8216; as a filename. This is alternative to default where filenames are given as parameters to the program.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display short usage information and exits.</p>
<dt><code>-5, &#8211;md5</code></p>
<dd> Calculates MD5 checksum for each file.</p>
<dt><code>-i, &#8211;info</code></p>
<dd> Displays even more information about each picture. Prints image coding (Huffman/Arithmetic), density (in dpi/dpc), and whether CCIR601 sampling was used or not.</p>
<dt><code>-l, &#8211;lsstyle</code></p>
<dd> Uses alternate listing format (ls -l style).</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Enables verbose mode (positively chatty).</p>
<dt><code>&#8211;version</code></p>
<dd> Displays program version.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Quiet mode, output just the jpeg infos.</p>
<dt><code>-m&lt;mode&gt;, &#8211;mode=&lt;mode&gt;</code></p>
<dd> Sets the delete mode, meaningful only when used with <i>-d</i> flag. <i>Mode</i> can be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>all</code></p>
<dd> files containing any type of errors/warnings, not nessessary preventing the decoding. (default)</p>
<dt><code>erronly</code></p>
<dd> only files with serious errors (ie. cannot be decoded at all). </p>
</dl>
</dl>
</dl>
<h2>BUGS</h2>
<p> None, so far :-) </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-jpegoptim/">jpegoptim</a>(1) </p>
<h2>AUTHOR</h2>
<p> Timo Kokkonen (tjko [at] jyu.fi) </p>
<h2>COPYING</h2>
<p> Copyright (C) 1996-1998 Timo Kokkonen </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.<br />
&nbsp;<wbr>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.<br />
&nbsp;<wbr>You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
