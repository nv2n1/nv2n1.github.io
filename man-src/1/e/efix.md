---
title: "efix(1)"
name: "efix"
section: "1"
letter: "e"
url: "/docs/linux/man/1-efix/"
description: "efix – convert between fax, text, bit-map and gray-scale formats"
---

<h2 class="name">NAME</h2>
<p> efix &#8211; convert between fax, text, bit-map and gray-scale formats </p>
<h2>SYNOPSIS</h2>
<p> <code>efix</code> [ <i>options</i> ] <i>file&#8230;</i> </p>
<h2>OPTIONS</h2>
<p> Where <i>options</i> are: </p>
<dl>
<dt><code>-i </code><i>f</i></p>
<dd> the input image is in format <i>f</i>. Default is to automatically determine the input type from its contents. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fax</code></p>
<dd> fax (&quot;Group3&quot;) 1-D coded image </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>text</code></p>
<dd> text. Line feeds separate lines, form feeds cause page breaks and tabs are expanded assuming tabs every 8 columns. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pbm</code></p>
<dd> raw PBM (portable bit map) </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>tiffg3</code></p>
<dd> TIFF format with Group 3 (fax) compression. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>tiffraw</code></p>
<dd> TIFF format with no compression. </p>
<dt><code>-o </code><i>f</i></p>
<dd> write the output in format <i>f</i>. Default is tiffg3. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fax</code></p>
<dd> fax (&quot;Group3&quot;) 1-D coded image </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pbm</code></p>
<dd> raw PBM </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pgm</code></p>
<dd> raw PGM (Portable Gray Map). Gray-scale values are produced by summing pixels in 4&#215;4 pixel blocks. The output file is 1/4 of the size given by -p. The resulting image has 17 discrete values between 0 and 255. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pcl</code></p>
<dd> HP-PCL (e.g. HP LaserJet). </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ps</code></p>
<dd> encapsulated Postscript (e.g. Apple Laserwriter). The file is compressed using differential coding vertically and run-length coding horizontally. There is no provision for positioning the image within the page and so the image will appear at the lower left corner of the page when printed. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>tiffg3</code></p>
<dd> TIFF format with Group 3 (fax) compression. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>tiffraw</code></p>
<dd> TIFF format with no compression. </p>
<dt><code>-n </code><i>pat</i></p>
<dd> use the <a href="/docs/linux/man/3-printf/">printf</a>(3) pattern <i>path</i> to generate the output file name. Up to three %d escapes will be replaced by the page number starting with 1 (e.g. -n order.%03d will create file names order.001, order.002, etc.) </p>
<dt><code>-v </code><i>lvl</i></p>
<dd> print messages of type in string <i>lvl</i>. Each <i>lower-case</i> letter in <i>lvl</i> enables one type of message: </p>
<dl>
<dt>
<dd> <code>e &#8211; </code> errors<br />
 <code>w &#8211; </code> warnings<br />
 <code>i &#8211; </code> information messages<br />
 <code>a &#8211; </code> program arguments<br />
 <code>f &#8211; </code> file format details</dl>
<dl>
<dt>
<dd> The default is &quot;ewi&quot;.</dl>
<dt><code>-f </code><i>fnt</i></p>
<dd> use font file <i>fnt</i> for text. The font file for an WxH font should be a bit map of an image of H rows and 256*W columns. Each successive WxH cell contains the bit map for characters with codes from 0 to 255. The default is to use a built-in 8&#215;16 font. </p>
<dt><code>-s </code><i>X</i>x<i>Y</i></p>
<dd> scale the input by a factor of X horizontally and Y vertically. Scaling does not change the size of the output (use -p). If Y is not specified it is assumed to be the same as X. Any floating point value may be used for X and Y. The default is 1,1. </p>
<dt><code>-d </code><i>R</i>,<i>D</i></p>
<dd> displace the output right by R and down by D (opposite if negative). See below for units. Default is 0,0. </p>
<dt><code>-p </code><i>W</i>x<i>H</i></p>
<dd> truncate or pad the output to generate an image of width W and height H. This does not scale the input. See below for units. The default is the size of the input image if it can be determined or A4 (215x297mm) if it can&#8217;t. </p>
<dt><code>-r </code><i>X</i>x<i>Y</i></p>
<dd> assume an output device resolution of X by Y dots per inch. If Y is not specified it is assumed to be the same as X. The default is the input resolution if it can be determined or the fax resolution of 204.1&#215;195.6 dpi if it can&#8217;t. </p>
<dt><code>-R </code><i>X</i>x<i>Y</i></p>
<dd> assume an input device resolution of X by Y dots per inch. If Y is not specified it is assumed to be the same as X. The default is the input resolution if it can be determined or the fax resolution of 204.1&#215;195.6 dpi if it can&#8217;t. </p>
<dt><code>-l </code><i>n</i></p>
<dd> place n lines per page during text input. Default is 66. </p>
<dt><code>-O </code><i>f</i></p>
<dd> overlay (logical OR) the image from file f into the output. Use &quot;-&quot; for standard input (-O-). Default is no overlay file. </p>
<dt><code>-M</code></p>
<dd> ignore all other options and copy the standard input to the standard output while applying base64 (MIME) encoding as specified by RFC 1521. </p>
</dl>
<h2>FILES</h2>
<p> If no -n options are given, output is written to the standard output. </p>
<h2>UNITS</h2>
<p> The units of the W, H, R, and D values above are in inches by default. Any floating point value may be used. Units of inches, centimetres, millimetres or points (72 per inch) can be used instead by appending one of the strings `in&#8217;, `cm&#8217;, `mm&#8217;, or `pt&#8217; to the argument (e.g. -d2,4cm). </p>
<h2>CUT AND PASTE</h2>
<p> The -d and -p options allow efix to cut out images from received faxes for use in other faxes or documents. The -d option specifies the top left portion of the desired image and the -p option gives the size of the cut image. For example, the command</p>
<dl>
<dt>
<dd>
<pre>
        efix -d-5,-8 -p2,1 sample.001 &gt;sig.001
</pre>
</dl>
<p> would cut out part of the input with its top left corner 5 inches from the left edge and 8 inches from top of the input image. The output image would be 2 inches wide and 1 inch high. </p>
<p> The -O option allows efix to superimpose two or more images. The overlay image must be in fax format and cannot be scaled, truncated or shifted. However, multiple efix commands may be used to transform images before combining them. For example, the commands</p>
<dl>
<dt>
<dd>
<pre>
        efix -d4,8 signature &gt;sig.fax
        efix -O sig.fax letterhead &gt;letterhead.fax
        efix -O letterhead.fax letter.002 &gt;letter.002.new
</pre>
</dl>
<p> will shift the image in the file signature down 8 inches and right 4 inches and combine (overlay) it with the images in the files letterhead and letter.002. </p>
<h2>REFERENCES</h2>
<p> Gunter Born, &quot;The File Formats Handbook&quot;, International Thompson Computer Press, 1995. </p>
<h2>COPYRIGHT</h2>
<p> efix is copyright 1994 &#8212; 1999 by Ed Casas. It may be used, copied and modified under the terms of the GNU Public License. </p>
<h2>DISCLAIMER</h2>
<p> Although <code>efix</code> has been tested it may have errors that will prevent it from working correctly on your system. Some of these errors may cause serious problems including loss of data. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-efax/">efax</a>(1),</code> <code><a href="/docs/linux/man/1-ghostscript/">ghostscript</a>(1),</code> <code><a href="/docs/linux/man/5-pbm/">pbm</a>(5),</code> <code><a href="/docs/linux/man/5-pgm/">pgm</a>(5).</code> </p>
<h2>BUGS</h2>
<p> Only reads two types of TIFF compression formats. </p>
<p> Does not write multi-page TIFF files (a feature). </p>
<h2>Index</h2>
