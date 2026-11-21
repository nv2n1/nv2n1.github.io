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
</dt><dd> [-b | &#8211;bold] [-c | &#8211;asce=<i>NUM</i>] [-d | &#8211;desc=<i>NUM</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [-i | &#8211;index=<i>NUM</i>] [-n | &#8211;name=<i>NAME</i>] [&#8211;no-bitmap]</dd></dl>
<dl>
<dt>
</dt><dd> [&#8211;no-hinting] &lt;-o | &#8211;output=<i>FILE</i>&gt;</dd></dl>
<dl>
<dt>
</dt><dd> [-r | &#8211;range=<i>FROM-TO</i>[<i>,FROM-TO</i>]] [-s | &#8211;size=<i>SIZE</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [-v | &#8211;verbose] [&#8211;width-spec] <i>FONT_FILES</i> </dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>grub-mkfont</code> converts font files from common formats into the PF2 format used by GRUB. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;ascii-bitmaps</dt>
<dd> Save only bitmaps for ASCII characters. </dd>
<dt>&#8211;force-autohint</dt>
<dd> Force generation of automatic hinting. </dd>
<dt>&#8211;bold</dt>
<dd> Convert font to bold. </dd>
<dt>&#8211;asce=<i>NUM</i></dt>
<dd> Set font ascent to <i>NUM</i>. </dd>
<dt>&#8211;desc=<i>NUM</i></dt>
<dd> Set font descent to <i>NUM</i>. </dd>
<dt>&#8211;index=<i>NUM</i></dt>
<dd> Select face index <i>NUM</i>. </dd>
<dt>&#8211;name=<i>NAME</i></dt>
<dd> Set font family to <i>NAME</i>. </dd>
<dt>&#8211;no-bitmap</dt>
<dd> Ignore bitmap strikes when loading. </dd>
<dt>&#8211;no-hinting</dt>
<dd> Disable hinting. </dd>
<dt>&#8211;output=<i>FILE</i></dt>
<dd> Save ouptut to <i>FILE</i>. This argument is required. </dd>
<dt>&#8211;range=<i>FROM-TO</i><i>,FROM-TO</i></dt>
<dd> Set the font ranges to each pair of <i>FROM</i>,<i>TO</i>. </dd>
<dt>&#8211;size=<i>SIZE</i></dt>
<dd> Set font size to <i>SIZE</i>. </dd>
<dt>&#8211;verbose</dt>
<dd> Print verbose messages. </dd>
<dt>&#8211;width-spec</dt>
<dd> Create a width summary file. </dd>
<dt><i>FONT_FILES</i></dt>
<dd> The input files to be converted. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
