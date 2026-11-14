---
title: "exiftran(1)"
name: "exiftran"
section: "1"
letter: "e"
url: "/docs/linux/man/1-exiftran/"
description: "exiftran – transform digital camera jpeg images # #"
---

<p>#</p>
<h2 class="name">NAME</h2>
<p> exiftran &#8211; transform digital camera jpeg images # # </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>exiftran</code> [<i>options</i>] <i>file1 file2 &#8230; fileN</i></p>
<dd>
<dt><code>exiftran</code> -i [<i>transform options</i>] [<i>others options</i>] <i>file1 file2 &#8230; fileN</i></p>
<dd>
<dt><code>exiftran</code> -o <i>outputfile</i> [<i>transform options</i>] [<i>other options</i>] <i>inputfile</i></p>
<dd>
<dt><code>exiftran</code> -d <i>file1 file2 &#8230; fileN</i> &gt; <i>exifinfo</i></p>
<dd> # #</dl>
<h2>DESCRIPTION</h2>
<p> <code>Exiftran</code> is a command line utility to transform digital camera <i>jpeg</i> images. It can do lossless rotations like <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1), but unlike <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1) it cares about the <i>EXIF</i> data: It can rotate images automatically by checking the exif orientation tag; it updates the exif informations if needed (image dimension, orientation); it also rotates the exif thumbnail. It can process multiple images at once. # #</p>
<h2>TRANSFORM OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Automatic (using exif orientation tag).</p>
<dt><code>-9</code></p>
<dd> Rotate by 90 degrees clockwise.</p>
<dt><code>-1</code></p>
<dd> Rotate by 180 degrees clockwise.</p>
<dt><code>-2</code></p>
<dd> Rotate by 270 degrees clockwise.</p>
<dt><code>-f</code></p>
<dd> Mirror image vertically (top / bottom).</p>
<dt><code>-F</code></p>
<dd> Mirror image horizontally (left to right).</p>
<dt><code>-t</code></p>
<dd> Transpose (across UL-to-LR corner).</p>
<dt><code>-T</code></p>
<dd> Transverse (across UR-to-LL corner).</p>
<dt><code>-nt</code></p>
<dd> Don&#8217;t transform exif thumbnail.</p>
<dt><code>-ni</code></p>
<dd> Don&#8217;t transform jpeg image. You might need this or the <code>-nt</code> option to fixup things in case you transformed the image with some utility which ignores the exif thumbnail. Just generating a new thumbnail with <code>-g</code> is another way to fix it.</p>
<dt><code>-no</code></p>
<dd> Don&#8217;t update the orientation tag. By default <code>exiftran</code> sets the orientation to &quot;1&quot; (no transformation needed) to avoid other exif-aware applications try to rotate the already-rotated image again. # #</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Print a short help text.</p>
<dt><code>-d</code></p>
<dd> Dump exif data for the file(s).</p>
<dt><code>-c</code><i>&nbsp;<wbr>text</i></p>
<dd> Set jpeg comment tag to <i>text</i>.</p>
<dt><code>-g</code></p>
<dd> (re)generate exif thumbnail.</p>
<dt><code>-o</code><i>&nbsp;<wbr>file</i></p>
<dd> Specify output <i>file</i>. Only one input file is allowed in this mode.</p>
<dt><code>-i</code></p>
<dd> Enable inplace editing of the images. <code>Exiftran</code> allows multiple input files then. You must specify either this option or a output file with <code>-o</code> for all operations which modify the image (i.e. everything but <code>-d</code> right now).</p>
<dt><code>-b</code></p>
<dd> Create a backup file when doing inplace editing (imply <code>-i</code>).</p>
<dt><code>-p</code></p>
<dd> Preserve timestamps (atime + mtime) when doing inplace editing (imply <code>-i</code>). # #</dl>
<h2>EXAMPLES</h2>
<p> Autorotate all jpeg files in the current directory: </p>
<p><i>exiftran -ai&nbsp;<wbr>*.jpeg</i> # #</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-exif/">exif</a></code>(1), <code><a href="/docs/linux/man/1-exiftags/">exiftags</a></code>(1), <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1) # #</p>
<h2>AUTHOR</h2>
<p> Gerd Hoffmann <code>&lt;gerd [at] kraxel.org&gt;</code> # #</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2002-2012 Gerd Hoffmann &lt;gerd [at] kraxel.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
