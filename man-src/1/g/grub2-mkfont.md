---
title: "grub2-mkfont(1)"
name: "grub2-mkfont"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub2-mkfont/"
description: "grub-mkfont — Convert common font file formats into the PF2 format."
---

<h2>NAME</h2>
<p> <code>grub-mkfont</code> &#8212; Convert common font file formats into the PF2 format. </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-mkfont</code> [&#8211;ascii-bitmaps] [-a | &#8211;force-autohint]</p>
<dl>
<dt>
<dd> [-b | &#8211;bold] [-c | &#8211;asce=<i>NUM</i>] [-d | &#8211;desc=<i>NUM</i>]</dl>
<dl>
<dt>
<dd> [-i | &#8211;index=<i>NUM</i>] [-n | &#8211;name=<i>NAME</i>] [&#8211;no-bitmap]</dl>
<dl>
<dt>
<dd> [&#8211;no-hinting] &lt;-o | &#8211;output=<i>FILE</i>&gt;</dl>
<dl>
<dt>
<dd> [-r | &#8211;range=<i>FROM-TO</i>[<i>,FROM-TO</i>]] [-s | &#8211;size=<i>SIZE</i>]</dl>
<dl>
<dt>
<dd> [-v | &#8211;verbose] [&#8211;width-spec] <i>FONT_FILES</i> </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>grub-mkfont</code> converts font files from common formats into the PF2 format used by GRUB. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;ascii-bitmaps</p>
<dd> Save only bitmaps for ASCII characters. </p>
<dt>&#8211;force-autohint</p>
<dd> Force generation of automatic hinting. </p>
<dt>&#8211;bold</p>
<dd> Convert font to bold. </p>
<dt>&#8211;asce=<i>NUM</i></p>
<dd> Set font ascent to <i>NUM</i>. </p>
<dt>&#8211;desc=<i>NUM</i></p>
<dd> Set font descent to <i>NUM</i>. </p>
<dt>&#8211;index=<i>NUM</i></p>
<dd> Select face index <i>NUM</i>. </p>
<dt>&#8211;name=<i>NAME</i></p>
<dd> Set font family to <i>NAME</i>. </p>
<dt>&#8211;no-bitmap</p>
<dd> Ignore bitmap strikes when loading. </p>
<dt>&#8211;no-hinting</p>
<dd> Disable hinting. </p>
<dt>&#8211;output=<i>FILE</i></p>
<dd> Save ouptut to <i>FILE</i>. This argument is required. </p>
<dt>&#8211;range=<i>FROM-TO</i><i>,FROM-TO</i></p>
<dd> Set the font ranges to each pair of <i>FROM</i>,<i>TO</i>. </p>
<dt>&#8211;size=<i>SIZE</i></p>
<dd> Set font size to <i>SIZE</i>. </p>
<dt>&#8211;verbose</p>
<dd> Print verbose messages. </p>
<dt>&#8211;width-spec</p>
<dd> Create a width summary file. </p>
<dt><i>FONT_FILES</i></p>
<dd> The input files to be converted. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
<h2>Index</h2>
