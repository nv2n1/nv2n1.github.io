---
title: "ncl_cppklb(3)"
name: "ncl_cppklb"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cppklb/"
---

CPPKLB - Picks a set of labels for labeled contour levels. 

<h2>Synopsis</h2>CALL CPPKLB (ZDAT, RWRK, IWRK)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cppklb (float *zdat, float *rwrk, int *iwrk)
<h2>Description</h2>All three arguments are arrays used in the last call to CPRECT, CPSPS1, or CPSPS2, the contents of which must not have been changed since that call.
<dl COMPACT><dt>ZDAT
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input) is the data array.
<dt>RWRK
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the real workspace array.
<dt>IWRK
<dd>(INTEGER array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the integer workspace array.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>Normally, CPPKLB is called by Conpack when labels for the contour levels are needed. You can call CPPKLB directly (after the initialization call to CPRECT, CPSPS1 or CPSPS2) when you want to modify the resulting parameter arrays that specify the labels. 

 If the constant-field-flag 'CFF' is non-zero, indicating that, during the last call to CPRECT, CPSPS1, or CPSPS2, the data were found to be essentially constant, CPPKLB does nothing. Otherwise, CPPKLB examines the first 'NCL' elements of the parameter array 'CLV', which defines the contour levels, and the associated parameter arrays, looking for levels that are to be labeled ('CLU' = 2 or 3) for which no label is specified (the associated element of 'LLT' is ' ', a single blank.) If any such levels are found, labels are generated for them. 

 The scale factor 'SFU' may be set as a byproduct of choosing the labels. See the description of the parameters 'SFU' (scale factor used) and 'SFS' (scale factor selector) in the conpack_params man page. 

 After calling CPPKLB, a user program may examine the generated labels and change them in various ways.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: ccpklb.
<h2>Access</h2>To use CPPKLB or c_cppklb, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
