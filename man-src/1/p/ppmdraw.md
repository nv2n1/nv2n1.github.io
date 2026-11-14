---
title: "ppmdraw(1)"
name: "ppmdraw"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmdraw/"
description: "ppmdraw – draw lines, text, etc on a PPM image"
---

<h2 class="name">NAME</h2>
<p> ppmdraw &#8211; draw lines, text, etc on a PPM image</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmdraw</code> </p>
<p> { <code>-script=</code><i>script</i> | <code>-scriptfile=</code><i>filename</i> } [<code>-verbose</code>] </p>
<p> [<i>ppmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>ppmdraw</code> draws lines, shapes, text, etc. on a PPM image. It is essentially an easy-to-program front end to <code>libnetpbm</code>&#8216;s &#8216;ppmd&#8217; subroutines. It lets you create a human-friendly script to describe the drawing rather than write a C program. </p>
<p> You supply drawing instructions with a script, which you supply either in a file named by a <code>-scriptfile</code> option or as the value of a <code>-script</code> option. Here is an example script: </p>
<pre><code>

setpos 50 50;
text_here 10 30 'hello';
setcolor black;
text_here 10 0 'there';
line_here 5 20;
</code></pre>
<p> This example starts at Column 50, Row 50 of the input image and writes the word &#8216;hello&#8217; there in 10 pixel high white letters at a 30 degree angle up from horizontal. Then, from where that leaves off, the script writes &#8216;there&#8217; in 10 pixel high black letters horizontally. Finally, it draws a black line to a point 5 pixels over and 20 pixels down from the end of &#8216;there.&#8217; </p>
<p> If you don&#8217;t specify <i>ppmfile</i>, <code>ppmdraw</code> reads its input PPM image from Standard Input. </p>
<p> The output image goes to Standard Output. </p>
<p> <code>ppmdraw</code> works on multi-image streams. It executes the same script on each input image and produces an output stream with one image for each input image. But before Netpbm 10.32 (February 2006), <code>ppmdraw</code> ignored every image after the first. </p>
<p> If you just want to add a single line of text to an image, <code>ppmlabel</code> may be more what you want. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-script=</code><i>script</i></p>
<dd> This option gives the script. See Script . </p>
<p> You may not specify both <code>-script</code> and <code>-scriptfile</code>. </p>
<dt><code>-scriptfile=</code><i>filename</i></p>
<dd> This option names a file that contains the script. <code>&#8211;</code> means Standard Input. </p>
<p> You may not specify both <code>-script</code> and <code>-scriptfile</code>. </p>
<p> You may not specify <code>&#8211;</code> (Standard Input) for both <code>-scriptfile</code> and the input image file. </p>
</dl>
<h2>SCRIPT</h2>
<p> The heart of <code>ppmdraw</code> function is its script. The script is a character stream. The stream consists of commands. Commands are separated by semicolons. White space is regarded just like in C: Any contiguous stretch of unquoted white space is equivalent to a single space character. Note that this means newlines have no particular significance. </p>
<p> A command is composed of tokens, separated from each other by white space. To write a token that contains white space, enclose it in double quotes. Everything between two matched quotation marks is one token. </p>
<p> The first token of a command is the verb, which determines the basic function of the command. The rest of the tokens of the command are arguments, the meaning of which depends upon the verb. The following list gives all the valid verbs, and for each its meaning and its arguments. </p>
<p> Many command have arguments that specify a position on the canvas, which you specify by row and column. Row 0 is the top row. Column 0 is the leftmost column. You may specify negative numbers (but such a position would necessarily be off the canvas). </p>
<p> Your drawing instructions may involve positions not on the canvas. But any pixels you draw there just get discarded. </p>
<dl>
<dt>setpos</p>
<dd> Set the &#8216;current position&#8217; in the image. This affects where subsequent commands draw things. The 2 arguments are the column and row number. </p>
<p> At the start of the script, the current position is (0,0). </p>
<dt>setlinetype</p>
<dd> The 1 argument is &#8216;normal&#8217; or &#8216;nodiag.&#8217;. This effects a <code>ppmd_setlinetype()</code> call. Further details are not yet documented. </p>
<dt>setlineclip</p>
<dd> This effects a <code>ppmd_setlineclip()</code> call. Not yet documented. </p>
<dt>setcolor</p>
<dd> This sets the &#8216;current color&#8217;, which determines the color in which subsequent drawing commands draw. Before the first <code>setcolor</code>, the current color is white. </p>
<dt>setfont</p>
<dd> This sets the &#8216;current font&#8217;, which determines the font in which subsequent text drawing commands draw. Before the first <code>setfont</code>, the current color is a built in font called &#8216;standard.&#8217; </p>
<p> The argument of this command is a file name. It is the name of a Netpbm PPMD font file. </p>
<p> A Netpbm PPMD font file typically has a name that ends in &#8216;.ppmdfont&#8217; and its first 8 bytes are the ASCII encoding of &#8216;ppmdfont&#8217;. </p>
<p> There is only one of these fonts as far as we know. It is distributed with Netpbm as the file <code>standard.ppmdfont</code>, but you don&#8217;t need to use that file because the same font is built into the Netpbm library and is the default. If you want to make a new font, you can find the format of a ppmdfont file in the Netpbm interface header file <code>ppmdfont.h</code>, but you&#8217;ll have to make your own tools to build it. </p>
<dt>line</p>
<dd> This draws a one pixel wide line in the current color. The 4 arguments are: starting column, starting row, ending column, ending row. </p>
<p> This command does not affect the current position. </p>
<dt>line_here</p>
<dd> This is like <code>line</code>, except it works in a more relative way. </p>
<p> The line starts at the current point. The two arguments are the rightward and downward displacement from there to the terminal point. The command moves the current position to the terminal point after drawing. </p>
<dt>spline3</p>
<dd> This draws a spline in the current color between 2 points, using a third as a control point. It approximates a cubic spline segment. </p>
<p> The shape of the curve is such that it passes through the specified endpoints, and lines tangent to the curve at those endpoints intersect at the control point. Controlling the tangents allows you to connect this curve to other curves generated the same way without having corners at the connection points. </p>
<p> The 6 arguments are the starting point column, starting point row, control point column, control point row, ending point column, and ending point row. </p>
<p> This command does not affect the current position. </p>
<dt>circle</p>
<dd> This command draws a circle in the current color. The three arguments are the column number and row number of the center of the circle and the radius of the circle in pixels. </p>
<dt>filledrectangle</p>
<dd> This command draws a rectangle filled with the current color. </p>
<p> The 4 arguments are the column and row numbers of the upper left corner of the rectangle, the width of the rectangle, and the height of the rectangle. </p>
<dt>text</p>
<dd> This command draws text in the current color in the built-in font. The 5 arguments are: </p>
<dt>&bull;</p>
<dd> column number of starting point of baseline</p>
<dt>&bull;</p>
<dd> row number of starting point of baseline</p>
<dt>&bull;</p>
<dd> height of characters, in pixels</p>
<dt>&bull;</p>
<dd> angle of baseline in degrees elevated from the horizontal</p>
<dt>&bull;</p>
<dd> text </p>
<p> Note that if your text contains white space, you&#8217;ll have to use double quotes to cause it to be a single token. </p>
<dt>text_here</p>
<dd> This is like <code>text</code>, except that the baseline starts at the current position and the command updates the current position to the other end of the baseline after it draws. </p>
<p> Bear in mind that a script starts with the current position in the top line, so if you leave it there, only the bottom line of your text will be within the image! </p>
</dl>
<h2>HISTORY</h2>
<p> <code>ppmdraw</code> was new in Netpbm 10.29 (August 2005). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmlabel/">ppmlabel</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<h2>Index</h2>
