---
title: "fonttosfnt(1)"
name: "fonttosfnt"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fonttosfnt/"
description: "fonttosfnt – Wrap a bitmap font in a sfnt (TrueType) wrapper"
---

<h2 class="name">NAME</h2>
<p> fonttosfnt &#8211; Wrap a bitmap font in a sfnt (TrueType) wrapper </p>
<h2>SYNOPSIS</h2>
<p> <code>fonttosfnt</code> [ <i>options</i> ] <code>-o</code> <i>file.ttf</i> [ <code>&#8212;</code> ] <i>font</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Wrap a bitmap font or a set of bitmap fonts in a sfnt (TrueType or OpenType) wrapper.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></dt>
<dd> Be verbose.</dd>
<dt><code>-c</code></dt>
<dd> Do not crop glyphs. This usually increases file size, but may sometimes yield a modest decrease in file size for small character cell fonts (terminal fonts).</dd>
<dt><code>-b</code></dt>
<dd> Write byte-aligned glyph data. By default, unaligned data is written, which yields a smaller file size.</dd>
<dt><code>-r</code></dt>
<dd> Do not reencode fonts. By default, fonts are reencoded to Unicode whenever possible.</dd>
<dt><code>-g</code><i> n</i></dt>
<dd> Set the type of scalable glyphs that we write. If <i>n</i> is 0, no scalable glyphs are written; this is legal but confuses most current software. If <i>n</i> is 1, a single scalable glyph (the undefined glyph) is written; this is recommended, but triggers a bug in current versions of <code>FreeType</code>. If <i>n</i> is 2 (the default), a sufficiently high number of blank glyphs are written, which works with <code>FreeType</code> but increases file size.</dd>
<dt><code>-m</code><i> n</i></dt>
<dd> Set the type of scalable metrics that we write. If <i>n</i> is 0, no scalable metrics are written, which may or may not be legal. If <i>n</i> is 1, full metrics for a single glyph are written, and only left sidebearing values are written for the other glyphs. If <i>n</i> is 2, scalable metrics for all glyphs are written, which increases file size and is not recommended. The default is 1.</dd>
<dt><code>&#8212;</code></dt>
<dd> End of options.</dd></dl>
<h2>BUGS</h2>
<p> Some of the font-level values, notably sub- and superscript positions, are dummy values.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), Xft(3x). <i>Fonts in X11.</i></p>
<h2>AUTHOR</h2>
<p> The version of <code>Fonttosfnt</code> included in this X.Org Foundation release was originally written by Juliusz Chroboczek &lt;jch [at] freedesktop.org&gt; for the XFree86 project. </p>
