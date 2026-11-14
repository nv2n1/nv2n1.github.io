---
title: "ppmshift(1)"
name: "ppmshift"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmshift/"
---

<h2 class="name">NAME</h2>
 

 ppmshift - shift lines of a portable pixmap left or right by a random amount 

<h2>SYNOPSIS</h2>

 ppmshift <i>shift</i> [<i>ppmfile</i>]

<h2>DESCRIPTION</h2>

 Reads a portable pixmap as input. Shifts every row of image data to the left or right by a certain amount. The 'shift' parameter determines by how many pixels a row is to be shifted at most. 

 Another one of those effects I intended to use for MPEG tests. Unfortunately, this program will not help me here - it creates too random patterns to be used for animations. Still, it might give interesting results on still images.

<h2>EXAMPLE</h2>

 Check this out: Save your favourite model's picture from something like alt.binaries.pictures.supermodels (ok, or from any other picture source), convert it to ppm, and process it e.g. like this, assuming the picture is 800x600 pixels: 
&nbsp;<wbr>&nbsp;#&nbsp;take the upper half, and leave it like it is 
&nbsp;<wbr>&nbsp;pnmcut 0 0 800 300 cs.ppm&nbsp;&gt;upper.ppm 

 
&nbsp;<wbr>&nbsp;#&nbsp;take the lower half, flip it upside down, dim it and distort it a little 
&nbsp;<wbr>&nbsp;pnmcut 0 300 800 300 cs.ppm | pnmflip -tb | ppmdim 0.7 |&nbsp; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ppmshift 10&nbsp;&gt;lower.ppm 

 
&nbsp;<wbr>&nbsp;#&nbsp;and concatenate the two pieces 
&nbsp;<wbr>&nbsp;pnmcat -tb upper.ppm lower.ppm&nbsp;&gt;newpic.ppm The resulting picture looks like the image being reflected on a water surface with slight ripples.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/5-ppm/">ppm</a>(5), <a HREF="/docs/linux/man/1-pnmcut/">pnmcut</a>(1), <a HREF="/docs/linux/man/1-pnmflip/">pnmflip</a>(1), <a HREF="/docs/linux/man/1-ppmdim/">ppmdim</a>(1), <a HREF="/docs/linux/man/1-pnmcat/">pnmcat</a>(1)

<h2>AUTHOR</h2>

 Copyright (C) 1993 by Frank Neumann 

<h2>Index</h2>


