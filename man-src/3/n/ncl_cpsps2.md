---
title: "ncl_cpsps2(3)"
name: "ncl_cpsps2"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpsps2/"
---

CPSPS2 - Interpolates from an array of data on a &quot;sparse&quot; rectangular grid which is irregularly spaced in X and Y to an array of data on a &quot;dense&quot; rectangular grid and initializes contouring from the array on the dense grid. (By a &quot;sparse&quot; grid is meant one whose dimensions are smaller than one would like, so that contour lines constructed directly on it are composed of long straight segments.) CPSPS2 may be viewed as a data smoothing routine. 

<h2>Synopsis</h2>&nbsp;<wbr>CALL CPSPS2&nbsp;<wbr>(XSPS, YSPS, ZSPS, KSPS, MSPS, NSPS, RWRK,&nbsp;<wbr> 
 + LRWK, IWRK, LIWK, ZDAT, LZDT)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cpsps2 (float *xsps, float *ysps, float *zsps, 
 int ksps, int msps, int nsps, float *rwrk, int lrwk, 
 int *iwrk, int liwk, float *zdat, int lzdt)
<h2>Description</h2><dl COMPACT><dt>XSPS
<dd>(REAL array, dimensioned MSPS) is the array of X coordinates of the irregular rectangular grid. These must be in strictly increasing numerical order.
<dt>YSPS
<dd>(REAL array, dimensioned NSPS) is the array of Y coordinates of the irregular rectangular grid. These must be in strictly increasing numerical order.
<dt>ZSPS
<dd>(REAL array, dimensioned KSPS x n, where &quot;n&quot; is greater than or equal to NSPS, input) is the &quot;sparse&quot; array of data, from which the &quot;dense&quot; array is to be generated.
<dt>KSPS
<dd>(INTEGER, input) is the first dimension of the array ZSPS.
<dt>MSPS
<dd>(INTEGER, input) is the first dimension of the &quot;sparse&quot; array of data in ZSPS. MSPS must be less than or equal to KSPS.
<dt>NSPS
<dd>(INTEGER, input) is the second dimension of the &quot;sparse&quot; array of data in ZSPS. NSPS must be less than or equal to the declared second dimension of the array ZSPS.
<dt>RWRK
<dd>(REAL array, dimensioned LRWK, input/output) is the real work array.
<dt>LRWK
<dd>(INTEGER, input) is the length of RWRK.
<dt>IWRK
<dd>(INTEGER array, dimensioned LIWK, input/output) is the integer work array.
<dt>LIWK
<dd>(INTEGER, input) is the length of IWRK.
<dt>ZDAT
<dd>(REAL array, dimensioned LZDT, output) is the array in which the interpolated &quot;dense&quot; array of data is to be returned. The dimensions of the interpolated array may be supplied by the user or determined by Conpack, depending on the value of the parameter 'ZDS'. Note that, if Conpack determines the dimensions of the &quot;dense&quot; array, it will attempt to use an aspect ratio which is close to that implied by the value of the ratio
<dl COMPACT><dd>(XSPS(MSPS)<a HREF="/docs/linux/man/1--xsps/">-XSPS</a>(1))/(YSPS(NSPS)<a HREF="/docs/linux/man/1--ysps/">-YSPS</a>(1))</dl><dt>LZDT
<dd>(INTEGER, input) is the length of ZDAT.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions, with the following exceptions: 

<dl COMPACT><dt>zsps(l,ksps)
<dd>Dimensioned l by ksps, where l &le; nsps.
<dt>ksps
<dd>The second dimension of the array zsps.
<dt>msps
<dd>The second dimension of the sparse array of data in zsps. msps &le; ksps.
<dt>nsps
<dd>The first dimension of the sparse array of data in zsps. nsps &le; l, the declared first dimension of the array zsps.</dl><h2>Usage</h2>CPSPS2 performs the same functions as CPRECT, but, in addition, it interpolates from a sparse array of data to a dense array of data. CPSPS2 does this by using the routines SURF1 and SURF2, from the package Fitpack, by Alan K. Cline, to fit bicubic splines under tension to the sparse array of data and to compute the dense grid of data that is returned to you. The tension on the spline surfaces is specified by the parameter 'T3D'. By default, CPSPS2 selects the dimensions of the dense array of data; if desired, you can specify these dimensions by setting the parameter 'ZDS' non-zero and the parameters 'ZD1', 'ZDM', and 'ZDN' to the desired values. In either case, once 'ZD1', 'ZDM', and 'ZDN' are set, they should not be reset by you until the contour plot is complete and a different contour plot is to be drawn. 

 Because the routines SURF1 and SURF2 do not have a built-in special value feature, if the special value parameter 'SPV' is set non-zero and the sparse array contains occurrences of that value, special action must be taken. The indices of the special values in the sparse array are saved in a part of the integer workspace array; the special values are then replaced by values interpolated from adjacent grid points and the resulting array is used to obtain the dense array; then, the special values in the sparse array are restored and the corresponding elements of the dense array are also given the special value.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: ccpsps2.
<h2>Access</h2>To use CPSPS2 or c_cpsps2, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
