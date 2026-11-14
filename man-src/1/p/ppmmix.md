---
title: "ppmmix(1)"
name: "ppmmix"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmmix/"
description: "ppmmix – blend together two portable pixmaps"
---

<h2 class="name">NAME</h2>
<p> ppmmix &#8211; blend together two portable pixmaps </p>
<h2>SYNOPSIS</h2>
<p> ppmmix <i>fadefactor </i> <i>ppmfile1 ppmfile2</i></p>
<h2>DESCRIPTION</h2>
<p> Reads two portable pixmaps as input. Mixes them together using the specified fade factor. The fade factor may be in the range from 0.0 (only ppmfile1&#8217;s image data) to 1.0 (only ppmfile2&#8217;s image data). Anything in between gains a smooth blend between the two images. </p>
<p> The two pixmaps must have the same size. </p>
<p> <code>pnmcomp</code> is a more general alternative. It allows you to mix images of different size and to have the fade factor vary throughout the image (through the use of an alpha mask). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pnmcomp/">pnmcomp</a></code>(5), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1993 by Frank Neumann </p>
<h2>Index</h2>
