---
title: "ncl_wmdrrg(3)"
name: "ncl_wmdrrg"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmdrrg/"
---

WMDRRG - plots weather map regions (indicating &quot;snow&quot;, &quot;rain&quot;, etc.), or solid regions indicating temperature zones.

<h2>Synopsis</h2>

CALL WMDRRG(N,X,Y,ITYPE,NC,XC,YC)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/gks.h&gt; 

 void c_wmdrrg(int n, float *x, float *y, char *itype, int nc, float *xc, float *yc)

<h2>Description</h2>

<dl><dt>N
</dt><dd>(Integer, Input) - The number of points supplied in the second and third arguments.
</dd><dt>X
</dt><dd>(Real, Input) - The X coordinates (specified in world coordinates) of N points that specify the control points of a spline curve that will be fitted to represent the requested region.
</dd><dt>Y
</dt><dd>(Real, Input) - The Y coordinates (specified in world coordinates) of N points that specify the control points of a spline curve that will be fitted to represent the requested region.
</dd><dt>ITYPE
</dt><dd>(Character, Input) - Indicates the weather type to fill the region with, or a solid color.
</dd><dl><dd></dd><dl><dt>ITYPE can be one of:
</dt><dd>&nbsp;<wbr>'T'&nbsp;<wbr>for thunderstorms 
&nbsp;<wbr>'SH'&nbsp;<wbr>for showers 
&nbsp;<wbr>'R'&nbsp;<wbr>for rain 
&nbsp;<wbr>'F'&nbsp;<wbr>for flurries 
&nbsp;<wbr>'SN'&nbsp;<wbr>for snow 
&nbsp;<wbr>'I'&nbsp;<wbr>for ice <pre><code>'INDEXnn' where the number &quot;nn&quot; denotes a color index for a solid fill.
NC
(Integer, input) - If NC is greater than 2, then the region resulting from
the spline fit to ((X(I),Y(I)),I=1,N) will be clipped against the region in
((XC(I),YC(I)),I=1,NC). If no clipping is to be done, then set NC equal to 1.
XC
(Real, Input) - The X coordinates  (specified in world coordinates) of
NC points that specify a clipping polygon for the region resulting from
the spline fit to ((X(I),Y(I)),I=1,N), if NC is greater than 2.
YC
(Real, Input) - The Y coordinates  (specified in world coordinates) of
NC points that specify a clipping polygon for the region resulting from
the spline fit to ((X(I),Y(I)),I=1,N), if NC is greater than 2.</code></pre>
<h2>Usage</h2>
Set the values for the appropriate internal parameters before calling WMDRRG to produce the desired region. The internal parameters that control the appearance of regions are: COL and RHT. As mentioned above, the points specified in the X and Y arrays serve as control points for a spline curve that is fitted to the input polygon. X(N) should equal X(1) and Y(N) should equal Y(1).
<h2>Access</h2>
To use WMDRRG or c_wmdrrg, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>
Online: wmap, wmdflt, wmgetc, wmgeti, wmgetr, wmsetc, wmseti, wmsetr, wmap_params 
 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data
<h2>Copyright</h2>
Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
</dd></dl></dl></dl>