---
title: "ncl_tdgrds(3)"
name: "ncl_tdgrds"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdgrds/"
---

TDGRDS - Draw perimeters, optionally with ticks or grid lines, on the six sides of a box. This routine calls TDPARA and will therefore change the definition of the reference parallelogram.

<h2>Synopsis</h2>

CALL TDGRDS (UMIN, VMIN, WMIN, UMAX, VMAX, WMAX, USTP, VSTP, WSTP, IGRT, IHID)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdgrds(float umin, float vmin, float wmin, float umax, float vmax, float wmax, float ustp, float vstp, float wstp, int igrt, int ihid)

<h2>Description</h2>

The arguments of TDGRDS are as follows:
<dl><dt>UMIN, VMIN, WMIN, UMAX, VMAX, WMAX
<dd>(input expressions of type REAL) - coordinate values defining the box in 3-space. The names of these should make it clear what they are.
<dt>USTP, VSTP, and WSTP
<dd>(input expressions of type REAL) - specify step sizes between ticks or grid lines in the U direction, the V direction, and the W direction, respectively. If one of these values is less than or equal to zero, the ticks or grid lines in the associated direction are omitted.
<dt>IGRT
<dd>(an input expression of type INTEGER) - of the form 10*IGRN+IGRF, where IGRN is a value specifying what to draw on the near sides of the box and IGRF is a value specifying what to draw on the far sides of the box, where &quot;near&quot; and &quot;far&quot; are as defined by the current line of sight. Each of IGRN and IGRF can have one of the values 0 (draw nothing), 1 (draw just a perimeter), 2 (draw a perimeter with inward-pointing ticks), or 3 (draw a perimeter with a grid). For example, to draw grids on the far side of the box and just perimeters on the near sides of the box, use IGRT = 13.
<dt>IHID
<dd>(an input expression of type INTEGER) - set to 0 to draw only those sides of the box that cannot be hidden by something inside the box or to 1 to draw only those sides of the box that can be hidden by something inside the box. Standard operating procedure is to call TDGRDS before drawing surfaces inside a box, with IHID set to 1, and then call it again after drawing surfaces inside a box, with IHID set to 0.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDGRDS or c_tdgrds, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
