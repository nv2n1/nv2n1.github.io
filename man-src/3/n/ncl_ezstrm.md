---
title: "ncl_ezstrm(3)"
name: "ncl_ezstrm"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ezstrm/"
---

EZSTRM - A front-end to STRMLN with a simpler interface. Like STRMLN, it plots a streamline representation of field flow data in a single call. 

<h2>Status</h2>EZSTRM is obsolete, and is supported only to provide compatibility with old NCAR Graphics codes. However, the compatibility mode parameter, CPM, offers a number of options to help ease the the transition to the new version of the utility. When writing new code you are encouraged not to use this entry point, since it provides less capability than the standard Streamlines interface, and may eventually be phased out.
<h2>Synopsis</h2>CALL EZSTRM (U,V,WORK,IMAX,JMAX)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ezstrm (float *u, float *v, float *work, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int imax, int jmax)
<h2>Description</h2><dl COMPACT><dt>U
<dd>(REAL 2-dimensional array, dimensioned IMAX x n: n &gt;= JMAX, input) By default, assumed to contain the first dimensional Cartesian components of the vector field. However, if PLR is non-zero, it is treated as containing the vector magnitudes.
<dt>V
<dd>(REAL 2-dimensional array, dimensioned IMAX x n: n &gt;= JMAX, input) By default, assumed to contain the second dimensional Cartesian components of the vector field. However, if PLR is non-zero, it is treated as containing the vector angles.
<dt>WORK
<dd>(REAL array, dimensioned n: n&gt;= 2*IMAX*JMAX working space): User provided work array used to store the normalized vector component values, and also to keep track of the grid boxes eligible for starting a streamline or placement of a directional arrow.
<dt>IMAX
<dd>(INTEGER, input) Actual size of the first dimension of arrays U and V
<dt>JMAX
<dd>(INTEGER, input) Assumed size of the second dimension of arrays U and V.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exceptions: 

<dl COMPACT><dt>imax
<dd>The actual size of the second dimension of arrays u and v.
<dt>jmax
<dd>The assumed size of first dimension of arrays u and v.</dl><h2>Usage</h2>U and V are 2-dimensional vector component arrays, whose actual first dimensions must be equal to the value of IMAX, and whose second dimensions must equal or exceed the value of JMAX. The WORK array must, at minimum, be of length 2*IMAX*JMAX. 

 Assuming the default value of the compatibility mode parameter, CPM, Streamlines always performs a SET call and draws a perimeter around the plot when accessed through the EZSTRM interface. Before the return from EZSTRM, another call to SET restores the previous coordinate system mapping. 

 By modifying the value of CPM, you may take more control over the utility than originally possible using this entry point. For instance, you can override the default value of the SET parameter, or use the Version 3.2 coordinate system mapping routines instead of the old FX and FY functions. Nevertheless, when creating new code, use the STINIT/STREAM interface, since its capabilities are greater and more likely to improve with time.
<h2>Access</h2>To use EZSTRM, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: fx, stgetc, stgeti, stgetr, stinit, stream, streamlines, streamlines_params, strset, stsetc, stseti, stsetr, stuixy, stumsl, stumta, stumxy, ncarg_cbind.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
