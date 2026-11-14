---
title: "ppmpat(1)"
name: "ppmpat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmpat/"
description: "ppmpat – make a pretty pixmap"
---

<h2 class="name">NAME</h2>
<p> ppmpat &#8211; make a pretty pixmap </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmpat</code> <code>-gingham2</code>|<code>-g2</code>|<code>-gingham3</code>| <code>-g3</code>|<code>-madras</code>|<code>-tartan</code>| <code>-poles</code>|<code>-squig</code>|<code>-camo</code>| <code>-anticamo</code> <i>width height</i></p>
<h2>DESCRIPTION</h2>
<p> Produces a portable pixmap of the specified width and height, with a pattern in it. </p>
<p> This program is mainly to demonstrate use of the ppmdraw routines, a simple but powerful drawing library. See the ppmdraw.h include file for more info on using these routines. Still, some of the patterns can be rather pretty. If you have a color workstation, something like <code>ppmpat -squig 300 300 | ppmquant 128</code> should generate a nice background.</p>
<h2>OPTIONS</h2>
<p> The different flags specify various different pattern types:</p>
<dl>
<dt><code>-gingham2</code></p>
<dd> A gingham check pattern. Can be tiled.</p>
<dt><code>-gingham3</code></p>
<dd> A slightly more complicated gingham. Can be tiled.</p>
<dt><code>-madras</code></p>
<dd> A madras plaid. Can be tiled.</p>
<dt><code>-tartan</code></p>
<dd> A tartan plaid. Can be tiled.</p>
<dt><code>-poles</code></p>
<dd> Color gradients centered on randomly-placed poles. May need to be run through <i>ppmquant</i>.</p>
<dt><code>-squig</code></p>
<dd> Squiggley tubular pattern. Can be tiled. May need to be run through <i>ppmquant</i>.</p>
<dt><code>-camo</code></p>
<dd> Camouflage pattern. May need to be run through <i>ppmquant</i>.</p>
<dt><code>-anticamo</code></p>
<dd> Anti-camouflage pattern &#8211; like -camo, but ultra-bright colors. May need to be run through <i>ppmquant</i>.</dl>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>REFERENCES</h2>
<p> Some of the patterns are from &quot;Designer&#8217;s Guide to Color 3&quot; by Jeanne Allen.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmtile/">pnmtile</a>(1), <a href="/docs/linux/man/1-ppmquant/">ppmquant</a>(1), <a href="/docs/linux/man/5-ppm/">ppm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
