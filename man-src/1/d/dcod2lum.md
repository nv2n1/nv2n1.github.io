---
title: "dcod2lum(1)"
name: "dcod2lum"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcod2lum/"
description: "dcod2lum – Convert hardcopy characteristic curve file to softcopy format"
---

<h2 class="name">NAME</h2>
<p> dcod2lum &#8211; Convert hardcopy characteristic curve file to softcopy format </p>
<h2>SYNOPSIS</h2>
<pre>
dcod2lum in-file out-file
</pre>
<h2>DESCRIPTION</h2>
<p> Command line program that converts a hardcopy characteristic curve file to softcopy format. In other words, the measured optical density (OD) values from the input file are transformed to the luminance space according to the formula: </p>
<pre>
  L = La + L0 * 10^(-D)
</pre>
<p> where <i>L</i> is the resulting luminance, <i>La</i> is the reflected ambient light and <i>L0</i> the illumination (both measured in cd/m^2), &#8216;D&#8217; the optical density (OD). Please note that if no illumination value is specified in the input file (keyword <i>lum</i>) all optical density values are mapped to a constant luminance.</p>
<h2>PARAMETERS</h2>
<pre>
in-file   hardcopy characteristic curve file to be converted
out-file  softcopy characteristic curve file to be written
</pre>
<h2>NOTES</h2>
<p> The format of both input and ouput file is described the documentation of the <code>dcmdspfn</code> command line tool. In addition, the <i>data</i> folder contains sample characteristics file monitors, cameras, printers and scanners.</p>
<h2>FILES</h2>
<p> <i>&lt;datadir&gt;/camera.lut</i> &#8211; sample characteristics file of a camera<br />
 <i>&lt;datadir&gt;/monitor.lut</i> &#8211; sample characteristics file of a monitor<br />
 <i>&lt;datadir&gt;/printer.lut</i> &#8211; sample characteristics file of a printer<br />
 <i>&lt;datadir&gt;/scanner.lut</i> &#8211; sample characteristics file of a scanner</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmdspfn/">dcmdspfn</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
