---
title: "ncl_sfgetp(3)"
name: "ncl_sfgetp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_sfgetp/"
---

SFGETP - Used to retrieve the current dot pattern.

<h2>Synopsis</h2>

CALL SFGETP (IDP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_sfgetp (int idp[8][8])

<h2>Description</h2>

<dl><dt>IDP
<dd>(an output array of type INTEGER, dimensioned 8x8) contains 0s and 1s specifying the dot pattern currently contained in the internal array LDP. When dot fill is selected, each fill line is drawn using dots the same distance apart along the line as the lines are from each other. The dots thus fall at the intersection points of a square grid. Each dot is associated with a particular element of LDP. If that element is a 1, the dot is drawn; if it is a 0, the dot is not drawn. The association is done in such a way as to replicate the pattern specified by LDP across the entire filled area. 

 If the fill angle is 0 (the default), then incrementing the first subscript of LDP corresponds to a horizontal motion across the plot from left to right and incrementing the second subscript of LDP corresponds to a vertical motion across the plot from top to bottom. This allows the contents of IDP to be declared in a DATA statement which creates a &quot;picture&quot; of the pattern. For example, the FORTRAN statements 

<dl><dd>&nbsp;<wbr>DIMENSION IDP(8,8) 
 
&nbsp;<wbr>... 
 
&nbsp;<wbr>DATA IDP&nbsp;<wbr>/&nbsp;<wbr>0,0,0,0,0,0,0,0,&nbsp;<wbr> 
 + 0,1,1,1,1,1,1,0, 
 + 0,1,0,0,0,0,0,1, 
 + 0,1,0,0,0,0,0,1, 
 + 0,1,1,1,1,1,1,0, 
 + 0,1,0,0,0,1,0,0, 
 + 0,1,0,0,0,0,1,0, 
 + 0,1,0,0,0,0,0,1/</dl><dd>creates the letter &quot;R&quot;, with the correct orientation. 

 The default dot pattern consists of all 1s.</dl>

<h2>Usage</h2>

This routine allows you to retrieve the current value of Softfill's dot pattern. For a description of Softfill's dot pattern parameter, see the softfill_params man page.

<h2>Access</h2>

To use SFGETP or c_sfgetp, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: softfill, softfill_params, sfgetc, sfgeti, sfgetr, sfsetc, sfseti, sfsetp, sfsetr, sfsgfa, sfwrld, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
