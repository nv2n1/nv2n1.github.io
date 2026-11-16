---
title: "xcf2pnm(1)"
name: "xcf2pnm"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xcf2pnm/"
description: "xcf2pnm – convert from GIMP xcf files to ppm/pgm/pbm format"
---

<h2>NAME</h2>
<p> xcf2pnm &#8211; convert from GIMP xcf files to ppm/pgm/pbm format</p>
<h2>SYNOPSIS</h2>
<p> <code>xcf2pnm</code> [ <i>options</i> ] <i>filename</i> [ <i>layer names</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>xcf2pnm</code> is a command-line tool that converts image files in the XCF format used by <code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1) to the generic image formats <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), and <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), flattening layers if necessary. It does not need to have the Gimp engine itself available.</p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-a</code> <i>filename</i>, <code>&#8211;alpha</code> <i>filename</i></dt>
<dd> Output a transparency mask for the flattened image to <i>filename</i> as a <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5) file, in addition to the ordinary output. If the flattened image is completely opaque, this will produce an error message and exit status 101; use <code>-A</code> to suppress this.</dd>
<dt><code>-A</code>, <code>&#8211;force-alpha</code></dt>
<dd> Invent a trivial alpha channel even if the flattened image is completely opaque.</dd>
<dt><code>-b</code> <i>color</i>, <code>&#8211;background</code> <i>color</i></dt>
<dd> Use this color for transparent pixels in the image. The color can be given as <code>#rrggbb</code> or <code>#rgb</code> hexadecimal values, or as an X11 color name (which will only work if a color name database can be found in one of a number of standard locations).</dd>
<dt><code>-c</code>, <code>&#8211;color</code>, <code>&#8211;colour</code></dt>
<dd> Force the output to use RGB color space even if it there are more compact alternatives. This will be selected automatically if the output file&#8217;s name ends with <code>.ppm</code>.</dd>
<dt><code>-C</code>, <code>&#8211;autocrop</code></dt>
<dd> Set the converted part of the image such that it just include the boundaries of the visible (or selected) layers. This may make it either smaller or larger than the canvas, depending on the position and size of the visible layers. (Note that the <i>contents</i> of the layers is not taken into account when autocropping).</dd>
<dt>
</dt><dd> In the absence of options that specify otherwise, the converted image will cover the entire XCF canvas.</dd>
<dt><code>-D</code>, <code>&#8211;dissolve</code></dt>
<dd> Do a &quot;dissolve&quot; step to eliminate partial transparency after flattening. If <code>-b</code> is also given, this happens before the background color is applied.</dd>
<dt><code>-f</code>, <code>&#8211;full-image</code></dt>
<dd> First flatten the entire image to a memory buffer before writing output. Then analyse the image to decide on the details of the output format (e.g., whether a grayscale output is sufficient). Without this option, the program flattens only a singe row of &quot;tiles&quot; (height 64) at a time.</dd>
<dt><code>-g</code>, <code>&#8211;gray</code>, <code>&#8211;grey</code></dt>
<dd> Force the output to be a grayscale image even if it may be monochrome. If any colored pixels are encountered, exit with status 103. This will be selected automatically if the output file&#8217;s name ends with <code>.pgm</code>.</dd>
<dt><code>-G</code>, <code>&#8211;for-gif</code></dt>
<dd> Assert that the flattened image will have no partial transparency (allowing a more compact representation of the alpha output). Exit with status 102 if the flattened image has any partial transparency. If <code>-b</code> is also given, this tests whether there there is partial transparency before applying the background color.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print an option summery to standard output and exit with a return code of 0.</dd>
<dt><code>-j</code>, <code>&#8211;bzip</code></dt>
<dd> Equivalent to <code>-Z bzcat</code>. Default if the filename ends with <code>bz2</code>.</dd>
<dt><code>-m</code>, <code>&#8211;mono</code></dt>
<dd> Force the output to be a monochrome image. If any colors except black and white are encountered, exit with status 103. This will be selected automatically if the output file&#8217;s name ends with <code>.pbm</code>.</dd>
<dt><code>-n</code>, <code>&#8211;pnm</code></dt>
<dd> Suppress the automatic choice of <code>-c</code>, <code>-g</code>, or <code>-m</code> based on output filename, and instead select the output format based on image contents. This is the default if the filename is not recognized, and when writing to stdout.</dd>
<dt><code>-o</code> <i>filename</i>, <code>&#8211;output</code> <i>filename</i></dt>
<dd> Write the converted picture to <i>filename</i> instead of to standard output.</dd>
<dt><code>-O</code> <i>x</i><code>,</code>y, <code>&#8211;offset</code> <i>x</i><code>,</code>y</dt>
<dd> Offset the converted part of the image from the top-left corner of the XCF canvas. Usually used with <code>-S</code>.</dd>
<dt><code>-S</code> <i>w</i><code>x</code>h, <code>&#8211;size</code> <i>w</i><code>x</code>h</dt>
<dd> Crop the converted image to width <i>w</i> and height <i>h</i>.</dd>
<dt><code>-T</code>, <code>&#8211;truecolor</code></dt>
<dd> Use standard RGB compositing for flattening indexed layers. Without this option, <code>xcf2pnm</code> will mimic the Gimp&#8217;s current strategy of rounding each alpha value to either full transparency or full opacity, and interpret all layer modes as <code>Normal</code>.</dd>
<dt><code>-u</code>, <code>&#8211;utf8</code></dt>
<dd> Use the raw UTF-8 representation from the XCF file to compare and display layer names. Ordinarily, layer names will be converted to the character set of the current locale.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Print progress messages about the conversion to standard error.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print the version numer of <code>xcftools</code> to standard output and exit with a return code of 0.</dd>
<dt><code>-z</code>, <code>&#8211;gzip</code></dt>
<dd> Equivalent to <code>-Z zcat</code>. Default if the filename ends with <code>gz</code>.</dd>
<dt><code>-Z</code> <i>command</i>, <code>&#8211;unpack</code> <i>command</i></dt>
<dd> Specify a command that the input file is filtered through before being interpreted as an XCF file. The command is invoked as <i>command filename</i> and must produce output to its standard output. Note that it is not possible to specify arguments as part of <i>command</i>. An uncompressor is selected automatically if the filename ends with <code>gz</code> or <code>bz2</code>; to suppress this, use <code>-Z cat</code> (which is implemented without actually starting a <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) process). Several groups of options are mutually incompatible; in each group the one given last will win:</dd>
<dt>1)</dt>
<dd> <code>-A</code> and <code>-b</code>.</dd>
<dt>2)</dt>
<dd> <code>-c</code>, <code>-g</code>, <code>-m</code>, and <code>-n</code>.</dd>
<dt>3)</dt>
<dd> <code>-D</code> and <code>-G</code>.</dd>
<dt>4)</dt>
<dd> <code>-j</code>, <code>-z</code>, and <code>-Z</code>.</dd>
<dt>5)</dt>
<dd> <code>-C</code> and <code>-O</code>/<code>-S</code>.</dd></dl>
<h2>LAYER SPECIFICATIONS</h2>
<p> If no <i>layer name</i> is given on the command line, all of the visible layers in the XCF file are merged to produce the output image. It is also possible to specify the layers to merge explicitly, by giving their names as separate arguments after the input filename. In that case, the output will contain <i>only</i> the named layers. The layers will be merged in the order they appear on the command line, with the leftmost being &quot;at the bottom&quot; &#8211; that is, the layer ordering in the XCF file will be ignored. The following options can be given <i>after</i> a layer name to override the global properties of the layer:</p>
<dl>
<dt><code>&#8211;mask</code></dt>
<dd> Enable the layer mask.</dd>
<dt><code>&#8211;mode</code> <i>mode</i></dt>
<dd> Set the layer mode (e.g., <code>Normal</code> or <code>Multiply</code>).</dd>
<dt><code>&#8211;nomask</code></dt>
<dd> Disable the layer mask.</dd>
<dt><code>&#8211;opacity</code> <i>n</i></dt>
<dd> Set the opacity on a scale from 0 to 255 (as used internally)</dd>
<dt><code>&#8211;percent</code> <i>n</i></dt>
<dd> Set the opacity on a scale from 0 to 100 (as in the Gimp user interface).</dd></dl>
<h2>EXIT STATUS</h2>
<p> The exit status of <code>xcf2pnm</code> is</p>
<dl>
<dt>0</dt>
<dd> Success</dd>
<dt>20</dt>
<dd> Problems parsing the command line, including unknown color names (or missing color name directory) for <code>-b</code>.</dd>
<dt>21</dt>
<dd> The specified XCF file does not exist or cannot be read.</dd>
<dt>22</dt>
<dd> A layer named on the command line was not found, or the <code>&#8211;mask</code> option was used for a layer that has no layer mask.</dd>
<dt>100</dt>
<dd> Transparent pixels were found, but neither <code>-a</code> nor <code>-b</code> was given.</dd>
<dt>101</dt>
<dd> The <code>-a</code> option was given yet the image has no transparency. (Use <code>-A</code> to go on anyway).</dd>
<dt>102</dt>
<dd> The <code>-G</code> option was given, yet partial transparency was found.</dd>
<dt>103</dt>
<dd> <code>-g</code> (or <code>-m</code>) was given, yet colored (or gray) pixels were found.</dd>
<dt>123</dt>
<dd> The XCF file contains presumably valid features that <code>xcftools</code> does not support. (As of this writing there is no known way of getting the Gimp to write an XCF file that will provoke this return. Please notify the author if you discover one).</dd>
<dt>125</dt>
<dd> The XCF file is malformed.</dd>
<dt>126</dt>
<dd> An uncompression program could not be executed, or terminated abnormally.</dd>
<dt>127</dt>
<dd> Unexpected I/O error, internal errors, or other &quot;this can&#8217;t happen&quot; situations. If an uncompression program returns an error exit status, this will be returned from <code>xcf2pnm</code> too.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd> <code>xcf2pnm -b white foo.xcf &gt; foo.ppm</code></dd>
<dt>
</dt><dd> <code>xcf2pnm -a footrans.pgm -o foo.ppm foo.xcf Layer1 Layer2</code> To test whether the flattened image has any transparency, use</dd>
<dt>
</dt><dd> <code>xcf2pnm foo.xcf &gt; /dev/null</code> To test whether the flattened image has <i>partially</i> transparent pixels, use</dd>
<dt>
</dt><dd> <code>xcf2pnm -b white -G &gt; /dev/null</code></dd></dl>
<h2>BUGS AND LIMITATIONS</h2>
<p> When several partially transparent layers are merged, the pixel values are interpolated without gamma correction. (The Gimp also does it this way). Some slight rounding errors in the interpolation are inevitable; <code>xcf2pnm</code> sometimes has different rounding errors than the Gimp itself, especially when more than two layers are involved, or in case of some of the more exotic layer modes. These differences are usually not visible to the eye. Floating selections are currently not handled correctly. There are probably other bugs lurking in corner cases. If you discover one, please notify the author. </p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/X11/rgb.txt</code></dt>
<dd>
</dd><dt><code>/usr/share/X11/rgb.txt</code></dt>
<dd>
</dd><dt><code>/usr/lib/X11/rgb.txt</code></dt>
<dd> Color name database for <code>-b</code>.</dd></dl>
<h2>AUTHOR</h2>
<p> <code>xcf2pnm</code> was written by Henning Makholm &lt;henning [at] makholm.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xcfinfo/">xcfinfo</a></code>(1), <code><a href="/docs/linux/man/1-xcf2png/">xcf2png</a></code>(1) </p>
<h2>Index</h2>
