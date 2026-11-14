---
title: "ncl_gaccum_tran_matrix(3)"
name: "ncl_gaccum_tran_matrix"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gaccum_tran_matrix/"
description: "gaccum_tran_matrix (Accumulate transformation matrix) – Constructs a GKS segment transformation matrix by starting with an existing matrix and composing it with a shift vector, a rotation angle, an..."
---

<p>gaccum_tran_matrix (Accumulate transformation matrix) &#8211; Constructs a GKS segment transformation matrix by starting with an existing matrix and composing it with a shift vector, a rotation angle, and X and Y scale factors to create a new transformation matrix. The rotation and scaling are done with respect to a user-defined fixed point.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gaccum_tran_matrix(const Gtran_matrix t_matrix, const Gpoint *point, const Gvec *shift, Gdouble angle, const Gvec *scale, Gcoord_switch coord_switch, Gtran_matrix tran_matrix);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>t_matrix</p>
<dd>(Gfloat, Input) &#8211; A 2&#215;3 GKS transformation matrix.</p>
<dt>point.x</p>
<dd>(Gfloat, Input) &#8211; X coordinate value for a fixed point to be used for the scaling and rotation parts of the output transformation. point.x is either in world coordinates or normalized device coordinates depending on the setting of the argument coord_switch described below.</p>
<dt>point.y</p>
<dd>(Gfloat, Input) &#8211; Y coordinate value for a fixed point to be used for the scaling and rotation parts of the output transformation. point.y is either in world coordinates or normalized device coordinates depending on the setting of the argument coord_switch described below.</p>
<dt>shift.delta_x</p>
<dd>(Gfloat, Input) &#8211; The X component of a shift vector to be used for the scaling part of the output transformation. shift.delta_x is either in world coordinates or normalized device coordinates depending on the setting of the argument coord_switch described below.</p>
<dt>shift.delta_y</p>
<dd>(Gfloat, Input) &#8211; The Y component of a shift vector to be used for the scaling part of the output transformation. shift.delta_y is either in world coordinates or normalized device coordinates depending on the setting of the argument coord_switch described below.</p>
<dt>angle</p>
<dd>(Input) &#8211; The rotation angle, in radians, to be used for the rotation part of the output transformation.</p>
<dt>scale.delta_x</p>
<dd>(Gfloat, Input) &#8211; X coordinate scale factor to be used in the scaling part of the output transformation.</p>
<dt>scale.delta_y</p>
<dd>(Gfloat, Input) &#8211; Y coordinate scale factor to be used in the scaling part of the output transformation.</p>
<dt>coord_switch</p>
<dd>(Input) &#8211; A coordinate switch to indicate whether the values for the arguments point and shift (described above) are in world coordinates or normalized device coordinates. Possible values include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GCOORD_WC</p>
<dd>World coordinates</p>
<dt>GCOORD_NDC</p>
<dd>Normalized device coordinates</p>
<dt>tran_matrix</p>
<dd>(Gfloat, Output) &#8211; A 2&#215;3 array that contains the GKS transformation matrix in a form that can be used as input to other GKS functions such as gset_seg_tran. This matrix is constructed by composing the scale, rotate, and shift input, described above, with the original input matrix t_matrix.</dl>
</dl>
</dl>
<h2>Usage</h2>
<p>If world coordinates are used, the shift vector and the fixed point are transformed by the current normalization transformation. </p>
<p> The order in which the transformations are applied is: input matrix, scale, rotate, and shift. </p>
<p> Elements tran_matrix[0][2] and tran_matrix[1][2] are in normalized device coordinates and the other elements of tran_matrix are unitless. </p>
<p> gaccum_tran_matrix can be used to construct more general transformation matrices than geval_tran_matrix. The most common usage of gaccum_tran_matrix is to change the order in which the operations of scale, rotate, and shift are applied (which is fixed in geval_tran_matrix). The example below shows how to construct a transformation matrix that shifts first and then rotates.</p>
<h2>Example</h2>
<p>Assuming that the input matrix t_matrix is initially the identity, the following code </p>
<pre> pi = 3.1415926;
 point.x = point.y = 0.5;
 shift.delta_x = 0.25;
 shift.delta_y = 0.;
 scale.delta_x = 1.0;
 scale.delta_y = 1.0;
 gaccum_tran_matrix(t_matrix,&amp;point,&amp;shift,0.,&amp;scale,GCOORD_WC,tout);
 for( i = 0; i &lt; 2; i++ ) {
 for( j = 0; j &lt; 3; j++ ) {
 t_matrix[i][j] = tout[i][j];
 }
 }
 shift.delta_x = 0.;
 shift.delta_y = 0.;
 gaccum_tran_matrix(t_matrix,&amp;point,&amp;shift,45.*pi/180.,&amp;scale,GCOORD_WC,tout);</pre>
<p>would produce a transformation matrix in tout that would shift by (.25,0.) first, and then rotate by 45 degrees.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>geval_tran_matrix(3NCARG),</code> <code>gclose_seg(3NCARG),</code> <code>gcreate_seg(3NCARG),</code> <code>gcopy_seg_ws(3NCARG),</code> <code>gdel_seg(3NCARG),</code> <code>ginq_name_open_seg(3NCARG),</code> <code>ginq_set_seg_names(3NCARG),</code> <code>gset_seg_tran(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
