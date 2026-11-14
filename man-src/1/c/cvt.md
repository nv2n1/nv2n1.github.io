---
title: "cvt(1)"
name: "cvt"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cvt/"
description: "cvt – calculate VESA CVT mode lines"
---

<h2 class="name">NAME</h2>
<p> cvt &#8211; calculate VESA CVT mode lines </p>
<h2>SYNOPSIS</h2>
<p> <code>cvt</code> [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-r</code>|<code>&#8211;reduced</code>] <i>h-resolution</i> <i>v-resolution</i> [<code>refresh</code>]</p>
<h2>DESCRIPTION</h2>
<p> <i>Cvt</i> is a utility for calculating VESA Coordinated Video Timing modes. Given the desired horizontal and vertical resolutions, a modeline adhering to the CVT standard is printed. This modeline can be included in Xorg <code><a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5)</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>refresh</code></p>
<dd> Provide a vertical refresh rate in Hz. The CVT standard prefers either 50.0, 60.0, 75.0 or 85.0Hz. The default is 60.0Hz.</p>
<dt><code>-v</code>|<code>&#8211;verbose</code></p>
<dd> Warn verbosely when a given mode does not completely correspond with CVT standards.</p>
<dt><code>-r</code>|<code>&#8211;reduced</code></p>
<dd> Create a mode with reduced blanking. This allows for higher frequency signals, with a lower or equal dotclock. Not for Cathode Ray Tube based displays though. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-gtf/">gtf</a>(1)</p>
<h2>AUTHOR</h2>
<p> Luc Verhaegen. </p>
<p> This program is based on the Coordinated Video Timing sample implementation written by Graham Loveridge. This file is publicly available at &lt;<a rel="nofollow" href="http://www.vesa.org/Public/CVT/CVTd6r1.xls">http://www.vesa.org/Public/CVT/CVTd6r1.xls</a>&gt;. CVT is a VESA trademark. </p>
<h2>Index</h2>
