---
title: "pamwipeout(1)"
name: "pamwipeout"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamwipeout/"
description: "pamwipeout – replace detail with smooth gradient from one edge to the other"
---

<h2 class="name">NAME</h2>
<p> pamwipeout &#8211; replace detail with smooth gradient from one edge to the other</p>
<h2>SYNOPSIS</h2>
<p> <code>pamwipeout</code> {<code>-lr | -tb</code>} [<i>filename</i>] </p>
<p> Minimum unique abbreviation of options is acceptable. You may use double hyphens instead of single hyphen to denote options. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> The <code>pamwipeout</code> utility takes a Neptbm image as input and the uses two opposite edges of the image to wipe out anything in between. You can use it in combination with <code>pamcut</code> and <code>pnmpaste</code> / <code>pamcomp</code> to remove unwanted parts of a larger image. The program replaces the pixels in between the two edges with a gradient from one edge to the other. </p>
<p> In <code>top-bottom</code> mode, the program reads the whole image into memory before it can start processing. In <code>left-right</code> it will read the image a row at the time, process that row and write it to the output file. Therefore, in case of very large images, it may be better to use instead of &quot;<code>pamwipeout -tb</code>&quot; a pipe of &quot;<code>pamflip -cw | pamwipeout -lr | pamflip -ccw</code>&quot;. </p>
<p> In his blog at<br />
&nbsp;<wbr> <a rel="nofollow" href="http://www.i-am.ws">www.i-am.ws</a> , the author wrote about a predecessor of &quot;pamwipeout&quot; at the time named &quot;pnmblend&quot;. It shows a good example of what can be accomplished with this utility. </p>
<h2>PARAMETERS</h2>
<p> <i>Filename</i> is the name of the input file. If you don&#8217;t specify this, <code>pamwipeout</code> reads the image from Standard Input. </p>
<h2>OPTIONS</h2>
<p> &lt;dl compact=&quot;compact&quot;&gt;</p>
<dl>
<dt><code>-tb</code> | <code>-lr</code></p>
<dd>
<p> This option chooses between a vertical and a horizontal gradient. You must specify one of these, but not both. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1)<br />
&nbsp;<wbr>and <code><a href="/docs/linux/man/1-pamflip/">pamflip</a></code>(1) , <code><a href="/docs/linux/man/1-pamcut/">pamcut</a></code>(1) , <code><a href="/docs/linux/man/1-pamcomp/">pamcomp</a></code>(1) , <code><a href="/docs/linux/man/1-pnmpaste/">pnmpaste</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamwipeout</code> was new in Netpbm 10.54 (March 2011). </p>
<h2>AUTHORS</h2>
<p> <i>Willem van Schaik</i> wrote this program in January 2011 and contributed it to Netpbm. </p>
<h2>Index</h2>
