---
title: "airmass(1)"
name: "airmass"
section: "1"
letter: "a"
url: "/docs/linux/man/1-airmass/"
description: "airmass – Computing airmass coefficient"
---

<h2 class="name">NAME</h2>
<p> airmass &#8211; Computing airmass coefficient</p>
<h2>SYNOPSIS</h2>
<p> <code>airmass </code><i>[options] source_file &#8230;</i> &#8211; batch mode<br />
 <code>airmass </code><i>[options]</i> &#8211; terminal mode </p>
<h2>DESCRIPTION</h2>
<p> The Airmass program computes value of the airmass coefficient (X) from given julian date, object&#8217;s coordinates and observer&#8217;s coordinates. It works either in batch mode, where the table stored in file is converted and saved to another file, or in terminal mode, where the user enters simple commands and queries by keyboard. </p>
<p> When running the batch mode, the program reads the source file line by line, and expects the JD value in the first column, which must be divided at least one of common used dividers (semicolon, comma, space, tab char, &#8230;). The JD value can be in full (2453xxx.x) or short (53xxx.x) form. Decimal places must be separated by point, not comma. The lines, which doesn&#8217;t consist of valid julian date, are copied into output without any change. In other cases the heliocentric correction is computed, its value is added to or subtracted from read julian date and the old JD value is replaced by the new one in the same form (full or short form, number of decimal places). The rest of the line is unchanged. </p>
<p> In terminal mode, the opening informations is displayed and the program prompts the user to enter object&#8217;s coordinates. First, specify right ascension (<i>R.A.</i>) a confirm by the Enter key. By the same way, the declination (<i>DEC.</i>) is set up. The value is printed out as response to the command. Then, by the same way again, the observer&#8217;s geographical longitude (<i>LON.</i>) and latitude (<i>LAT.</i>) is entered. Use positive values of latitude to the north of equator. Positive values of longitude means, that the location is to the east of zero meridian. After setting up coordinates, entering of a julian date is expected (<i>JD</i>). The user enters the julian date and the program computes and prints out the values of azimuth, altitude and value of airmass coefficient. All commands are descibed below. Entering the <i>q</i> command exits the program. </p>
<h2>OPTIONS</h2>
<p> The list of input files is usualy entered directly on the command line. If you are going to process a large set of files, you can use the question marks (for a single chars) or the asterisk (for a strings of chars). </p>
<p> The alternate way, how to process a large set of files, is the batch mode. In this mode, the list of input files is read from a given file or from the standard input. The directory file, for example named <i>dirfile</i>, must have the text format and the names of the input files are written on the separate lines. If the files are placed not in the current working directory, you have to specify the proper path in full or shortened form. </p>
<p> The <i>mask</i> parameters allows to set the naming of output files. The mask consists of letters, numbers and other characters allowed in the file name by the operating system. The special meaning has the question mark or the sequence of it. They will be replaced by the ordinal number of the output file, the number is always indented by leading zeros to the same number of decimal places as the number of the question marks. For example, when the mask <i>amass????.fts</i> is given, the output files named <i>amass0001.fts, amass0002.fts, amass0003.fts</i> will be generated. </p>
<dl>
<dt><code>@</code><i>dirfile</i></p>
<dd> The program will read the list of source files from specified file.</p>
<dt><code>@</code></p>
<dd> The program will read the list of source files from stdin.</p>
<dt><code>mask=</code><i>mask</i>, <code>-o</code><i>mark</i></p>
<dd> Mask of the output file(s). Default is <i>amass????.dat</i>.</p>
<dt><code>-c</code><i>x</i></p>
<dd> Initial counter value. Default is 1.</p>
<dt><code>ra=</code><i>hhmmss</i></p>
<dd> Object&#8217;s right ascension.</p>
<dt><code>dec=</code><i>+dddmmss</i></p>
<dd> Object&#8217;s declination.</p>
<dt><code>lon=</code><i>+dddmmss</i></p>
<dd> Observers&#8217;s geographical longitude.</p>
<dt><code>lat=</code><i>+dddmmss</i></p>
<dd> Observer&#8217;s geographical latitude.</p>
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
<p> The program adds values of airmass coefficient to the table stored in <i>data.dat</i> file and the resulting table stores in <i>helioc.dat</i> file. The object&#8217;s coordinates are R.A. = 18h 29m 32s, DEC. = +22d 34m 24s, the observer&#8217;s coordinates are LON. = 16d 40m = 16.6667 deg. to the east of the zero meridian and LAT. = 49d 13m = 49.2167 deg. to the north of the equator.</p>
<dl>
<dt>
<dd> <code>airmass lon=16.6667 lat=49.2167 ra=182932 dec=223424 data.dat</code> </p>
</dl>
<h2>EXIT STATUS</h2>
<p> airmass returns a zero exist status if it succeeds to convert all specified file. Otherwise, it will stop immediately when the error occurs and returns nonzero code. </p>
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
