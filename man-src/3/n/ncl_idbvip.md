---
title: "ncl_idbvip(3)"
name: "ncl_idbvip"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_idbvip/"
---

IDBVIP - produces interpolated values at points (XI(I), YI(I)), I=1,...,NIP. This is useful for filling in missing data points on a grid. 

<h2>Synopsis</h2>CALL IDBVIP (MD,NDP,XD,YD,ZD,NIP,XI,YI,ZI,IWK,WK)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_idbvip (int md, int ndp, float *xd, float *yd, 
 float *zd, int nip, float *xi, float *yi, float *zi, 
 int *iwk, float *wk)
<h2>Description</h2><dl COMPACT><dt>MD
<dd>Mode of computation (must be 1, 2, or 3, else an error return occurs.)
<dl COMPACT><dd><dl COMPACT><dt>1
<dd>If this is the first call to this subroutine, or if the value of NDP has been changed from the previous call, or if the contents of the XD or YD arrays have been changed from the previous call.
<dt>2
<dd>If the values of NDP and the XD and YD arrays are unchanged from the previous call, but new values for XI, YI are being used. If MD = 2 and NDP has been changed since the previous call to IDBVIP, an error return occurs.
<dt>3
<dd>If the values of NDP, NIP, XD, YD, XI, YI are unchanged from the previous call, i.e. if the only change on input to IDBVIP is in the ZD array. If MD=3 and NDP or NIP has been changed since the previous call to IDBVIP, an error return occurs.</dl></dl><dd>Between the call with MD=2 or MD=3 and the preceding call, the IWK and WK work arrays should not be disturbed.
<dt>NDP
<dd>Number of data points (must be 4 or greater, else an error return occurs).
<dt>XD
<dd>Array of dimension NDP containing the X coordinates of the data points.
<dt>YD
<dd>Array of dimension NDP containing the Y coordinates of the data points.
<dt>ZD
<dd>Array of dimension NDP containing the Z coordinates of the data points.
<dt>NIP
<dd>The number of output points at which interpolation is to be performed (must be 1 or greater, else an error return occurs).
<dt>XI
<dd>Array of dimension NIP containing the X coordinates of the output points.
<dt>YI
<dd>Array of dimension NIP containing the Y coordinates of the output points.
<dt>IWK
<dd>Integer work array of dimension at least 31*NDP + NIP.
<dt>WK
<dd>Real work array of dimension at least 8*NDP.
<dt>ZI
<dd>Array of dimension NIP where interpolated Z values are to be stored.</dl><h2></h2>Inadequate work space IWK and WK may may cause incorrect results. 

 The data points must be distinct and their projections in the X-Y plane must not be collinear, otherwise an error return occurs.
<h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>To use Bivar routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Access</h2>To use IDBVIP or c_idbvip, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the bivar man page for a description of all Bivar error messages and/or informational messages.
<h2>See Also</h2>Online: bivar, bivar_params, idsfft, idpltr, idgeti, idgetr, idseti, idsetr, ncarg_cbind
<h2>Acknowledgments</h2>Bivar was written by Hiroshi Akima in August 1975 and rewritten by him in late 1976. In 1989, a new version of Bivar, incorporating changes described in a Rocky Mountain Journal of Mathematics was obtained from Dr. Akima, and included in NCAR Graphics with his permission. In 1995, Dave Kennison incorporated the capability of doing linear interpolation and a different kind of triangulation, put in a parameter access interface, and wrote a routine to allow the triangulation to be plotted.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
