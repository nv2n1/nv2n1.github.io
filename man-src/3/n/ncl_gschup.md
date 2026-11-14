---
title: "ncl_gschup(3)"
name: "ncl_gschup"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gschup/"
---

GSCHUP (Set character up vector) - specifies the angle at which subsequent text is to be drawn with GTX.
<h2>Synopsis</h2>CALL GSCHUP (CHUX, CHUY)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_char_up_vec(const Gvec *char_up_vec);
<h2>Description</h2><dl COMPACT><dt>CHUX
<dd>(Real, Input) - Gives the X (horizontal) world coordinate of a vector.
<dt>CHUY
<dd>(Real, Input) - Gives the Y (vertical) world coordinate of a vector.</dl><h2>Usage</h2>The coordinates (CHUX, CHUY) relative to the point (0.,0.) establish a vector direction. This direction specifies the up direction of individual characters. This direction also specifies the orientation of a text string in that the characters in a string are placed along a line perpendicular to the character up vector. By default the character up vector is (0.,1.) so that characters are drawn in their normal horizontal orientation. The magnitude of the up vector is not used so that (0.,23.) is the same as (0.,1.).
<h2>Examples</h2><pre> CALL GSCHUP(-1.,0.)</pre>would specify the character up vector as (-1.,0.) and subsequent text written with GTX would be rotated 90 degrees from normal and would be appropriate for a Y-axis label. 

 <pre> CALL GSCHUP(1.,1.)</pre>would specify the character up vector as (1.,1.) and subsequent text written with GTX would be rotated -45 degress from normal.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxal, gstxfp, gschh, gschsp, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, gset_char_up_vec 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
