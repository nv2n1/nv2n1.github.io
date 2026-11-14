---
title: "ncl_gevtm(3)"
name: "ncl_gevtm"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gevtm/"
---

GEVTM (Evaluate transformation matrix) - Constructs a GKS segment transformation matrix starting from a given point, a shift vector, a rotation angle, and X and Y scale factors.
<h2>Synopsis</h2>CALL GEVTM(X0,Y0,DX,DY,PHI,FX,FY,SW,MOUT)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void geval_tran_matrix(const Gpoint *point, const Gvec *shift, Gdouble angle, const Gvec *scale, Gcoord_switch coord_switch, Gtran_matrix tran_matrix);
<h2>Description</h2><dl COMPACT><dt>X0
<dd>(Real, Input) - An X coordinate value for a fixed point to be used for the scaling and rotation parts of the output transformation. X is either in world coordinates or normalized device coordinates depending on the setting of the argument SW described below.
<dt>Y0
<dd>(Real, Input) - A Y coordinate value for a fixed point to be used for the scaling and rotation parts of the output transformation. Y is either in world coordinates or normalized device coordinates depending on the setting of the argument SW described below.
<dt>DX
<dd>(Real, Input) - The X component of a shift vector to be used for the scaling part of the output transformation. DX is either in world coordinates or normalized device coordinates depending on the setting of the argument SW described below.
<dt>DY
<dd>(Real, Input) - The Y component of a shift vector to be used for the scaling part of the output transformation. DY is either in world coordinates or normalized device coordinates depending on the setting of the argument SW described below.
<dt>PHI
<dd>(Real, Input) - The rotation angle, in radians, to be used for the rotation part of the output transformation.
<dt>FX
<dd>(Real, Input) - An X coordinate scale factor to be used in the scaling part of the output transformation.
<dt>FY
<dd>(Real, Input) - A Y coordinate scale factor to be used in the scaling part of the output transformation.
<dt>SW
<dd>(Integer, Input) - A coordinate switch to indicate whether the values for the arguments X0, Y0, DX, and DY (described above) are in world coordinates or normalized device coordinates. SW=0 indicates world coordinates and SW=1 indicates normalized device coordinates.
<dt>MOUT
<dd>(Real, Output) - A 2x3 array that contains the GKS transformation matrix in a form that can be used as input to other GKS functions such as GSSGT.</dl><h2>Usage</h2>If world coordinates are used, the shift vector and the fixed point are transformed by the current normalization transformation. 

 The order of the transformation operations as built into the output matrix is: scale (relative to the fixed point); rotate (relative to the fixed point; shift. 

 Elements MOUT(1,3) and MOUT(2,3) are in normalized device coordinates and the other elements of MOUT are unitless.
<h2>Example</h2>The following code <pre> PI = 3.1415926
 CALL GEVTM(.5,.5,.25,0.,45.*PI/180.,.5,1.5,0,TM)</pre>would produce a transformation matrix in TM that would: scale the X coordinates by .5, scale the Y coordinates by 1.5 (relative to the fixed point of (.5,.5) ); rotate by 45 degrees (relative to the fixed point (.5,.5) ); and shift by .25 in X and 0. in Y. The input values for the fixed point and shift vector are in world coordintes.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gactm, gclsg, gcrsg, gcsgwk, gdsg, gqopsg, gqsgus, gssgt., geval_tran_matrix 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
