---
title: "ncl_polypack(3)"
name: "ncl_polypack"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_polypack/"
---

Polypack - a set of routines allowing polygons to be manipulated in various ways. Each of the six principal routines is given a &quot;clip&quot; polygon, a &quot;subject&quot; polygon, and a workspace; it operates on the two polygons in some way to create either a derivative polygon or a set of trapezoids representing the interior of that derivative polygon and then passes these on to a user-specified processing routine.

<h2>Synopsis</h2>

PPDIPO - generates and returns the boundary of the &quot;difference&quot; polygon, which consists of all points that are inside the subject polygon but not inside the clip polygon. 

 PPINPO - generates and returns the boundary of the &quot;intersection&quot; polygon, which consists of all points that are inside both the clip polygon and the subject polygon. 

 PPUNPO - generates and returns the boundary of the &quot;union&quot; polygon, which consists of all points that are inside either or both of the clip polygon and the subject polygon. 

 PPDITR - generates and returns a set of trapezoids representing the interior of the &quot;difference&quot; polygon, which consists of all points that are inside the subject polygon but not inside the clip polygon. 

 PPINTR - generates and returns a set of trapezoids representing the interior of the &quot;intersection&quot; polygon, which consists of all points that are inside both the clip polygon and the subject polygon. 

 PPUNTR - generates and returns a set of trapezoids representing the interior of the &quot;union&quot; polygon, which consists of all points that are inside either or both of the clip polygon and the subject polygon. 

 PPPPAP - can be called to preprocess a polygon in such a way as to remove certain peculiarities that can cause minor cosmetic errors in the output from the routines that return trapezoids. 

 PPPLCL - clips a polyline against a clipping rectangle. It is intended that, eventually, there should be a better routine that will clip a polyline against an arbitrary polygon, but that routine has not yet been written.

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 c_ppdipo 
 c_ppditr 
 c_ppinpo 
 c_ppintr 
 c_ppplcl 
 c_ppppap 
 c_ppunpo 
 c_ppuntr

<h2>Access</h2>

To use Polypack routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

None. All error conditions in Polypack routines are reported by means of an error-flag argument.

<h2>See Also</h2>

Online: ppdipo, ppditr, ppinpo, ppintr, ppplcl, ppppap, ppunpo, ppuntr, ncarg_cbind. 

 Hardcopy: None.

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
