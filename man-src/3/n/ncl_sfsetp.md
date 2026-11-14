---
title: "ncl_sfsetp(3)"
name: "ncl_sfsetp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_sfsetp/"
---

SFSETP - Defines a new dot pattern.

<h2>Synopsis</h2>

CALL SFSETP (IDP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_sfsetp (int idp[8][8])

<h2>Description</h2>

<dl><dt>IDP
<dd>(an input array of type INTEGER, dimensioned 8x8) contains 0s and 1s specifying the dot pattern to be transferred to the internal array LDP for use by SFWRLD and SFNORM. When dot fill is selected, each fill line is drawn using dots the same distance apart along the line as the lines are from each other. The dots thus fall at the intersection points of a square grid. Each dot is associated with a particular element of LDP. If that element is a 1, the dot is drawn; if it is a 0, the dot is not drawn. The association is done in such a way as to replicate the pattern specified by LDP across the entire filled area. 

 If the fill angle is 0 (the default), then incrementing the first subscript of LDP corresponds to a horizontal motion across the plot from left to right and incrementing the second subscript of LDP corresponds to a vertical motion across the plot from top to bottom. This allows the contents of IDP to be declared in a DATA statement which creates a &quot;picture&quot; of the pattern. For example, the FORTRAN statements 

<dl><dd>&nbsp;<wbr>DIMENSION IDP(8,8) 
 
&nbsp;<wbr>... 
 
&nbsp;<wbr>DATA IDP&nbsp;<wbr>/&nbsp;<wbr>0,0,0,0,0,0,0,0, 
 + 0,1,1,1,1,1,1,0, 
 + 0,1,0,0,0,0,0,1, 
 + 0,1,0,0,0,0,0,1, 
 + 0,1,1,1,1,1,1,0, 
 + 0,1,0,0,0,1,0,0, 
 + 0,1,0,0,0,0,1,0, 
 + 0,1,0,0,0,0,0,1/</dl><dd>creates the letter &quot;R&quot;, with the correct orientation. 

 The contents of the array IDP are transferred to the internal array LDP. The new dot pattern is used until a subsequent call to SFSETP changes the contents of LDP again. 

 The default dot pattern consists of all 1s.</dl>

<h2>C-Binding Description</h2>

The C-binding argument description is the same as the FORTRAN argument description.

<h2>Usage</h2>

This routine allows you to set the current value of Softfill's dot pattern. For a description of Softfill's dot pattern parameter, see the softfill_params man page.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: sfex01, tsoftf.

<h2>Access</h2>

To use SFSETP or c_sfsetp, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: softfill, softfill_params, sfgetc, sfgeti, sfgetp, sfgetr, sfsetc, sfseti, sfsetr, sfsgfa, sfwrld, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
