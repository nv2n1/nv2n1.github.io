---
title: "libpbm(3)"
name: "libpbm"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libpbm/"
description: "libpbm – libnetpbm functions to read and write PBM image files"
---

<h2 class="name">NAME</h2>
<p> libpbm &#8211; libnetpbm functions to read and write PBM image files</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;netpbm/pbm.h&gt;</code> </p>
<p> <code>bit **pbm_allocarray(int</code> <i>cols</i><code>, int </code><i>rows</i><code>);</code> </p>
<p> <code>bit *pbm_allocrow(int</code> <i>cols</i><code>);</code> </p>
<p> <code>pbm_freearray(bit </code> <code>**</code><i>bits</i><code>, int </code><i>rows</i><code>);</code> </p>
<p> <code>pbm_freerow(bit</code> <code>*</code><i>bitrow</i><code>);</code> </p>
<p> <code>void pbm_readpbminit(FILE *</code> <i>fp</i><code>, int *</code><i>colsP</i><code>, int *</code><i>rowsP</i><code>, int *</code><i>formatP</i><code>);</code> </p>
<p> <code>void pbm_readpbmrow(FILE *</code> <i>fp</i><code>, bit *</code><i>bitrow</i><code>, int </code><i>cols</i><code>, int </code><i>format</i><code>);</code> </p>
<p> <code>void pbm_readpbmrow_packed(FILE *</code> <i>fp</i><code>,</code> <code>unsigned char * const </code><i>packed_bits</i><code>,</code> <code>const int </code><i>cols</i><code>,</code> <code>const int </code><i>format</i><code>);</code> </p>
<p> <code>void bit** pbm_readpbm(FILE *</code> <i>fp</i><code>, int *</code><i>colsP</i><code>, int *</code><i>rowsP</i><code>);</code> </p>
<p> <code>void pbm_writepbminit(FILE *</code> <i>fp</i><code>, int </code><i>cols</i><code>, int </code><i>rows</i><code>, int </code><i>forceplain</i><code>);</code> </p>
<p> <code>void pbm_writepbmrow(FILE *</code> <i>fp</i><code>, bit *</code><i>bitrow</i><code>, int </code><i>cols</i><code>, int </code><i>forceplain</i><code>);</code> </p>
<p> <code>void pbm_writepbmrow_packed(FILE *</code> <i>fp</i><code>,</code> <code>unsigned char * const </code><i>packed_bits</i><code>,</code> <code>const int </code><i>cols</i><code>,</code> <code>const int </code><i>forceplain</i><code>);</code> </p>
<p> <code>void pbm_writepbm(FILE *</code> <i>fp</i><code>, bit **</code><i>bits</i><code>, int </code><i>cols</i><code>, int </code><i>rows</i><code>, int </code><i>forceplain</i><code>);</code> </p>
<p> <code>#define pbm_packed_bytes(</code><i>cols</i><code>) &#8230;</code> </p>
<p> <code>void pbm_nextimage(</code> <code>FILE *</code><i>file</i><code>,</code> <code>int * const </code><i>eofP</i><code>);</code> </p>
<p> <code>void pbm_check(</code> <code>FILE * </code><i>file</i><code>,</code> <code>const enum pm_check_type </code><i>check_type</i><code>,</code> <code>const int </code><i>format</i><code>,</code> <code>const int </code><i>cols</i><code>,</code> <code>const int </code><i>rows</i><code>,</code> <code>enum pm_check_code * const </code><i>retval</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> These library functions are part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<h3>TYPES AND CONSTANTS</h3>
<p> <code>typedef &#8230; bit;</code> </p>
<p> <code>#define PBM_WHITE &#8230;</code> </p>
<p> <code>#define PBM_BLACK &#8230;</code> </p>
<p> Each <code>bit</code> should contain only the values of <code>PBM_WHITE</code> or <code>PBM_BLACK</code>. </p>
<p> <code>#define PBM_FORMAT &#8230;</code> </p>
<p> <code>#define RPBM_FORMAT &#8230;</code> </p>
<p> <code>#define PBM_TYPE PBM_FORMAT</code> </p>
<p> <code>#define </code> <code>PBM_FORMAT_TYPE(</code><i>f</i><code>) &#8230;</code> </p>
<p> These are for distinguishing different file formats and types. </p>
<h3>INITIALIZATION</h3>
<p> <code>pbm_init()</code> is obsolete (at least since Netpbm 9.25 (March 2002)). Use <code>pm_proginit()</code> instead. </p>
<p> <code>pbm_init()</code> is identical to <code>pm_proginit</code>. </p>
<h3>MEMORY MANAGEMENT</h3>
<p> <code>pbm_allocarray()</code> allocates an array of bits. <code>pbm_allocrow()</code> allocates a row of the given number of bits. <code>pbm_freearray()</code> frees the array allocated with <code>pbm_allocarray()</code> containing the given number of rows. <code>pbm_freerow()</code> frees a row of bits. </p>
<h3>READING PBM IMAGE FILES</h3>
<p> <code>pbm_readpbminit()</code> reads the header from a PBM image in a PBM file, filling in the rows, cols and format variables. <code>pbm_readpbmrow()</code> reads a row of bits into the <i>bitrow </i> array. Format and cols were filled in by <code>pbm_readpbminit()</code>. </p>
<p> <code>pbm_readpbmrow_packed()</code> is like <code>pbm_readpbmrow()</code> except instead of returning a <code>bits</code> array, it returns an array <i>packed_bits</i> of bytes with the pixels of the image row packed into them. The pixels are in order from left to right across the row and from the beginning of the array to the end. Within a byte, the bits are in order from the most significant bit to the least significant bit. If the number of pixels in the row is not a multiple of 8, the last byte returned is padded on the least significant bit side with undefined bits. White is represented by a <code>PBM_WHITE</code> bit; black by <code>PBM_BLACK</code>. </p>
<p> <code>pbm_readpbm()</code> reads an entire bitmap file into memory, returning the allocated array and filling in the rows and cols variables. This function combines <code>pbm_readpbminit()</code>, <code>pbm_allocarray()</code> and <code>pbm_readpbmrow()</code>. </p>
<p> <code>pbm_readpbminit()</code> and <code>pbm_readpbm</code> abort the program with a message to Standard Error if the PBM image header is not syntactically valid, including if it contains a number too large to be processed using the system&#8217;s normal data structures (to wit, a number that won&#8217;t fit in a C &#8216;int&#8217;). </p>
<p> <code>ppm_readppminit()</code> and <code>ppm_readppm</code> abort the program with a message to Standard Error if the PPM image header is not syntactically valid, including if it contains a number too large to be processed using the system&#8217;s normal data structures (to wit, a number that won&#8217;t fit in a C &#8216;int&#8217;). </p>
<h3>WRITING PBM IMAGE FILES</h3>
<p> <code>pbm_writepbminit()</code> writes the header for a PBM image in a PBM file. <i>forceplain</i> is a boolean value specifying that a plain format (text) file to be written, as opposed to a raw format (binary) one. <code>pbm_writepbmrow()</code> writes a row to a PBM file. <code>pbm_writepbmrow_packed()</code> is the same as <code>pbm_writepbmrow()</code> except that you supply the row to write as an array of bytes packed with bits instead of as a <code>bits</code> array. The format of <i>packed_bits </i> is the same as that returned by <code>pbm_readpbmrow()</code>. </p>
<p> <code>pbm_writepbm()</code> writes the header and all data for a PBM image to a PBM file. This function combines <code>pbm_writepbminit()</code> and <code>pbm_writepbmrow()</code>. </p>
<h3>MISCELLANEOUS</h3>
<p> <code>pbm_nextimage()</code> positions a PBM input file to the next image in it (so that a subsequent <code>pbm_readpbminit()</code> reads its header). </p>
<p> Immediately before a call to <code>pbm_nextimage()</code>, the file must be positioned either at its beginning (i.e. nothing has been read from the file yet) or just after an image (i.e. as left by a <code>pbm_readpbmrow() </code> of the last row in the image). </p>
<p> Note that in the raw PNM and PAM format, the next image always starts immediately after the previous image, so all <code>pbm_nextimage()</code> really does is test whether there is a next image or the file is positioned at end-of-file. In plain PNM, though, there may be white space between images. </p>
<p> If <code>pbm_nextimage() </code> successfully positions to the next image, it returns <code>*</code><i>eofP</i> false (0). If there is no next image in the file, it returns <code>*</code><i>eofP</i> true . If it can&#8217;t position or determine the file status due to a file error, it throws an error . </p>
<p> <code>pbm_check()</code> checks for the common file integrity error where the file is the wrong size to contain all the image data. <code>pbm_check()</code> assumes the file is positioned after an image header (as if <code>pbm_readpbminit() </code> was the last operation on the file). It checks the file size to see if the number of bytes left in the file are the number required to contain the image raster. If the file is too short, <code>pbm_check()</code> causes the program t throws an error . Otherwise, it returns one of the following values (enumerations of the <code>enum pm_check_code</code> type) as <code>*</code><i>retval</i>: </p>
<dl>
<dt><code>PM_CHECK_OK</code></p>
<dd> The file&#8217;s size is exactly what is required to hold the image raster. </p>
<dt><code>PM_CHECK_UNKNOWN_TYPE</code></p>
<dd> <i>format</i> is not a format whose size <code>pbm_check()</code> can anticipate. The only format with which <code>pbm_check()</code> can deal is raw PBM format. </p>
<dt><code>PM_CHECK_TOO_LONG</code></p>
<dd> The file is longer than it needs to be to contain the image raster. The extra data might be another image. </p>
<dt><code>PM_CHECK_UNCHECKABLE</code></p>
<dd> The file is not a kind that has a predictable size, so there is no simple way for <code>pbm_check()</code> to know if it is the right size. Only a regular file has predictable size. A pipe is a common example of a file that does not. </p>
</dl>
<p> <i>check_type</i> must have the value <code>PM_CHECK_BASIC </code> (an enumerated value of the <code>pm_check_type</code> enumerated type). Otherwise, the effect of <code>pbm_check()</code> is unpredictable. This argument exists for future backward compatible expansion of the function of <code>pbm_check()</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-libpgm/">libpgm</a></code>(1) , <code><a href="/docs/linux/man/1-libppm/">libppm</a></code>(1) , <code><a href="/docs/linux/man/1-libpnm/">libpnm</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Tony Hansen and Jef Poskanzer. </p>
<h2>Index</h2>
