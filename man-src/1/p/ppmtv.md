---
title: "ppmtv(1)"
name: "ppmtv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtv/"
---

<h2 class="name">NAME</h2>
 

 ppmtv - make a portable pixmap look like taken from an American TV 

<h2>SYNOPSIS</h2>

 ppmtv <i>dimfactor</i> [<i>ppmfile</i>]

<h2>DESCRIPTION</h2>

 Reads a portable pixmap as input. Dims every other row of image data down by the specified dim factor. This factor may be in the range of 0.0 (the alternate lines are totally black) to 1.0 (original image). 

 This creates an effect similar to what I've once seen in the video clip 'You could be mine' by Guns'n'Roses. In the scene I'm talking about you can see John Connor on his motorbike, looking up from the water trench (?) he's standing in. While the camera pulls back, the image gets 'normal' by brightening up the alternate rows of it. I thought this would be an interesting effect to try in MPEG. I did not yet check this out, however. Try for yourself.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/5-ppm/">ppm</a>(5), <a HREF="/docs/linux/man/1-ppmdim/">ppmdim</a>(1)

<h2>AUTHOR</h2>

 Copyright (C) 1993 by Frank Neumann 

<h2>Index</h2>


