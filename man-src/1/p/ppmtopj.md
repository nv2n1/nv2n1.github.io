---
title: "ppmtopj(1)"
name: "ppmtopj"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtopj/"
description: "ppmtopj – convert a portable pixmap to an HP PaintJet file"
---

<h2 class="name">NAME</h2>
<p> ppmtopj &#8211; convert a portable pixmap to an HP PaintJet file </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtopj</code> [-gamma <i>val</i>] [<code>-xpos</code> <i>val</i>] [<code>-ypos</code> <i>val</i>] [<code>-back</code> <code>dark</code>|<code>lite</code>] [<code>-rle</code>] [<code>-center</code>] [<code>-render</code> <code>none|snap|bw|dither|diffuse|monodither|monodiffuse|clusterdither|monoclusterdither</code>] [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input and converts it into a format suitable to be printed by an HP PaintJet printer. </p>
<p> For best results, the input file should be in 8-color RGB form; i.e. it should have only the 8 binary combinations of full-on and full-off primaries. You could get this by sending the input file through <i>ppmquant -map</i> with a map file such as: </p>
<pre>
    P3
    8 1
    255
    0 0 0      255 0 0    0 255 0    0 0 255
    255 255 0  255 0 255  0 255 255  255 255 255
</pre>
<p> Or else you could use use <i>ppmdither -red 2 -green 2 -blue 2.</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-rle</code></p>
<dd> Run length encode the image. (This can result in larger images)</p>
<dt><code>-back</code></p>
<dd> Enhance the foreground by indicating if the background is light or dark compated to the foreground.</p>
<dt><code>-render</code><i> alg</i></p>
<dd> Use an internal rendering algorithm (default dither).</p>
<dt><code>-gamma</code><i> int</i></p>
<dd> Gamma correct the image using the integet parameter as a gamma (default 0).</p>
<dt><code>-center</code></p>
<dd> Center the image to an 8.5 by 11 page</p>
<dt><code>-xpos</code><i> pos</i></p>
<dd> Move by pos pixels in the x direction.</p>
<dt><code>-ypos</code><i> pos</i></p>
<dd> Move by pos pixels in the y direction.</dl>
<h2>REFERENCES</h2>
<p> HP PaintJet XL Color Graphics Printer User&#8217;s Guide</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmdepth/">pnmdepth</a>(1), <a href="/docs/linux/man/1-ppmquant/">ppmquant</a>(1), <a href="/docs/linux/man/1-ppmdither/">ppmdither</a>(1), <a href="/docs/linux/man/5-ppm/">ppm</a>(5)</p>
<h2>BUGS</h2>
<p> Most of the options have not been tested because of the price of the paper.</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Christos Zoulas. </p>
<h2>Index</h2>
