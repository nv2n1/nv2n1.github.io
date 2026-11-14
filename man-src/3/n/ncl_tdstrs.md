---
title: "ncl_tdstrs(3)"
name: "ncl_tdstrs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdstrs/"
---

TDSTRS - Set the values defining a selected rendering style, which affects the appearance of triangles drawn by a call to the routine TDDTRI.

<h2>Synopsis</h2>

CALL TDSTRS (IRST, IFC1, IFC2, IFC3, IFC4, ILC1, ILC2, ILTD, USTP, VSTP, WSTP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdstrs(int irst, int ifc1, int ifc2, int ifc3, int ifc4, int ilc1, int ilc2, int iltd, float ustp, float vstp, float wstp)

<h2>Description</h2>

The arguments of TDSTRS are as follows:
<dl><dt>IRST
<dd>(an input expression of type INTEGER) - the index of the particular rendering style which is to be retrieved.
<dt>IFC1 and IFC2
<dd>(output variables of type INTEGER) - color indices specifying a range of colors to be used for the &quot;bottom&quot; side of a surface (where function values are less than the value on the surface). If IFC1 is negative, filling of triangles seen from the &quot;bottom&quot; is turned off. If IFC1 is zero or greater, but IFC2 is less than or equal to it, the color with index IFC1 is used. If IFC1 is zero or greater and IFC2 is greater than IFC1, then a range of color indices is specified; colors near the beginning of that range are used for triangles that are nearly perpendicular to the line of sight, while colors near the end of that range are used for triangles more nearly parallel to the line of sight. (Normally, one should make triangles perpendicular to the line of sight lighter than those parallel to the line of sight.)
<dt>IFC3 and IFC4
<dd>(output variables of type INTEGER) - color indices specifying a range of colors to be used for the &quot;top&quot; side of a surface (where function values are greater than the value on the surface). If IFC3 is negative, filling of triangles seen from the &quot;top&quot; is turned off. If IFC3 is zero or greater, but IFC4 is less than or equal to it, the color with index IFC3 is used. If IFC3 is zero or greater and IFC4 is greater than IFC3, then a range of color indices is specified; colors near the beginning of that range are used for triangles that are nearly perpendicular to the line of sight, while colors near the end of that range are used for triangles more nearly parallel to the line of sight. (Normally, one should make triangles perpendicular to the line of sight lighter than those parallel to the line of sight.)
<dt>ILC1
<dd>(an output variable of type INTEGER) - the color index specifying a color to be used for lines drawn on the &quot;bottom&quot; side of a surface. If ILC1 is negative, the drawing of these lines is turned off.
<dt>ILC2
<dd>(an output variable of type INTEGER) - the color index specifying a color to be used for lines drawn on the &quot;top&quot; side of a surface. If ILC2 is negative, the drawing of these lines is turned off.
<dt>ILTD
<dd>(an output variable of type INTEGER) - a flag, which, if set non-zero, turns on the drawing of the edges of the individual triangles into which surfaces have been decomposed.
<dt>USTP, VSTP, and WSTP
<dd>(output variables of type REAL) - the distances between slices in the U, V, and W directions, respectively. If a given value is zero, the associated slice lines are not drawn.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDSTRS or c_tdstrs, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
