---
title: "dconvlum(1)"
name: "dconvlum"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dconvlum/"
description: "dconvlum – Convert VeriLUM files to DCMTK display files"
---

<h2 class="name">NAME</h2>
<p> dconvlum &#8211; Convert VeriLUM files to DCMTK display files </p>
<h2>SYNOPSIS</h2>
<pre>
dconvlum in-file out-file [ambient]
</pre>
<h2>DESCRIPTION</h2>
<p> Command line program that converts VeriLUM file with characteristic curve data (<i>CCx_xx.dat</i>) to a format used for the Barten transformation in this toolkit. VeriLUM is a calibration package from ImageSmiths consisting of a photometer (with serial RS232 connector) and a Windows NT software.</p>
<h2>PARAMETERS</h2>
<pre>
in-file   VeriLUM characteristic curve file to be converted
out-file  DCMTK display file to be written
ambient   ambient light (cd/m^2, floating point value)
</pre>
<h2>NOTES</h2>
<p> The output file describing the characteristic curve of a display system (monitor) is a simple text file. Lines starting with a &#8216;#&#8217; are treated as comments and therefore skipped as well as blank lines. This conversion program creates such a file automatically (including some comment lines) by transforming the information stored in the VeriLUM file. The number following the magic word &#8216;max&#8217; defines the maximum DDL value (e.g. 255 for 8 bit displays). This definition is required before the luminance data can be defined. Optionally the ambient light value can be specified in this file too. The floating point value (in candela per square meter) must follow the word &#8216;amb&#8217;. Finally the luminance values are defined for each corresponding DDL (device driving level) value. The entries do not necessarily have to be ordered or complete, i.e. there can be less than &#8216;max&#8217; + 1 entries. Missing values are calculated by cubic spline interpolation. </p>
<p> See DICOM standard part 14 for more details on display calibration and Barten&#8217;s model (including GSDF).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmdspfn/">dcmdspfn</a></code>(1), <code><a href="/docs/linux/man/1-dcm2pnm/">dcm2pnm</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1999-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
