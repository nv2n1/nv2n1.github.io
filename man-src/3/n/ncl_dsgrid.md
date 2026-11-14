---
title: "ncl_dsgrid(3)"
name: "ncl_dsgrid"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dsgrid/"
---

Dsgrid is a package for gridding 3D and 2D randomly-spaced data using an inverse distance weighted average algorithm. Single precision and double precision interfaces exist in both Fortran and C. 

<h2>Synopsis</h2>FORTRAN single precision 
 ------------------------ 

 
&nbsp;<wbr>DSGRID2S&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>primary function for gridding 2D data. 
 
&nbsp;<wbr>DSGRID3S&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>primary function for gridding 3D data. 
 
&nbsp;<wbr>DSSETI&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set INTEGER parameter values. 
 
&nbsp;<wbr>DSGETI&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>retrieve values for INTEGER parameters. 
 
&nbsp;<wbr>DSSETR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set REAL parameter values. 
 
&nbsp;<wbr>DSGETR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>retrieve values for REAL parameters. 
 
&nbsp;<wbr>DSSETC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set CHARACTER valued parameters. 
 
&nbsp;<wbr>DSGETC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>retrieve values for CHARACTER parameters. 
 
&nbsp;<wbr>DSPNT2S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolate 2D data at specified points. 
 
&nbsp;<wbr>DSPNT3S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolate 3D data at specified points. 

 Fortran double precision (not supported on UNICOS): 
 -------------------------------------------------- 

 
&nbsp;<wbr>DSGRID2D&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>primary function for gridding 2D data. 
 
&nbsp;<wbr>DSGRID3D&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>primary function for gridding 3D data. 
 
&nbsp;<wbr>DSSETI&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set INTEGER parameter values. 
 
&nbsp;<wbr>DSGETI&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>retrieve values for INTEGER parameters. 
 
&nbsp;<wbr>DSSETRD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set DOUBLE PRECISION parameter values. 
 
&nbsp;<wbr>DSGETRD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>retrieve DOUBLE PRECISION parameters. 
 
&nbsp;<wbr>DSSETC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set CHARACTER valued parameters. 
 
&nbsp;<wbr>DSGETC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>retrieve values for CHARACTER parameters. 
 
&nbsp;<wbr>DSPNT2D&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolate 2D data at specified points. 
 
&nbsp;<wbr>DSPNT3D&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolate 3D data at specified points. 

 C single precision: 
 ------------------ 

 
&nbsp;<wbr>c_dsgrid2s&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>primary function for gridding 2D data. 
 
&nbsp;<wbr>c_dsgrid3s&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>primary function for gridding 3D data. 
 
&nbsp;<wbr>c_dsseti&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set int parameter values. 
 
&nbsp;<wbr>c_dsgeti&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>retrieve values for int parameters. 
 
&nbsp;<wbr>c_dssetr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set float parameter values. 
 
&nbsp;<wbr>c_dsgetr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>retrieve values for float parameters. 
 
&nbsp;<wbr>c_dssetc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set char valued parameters. 
 
&nbsp;<wbr>c_dsgetc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>retrieve values for char parameters. 
 
&nbsp;<wbr>c_dspnt2s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolate 2D data at specified points. 
 
&nbsp;<wbr>c_dspnt3s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolate 3D data at specified points. 

 C double precision: 
 ------------------ 

 
&nbsp;<wbr>c_dsgrid2d&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>primary function for gridding 2D data. 
 
&nbsp;<wbr>c_dsgrid3d&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>primary function for gridding 3D data. 
 
&nbsp;<wbr>c_dsseti&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set int parameter values. 
 
&nbsp;<wbr>c_dsgeti&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>retrieve values for int parameters. 
 
&nbsp;<wbr>c_dssetrd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set double parameter values. 
 
&nbsp;<wbr>c_dsgetrd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>retrieve values for double parameters. 
 
&nbsp;<wbr>c_dssetc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>set char valued parameters. 
 
&nbsp;<wbr>c_dsgetc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>retrieve values for char parameters. 
 
&nbsp;<wbr>c_dspnt2d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolate 2D data at specified points. 
 
&nbsp;<wbr>c_dspnt3d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>interpolate 3D data at specified points. 

<h2>Access</h2>To use Dsgrid entries, load the NCAR Graphics library ngmath.
<h2>See Also</h2>Individual entries, dsgrid_params, dsgrid_errors. 

 Complete documentation for Dsgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
