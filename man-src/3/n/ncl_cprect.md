---
title: "ncl_cprect(3)"
name: "ncl_cprect"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cprect/"
---

CPRECT - Initializes the contouring of a rectangular array of data. 

<h2>Synopsis</h2>CALL CPRECT (ZDAT, KZDT, MZDT, NZDT, RWRK, LRWK, IWRK, LIWK)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cprect (float *zdat, int kzdt, int mzdt, int nzdt, 
 float *rwrk, int lrwk, int *iwrk, int liwk)
<h2>Description</h2><dl COMPACT><dt>ZDAT
<dd>(REAL array, dimensioned KZDT x n, where &quot;n&quot; is greater than or equal to NZDT, input) is the array of data to be contoured.
<dt>KZDT
<dd>(INTEGER, input) is the first dimension of the array ZDAT.
<dt>MZDT
<dd>(INTEGER, input) is the first dimension of the array of data in ZDAT. MZDT must be less than or equal to KZDT.
<dt>NZDT
<dd>(INTEGER, input) is the second dimension of the array of data in ZDAT. NZDT must be less than or equal to the declared second dimension of the array ZDAT.
<dt>RWRK
<dd>(REAL array, dimensioned LRWK, input/output) is the real work array.
<dt>LRWK
<dd>(INTEGER, input) is the length of RWRK.
<dt>IWRK
<dd>(INTEGER array, dimensioned LIWK, input/output) is the integer work array.
<dt>LIWK
<dd>(INTEGER, input) is the length of IWRK.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exceptions:
<dl COMPACT><dt>zdat(l,kzdt)
<dd>zdat is dimensioned l by kzdt, where l &ge; nzdt.
<dt>kzdt
<dd>The second dimension of the array zdat.
<dt>mzdt
<dd>The second dimension of the array of data in zdat. mzdt &le; kzdt.
<dt>nzdt
<dd>The first dimension of the array of data in zdat. nzdt &le; l, where l is the declared first dimension of the array zdat.</dl><h2>Usage</h2>The routine CPRECT is called to initialize the process of drawing a contour plot from a rectangular array of data. The arguments define the data array, a real workspace array, and an integer workspace array. The dimensions of all the arrays are transferred to variables in COMMON, so that, in calls to other Conpack routines, those dimensions may be omitted. 

 CPRECT initializes the internal pointers that manage workspace use; also, it decides the appropriate ranges of X and Y coordinates for drawing contour lines and positioning labels. 

 If Conpack is to call SET, appropriate arguments are determined and SET is called; otherwise, GETSET is called to retrieve the arguments from the user's call to SET. 

 The list of label positions (if any) left over from previous calls to the package is discarded. 

 If contour levels are to be chosen by Conpack, 'NCL' is zeroed so that the levels will be chosen when they are needed. 

 The minimum and maximum values in the data array are located and it is decided whether the data are essentially constant. 

 Numeric-label parameters that depend on the range of values in the data array are initialized. 

 A scale factor may be chosen.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: caredg, ccpback, ccpcff, ccpcfx, ccpcica, ccpci, ccpcis, ccpcit, ccpclc, ccpcld, ccpcldm, ccpcldr, ccpcll, ccpclu, ccpdflt, ccpfil, ccpga, ccphand, ccphcf, ccphl, ccphlt, ccpila, ccpils, ccpilt, ccpklb, ccplbam, ccplbdr, ccpllb, ccpllc, ccplll, ccpllo, ccpllp, ccpllt, ccpmap, ccpmovi, ccpmpxy, ccpncls, ccpnet, ccpnof, ccpnsd, ccppc, ccppc1, ccppc2, ccppc3, ccppc4, ccppkcl, ccppole, ccprc, ccprect, ccprwc, ccprwu, ccpscam, ccpset, ccpspv, ccpt2d, ccptitle, ccpvp, ccpvs, cidsfft, colcon, cpex01, cpex02, cpex03, cpex04, cpex05, cpex06, cpex07, cpex08, cbex01, vvex01, tconpa, fcover, ffex03, ffex05, fsfsgfa.
<h2>Access</h2>To use CPRECT or c_cprect, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
