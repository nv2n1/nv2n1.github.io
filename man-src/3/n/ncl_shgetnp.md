---
title: "ncl_shgetnp(3)"
name: "ncl_shgetnp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_shgetnp/"
---

SHGETNP - find the nearest points to a specified point in 3-space.

<h2>Synopsis</h2>

CALL SHGETNP (PX, PY, PZ, N, X, Y, Z, IFLAG, IWK, RWK, NP, IER)

<h2>Description</h2>

<dl><dt>PX
<dd>(real,input) The X coordinate value for a point P whose nearest neighbor is to be found.
<dt>PY
<dd>(real,input) The Y coordinate value for a point P whose nearest neighbor is to be found.
<dt>PZ
<dd>(real,input) The Z coordinate value for a point P whose nearest neighbor is to be found.
<dt>X
<dd>(real, input) An array containing the X coordinates of the input data points.
<dt>Y
<dd>(real, input) An array containing the Y coordinates of the input data points.
<dt>Z
<dd>(real, input) An array containing the Z coordinates of the input data points.
<dt>IFLAG
<dd>(integer, input) A flag that equals 0 if this is the first call to this subroutine for the given dataset and equals 1 otherwise.
<dt>IRK
<dd>(integer, input) An integer workspace dimensioned for at least 2*N.
<dt>RWK
<dd>(real, input) A real workspace dimensioned for at least 11*N+6.
<dt>NP
<dd>(integer, output) An index such that (X(NP),Y(NP),Z(NP)) is the nearest input data point to P. NP = 0 if IER .NE. 0. On successive calls to this subroutine after the first (that is when IFLAG=1) you can find the Mth closest point to (PX,PY,PZ) with the Mth call. IWK and RWK should not be modified between calls to SHGETNP if you are wanting to find successive nearest neighbors.
<dt>IER
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for shgrid_errors for details.</dl>

<h2>Usage</h2>

SHGETNP is called to find the nearest point to a specified point in 3-space. Successive calls to SHGETNP will determine the point nearest the specified point exclusive of the points found in previous calls, i.e. successive calls can be used to find the N nearest points for any N between one and the maximum number of points in the input dataset.

<h2>Access</h2>

To use SHGETNP, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

shgrid, shseti, shgeti, shgrid_params. 

 Complete documentation for Shgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html</a>

<h2>Copyright</h2>

Copyright (C) 1997-2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
