---
title: "ncl_setr(3)"
name: "ncl_setr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_setr/"
---

SETR - Establishes certain constants so that SRFACE produces a picture whose size changes with respect to the viewer's distance from the object. It can also be used when making a movie of an object evolving in time to keep it positioned properly on the screen, saving computer time in the bargin. Call it with r0 negative to turn off this feature.

<h2>Synopsis</h2>

SUBROUTINE SETR (XMIN,XMAX,YMIN,YMAX,ZMIN,ZMAX,R0)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_setr (float xmin, float xmax, float ymin, float ymax, 
 float zmin, float zmax, float r0)

<h2>Description</h2>

<dl><dt>XMIN,XMAX
<dd>Specifies the range of X array that will be passed to SRFACE.
<dt>YMIN,YMAX
<dd>Specifies the range of Y array that will be passed to SRFACE.
<dt>ZMIN,ZMAX
<dd>Specifies the range of Z array that will be passed to SRFACE. If a movie is being made of an evolving Z array, ZMIN and ZMAX should contain range of the union of all the Z arrays. They need not be exact.
<dt>R0
<dd>Distance between observer and point looked at when the picture is to fill the screen when viewed from the direction which makes the picture biggest. If R0 is not positive, then the relative size feature is turned off, and subsequent pictures will fill the screen.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use SETR or c_setr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: surface, surface_params, ezsrfc, pwrzs, srface. ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
