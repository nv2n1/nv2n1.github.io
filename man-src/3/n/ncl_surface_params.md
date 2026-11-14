---
title: "ncl_surface_params(3)"
name: "ncl_surface_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_surface_params/"
---

Surface_params - This document briefly describes the Surface internal parameters.

<h2>Description</h2>

There are no parameter access routines available for the Surface utility. Therefore, parameters must be set through the common blocks SRFBLK and SRFIP1. 

 In order to access the internal parameters, you must declare the following common blocks for the Surface parameters in your code. 

 <pre> COMMON /SRFBLK/ LIMU(1024) ,LIML(1024) ,CL(41) ,NCL ,
1 LL ,FACT ,IROT ,NDRZ ,
2 NUPPER ,NRSWT ,BIGD ,UMIN ,
3 UMAX ,VMIN ,VMAX ,RZERO ,
4 IOFFP ,NSPVAL ,SPVAL ,BIGEST
 COMMON /SRFIP1/ IFR ,ISTP ,IROTS ,IDRX ,
1 IDRY ,IDRZ ,IUPPER ,ISKIRT ,
2 NCLA ,THETA ,HSKIRT ,CHI ,
3 CLO ,CINC ,ISPVAL</pre>Note that not all of the variables declared above are considered user-modifiable parameters. Definitions of only user-modifiable parameters follow: 

 <pre><dl><dt>IFR<dd>-1 Call FRAME first.
<br>
 0 Do not call FRAME.
<br>
+1 Call FRAME when done (default).
<dt>ISTP<dd>-1 Draws alternating frames, slightly offset 
<br>
 (For movies, IROTS = 0).
 0 Blank frame between for stereo slide (IROTS = 1)
<br>
 (default).
<br>
+1 Both on same frame. (left picture to left 
<br>
 side. IROTS = 0).
 
<dt>IROTS<dd>0 +Z in vertical plotting direction (CINE mode)
<br>
 (default).
<br>
+1 +Z in horizontal plotting direction (COMIC mode).
<dt>IDRX<dd>+1 Draw lines of constant X (default).
<br>
 0 Do not.
<dt>IDRY<dd>+1 Draw lines of constant Y (default).
<br>
 0 Do not.
<dt>IDRZ<dd>+1 Draw lines of constant Z (contour lines).
<br>
 0 Do not (default).
<dt>IUPPER<dd>+1 Draw upper side of surface.
<br>
 0 Draw both sides (default).
<br>
-1 Draw lower side.
<dt>ISKIRT<dd>+1 Draw a skirt around the surface.
<br>
 BOTTOM = HSKIRT.
<br>
 0 Do not (default).
<dt>NCLA<dd>Approximate number of levels of constant Z
<br>
 that are drawn if levels are not specified.
<br>
 40 is the maximum and 6 is the default.
<dt>THETA<dd>The angle in radians between eyes for stereo pairs.
<br>
 The default is .02.
<dt>HSKIRT<dd>Height of skirt (if ISKIRT = 1). The default is 0.
<dt>CHI<dd>Highest level of constant Z. The default is 0.
<dt>CLO<dd>Lowest level of constant Z. The default is 0.
<dt>CINC<dd>Increment between levels. The default is 0.
<dt>IOFFP<dd>Flag to control the use of the special value feature. Do
<br>
 not have both IOFFP=1 and ISKIRT=1.
<br>
 0 Feature not in use (default).
<br>
+1 Feature in use. No lines are drawn to data points
<br>
 that are equal to SPVAL.
<dt>SPVAL<dd>Special value used to mark unknown data when 
<br>
 IOFFP=1. The default is 0.</pre></dl>

<h2>See Also</h2>

Online: surface, ezsrfc, pwrzs, setr, srface. ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
