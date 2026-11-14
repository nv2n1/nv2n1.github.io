---
title: "ncl_rgbhls(3)"
name: "ncl_rgbhls"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_rgbhls/"
---

RGBHLS - Converts a color specification given in the Red, Green, Blue (RGB) color space to color values in the Hue, Lightness, Saturation (HLS) color space.

<h2>Synopsis</h2>

CALL RGBHLS (R, G, B, H, L, S)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_rgbhls (float r, float g, float b, float *h, 
 float *l, float *s)

<h2>Description</h2>

<dl><dt>R
<dd>(REAL, input, range [0.,1.]) represents the red intensity component of the input point in RGB color space.
<dt>G
<dd>(REAL, input, range [0.,1.]) represents the green intensity component of the input point in RGB color space.
<dt>B
<dd>(REAL, input, range [0.,1.]) represents the blue intensity component of the input point in RGB color space.
<dt>H
<dd>(REAL, output, range [0.,360.) ) represents the hue of the input point in HLS color space. A value of (0.,0.,B) in the input space will result in a hue of 0. in the output space.
<dt>L
<dd>(REAL, output, range [0.,100.]) represents the lightness value of the input point in HLS color space. Lightness is a measure of the quantity of light - a lightness of 0. is black, and a lightness of 100. gives white. The pure hues occur at lightness value 50.
<dt>S
<dd>(REAL, output, range [0.,100.]) represents the saturation value of the input point in HLS color space. Saturation is a measure of how much white light is mixed with the color. Saturation values of 0. represent grays (with a gray value equal to the lightness value L). Saturation values of 100. are fully saturated colors. The hue is undefined when S=0. The fully saturated pure hues occur when S=100. and L=50. The saturation value should be thought of as a percentage.</dl>

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: tcolcv, fcce02.

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use RGBHLS or c_rgbhls, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the colconv man page for a description of all Colconv error messages and/or informational messages.

<h2>See Also</h2>

Online: colconv, hlsrgb, hsvrgb, rgbhsv, rgbyiq, yiqrgb, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
