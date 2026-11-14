---
title: "ncl_idsfft(3)"
name: "ncl_idsfft"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_idsfft/"
---

IDSFFT - Performs smooth surface fitting when the projections of the data points in the X-Y plane are irregularly distributed in the plane. 

<h2>Synopsis</h2>&nbsp;<wbr>CALL IDSFFT&nbsp;<wbr>(MD, NDP, XD, YD, ZD, MREG, NREG, KREG, 
 + XREG, YREG, ZREG, IWK, WK)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_idsfft (int md, int ndp, float *xd, float *yd, 
 float *zd, int mreg, int nreg, int kreg, float *xreg, 
 float *yreg, float *zreg, int *iwk, float *wk)
<h2>Description</h2><dl COMPACT><dt>MD
<dd>(Integer, Input/output) - Mode of computation (must be 1, 2, or 3).
<dl COMPACT><dd><dl COMPACT><dt>1
<dd>If this is the first call to this subroutine, or if the value of NDP has been changed from the previous call, or if the contents of the XD or YD arrays have been changed from the previous call.
<dt>2
<dd>If the values of NDP and the XD, YD arrays are unchanged from the previous call, but new values for XREG, YREG are being used. If MD=2 and NDP has been changed since the previous call to IDSFFT, an error return occurs.
<dt>3
<dd>If the values of NDP, MREG, NREG, XD, YD, XREG, YREG are unchanged from the previous call, that is, if the only change on input to IDSFFT is in the ZD array. If MD=3 and NDP, MREG or NREG has been changed since the previous call to IDSFFT, an error return occurs. 

 Between the call with MD=2 or MD=3 and the preceding call, the IWK and WK work arrays should not be disturbed.</dl></dl><dt>NDP
<dd>(Integer, Input) - Number of random data points (must be 4 or greater).
<dt>XD(NDP)
<dd>(Real array, Input) - Array of dimension NDP containing the X coordinates of the data points.
<dt>YD(NDP)
<dd>(Real array, Input) - Array of dimension NDP containing the Y coordinates of the data points.
<dt>ZD(NDP)
<dd>(Real array, Input) - Array of dimension NDP containing the Z coordinates of the data points.
<dt>MREG
<dd>(Integer, Input) - Number of output grid points in the X-direction (must be 1 or greater).
<dt>NREG
<dd>(Integer, Input) - Number of output grid points in the Y-direction (must be 1 or greater).
<dt>KREG
<dd>(Integer, Input) - First dimension of ZREG as declared in the calling program. KREG must be greater than or equal to MREG, else an error return occurs.
<dt>XREG(MREG)
<dd>(Real array, Input) - Array of dimension MREG containing the X coordinates of the output grid points.
<dt>YREG(NREG)
<dd>(Real array, Input) - Array of dimension NREG containing the Y coordinates of the output grid points.
<dt>ZREG(KREG,NREG)
<dd>(Real array, Output) - Real, two-dimensional array of dimension (KREG,NREG), storing the interpolated Z values at the output grid points.
<dt>IWK(*)
<dd>(Integer array, Workspace) - Integer work array of dimension at least 31 * NDP + MREG * NREG.
<dt>WK(*)
<dd>(Real array, Workspace) - Real work array of dimension at least 6 * NDP.</dl><h2></h2>Inadequate work space IWK and WK may may cause incorrect results. 

 The data points must be distinct and their projections in the X-Y plane must not be collinear; otherwise, an error return occurs.
<h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN
<h2>Examples</h2>To use IDSFFT routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. 

 Use the ncargex command to see the following relevant examples: ccpcldm, ccpfil, ccplbam, ccpllb, ccpllc, ccplll, ccpllo, ccpllp, ccpllt, ccpllw, ccpnet, ccppc, ccppc1, ccppc2, ccppc3, ccppc4, ccprc, ccpscam, cidsfft, fsfsgfa, cbex01.
<h2>Access</h2>To use IDSFFT or c_idsfft, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the bivar man page for a description of all Bivar error messages and/or informational messages.
<h2>See Also</h2>Online: bivar, bivar_params, idbvip, idpltr, idgeti, idgetr, idseti, idsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Acknowledgments</h2>Bivar was written by Hiroshi Akima in August 1975 and rewritten by him in late 1976. In 1989, a new version of Bivar, incorporating changes described in a Rocky Mountain Journal of Mathematics was obtained from Dr. Akima, and included in NCAR Graphics with his permission. In 1995, Dave Kennison incorporated the capability of doing linear interpolation and a different kind of triangulation, put in a parameter access interface, and wrote a routine to allow the triangulation to be plotted.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
