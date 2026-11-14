---
title: "libnetpbm(3)"
name: "libnetpbm"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnetpbm/"
description: "libnetpbm – general introduction to the netpbm library"
---

<h2 class="name">NAME</h2>
<p> libnetpbm &#8211; general introduction to the netpbm library </p>
<h2>DESCRIPTION</h2>
<p> <code>libnetpbm</code> is a C programming library for reading, writing, and manipulating Netpbm images. It also contains a few general graphics manipulation tools, but it is not intended to be a graphics tools library. For graphics tools, Netpbm expects you to run the Netpbm programs. From a C program, the <code>libnetpbm</code> function <code>pm_system()</code> makes this easy. However, since it creates a process and execs a program, this may be too heavyweight for some applications. </p>
<p> To use <code>libnetpbm</code> services in your C program, #include the <code>pam.h</code> interface header file. For historical reasons, you can also get by in some cases with <code>pbm.h</code>, <code>pgm.h</code>, <code>ppm.h</code>, or <code>pnm.h</code>, but there&#8217;s really no point to that anymore. </p>
<p> The <code>libnetpbm</code> functions are divided into these categories: </p>
<dl>
<dt>&bull;</p>
<dd> PBM functions. These have names that start with <code>pbm</code> and work only on PBM images.</p>
<dt>&bull;</p>
<dd> PGM functions. These have names that start with <code>pgm</code> and work only on PGM images.</p>
<dt>&bull;</p>
<dd> PPM functions. These have names that start with <code>ppm</code> and work only on PPM images.</p>
<dt>&bull;</p>
<dd> PNM functions. These have names that start with <code>pnm</code> and work on PBM, PGM, and PPM images.</p>
<dt>&bull;</p>
<dd> PAM functions. These also have names that start with <code>pnm</code> and work on all the Netpbm image types.</p>
<dt>&bull;</p>
<dd> PM functions. These are utility functions that aren&#8217;t specific to any particular image format. </p>
</dl>
<p> For new programming, you rarely need to concern yourself with the PBM, PGM, PPM, and PNM functions, because the newer PAM functions do the same thing and are easier to use. For certain processing of bi-level images, the PBM functions are significantly more efficient, though. </p>
<p> <code>libnetpbm</code> has a backward compatibility feature that means a function designed to read one format can read some others too, converting on the fly. In particular, a function that reads a PGM image will also read a PBM image, but converts it as it reads it so that for programming purposes, it is a PGM image. Similarly, a function that reads PPM can read PBM and PGM as well. And a function that reads PBM, PGM, or PPM can read a PAM that has an equivalent tuple type. </p>
<p> For each of the five classes of <code>libnetpbm</code> image processing functions, <code>libnetpbm</code> has in in-memory representation for a pixel, a row, and a whole image. Do not confuse this format with the actual image format, as you would see in a file. The <code>libnetpbm</code> in-memory format is designed to make programming very easy. It is sometimes extremely inefficient, even more than the actual image format. For example, a pixel that a PPM image represents with 3 bytes, <code>libnetpbm</code>&#8216;s PAM functions represent with 16 bytes. A pixel in a PBM image is represented by a single bit, but the PNM functions represent that pixel in memory with 96 bits. </p>
<p> See <code>Libnetpbm</code>User&#8217;s<code><a href="/docs/linux/man/1-manual/">Manual</a></code>(1)<br />
&nbsp;<wbr>for the basics on using <code>libnetpbm</code> in a program. </p>
<p> You can look up the reference information for a particular function in <code>The</code>libnetpbm<code><a href="/docs/linux/man/1-directory/">Directory</a></code>(1) </p>
<p> Before Netpbm release 10 (June 2002), this library was split into four: libpbm, libpgm, libppm, and libpnm. That&#8217;s largely the reason for the multiple sets of functions and scattered documentation. </p>
<h2>Index</h2>
