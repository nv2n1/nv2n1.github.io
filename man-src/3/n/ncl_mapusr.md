---
title: "ncl_mapusr(3)"
name: "ncl_mapusr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapusr/"
---

MAPUSR - Called by EZMAP routines that draw the various parts of the map. The default version does nothing. A user-written version may be supplied to change the appearance of the map. Note that this routine is not called by any of the EZMAPB routines; they call MPCHLN instead. 

<h2>Synopsis</h2>CALL MAPUSR (IPRT)
<h2>Description</h2><pre><code>IPRT
(input expression, of type INTEGER), if positive, says that a
particular part of the map is about to be drawn, as follows:</code></pre>
<dl COMPACT><dt>IPRT
</dt><dd>Part of map about to be drawn
</dd><dt>1
</dt><dd>Perimeter.
</dd><dt>2
</dt><dd>Grid.
</dd><dt>3
</dt><dd>Labels.
</dd><dt>4
</dt><dd>Limb lines.
</dd><dt>5
</dt><dd>Continental outlines.
</dd><dt>6
</dt><dd>U.S. state outlines.
</dd><dt>7
</dt><dd>International outlines.</dd></dl></dl><dd>If IPRT is negative, then the drawing of the last part is complete. The absolute value of IPRT will be one of the above values. Changed quantities should be restored.</dd></dl><h2>Usage</h2>EZMAP executes the statement 

<dl COMPACT><dd>CALL MAPUSR (IPRT)</dd></dl>
 

 just before and just after each portion of a map is drawn. The default version of MAPUSR does nothing. 

 A user-supplied version of MAPUSR may set/reset the dotting parameter 'DL', the DASHCHAR dash pattern, the color index, etc., so as to achieve a desired effect.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: mpex08.
<h2>Access</h2>To use MAPUSR, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
