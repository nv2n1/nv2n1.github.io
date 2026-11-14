---
title: "ncl_yiqrgb(3)"
name: "ncl_yiqrgb"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_yiqrgb/"
---

YIQRGB - Converts a color specification given in the YIQ color space to the equivalent color specification in the Red, Green, Blue (RGB) color space.

<h2>Synopsis</h2>

CALL YIQRGB (Y, I, Q, R, G, B)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_yiqrgb (float y, float i, float q, float *r, 
 float *g, float *b)

<h2>Description</h2>

<dl><dt>Y
<dd>(REAL, input, range [0.,1.]) specifies the color component of a television signal that is shown on black-and-white televisions; Y minimizes the effect of two colors appearing different to the human eye but mapping to similar monochrome intensities.
<dt>I
<dd>(REAL, input, range [-.6,.6])
<dt>Q
<dd>(REAL, input, range [-.52,.52])
<dt>R
<dd>(REAL, output, range [0.,1.]) represents the red intensity component of the output color in RGB color space.
<dt>G
<dd>(REAL, output, range [0.,1.]) represents the green intensity component of the output color in RGB color space.
<dt>B
<dd>(REAL, output, range [0.,1.]) represents the blue intensity component of the output color in RGB color space.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: tcolcv, fcce02.

<h2>Access</h2>

To use YIQRGB or c_yiqrgb, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: colconv, hlsrgb, hsvrgb, rgbhls, rgbhsv, rgbyiq, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
