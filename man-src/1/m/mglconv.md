---
title: "mglconv(1)"
name: "mglconv"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mglconv/"
description: "mglconv – Execute MathGL scripts to generate graphical output."
---

<h2>NAME</h2>
<p> mglconv &#8211; Execute MathGL scripts to generate graphical output.</p>
<h2>SYNOPSIS</h2>
<p> <code>mglconv</code> [parameters] scriptfile</p>
<h2>DESCRIPTION</h2>
<p> <code>mglconv</code> reads MGL scripts from <i>scriptfile</i> to produce plots of specified functions or data. Result can be saved in bitmap (PNG/JPEG/GIF/BMP) or vector (EPS/SVG/LaTeX/OFF/STL/OBJ/X3D) format. You can use <code>&#8211;</code> as file name for reading script from standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1 string</code></dt>
<dd> Set <i>string</i> as argument $1 for script.</dd>
<dt><code>&#8230;</code></dt>
<dd>
</dd><dt><code>-9 string</code></dt>
<dd> Set <i>string</i> as argument $9 for script.</dd>
<dt><code>-A value</code></dt>
<dd> Add <i>value</i> into the list of animation parameters.</dd>
<dt><code>-C v1:v2[:dv]</code></dt>
<dd> Add values in range <i>v1:v2</i> with step <i>dv</i> (default is 1) into the list of animation parameters.</dd>
<dt><code>-L locname</code></dt>
<dd> Set the locale to <i>locname.</i></dd>
<dt><code>-o name</code></dt>
<dd> Set output file name.</dd>
<dt><code>-h</code></dt>
<dd> Print help message.</dd></dl>
<h2>AUTHOR</h2>
<p> mglconv was written by Alexey Balakin, <a rel="nofollow" href="http://mathgl.sourceforge.net/">http://mathgl.sourceforge.net/</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mglview/">mglview</a></code>(1), <code><a href="/docs/linux/man/5-mgl/">mgl</a></code>(5) </p>
<h2>Index</h2>
