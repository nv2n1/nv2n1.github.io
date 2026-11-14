---
title: "ncl_surface(3)"
name: "ncl_surface"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_surface/"
---

Surface - A utility for drawing perspective picture of a function of two variables with hidden lines removed.

<h2>Synopsis</h2>

EZSRFC - Draws a perspective picture of a function of two variables with hidden lines removed. The function is approximated by a two-dimensional array of heights. Use EZSRFC only if the entire array is to be drawn, the data points are equally spaced in the X-Y plane, there are no stereo pairs, and scaling is chosen internally. 

 PWRZS - A character-plotting routine for plotting characters in three-space when using SRFACE. 

 SETR - Establishes certain constants so that SRFACE produces a picture whose size changes with respect to the viewer's distance from the object. It can also be used when making a movie of an object evolving in time to keep it positioned properly on the screen, saving computer time in the bargin. Call it with r0 negative to turn off this feature. 

 SRFACE - Draws a perspective picture of a function of two variables with hidden lines removed. The function is approximated by a two-dimensional array of heights.

<h2>C-Binding Synopsis</h2>

c_ezsrfc 
 c_pwrzs 
 c_setr 
 c_srface

<h2>Access</h2>

To use Surface routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: surface_params, ezsrfc, pwrzs, setr, srface. ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
