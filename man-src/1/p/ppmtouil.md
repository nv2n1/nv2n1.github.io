---
title: "ppmtouil(1)"
name: "ppmtouil"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtouil/"
description: "ppmtouil – convert a portable pixmap into a Motif UIL icon file"
---

<h2 class="name">NAME</h2>
<p> ppmtouil &#8211; convert a portable pixmap into a Motif UIL icon file </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtouil</code> [<code>-name</code> <i>uilname</i>] [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces a Motif UIL icon file as output. </p>
<p> If the program was compiled with an rgb database specified, and a RGB value from the ppm input matches a RGB value from the database, then the corresponding color name mnemonic is printed in the UIL&#8217;s colormap. If no rgb database was compiled in, or if the RGB values don&#8217;t match, then the color will be printed with the #RGB, #RRGGBB, #RRRGGGBBB, or #RRRRGGGGBBBB hexadecimal format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-name</code></p>
<dd> Allows you to specify the prefix string which is printed in the resulting UIL output. If not specified, will default to the filename (without extension) of the ppmfile argument. If <code>-name</code> is not specified and no ppmfile is specified (i.e. piped input), the prefix string will default to the string &quot;noname&quot;.</dl>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-ppm/">ppm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Converted by Jef Poskanzer from ppmtoxpm.c, which is Copyright (C) 1990 by Mark W. Snitily </p>
<h2>Index</h2>
