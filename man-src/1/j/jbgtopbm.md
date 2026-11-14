---
title: "jbgtopbm(1)"
name: "jbgtopbm"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jbgtopbm/"
description: "jbgtopbm – JBIG1 to portable bitmap file converter"
---

<h2>NAME</h2>
<p> jbgtopbm &#8211; JBIG1 to portable bitmap file converter</p>
<h2>SYNOPSIS</h2>
<p> <code>jbgtopbm</code> [ <i>options</i> ] [ <i>input-file</i> | &#8211; [ <i>output-file</i> ]] </p>
<h2>DESCRIPTION</h2>
<p> Reads in a <i>JBIG1</i> bi-level image entity (BIE) from a file or standard input, decompresses it, and outputs a portable bitmap (PBM) file. </p>
<p> <i>JBIG1</i> is a highly effective lossless compression algorithm for bi-level images (one bit per pixel), which is particularly suitable for scanned document pages. </p>
<p> A <i>JBIG1</i> encoded image can be stored in several resolutions in one or several BIEs. All resolution layers except the lowest one are stored efficiently as differences to the next lower resolution layer. Options <code>-x</code> and <code>-y</code> can be used to stop the decompression at a specified maximal output image size. With option <code>-m</code> the input file can consist of multiple concatenated BIEs which contain different increasing resolution layers of the same image. </p>
<p> If more than one bit per pixel is stored in the JBIG1 file, then a PGM file will be produced.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;</code></p>
<dd> A single hyphen instead of an input file name will cause <i>jbgtopbm</i> to read the data from standard input instead from a file.</p>
<dt><code>-x</code><i> number</i></p>
<dd> Decode only up to the largest resolution layer which is still not more than <i>number</i> pixels wide. If no such resolution layer exists, then use the smallest one available.</p>
<dt><code>-y</code><i> number</i></p>
<dd> Decode only up to the largest resolution layer which is still not more than <i>number</i> pixels high. If no such resolution layer exists, then use the smallest one available. Options <code>-x</code> and <code>-y</code> can also be used together in which case the largest layer that satisfies both limits will be selected.</p>
<dt><code>-m</code></p>
<dd> Process multiple concatenated BIEs. If there are bytes left after the final SDE in the first BIE, then with this option <i>jbgtopbm</i> will attempt to decode these as the start of another BIE that may contain higher resolution data. Normally, any remaining bytes will generate a warning message.</p>
<dt><code>-b</code></p>
<dd> Use binary values instead of Gray code words in order to decode pixel values from multiple bitplanes. This option has only an effect if the input has more than one bitplane and a PGM output file is produced. Note that the decoder has to be used in the same mode as the encoder and cannot determine from the BIE, whether Gray or binary code words were used by the encoder.</p>
<dt><code>-d</code></p>
<dd> Diagnose a single BIE. With this option, <i>jbgtopbm</i> will print a summary of the header information found in the input file, followed by a list of all PSCD and ESC marker sequences encountered until the end of the file is reached.</p>
<dt><code>-p</code><i> number</i></p>
<dd> If the input contains multiple bitplanes, then extract only the specified single plane as a PBM file. The first plane has number 0.</dl>
<h2>BUGS</h2>
<p> Using standard input and standard output for binary data works only on systems where there is no difference between binary and text streams (e.g., Unix). On other systems (e.g., MS-DOS), using standard input or standard output may cause control characters like CR or LF to be inserted or deleted and this will damage the binary data.</p>
<h2>STANDARDS</h2>
<p> This program implements the <i>JBIG1</i> image coding algorithm as specified in ISO/IEC 11544:1993 and ITU-T T.82(1993).</p>
<h2>AUTHOR</h2>
<p> The <i>jbgtopbm </i> program is part of the <i>JBIG-KIT</i> package, which has been developed by Markus Kuhn. The most recent version of this portable <i>JBIG1</i> library and tools set is available from &lt;<a rel="nofollow" href="http://www.cl.cam.ac.uk/~mgk25/jbigkit/">http://www.cl.cam.ac.uk/~mgk25/jbigkit/</a>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pbm/">pbm</a>(5), <a href="/docs/linux/man/5-pgm/">pgm</a>(5), <a href="/docs/linux/man/1-pbmtojbg/">pbmtojbg</a>(1) </p>
<h2>Index</h2>
