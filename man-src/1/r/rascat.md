---
title: "rascat(1)"
name: "rascat"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rascat/"
description: "Rascat – concatenate, convert raster files"
---

<h2>NAME</h2>
<p> Rascat &#8211; concatenate, convert raster files</p>
<h2>SYNOPSIS</h2>
<p> <code>rascat</code> [ <code>-help </code> ] [ <code>-ifmt</code><i> format</i> ] [ <code>-ira</code><i> algorithm</i> ] [ <code>-ofmt</code><i> format</i> ] [ <code>-output</code><i> file</i> ] [ <code>-resolution</code><i> resolution</i> ] [ <code>-rgbscale</code><i> scale-factor</i> ] [ <code>-scale</code><i> scale-factor</i> ] [ <code>-verbose</code> ] [ <code>-Version</code> ] [ <code>-window</code><i> nx ny x y</i> ] [ <code>-pal</code><i> palette_file</i> ] [ <code>&#8211;</code><i>|</i><code>file&#8230;</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>rascat</code> reads each <i>file</i> in sequence and copies its contents to the standard output performing any format conversion and data massaging necessary as specified by the command line options. By default, <code>rascat</code> determines the format of a file by looking at the file name extension. If there are multiple files input into rascat with varying file formats <code>rascat </code> will perform format conversion such that the resulting concatenated file will be in the format of the first file processed. </p>
<p> Input files must all have the same spatial resolution and have the same depth; 8-bit and 24-bit files may not be intermixed. Furthermore, if an input file contains multiple images each image in that file must have the same spatial resolution and be of the same depth. </p>
<p> Currently, only 8-bit-indexed and 24-bit-direct color encodings are supported. </p>
<p> See <code>ras_formats(5NCARG)</code> for a list of supported image formats.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print a usage message and exit.</p>
<dt><code>-ifmt</code><i> format</i></p>
<dd> Specify the input file format. <i>format</i> is one of the file name extensions discussed in <code>ras_formats(5NCARG) </code> (without the &quot;.&quot;, e.g. <code>xwd).</code> When this option is specified file name extensions are not necessary and are ignored if present. All input files must have the same format.</p>
<dt><code>-ira</code><i> algorithm</i></p>
<dd> Specify the image resampling algorithm to be used when either the <code>-scale</code> or the <code>-resolution</code> command line option is used. <i>algorithm</i> may be either <code>NN</code>, indicating a &quot;nearest neighbor&quot; algorithm, or <code>BL</code>, indicating a &quot;bilinear interplation&quot; algorithm. The default is to do &quot;nearest neighbor&quot; interpolation.</p>
<dt><code>-ofmt</code><i> format</i></p>
<dd> Specify the output file format. <i>format</i> is one of the aforementioned file name extensions. If used in conjunction with the <code>-output </code> option the output file name requires no name extension and is ignored if present.</p>
<dt><code>-output</code><i> file</i></p>
<dd> Specify an ouput file name and possibly an implicit output format. By default rascat writes to the standard output. When this option is used output is written to <i>file</i>. If the <code>-ofmt</code> option is not specified <i>file</i> must have a file name extension recognized by <code>rascat.</code> In which case the file name extension will determine the output format.</p>
<dt><code>-resolution</code><i> resolution</i></p>
<dd> Resample the spatial resolution of input imagery to <i>resolution</i>, where <i>resolution</i> is the number of pixels in the x direction, followed by an <code>x</code>, followed by the number of pixels in the y direction, with no intervening spaces. For example, 512&#215;512, specifies a 512 by 512 pixel resolution.</p>
<dt>
<dd> Warning: Aspect ratios are not preserved by this option. If the resolution of your input imagery has a different aspect ratio then that specified by <i>resolution</i> the resultant image will be distorted.</p>
<dt><code>-rgbscale</code><i> scale-factor</i></p>
<dd> Specify a floating point scaling factor, <i>scale-factor</i>, to be applied to all the color intensities contained in the input files. This option may be fairly computationally expensive with 24-bit-direct encoded imagery.</p>
<dt><code>-scale</code><i> scale-factor</i></p>
<dd> Specify a uniform, floating-point scaling factor to be applied to the spatial resolution of the input files. Unlike the <code>-resolution </code> option this option guarantees to preserve the aspect ratio of your imagery. For example, setting <i>scale-factor</i> to <code>0.5</code> causes your imagery to be resampled to one fourth of its original spatial resolution. If its original resolution was 1024&#215;1024 the resultant resolution would be 512&#215;512.</p>
<dt><code>-verbose</code></p>
<dd> Tells rascat to operate in verbose mode.</p>
<dt><code>-Version</code></p>
<dd> Print rascat&#8217;s version number and then exit.</p>
<dt><code>-window</code><i> nx ny x y</i></p>
<dd> Specify a subregion of the input imagery to be extracted. The area outside the rectangular subregion defined by <i>nx</i>, <i>ny</i>, <i>x</i> and <i>y</i> is discarded. <i>x</i> and <i>y</i> specify the position of the upper-left corner of the rectangle. <i>nx</i> and <i>ny</i> specify the rectangle&#8217;s width and height, respectively.</p>
<dt><code>-pal</code><i> palette_file</i></p>
<dd> Set the palette for the output rasterfile from <i>palettefile</i>, which can be either an HDF-type palette with an extension of &quot;.pal&quot;, or a textual palette with an extension of &quot;.txt&quot;. See ras_palette(5NCARG) for documentation on the formats. This option applies to indexed-color imagery only.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>NCARG_TMP</code></p>
<dd> If set, this environment variable contains a directory path to be used for temporary files. On most systems the default is <code>/tmp</code>. On some systems the default is <code>/usr/tmp</code>.</dl>
<h2>EXAMPLES</h2>
<p> In the following example a NRIF file, a Sun raster image file, and a XWD file are concatenated and converted into a single NRIF file: </p>
<dl>
<dt>
<dd> % rascat file1.nrif file2.sun file3.xwd &gt; file123.nrif</dl>
<p> In this example the same files are converted and concatenated into a sun file: </p>
<dl>
<dt>
<dd> % rascat -ofmt sun file1.nrif file2.sun file3.xwd &gt; file123.sun </p>
</dl>
<p> The <code>-ofmt</code> option is necessary in this example because the first file <code>rascat</code> encounters is an NRIF file. </p>
<p> Finally, in this example the upper left 512 by 512 rectangle of the file <code>foo.sun</code> is extracted and written to the file <code>foo.512&#215;512.sun</code>: </p>
<dl>
<dt>
<dd> % rascat -window 512 512 0 0 foo.sun &gt; foo.512&#215;512.sun</dl>
<h2>SEE ALSO</h2>
<p> <code>rasgetpal(1NCARG),</code> <code>rasls(1NCARG),</code> <code>rassplit(1NCARG),</code> <code>rasview(1NCARG),</code> <code>ras_formats(5NCARG),</code> <code>ras_palette(5NCARG)</code> </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>CAVEATS</h2>
<p> Aspect ratios are not preserved by the <code>-resolution</code> option. </p>
<p> Not all formats support both 8-bit and 24-bit encodings. </p>
<p> Indexed and direct color encodings cannot be mixed.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
