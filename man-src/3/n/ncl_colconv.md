---
title: "ncl_colconv(3)"
name: "ncl_colconv"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_colconv/"
---

Colconv - Allows a user to convert among the color models RGB, HSV, HLS, and YIQ. 

<h2>Synopsis</h2>HLSRGB - Converts a color specification given as Hue, Lightness, and Saturation (HLS) values to Red, Green, and Blue (RGB) intensity values in the RGB color space. 

 HSVRGB - Converts a color specification given in the Hue, Saturation, and Value (HSV) color space to color values in the Red, Green, Blue (RGB) color space. 

 RGBHLS - Converts a color specification given in the Red, Green, Blue (RGB) color space to color values in the Hue, Lightness, Saturation (HLS) color space. 

 RGBHSV - Converts a color specification given in the Red, Green, Blue (RGB) color space to color values in the Hue, Saturation, and Value (HSV) color space. 

 RGBYIQ - Converts a color specification given in the RGB Red, Green, Blue, (RGB) color space to a color specification in the YIQ color space. 

 YIQRGB - Converts a color specification given in the YIQ color space to the equivalent color specification in the Red, Green, Blue (RGB) color space.
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 c_hlsrgb 
 c_hsvrgb 
 c_rgbhls 
 c_rgbhsv 
 c_rgbyiq 
 c_yiqrgb
<h2>Access</h2>To use Colconv or c_colconv routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. 

<h2>Messages</h2>When error conditions are detected, the support routine SETER is called in such a way that it writes a message to the standard error file (as defined by <a HREF="/docs/linux/man/4-i1mach/">I1MACH</a>(4)) and then terminates execution. The possible error messages are as follows:
<dl COMPACT><dt>HLSRGB - L out of range
<dd>Lightness is less than 0. or greater than 100.
<dt>HLSRGB - S out of range
<dd>Saturation is less than 0. or greater than 100.
<dt>HSVRGB - S out of range
<dd>Saturation is less than 0. or greater than 1.
<dt>HSVRGB - V out of range
<dd>Value of input color is less than 0. or greater than 1.
<dt>RGBHLS - R out of range
<dd>Value of red intensity component is less than 0. or greater than 1.
<dt>RGBHLS - G out of range
<dd>Value of green intensity component is less than 0. or greater than 1.
<dt>RGBHLS - B out of range
<dd>Value of blue intensity component is less than 0. or greater than 1.
<dt>RGBHSV - R out of range
<dd>Value of red intensity component is less than 0. or greater than 1.
<dt>RGBHSV - G out of range
<dd>Value of green intensity component is less than 0. or greater than 1.
<dt>RGBHSV - B out of range
<dd>Value of blue intensity component is less than 0. or greater than 1.</dl><h2>See Also</h2>Online: hlsrgb, hsvrgb, rgbhls, rgbhsv, rgbyiq, yiqrgb, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
