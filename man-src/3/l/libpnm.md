---
title: "libpnm(3)"
name: "libpnm"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libpnm/"
description: "libpnm – libnetpbm functions to read and write PNM image files"
---

<h2 class="name">NAME</h2>
<p> libpnm &#8211; libnetpbm functions to read and write PNM image files</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;netpbm/pnm.h&gt;</code> </p>
<p> <code>void pnm_init(</code> <code>int *</code><i>argcP</i><code>,</code> <code>char *</code><i>argv</i><code>[]</code> <code>);</code> </p>
<p> <code>xel ** pnm_allocarray(</code> <code>int </code><i>cols</i><code>,</code> <code>int </code><i>rows</i><code>);</code> </p>
<p> <code>xel * pnm_allocrow(</code> <code>int </code><i>cols</i><code>);</code> </p>
<p> <code>void pnm_freearray(</code> <code>xel **</code><i>xels</i><code>,</code> <code>int </code><i>rows</i><code>);</code> </p>
<p> <code>void pnm_freerow(</code> <code>xel *</code><i>xelrow</i><code>);</code> </p>
<p> <code>void pnm_readpnminit( </code> <code>FILE *</code><i>fp</i><code>,</code> <code>int *</code><i>colsP</i><code>,</code> <code>int *</code><i>rowsP</i><code>,</code> <code>xelval *</code><i>maxvalP</i><code>,</code> <code>int *</code><i>formatP</i><code> );</code> </p>
<p> <code>void pnm_readpnmrow( </code> <code>FILE *</code><i>fp</i><code>,</code> <code>xel *</code><i>xelrow</i><code>,</code> <code>int </code><i>cols</i><code>,</code> <code>xelval </code><i>maxval</i><code>,</code> <code>int </code><i>format</i><code> );</code> </p>
<p> <code>xel ** pnm_readpnm( </code> <code>FILE *</code><i>fp</i><code>,</code> <code>int *</code><i>colsP</i><code>,</code> <code>int *</code><i>rowsP</i><code>,</code> <code>xelval *</code><i>maxvalP</i><code>, int</code><i>*</i><code> formatP </code><i>);</i> </p>
<p> <code>void pnm_writepnminit( </code> <code>FILE * fp , </code> <code>int </code><i>cols</i><code>,</code> <code>int </code><i>rows</i><code>,</code> <code>xelval </code><i>maxval</i><code>,</code> <code>int </code><i>format</i><code>,</code> <code>int </code><i>forceplain</i><code>);</code> </p>
<p> <code>void pnm_writepnmrow( </code> <code>FILE *</code><i>fp</i><code>,</code> <code>xel *</code><i>xelrow</i><code>,</code> <code>int cols</code><i>,</i> <code>xelval </code><i>maxval</i><code>,</code> <code>int </code><i>format</i><code>,</code> <code>int </code><i>forceplain</i><code> );</code> </p>
<p> <code>void pnm_writepnm( </code> <code>FILE *</code><i>fp</i><code>,</code> <code>xel ** </code><i>xels</i><code>,</code> <code>int </code><i>cols</i><code>,</code> <code>int </code><i>rows</i><code>,</code> <code>xelval </code><i>maxval</i><code>,</code> <code>int </code><i>format</i><code>,</code> <code>int </code><i>forceplain</i><code> );</code> </p>
<p> <code>void pnm_nextimage(</code><code>FILE *</code> <i>file</i><code>,</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>int&nbsp;<wbr>*&nbsp;<wbr>const</code>&nbsp;<wbr><i>eofP</i><code>);</code> </p>
<p> <code>void pnm_check(</code> <code>FILE * </code><i>file</i><code>,</code> <code>const enum pm_check_type </code><i>check_type</i><code>,</code> <code>const int </code><i>format</i><code>,</code> <code>const int </code><i>cols</i><code>,</code> <code>const int </code><i>rows</i><code>,</code> <code>const xelval </code><i>maxval</i><code>,</code> <code>enum pm_check_code *</code><i>retvalP</i><code>);</code> </p>
<p> <code>void pnm_promoteformatrow( </code> <code>xel *</code><i>xelrow</i><code>,</code> <code>int </code><i>cols</i><code>,</code> <code>xelval </code><i>maxval</i><code>,</code> <code>int </code><i>format</i><code>,</code> <code>xelval </code><i>newmaxval</i><code>,</code> <code>int </code><i>newformat</i><code>);</code> </p>
<p> <code>void pnm_promoteformat( </code> <code>xel **</code><i>xels</i><code>,</code> <code>int </code><i>cols</i><code>,</code> <code>xelval </code><i>maxval</i><code>,</code> <code>int </code><i>format</i><code>,</code> <code>xelval </code><i>newmaxval</i><code>,</code> <code>int </code><i>newformat</i><code>);</code> </p>
<p> <code>xel pnm_whitexel( </code> <code>xelval </code><i>maxval</i><code>,</code> <code>int </code><i>format</i><code>);</code> </p>
<p> <code>xel pnm_blackxel( </code> <code>xelval </code><i>maxval</i><code>,</code> <code>int </code><i>format</i><code>);</code> </p>
<p> <code>void pnm_invertxel( </code> <code>xel *</code><i>x</i><code>,</code> <code>xelval </code><i>maxval</i><code>,</code> <code>int </code><i>format</i><code>);</code> </p>
<p> <code>xel pnm_backgroundxelrow( </code> <code>xel *</code><i>xelrow</i><code>,</code> <code>int </code><i>cols</i><code>,</code> <code>xelval </code><i>maxval</i><code>,</code> <code>int </code><i>format</i><code>);</code> </p>
<p> <code>xel pnm_backgroundxel( </code> <code>xel **</code><i>xels</i><code>,</code> <code>int </code><i>cols</i><code>,</code> <code>int </code><i>rows</i><code>,</code> <code>xelval </code><i>maxval</i><code>,</code> <code>int </code><i>format</i><code>);</code> </p>
<p> <code>typedef &#8230; xelval;</code> </p>
<p> <code>typedef &#8230; xel;</code> </p>
<p> <code>#define </code> <code>PNM_ASSIGN1(</code><i>x</i><code>,</code><i>v</i><code>)</code> <code>&#8230;</code> </p>
<p> <code>#define </code> <code>PNM_GET1(</code><i>x</i><code>)</code> <code>&#8230;</code> </p>
<p> <code>#define </code> <code>PNM_EQUAL(</code><i>x</i><code>,</code><i>y</i><code>)</code> <code>&#8230;</code> </p>
<p> <code>#define </code> <code>PNM_FORMAT_TYPE(</code><i>format</i><code>)</code> <code>&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> These library functions are part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<h3>TYPES AND CONSTANTS</h3>
<p> Each <code>xel</code> contains three <code>xelval</code>s, each of which should contain only the values between <code>0</code> and <code>PNM_MAXMAXVAL</code>, inclusive. </p>
<h3>XEL MANIPULATIONS</h3>
<p> The <code>PNM_GET1</code> macro extracts a single value from an xel, when ou know it&#8217;s from a PBM or PGM file. When it&#8217;s from a PPM file, use <code>PPM_GETR()</code>, <code>PPM_GETG()</code>, and <code>PPM_GETB()</code>. </p>
<p> The <code>PNM_ASSIGN1</code> macro assigns a single value to an xel, when you know it&#8217;s from a PBM or PGM file. When it&#8217;s from a PPM file, use <code>PPM_ASSIGN</code>. </p>
<p> The <code>PNM_EQUAL</code> macro checks two xels for equality. The <code>PNM_FORMAT_TYPE</code> macro computes a format type code from a format code. The format types are PBM, PGM, PPM, and PAM. But note that PBM, PGM, and PPM each are two different formats: a plain one and a raw one. So there are four format types, but seven formats. <code>PNM_FORMAT_TYPE</code> does not work on the PAM format code. </p>
<p> <code>pnm_whitexel()</code> and <code>pnm_blackxel()</code> return a white or black xel, respectively, for the given <i>maxval</i> and <i>format</i>. </p>
<p> <code>pnm_invertxel()</code> inverts an xel. </p>
<h3>INITIALIZATION</h3>
<p> <code>pnm_init()</code> is obsolete (at least since Netpbm 9.25 (March 2002)). Use <code>pm_proginit()</code> instead. </p>
<p> <code>pnm_init()</code> is identical to <code>pm_proginit</code>. </p>
<h3>MEMORY MANAGEMENT</h3>
<p> <code>pnm_allocarray()</code> allocates space for an array of xels. <code>pnm_freearray()</code> frees an array space allocated by <code>pnm_allocarray()</code> or <code>pnm_readpnm()</code>. </p>
<p> <code>pnm_allocrow()</code> allocates space for a row of a PNM image. <code>pnm_freerow()</code> frees it. </p>
<h3>READING PNM FILES</h3>
<p> <code>pnm_readpnminit()</code> is similar to <code>pnm_readpaminit()</code>, but reads only PNM images and has a different parameter list. </p>
<p> <code>pnm_readpnmrow()</code> is similar to <code>pnm_readpamrow()</code> but only works on PNM images and has a different parameter list and returns the row as an array of xels instead of tuples. </p>
<p> <code>pnm_readpnm()</code> is similar to <code>pnm_readpam()</code> except that it reads only PNM images and uses a different parameter list and returns an array of rows such that <code>pnm_readpnmrow()</code> would return rather than such that <code>pnm_readpamrow()</code> would return. </p>
<h3>WRITING FILES</h3>
<p> <code>pnm_writepnminit()</code> is similar to <code>pnm_writepaminit()</code> except that it can write only a PNM header and has a different parameter list. </p>
<p> <i>forceplain</i> is a binary value. True (nonzero) means to write the image in the plain (ASCII) version of the selected format. False (zero) means to write it in the raw (binary) version of the selected format. See <code>PNM</code>format<code><a href="/docs/linux/man/1-specification/">specification</a></code>(1) </p>
<p> <code>pnm_writepnmrow()</code> is similar to <code>pnm_writepamrow()</code> except that it works only on PNM images and has a different parameter list and takes an array of xels instead of an array of tuples. See the description of <i>forceplain </i> above. </p>
<p> <code>pnm_writepnm()</code> is similar to <code>pnm_writepam()</code> except that it works only on PNM image, has a different parameter list, and takes an array of rows of xels instead of an array of rows of tuples. See the description of <i>forceplain</i> above. </p>
<h3>FORMAT PROMOTION</h3>
<p> <code>pnm_promoteformatrow()</code> promotes a row of xels from one maxval and format to a new set. Use this when you are combining multiple anymaps of different types &#8211; just take the maximum of the maxvals and the maximum of the formats, and promote them all to that. </p>
<p> <code>pnm_promoteformat()</code> promotes an entire anymap. </p>
<h3>MISCELLANEOUS</h3>
<p> <code>pnm_nextimage()</code> positions a PNM input file to the next image in it (so that a subsequent <code>pnm_readpnminit()</code> reads its header). </p>
<p> <code>pnm_nextimage()</code> is analogous to <code>pbm_nextimage()</code>, but works on PPM, PGM, and PBM files. </p>
<p>&nbsp;<wbr><code>pnm_check()</code>&nbsp;<wbr>is similar to&nbsp;<wbr><code>pnm_checkpam()</code>&nbsp;<wbr>except it works only on PNM images. </p>
<p> <code>pnm_check()</code> is identical to <code>ppm_check()</code>. </p>
<p> <code>pnm_backgroundxelrow()</code> figures out an appropriate background xel based on the row of xels <i>xelrow</i>, which is <i>cols</i> xels wide, has maxval <i>maxval</i>, and represents an image with format <i>format</i>. </p>
<p> This estimate works best when the row is the top or bottom row of the image. </p>
<p> <code>pnm_backgroundxel()</code> does the same thing as <code>pnm_backgroundxelrow()</code>, except based on an entire image instead of just one row. This tends to do a slightly better job than <code>pnmbackgroundxelrow()</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-libnetpbm/">Libnetpbm</a></code>(1) , <code>Libnetpbm</code>User&#8217;s<code><a href="/docs/linux/man/1-guide/">Guide</a></code>(1) , <code>Libnetpbm</code><a href="/docs/linux/man/1-directory/">Directory</a><code>(1)</code> , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) , <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-libpbm/">libpbm</a></code>(1) , <code><a href="/docs/linux/man/1-libpgm/">libpgm</a></code>(1) , <code><a href="/docs/linux/man/1-libppm/">libppm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Tony Hansen and Jef Poskanzer. </p>
<h2>Index</h2>
