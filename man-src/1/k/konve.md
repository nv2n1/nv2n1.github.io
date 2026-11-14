---
title: "konve(1)"
name: "konve"
section: "1"
letter: "k"
url: "/docs/linux/man/1-konve/"
description: "konve – CCD image conversion"
---

<h2 class="name">NAME</h2>
<p> konve &#8211; CCD image conversion</p>
<h2>SYNOPSIS</h2>
<p> <code>konve </code><i>[options] source_file &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> The Konve program converts CCD frames from the format used by camera controling software to FITS format. The correction of time of observation or image flipping can be applied also. </p>
<p> The program can be run in several modes, the mode is selected by command-line parameters. Besides the usual conversion mode, it allows printing header informations of source files in short or detailed form. You can convert header only while not copying the image. Additional informations, which shall be written to the output files can be given in parameter file. </p>
<p> Current version of program supports reading SBIG (ST-xx) compressed and uncompressed files and the FITS files also. Note, that you can use FITS to FITS conversion for gathering files from many locations into one directory. It will solve the file name collisions. </p>
<h2>OPTIONS</h2>
<p> The list of input files is usualy entered directly on the command line. If you are going to process a large set of files, you can use the question marks (for a single chars) or the asterisk (for a strings of chars). </p>
<p> The alternate way, how to process a large set of files, is the batch mode. In this mode, the list of input files is read from a given file or from the standard input. The directory file, for example named <i>dirfile</i>, must have the text format and the names of the input files are written on the separate lines. If the files are placed not in the current working directory, you have to specify the proper path in full or shortened form. </p>
<p> The <i>mask</i> parameters allows to set the naming of output files. The mask consists of letters, numbers and other characters allowed in the file name by the operating system. The special meaning has the question mark or the sequence of it. They will be replaced by the ordinal number of the output file, the number is always indented by leading zeros to the same number of decimal places as the number of the question marks. For example, when the mask <i>kout????.fts</i> is given, the output files named <i>kout0001.fts, kout0002.fts, kout0003.fts</i> will be generated. </p>
<dl>
<dt><code>@</code><i>dirfile</i></p>
<dd> The program will read the list of source files from specified file.</p>
<dt><code>@</code></p>
<dd> The program will read the list of source files from stdin.</p>
<dt><code>par=</code><i>file</i>, <code>-p</code><i>file</i></p>
<dd> Optional parameter file. Default is none.</p>
<dt><code>mask=</code><i>mask</i>, <code>-o</code><i>mark</i></p>
<dd> Mask of output file(s). Default is <i>kout????.fts</i>.</p>
<dt><code>tcor=</code><i>sec</i></p>
<dd> Time correction in seconds. Default is 0.</p>
<dt><code>flip=</code><i>xy</i>, <code>-flip</code><i>xy</i></p>
<dd> Image flipping (values: &#8216;x&#8217;, &#8216;y&#8217;, &#8216;xy&#8217;).</p>
<dt><code>-c</code><i>x</i></p>
<dd> Initial counter value. Default is 1.</p>
<dt><code>-header</code></p>
<dd> Converts headers only, doesn&#8217;t convert image data.</p>
<dt><code>-info</code></p>
<dd> Prints short header informations of source files and does not generate output files.</p>
<dt><code>-details</code></p>
<dd> Prints full header informations of source files and does not generate output files.</p>
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
<p> The following command converts files &#8216;crcas01.st7&#8217;, &#8216;crcas02.st7&#8217; and &#8216;crcas03.st7&#8217; and writes the output to files &#8216;kout0001.fts&#8217;, &#8216;kout0002.fts&#8217; and &#8216;kout0003.fts&#8217;.</p>
<dl>
<dt>
<dd> <code>konve crcas01.st7 crcas02.st7 crcas03.st7</code> </p>
</dl>
<h2>EXIT STATUS</h2>
<p> konve returns a zero exist status if it succeeds to convert all specified file. Otherwise, it will stop immediately when the error occurs and returns nonzero code. </p>
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
