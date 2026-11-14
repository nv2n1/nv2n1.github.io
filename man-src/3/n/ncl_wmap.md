---
title: "ncl_wmap(3)"
name: "ncl_wmap"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmap/"
---

Wmap - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Synopsis</h2>

WMBARB - Plots wind barbs. 

 WMDFLT - Returns all values of all internal parameters to their defaults. 

 WMDRFT - Draws weather fronts. 

 WMDRRG - Draws weather regions (indicating &quot;snow&quot;, &quot;rain&quot;, etc.) or regions of solid color indicating temperature regions. 

 WMGETC - Retrieves the character value of a specified internal parameter. 

 WMGETI - Retrieves the integer value of a specified internal parameter. 

 WMGETR - Retrieves the real value of a specified internal parameter. 

 WMLABC - Plots city names and daily hi/lows. 

 WMLABS - Plots special symbols and daily weather icons. 

 WMLABT - Plots regional temperature labels. 

 WMLABW - Plots regional weather labels. 

 WMLGND - Plots weather map legends. 

 WMSETC - Gives a new character value to a specified internal parameter. 

 WMSETI - Gives a new integer value to a specified internal parameter. 

 WMSETR - Gives a new real value to a specified internal parameter. 

 WMSTNM - Plots station model data.

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 c_wmbarb 
 c_wmdflt 
 c_wmdrft 
 c_wmdrrg 
 c_wmgetc 
 c_wmgeti 
 c_wmgetr 
 c_wmlabc 
 c_wmlabs 
 c_wmlabt 
 c_wmlabw 
 c_wmlgnd 
 c_wmsetc 
 c_wmseti 
 c_wmsetr 
 c_wmstnm

<h2>Access</h2>

To use Wmap Fortran or C entries, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: wmap_params, wmbarb, wmdflt, wmdrft, wmdrrg, wmgetc, wmgeti, wmgetr, wmlabc, wmlabs, wmlabt, wmlabw, wmlgnd, wmsetc, wmseti, wmsetr, wmstnm, ncarg_cbind. 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
