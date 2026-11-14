---
title: "ncl_gactm(3)"
name: "ncl_gactm"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gactm/"
---

GACTM (Accumulate transformation matrix) - Constructs a GKS segment transformation matrix by starting with an existing matrix and composing it with a shift vector, a rotation angle, and X and Y scale factors to create a new transformation matrix. The rotation and scaling are done with respect to a user-defined fixed point.
<h2>Synopsis</h2>CALL GACTM(MINP,X0,Y0,DX,DY,PHI,FX,FY,SW,MOUT)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gaccum_tran_matrix(const Gtran_matrix t_matrix, const Gpoint *point, const Gvec *shift, Gdouble angle, const Gvec *scale, Gcoord_switch coord_switch, Gtran_matrix tran_matrix);
<h2>Description</h2><dl COMPACT><dt>MINP
<dd>(Real, Input) - A 2x3 GKS transformation matrix.
<dt>X0
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
<dd>(Real, Output) - A 2x3 array that contains the GKS transformation matrix in a form that can be used as input to other GKS functions such as GSSGT. This matrix is constructed by composing the scale, rotate, and shift input, described above, with the original input matrix MINP.</dl><h2>Usage</h2>If world coordinates are used, the shift vector and the fixed point are transformed by the current normalization transformation. 

 The order in which the transformations are applied is: input matrix, scale, rotate, and shift. 

 Elements MOUT(1,3) and MOUT(2,3) are in normalized device coordinates and the other elements of MOUT are unitless. 

 GACTM can be used to construct more general transformation matrices than GEVTM. The most common usage of GACTM is to change the order in which the operations of scale, rotate, and shift are applied (which is fixed in GEVTM). The example below shows how to construct a transformation matrix that shifts first and then rotates.
<h2>Example</h2>Assuming that the input matrix TIN is initially the identity, the following code <pre> PI = 3.1415926
 CALL GACTM(TIN,.5,.5,.25,0.,0.,1.,1.,0,TOUT)
 DO 20 I=1,2
 DO 30 J=1,3
 TIN(I,J) = TOUT(I,J)
 30 CONTINUE
 20 CONTINUE
 CALL GACTM(TIN,.5,.5,0.,0.,45.*PI/180.,1.,1.,0,TOUT)</pre>would produce a transformation matrix in TOUT that would shift by (.25,0.) first, and then rotate by 45 degrees.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gevtm, gclsg, gcrsg, gcsgwk, gdsg, gqopsg, gqsgus, gssgt., gaccum_tran_matrix 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
