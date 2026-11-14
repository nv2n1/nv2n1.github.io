---
title: "grn(1)"
name: "grn"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grn/"
description: "grn – groff preprocessor for gremlin files"
---

<h2 class="name">NAME</h2>
<p> grn &#8211; groff preprocessor for gremlin files </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-Cv</code> ] [ <code>-T </code><i>dev</i> ] [ <code>-M </code><i>dir</i> ] [ <code>-F </code><i>dir</i> ] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <i>grn</i> is a preprocessor for including <i>gremlin</i> pictures in <i>groff</i> input. <i>grn</i> writes to standard output, processing only input lines between two that start with <code>.GS</code> and <code>.GE</code>. Those lines must contain <i>grn</i> commands (see below). These commands request a <i>gremlin</i> file, and the picture in that file is converted and placed in the <i>troff</i> input stream. The <code>.GS</code> request may be followed by a C, L, or R to center, left, or right justify the whole <i>gremlin</i> picture (default justification is center). If no <i>file</i> is mentioned, the standard input is read. At the end of the picture, the position on the page is the bottom of the <i>gremlin</i> picture. If the <i>grn</i> entry is ended with <code>.GF</code> instead of <code>.GE</code>, the position is left at the top of the picture. </p>
<p> Please note that currently only the -me macro package has support for <code>.GS</code>, <code>.GE</code>, and <code>.GF</code>.</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>-T</code><i>dev</i></p>
<dd> Prepare output for printer <i>dev</i>. The default device is <code>ps</code>. See <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) for acceptable devices.</p>
<dt><code>-M</code><i>dir</i></p>
<dd> Prepend <i>dir</i> to the default search path for <i>gremlin</i> files. The default path is (in that order) the current directory, the home directory, <i>/usr/:lib/:groff/:site-tmac</i>, <i>/usr/:share/:groff/:site-tmac</i>, and <i>/usr/:share/:groff/:1.22.4/:tmac</i>.</p>
<dt><code>-F</code><i>dir</i></p>
<dd> Search <i>dir</i> for subdirectories <i>dev</i>name (<i>name</i> is the name of the device) for the <i>DESC</i> file before the default font directories <i>/usr/:share/:groff/:site-font</i>, <i>/usr/:share/:groff/:1.22.4/:font</i>, and <i>/usr/:lib/:font</i>.</p>
<dt><code>-C</code></p>
<dd> Recognize <code>.GS</code> and <code>.GE</code> (and <code>.GF</code>) even when followed by a character other than space or newline.</p>
<dt><code>-v</code></p>
<dd> Print the version number.</dl>
<h2>GRN COMMANDS</h2>
<p> Each input line between <code>.GS</code> and <code>.GE</code> may have one <i>grn</i> command. Commands consist of one or two strings separated by white space, the first string being the command and the second its operand. Commands may be upper or lower case and abbreviated down to one character. </p>
<p> Commands that affect a picture&#8217;s environment (those listed before <code>default</code>, see below) are only in effect for the current picture: The environment is reinitialized to the defaults at the start of the next picture. The commands are as follows:</p>
<dl>
<dt><code>1&nbsp;</code><i>N</i></p>
<dd> <code>2&nbsp;</code><i>N</i> <code>3&nbsp;</code><i>N</i> <code>4&nbsp;</code><i>N</i> Set <i>gremlin</i>&#8216;s text size number 1 (2, 3, or 4) to <i>N</i> points. The default is 12 (16, 24, and 36, respectively).</p>
<dt><code>roman&nbsp;</code><i>f</i></p>
<dd> <code>italics&nbsp;</code><i>f</i> <code>bold&nbsp;</code><i>f</i> <code>special&nbsp;</code><i>f</i> Set the roman (italics, bold, or special) font to <i>troff</i>&#8216;s font <i>f</i> (either a name or number). The default is R (I, B, and S, respectively).</p>
<dt><code>l&nbsp;</code><i>f</i></p>
<dd> <code>stipple&nbsp;</code><i>f</i> Set the stipple font to <i>troff</i>&#8216;s stipple font <i>f</i> (name or number). The command <code>stipple</code> may be abbreviated down as far as &#8216;st&#8217; (to avoid confusion with <code>special</code>). There is <i>no</i> default for stipples (unless one is set by the default command), and it is invalid to include a <i>gremlin</i> picture with polygons without specifying a stipple font.</p>
<dt><code>x&nbsp;</code><i>N</i></p>
<dd> <code>scale&nbsp;</code><i>N</i> Magnify the picture (in addition to any default magnification) by <i>N</i>, a floating point number larger than zero. The command <code>scale</code> may be abbreviated down to &#8216;sc&#8217;.</p>
<dt><code>narrow&nbsp;</code><i>N</i></p>
<dd> <code>medium&nbsp;</code><i>N</i> <code>thick&nbsp;</code><i>N</i> Set the thickness of <i>gremlin</i>&#8216;s narrow (medium and thick, respectively) lines to <i>N</i> times 0.15pt (this value can be changed at compile time). The default is 1.0 (3.0 and 5.0, respectively), which corresponds to 0.15pt (0.45pt and 0.75pt, respectively). A thickness value of zero selects the smallest available line thickness. Negative values cause the line thickness to be proportional to the current point size.</p>
<dt><code>pointscale&nbsp;</code><i>&lt;off/on&gt;</i></p>
<dd> Scale text to match the picture. Gremlin text is usually printed in the point size specified with the commands <code>1</code>, <code>2</code>, <code>3</code>, or~<code>4</code>, regardless of any scaling factors in the picture. Setting <code>pointscale</code> will cause the point sizes to scale with the picture (within <i>troff</i>&#8216;s limitations, of course). An operand of anything but <i>off</i> will turn text scaling on.</p>
<dt><code>default</code></p>
<dd> Reset the picture environment defaults to the settings in the current picture. This is meant to be used as a global parameter setting mechanism at the beginning of the <i>troff</i> input file, but can be used at any time to reset the default settings.</p>
<dt><code>width&nbsp;</code><i>N</i></p>
<dd> Forces the picture to be <i>N</i> inches wide. This overrides any scaling factors present in the same picture. &#8216;<code>width</code> <i>0</i>&#8216; is ignored.</p>
<dt><code>height&nbsp;</code><i>N</i></p>
<dd> Forces picture to be <i>N</i> inches high, overriding other scaling factors. If both &#8216;width&#8217; and &#8216;height&#8217; are specified the tighter constraint will determine the scale of the picture. <code>Height</code> and <code>width</code> commands are not saved with a <code>default</code> command. They will, however, affect point size scaling if that option is set.</p>
<dt><code>file&nbsp;</code><i>name</i></p>
<dd> Get picture from <i>gremlin</i> file <i>name</i> located the current directory (or in the library directory; see the <code>-M</code> option above). If two <code>file</code> commands are given, the second one overrides the first. If <i>name</i> doesn&#8217;t exist, an error message is reported and processing continues from the <code>.GE</code> line.</dl>
<h2>NOTES ABOUT GROFF</h2>
<p> Since <i>grn</i> is a preprocessor, it doesn&#8217;t know about current indents, point sizes, margins, number registers, etc. Consequently, no <i>troff</i> input can be placed between the <code>.GS</code> and <code>.GE</code> requests. However, <i>gremlin</i> text is now processed by <i>troff</i>, so anything valid in a single line of <i>troff</i> input is valid in a line of <i>gremlin</i> text (barring &#8216;.&#8217; directives at the beginning of a line). Thus, it is possible to have equations within a <i>gremlin</i> figure by including in the <i>gremlin</i> file <i>eqn</i> expressions enclosed by previously defined delimiters (e.g. <i>$$</i>). </p>
<p> When using <i>grn</i> along with other preprocessors, it is best to run <i>tbl</i> before <i>grn</i>, <i>pic</i>, and/or <i>ideal</i> to avoid overworking <i>tbl</i>. <i>Eqn</i> should always be run last. </p>
<p> A picture is considered an entity, but that doesn&#8217;t stop <i>troff</i> from trying to break it up if it falls off the end of a page. Placing the picture between &#8216;keeps&#8217; in -me macros will ensure proper placement. </p>
<p> <i>grn</i> uses <i>troff</i>&#8216;s number registers <code>g1</code> through <code>g9</code> and sets registers <code>g1</code> and <code>g2</code> to the width and height of the <i>gremlin</i> figure (in device units) before entering the <code>.GS</code> request (this is for those who want to rewrite these macros).</p>
<h2>GREMLIN FILE FORMAT</h2>
<p> There exist two distinct <i>gremlin</i> file formats, the original format from the <i>AED</i> graphic terminal version, and the <i>SUN</i> or <i>X11</i> version. An extension to the <i>SUN</i>/<i>X11</i> version allowing reference points with negative coordinates is <code>not</code> compatible with the <i>AED</i> version. As long as a <i>gremlin</i> file does not contain negative coordinates, either format will be read correctly by either version of <i>gremlin</i> or <i>grn</i>. The other difference from <i>SUN</i>/<i>X11</i> format is the use of names for picture objects (e.g., POLYGON, CURVE) instead of numbers. Files representing the same picture are shown in Table 1 in each format. </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td>sungremlinfile</td>
<td></td>
<td>gremlinfile
</td>
</tr>
<tr VALIGN=top>
<td>0 240.00 128.00</td>
<td></td>
<td>0 240.00 128.00
</td>
</tr>
<tr VALIGN=top>
<td>CENTCENT</td>
<td></td>
<td>2
</td>
</tr>
<tr VALIGN=top>
<td>240.00 128.00</td>
<td></td>
<td>240.00 128.00
</td>
</tr>
<tr VALIGN=top>
<td>185.00 120.00</td>
<td></td>
<td>185.00 120.00
</td>
</tr>
<tr VALIGN=top>
<td>240.00 120.00</td>
<td></td>
<td>240.00 120.00
</td>
</tr>
<tr VALIGN=top>
<td>296.00 120.00</td>
<td></td>
<td>296.00 120.00
</td>
</tr>
<tr VALIGN=top>
<td>*</td>
<td></td>
<td>-1.00 -1.00
</td>
</tr>
<tr VALIGN=top>
<td>2 3</td>
<td></td>
<td>2 3
</td>
</tr>
<tr VALIGN=top>
<td>10 A Triangle</td>
<td></td>
<td>10 A Triangle
</td>
</tr>
<tr VALIGN=top>
<td>POLYGON</td>
<td></td>
<td>6
</td>
</tr>
<tr VALIGN=top>
<td>224.00 416.00</td>
<td></td>
<td>224.00 416.00
</td>
</tr>
<tr VALIGN=top>
<td>96.00 160.00</td>
<td></td>
<td>96.00 160.00
</td>
</tr>
<tr VALIGN=top>
<td>384.00 160.00</td>
<td></td>
<td>384.00 160.00
</td>
</tr>
<tr VALIGN=top>
<td>*</td>
<td></td>
<td>-1.00 -1.00
</td>
</tr>
<tr VALIGN=top>
<td>5 1</td>
<td></td>
<td>5 1
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td></td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>-1</td>
<td></td>
<td>-1
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 1. File examples
</td>
</tr>
</table>
<p></center> </p>
<dl>
<dt>&bull;</p>
<dd> The first line of each <i>gremlin</i> file contains either the string <code>gremlinfile</code> (<i>AED</i> version) or <code>sungremlinfile</code> (<i>SUN</i>/<i>X11</i>)</p>
<dt>&bull;</p>
<dd> The second line of the file contains an orientation, and <code>x</code> and <code>y</code> values for a positioning point, separated by spaces. The orientation, either <code>0</code> or <code>1</code>, is ignored by the <i>SUN</i>/<i>X11</i> version. <code>0</code> means that <i>gremlin</i> will display things in horizontal format (drawing area wider than it is tall, with menu across top). <code>1</code> means that <i>gremlin</i> will display things in vertical format (drawing area taller than it is wide, with menu on left side). <code>x</code> and <code>y</code> are floating point values giving a positioning point to be used when this file is read into another file. The stuff on this line really isn&#8217;t all that important; a value of &#8220;1 0.00 0.00&#8221; is suggested.</p>
<dt>&bull;</p>
<dd> The rest of the file consists of zero or more element specifications. After the last element specification is a line containing the string &#8220;-1&#8221;.</p>
<dt>&bull;</p>
<dd> Lines longer than 127 characters are chopped to this limit.</dl>
<h2>ELEMENT SPECIFICATIONS</h2>
<dl>
<dt>&bull;</p>
<dd> The first line of each element contains a single decimal number giving the type of the element (<i>AED</i> version) or its ASCII name (<i>SUN</i>/<i>X11</i> version). See Table 2. </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3><i>gremlin</i> File Format &#8211; Object Type Specification
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>AED</i> Number</td>
<td ALIGN=center><i>SUN/</i>/,<i>X11</i> Name</td>
<td ALIGN=center>Description
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>BOTLEFT</td>
<td>bottom-left-justified text
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>BOTRIGHT</td>
<td>bottom-right-justified text
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>CENTCENT</td>
<td>center-justified text
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>VECTOR</td>
<td>vector
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>ARC</td>
<td>arc
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>CURVE</td>
<td>curve
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>POLYGON</td>
<td>polygon
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>BSPLINE</td>
<td>b-spline
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>BEZIER</td>
<td>B&eacute;zier
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>TOPLEFT</td>
<td>top-left-justified text
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>TOPCENT</td>
<td>top-center-justified text
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>TOPRIGHT</td>
<td>top-right-justified text
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>CENTLEFT</td>
<td>left-center-justified text
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>CENTRIGHT</td>
<td>right-center-justified text
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>BOTCENT</td>
<td>bottom-center-justified text
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 2.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Type Specifications in <i>gremlin</i> Files
</td>
</tr>
</table>
<p></center> </p>
<dt>&bull;</p>
<dd> After the object type comes a variable number of lines, each specifying a point used to display the element. Each line contains an x-coordinate and a y-coordinate in floating point format, separated by spaces. The list of points is terminated by a line containing the string &#8220;-1.0 -1.0&#8221; (<i>AED</i> version) or a single asterisk, &#8220;*&#8221; (<i>SUN</i>/<i>X11</i> version).</p>
<dt>&bull;</p>
<dd> After the points comes a line containing two decimal values, giving the brush and size for the element. The brush determines the style in which things are drawn. For vectors, arcs, and curves there are six valid brush values: </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=right>1 &#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=center></td>
<td>thin dotted lines
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2 &#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=center></td>
<td>thin dot-dashed lines
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3 &#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=center></td>
<td>thick solid lines
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4 &#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=center></td>
<td>thin dashed lines
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>5 &#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=center></td>
<td>thin solid lines
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>6 &#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=center></td>
<td>medium solid lines
</td>
</tr>
</table>
<p></center> </p>
<p> For polygons, one more value, 0, is valid. It specifies a polygon with an invisible border. For text, the brush selects a font as follows: </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=right>1 &#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=center></td>
<td>roman (R font in groff)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2 &#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=center></td>
<td>italics (I font in groff)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3 &#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=center></td>
<td>bold (B font in groff)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4 &#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=center></td>
<td>special (S font in groff)
</td>
</tr>
</table>
<p></center> </p>
<p> If you&#8217;re using <i>grn</i> to run your pictures through <i>groff</i>, the font is really just a starting font: The text string can contain formatting sequences like &#8220;I&#8221; or &#8220;\d&#8221; which may change the font (as well as do many other things). For text, the size field is a decimal value between 1 and 4. It selects the size of the font in which the text will be drawn. For polygons, this size field is interpreted as a stipple number to fill the polygon with. The number is used to index into a stipple font at print time.</p>
<dt>&bull;</p>
<dd> The last line of each element contains a decimal number and a string of characters, separated by a single space. The number is a count of the number of characters in the string. This information is only used for text elements, and contains the text string. There can be spaces inside the text. For arcs, curves, and vectors, this line of the element contains the string &#8220;0&#8221;.</dl>
<h2>NOTES ON COORDINATES</h2>
<p> <i>gremlin</i> was designed for <i>AED</i>s, and its coordinates reflect the <i>AED</i> coordinate space. For vertical pictures, x-values range 116 to 511, and y-values from 0 to 483. For horizontal pictures, x-values range from 0 to 511 and y-values range from 0 to 367. Although you needn&#8217;t absolutely stick to this range, you&#8217;ll get best results if you at least stay in this vicinity. Also, point lists are terminated by a point of (-1, -1), so you shouldn&#8217;t ever use negative coordinates. <i>gremlin</i> writes out coordinates using format &#8220;%f1.2&#8221;; it&#8217;s probably a good idea to use the same format if you want to modify the <i>grn</i> code.</p>
<h2>NOTES ON SUN/X11 COORDINATES</h2>
<p> There is no longer a restriction on the range of coordinates used to create objects in the <i>SUN</i>/<i>X11</i> version of <i>gremlin</i>. However, files with negative coordinates <code>will</code> cause problems if displayed on the <i>AED</i>.</p>
<h2>FILES</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/:font/dev</i>name<i>/DESC</i></p>
<dd> Device description file for device <i>name</i>.</dl>
<h2>AUTHORS</h2>
<p> David Slattengren and Barry Roitblat wrote the original Berkeley <i>grn</i>. Daniel Senderowicz and Werner Lemberg modified it for <i>groff</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gremlin/">gremlin</a></code>(1), <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-pic/">pic</a></code>(1), <code><a href="/docs/linux/man/1-ideal/">ideal</a></code>(1) </p>
<h2>Index</h2>
