---
title: "hpxcvt(1)"
name: "hpxcvt"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpxcvt/"
description: "HPXcvt – Reorganise HEALPix data into a 2-D FITS image"
---

<p>HPXcvt &#8211; Reorganise HEALPix data into a 2-D FITS image</p>
<h2>Synopsis</h2>
<p><code>HPXcvt</code> [<i>-C&lt;col&gt;</i>] [<i>-c&lt;sys&gt;</i>] [<i>-n|-r</i>] [<i>-q&lt;quad&gt;</i>] [<i>-x&lt;n|s&gt;</i>]</p>
<h2>Description</h2>
<dl>
<dd>[&lt;infile&gt; [&lt;outfile&gt;]]</dd></dl>
<p> HPXcvt reorganises HEALPix data into a 2-D FITS image with HPX coordinate system. The input data may be stored in a FITS file as a primary image or image extension, or as a binary table extension. Both NESTED and RING pixel indices are supported. The input and output files may be omitted or specified as &quot;-&quot; to indicate stdin and stdout respectively.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code>&lt;col&gt;</dt>
<dd>Binary table column number from which to read data, default 1 (n.b. WMAP exclusion masks are in column 2).</dd>
<dt><code>-c</code>&lt;sys&gt;</dt>
<dd>Specify the coordinate system to be used to label the output map if the COORDSYS keyword is absent from the input FITS header. Recognised values are g (galactic), e (ecliptic) or q (equatorial).</dd>
<dt><code>-n</code>|-r</dt>
<dd>Assume n(ested) or r(ing) organization if the ORDERING keyword is absent from the input FITS header.</dd>
<dt><code>-q</code>&lt;quad&gt;</dt>
<dd>Recentre longitude at quad(mod 4) x 90 degrees, where quad(rant) is an integer.</dd>
<dt><code>-x</code>&lt;n|s&gt;</dt>
<dd>Use a north-polar or south-polar layout. </dd>
</dl>
