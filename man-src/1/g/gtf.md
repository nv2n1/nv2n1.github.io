---
title: "gtf(1)"
name: "gtf"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtf/"
description: "gtf – calculate VESA GTF mode lines"
---

<h2 class="name">NAME</h2>
<p> gtf &#8211; calculate VESA GTF mode lines </p>
<h2>SYNOPSIS</h2>
<p> <code>gtf</code> <i>h-resolution</i> <i>v-resolution</i> <i>refresh</i> [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-f</code>|<code>&#8211;fbmode</code>] [<code>-x</code>|<code>&#8211;xorgmode</code>]</p>
<h2>DESCRIPTION</h2>
<p> <i>Gtf</i> is a utility for calculating VESA GTF modes. Given the desired horizontal and vertical resolutions and refresh rate (in Hz), the parameters for a matching VESA GTF mode are printed out. Two output formats are supported: mode lines suitable for the Xorg <code><a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5)</code> file, and mode parameters suitable for the Linux <code><a href="/docs/linux/man/8-fbset/">fbset</a>(8)</code> utility. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code>|<code>&#8211;verbose</code></p>
<dd> Enable verbose printouts This shows a trace for each step of the computation.</p>
<dt><code>-x</code>|<code>&#8211;xorgmode</code></p>
<dd> Print the mode parameters as Xorg-style mode lines. This is the default format.</p>
<dt><code>-f</code>|<code>&#8211;fbset</code></p>
<dd> Print the mode parameters in a format suitable for <code><a href="/docs/linux/man/8-fbset/">fbset</a>(8)</code>.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-cvt/">cvt</a>(1)</p>
<h2>AUTHOR</h2>
<p> Andy Ritger. </p>
<p> This program is based on the Generalized Timing Formula (GTF(TM)) Standard Version: 1.0, Revision: 1.0. The GTF Excel(TM) spreadsheet, a sample (and the definitive) implementation of the GTF Timing Standard is available at &lt;<a href="ftp://ftp.vesa.org/pub/GTF/VTF_V1R1.xls">ftp://ftp.vesa.org/pub/GTF/VTF_V1R1.xls</a>&gt;. </p>
<h2>Index</h2>
