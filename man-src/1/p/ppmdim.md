---
title: "ppmdim(1)"
name: "ppmdim"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmdim/"
---

<h2 class="name">NAME</h2>
 

 ppmdim - dim a portable pixmap down to total blackness 

<h2>SYNOPSIS</h2>

 ppmdim <i>dimfactor</i> [<i>ppmfile</i>]

<h2>DESCRIPTION</h2>

 Reads a portable pixmap as input. Diminishes its brightness by the specified dimfactor down to total blackness. The dimfactor may be in the range from 0.0 (total blackness, deep night, nada, null, nothing) to 1.0 (original picture's brightness). 

 As <i>pnmgamma </i> does not do the brightness correction in the way I wanted it, this small program was written. 

 ppmdim is similar to <i>ppmbrighten</i> , but not exactly the same.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/5-ppm/">ppm</a>(5), <a HREF="/docs/linux/man/1-ppmflash/">ppmflash</a>(1), <a HREF="/docs/linux/man/1-pnmgamma/">pnmgamma</a>(1), <a HREF="/docs/linux/man/1-ppmbrighten/">ppmbrighten</a>(1)

<h2>AUTHOR</h2>

 Copyright (C) 1993 by Frank Neumann 

<h2>Index</h2>


