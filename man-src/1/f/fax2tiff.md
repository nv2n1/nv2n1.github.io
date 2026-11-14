---
title: "fax2tiff(1)"
name: "fax2tiff"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fax2tiff/"
description: "fax2tiff – create a TIFF Class F fax file from raw fax data"
---

<h2>NAME</h2>
<p> fax2tiff &#8211; create a <font SIZE="-1">TIFF</font> Class F fax file from raw fax data</p>
<h2>SYNOPSIS</h2>
<p> <code>fax2tiff</code> [ <i>options</i> ] [ <code>-o</code> <i>output.tif</i> ] <i>input.raw</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Fax2tiff</i> creates a <font SIZE="-1">TIFF</font> file containing <font SIZE="-1">CCITT</font> Group 3 or Group 4 encoded data from one or more files containing &#8220;raw&#8221; Group 3 or Group 4 encoded data (typically obtained directly from a fax modem). By default, each row of data in the resultant <font SIZE="-1">TIFF</font> file is 1-dimensionally encoded and padded or truncated to 1728 pixels, as needed. The resultant image is a set of low resolution (98 lines/inch) or medium resolution (196 lines/inch) pages, each of which is a single strip of data. The generated file conforms to the <font SIZE="-1">TIFF</font> Class F (<font SIZE="-1">FAX</font>) specification for storing facsimile data. This means, in particular, that each page of the data does <code>not</code> include the trailing <i>return to control</i> (<font SIZE="-1">RTC</font>) code; as required for transmission by the <font SIZE="-1">CCITT</font> Group 3 specifications. The old, &#8220;classic&#8221;, format is created if the <code>-c</code> option is used. (The Class F format can also be requested with the <code>-f</code> option.) </p>
<p> The default name of the output image is <i>fax.tif</i>; this can be changed with the <code>-o</code> option. Each input file is assumed to be a separate page of facsimile data from the same document. The order in which input files are specified on the command line is the order in which the resultant pages appear in the output file.</p>
<h2>OPTIONS</h2>
<p> Options that affect the interpretation of input data are:</p>
<dl>
<dt><code>-3</code></p>
<dd> Assume input data is <font SIZE="-1">CCITT</font> Group 3 encoded (default).</p>
<dt><code>-4</code></p>
<dd> Assume input data is <font SIZE="-1">CCITT</font> Group 4 encoded.</p>
<dt><code>-U</code></p>
<dd> Assume input data is uncompressed (Group 3 or Group 4).</p>
<dt><code>-1</code></p>
<dd> Assume input data is encoded with the 1-dimensional version of the <font SIZE="-1">CCITT</font> Group 3 Huffman encoding algorithm (default).</p>
<dt><code>-2</code></p>
<dd> Assume input data is 2-dimensional version of the <font SIZE="-1">CCITT</font> Group 3 Huffman encoding algorithm.</p>
<dt><code>-P</code></p>
<dd> Assume input data is <code>not</code> EOL-aligned (default). This option has effect with Group 3 encoded input only.</p>
<dt><code>-A</code></p>
<dd> Assume input data is EOL-aligned. This option has effect with Group 3 encoded input only.</p>
<dt><code>-M</code></p>
<dd> Treat input data as having bits filled from most significant bit (<font SIZE="-1">MSB</font>) to most least bit (<font SIZE="-1">LSB</font>).</p>
<dt><code>-L</code></p>
<dd> Treat input data as having bits filled from least significant bit (<font SIZE="-1">LSB</font>) to most significant bit (<font SIZE="-1">MSB</font>) (default).</p>
<dt><code>-B</code></p>
<dd> Assume input data was encoded with black as 0 and white as 1.</p>
<dt><code>-W</code></p>
<dd> Assume input data was encoded with black as 1 and white as 0 (default).</p>
<dt><code>-R</code></p>
<dd> Specify the vertical resolution, in lines/inch, of the input images. By default input are assumed to have a vertical resolution of 196 lines/inch. If images are low resolution facsimile, a value of 98 lines/inch should be specified.</p>
<dt><code>-X</code></p>
<dd> Specify the width, in pixels, of the input images. By default input are assumed to have a width of 1728 pixels.</dl>
<p> Options that affect the output file format are:</p>
<dl>
<dt><code>-o</code></p>
<dd> Specify the name of the output file.</p>
<dt><code>-7</code></p>
<dd> Force output to be compressed with the <font SIZE="-1">CCITT</font> Group 3 Huffman encoding algorithm (default).</p>
<dt><code>-8</code></p>
<dd> Force output to be compressed with the <font SIZE="-1">CCITT</font> Group 4 Huffman encoding.</p>
<dt><code>-u</code></p>
<dd> Force output to be uncompressed (Group 3 or Group 4).</p>
<dt><code>-5</code></p>
<dd> Force output to be encoded with the 1-dimensional version of the <font SIZE="-1">CCITT</font> Group 3 Huffman encoding algorithm.</p>
<dt><code>-6</code></p>
<dd> Force output to be encoded with the 2-dimensional version of the <font SIZE="-1">CCITT</font> Group 3 Huffman encoding algorithm (default).</p>
<dt><code>-a</code></p>
<dd> Force the last bit of each <i>End Of Line</i> (<font SIZE="-1">EOL</font>) code to land on a byte boundary (default). This &#8220;zero padding&#8221; will be reflected in the contents of the <i>Group3Options</i> tag of the resultant <font SIZE="-1">TIFF</font> file. This option has effect with Group 3 encoded output only.</p>
<dt><code>-p</code></p>
<dd> Do not EOL-align output. This option has effect with Group 3 encoded output only.</p>
<dt><code>-c</code></p>
<dd> Generate &quot;classic&quot; Group 3 TIFF format.</p>
<dt><code>-f</code></p>
<dd> Generate TIFF Class F (TIFF/F) format (default).</p>
<dt><code>-m</code></p>
<dd> Force output data to have bits filled from most significant bit (<font SIZE="-1">MSB</font>) to most least bit (<font SIZE="-1">LSB</font>).</p>
<dt><code>-l</code></p>
<dd> Force output data to have bits filled from least significant bit (<font SIZE="-1">LSB</font>) to most significant bit (<font SIZE="-1">MSB</font>) (default).</p>
<dt><code>-r</code></p>
<dd> Specify the number of rows (scanlines) in each strip of data written to the output file. By default (or when value <code>0</code> is specified), <i>tiffcp</i> attempts to set the rows/strip that no more than 8 kilobytes of data appear in a strip (with except of G3/G4 compression schemes). If you specify special value <code>-1</code> it will results in infinite number of the rows per strip. The entire image will be the one strip in that case. This is default in case of G3/G4 output compression schemes.</p>
<dt><code>-s</code></p>
<dd> Stretch the input image vertically by writing each input row of data twice to the output file.</p>
<dt><code>-v</code></p>
<dd> Force <i>fax2tiff</i> to print the number of rows of data it retrieved from the input file.</p>
<dt><code>-z</code></p>
<dd> Force output to be compressed with the LZW encoding.</dl>
<h2>DIAGNOSTICS</h2>
<p> The following warnings and errors come from the decoding routines in the library. </p>
<p> <code>Warning, %s: Premature EOL at scanline %d (x %d).
</code>. The input data had a row that was shorter than the expected width. The row is padded with white. </p>
<p> <code>%s: Premature EOF at scanline %d (x %d).
</code>. The decoder ran out of data in the middle of a scanline. The resultant row is padded with white. </p>
<p> <code>%s: Bad code word at row %d, x %d
</code>. An invalid Group 3 <i>code</i> was encountered while decoding the input file. The row number and horizontal position is given. The remainder of the input row is discarded, while the corresponding output row is padded with white. </p>
<p> <code>%s: Bad 2D code word at scanline %d.
</code>. An invalid Group 4 or 2D Group 3 <i>code</i> was encountered while decoding the input file. The row number and horizontal position is given. The remainder of the input row is discarded, while the corresponding output row is padded with white.</p>
<h2>BUGS</h2>
<p> Input data are assumed to have a a &#8220;top left&#8221; orientation; it should be possible to override this assumption from the command line.</p>
<h2>SEE ALSO</h2>
<p> <font SIZE="-1"><code>CCITT</code></font><code> Recommendation T.4</code> (Standardization of Group 3 Facsimile Apparatus for Document Transmission). </p>
<p> <code>The Spirit of TIFF Class F,</code> an appendix to the TIFF 5.0 specification prepared by Cygnet Technologies. </p>
<p> <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffdither/">tiffdither</a></code>(1), <code><a href="/docs/linux/man/1-tiffgt/">tiffgt</a></code>(1), <code><a href="/docs/linux/man/3-libtiff/">libtiff</a></code>(3) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
