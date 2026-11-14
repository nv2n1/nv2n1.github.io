---
title: "ncl_init3d(3)"
name: "ncl_init3d"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_init3d/"
---

INIT3D - Draws an isosurface when used in conjunction with entry DANDR. 

<h2>Synopsis</h2>CALL INIT3D (EYE,NU,NV,NW,ST1,LX,NY,IS2,IU,S)
<h2>Status</h2>This routine is part of the obsolete Isosrfhr utility. Isosrfhr has been replaced by the Isosurface utility. To see the Isosurface utility overview man page, type &quot;man isosurface&quot;.
<h2>Description</h2><dl COMPACT><dt>EYE
<dd>(an input array of type REAL, dimensioned 3) is the position of the eye in the UVW coordinate system. Objects are considered to be in a box with 2 extreme corners at (1,1,1) and (NU,NV,NW). The eye position must have positive coordinates away from the coordinate planes U = 0, V = 0, and W = 0. While gaining experience with the package, use <a HREF="/docs/linux/man/1-eye/">EYE</a>(1) = 5.*NU, <a HREF="/docs/linux/man/2-eye/">EYE</a>(2) = 4.*NV, and <a HREF="/docs/linux/man/3-eye/">EYE</a>(3) = 3.*NW.
<dt>NU
<dd>(an input expression of type INTEGER) defines the range to be used for the U dimension of the 3-D UVW grid.
<dt>NV
<dd>(an input expression of type INTEGER) defines the range to be used for the V dimension of the 3-D UVW grid.
<dt>NW
<dd>(an input expression of type INTEGER) defines the range to be used for the W dimension of the 3-D UVW grid.
<dt>ST1
<dd>(an input array of type REAL) used as scratch work space. It must be dimensioned at least of size NV*NW*2 words.
<dt>LX
<dd>(an input array of type INTEGER) which is the first dimension of array IS2. It must be of a length to hold NX bits. On a 64 bit machine it would be LX=(NX-1)/64+1.
<dt>NY
<dd>(an input expression of type INTEGER) defines the range of cells in the Y-direction of the XY pixel model of the image plane. NY is also the second dimension of array IS2.
<dt>IS2
<dd>(an input array of type INTEGER) which holds the XY pixel model of the image plane. It is dimensioned LX by NY. The pixel model contains NX by NY elements. The sizes of NX and NY vary with the choice of options. For example, if hidden lines are drawn, NX and NY (and LX) can be smaller than when hidden lines are not drawn. If some visible lines are not drawn, NX and NY (and LX) must be made larger. As a guide, some examples which have been adequate are: <pre> GIVEN USE
 NU NV NW NX NY
--------------------------------
 100 100 60 200 200
 60 60 60 110 110
 40 40 40 75 75</pre><dt>IU
<dd>(an input expression of type INTEGER) defines the unit number of a scratch file for the package. ST1 will be written NU times on this file.
<dt>S
<dd>(an input array of type REAL, dimensioned 4) contains the world coordinates of the area where the picture is to be drawn. That is, all plotting coordinates generated will be bounded as follows: X coordinates will be between <a HREF="/docs/linux/man/1-s/">S</a>(1) and <a HREF="/docs/linux/man/2-s/">S</a>(2), Y coordinates will be between <a HREF="/docs/linux/man/3-s/">S</a>(3) and <a HREF="/docs/linux/man/4-s/">S</a>(4). To prevent distortion, have <a HREF="/docs/linux/man/2-s/">S</a>(2)<a HREF="/docs/linux/man/1--s/">-S</a>(1) = <a HREF="/docs/linux/man/4-s/">S</a>(4)<a HREF="/docs/linux/man/3--s/">-S</a>(3). 

 All coordinates should be in a range between 10. and 1010.</dl><h2>Usage</h2>Entries INIT3D and DANDR must be used in tandem to create a plot. First call entry INIT3D to create a set of 2-D perspective planes which are output to a scratch file. Then, in the calling program you must loop over the U dimension of UVW space starting at the last slab, NU, and moving forward to slab 1. Initially set all elements of IOBJS to zeros. Then, at all locations (J,K) where the surface of an object would appear, set IOBJS(J,K) = 1. When IOBJS(J,K) has been defined for that VW slab (U = NU - I + 1), call the entry DANDR, which draws any object contours based on the 2-D perspective defined for that slab. 

 An Isosrfhr example of the logical structure of a program follows: <pre> C Entry INIT3D writes NU 2-D perspective planes, ST1(NV,NW,2),
 C of the UVW grid, viewed from the position EYE, to a scratch file.
 C
 CALL INIT3D(EYE,NU,NV,NW,ST1,LX,NY,IS2,IU,S)
 C
 C NU is the extent of the U dimension.
 C
 DO 1 IBKWDS = 1,NU
 I = NU+1-IBKWDS
 C
 C You must define the presence of the objects at each VW grid point for
 C all slabs in the U direction. Ones are used to indicate the presence
 C of an object. Zeros indicate no object.
 C
 C IF (OBJ.EQ.YES) IOBJS(J,K) = 1
 C IF (OBJ.EQ.NO) IOBJS(J,K) = 0
 C
 C DANDR reads ST1(NV,NW,2) for slab I.
 C
 1 CALL DANDR(NV,NW,ST1,LX,NX,NY,IS2,IU,S,IOBJS,MV)</pre><h2>Examples</h2>Use the ncargex command to see the following relevant examples: tisohr
<h2>Access</h2>To use INIT3D load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: isosrfhr, dandr, isosurface, isosurface_params, ezisos, isgeti, isgetr, isseti, issetr, pwrzi, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
