---
title: "ncl_rgbyiq(3)"
name: "ncl_rgbyiq"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_rgbyiq/"
---

RGBYIQ - Converts a color specification given in the RGB Red, Green, Blue, (RGB) color space to a color specification in the YIQ color space.

<h2>Synopsis</h2>

CALL RGBYIQ (R, G, B, Y, I, Q)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_rgbyiq (float r, float g, float b, float *y, 
 float *i, float *q)

<h2>Description</h2>

<dl><dt>R
<dd>(REAL, input, range [0.,1.]) represents the red intensity component of the input point in RGB color space.
<dt>G
<dd>(REAL, input, range [0.,1.]) represents the green intensity component of the input point in RGB color space.
<dt>B
<dd>(REAL, input, range [0.,1.]) represents the blue intensity component of the input point in RGB color space.
<dt>Y
<dd>(REAL, output, range [0.,1.]) This is the color component of a television signal that is shown on black-and-white televisions; Y minimizes the effect of two colors appearing different to the human eye but mapping to similar monochrome intensities.
<dt>I
<dd>(REAL, output, range [-.6,.6]) attains its maximum when the input triple is (1.,0.,0.); I attains its minimum when the input triple is (0.,1.,1.).
<dt>Q
<dd>(REAL, output, range [-.52,.52]) attains its maximum when the input triple is (1.,0.,1.); Q attains its minimum when the input triple is (0.,1.,0.).</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Examples</h2>

Use the ncargex command to see the following relevant example: tcolcv, fcce02.

<h2>Access</h2>

To use RGBYIQ or c_rgbyiq, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: colconv, hlsrgb, hsvrgb, rgbhls, rgbhsv, yiqrgb, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
