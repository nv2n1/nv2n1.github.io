---
title: "pamtompfont(1)"
name: "pamtompfont"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtompfont/"
description: "pamtompfont – Convert Netpbm image to Mplayer bitmap font file"
---

<h2>NAME</h2>
<p> pamtompfont &#8211; Convert Netpbm image to Mplayer bitmap font file </p>
<h2>SYNOPSIS</h2>
<p> <code>pamtompfont</code> [<i>imagefile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtompfont</code> reads a Netpbm image (PNM or PAM) and converts it to an Mplayer bitmap font raster file. </p>
<p> This is the original font format used by Mplayer (for subtitles, on-screen messages, etc.), before it had the ability to use Freetype to access standard fonts. </p>
<p> The format was apparently an image format before Mplayer adopted it for fonts, but I have no idea where it came from or where else it might be used. </p>
<p> An Mplayer bitmap font consists of a font descriptor file and raster files. The font descriptor file identifies the raster files by file name. A raster file contains a single rectangular raster image which contains an arrangement of a bunch of glyphs. Each glyph is a rectangular image and the font descriptor indicates where in the image the glyph for each codepoint is. Every glyph in the font has the same height, so the font descriptor just indicates the file position in the raster file of the to left corner of the glyph, and the width of the glyph in pixels. </p>
<h2>OPTIONS</h2>
<p> None. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamtompfont</code> was added to Netpbm in Release 10.43 (June 2008). </p>
<h2>Index</h2>
