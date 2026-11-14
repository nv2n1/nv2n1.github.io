---
title: "pbmtextps(1)"
name: "pbmtextps"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtextps/"
description: "pbmtextps – render text into a bitmap via postscript"
---

<h2 class="name">NAME</h2>
<p> pbmtextps &#8211; render text into a bitmap via postscript </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtextps</code> [<code>-font</code> <i>fontfile</i>] [<code>-fontsize</code> <i>fontsize</i>] [<code>-resolution</code> <i>resolution</i>] [<code>-stroke</code> <i>strokesize</i>] [<code>-verbose</code> [<i>text</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>pbmtextps</code> takes a single line of text from the command line and renders it into a PBM image. </p>
<p> The image is cropped at the top and the right. It is not cropped at the left or bottom so that the text begins at the same position relative to the origin. You can use <code>pnmcrop</code> to crop it all the way. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-font</code></p>
<dd> By default, <code>pbmtextps</code> uses TimesRoman. You can specify the font to use with the <code>-font</code> option. This is the name of any valid postscript font which is installed on your system. </p>
<dt><code>-fontsize</code></p>
<dd> Size of font in points. See the <code>-resolution</code> option for information on how to interpret this size. </p>
<p> Default is 24 points. </p>
<dt><code>-resolution</code></p>
<dd> Resolution in dots per inch of distance measurements pertaining to generation of the image. PBM images don&#8217;t have any inherent resolution, so a distance such as &quot;1 inch&quot; doesn&#8217;t mean anything unless you separately specify what resolution you&#8217;re talking about. That&#8217;s what this option does. </p>
<p> In particular, the meaning of the font size is determined by this resolution. If the font size is 24 points and the resolution is 150 dpi, then the font size is 50 pixels. </p>
<p> Default is 150 dpi. </p>
<dt><code>-stroke</code></p>
<dd> Width of line to use for stroke font. There is no default stroke width because the letters are solid by default.<br />
&nbsp; </p>
</dl>
<h2>USAGE</h2>
<p> See <code>pbmtext</code> for usage examples. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmtext/">pbmtext</a></code>(1), <code><a href="/docs/linux/man/1-pnmcut/">pnmcut</a></code>(1), <code><a href="/docs/linux/man/1-pnmcrop/">pnmcrop</a></code>(1), <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1), <code><a href="/docs/linux/man/1-ppmchange/">ppmchange</a></code>(1), <code><a href="/docs/linux/man/1-pnmrotate/">pnmrotate</a></code>(1), <code><a href="/docs/linux/man/1-ppmlabel/">ppmlabel</a></code>(1), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2002 by James McCann </p>
<h2>Index</h2>
