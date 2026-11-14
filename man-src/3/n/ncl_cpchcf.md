---
title: "ncl_cpchcf(3)"
name: "ncl_cpchcf"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpchcf/"
---

CPCHCF - Called by Conpack routines when a constant field is detected. The default version does nothing. A user-written version may be supplied to provide control as the constant-field message is drawn. 

<h2>Synopsis</h2>CALL CPCHCF (IFLG)
<h2>Description</h2><dl COMPACT><dt>IFLG
<dd>(INTEGER, input) is positive if an action is about to be taken, negative if an action has just been completed. The action in question is defined by the absolute value of IFLG, as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The value 1 implies the determination of the size of the label (by means of a call to PLCHHQ, in the package Plotchar, with ANGD=360.).
<dt>&bull;
<dd>The value 2 implies the filling of the box around the label, which is done before the drawing of the label itself.
<dt>&bull;
<dd>The value 3 implies the drawing of the label (by means of a call to PLCHHQ, in the package Plotchar).
<dt>&bull;
<dd>The value 4 implies the drawing of the box around the label, which is done after the drawing of the label itself.</dl></dl>
</dl><h2>Usage</h2>The routine CPCHCF is not to be called by the user. It is called several times by Conpack while a constant-field label is being drawn. The default version of CPCHCF does nothing. A user-supplied replacement may change attributes such as color and line width (by calling the SPPS routine SETUSV or the appropriate GKS routines). The text of the label being written may be retrieved by means of a &quot;CALL CPGETC ('CTM',CVAL)&quot;. The text of the label may be changed by means of a &quot;CALL CPSETC ('CTM',CVAL)&quot;; this should only be done during a call with IFLG = 1 or 3 and, if it is done for one of those two values, it should also be done for the other. When CPCHCF is called, the parameter 'ZDV' will have been set to the value of the field; its value may be retrieved and used by CPCHCF.
<h2>Access</h2>To use CPCHCF, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: conpack, cpback, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsprs, cpsps1, cpsps2, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
