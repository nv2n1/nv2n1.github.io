---
title: "pamsplit(1)"
name: "pamsplit"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamsplit/"
description: "pamsplit – split a multi-image Netpbm file into single-image files"
---

<h2 class="name">NAME</h2>
<p> pamsplit &#8211; split a multi-image Netpbm file into single-image files</p>
<h2>SYNOPSIS</h2>
<p> <code>pamsplit</code> </p>
<p> [<i>netpbmfile</i> </p>
<p> [<i> output_file_pattern</i>]] </p>
<p> [<code>-padname=</code><i>n</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamsplit</code> reads a PNM or PAM stream as input. It copies each image in the input into a separate file, in the same format. </p>
<p> <i>netpbmfile</i> is the file name of the input file, or <code>&#8211;</code> to indicate Standard Input. The default is Standard Input. </p>
<p> <i>output_file_pattern</i> tells how to name the output files. It is the file name of the output file, except that the first occurrence of &#8216;%d&#8217; in it is replaced by the image sequence number in unpadded ASCII decimal, with the sequence starting at 0. If there is no &#8216;%d&#8217; in the pattern, <code>pamsplit</code> fails. </p>
<p> The default output file pattern is &#8216;image%d&#8217;. </p>
<p> The <code>-padname</code> option specifies to how many characters you want the image sequence number in the output file name padded with zeroes. <code>pamsplit</code> adds leading zeroes to the image sequence number to get up to at least that number of characters. This is just the number of characters in the sequence number part of the name. For example, <tt>pamsplit - outputfile%d.ppm -padname=3</tt> would yield output filenames <code>outputfile000.ppm</code>, <code>outputfile001.ppm</code>, etc. </p>
<p> The default is no padding (equivalent to <code>-padname=0</code>). </p>
<p> The <code>-padname</code> option was new in Netpbm 10.23 (July 2004). Before that, there was never any padding. </p>
<p> Note that to do the reverse operation (combining multiple single-image Netpbm files into a multi-image one), there is no special Netpbm program. Just use <code>cat</code>. </p>
<p> If you just want to find out basic information about the images in a stream, you can use <code>pamfile</code> on the stream. </p>
<p> To extract images from a stream and generate a single stream containing them, use <code>pampick</code>. </p>
<p> To run a program on each image in a stream without the hassle of temporary files, use <code>pamexec</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamfile/">pamfile</a></code>(1) , <code><a href="/docs/linux/man/1-pampick/">pampick</a></code>(1) , <code><a href="/docs/linux/man/1-pampick/">pampick</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code>cat</code> man page </p>
<h2>Index</h2>
