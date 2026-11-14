---
title: "ncl_ngritd(3)"
name: "ncl_ngritd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngritd/"
---

NGRITD - Given the coordinates of a point, this routine performs a rotation of that point about a specified axis by a specified angle.

<h2>Synopsis</h2>

CALL NGRITD (IAXS,ANGL,UCRD,VCRD,WCRD)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_ngritd(int iaxs, float angl, float *ucrd, float *ycrd, 
 float *wcrd)

<h2>Description</h2>

<dl><dt>IAXS
<dd>(an input expression of type INTEGER) specifies the axis about which rotation is to be done (1 for the U axis, 2 for the V axis, and 3 for the W axis).
<dt>ANGL
<dd>(an input expression of type REAL) specifies the magnitude, in degrees, of the rotation angle.
<dt>UCRD
<dd>(an input/output variable of type REAL) specifies the U coordinate of the point being rotated.
<dt>VCRD
<dd>(an input/output variable of type REAL) specifies the V coordinate of the point being rotated.
<dt>WCRD
<dd>(an input/output variable of type REAL) specifies the W coordinate of the point being rotated.</dl>

<h2>C-Binding Description</h2>

The C binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine is used by NGGCOG and NGGSOG to effect the rotations that are used to generate an object of a specified shape at a specified point on the surface of the globe. 

 NGRITD assumes that the UVW coordinate system is right-handed. Positive values of ANGL give counter-clockwise rotations and negative values of ANGL give clockwise rotations. (When IAXS = 1, ANGL = 90 carries the positive V axis into the positive W axis; when IAXS = 2, ANGL = 90 carries the positive W axis into the positive U axis; when IAXS = 3, ANGL = 90 carries the positive U axis into the positive V axis.)

<h2>Examples</h2>

Use the ncargex command to see the following relevant example: cpex10.

<h2>Access</h2>

To use NGRITD or c_ngritd, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

None.

<h2>See Also</h2>

Online: nggcog(3NCARG), nggsog(3NCARG).

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
