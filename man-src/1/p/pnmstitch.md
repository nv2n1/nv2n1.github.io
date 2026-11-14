---
title: "pnmstitch(1)"
name: "pnmstitch"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmstitch/"
description: "pnmstitch – stitch together two panoramic (side-by-side) photographs"
---

<h2 class="name">NAME</h2>
<p> pnmstitch &#8211; stitch together two panoramic (side-by-side) photographs</p>
<h2>SYNOPSIS</h2>
<p> <code>pnmstitch</code> [ [<i>left_filespec</i>] <i>right_filespec</i> | <i>left_filespec</i> <i>right_filespec</i> <i>output_filespec</i> ] [<code>-width=</code><i>width</i>] [<code>-height=</code><i>height</i>] [<code>-xrightpos=</code><i>column</i>] [<code>-yrightpos=</code><i>row</i>] [<code>-stitcher=</code>{<code>RotateSliver</code>, <code>BiLinearSliver</code>,<code>LinearSliver</code>}] [<code>-filter=</code>{<code>LineAtATime</code>,<code>HorizontalCrop</code>}] [<code>-output=</code><i>output_filespec</i>] [<code>-verbose</code>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pnmstitch</code> stitches together two panoramic photographs. This means if you have photographs of the left and right side of something that is too big for a single camera frame, <code>pnmstitch</code> can join them into one wide picture. </p>
<p> <code>pnmstitch</code> works only on side-by-side images, not top and bottom (though you could certainly use <code>pamflip</code> in combination with <code>pnmstitch</code> to achieve this). It stitches together two images, but you can use it repeatedly to stitch together as many as you need to. </p>
<p> Your photographs must overlap in order for <code>pnmstitch</code> to work, and the overlap should be substantial. <code>pnmstitch</code> shifts and stretches the right hand image to match it up the left hand image. You probably want to crop the result with <code>pamcut</code> to make a nice rectangular image. </p>
<p> If you&#8217;re just trying to join (concatenate) two images at their edges, use <code>pnmcat</code>. </p>
<p> The <i>left_filespec</i> and <i>right_filespec</i> arguments are the specifications (names) of the PNM files containing the left hand and right hand images. If you specify only <i>right_filespec</i>, the left hand image comes from Standard Input. If you specify neither, both images come from Standard Input as a multi-image file containing first the left and then the right image. </p>
<p> <i>output_filespec</i> is the specification (name) of the output PNM file. The <code>-output</code> option also specifies the output file. You cannot specify both the argument and the option. If you specify neither, the output goes to Standard Output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-width=</code><i>width</i></p>
<dd>
<dt><code>-height=</code><i>height</i></p>
<dd>
<dt><code>-xrightpos=</code><i>column</i></p>
<dd>
<dt><code>-yrightpos=</code><i>row</i></p>
<dd> These are constraints on where <code>pnmstitch</code> stitches the images together. For the <code>LinearSliver</code> method, <i>column</i> and <i>row</i> tell what location in the right hand image matches up to the top right corner of the left hand image.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-stitcher=</code>{<code>RotateSliver</code>,<code>BiLinearSliver</code>,</p>
<dd> <code>LinearSliver</code>} The default is <code>RotateSliver</code>. </p>
<dt><code>-filter=</code>{<code>LineAtATime</code>,<code>HorizontalCrop</code>}</p>
<dd> No details available.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-output=</code><i>output_filespec</i></p>
<dd> Name of output file. If you don&#8217;t specify this option, the output image goes to Standard Output. </p>
<dt><code>-verbose</code></p>
<dd> This option causes <code>pnmstitch</code> to issue messages to Standard Error about the stitching process.<br />
&nbsp;<wbr>&nbsp;<wbr> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamcut/">pamcut</a></code>(1) , <code><a href="/docs/linux/man/1-pnmcat/">pnmcat</a></code>(1) , <code><a href="/docs/linux/man/1-pamflip/">pamflip</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> This program was added to Netpbm in Release 10.7 (August 2002). </p>
<h2>Index</h2>
