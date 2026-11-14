---
title: "pamtopfm(1)"
name: "pamtopfm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtopfm/"
description: "pamtopfm – Convert Netpbm image to PFM (Portable Float Map)"
---

<h2>NAME</h2>
<p> pamtopfm &#8211; Convert Netpbm image to PFM (Portable Float Map) </p>
<h2>SYNOPSIS</h2>
<p> <code>pamtopfm</code> [<code>-endian=</code>{<code>big</code>|<code>little</code>}] [<code>-scale=</code><i>float</i>] [<i>imagefile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtopfm</code> reads a Netpbm image (PNM or PAM) and converts it to a PFM (Portable Float Map) image. </p>
<p> The PFM (Portable Float Map) image format is a lot like PPM, but uses floating point numbers with no maxval to achieve a High Dynamic Range (HDR) format. That means it doesn&#8217;t have a concept of absolute color and it can represent generic light intensity information rather than just visual information like PPM does. For example, two pixels that are so close in intensity that the human eye cannot tell them apart are not visually distinct, so a visual image format such as PPM would have no reason to use different sample values for them. But an HDR format would. </p>
<p> There are details of the PFM format in the <code>PFM</code> Format Description (1) </p>
<p> USC&#8217;s HDRShop program and a program called Lefty use it. </p>
<p> <code>pamtopfm</code> creates a color PFM image if its input is RGB (PPM) and a non-color PFM otherwise. </p>
<p> Use <code><a href="/docs/linux/man/1-pfmtopam/">pfmtopam</a></code>(1)<br />
&nbsp;<wbr>to convert a PFM image to Netpbm format. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-scale=</code><i>float</i></p>
<dd>
<p> This specifies the scale factor of the PFM image.<br />
&nbsp;<wbr>&nbsp;<wbr>Scale factor is a component of the PFM format.<br />
&nbsp;<wbr>&nbsp;<wbr>Default is 1.0. </p>
<dt><code>-endian=</code>{<code>big</code>|<code>little</code>}</p>
<dd>
<p> This specifies the endianness of the PFM image. The samples<br />
&nbsp;<wbr>&nbsp;<wbr>in the raster of a PFM image are 4 byte IEEE floating point<br />
&nbsp;<wbr>&nbsp;<wbr>numbers.&nbsp;<wbr>&nbsp;<wbr>A parameter of the IEEE format, and therefore the PFM<br />
&nbsp;<wbr>&nbsp;<wbr>format, is endianness, i.e. whether the specified bytes are<br />
&nbsp;<wbr>&nbsp;<wbr>ordered from low addresses to high addresses or vice versa. </p>
<p> <code>big</code> means big endian &#8212; the natural ordering;<br />
&nbsp;<wbr>&nbsp;<wbr><code>little</code>&nbsp;<wbr>means little-endian, the Intel-friendly ordering. </p>
<p> Default is whichever endianness the machine on which <code>pamtopfm</code><br />
&nbsp;<wbr>&nbsp;<wbr>runs uses internally, which results in the faster execution. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) , <code><a href="/docs/linux/man/1-pfmtopam/">pfmtopam</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamtopfm</code> was added to Netpbm in Release 10.22 (April 2004). </p>
<h2>Index</h2>
