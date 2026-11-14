---
title: "pamtojpeg2k(1)"
name: "pamtojpeg2k"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtojpeg2k/"
description: "pamtojpeg2k – convert PAM/PNM image to a JPEG-2000 code stream"
---

<h2 class="name">NAME</h2>
<p> pamtojpeg2k &#8211; convert PAM/PNM image to a JPEG-2000 code stream</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtojpeg2k</code> [<code>-imgareatlx=</code><i>column</i>] [<code>-imgareatly=</code><i>row</i>] [<code>-tilegrdtlx=</code><i>column</i>] [<code>-tilegrdtly=</code><i>row</i>] [<code>-tilewidth=</code><i>columns</i>] [<code>-tileheight=</code><i>rows</i>] [<code>-prcwidth=</code><i>columns</i>] [<code>-prcheight=</code><i>rows</i>] [<code>-cblkwidth=</code><i>columns</i>] [<code>-cblkheight=</code><i>rows</i>] [<code>-mode=</code>{<code>integer</code>|<code>int</code>|<code>real</code>}] [<code>-compression=</code><i>ratio</i>] [<code>-ilyrrates=</code><i>ratestring</i>] [<code>-numrlvls=</code><i>number</i>] [<code>-progression=</code>{<code>lrcp</code>|<code>rlcp</code>|<code>rpcl</code>|<code>pcrl</code>|<code>cprl</code>}] [<code>-numgbits=</code><i>number</i>] [<code>-nomct</code>] [<code>-sop</code>] [<code>-eph</code>] [<code>-lazy</code>] [<code>-termall</code>] [<code>-segsym</code>] [<code>-vcausal</code>] [<code>-pterm</code>] [<code>-resetprob</code>] [<code>-verbose</code>] [<code>-debuglevel=</code><i>number</i>] <i>filename</i> </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtojpeg2k</code> converts the named PBM, PGM, PPM, or PAM file, or Standard Input if no file is named, to a JPEG-2000 code stream (JPC) file on Standard Output. </p>
<p> The JPEG-2000 specification specifies two different formats: JP2 and JPEG-2000 code stream (JPC). JP2 represents a visual image quite specifically, whereas JPC is a more or less arbitrary array of codes. <code>pamtojpeg2k</code> can&#8217;t produce a JP2, but the JPC image that <code>pamtojpeg2k</code> produces is very similar to a JP2 if the input is a PBM, PGM, or PPM image or equivalent PAM image. One difference is that the RGB intensity values in a JP2 are SRGB values, while <code>pamtojpeg2k</code> produces ITU-R Recommendation BT.709 values. Those are very similar, but not identical. Another difference is that a JP2 can contain extra information about an image that JPC cannot. </p>
<p> When the input is a PAM image other than a PBM, PGM, or PPM equivalent, the JPC raster produced contains whatever the PAM raster does. It can have any number of planes with any meanings; the planes are in the same order in the JPC output as in the PAM input. </p>
<p> A JPC image has a &quot;precision,&quot; which is the number of bits used for each code (in Netpbm lingo, &quot;sample&quot;). Actually, it has a separate precision for each component. <code>pamtojpeg2k</code> uses for the precision of every component the least number of bits that can represent the maxval of the input image. A JPC image does not have an independent concept of maxval; the maxval of a JPC sample is the maximum value that the number of bits specified by the precision can represent in pure binary code. E.g. if the precision is 4, the maxval is 15. <code>pamtojpeg2k</code> does of course scale the sample values from the input maxval to the output maxval. Example: The input maxval is 99. This means JPC precision is 7 bits and the JPC maxval is 127. A sample value of 33 in the input becomes a sample value of 43 in the output. </p>
<p> <code>pamtojpeg2k</code> generates the JPC output with the Jasper JPEG-2000 library . See documentation of the library for details on what <code>pamtojpeg2k</code> produces. Note that the Jasper library contains facilities for reading PNM images, but <code>pamtojpeg2k</code> does not use those. It uses the Netpbm library instead. Note that the makers of the Jasper library write it &quot;JasPer,&quot; but Netpbm documentation follows standard American English typography rules, which don&#8217;t allow that kind of capitalization. </p>
<p> Use <code>jpeg2ktopam</code> to convert in the other direction. </p>
<p> The program <code>jasper</code>, which is packaged with the Jasper JPEG-2000 library, also converts between JPEG-2000 and PNM formats. Because it&#8217;s packaged with the library, it may exploit it better, especially recently added features. However, since it does not use the Netpbm library to read and write the Netpbm formats, it doesn&#8217;t do as good a job on that side. </p>
<h2>OPTIONS</h2>
<p> Most of the options are identical in name and function to options that the Jasper library JPC encoder subroutine takes. See Jasper documentation for details. Here, we document only options that are not direct analogs of Jasper options. </p>
<dl>
<dt><code>-compression=</code><i>ratio</i></p>
<dd> <i>ratio</i> is a floating point number that specifies the compression ratio. <code>pamtojpeg2k</code> will adjust quality as necessary to ensure that you get this compression ratio. E.g. 4 means the output will be about one fourth the size in bytes of the input file. </p>
<p> The ratio concerns just the raster part of the image, with the denominator being what the raster would take if it were encoded the most naive way possible (e.g. 3 bytes per pixel in 8-bit-per-sample RGB). It does, however, include metadata that is part of the compressed raster. Because of that, it may not be possible to give you your requested compression ratio at any quality. If it isn&#8217;t, <code>pamtojpeg2k</code> fails with a message saying so. </p>
<p> If you don&#8217;t specify this option, <code>pamtojpeg2k</code> gives you the best compression it can without losing any quality. Because of the metadata issue described above, this may mean, for a small image, the image actually expands. </p>
<p> Note that though the Jasper library takes a compression factor, this option specifies a compression ratio. The compression factor is the multiplicative inverse of (1 divided by) the compression ratio. </p>
<p> Before Netpbm 10.61 (December 2012), the default was a compression ratio of 1, and if <code>pamtojpeg2k</code> could not make the output that small, it just made it as small as it could, with zero quality. You know this is happening when you see the warning message, &#8217;empty layer generated.&#8217; </p>
<dt><code>-verbose</code></p>
<dd> This option causes <code>pamtojpeg2k</code> to issue informational messages about the conversion process. </p>
<dt><code>-debuglevel</code>=<i>number</i></p>
<dd> This option controls debug messages from the Jasper library. <code>pamtojpeg2k</code> passes <i>number</i> as the debug level to the Jasper JPC encoder. </p>
<p>&nbsp;<wbr>&nbsp;<wbr></dl>
<h2>EXAMPLES</h2>
<p> This example compresses losslessly. </p>
<pre>
  pamtojpeg2k myimg.ppm &gt;myimg.jpc
</pre>
<p> <code>jpeg2ktopam</code> will recreate myimg.ppm exactly. </p>
<p> This example compresses the file to one tenth its original size, throwing away information as necessary. </p>
<pre>
  pamtojpeg2k -compression=10 myimg.pgm &gt;myimg.jpc
</pre>
<h2>ABOUT JPEG-2000</h2>
<p> JPEG-2000 is a format that compresses a visual image (or a similar set of data) into a minimal number of bytes for storage or transmission. In that, its goal is similar to JPEG. It has two main differences from JPEG. </p>
<p> One difference is that it does a much better job on most images of throwing out information in order to achieve a smaller output. That means when you reconstruct the image from the resulting compressed file, it looks a lot closer to the image you started with JPEG-2000 than with JPEG, for the same compressed file size. Or, looked at another way, with JPEG-2000 you get a much smaller file than with JPEG for the same image quality. </p>
<p> The second difference is that with JPEG-2000, you decide how much compression you want and the compressor adjusts the quality to meet your requirement, whereas with JPEG, you decide how much quality you want and the compressor adjusts the size of the output to meet your requirement. I.e. with JPEG-2000, the quality of the result depends on the compressibility of the input, but with JPEG, the <i>size</i> of the result depends on the compressibility of the input. </p>
<p> With JPEG-2000, you can specify lossless compression, thus making it compete with GIF and PNG. With standard JPEG, you always lose something. (There are rumored to be variations of JPEG around that are lossless, though). </p>
<p> JPEG is much older than JPEG-2000 and far more popular. JPEG is one of the half dozen most popular graphics formats and virtually all graphics facilities understand it. JPEG-2000 is virtually unknown. </p>
<p> There is no compatibility between JPEG and JPEG-2000. Programs that read JPEG do not automatically read JPEG-2000 and vice versa. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jpeg2ktopam/">jpeg2ktopam</a></code>(1) , <code><a href="/docs/linux/man/1-pnmtopeg/">pnmtopeg</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) , <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , </p>
<h2>History</h2>
<p> <code>pamtojpeg2k</code> was added to Netpbm in Release 10.12 (November 2002). </p>
<h2>Index</h2>
