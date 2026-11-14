---
title: "ncl_mplndm(3)"
name: "ncl_mplndm"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mplndm/"
---

MPLNDM - Reads a specified EZMAP database and draws boundary lines from it, masked by a specified area map. 

<h2>Synopsis</h2>CALL MPLNDM (FLNM,ILVL,IAMA,XCRA,YCRA,MCRA,IAAI,IAGI,NOGI,ULPR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mplndm (char *flnm, int ilvl, int *iama, float *xcra, float *ycra, int mcra, int *iaai, int *iagi, int nogi, int (*ulpr_)(float *xcra, float *ycra, int *ncra, int *iaai, int *iagi, int *ngps))
<h2>Description</h2><pre><code>FLNM
(an input expression of type CHARACTER) specifies the name of the database to
be used.  MPLNDM will first look for the files of the specified database in
the current working directory;
if the files are not found there, MPLNDM will
look for them in the NCAR Graphics database directory.  The database created in
1998 and provided as part of Version 4.1 of NCAR Graphics is named &quot;Earth..1&quot;.
ILVL
(an input expression of type INTEGER) specifies the level at which the database
is to be used.  The value 1 says to use only land/water boundaries, the value 2
says to add continental boundaries (like the boundary which separates Africa
from Eurasia), the value 3 says to add the boundaries of countries, and
the value 4 says to add states.  (The value 5 will eventually be used to add
counties.)
IAMA
(an input/output array of type INTEGER, dimensioned as specified in a call to
the AREAS routine ARINAM) is the array containing the area map against which
boundary lines are to be masked.  The area map must have been initialized by
a call to ARINAM;
it should contain the edges required to create a desired
    effect.For example,
    an area map might be created that defines a region of
        interest,
    within which user data is available and within which boundary lines
        are to be drawn.XCRA and
        YCRA(scratch arrays, dimensioned at least MCRA, of type REAL) are to be used by
    MPLNDM in calls to the AREAS routine ARDRLN;
they will eventually be used in
        calls to the user -
    provided line - processing routine ULPR.MCRA(an input expression of type INTEGER) is the dimension of the arrays XCRA and YCRA.IAAI and IAGI(scratch arrays, dimensioned at least NOGI, of type INTEGER) are to be used by MPLNDM in calls to the AREAS routine ARDRLN; they will eventually be used
in calls to the user-provided line-processing routine ULPR. The mnemonics
stand for &quot;Integer Array of Area Identifiers&quot; and &quot;Integer Array of Group
Identifiers&quot;, respectively.
NOGI
(an input expression of type INTEGER) is the dimension of the arrays
IAAI and IAGI. The mnemonic stands for &quot;Number Of Group Identifiers (of
edges in the area map)&quot;, which determines the required dimension of IAAI
and IAGI.
ULPR
is the name of the user-supplied line-processing routine. It must be declared
EXTERNAL in the routine that calls MPLNDM, so that the compiler and loader will
know that it is the name of a routine to be called instead of a variable. The
user routine ULPR will be called once for each piece of a boundary line
resulting from the masking process;
it may decide to draw(or to not draw)
    each such piece.ULPR will be called using a FORTRAN statement like

    CALL ULPR(XCRA, YCRA, NCRA, IAAI, IAGI, NGPS)

where XCRA and YCRA are real arrays holding the normalized device coordinates
of NCRA points defining a polyline which is part of some boundary line and IAAI
and IAGI are integer arrays holding NGPS area-identifier/group-identifier pairs
for the area within which that piece of the line lies. In writing ULPR, the
user may rely upon a SET call's having been done which makes it possible to
use normalized device coordinates in calls to routines like CURVE, CURVED, GPL,
etc.  For more details, see the reference document for the package named AREAS
and, in particular, the description of the subroutine ARDRLN.</code></pre>
<h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>MPLNDM is called to draw the lines defined by the map database whose name is FLNM, masked against the area map in the array IAMA. 

 MPLNDM is much like MPLNDR, except that the boundary lines are drawn using calls to MAPITM and MAPIQM, which does the masking of the lines against an area map and passes the pieces resulting from the masking process along to a user-provided line-drawing routine.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: mpex11.
<h2>Access</h2>To use MPLNDM or c_mplndm, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
