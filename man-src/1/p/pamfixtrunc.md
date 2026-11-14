---
title: "pamfixtrunc(1)"
name: "pamfixtrunc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamfixtrunc/"
description: "pamfixtrunc – repair a Netpbm image whose file is truncated"
---

<h2 class="name">NAME</h2>
<p> pamfixtrunc &#8211; repair a Netpbm image whose file is truncated</p>
<h2>SYNOPSIS</h2>
<p> <code>pamfixtrunc</code> </p>
<p> [<code>-verbose</code>] </p>
<p> [<i>netpbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamfixtrunc</code> reads as much as it can of a Netpbm image that may be truncated (i.e. the file may not contain the last part of the image) and writes out a valid Netpbm image that is just missing the bottom rows of the original (pre-truncation) image. </p>
<p> The header of a Netpbm image implies how large the image must be (how many bytes the file must contain). If the file is actually smaller than that, a Netpbm program that tries to read the image fails, with an error message telling you that it couldn&#8217;t read the whole file. The data in the file is arranged in row order, from top to bottom, and the most common reason for the file being smaller than its header says it should be is because the bottommost rows are simply missing. So <code>pamfixtrunc</code> assumes that is the case and generates a new image with just the rows that are readable. (technically, that means the output&#8217;s header indicates a smaller number of rows and omits any partial last row). </p>
<p> The most common way for a Netpbm file to be small is that something interrupted the program that generated it before it was finished writing the file. For example, the program ran out of its own input or encountered a bug or ran out of space in which to write the output. </p>
<p> Another problem <code>pamfixtrunc</code> deals with is where the file isn&#8217;t actually too small, but due to a system error, a byte in the middle of it cannot be read (think of a disk storage failure). <code>pamfixtrunc</code> reads the input sequentially until it can&#8217;t read any further, for any reason. So it treats such an image as a truncated one, ignoring all data after the unreadable byte. </p>
<p> But be aware that an image file is sometimes too small because of a bug in the program that generated it, and in that case it is not simply a matter of the bottom of the image missing, so <code>pamfixtrunc</code> simply creates a valid Netpbm image containing a garbage picture. </p>
<p> <code>pamfixtrunc</code> looks at only on the first image in a multi-image stream. </p>
<p> If you want to test an image file to see if it is corrupted by being too small, use <code>pamfile &#8211;allimages</code> . It fails with an error message if the file is too small. </p>
<p> If you want to cut the bottom off a valid Netpbm image, use <code>pamcut</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pamcut/">pamcut</a></code>(1) , <code><a href="/docs/linux/man/1-pamfile/">pamfile</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> <code>pamfixtrunc</code> was new in Netpbm 10.38 (March 2007). </p>
<h2>Index</h2>
