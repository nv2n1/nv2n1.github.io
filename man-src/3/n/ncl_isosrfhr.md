---
title: "ncl_isosrfhr(3)"
name: "ncl_isosrfhr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_isosrfhr/"
---

Isosrfhr - Draws a wireframe surface with hidden contours removed. 

<h2>Status</h2>Isosrfhr is obsolete. It was written to do one contour plane at a time when computers had small memories. It has been replaced by the Isosurface utility. For a description of Isosurface: type &quot;man isosurface&quot;. 

 Isosrfhr continues to be provided for compatibility of early NCAR Graphics codes. If you are writing new code, we suggest that you use Isosurface.
<h2>Synopsis</h2>DANDR - Draws the contours represented by a single U plane. The calling program must loop over the number of U planes (NU) which routine INIT3D has stored on a scratch file. 
 INIT3D - Transforms the VW grids (NU of them) into a series of 2-D perspectives which are stored on a file. Entry INIT3D must be called before the entry DANDR is called for the first time.
<h2>Usage</h2>Entries INIT3D and DANDR must be used in tandem to create a plot. First call entry INIT3D to create a set of 2-D perspective planes which are output to a scratch file. Then, in the calling program you must loop over the U dimension of UVW space starting at the last slab, NU, and moving forward to slab 1. Initially set all elements of IOBJS to zeros. Then, at all locations (J,K) where the surface of an object would appear, set IOBJS(J,K) = 1. When IOBJS(J,K) has been defined for that VW slab (U = NU - I + 1), call the entry DANDR, which draws any object contours based on the 2-D perspective defined for that slab. 

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
 1 CALL DANDR(NV,NW,ST1,LX,NX,NY,IS2,IU,S,IOBJS,MV)</pre><h2>Access</h2>To use Isosrfhr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: init3d, dandr, isosurface, isosurface_params, ezisos, isgeti, isgetr, isosrf, isseti, issetr, pwrzi, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
