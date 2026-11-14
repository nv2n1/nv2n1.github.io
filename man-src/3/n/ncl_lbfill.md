---
title: "ncl_lbfill(3)"
name: "ncl_lbfill"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_lbfill/"
---

LBFILL - A routine that is called by LBLBAR (when the argument IFTP is non-zero) to fill portions of the bar. The default version of this routine does color fill by calling GSFACI and GFA. A user-written version may be supplied to do a different kind of fill. 

<h2>Synopsis</h2>CALL LBFILL (IFTP, XCRA, YCRA, NCRA, INDX)
<h2>Description</h2><dl COMPACT><dt>IFTP
<dd>(an input expression of type INTEGER) is the value of the argument IFTP from the user's call to LBLBAR.
<dt>XCRA, YCRA
<dd>(input arrays of type REAL) are real arrays containing the X and Y coordinates of five points defining a rectangular box which is to be filled in some manner. The fifth point defined by these arrays will always be a duplicate of the first.
<dt>NCRA
<dd>(an input expression of type INTEGER) is the number of points defining the rectangular box. Its value will always be five.
<dt>INDX
<dd>(an input expression of type INTEGER) is one of the indices from the array LFIN, in the user's call to LBLBAR. Its value may be used as a color index or as a pattern selector.</dl><h2>Usage</h2>This routine is called by LBLBAR when LBLBAR's argument IFTP is non-zero. LBFILL is called once for each sub-box in the label bar, using a statement of the form: 

<dl COMPACT><dd>CALL LBFILL (IFTP,XCRA,YCRA,NCRA,INDX)</dl>
 

 and is expected to fill the sub-box defined by its arguments. The default version of the routine looks like this: 

<dl COMPACT><dd>SUBROUTINE LBFILL (IFTP,XCRA,YCRA,NCRA,INDX)
<dl COMPACT><dd>DIMENSION XCRA(*),YCRA(*) 
 CALL GSFACI (INDX) 
 CALL GFA (NCRA-1,XCRA,YCRA) 
 RETURN</dl>
 END</dl>
 

 This version does color fill of the box, using the last argument as a color index. The user may replace this routine with a version that does any desired sort of fill; usually, this can be done by simply compiling the desired version, so that the default one from the package will not be loaded.
<h2>Access</h2>To use LBFILL, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: labelbar, labelbar_params, lbgeti, lbgetr, lblbar, lbseti, lbsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
