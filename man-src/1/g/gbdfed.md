---
title: "gbdfed(1)"
name: "gbdfed"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gbdfed/"
description: "gbdfed – GTK-based BDF font editor"
---

<h2>NAME</h2>
<p> gbdfed &#8211; GTK-based BDF font editor </p>
<h2>SYNOPSIS</h2>
<p> <code>gbdfed</code> [<i>options</i>] [<i>fonts &#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> <i>gbdfed</i> lets you interactively create new bitmap font files or modify existing ones. It allows editing multiple fonts and multiple glyphs, it allows cut and paste operations between fonts and glyphs and editing font properties. <i>gbdfed</i> can import Metafont PK/GF fonts, Han Bitmap Font Format (HBF) fonts, Linux console fonts (PSF, CP, and EGA/VGA) fonts, Sun VF fonts, OpenType/TrueType (OTF/TTF) fonts, or grab a font from the X server (when running under X11). <i>gbdfed</i> can export PSF2 Linux console fonts and HEX fonts (see online help). </p>
<p> <i>gbdfed</i> works on X Window System Version 11 (X11), Release 5 or 6, with GTK+ 2.6 or greater. It may work on Windows, but hasn&#8217;t been tested yet. </p>
<h2>OPTIONS</h2>
<p> <i>gbdfed</i> accepts the following command line arguments: </p>
<dl>
<dt><i>-nc</i></p>
<dd> do not preserve comments (by default, <i>gbdfed</i> automatically collects comments that are saved with the font).</dl>
<dl>
<dt><i>-nu</i></p>
<dd> do not preserve unencoded glyphs (by default, <i>gbdfed</i> preserves the unencoded glyphs).</dl>
<dl>
<dt><i>-nm</i></p>
<dd> do not make metrics corrections (by default, <i>gbdfed</i> attempts to make metrics corrections automatically).</dl>
<dl>
<dt><i>-np</i></p>
<dd> do not pad character-cell bitmaps (by default, <i>gbdfed</i> pads character-cell bitmaps with 0&#8217;s to the cell dimensions when the font is saved).</dl>
<dl>
<dt><i>-bp</i></p>
<dd> allow blank pages (by default, <i>gbdfed</i> skips blank pages).</dl>
<dl>
<dt><i>-ed</i></p>
<dd> do not present the &quot;Really Exit?&quot; dialog (by default, this dialog always presented).</dl>
<dl>
<dt><i>-ps n</i></p>
<dd> set default point size (if unspecified, <i>gbdfed</i> sets it to 12).</dl>
<dl>
<dt><i>-hres n</i></p>
<dd> set default horizontal resolution.</dl>
<dl>
<dt><i>-vres n</i></p>
<dd> set default vertical resolution.</dl>
<dl>
<dt><i>-res n</i></p>
<dd> set both default resolutions (if unspecified, <i>gbdfed</i> sets both horizontal and vertical resolution to that of display, (e.g. 90&#215;90 dpi for Sun workstations).</dl>
<dl>
<dt><i>-sp s</i></p>
<dd> set the default font spacing (&quot;p&quot; for Proportional, &quot;m&quot; for Monowidth, or &quot;c&quot; for Character Cell).</dl>
<dl>
<dt><i>-eol e</i></p>
<dd> set the default end-of-line type (&quot;u&quot; for Unix LF, &quot;d&quot; for DOS/Windows CRLF, or &quot;m&quot; for Macintosh CR). CR)</dl>
<dl>
<dt><i>-g glyph-code</i></p>
<dd> specify the initial glyph code at startup. The glyph code can be specified in decimal, octal, or hex. Octal numbers must be prefixed with the digit 0, and hex numbers must be prefixed with one of: <i>0x, 0X, U+, U-, 
