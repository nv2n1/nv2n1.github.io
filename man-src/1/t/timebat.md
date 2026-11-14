---
title: "timebat(1)"
name: "timebat"
section: "1"
letter: "t"
url: "/docs/linux/man/1-timebat/"
description: "timebat – CCD time correction"
---

<h2 class="name">NAME</h2>
<p> timebat &#8211; CCD time correction</p>
<h2>SYNOPSIS</h2>
<p> <code>timebat </code><i>[options] </i><code>tcor=</code><i>seconds source_file &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> The Timebat program applies time correction to the source frames. It means, that it adds given amount of time to the times of observation. The program does not touch neither the image data nor other parameters in header. </p>
<p> The source frames and also dark frame must be in FITS format. The output file is in FITS format too. </p>
<h2>OPTIONS</h2>
<p> The list of input files is usualy entered directly on the command line. If you are going to process a large set of files, you can use the question marks (for a single chars) or the asterisk (for a strings of chars). </p>
<p> The alternate way, how to process a large set of files, is the batch mode. In this mode, the list of input files is read from a given file or from the standard input. The directory file, for example named <i>dirfile</i>, must have the text format and the names of the input files are written on the separate lines. If the files are placed not in the current working directory, you have to specify the proper path in full or shortened form. </p>
<p> The <i>mask</i> parameters allows to set the naming of output files. The mask consists of letters, numbers and other characters allowed in the file name by the operating system. The special meaning has the question mark or the sequence of it. They will be replaced by the ordinal number of the output file, the number is always indented by leading zeros to the same number of decimal places as the number of the question marks. For example, when the mask <i>tout????.fts</i> is given, the output files named <i>tout0001.fts, tout0002.fts, tout0003.fts</i> will be generated. </p>
<dl>
<dt><code>@</code><i>dirfile</i></p>
<dd> The program will read the list of source files from specified file.</p>
<dt><code>@</code></p>
<dd> The program will read the list of source files from stdin.</p>
<dt><code>tcor=</code><i>n</i>, <code>-t</code><i>n</i></p>
<dd> Time correction in seconds.</p>
<dt><code>mask=</code><i>mask</i>, <code>-o</code><i>mark</i></p>
<dd> Mask of the output file(s). Default is <i>tout????.fts</i>.</p>
<dt><code>-c</code><i>x</i></p>
<dd> Initial counter value. Default is 1.</p>
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
<p> The following command shifts time of observation of &#8216;kout0001.fts&#8217; by 1 hour to the future. The output shall be written to &#8216;tout0001.fts&#8217; file.</p>
<dl>
<dt>
<dd> <code>timebat tcor=3600 kout0001.fts</code> </p>
</dl>
<h2>EXIT STATUS</h2>
<p> timebat returns a zero exist status if it succeeds to convert all specified file. Otherwise, it will stop immediately when the error occurs and returns nonzero code. </p>
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
