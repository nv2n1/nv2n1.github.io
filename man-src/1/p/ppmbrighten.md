---
title: "ppmbrighten(1)"
name: "ppmbrighten"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmbrighten/"
---

<h2 class="name">NAME</h2>
 

 ppmbrighten - change an images Saturation and Value from an HSV map 

<h2>SYNOPSIS</h2>

 ppmbrighten [-n] [-s &lt;+- saturation&gt;] [-v &lt;+- value&gt;] &lt;ppmfile&gt;

<h2>DESCRIPTION</h2>

 Reads a portable pixmap as input. Converts the image from RGB space to HSV space and changes the Value by &lt;+- value&gt; as a percentage. Likewise with the Saturation. Doubling the Value would involve 

 ppmbrighten -v 100 

 to add 100 percent to the Value. 

 The 'n' option normalizes the Value to exist between 0 and 1 (normalized).

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-pgmnorm/">pgmnorm</a>(1), <a HREF="/docs/linux/man/5-ppm/">ppm</a>(5)

<h2>AUTHOR</h2>

 Copyright (C) 1990 by Brian Moffet Copyright (C) 1989 by Jef Poskanzer. 

 Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. This software is provided &quot;as is&quot; without express or implied warranty.

<h2>NOTES</h2>

 This program does not change the number of colors. 

<h2>Index</h2>


