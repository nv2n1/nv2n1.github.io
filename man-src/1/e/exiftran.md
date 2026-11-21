---

title: "exiftran(1)"
name: "exiftran"
section: "1"
letter: "e"
url: "/docs/linux/man/1-exiftran/"
description: "exiftran – transform digital camera jpeg images # #"
---

<p>#</p>
<dl>
<dt><code>exiftran</code> [<i>options</i>] <i>file1 file2 &#8230; fileN</i></dt>
<dd>
</dd><dt><code>exiftran</code> -i [<i>transform options</i>] [<i>others options</i>] <i>file1 file2 &#8230; fileN</i></dt>
<dd>
</dd><dt><code>exiftran</code> -o <i>outputfile</i> [<i>transform options</i>] [<i>other options</i>] <i>inputfile</i></dt>
<dd>
</dd><dt><code>exiftran</code> -d <i>file1 file2 &#8230; fileN</i> &gt; <i>exifinfo</i></dt>
<dd> # #</dd></dl>
<p> <code>Exiftran</code> is a command line utility to transform digital camera <i>jpeg</i> images. It can do lossless rotations like <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1), but unlike <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1) it cares about the <i>EXIF</i> data: It can rotate images automatically by checking the exif orientation tag; it updates the exif informations if needed (image dimension, orientation); it also rotates the exif thumbnail. It can process multiple images at once. # #</p>
<h2>TRANSFORM OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd> Automatic (using exif orientation tag).</dd>
<dt><code>-9</code></dt>
<dd> Rotate by 90 degrees clockwise.</dd>
<dt><code>-1</code></dt>
<dd> Rotate by 180 degrees clockwise.</dd>
<dt><code>-2</code></dt>
<dd> Rotate by 270 degrees clockwise.</dd>
<dt><code>-f</code></dt>
<dd> Mirror image vertically (top / bottom).</dd>
<dt><code>-F</code></dt>
<dd> Mirror image horizontally (left to right).</dd>
<dt><code>-t</code></dt>
<dd> Transpose (across UL-to-LR corner).</dd>
<dt><code>-T</code></dt>
<dd> Transverse (across UR-to-LL corner).</dd>
<dt><code>-nt</code></dt>
<dd> Don&#8217;t transform exif thumbnail.</dd>
<dt><code>-ni</code></dt>
<dd> Don&#8217;t transform jpeg image. You might need this or the <code>-nt</code> option to fixup things in case you transformed the image with some utility which ignores the exif thumbnail. Just generating a new thumbnail with <code>-g</code> is another way to fix it.</dd>
<dt><code>-no</code></dt>
<dd> Don&#8217;t update the orientation tag. By default <code>exiftran</code> sets the orientation to &quot;1&quot; (no transformation needed) to avoid other exif-aware applications try to rotate the already-rotated image again. # #</dd></dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Print a short help text.</dd>
<dt><code>-d</code></dt>
<dd> Dump exif data for the file(s).</dd>
<dt><code>-c</code><i>&nbsp;<wbr>text</i></dt>
<dd> Set jpeg comment tag to <i>text</i>.</dd>
<dt><code>-g</code></dt>
<dd> (re)generate exif thumbnail.</dd>
<dt><code>-o</code><i>&nbsp;<wbr>file</i></dt>
<dd> Specify output <i>file</i>. Only one input file is allowed in this mode.</dd>
<dt><code>-i</code></dt>
<dd> Enable inplace editing of the images. <code>Exiftran</code> allows multiple input files then. You must specify either this option or a output file with <code>-o</code> for all operations which modify the image (i.e. everything but <code>-d</code> right now).</dd>
<dt><code>-b</code></dt>
<dd> Create a backup file when doing inplace editing (imply <code>-i</code>).</dd>
<dt><code>-p</code></dt>
<dd> Preserve timestamps (atime + mtime) when doing inplace editing (imply <code>-i</code>). # #</dd></dl>
<h2>EXAMPLES</h2>
<p> Autorotate all jpeg files in the current directory: </p>
<p><i>exiftran -ai&nbsp;<wbr>*.jpeg</i> # #</p>
<h2>SEE ALSO</h2>
<p> <code>exif</code>(1), <code>exiftags</code>(1), <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1) # #</p>
<h2>AUTHOR</h2>
<p> Gerd Hoffmann <code>&lt;gerd [at] kraxel.org&gt;</code> # #</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2002-2012 Gerd Hoffmann &lt;gerd [at] kraxel.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
