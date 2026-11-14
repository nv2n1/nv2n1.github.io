---
title: "munifind(1)"
name: "munifind"
section: "1"
letter: "m"
url: "/docs/linux/man/1-munifind/"
description: "munifind – Finding variable stars on CCD photometry files"
---

<h2 class="name">NAME</h2>
<p> munifind &#8211; Finding variable stars on CCD photometry files</p>
<h2>SYNOPSIS</h2>
<p> <code>munifind </code><i>[options] source_file &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> The munifind program is the useful tool used in semi-automatic scaning of variable stars in the series of source files. It is based on the relation between the standard deviations of the brightness of the stars and their mean brightness. The program reads all photometry files and compute the mean brightness and standard deviations of brightness of all stars. The algorithm automatically removes stars that are missing on majority of source frames (threshold parameter). The comparison star is automaticaly selected or given by a optional parameter. </p>
<p> The output file is saved in text format and contains the table of mean magnitudes and standard deviations. </p>
<h2>OPTIONS</h2>
<p> The list of input files is usualy entered directly on the command line. If you are going to process a large set of files, you can use the question marks (for a single chars) or the asterisk (for a strings of chars). </p>
<p> The alternate way, how to process a large set of files, is the batch mode. In this mode, the list of input files is read from a given file or from the standard input. The directory file, for example named <i>dirfile</i>, must have the text format and the names of the input files are written on the separate lines. If the files are placed not in the current working directory, you have to specify the proper path in full or shortened form. </p>
<dl>
<dt><code>@</code><i>dirfile</i></p>
<dd> The program will read the list of source files from specified file.</p>
<dt><code>@</code></p>
<dd> The program will read the list of source files from stdin.</p>
<dt><code>src=</code><i>file</i>, <code>-a</code><i>file</i></p>
<dd> Optional source file name in read-all format.</p>
<dt><code>par=</code><i>file</i> <code>-p</code><i>file</i></p>
<dd> Optional parameter file. Default is <i>munifind.ini</i>.</p>
<dt><code>out=</code><i>file</i>, <code>-o</code><i>file</i></p>
<dd> Name of the output file. Default is <i>munifind.dat</i>.</p>
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
<p> The following command demonstrates, how to create a file of magnitudes and the deviations from the source files &#8216;test1.mat&#8217;, &#8216;test2.mat&#8217; and &#8216;test3.mat&#8217;.</p>
<dl>
<dt>
<dd> <code>munifind test1.mat test2.mat test3.mat</code> </p>
</dl>
<h2>EXIT STATUS</h2>
<p> munifind returns a zero exist status if it succeeds to convert all specified file. Otherwise, it will stop immediately when the error occurs and returns nonzero code. </p>
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
