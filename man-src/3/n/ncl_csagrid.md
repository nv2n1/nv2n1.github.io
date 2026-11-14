---
title: "ncl_csagrid(3)"
name: "ncl_csagrid"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_csagrid/"
---

Csagrid is a software package in the ngmath library that implements a cubic spline approximation algorithm to fit a function to input data. The input for the approximation is a set of randomly-spaced data. These data may be one-dimensional, two-dimensional, or three-dimensional. 

 The output is a set of values at coordinates on a user-specified grid, or at a set of user-specified points (including at a single point). 

 Functionally equivalent Fortran, C, and NCL interfaces are provided. 

 Csagrid is based on the work of David Fulker and his package Splpack. 

<h2>Synopsis</h2>Fortran one-dimensional input 
 ----------------------------- 

 
&nbsp;<wbr>CSA1S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>simple entry 
 
&nbsp;<wbr>CSA1XS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry 

 Fortran two-dimensional input 
 ----------------------------- 

 
&nbsp;<wbr>CSA2S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- simple entry, gridded output 
 
&nbsp;<wbr>CSA2XS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry, gridded output 
 
&nbsp;<wbr>CSA2LS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- simple entry, list output 
 
&nbsp;<wbr>CSA2LXS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry, list output 

 Fortran three-dimensional input 
 ----------------------------- 

 
&nbsp;<wbr>CSA3S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- simple entry, gridded output 
 
&nbsp;<wbr>CSA3XS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry, gridded output 
 
&nbsp;<wbr>CSA3LS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- simple entry, list output 
 
&nbsp;<wbr>CSA3LXS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry, list output 

 C one-dimensional input 
 ----------------------------- 

 
&nbsp;<wbr>c_csa1s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>simple entry 
 
&nbsp;<wbr>c_csa1xs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry 

 C two-dimensional input 
 ----------------------------- 

 
&nbsp;<wbr>c_csa2s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- simple entry, gridded output 
 
&nbsp;<wbr>c_csa2xs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry, gridded output 
 
&nbsp;<wbr>c_csa2ls&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- simple entry, list output 
 
&nbsp;<wbr>c_csa2lxs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry, list output 

 C three-dimensional input 
 ----------------------------- 

 
&nbsp;<wbr>c_csa3s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- simple entry, gridded output 
 
&nbsp;<wbr>c_csa3xs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry, gridded output 
 
&nbsp;<wbr>c_csa3ls&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- simple entry, list output 
 
&nbsp;<wbr>c_csa3lxs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry, list output 

 NCL one-dimensional input 
 ----------------------------- 

 
&nbsp;<wbr>csa1s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>simple entry 
 
&nbsp;<wbr>csa1xs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry 

 NCL two-dimensional input 
 ----------------------------- 

 
&nbsp;<wbr>csa2s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- simple entry, gridded output 
 
&nbsp;<wbr>csa2xs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry, gridded output 
 
&nbsp;<wbr>csa2ls&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- simple entry, list output 
 
&nbsp;<wbr>csa2lxs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry, list output 

 NCL three-dimensional input 
 ----------------------------- 

 
&nbsp;<wbr>csa3s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- simple entry, gridded output 
 
&nbsp;<wbr>csa3xs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry, gridded output 
 
&nbsp;<wbr>csa3ls&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- simple entry, list output 
 
&nbsp;<wbr>csa3lxs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- expanded entry, list output
<h2>Access</h2>To use Csagrid entries, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, csa1s, csa1xs, csa2s, csa2xs, csa2ls, csa2lxs, csa3s, csa3xs, csa3ls, csa3lxs, c_csa1s, c_csa1xs, c_csa2s, c_csa2xs, c_csa2ls, c_csa2lxs, c_csa3s, c_csa3xs, c_csa3ls, c_csa3lxs. 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
