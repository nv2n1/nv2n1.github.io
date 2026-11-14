---
title: "ncl_supmap(3)"
name: "ncl_supmap"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_supmap/"
---

Draws a map with a single call. An implementation of the routine from which EZMAP grew.

<h2>Synopsis</h2>

&nbsp;<wbr>CALL SUPMAP&nbsp;<wbr>(JPRJ, PLAT, PLON, ROTA, PLM1, PLM2, PLM3,&nbsp;<wbr> 
 + PLM4, JLTS, JGRD, IOUT, IDOT, IERR)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_supmap (int jprj, float plat, float plon, 
 float rota, float *plm1, float *plm2, float *plm3, 
 float *plm4, int jlts, int jgrd, int iout, int idot, 
 int *ierr)

<h2>Description</h2>

<dl><dt>JPRJ
<dd>(input expression, of type INTEGER) defines the projection type and indicates whether or not continental outlines are to be plotted, as follows:
<dl><dd><dl><dt>&bull;
<dd>IABS(JPRJ) defines the projection type, as follows (values less than 1 or greater than 10 are treated as 1 or 10, respectively):
<dl><dd><dl><dt>IABS(JPRJ)
<dd>Projection Type
<dt>1
<dd>Stereographic.
<dt>2
<dd>Orthographic.
<dt>3
<dd>Lambert conformal conic.
<dt>4
<dd>Lambert equal area.
<dt>5
<dd>Gnomonic.
<dt>6
<dd>Azimuthal equidistant.
<dt>7
<dd>Satellite view.
<dt>8
<dd>Cylindrical equidistant.
<dt>9
<dd>Mercator.
<dt>10
<dd>Mollweide-type.</dl></dl><dd>Using the value 2 causes the EZMAP parameter 'SA' to be zeroed. ('SA', if greater than 1., says that a satellite-view projection, rather than an orthographic projection, is to be used, and specifies the distance of the satellite from the center of the earth, in units of earth radii.) 

 Using the value 7 causes 'SA' to be examined. If it has a non-zero value, the value is left alone. If it has a zero value, its value is reset to 6.631, which is about right for a satellite in a geosynchronous equatorial orbit.</dl></dl><dl><dd><dl><dt>&bull;
<dd>The sign of JPRJ, when IOUT is -1, 0, or +1, indicates whether the continental outlines are to be plotted or not. See IOUT, below.</dl></dl><dt>PLAT, PLON, and ROTA
<dd>(input expressions, of type REAL) define the origin of the projection and its rotation angle and are used in the same way as they would be in a call to the routine MAPROJ (which see).
<dt>JLTS
<dd>(input expression, of type INTEGER), and PLM1, PLM2, PLM3, and PLM4 (input arrays, dimensioned 2, of type REAL) specify the rectangular limits of the map. These arguments are used in the same way as they would be in a call to MAPSET (which see), except that JLTS is an integer instead of a character string. IABS(JLTS) may take on the values 1 through 5, as follows:
<dl><dd><dl><dt>IABS(JLTS)
<dd>Equivalent character string in a call to MAPSET
<dt>1
<dd>'MA' - maximal area desired.
<dt>2
<dd>'CO' - corner points given in PLM1, PLM2, PLM3, and PLM4.
<dt>3
<dd>'LI' - U/V limits given in PLM1, PLM2, PLM3, and PLM4.
<dt>4
<dd>'AN' - angles given in PLM1, PLM2, PLM3, and PLM4.
<dt>5
<dd>'PO' - edge points given in PLM1, PLM2, PLM3, and PLM4.</dl></dl><dd>At one time, the sign of JLTS specified whether or not a line of text was to be written at the bottom of the plot produced. This line may no longer be written and the sign of JLTS is therefore ignored.
<dt>JGRD
<dd>(input expression, of type INTEGER) is used in the following way: The value of &quot;MOD(IABS(JGRD),1000)&quot; is the value, in degrees, of the interval at which lines of latitude and longitude are to be plotted. If the given interval is zero, grid lines and labels are not plotted. If JGRD is less than zero, the perimeter is not plotted. Set JGRD to -1000 to suppress both grid lines and perimeter and to +1000 to suppress the grid lines, but leave the perimeter. The value -0 may have a meaning on ones' complement machines, but should be avoided; use -1000 instead.
<dt>IOUT
<dd>(input expression, of type INTEGER) has the value 0 to suppress U.S. state outlines, and the value -1 or +1 to plot U.S. state outlines. In both of these cases, the sign of JPRJ indicates whether continental outlines are to be plotted (JPRJ positive) or not (JPRJ negative). Originally, SUPMAP recognized only these values of IOUT; now, if IOUT is less than 0 or greater than 1, the sign of JPRJ is ignored, and IOUT selects an outline group, as follows:
<dl><dd><dl><dt>IOUT
<dd>Outline group selected
<dt>-2 or less
<dd>'NO' (no outlines)
<dt>2
<dd>'CO' (continental outlines)
<dt>3
<dd>'US' (U.S. state outlines)
<dt>4
<dd>'PS' (continental outlines plus international outlines plus U.S. state outlines)
<dt>5 or greater
<dd>'PO' (continental outlines plus international outlines)</dl></dl><dd>At one time, the sign of IOUT specified whether or not a line of text was to be written on the print output unit. This may no longer be done.
<dt>IDOT
<dd>(input expression, of type INTEGER) is a 0 to get continuous outlines, a 1 to get dotted outlines.
<dt>IERR
<dd>(output variable, of type INTEGER) is the only output parameter. A non-zero value indicates that an error has occurred. The section &quot;ERROR CONDITIONS&quot; lists the possible values of IERR.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: caredg, cmpgci, cmpsup, mpex03, mpex08, mpexfi, bnchmk, stex03, vvex02.

<h2>Access</h2>

To use SUPMAP or c_supmap, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
