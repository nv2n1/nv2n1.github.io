---
title: "autoflat(1)"
name: "autoflat"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autoflat/"
description: "autoflat – CCD flat-frame composition"
---

<h2 class="name">NAME</h2>
<p> autoflat &#8211; CCD flat-frame composition</p>
<h2>SYNOPSIS</h2>
<p> <code>autoflat </code><i>[options] source_file &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> The Autoflat program compose a set of flat-fields and performs one flat-field called master-flat. The source frames are normalized to brigtness defined level (10000 by default). Then, it computes the robust median algorithm to the corresponding pixels to get the resulting value. Applying this function, you can achieve high quality correction frame to reduce the noise. The separate correction frame has to be used for each filter, if the color fliters were used. Avoid eventual camera rotation on its mount. </p>
<p> All source frames must be in FITS format and of same dimensions. Frames of the same color filter and exposition duration should be used. The output file is in FITS format too. </p>
<h2>OPTIONS</h2>
<p> The list of input files is usualy entered directly on the command line. If you are going to process a large set of files, you can use the question marks (for a single chars) or the asterisk (for a strings of chars). </p>
<p> The alternate way, how to process a large set of files, is the batch mode. In this mode, the list of input files is read from a given file or from the standard input. The directory file, for example named <i>dirfile</i>, must have the text format and the names of the input files are written on the separate lines. If the files are placed not in the current working directory, you have to specify the proper path in full or shortened form. </p>
<dl>
<dt><code>@</code><i>dirfile</i></p>
<dd> The program will read the list of source files from specified file.</p>
<dt><code>@</code></p>
<dd> The program will read the list of source files from stdin.</p>
<dt><code>par=</code><i>file</i>, <code>-p</code><i>file</i></p>
<dd> Optional parameter file. Default is <i>autoflat.ini</i>.</p>
<dt><code>out=</code><i>file</i>, <code>-o</code><i>file</i></p>
<dd> Name of the output file. Default is <i>autoflat.fts</i>.</p>
<dt><code>&#8211;help</code></p>
<dd> Prints short help.</p>
<dt><code>&#8211;license</code></p>
<dd> Prints the license.</p>
<dt><code>&#8211;version</code></p>
<dd> Prints the program name and its version.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Quiet mode &#8212; inhibits the screen printouts.</p>
<dt><code>&#8211;debug</code></p>
<dd> Debug mode &#8212; extends the screen printouts. </p>
</dl>
<h2>EXAMPLES</h2>
<p> The following command computes median of frames: &#8216;test1.fts&#8217;, &#8216;test2.fts&#8217; a &#8216;test3.fts&#8217;; than the resulting frame normalizes to level of 10000 and stores the output frame to &#8216;autoflat.fts&#8217;.</p>
<dl>
<dt>
<dd> <code>autoflat test1.fts test2.fts test3.fts</code> </p>
</dl>
<h2>EXIT STATUS</h2>
<p> autoflat returns a zero exist status if it succeeds to convert all specified file. Otherwise, it will stop immediately when the error occurs and returns nonzero code. </p>
<h2>DIRECTORIES</h2>
<p> <i>~/.cmunipack</i> <i>/usr/local/share/cmunipack</i> </p>
<h2>AUTHORS</h2>
<p> The project manager David Motl is also the author of the most part of the source codes. Some algorithms originates from Munipack package, coded by Filip Hroch. Algorithms for aperture photometry originates from Daophot software by P. B. Stetson. Munifind algorithm originates from Varfind tool written by Rudolf Novak and Lukas Kral. </p>
<p> The package uses the FITSIO library (Dr. William Pence, NASA), the FreeImage library maintained by Herve Drolon and the James Clark&#8217;s EXPAT library. </p>
<p> The english version of the documentation was written by David Motl with great help of Petr Lutcha and Jitka Kudrnacova. </p>
<h2>BUG REPORTS</h2>
<p> David Motl (dmotl [at] volny.cz) </p>
<h2>COPYING</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-airmass/">airmass</a>(1),</code> <code><a href="/docs/linux/man/1-autoflat/">autoflat</a>(1),</code> <code><a href="/docs/linux/man/1-cmunipack/">cmunipack</a>(1),</code> <code><a href="/docs/linux/man/1-darkbat/">darkbat</a>(1),</code> <code><a href="/docs/linux/man/1-flatbat/">flatbat</a>(1),</code> <code><a href="/docs/linux/man/1-helcor/">helcor</a>(1),</code> <code><a href="/docs/linux/man/1-kombine/">kombine</a>(1),</code> <code><a href="/docs/linux/man/1-konve/">konve</a>(1),</code> <code><a href="/docs/linux/man/1-meandark/">meandark</a>(1),</code> <code><a href="/docs/linux/man/1-munifind/">munifind</a>(1),</code> <code><a href="/docs/linux/man/1-munilist/">munilist</a>(1),</code> <code><a href="/docs/linux/man/1-munimatch/">munimatch</a>(1),</code> <code><a href="/docs/linux/man/1-muniphot/">muniphot</a>(1),</code> <code><a href="/docs/linux/man/1-timebat/">timebat</a>(1)</code> </p>
<h2>Index</h2>
