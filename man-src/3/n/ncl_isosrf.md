---
title: "ncl_isosrf(3)"
name: "ncl_isosrf"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_isosrf/"
---

ISOSRF - Draws an isosurface. 

<h2>Synopsis</h2>CALL ISOSRF (F,LU,MU,LV,MV,MW,EYE,MUVWP2,SLAB,FISO,IFLAG)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_isosrf (float *f, int lu, int mu, int lv, int mv, 
 int mw, float eye[3], int muvwp2, float *slab, float fiso, 
 int iflag)
<h2>Utility</h2>This routine is part of the Isosurface utility in NCAR Graphics. To see the overview man page for this utility, type &quot;man isosurface&quot;.
<h2>Description</h2><dl COMPACT><dt>F
<dd>(an input array of type REAL, dimensioned LU x LV x m, where &quot;m&quot; is greater than or equal to MW) is a three-dimensional array of data defining the function f(u,v,w). Only the portion of the array consisting of elements F(IU,IV,IW), for IU = 1 to MU, IV = 1 to MV, and IW = 1 to MW, is to be used. This may or may not be the entire array. The data are considered to lie in a box in 3-space with opposite corners (in the UVW coordinate system) (1.,1.,1.) and (REAL(MU),REAL(MV),REAL(MW)). The element F(IU,IV,IW) is considered to be the value of the function f at the point (REAL(IU),REAL(IV),REAL(IW)).
<dt>LU
<dd>(an input expression of type INTEGER) is the first dimension of the array F.
<dt>MU
<dd>(an input expression of type INTEGER) defines the range to be used for the first subscript of the array F.
<dt>LV
<dd>(an input expression of type INTEGER) is the second dimension of the array F.
<dt>MV
<dd>(an input expression of type INTEGER) defines the range to be used for the second subscript of the array F.
<dt>MW
<dd>(an input expression of type INTEGER) defines the range to be used for the third subscript of the array F.
<dt>EYE
<dd>(an input array of type REAL, dimensioned 3) is the position of the eye in the UVW coordinate system. The eye position, at (<a HREF="/docs/linux/man/1-eye/">EYE</a>(1),<a HREF="/docs/linux/man/2-eye/">EYE</a>(2),<a HREF="/docs/linux/man/3-eye/">EYE</a>(3)), must be outside the box containing the data. The point being looked at is at the center of the data box and the projection plane is perpendicular to the line of sight. While gaining experience with the routine, a good choice for EYE is (5.*REAL(MU),3.5*REAL(MV),2.*REAL(MW)).
<dt>MUVWP2
<dd>(an input expression of type INTEGER) has the value MAX(MU,MV,MW)+2.
<dt>SLAB
<dd>(a scratch array of type REAL, dimensioned at least MUVWP2 x MUVWP2) is a workspace for ISOSRF.
<dt>FISO
<dd>(an input expression of type REAL) is the value of fiso in the equation f(u,v,w)=fiso, which defines the isosurface to be drawn.
<dt>IFLAG
<dd>(an input expression of type INTEGER) serves two purposes:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The absolute value of IFLAG determines which type of lines are drawn to approximate the isosurface. Three types of lines are considered: lines of constant U, lines of constant V, and lines of constant W. The following table lists the types of lines drawn for various values of ABS(IFLAG): 

 <table> <tr VALIGN=top><td>ABS(IFLAG)</td><td ALIGN=center>Constant U</td><td ALIGN=center>Constant V</td><td ALIGN=center>Constant W
</td></tr><tr VALIGN=top><td ALIGN=center>1</td><td ALIGN=center>no</td><td ALIGN=center>no</td><td ALIGN=center>yes
</td></tr><tr VALIGN=top><td ALIGN=center>2</td><td ALIGN=center>no</td><td ALIGN=center>yes</td><td ALIGN=center>no
</td></tr><tr VALIGN=top><td ALIGN=center>3</td><td ALIGN=center>no</td><td ALIGN=center>yes</td><td ALIGN=center>yes
</td></tr><tr VALIGN=top><td ALIGN=center>4</td><td ALIGN=center>yes</td><td ALIGN=center>no</td><td ALIGN=center>no
</td></tr><tr VALIGN=top><td ALIGN=center>5</td><td ALIGN=center>yes</td><td ALIGN=center>no</td><td ALIGN=center>yes
</td></tr><tr VALIGN=top><td ALIGN=center>6</td><td ALIGN=center>yes</td><td ALIGN=center>yes</td><td ALIGN=center>no
</td></tr><tr VALIGN=top><td ALIGN=center>7</td><td ALIGN=center>yes</td><td ALIGN=center>yes</td><td ALIGN=center>yes
</td></tr> </table><dt>&bull;
<dd>The sign of IFLAG determines what is inside and what is outside the solid bounded by the isosurface and thus which lines are visible and what is done at the boundary of the box containing the data. If IFLAG is positive, values greater than FISO are considered to be inside the solid formed by the isosurface. If IFLAG is negative, values less than FISO are considered to be inside the solid formed by the isosurface. If the algorithm draws a cube, reverse the sign of IFLAG.</dl></dl>
</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the Fortran argument descriptions, with the following exceptions:
<dl COMPACT><dt>f
<dd>t is dimensioned mw by mv by mu
<dt>mu
<dd>The third dimension of the array f
<dt>mw
<dd>The first dimension of the array f</dl><h2>Usage</h2>Transformations can be achieved by adjusting scaling statement functions in ISOSRF, SET3D, and TR32. 

 The hidden-line algorithm is not exact, so visibility errors can occur. 

 Three-dimensional perspective character labeling of isosurfaces is possible by calling the routine PWRZI.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tisosr, tpwrzi, fisissrf, fispwrzi.
<h2>Access</h2>To use ISOSRF or c_isosrf load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: isosurface, isosurface_params, ezisos, isgeti, isgetr, isseti, issetr, pwrzi, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
