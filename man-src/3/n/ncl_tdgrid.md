---
title: "ncl_tdgrid(3)"
name: "ncl_tdgrid"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdgrid/"
---

TDGRID - Draw a perimeter, optionally with ticks or grid lines, around the edges of the reference parallelogram defined by the last call to TDPARA. This routine is normally called indirectly (by virtue of a call to TDGRDS), but there is no reason why it should not be called directly.

<h2>Synopsis</h2>

CALL TDGRID (XBEG, XSTP, NOXS, YBEG, YSTP, NOYS, IGRD)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdgrid(float xbeg, float xstp, int noxs, float ybeg, float ystp, int noys, int igrd)

<h2>Description</h2>

The arguments of TDGRID are as follows:
<dl><dt>XBEG, XSTP, and NOXS
<dd>(input expressions of types REAL, REAL, and INTEGER, respectively) - define where ticks or grid lines are to be drawn along the &quot;X&quot; axis of the parallelogram (at XBEG, XBEG+XSTP, XBEG+2*XSTP, ... XBEG+NOXS*XSTP).
<dt>YBEG, YSTP, and NOYS
<dd>(input expressions of types REAL, REAL, and INTEGER, respectively) - define where ticks or grid lines are to be drawn along the &quot;Y&quot; axis of the parallelogram (at YBEG, YBEG+YSTP, YBEG+2*YSTP, ... YBEG+NOYS*YSTP).
<dt>IGRD
<dd>(an input expression of type INTEGER) - defines what is to be drawn and has one of the values 1 (draw just a perimeter), 2 (draw a perimeter with inward-pointing ticks), or 3 (draw a perimeter with a grid).</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDGRID or c_tdgrid, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
