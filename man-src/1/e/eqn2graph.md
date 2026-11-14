---
title: "eqn2graph(1)"
name: "eqn2graph"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eqn2graph/"
description: "eqn2graph – convert an EQN equation into a cropped image"
---

<h2 class="name">NAME</h2>
<p> eqn2graph &#8211; convert an EQN equation into a cropped image </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-format </code><i>output-format</i> ] [<i>convert-arguments</i>] <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <i>eqn2graph</i> reads a one-line <i><a href="/docs/linux/man/1-eqn/">eqn</a></i>(1) equation from the standard input and writes an image file, by default in Portable Network Graphics (PNG) format, to the standard output. </p>
<p> The input EQN code should <i>not</i> be preceded by the <code>.EQ</code> macro that normally precedes it within <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1) macros; nor do you need to have dollar-sign or other delimiters around the equation. </p>
<p> Arguments not recognized by <i>eqn2graph</i> are passed to the ImageMagick or GraphicsMagick program <i><a href="/docs/linux/man/1-convert/">convert</a></i>(1). By specifying these, you can give your image a border, set the image&#8217;s pixel density, or perform other useful transformations. </p>
<p> The output image is clipped using <i>convert</i>&#8216;s <code>-trim</code> option to the smallest possible bounding box that contains all the black pixels.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-format </code><i>output-format</i></p>
<dd> Write the image in <i>output-format</i>, which must be understood by <i>convert</i>; the default is PNG.</p>
<dt><code>&#8211;help</code></p>
<dd> Display a usage message and exit.</p>
<dt><code>-v</code></p>
<dd> <code>&#8211;version</code> Display version information and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>GROFF_TMPDIR</i></p>
<dd> <i>TMPDIR</i> <i>TMP</i> <i>TEMP</i> These environment variables are searched in the given order to determine the directory where temporary files will be created. If none are set, <i>/tmp</i> is used.</dl>
<h2>AUTHORS</h2>
<p> <i>eqn2graph</i> was written by Eric S. Raymond based on a recipe for <i><a href="/docs/linux/man/1-pic2graph/">pic2graph</a></i>(1), by W. Richard Stevens.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pic2graph/">pic2graph</a></i>(1), <i><a href="/docs/linux/man/1-grap2graph/">grap2graph</a></i>(1), <i><a href="/docs/linux/man/1-eqn/">eqn</a></i>(1), <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1), <i><a href="/docs/linux/man/1-convert/">convert</a></i>(1) </p>
<h2>Index</h2>
