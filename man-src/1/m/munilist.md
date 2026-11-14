---
title: "munilist(1)"
name: "munilist"
section: "1"
letter: "m"
url: "/docs/linux/man/1-munilist/"
description: "munilist – Making listing from CCD photomtetry files"
---

<h2 class="name">NAME</h2>
<p> munilist &#8211; Making listing from CCD photomtetry files</p>
<h2>SYNOPSIS</h2>
<p> <code>munilist -os </code><i>[options</i>] <i>var comp chk1 chk2 &#8230; source_file &#8230;</i><br />
 <code>munilist -of </code><i>[options</i>] <i>s1 s2 &#8230; source_file &#8230;</i><br />
 <code>munilist -oa </code><i>[options</i>] <i>source_file &#8230;</i><br />
 <code>munilist -ot </code><i>[options</i>] <i>source_file &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> The Munilist program reads photometry files and creates the table of magnitudes of selected stars in the dependence on a time. The table is written to a output file in text format. The format of the table depends on given parameters and on the number of selected stars. The Munilist is usually the last step of reduction process. </p>
<p> The list of stars is given on command line, the stars are identified by index number according to their order in the file (not by the indices in the first column in the photometry file!), first star in the file has index 1, empty lines are included. </p>
<h2>OPTIONS</h2>
<p> The list of input files is usualy entered directly on the command line. If you are going to process a large set of files, you can use the question marks (for a single chars) or the asterisk (for a strings of chars). </p>
<p> The alternate way, how to process a large set of files, is the batch mode. In this mode, the list of input files is read from a given file or from the standard input. The directory file, for example named <i>dirfile</i>, must have the text format and the names of the input files are written on the separate lines. If the files are placed not in the current working directory, you have to specify the proper path in full or shortened form. </p>
<dl>
<dt><code>@</code><i>dirfile</i></p>
<dd> The program will read the list of source files from specified file.</p>
<dt><code>@</code></p>
<dd> The program will read the list of source files from stdin.</p>
<dt><code>src=</code><i>file</i></p>
<dd> Optional source file name in read-all format.</p>
<dt><code>par=</code><i>file</i> <code>-p</code><i>file</i></p>
<dd> Optional parameter file. Default is <i>munilist.ini</i>.</p>
<dt><code>out=</code><i>file</i>, <code>-o</code><i>file</i></p>
<dd> Name of the output file. Default is <i>data.dat</i>.</p>
<dt><code>ap=</code><i>n</i></p>
<dd> Aperture index. Default is 1.</p>
<dt><i>var comp chk1 chk2 &#8230;</i></p>
<dd> Indices of variable star, comparison stars and check stars.</p>
<dt><i>s1 s2 &#8230;</i></p>
<dd> Indices of selected stars.</p>
<dt><code>-os</code></p>
<dd> Use the &#8216;differential magnitudes&#8217; output format. This is the default behavior.</p>
<dt><code>-of</code></p>
<dd> Use the &#8216;instrumental magnitudes&#8217; output format.</p>
<dt><code>-oa</code></p>
<dd> Use the &#8216;read-all&#8217; output format.</p>
<dt><code>-ot</code></p>
<dd> Use the &#8216;track-list&#8217; output format.</p>
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
<p> The following command creates table of brightness of the star #2 (stored on second position in photometry files) relative to the star #3. The output in short format is required; the magnitudes will be differential instrumental magnitues (V-C).</p>
<dl>
<dt>
<dd> <code>munilist 2 3 test1.mat test2.mat test3.mat</code> </p>
</dl>
<h2>EXIT STATUS</h2>
<p> munilist returns a zero exist status if it succeeds to convert all specified file. Otherwise, it will stop immediately when the error occurs and returns nonzero code. </p>
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
