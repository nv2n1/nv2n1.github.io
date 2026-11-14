---
title: "pampick(1)"
name: "pampick"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pampick/"
description: "pampick – pick images out of a multi-image Netpbm image stream"
---

<h2 class="name">NAME</h2>
<p> pampick &#8211; pick images out of a multi-image Netpbm image stream</p>
<h2>SYNOPSIS</h2>
<p> <code>pampick</code> </p>
<p> <i>image_sequence_number</i> &#8230; </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pampick</code> reads a PNM or PAM image stream as input. It picks certain images from the stream and copies them to a new image stream on Standard Output. </p>
<p> You identify the images to pick by sequence number within the stream. Each <i>image_sequence_number</i> is a decimal sequence number, with zero meaning the first image. </p>
<p> The arguments must be in increasing order, without duplicates. The results are undefined if they are not. (There are a number of enhancements that might be made in future releases that would make whatever <code>pampick</code> does today when you break this rule change). <code>pampick</code> outputs the images in the same order as they appear in the input. If you specify no sequence numbers, <code>pampick</code> outputs nothing. If you specify a sequence number that is beyond what is in the input, <code>pampick</code> fails with an error message to that effect. </p>
<p> <code>pampick</code> always reads the entire input stream. (This is helpful when the input stream is a pipe and whatever is feeding the pipe would be upset if it filled up or broke). </p>
<p> To see how many images, and what kind, are in a stream, use <code>pamfile</code>. </p>
<p> To extract all the images in a stream into separate named files, use <code>pamsplit</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamfile/">pamfile</a></code>(1) , <code><a href="/docs/linux/man/1-pamsplit/">pamsplit</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code>cat</code> man page </p>
<h2>HISTORY</h2>
<p> <code>pampick</code> was new in Netpbm 10.31 (December 2005); </p>
<h2>Index</h2>
