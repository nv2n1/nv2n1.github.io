---
title: "ncl_tdlbls(3)"
name: "ncl_tdlbls"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdlbls/"
---

TDLBLS - Draw labels on selected sides of a projected box. This routine calls TDPARA and will therefore change the definition of the reference parallelogram; it also changes the value of the internal parameter 'CS2'.

<h2>Synopsis</h2>

CALL TDLBLS (UMIN, VMIN, WMIN, UMAX, VMAX, WMAX, UNLB, VNLB, WNLB, UILB, VILB, WILB, IPCK)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdlbls(float umin, float vmin, float wmin, float umax, float vmax, float wmax, char* unlb, char* vnlb, char* wnlb, char* uilb, char* vilb, char* wilb, int ipck)

<h2>Description</h2>

The arguments of TDLBLS are as follows:
<dl><dt>UMIN, VMIN, WMIN, UMAX, VMAX, WMAX
<dd>(input expressions of type REAL) - coordinate values defining the box in 3-space. The names of these should make it clear what they are.
<dt>UNLB, VNLB, and WNLB
<dd>(input, of type CHARACTER) - these strings contain numeric labels to be placed on a U axis, a V axis, and a W axis, respectively. The labels need not be in any particular order, but they have to be separated by blanks and each has to be readable using a FORTRAN format of the form &quot;En.0&quot;, where &quot;n&quot; is the length of the label.
<dt>UILB, VILB, and WILB
<dd>(input, of type CHARACTER) - these strings contain informational labels for a U axis, a V axis, and a W axis, respectively.
<dt>IPCK
<dd>(an input expression of type INTEGER) - determines which edges of the box are labelled. If IPCK is zero, all six outer edges are labelled, but if IPCK is non-zero, only three edges are labelled, one set of three if IPCK is negative, a different set if IPCK is positive.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDLBLS or c_tdlbls, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
