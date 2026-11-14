---
title: "ncl_ezisos(3)"
name: "ncl_ezisos"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ezisos/"
---

EZISOS - Draws an isosurface. 

<h2>Synopsis</h2>CALL EZISOS (F,MU,MV,MW,EYE,SLAB,FISO)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ezisos (float *f, int mu, int mv, int mw, 
 float eye[3], float *slab, float fiso)
<h2>Description</h2><dl COMPACT><dt>F
<dd>(an input array of type REAL, dimensioned MU x MV x MW) is a three-dimensional array of data defining the function f(u,v,w). The entire array (elements F(IU,IV,IW), for IU = 1 to MU, IV = 1 to MV, and IW = 1 to MW) is to be used. The data are considered to lie in a box in 3-space with opposite corners (in the UVW coordinate system) (1.,1.,1.) and (REAL(MU),REAL(MV),REAL(MW)). The element F(IU,IV,IW) is considered to be the value of the function f at the point (REAL(IU),REAL(IV),REAL(IW)).
<dt>MU
<dd>(an input expression of type INTEGER) is the first dimension of the array F.
<dt>MV
<dd>(an input expression of type INTEGER) is the second dimension of the array F.
<dt>MW
<dd>(an input expression of type INTEGER) is the third dimension of the array F.
<dt>EYE
<dd>(an input array of type REAL, dimensioned 3) is the position of the eye in the UVW coordinate system. The eye position, at (<a HREF="/docs/linux/man/1-eye/">EYE</a>(1),<a HREF="/docs/linux/man/2-eye/">EYE</a>(2),<a HREF="/docs/linux/man/3-eye/">EYE</a>(3)), must be outside the box containing the data. The point being looked at is at the center of the data box and the projection plane is perpendicular to the line of sight. While gaining experience with the routine, a good choice for EYE is (5.*REAL(MU),3.5*REAL(MV),2.*REAL(MW)).
<dt>SLAB
<dd>(a scratch array of type REAL, dimensioned at least n x n, where &quot;n&quot; is defined to be MAX[MU,MV,MW]+2) is a workspace for ISOSRF.
<dt>FISO
<dd>(an input expression of type REAL) is the value of fiso in the equation f(u,v,w)=fiso, which defines the isosurface to be drawn.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the Fortran argument descriptions, with the following exceptions:
<dl COMPACT><dt>f
<dd>t is dimensioned mw by mv by mu
<dt>mu
<dd>The third dimension of the array f
<dt>mw
<dd>The first dimension of the array f</dl><h2>Usage</h2>EZISOS is called to draw an isosurface if all of the input array is to be used (rather than a subset of it), if ISOSRF's argument IFLAG is to be chosen internally, and if a frame advance is to be done after the isosurface is drawn. If any of these conditions is not met, use ISOSRF instead.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: tisosr, fisissrf.
<h2>Access</h2>To use EZISOS or c_ezisos, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: isosurface, isosurface_params, isgeti, isgetr, isosrf, isseti, issetr, pwrzi, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
