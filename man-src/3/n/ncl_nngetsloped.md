---
title: "ncl_nngetsloped(3)"
name: "ncl_nngetsloped"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nngetsloped/"
---

NNGETSLOPED - retrieve the double precision slope at a specified coordinate.

<h2>Synopsis</h2>

CALL NNGETSLOPED (I,J,SLOPE,IER)

<h2>Description</h2>

<dl><dt>I
<dd>(Integer, Input) - A subscript indexing the first dimensioned variable in the output grid of the most recent call to NATGRIDD.
<dt>J
<dd>(Integer, Input) - A subscript indexing the second dimensioned variable in the output grid of the most recent call to NATGRIDD.
<dt>SLOPE
<dd>(Double precision, Output) - The slope at the grid point Z(I,J), where Z is the output grid in the most recent call to NATGRIDD.
<dt>IER
<dd>(Integer, Output) - An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for natgrid_errors for details.</dl>

<h2>Access</h2>

To use NNGETSLOPED, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

natgrid, natgridd, natgrid_params. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
