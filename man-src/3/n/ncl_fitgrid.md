---
title: "ncl_fitgrid(3)"
name: "ncl_fitgrid"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_fitgrid/"
---

Fitgrid is a package for interpolating one dimensional and two dimensional data. The package has the following functionality: 
 

 1.) Interpolating single-valued functions in one dimension. 
 2.) Interpolating parametric curves in the plane. 
 3.) Computing an interpolatory surface through a rectangular grid of functional values. 
 4.) Interpolating periodic functions in one dimension. 
 5.) Finding integrals and derivatives of interpolated functions. 
 

<h2>Synopsis</h2>FORTRAN single precision 
 ------------------------ 

 
&nbsp;<wbr>CURV1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>does set-up for CURV2.&nbsp;<wbr> 
 
&nbsp;<wbr>CURV2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>1D interpolation for non-periodic functions. 
 
&nbsp;<wbr>CURVD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>derivatives for 1D functions. 
 
&nbsp;<wbr>CURVI&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>integrals for 1D functions. 
 
&nbsp;<wbr>CURVP1&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>does set-up for CURVP2 . 
 
&nbsp;<wbr>CURVP2&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>1D interpolation for periodic functions. 
 
&nbsp;<wbr>CURVPI&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>integrals for periodic functions. 
 
&nbsp;<wbr>CURVS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>does smoothing and set-up for CURV2. 
 
&nbsp;<wbr>CURVPS&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>does smoothing for periodic functions. 
 
&nbsp;<wbr>KURV1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>does set-up for KURV2. 
 
&nbsp;<wbr>KURV2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolation for parametric curves. 
 
&nbsp;<wbr>KURVD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>derivatives for parametric curves. 
 
&nbsp;<wbr>KURVP1&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set-up for KURVP2. 
 
&nbsp;<wbr>KURVP2&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolation for closed parametric curves. 
 
&nbsp;<wbr>KURVPD&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>derivatives for closed parametric curves. 
 
&nbsp;<wbr>SURF1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set-up for SURF2. 
 
&nbsp;<wbr>SURF2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>2D interpolation for gridded data. 
 

 C single precision: 
 ------------------ 

 
&nbsp;<wbr>c_ftcurv&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>1D interpolation for non-periodic functions. 
 
&nbsp;<wbr>c_ftcurvd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>derivatives for 1D functions. 
 
&nbsp;<wbr>c_ftcurvi&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>integrals for 1D functions. 
 
&nbsp;<wbr>c_ftcurvp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>1D interpolation for periodic functions. 
 
&nbsp;<wbr>c_ftcurvpi&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>integrals for periodic functions. 
 
&nbsp;<wbr>c_ftcurvs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>does smoothing for non-periodic functions. 
 
&nbsp;<wbr>c_ftcurvps&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>does smoothing for periodic functions. 
 
&nbsp;<wbr>c_ftkurv&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolation for parametric curves. 
 
&nbsp;<wbr>c_ftkurvp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolation for closed parametric curves. 
 
&nbsp;<wbr>c_ftkurvd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>derivatives for parametric curves. 
 
&nbsp;<wbr>c_ftkurvpd&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolation for closed parametric curves. 
 
&nbsp;<wbr>c_ftsurf&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>2D interpolation for rectangular data. 
 
&nbsp;<wbr>c_ftseti&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set values for int parameters. 
 
&nbsp;<wbr>c_ftgeti&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>get values for int parameters. 
 
&nbsp;<wbr>c_ftsetr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set values for float parameters. 
 
&nbsp;<wbr>c_ftgetr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>get values for float parameters. 
 
&nbsp;<wbr>c_ftsetc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set values for string parameters. 
 
&nbsp;<wbr>c_ftgetc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>get values for string parameters. 
 
&nbsp;<wbr>c_ftsetfa&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set values for float arrays. 
 
&nbsp;<wbr>c_ftgetfa_size&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>get array size of float array. 
 
&nbsp;<wbr>c_ftgetfa_data&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>get float array data. 
 

 

<h2>Access</h2>To use fitgrid entries, load the NCAR Graphics library ngmath.
<h2>See Also</h2>Individual entries, fitgrid_params 

 Complete documentation for fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
