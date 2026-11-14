---
title: "xcf2png(1)"
name: "xcf2png"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xcf2png/"
description: "xcf2png – convert from GIMP xcf files to png format"
---

<h2>NAME</h2>
<p> xcf2png &#8211; convert from GIMP xcf files to png format</p>
<h2>SYNOPSIS</h2>
<p> <code>xcf2png</code> [ <i>options</i> ] <i>filename</i> [ <i>layer names</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>xcf2png</code> is a command-line tool that converts image files in the XCF format used by <code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1) to the generic image format <code>png</code>, flattening layers if necessary. It does not need to have the Gimp engine itself available.</p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;force-alpha</code></p>
<dd> Invent a trivial alpha channel even if the flattened image is completely opaque.</p>
<dt><code>-b</code> <i>color</i>, <code>&#8211;background</code> <i>color</i></p>
<dd> Use this color for transparent pixels in the image. The color can be given as <code>#rrggbb</code> or <code>#rgb</code> hexadecimal values, or as an X11 color name (which will only work if a color name database can be found in one of a number of standard locations).</p>
<dt><code>-c</code>, <code>&#8211;color</code>, <code>&#8211;colour</code></p>
<dd> Force the output to use RGB color space even if it there are more compact alternatives.</p>
<dt><code>-C</code>, <code>&#8211;autocrop</code></p>
<dd> Set the converted part of the image such that it just include the boundaries of the visible (or selected) layers. This may make it either smaller or larger than the canvas, depending on the position and size of the visible layers. (Note that the <i>contents</i> of the layers is not taken into account when autocropping).</p>
<dt>
<dd> In the absence of options that specify otherwise, the converted image will cover the entire XCF canvas.</p>
<dt><code>-D</code>, <code>&#8211;dissolve</code></p>
<dd> Do a &quot;dissolve&quot; step to eliminate partial transparency after flattening. If <code>-b</code> is also given, this happens before the background color is applied.</p>
<dt><code>-f</code>, <code>&#8211;full-image</code></p>
<dd> First flatten the entire image to a memory buffer before writing output. Then analyse the image to decide on the details of the output format (e.g., whether a grayscale output is sufficient). Without this option, the program flattens only a singe row of &quot;tiles&quot; (height 64) at a time.</p>
<dt><code>-g</code>, <code>&#8211;gray</code>, <code>&#8211;grey</code></p>
<dd> Force the output to be a grayscale image even if it may be monochrome. If any colored pixels are encountered, exit with status 103. This will be selected automatically if the output file&#8217;s name ends with <code>.pgm</code>.</p>
<dt><code>-G</code>, <code>&#8211;for-gif</code></p>
<dd> Assert that the flattened image will have no partial transparency (allowing a more compact representation of the alpha output). Exit with status 102 if the flattened image has any partial transparency. If <code>-b</code> is also given, this tests whether there there is partial transparency before applying the background color.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print an option summery to standard output and exit with a return code of 0.</p>
<dt><code>-j</code>, <code>&#8211;bzip</code></p>
<dd> Equivalent to <code>-Z bzcat</code>. Default if the filename ends with <code>bz2</code>.</p>
<dt><code>-o</code> <i>filename</i>, <code>&#8211;output</code> <i>filename</i></p>
<dd> Write the converted picture to <i>filename</i> instead of to standard output.</p>
<dt><code>-O</code> <i>x</i><code>,</code>y, <code>&#8211;offset</code> <i>x</i><code>,</code>y</p>
<dd> Offset the converted part of the image from the top-left corner of the XCF canvas. Usually used with <code>-S</code>.</p>
<dt><code>-S</code> <i>w</i><code>x</code>h, <code>&#8211;size</code> <i>w</i><code>x</code>h</p>
<dd> Crop the converted image to width <i>w</i> and height <i>h</i>.</p>
<dt><code>-T</code>, <code>&#8211;truecolor</code></p>
<dd> Use standard RGB compositing for flattening indexed layers. Without this option, <code>xcf2png</code> will mimic the Gimp&#8217;s current strategy of rounding each alpha value to either full transparency or full opacity, and interpret all layer modes as <code>Normal</code>.</p>
<dt><code>-u</code>, <code>&#8211;utf8</code></p>
<dd> Use the raw UTF-8 representation from the XCF file to compare and display layer names. Ordinarily, layer names will be converted to the character set of the current locale.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print progress messages about the conversion to standard error.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version numer of <code>xcftools</code> to standard output and exit with a return code of 0.</p>
<dt><code>-z</code>, <code>&#8211;gzip</code></p>
<dd> Equivalent to <code>-Z zcat</code>. Default if the filename ends with <code>gz</code>.</p>
<dt><code>-Z</code> <i>command</i>, <code>&#8211;unpack</code> <i>command</i></p>
<dd> Specify a command that the input file is filtered through before being interpreted as an XCF file. The command is invoked as <i>command filename</i> and must produce output to its standard output. Note that it is not possible to specify arguments as part of <i>command</i>. An uncompressor is selected automatically if the filename ends with <code>gz</code> or <code>bz2</code>; to suppress this, use <code>-Z cat</code> (which is implemented without actually starting a <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) process). Several groups of options are mutually incompatible; in each group the one given last will win:</p>
<dt>1)</p>
<dd> <code>-A</code> and <code>-b</code>.</p>
<dt>2)</p>
<dd> <code>-g</code> and <code>-c .</code></p>
<dt>3)</p>
<dd> <code>-D</code> and <code>-G</code>.</p>
<dt>4)</p>
<dd> <code>-j</code>, <code>-z</code>, and <code>-Z</code>.</p>
<dt>5)</p>
<dd> <code>-C</code> and <code>-O</code>/<code>-S</code>.</dl>
<h2>LAYER SPECIFICATIONS</h2>
<p> If no <i>layer name</i> is given on the command line, all of the visible layers in the XCF file are merged to produce the output image. It is also possible to specify the layers to merge explicitly, by giving their names as separate arguments after the input filename. In that case, the output will contain <i>only</i> the named layers. The layers will be merged in the order they appear on the command line, with the leftmost being &quot;at the bottom&quot; &#8211; that is, the layer ordering in the XCF file will be ignored. The following options can be given <i>after</i> a layer name to override the global properties of the layer:</p>
<dl>
<dt><code>&#8211;mask</code></p>
<dd> Enable the layer mask.</p>
<dt><code>&#8211;mode</code> <i>mode</i></p>
<dd> Set the layer mode (e.g., <code>Normal</code> or <code>Multiply</code>).</p>
<dt><code>&#8211;nomask</code></p>
<dd> Disable the layer mask.</p>
<dt><code>&#8211;opacity</code> <i>n</i></p>
<dd> Set the opacity on a scale from 0 to 255 (as used internally)</p>
<dt><code>&#8211;percent</code> <i>n</i></p>
<dd> Set the opacity on a scale from 0 to 100 (as in the Gimp user interface).</dl>
<h2>EXIT STATUS</h2>
<p> The exit status of <code>xcf2png</code> is</p>
<dl>
<dt>0</p>
<dd> Success</p>
<dt>20</p>
<dd> Problems parsing the command line, including unknown color names (or missing color name directory) for <code>-b</code>.</p>
<dt>21</p>
<dd> The specified XCF file does not exist or cannot be read.</p>
<dt>22</p>
<dd> A layer named on the command line was not found, or the <code>&#8211;mask</code> option was used for a layer that has no layer mask.</p>
<dt>102</p>
<dd> The <code>-G</code> option was given, yet partial transparency was found.</p>
<dt>103</p>
<dd> <code>-g</code> was given, yet colored pixels were found.</p>
<dt>123</p>
<dd> The XCF file contains presumably valid features that <code>xcftools</code> does not support. (As of this writing there is no known way of getting the Gimp to write an XCF file that will provoke this return. Please notify the author if you discover one).</p>
<dt>125</p>
<dd> The XCF file is malformed.</p>
<dt>126</p>
<dd> An uncompression program could not be executed, or terminated abnormally.</p>
<dt>127</p>
<dd> Unexpected I/O error, internal errors, or other &quot;this can&#8217;t happen&quot; situations. If an uncompression program returns an error exit status, this will be returned from <code>xcf2png</code> too.</dl>
<h2>BUGS AND LIMITATIONS</h2>
<p> When several partially transparent layers are merged, the pixel values are interpolated without gamma correction. (The Gimp also does it this way). Some slight rounding errors in the interpolation are inevitable; <code>xcf2png</code> sometimes has different rounding errors than the Gimp itself, especially when more than two layers are involved, or in case of some of the more exotic layer modes. These differences are usually not visible to the eye. Floating selections are currently not handled correctly. There are probably other bugs lurking in corner cases. If you discover one, please notify the author. </p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/X11/rgb.txt</code></p>
<dd>
<dt><code>/usr/share/X11/rgb.txt</code></p>
<dd>
<dt><code>/usr/lib/X11/rgb.txt</code></p>
<dd> Color name database for <code>-b</code>.</dl>
<h2>AUTHOR</h2>
<p> <code>xcf2png</code> was written by Henning Makholm &lt;henning [at] makholm.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xcfinfo/">xcfinfo</a></code>(1), <code><a href="/docs/linux/man/1-xcf2pnm/">xcf2pnm</a></code>(1) </p>
<h2>Index</h2>
