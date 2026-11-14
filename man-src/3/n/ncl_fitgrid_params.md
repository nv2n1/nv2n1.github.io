---
title: "ncl_fitgrid_params(3)"
name: "ncl_fitgrid_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_fitgrid_params/"
---

fitgrid_params - This document briefly describes all the internal parameters of Fitgrid. 

<h2>Description</h2>Each entry below includes the name of a parameter, its Fortran type (use the obvious equivalents for C), its default value, and a short description of the parameter.
<dl COMPACT><dt>'SIG' - Real - 1.
<dd>Value of the tension factor.
<dt>'SL1' - Real - 0.
<dd>The slope of the curve at the first point (see parameter SF1).
<dt>'SLN' - Real - 0.
<dd>The slope of the curve at the final point (see parameter SF1).
<dt>'SF1' - Integer - 3
<dd>Controls the use of parameters SL1 and SL2: 0=use both; 1=use SL1 only; 2=use SL2 only; 3=use neither.
<dt>'SF2' - Integer - 3
<dd>Controls the use of parameters SMT and EPS: 0=use neither; 1=use both; 2=use SMT only; 3=use EPS only.
<dt>'SMT' - Real - none
<dd>Smoothing parameter for ftcurvs, ftcurvps, c_ftcurvs, and c_ftcurvps.
<dt>'EPS' - Real - none
<dd>Smoothing parameter for ftcurvs, ftcurvps, c_ftcurvs, and c_ftcurvps.
<dt>'ZX1' - Real array - none
<dd>X partials at left for ftsurf and c_ftsurf.
<dt>'ZXM' - Real array - none
<dd>X partials at right for ftsurf and c_ftsurf.
<dt>'ZY1' - Real array - none
<dd>Y partials at bottom for ftsurf and c_ftsurf.
<dt>'ZYN' - Real array - none
<dd>Y partials at top for ftsurf and c_ftsurf.
<dt>'Z11' - Real - none
<dd>X-Y partial at lower left for ftsurf and c_ftsurf.
<dt>'ZM1' - Real - none
<dd>X-Y partial at lower right for ftsurf and c_ftsurf.
<dt>'Z1N' - Real - none
<dd>X-Y partial at upper left for ftsurf and c_ftsurf.
<dt>'ZMN' - Real - none
<dd>X-Y partial at upper right for ftsurf and c_ftsurf.
<dt>'DF1' - Integer - 1
<dd>Flag indicating if ZX1 is user supplied: 0=yes; 1=no.
<dt>'DF2' - Integer - 1
<dd>Flag indicating if ZXM is user supplied: 0=yes; 1=no.
<dt>'DF3' - Integer - 1
<dd>Flag indicating if ZY1 is user supplied: 0=yes; 1=no.
<dt>'DF4' - Integer - 1
<dd>Flag indicating if ZYN is user supplied: 0=yes; 1=no.
<dt>'DF5' - Integer - 1
<dd>Flag indicating if Z11 is user supplied: 0=yes; 1=no.
<dt>'DF6' - Integer - 1
<dd>Flag indicating if ZM1 is user supplied: 0=yes; 1=no.
<dt>'DF7' - Integer - 1
<dd>Flag indicating if Z1M is user supplied: 0=yes; 1=no.
<dt>'DF8' - Integer - 1
<dd>Flag indicating if ZMN is user supplied: 0=yes; 1=no.</dl><h2>See Also</h2>fitgrid, fitgrid_params, curv1, curv2, curvd, curvi, curvp1, curvp2, curvpi, curvs, curvps, kurv1, kurv2, kurvd, kurvp1, kurvp2, kurvpd, surf1, surf2, c_ftcurv, c_ftcurvd, c_ftcurvi, c_ftcurvp, c_ftcurvpi, c_ftcurvs, c_ftcurvps, c_ftkurv, c_ftkurvp, c_ftkurvd, c_ftkurvpd, c_ftsurf, c_ftseti, c_ftgeti, c_ftsetr, c_ftgetr, c_ftsetc, c_ftgetc, c_ftsetfa, c_ftgetfa_size, c_ftgetfa_data. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
