---
title: "ppmflash(1)"
name: "ppmflash"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmflash/"
---

<h2 class="name">NAME</h2>
 

 ppmflash - brighten a picture up to complete white-out 

<h2>SYNOPSIS</h2>

 ppmflash <i>flashfactor </i> [<i>ppmfile</i>]

<h2>DESCRIPTION</h2>

 Reads a portable pixmap as input. Increases its brightness by the specified flashfactor up to a total white-out image. The flashfactor may be in the range from 0.0 (original picture's brightness) to 1.0 (full white-out, The Second After). 

 As <i>pnmgamma</i> does not do the brightness correction in the way I wanted it, this small program was written. 

 This program is similar to <i>ppmbrighten</i> , but not exactly the same.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/5-ppm/">ppm</a>(5), <a HREF="/docs/linux/man/1-ppmdim/">ppmdim</a>(1), <a HREF="/docs/linux/man/1-pnmgamma/">pnmgamma</a>(1), <a HREF="/docs/linux/man/1-ppmbrighten/">ppmbrighten</a>(1)

<h2>AUTHOR</h2>

 Copyright (C) 1993 by Frank Neumann 

<h2>Index</h2>


