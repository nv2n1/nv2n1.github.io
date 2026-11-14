---
title: "ncl_tick3(3)"
name: "ncl_tick3"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tick3/"
---

TICK43 - Gives user control of tick mark length in PERIM3. 

 NOTE: At one time, the Threed routine TICK3 was used to set tick-mark length. TICK3 has been superseded by TICK43 and is therefore considered obsolete. If you call TICK3, it will call TICK43 for you. The statement
<dl><dd>CALL TICK3 (MAJOR,MINOR)</dl>
 

 should be replaced by the equivalent statement
<dl><dd>CALL TICK43 (MAJOR,MINOR,MAJOR,MINOR,MAJOR,MINOR)</dl>

<h2>Synopsis</h2>

CALL TICK43 (MAJORU,MINORU,MAJORV,MINORV,MAJORW,MINORW)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tick43 (int majoru, int minoru, int majorv, int minorv, 
 int majorw, int minorw)

<h2>Description</h2>

<dl><dt>MAJORU
<dd>(an input expression of type INTEGER) specifies the length of major ticks to be used on perimeter sides that are parallel to the U axis.
<dt>MINORU
<dd>(an input expression of type INTEGER) specifies the length of minor ticks to be used on perimeter sides that are parallel to the U axis.
<dt>MAJORV,MINORV
<dd>(input expressions of type INTEGER) specify the lengths of major and minor ticks for perimeter sides parallel to the V axis.
<dt>MAJORW,MINORW
<dd>(input expressions of type INTEGER) specify the lengths of major and minor ticks for perimeter sides parallel to the W axis.</dl>
 

 All tick lengths are specified as integers between 0 and 1024. The value &quot;n&quot; produces a tick that is n/1024ths as long as the longest side of the box defined by the arguments UMIN, UMAX, VMIN, VMAX, WMIN, and WMAX in the last call to SET3. The default values are 12 for a major tick and 8 for a minor tick.

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TICK43 or c_tick43, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: threed, curve3, fence3, frst3, line3, perim3, point3, psym3, pwrz, pwrzt, set3, threed, tick3, vect3, ncarg_cbind.

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
