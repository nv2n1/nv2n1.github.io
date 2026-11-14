---
title: "ncl_css_overview(3)"
name: "ncl_css_overview"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_css_overview/"
---

Cssgrid is a software package in the ngmath library that implements a tension spline interpolation algorithm to fit a function to input data randomly located on the surface of a sphere. 

 There are user-settable parameters that control various aspects of the algorithm, the most important of which is the tension factor that controls the level a tautness of the spline fit. This varies from pure cubic spline interpolation for a tension factor of 0. to near linear interpolation for a large tension factor. By default, the tension factor is automatically computed to optimize certain fitting criteria. 

 The output is a set of values at coordinates on a user-specified lat/lon grid (which can be a single point). Procedures also exist for finding a Dealunay triangulation and Voronoi polygons. 

 Functionally equivalent Fortran, C, and NCL interfaces are provided. Fortran and C codes are available in both single and double precision. 

 Cssgrid is based on the work of Robert Renka and his packages STRIPACK and SSRFPACK. 

<h2>Synopsis</h2>Fortran 
 ----------------------------- 
 
&nbsp;<wbr>CSSGRID&nbsp;<wbr>&nbsp;<wbr>- interpolation on a sphere 
 
&nbsp;<wbr>CSSTRI&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- calculates Delaunay triangulation 
 
&nbsp;<wbr>CSVORO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- calculates Voronoi polygons 
 
&nbsp;<wbr>CSS2C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- converts from lat/lon to Cartesian coordinates 
 
&nbsp;<wbr>CSC2S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- converts from Cartesian to lat/lon coordinates 
 
&nbsp;<wbr>CSSETI&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- set values for integer-valued parameters 
 
&nbsp;<wbr>CSGETI&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- retrieve values for integer-valued parameters 
 
&nbsp;<wbr>CSSETR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- set values for real valued parameters 
 
&nbsp;<wbr>CSGETR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- retrieve values for real valued parameters 
 
&nbsp;<wbr>CSSETD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- set values for double precision-valued parameters 
 
&nbsp;<wbr>CSGETD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- retrieve values for double precision-valued parameters 
 
&nbsp;<wbr>CSSGRIDD - interpolation on a sphere&nbsp;<wbr>(double precision entry) 
 
&nbsp;<wbr>CSSTRID&nbsp;<wbr>&nbsp;<wbr>- calculates Delaunay triangulation&nbsp;<wbr>(double precision entry) 
 
&nbsp;<wbr>CSVOROD&nbsp;<wbr>&nbsp;<wbr>- calculates Voronoi polygons&nbsp;<wbr>(double precision entry) 
&nbsp;<wbr>CSS2CD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- converts from lat/lon to Cartesian coordinates&nbsp;<wbr>(double precision entry) 
 
&nbsp;<wbr>CSC2SD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- converts from Cartesian to lat/lon coordinates&nbsp;<wbr>(double precision entry) 
 ----------------------------- 
 
&nbsp;<wbr>c_cssgrid&nbsp;<wbr>&nbsp;<wbr>- interpolation on a sphere 
 
&nbsp;<wbr>c_csstri&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- calculates Delaunay triangulation 
 
&nbsp;<wbr>c_csvoro&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- calculates Voronoi polygons 
 
&nbsp;<wbr>c_css2c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- converts from lat/lon to Cartesian coordinates 
 
&nbsp;<wbr>c_csc2s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- converts from Cartesian to lat/lon coordinates 
 
&nbsp;<wbr>c_csseti&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- set values for integer-valued parameters 
 
&nbsp;<wbr>c_csgeti&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- retrieve values for integer-valued parameters 
 
&nbsp;<wbr>c_cssetr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- set values for real valued parameters 
 
&nbsp;<wbr>c_csgetr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- retrieve values for real valued parameters 
 
&nbsp;<wbr>c_cssetd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- set values for double precision-valued parameters 
 
&nbsp;<wbr>c_csgetd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- retrieve values for double precision-valued parameters 
 
&nbsp;<wbr>c_cssgridd - interpolation on a sphere&nbsp;<wbr>(double precision entry) 
 
&nbsp;<wbr>c_csstrid&nbsp;<wbr>&nbsp;<wbr>- calculates Delaunay triangulation&nbsp;<wbr>(double precision entry) 
 
&nbsp;<wbr>c_csvorod&nbsp;<wbr>&nbsp;<wbr>- calculates Voronoi polygons&nbsp;<wbr>(double precision entry) 
 
&nbsp;<wbr>c_css2cd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- converts from lat/lon to Cartesian coordinates&nbsp;<wbr>(double precision entry) 
 
&nbsp;<wbr>c_csc2sd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- converts from Cartesian to lat/lon coordinates&nbsp;<wbr>(double precision entry)
<h2>Access</h2>To use Cssgrid entries, load the NCAR Graphics library ngmath.
<h2>See Also</h2>cssgrid_params cssgrid_errors 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
