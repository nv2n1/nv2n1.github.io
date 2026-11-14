---
title: "ncl_natgrid_params(3)"
name: "ncl_natgrid_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_natgrid_params/"
---

natgrid_params - This document briefly describes all the internal parameters of Natgrid. 

<h2>Description</h2><pre><code>Each entry below includes the name of a parameter, its Fortran type
(use the obvious equivalents for C),
its default value, and a short description of the parameter.

'ADF'   -   Integer   -    0
Flags if the data file of algorithmic information for display with
nnalg is produced - see parameter alg (0=no; 1=yes).
'ALG'   -   Character   -   'nnalg.dat'
File name for input to the algorithmic display tool nnalg
(see parameter adf).
'ASC'   -   Integer   -   1
Flags if automatic scaling is allowed (0 = no; 1 = yes).
'bI'   -   Real   -   1.5
Tautness factor that increases the effect of the gradient estimates
as bI increases.
'bJ'   -   Real   -   7.0
Tautness factor that decreases the breadth of the region
affected by the gradient estimates as bJ increases.
'EXT'   -   Integer   -   1
Flags whether extrapolation is allowed outside the
convex hull (0=no; 1=yes).
'HOR'   -   Real   -   0.1*(extent of X output grid)
Specifies the amount of horizontal overlap to be included outside
of the current region when doing subblocking.
'IGR'   -   Integer   -   0
Flag indicating if gradient estimates are to be computed (1=yes; 0=no).
'MAGX'   -   Real   -   1.0
Scale factor for X coordinate input values.
'MAGY'   -   Real   -   1.0
Scale factor for Y coordinate input values.
'MAGZ'   -   Real   -   1.0
Scale factor for Z coordinate input values.
'MDM'   -   Integer   -   10
Maximum number of informational messages about duplicate point culls.
'NON'   -   Integer   -   0
Flags whether interpolated values are allowed to be
negative (0=yes; 1=no).
'NUL'   -   Real   -   0.0
The value to be used on output for points outside of the convex
hull when extrapolation is not allowed.
'RAD'   -   Integer   -   0
Flags if slopes and aspects are returned in radians or degrees
(1=radians;0=degrees).
'SDI'   -   Integer   -   0
Flags if slopes and aspects are computed (0=no; 1=yes).
'UPD'   -   Integer   -   1
Flags if the output array goes from south to north or north to south
(0=north to south; 1=south to north).
'VER'   -   Real   -   0.1*(extent of Y output grid)
Specifies the amount of vertical overlap to be included outside
of the current region when doing subblocking.
'XAS'   -   Real   -   1.0
Contains the scale value for automatic scaling of X input values
in the most recent interpolation call.  For retrieval only.
'YAS'   -   Real   -   1.0
Contains the scale value for automatic scaling of Y input values
in the most recent interpolation call.  For retrieval only.
'ZAS'   -   Real   -   1.0
Contains the scale value for automatic scaling of Z input values
in the most recent interpolation call.  For retrieval only.</code></pre>
<h2>See Also</h2>c_natgridd, c_natgrids, c_nngetaspectd, c_nngetaspects, c_nngetc, c_nngeti, c_nngetr, c_nngetrd, c_nngetsloped, c_nngetslopes, c_nnpntd, c_nnpntend, c_nnpntendd, c_nnpntinitd, c_nnpntinits, c_nnpnts, c_nnsetc, c_nnseti, c_nnsetr, c_nnsetrd, natgrid, natgrid_params, natgridd, natgrids, nngetaspectd, nngetaspects, nngetc, nngeti, nngetr, nngetrd, nngetslopes, nngetslpped, nnpntd, nnpntend, nnpntendd, nnpntinitd, nnpntinits, nnpnts, nnsetc, nnseti, nnsetr, nnsetrd. <pre><code>Complete documentation for Natgrid is available at URL

http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</code></pre>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
