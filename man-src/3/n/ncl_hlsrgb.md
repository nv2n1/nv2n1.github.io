---
title: "ncl_hlsrgb(3)"
name: "ncl_hlsrgb"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_hlsrgb/"
---

HLSRGB - Converts a color specification given as Hue, Lightness, and Saturation (HLS) values to Red, Green, and Blue (RGB) intensity values. 

<h2>Synopsis</h2>CALL HLSRGB ( H, L, S, R, G, B )
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_hlsrgb (float h, float l, float s, float *r, 
 float *g, float *b)
<h2>Description</h2><dl COMPACT><dt>H
<dd>(REAL, input, range [0.,360.) ) represents the hue of the input color in HLS color space. H=0. corresponds to blue.
<dt>L
<dd>(REAL, input, range [0.,100.]) represents the lightness value of the input color in HLS color space. Lightness is a measure of the quantity of light - a lightness of 0. is black, and a lightness of 100. gives white. The pure hues occur at lightness value 50.
<dt>S
<dd>(REAL, input, range [0.,100.]) represents the saturation value of the input color in HLS color space. Saturation is a measure of how much white light is mixed with the color. Colors having a saturation value of 0. represent grays with a gray intensity value equal to the lightness L. Colors with a saturation value of 100. are fully saturated colors. The hue is undefined when S=0. The fully saturated pure hues occur when S=100. and L=50.
<dt>R
<dd>(REAL, output, range [0.,1.]) represents the red intensity component of the output color in RGB color space.
<dt>G
<dd>(REAL, output, range [0.,1.]) represents the green intensity component of the output color in RGB color space.
<dt>B
<dd>(REAL, output, range [0.,1.]) represents the blue intensity component of the output color in RGB color space.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpcldm, ccplbam, ccpllb, ccplll, ccpllw, colcon, fcce02.
<h2>Access</h2>To use HLSRGB or c_hlsrgb, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the colconv man page for a description of all Colconv error messages and/or informational messages.
<h2>See Also</h2>Online: colconv, hlsrgb, hsvrgb, rgbhls, rgbhsv, rgbyiq, yiqrgb, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
