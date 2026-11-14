---
title: "ncl_c_shgetnp(3)"
name: "ncl_c_shgetnp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_shgetnp/"
---

c_shgetnp - find the nearest points to a specified point in 3-space
<h2>Function Prototype</h2><pre>int c_shgetnp(float, float, float, int, float *, float *, float *,
 int, int *);</pre><h2>Synopsis</h2><pre>int c_shgetnp (px, py, pz, n, x[], y[], z[], iflag, ier );</pre><h2>Description</h2><dl COMPACT><dt>px
<dd>(float) The X coordinate value for a point P whose nearest neighbor is to be found.
<dt>py
<dd>(float) The Y coordinate value for a point P whose nearest neighbor is to be found.
<dt>pz
<dd>(float) The Z coordinate value for a point P whose nearest neighbor is to be found.
<dt>n
<dd>(int) The number of input data points, n &gt; 1.
<dt>x
<dd>(float) An array of length n containing the X coordinate values for the input data points.
<dt>y
<dd>(float) An array of length n containing the Y coordinate values for the input data points.
<dt>z
<dd>(float) An array of length n containing the Z coordinate values for the input data points.
<dt>iflag
<dd>(int) A flag that equals 0 if this is the first call to this subroutine for the given dataset and equals 1 otherwise.
<dt>ier
<dd>(pointer to int) An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then look at the man page for shgrid_errors for details.</dl><h2>Usage</h2>c_shgetnp is called to find the nearest point to a specified point in 3-space. Successive calls to c_shgetnp will determine the point nearest the specified point exclusive of the points found in previous calls, i.e. successive calls can be used to find the N nearest points for any N between one and the maximum number of points in the input dataset. 

 c_shgetnp returns an integer, say np, such that (x[np],y[np],z[np]) is the nearest input data point to P. np = -1 if *ier is not zero. On successive calls to this function after the first (that is when iflag=1) you can find the Mth closest point to (px,py,pz) with the Mth call.
<h2>Access</h2>To use c_shgetnp, load the NCAR Graphics library ngmath.
<h2>See Also</h2>shgetnp, c_shgrid, c_shseti, c_shgeti, shgrid_params. 

 Complete documentation for Sh is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
