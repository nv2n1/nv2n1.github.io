---
title: "ncl_tdpack(3)"
name: "ncl_tdpack"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdpack/"
---

Tdpack - A set of routines allowing one to draw representations of three-dimensional objects.

<h2>Synopsis</h2>

TDPACK (which stands for &quot;Three Dimensional PACKage&quot;) is a collection of routines for projecting objects from a 3-dimensional coordinate system having U, V, and W axes to a 2-dimensional projection plane having X and Y axes and/or for drawing the projections of those objects. This can be referred to somewhat loosely as &quot;drawing objects in three dimensions&quot;. 

 Tdpack consists of the following routines:
<dl><dt>Initialization Routines:
<dd><dt> TDINIT -
<dd>Define eye position, line of sight, up direction, and stereo flag.
<dt> TDPARA -
<dd>Define the reference parallelogram.
<dt> TDCLRS -
<dd>Define colors for TDPACK.
<dt>Parameter-Access Routines:
<dd><dt> TDGETI -
<dd>Get the integer value of an internal parameter.
<dt> TDGETR -
<dd>Get the real value of an internal parameter.
<dt> TDGTRS -
<dd>Get the definition of a specified rendering style.
<dt> TDSETI -
<dd>Set the integer value of an internal parameter.
<dt> TDSETR -
<dd>Set the real value of an internal parameter.
<dt> TDSTRS -
<dd>Define a specified rendering style.
<dt>Point-Transforming Routines:
<dd><dt> TDPRPT -
<dd>Project from 3-space to the projection plane.
<dt> TDPRPA -
<dd>Project from 3-space to the plane of the reference parallelogram.
<dt> TDPRPI -
<dd>Project from the plane of the reference parallelogram to 3-space.
<dt>Line-Drawing Routines:
<dd><dt> TDLINE -
<dd>Draw the projection of a line in 3-space.
<dt> TDLNPA -
<dd>Draw the projection of a line in the plane of the reference parallelogram.
<dt>Grid-Drawing Routines:
<dd><dt> TDGRDS -
<dd>Draw the grids on all the faces of a box in 3-space.
<dt> TDGRID -
<dd>Draw the grid on a particular face of a box in 3-space.
<dt>Label-Drawing Routines:
<dd><dt> TDLBLS -
<dd>Draw labels for all faces of a box in 3-space.
<dt> TDLBLA -
<dd>Draw labels for a particular face of a box in 3-space.
<dt> TDPLCH -
<dd>Draw characters in the plane of the reference parallelogram.
<dt>Surface-Drawing Routines:
<dd><dt> TDDTRI -
<dd>Draw triangles defined by a triangle list.
<dt> TDSTRI -
<dd>Add triangles defining a simple surface to a triangle list.
<dt> TDITRI -
<dd>Add triangles defining an isosurface to a triangle list.
<dt> TDMTRI -
<dd>Add triangles defining a 3D marker to a triangle list.
<dt> TDCTRI -
<dd>Order the triangles in a triangle list for proper rendering.
<dt> TDSORT -
<dd>Cut triangles with a plane perpendicular to one of the axes.
<dt> TDOTRI -
<dd>Generic sorting routine</dl>

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 c_tdinit 
 c_tdpara 
 c_tdclrs 
 c_tdgeti 
 c_tdgetr 
 c_tdgtrs 
 c_tdseti 
 c_tdsetr 
 c_tdstrs 
 c_tdprpt 
 c_tdprpa 
 c_tdprpi 
 c_tdline 
 c_tdlnpa 
 c_tdgrds 
 c_tdgrid 
 c_tdlbls 
 c_tdlbla 
 c_tdplch 
 c_tddtri 
 c_tdstri 
 c_tditri 
 c_tdmtri 
 c_tdotri 
 c_tdctri 
 c_tdsort

<h2>Access</h2>

To use Tdpack, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

When error conditions are detected, the support routine SETER is called. By default, SETER writes a message to the standard error file (as defined by <a HREF="/docs/linux/man/4-i1mach/">I1MACH</a>(4)) and then terminates execution. It is possible to put SETER into recovery mode and regain control after a recoverable error (which includes all of the possible errors). 

 The possible error messages are listed below. All errors are recoverable in the sense that a user program which has called ENTSR to set recovery mode will get control back after one of these errors occurs. 

 TDGETI - UNCLEARED PRIOR ERROR 
 TDGETR - UNCLEARED PRIOR ERROR 
 TDGETR - UNRECOGNIZED PARAMETER NAME 
 TDINIT - UNCLEARED PRIOR ERROR 
 TDPARA - UNCLEARED PRIOR ERROR 
 TDPRPA - UNCLEARED PRIOR ERROR 
 TDPRPI - UNCLEARED PRIOR ERROR 
 TDPRPT - UNCLEARED PRIOR ERROR 
 TDSETI - UNCLEARED PRIOR ERROR 
 TDSETR - UNCLEARED PRIOR ERROR 
 TDSETR - UNRECOGNIZED PARAMETER NAME

<h2>See Also</h2>

Online: tdclrs, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
