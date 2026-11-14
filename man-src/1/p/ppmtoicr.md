---
title: "ppmtoicr(1)"
name: "ppmtoicr"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtoicr/"
description: "ppmtoicr – convert a portable pixmap into NCSA ICR format"
---

<h2 class="name">NAME</h2>
<p> ppmtoicr &#8211; convert a portable pixmap into NCSA ICR format </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtoicr</code> [<code>-windowname</code> <i>name</i>] [<code>-expand</code> <i>expand</i>] [<code>-display</code> <i>display</i>] [<code>-rle</code>] [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap file as input. Produces an NCSA Telnet Interactive Color Raster graphic file as output. If <i>ppmfile</i> is not supplied, <i>ppmtoicr</i> will read from standard input. </p>
<p> Interactive Color Raster (ICR) is a protocol for displaying raster graphics on workstation screens. The protocol is implemented in NCSA Telnet for the Macintosh version 2.3. The ICR protocol shares characteristics of the Tektronix graphics terminal emulation protocol. For example, escape sequences are used to control the display. </p>
<p> <i>ppmtoicr</i> will output the appropriate sequences to create a window of the dimensions of the input pixmap, create a colormap of up to 256 colors on the display, then load the picture data into the window. </p>
<p> Note that there is no icrtoppm tool &#8211; this transformation is one way.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-windowname</code><i>name</i></p>
<dd> Output will be displayed in <i>name</i> (Default is to use <i>ppmfile</i> or &quot;untitled&quot; if standard input is read.)</p>
<dt><code>-expand</code><i>expand</i></p>
<dd> Output will be expanded on display by factor <i>expand</i> (For example, a value of 2 will cause four pixels to be displayed for every input pixel.)</p>
<dt><code>-display</code><i>display</i></p>
<dd> Output will be displayed on screen numbered <i>display</i></p>
<dt><code>-rle</code></p>
<dd> Use run-length encoded format for display. (This will nearly always result in a quicker display, but may skew the colormap.)</dl>
<h2>EXAMPLES</h2>
<p> To display a <i>ppm</i> file using the protocol: </p>
<pre>
    ppmtoicr ppmfile
</pre>
<p> This will create a window named <i>ppmfile</i> on the display with the correct dimensions for <i>ppmfile,</i> create and download a colormap of up to 256 colors, and download the picture into the window. The same effect may be achieved by the following sequence: </p>
<pre>
    ppmtoicr ppmfile &gt; filename
    cat filename
</pre>
<p> To display a GIF file using the protocol in a window titled after the input file, zoom the displayed image by a factor of 2, and run-length encode the data: </p>
<pre>
    giftopnm giffile | ppmtoicr -w giffile -r -e 2
</pre>
<h2>BUGS</h2>
<p> The protocol uses frequent <i>fflush</i> calls to speed up display. If the output is saved to a file for later display via <i>cat,</i> drawing will be much slower. In either case, increasing the Blocksize limit on the display will speed up transmission substantially.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ppm/">ppm</a>(5)</code> </p>
<p> <i>NCSA Telnet for the Macintosh</i>, University of Illinois at Urbana-Champaign (1989)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1990 by Kanthan Pillay (svpillay [at] Princeton.EDU), Princeton University Computing and Information Technology. </p>
<h2>Index</h2>
