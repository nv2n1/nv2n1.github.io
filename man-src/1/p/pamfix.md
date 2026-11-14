---
title: "pamfix(1)"
name: "pamfix"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamfix/"
description: "pamfix – repair a Netpbm image with various corruptions"
---

<h2 class="name">NAME</h2>
<p> pamfix &#8211; repair a Netpbm image with various corruptions</p>
<h2>SYNOPSIS</h2>
<p> <code>pamfix</code> </p>
<p> [<code>-verbose</code>] </p>
<p> [<i>netpbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamfix</code> reads a stream that is mostly a Netpbm image but may have certain types of corruptions and produces a valid Netpbm image that preserves much of the information in the original. In particular, Netpbm salvages streams that are truncated and that contain illegally large sample values. </p>
<p> <code>pamfix</code> looks at only on the first image in a multi-image stream. </p>
<h3>Truncated stream</h3>
<p> This is an stream that is missing the last part. Netpbm corrects this by creating an output image that simply has fewer rows. </p>
<p> You select this kind of repair with a <code>-truncate</code> option. </p>
<p> The header of a Netpbm image implies how large the image must be (how many bytes the file must contain). If the file is actually smaller than that, a Netpbm program that tries to read the image fails, with an error message telling you that it couldn&#8217;t read the whole file. The data in the file is arranged in row order, from top to bottom, and the most common reason for the file being smaller than its header says it should be is because the bottommost rows are simply missing. So <code>pamfix</code> assumes that is the case and generates a new image with just the rows that are readable. (technically, that means the output&#8217;s header indicates a smaller number of rows and omits any partial last row). </p>
<p> The most common way for a Netpbm file to be small is that something interrupted the program that generated it before it was finished writing the file. For example, the program ran out of its own input or encountered a bug or ran out of space in which to write the output. </p>
<p> Another problem <code>pamfix</code> deals with is where the file isn&#8217;t actually too small, but because of a system error, a byte in the middle of it cannot be read (think of a disk storage failure). <code>pamfix</code> reads the input sequentially until it can&#8217;t read any further, for any reason. So it treats such an image as a truncated one, ignoring all data after the unreadable byte. </p>
<p> But be aware that an image file is sometimes too small because of a bug in the program that generated it, and in that case it is not simply a matter of the bottom of the image missing, so <code>pamfix</code> simply creates a valid Netpbm image containing a garbage picture. </p>
<p> If you want to test an image file to see if it is corrupted by being too small, use <code>pamfile &#8211;allimages</code> . It fails with an error message if the file is too small. </p>
<p> If you want to cut the bottom off a valid Netpbm image, use <code>pamcut</code>. </p>
<h3>Excessive Sample Value</h3>
<p> This is a stream that contains a purported sample value that is higher than the maxval of the image. </p>
<p> The header of a Netpbm image tells the maxval of the image, which is a value that gives meaning to all the sample values in the raster. The sample values represent a fraction of the maxval, so a sample value that is greater than the maxval makes no sense. </p>
<p> A regular Netpbm program fails if you give it input that contains a value larger than the maxval where a sample value belongs. </p>
<p> <code>pamfix</code> has three ways of salvaging such a stream: </p>
<dl>
<dt>&bull;</p>
<dd> Clip to the maxval. Request this with <code>-clip</code>.</p>
<dt>&bull;</p>
<dd> Raise the maxval, thus lowering the fraction represented by every sample in the image. Request this with <code>-changemaxval</code>.</p>
<dt>&bull;</p>
<dd> Truncate the image at the first invalid sample value. Request this with <code>-truncate</code> and neither <code>-clip</code> nor <code>-changemaxval</code>. </p>
</dl>
<p> You cannot specify both <code>-clip</code> and <code>-changemaxval</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pamcut/">pamcut</a></code>(1) , <code><a href="/docs/linux/man/1-pamfile/">pamfile</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> <code>pamfix</code> was new in Netpbm 10.66 (March 2014). But it grew out of <code>pamfixtrunc</code>, which was new in Netpbm 10.38 (March 2007) and did only the truncated image repair (and for invalid sample values would simply pass them through to its output, generating an invalid Netpbm image). </p>
<h2>Index</h2>
