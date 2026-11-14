---
title: "ncl_rgbhsv(3)"
name: "ncl_rgbhsv"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_rgbhsv/"
---

RGBHSV - Converts a color specification given in the Red, Green, Blue (RGB) color space to color values in the Hue, Saturation, and Value (HSV) color space.

<h2>Synopsis</h2>

CALL RGBHSV (R, G, B, H, S, V)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_rgbhsv (float r, float g, float b, float *h, 
 float *s, float *v)

<h2>Description</h2>

<dl><dt>R
<dd>(REAL, input, range [0.,1.]) represents the red intensity component of the input point in RGB color space.
<dt>G
<dd>(REAL, input, range [0.,1.]) represents the green intensity component of the input point in RGB color space.
<dt>B
<dd>(REAL, input, range [0.,1.]) represents the blue intensity component of the input point in RGB color space.
<dt>H
<dd>(REAL, output, range [0.,360.) ) represents the hue of the input point in HSV color space. A value of (R,0.,0.) in the input space will result in a hue of 0. in the output space.
<dt>S
<dd>(REAL, output, range [0.,1.]) represents the saturation value of the input point in HSV color space. Saturation is a measure of how much white light is mixed with the color. Saturation values of 0. represent grays (with a gray value equal to V). Saturation values of 1. are fully saturated colors. The hue is technically undefined when S=0.; the code leaves H at its previous value when S=0. (0. initially). The fully saturated pure hues occur when S=1. and V=1.
<dt>V
<dd>(REAL, output, range [0.,1.]) represents the value in HSV space.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: tcolcv, fcce02.

<h2>Access</h2>

To use RGBHSV or c_rgbhsv, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the colconv man page for a description of all Colconv error messages and/or informational messages.

<h2>See Also</h2>

Online: colconv, hlsrgb, hsvrgb, rgbhls, rgbyiq, yiqrgb, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
