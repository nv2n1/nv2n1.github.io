---
title: "pnmtopalm(1)"
name: "pnmtopalm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtopalm/"
description: "pnmtopalm – convert a portable anymap into a Palm pixmap"
---

<h2 class="name">NAME</h2>
<p> pnmtopalm &#8211; convert a portable anymap into a Palm pixmap</p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtopalm</code> [<code>-verbose</code>] [<code>-depth</code> <i>N</i>] [<code>-maxdepth</code> <i>N</i>] [<code>-colormap</code>] [<code>-transparent</code> <i>color</i>] [<code>-offset</code>]<br />
 [<code>-rle-compression</code>|<code>-scanline-compression</code>] [<i>pnmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads a PNM image as input, from stdin or <i>pnmfile</i>. Produces a Palm pixmap as output. </p>
<p> Palm pixmap files are either greyscale files 1, 2, or 4 bits wide, or color files 8 bits wide, so <code>pnmtopalm </code> automatically scales colors to have an appropriate maxval, unless you specify a depth or max depth. Input files must have an appropriate number and set of colors for the selected output constraints. This often means that you should run the PNM image through <code>ppmquant</code> before you pass it to <code>pnmtopalm</code>. Netpbm comes with several colormap files you can use with <code>ppmquant</code> for this purpose. They are <code>palmgray2.map </code> (4 shades of gray for a depth of 2), <code>palmgray4.map </code> (16 shades of gray for a depth of 4), and <code>palmcolor8.map </code> (232 colors in default Palm colormap). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-verbose</code></p>
<dd> Display the format of the output file.</p>
<dt><code>-depth </code><i>N</i></p>
<dd> Produce a file of depth <i>N</i>, where <i>N </i> must be either 1, 2, 4, 8, or 16. Any depth greater than 1 will produce a version 1 or 2 bitmap. Because the default Palm 8-bit colormap is not grayscale, if the input is a grayscale or monochrome pixmap, the output will never be more than 4 bits deep, regardless of the specified depth. Note that 8-bit color works only in PalmOS 3.5 (and higher), and 16-bit direct color works only in PalmOS 4.0 (and higher). However, the 16-bit direct color format is also compatible with the various PalmOS 3.x versions used in the Handspring Visor, so these images may also work in that device.</p>
<dt><code>-maxdepth </code><i>N</i></p>
<dd> Produce a file of minimal depth, but in any case less than <i>N </i> bits wide. If you specify 16-bit, the output will always be 16-bit direct color.</p>
<dt><code>-offset</code></p>
<dd> Fill in the <code>nextDepthOffset </code> field in the file header, to provide for multiple renditions of the pixmap in the same file.</p>
<dt><code>-colormap</code></p>
<dd> Build a custom colormap and include it in the output file. This is not recommended by Palm, for efficiency reasons. Otherwise, <code>pnmtopalm </code> uses the default Palm colormap for color output.</p>
<dt><code>-transparent </code><i>color</i></p>
<dd> Marks <i>one</i> particular color as fully transparent. The format to specify the color is either (when for example orange) &quot;1.0,0.5,0.0&quot;, where the values are floats between zero and one, or with the syntax &quot;#RGB&quot;, &quot;#RRGGBB&quot; or &quot;#RRRRGGGGBBBB&quot; where R, G and B are hexadecimal numbers. This also makes the output bitmap a version 2 bitmap. Transparency works only on Palm OS 3.5 and higher.</p>
<dt><code>-rle-compression</code></p>
<dd> Specifies that the output Palm bitmap will use the Palm RLE compression scheme, and will be a version 2 bitmap. RLE compression works only with Palm OS 3.5 and higher.</p>
<dt><code>-scanline-compression</code></p>
<dd> Specifies that the output Palm bitmap will use the Palm scanline compression scheme, and will be a version 2 bitmap. Scanline compression works only in Palm OS 2.0 and higher. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-palmtopnm/">palmtopnm</a></code>(1), <code><a href="/docs/linux/man/1-ppmquant/">ppmquant</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<h2>NOTES</h2>
<p> An additional compression format, <code>packbits</code>, was added with PalmOS 4.0. This package should be updated to be able to generate that. </p>
<p> Palm pixmaps may contains multiple renditions of the same pixmap, in different depths. To construct an N-multiple-rendition Palm pixmap with <code>pnmtopalm</code>, first construct renditions 1 through N-1 using the <code>-offset</code> option, then construct the Nth pixmap without the <code>-offset </code> option. Then concatenate the individual renditions together in a single file using <code>cat</code>. </p>
<h2>AUTHORS</h2>
<p> This program was originally written as ppmtoTbmp.c, by Ian Goldberg and George Caswell. It was completely re-written by Bill Janssen to add color, compression, and transparency function.<br />
 Copyright 1995-2001 by Ian Goldberg, George Caswell, and Bill Janssen. </p>
<h2>Index</h2>
