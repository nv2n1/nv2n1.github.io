---
title: "ncl_bivar_params(3)"
name: "ncl_bivar_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_bivar_params/"
---

Bivar_params - This document briefly describes all Bivar parameters. 

<h2>Description</h2>Bivar currently supports two parameters. The current values may be retrieved using one of the routines IDGETI or IDGETR. Parameter values may be reset using the routine IDSETI or IDSETR. 

 The Bivar parameter descriptions appear below in alphabetical order. Each description begins with a line giving the parameter name and the intrinsic FORTRAN type of the parameter.
<dl COMPACT><dt>'ITY' - Integer
<dd>Interpolation Type. The default value, 0, says that quintic interpolation should be done. The value 1 says to use linear interpolation.
<dt>'TTY' - Integer
<dd>Triangulation Type. The default value, 0, says to use a triangulation due to C. L. Lawson that maximizes the minimum angle occurring in the triangles. The value 1 says to use the Delaunay triangulation, which ensures triangles whose circumscribed circles have no data points in their interiors.</dl><h2>See Also</h2>Online: bivar, idbvip, idsfft, idpltr, idgeti, idgetr, idseti, idsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
