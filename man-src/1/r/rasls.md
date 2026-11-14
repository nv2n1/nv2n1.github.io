---
title: "rasls(1)"
name: "rasls"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rasls/"
description: "rasls – list information on rasterfiles"
---

<h2>NAME</h2>
<p> rasls &#8211; list information on rasterfiles</p>
<h2>SYNOPSIS</h2>
<p> <code>rasls</code> [<code>-type</code>] [<code>-count</code>] [<code>-resolution</code>] [<code>-verbose</code>] [<code>-Version</code>] [<code>-ifmt </code><i>file_format</i>] [files]</p>
<h2>DESCRIPTION</h2>
<p> For each file <code>rasls</code> will generate a one line description of the rasterfile. Information provided includes the format type (Sun, HDF, etc.), the encoding (indexed, direct, etc.), resolution, and filename. Files that cannot be read as rasterfiles, are empty, are directories, or are otherwise unrecognizable are simply listed as such. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-type</code></p>
<dd> Print the encoding type of the rasterfile. Currently this will be either <i>indexed</i> or <i>direct</i>.</p>
<dt><code>-count</code></p>
<dd> Print the number of frames in the raster file.</p>
<dt><code>-resolution</code></p>
<dd> Print the spatial resolution of a file in pixels.</p>
<dt><code>-help</code></p>
<dd> Print help information.</p>
<dt><code>-verbose</code></p>
<dd> Print as much information as possible about each rasterfile. Information provided is a combination of format-independent and format-dependent parameters.</p>
<dt><code>-Version</code></p>
<dd> Print the version number.</p>
<dt><code>-ifmt</code><i> format</i></p>
<dd> Specify the input file format. <i>format</i> is one of the file name extensions discussed in <code>ras_formats(5NCARG)</code> (without the &quot;.&quot;, e.g. <code>xwd).</code> When this option is specified file name extensions are not necessary and are ignored if present. All input files must have the same format. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code>rasview</code>(1NCARG), <code>rascat</code>(1NCARG), <code>rasgetpal</code>(1NCARG), <code>rasls</code>(1NCARG), <code>rassplit</code>(1NCARG), <code>ras_formats</code>(5NCARG), <code>ras_palette</code>(5NCARG) </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
