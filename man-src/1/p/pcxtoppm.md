---
title: "pcxtoppm(1)"
name: "pcxtoppm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcxtoppm/"
description: "pcxtoppm – convert a PCX file into a portable pixmap"
---

<h2 class="name">NAME</h2>
<p> pcxtoppm &#8211; convert a PCX file into a portable pixmap</p>
<h2>SYNOPSIS</h2>
<p> <code>pcxtoppm</code> [<code>-stdpalette</code>] [<code>-verbose</code>] [<i>pcxfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads a PCX file as input. Produces a portable pixmap as output. Supported PCX types are:</p>
<dl>
<dt>Colormapped files with 2-16 colors.</p>
<dd> &quot;Packed pixel&quot; format (1, 2 or 4 bits/pixel, 1 plane) or bitplane format (1 bit/pixel, 1-4 planes). The program checks the colormap and uses an internal one if the provided colormap is completely black.</p>
<dt>Colormapped files with 256 colors</p>
<dd> 8 bits/pixel, 1 plane, colormap at the end of the file.</p>
<dt>24bit truecolor files</p>
<dd> 24bit RGB: 8 bits/pixel, 3 planes.</p>
<dt>32bit truecolor files</p>
<dd> 24bit RGB + 8bit intensity: 8 bits/pixel, 4 planes. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-stdpalette</code></p>
<dd> Enforce the use of the internal colormap for files with 16 colors or less. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmtopcx/">ppmtopcx</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHORS</h2>
<p> Copyright (C) 1990 by Michael Davidson.<br />
 Modified 1994 by Ingo Wilken (Ingo.Wilken [at] informatik.uni-oldenburg.de) </p>
<h2>Index</h2>
