---
title: "pfm(5)"
name: "pfm"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pfm/"
description: "PFM – PFM graphic image file format"
---

<p>PFM &#8211; PFM graphic image file format</p>
<h2>Description</h2>
<p>This document describes the PFM graphic image file format as understood by the Netpbm converters <code><a href="/docs/linux/man/1-pamtopfm/">pamtopfm</a></code>(1)<br />
&nbsp;<wbr>and <code><a href="/docs/linux/man/1-pfmtopam/">pfmtopam</a></code>(1) There are multiple similar formats known as PFM in the world, none of them authoritatively documented. The format described here is one that Bryan Henderson deduced from a program he found somewhere that dealt with a &#8216;PFM&#8217; format. The PFM format is inspired by the Netpbm formats, and you will see lots of similarity. It is not, however, an official Netpbm format. Its goal is not consistent with those of Netpbm formats. </p>
<h2>The format</h2>
<p>A PFM image is a stream of bytes. The stream consists of a header followed immediately by a raster. These two components are described below. There are no delimeters before or after the sections as described.</p>
<h3>PFM header</h3>
<p>The PFM header is 3 consecutive &#8216;lines&#8217; of ASCII text. After each line is a white space character. That character is typically a newline character, hence the term &#8216;line,&#8217; but doesn&#8217;t have to be. </p>
<p> <code>pamtopfm</code> uses a newline in the PFM it generates. </p>
<p> <code>Identifier Line</code> </p>
<p> The identifier line contains the characters &#8216;PF&#8217; or &#8216;Pf&#8217;. PF means it&#8217;s a color PFM. Pf means it&#8217;s a grayscale PFM. </p>
<p> <code>Dimensions Line</code> </p>
<p> The dimensions line contains two positive decimal integers, separated by a blank. The first is the width of the image; the second is the height. Both are in pixels. </p>
<p> <code>Scale Factor / Endianness</code> </p>
<p> The Scale Factor / Endianness line is a queer line that jams endianness information into an otherwise sane description of a scale. The line consists of a nonzero decimal number, not necessarily an integer. If the number is negative, that means the PFM raster is little endian. Otherwise, it is big endian. The absolute value of the number is the scale factor for the image. </p>
<p> The scale factor tells the units of the samples in the raster. You use somehow it along with some separately understood unit information to turn a sample value into something meaningful, such as watts per square meter.</p>
<h3>PFM raster</h3>
<p>The raster is a sequence of pixels, packed one after another, with no delimiters of any kind. They are grouped by row, with the pixels in each row ordered left to right and the rows ordered bottom to top. </p>
<p> Each pixel consists of 1 or 3 samples, packed one after another, with no delimiters of any kind. 1 sample for a grayscale PFM and 3 for a color PFM (see the Identifier Line of the PFM header). </p>
<p> Each sample consists of 4 consecutive bytes. The bytes represent a 32 bit string, in either big endian or little endian format, as determined by the Scale Factor / Endianness line of the PFM header. That string is an IEEE 32 bit floating point number code. Since that&#8217;s the same format that most CPUs and compiler use, you can usually just make a program use the bytes directly as a floating point number, after taking care of the endianness variation.</p>
