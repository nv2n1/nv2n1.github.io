---
title: "ncl_natgrid(3)"
name: "ncl_natgrid"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_natgrid/"
---

<pre><code>Natgrid is a package for gridding 2D randomly-spaced data using
a natural neighbor algorithm.  Single precison and double
precision interfaces exist in both Fortran and C.</code></pre>
<h2>Synopsis</h2>FORTRAN single precision 
 ------------------------ c_natgridd     -  primary function for gridding.


c_nnseti       -  set int parameter values.


c_nngeti       -  retrieve values for int parameters.


c_nnsetrd      -  set double parameter values.


c_nngetrd      -  retrieve values for double parameters.


c_nnsetc       -  set char valued parameters.


c_nngetc       -  retrieve values for char parameters.


c_nngetsloped  -  get slope values, if calculated.


c_nngetaspectd -  get aspect values, if calculated.


c_nnpntinitd   -  initiate single point mode.


c_nnpntd       -  interpolate at a single point.


c_nnpntendd    -  terminate single point mode. Fortran double precision (not supported on UNICOS): 
 -------------------------------------------------- c_natgridd     -  primary function for gridding.


c_nnseti       -  set int parameter values.


c_nngeti       -  retrieve values for int parameters.


c_nnsetrd      -  set double parameter values.


c_nngetrd      -  retrieve values for double parameters.


c_nnsetc       -  set char valued parameters.


c_nngetc       -  retrieve values for char parameters.


c_nngetsloped  -  get slope values, if calculated.


c_nngetaspectd -  get aspect values, if calculated.


c_nnpntinitd   -  initiate single point mode.


c_nnpntd       -  interpolate at a single point.


c_nnpntendd    -  terminate single point mode. C single precision: 
 ------------------ c_natgridd     -  primary function for gridding.


c_nnseti       -  set int parameter values.


c_nngeti       -  retrieve values for int parameters.


c_nnsetrd      -  set double parameter values.


c_nngetrd      -  retrieve values for double parameters.


c_nnsetc       -  set char valued parameters.


c_nngetc       -  retrieve values for char parameters.


c_nngetsloped  -  get slope values, if calculated.


c_nngetaspectd -  get aspect values, if calculated.


c_nnpntinitd   -  initiate single point mode.


c_nnpntd       -  interpolate at a single point.


c_nnpntendd    -  terminate single point mode. C double precision: 
 ------------------ c_natgridd     -  primary function for gridding.


c_nnseti       -  set int parameter values.


c_nngeti       -  retrieve values for int parameters.


c_nnsetrd      -  set double parameter values.


c_nngetrd      -  retrieve values for double parameters.


c_nnsetc       -  set char valued parameters.


c_nngetc       -  retrieve values for char parameters.


c_nngetsloped  -  get slope values, if calculated.


c_nngetaspectd -  get aspect values, if calculated.


c_nnpntinitd   -  initiate single point mode.


c_nnpntd       -  interpolate at a single point.


c_nnpntendd    -  terminate single point mode.
<h2>Access</h2>To use Natgrid entries, load the NCAR Graphics library ngmath.
<h2>See Also</h2>Individual entries, natgrid_params, natgrid_errors. <pre><code>Complete documentation for Natgrid is available at URL

http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</code></pre> An NCL (NCAR Command Language) interface also exists for Natgrid procedures.
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
