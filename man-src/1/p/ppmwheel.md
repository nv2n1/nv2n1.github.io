---
title: "ppmwheel(1)"
name: "ppmwheel"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmwheel/"
description: "ppmwheel – make a PPM image of a color wheel"
---

<h2 class="name">NAME</h2>
<p> ppmwheel &#8211; make a PPM image of a color wheel</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmwheel</code> <i>diameter</i> </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>ppmwheel</code> produces a PPM image of a color wheel of the specified diameter inside a white square just large enough to hold it. </p>
<p> The color wheel is based on the HSV color model. Hues are distributed angularly around the circle and the values are distributed radially and the saturation is zero everywhere. The values are zero at the center, increasing linearly to maximum at the edge. The maximum value corresponds to the maxval of the PPM image. </p>
<p> Hence, the image contains all of the secondary colors based on the red, green, and blue primary colors. A secondary color is one that is composed of light of at most two of the three primary colors. </p>
<h2>OPTIONS</h2>
<p> None. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmcie/">ppmcie</a></code>(1) , <code><a href="/docs/linux/man/1-ppmrainbow/">ppmrainbow</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>ppmwheel</code> was added to Netpbm in Release 10.14 (March 2003). </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1995 by Peter Kirchgessner </p>
<h2>Index</h2>
