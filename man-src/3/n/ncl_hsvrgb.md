---
title: "ncl_hsvrgb(3)"
name: "ncl_hsvrgb"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_hsvrgb/"
---

HSVRGB - Converts a color specification given in the Hue, Saturation, and Value (HSV) color space to color values in the Red, Green, Blue (RGB) color space. 

<h2>Synopsis</h2>CALL HSVRGB (H, S, V, R, G, B)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_hsvrgb (float h, float s, float v, float *r, 
 float *g, float *b)
<h2>Description</h2><dl COMPACT><dt>H
<dd>(REAL, input, range [0.,360.) ) represents the hue of the input color in HSV color space.
<dt>S
<dd>(REAL, input, range [0.,1.]) represents the saturation value of the input color in HSV color space. Saturation is a measure of how much white light is mixed with the color. Saturation values of 0. represent grays (with a gray value equal to the value V). Saturation values of 1. are fully saturated colors. The hue is undefined when S=0. The fully saturated pure hues occur when S=1. and V=1.
<dt>V
<dd>(REAL, input, range [0.,1.]) represents the value of the input color in HSV color space.
<dt>R
<dd>(REAL, output, range [0.,1.]) represents the red intensity component of the output color in RGB color space.
<dt>G
<dd>(REAL, output, range [0.,1.]) represents the green intensity component of the output color in RGB color space.
<dt>B
<dd>(REAL, output, range [0.,1.]) represents the blue intensity component of the output color in RGB color space.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: coex03, tcolcv, fcce02.
<h2>Access</h2>To use HSVRGB or c_hsvrgb, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the colconv man page for a description of all Colconv error messages and/or informational messages.
<h2>See Also</h2>Online: colconv, hlsrgb, rgbhls, rgbhsv, rgbyiq, yiqrgb, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
