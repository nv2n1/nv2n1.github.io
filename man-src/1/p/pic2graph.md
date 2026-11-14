---
title: "pic2graph(1)"
name: "pic2graph"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pic2graph/"
description: "pic2graph – convert a PIC diagram into a cropped image"
---

<h2 class="name">NAME</h2>
<p> pic2graph &#8211; convert a PIC diagram into a cropped image </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-unsafe</code> ] [ <code>-format </code><i>output-format</i> ] [ <code>-eqn </code><i>delimiters</i> ] [<i>convert-arguments</i>] <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <i>pic2graph</i> reads a <i><a href="/docs/linux/man/1-pic/">pic</a></i>(1) program from the standard input and writes an image file, by default in Portable Network Graphics (PNG) format, to the standard output. It furthermore translates <i><a href="/docs/linux/man/1-eqn/">eqn</a></i>(1) constructs, so it can be used for generating images of mathematical formulae. </p>
<p> The input PIC code should <i>not</i> be wrapped with the <code>.PS</code> and <code>.PE</code> macros that normally guard it within <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1) documents. </p>
<p> Arguments not recognized by <i>pic2graph</i> are passed to the ImageMagick or GraphicsMagick program <i><a href="/docs/linux/man/1-convert/">convert</a></i>(1). By specifying these, you can give your image a border, set the image&#8217;s pixel density, or perform other useful transformations. </p>
<p> The output image is clipped using <i>convert</i>&#8216;s <code>-trim</code> option to the smallest possible bounding box that contains all the black pixels.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-eqn </code><i>delimiters</i></p>
<dd> Use <i>delimiters</i> as the opening and closing characters that delimit <i>eqn</i> directives; the default is &#8220;$$&#8221;. The option argument <i>delimiters</i> should be a two-character string, but an empty string (&quot;&quot;) is accepted as a directive to disable <i>eqn</i> processing.</p>
<dt><code>-format </code><i>output-format</i></p>
<dd> Write the image in <i>output-format</i>, which must be understood by <i>convert</i>; the default is PNG.</p>
<dt><code>&#8211;help</code></p>
<dd> Display a usage message and exit.</p>
<dt><code>-unsafe</code></p>
<dd> Run <i>groff</i> in <i>unsafe</i> mode, enabling the PIC command <code>sh</code> to execute arbitrary Unix shell commands. The <i>groff</i> default is to forbid this.</p>
<dt><code>-v</code></p>
<dd> <code>&#8211;version</code> Display version information and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>GROFF_TMPDIR</i></p>
<dd> <i>TMPDIR</i> <i>TMP</i> <i>TEMP</i> These environment variables are searched in the given order to determine the directory where temporary files will be created. If none are set, <i>/tmp</i> is used.</dl>
<h2>AUTHORS</h2>
<p> <i>pic2graph</i> was written by Eric S. Raymond based on a recipe by W. Richard Stevens.</p>
<h2>SEE ALSO</h2>
<p> W. Richard Stevens, <i>Turning PIC into HTML</i> </p>
<p> <i><a href="/docs/linux/man/1-eqn2graph/">eqn2graph</a></i>(1), <i><a href="/docs/linux/man/1-grap2graph/">grap2graph</a></i>(1), <i><a href="/docs/linux/man/1-pic/">pic</a></i>(1), <i><a href="/docs/linux/man/1-eqn/">eqn</a></i>(1), <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1), <i><a href="/docs/linux/man/1-convert/">convert</a></i>(1) </p>
<h2>Index</h2>
