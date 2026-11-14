---
title: "ncl_mapeod(3)"
name: "ncl_mapeod"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapeod/"
---

MAPEOD - Called by the EZMAP routines MAPLOT and MAPBLA. The default version does nothing. A user-written version may be supplied to examine each outline-dataset segment and, perhaps, to delete selected ones. Note that this routine is not called by any of the EZMAPB routines; for the same purpose, they call the routine MPCHLN. 

<h2>Synopsis</h2>CALL MAPEOD (NOUT,NSEG,IDLS,IDRS,NPTS,PNTS)
<h2>Description</h2><dl COMPACT><dt>NOUT
<dd>(an input expression of type INTEGER) is the number of the outline dataset from which the segment comes, as follows:
<dl COMPACT><dd><dl COMPACT><dt>NOUT
<dd>Dataset from which the segment came
<dt>1
<dd>CO - Continental outlines only.
<dt>2
<dd>US - U.S. state outlines only.
<dt>3
<dd>PS - Continental, U.S. state, and international outlines.
<dt>4
<dd>PO - Continental and international outlines.</dl></dl><dt>NSEG
<dd>(an input expression of type INTEGER) is the number of the segment within the outline dataset. The maps in the example named &quot;mpex09&quot; show segment numbers for the outline dataset 'CO'; the program may be modified to produce maps showing segment numbers for any outline dataset.
<dt>IDLS and IDRS
<dd>(input expressions of type INTEGER) are identifiers for the areas to the left and right, respectively, of the segment. (Left and right are defined from the standpoint of a viewer standing at point 1 of the segment and looking toward point 2.)
<dt>NPTS
<dd>(an input/output variable of type INTEGER), on entry, is the number of points defining the outline segment. NPTS may be zeroed by MAPEOD to suppress plotting of the segment on the map.
<dt>PNTS
<dd>(an input/output array, dimensioned 2*NPTS, of type REAL) is an array of coordinates. <a HREF="/docs/linux/man/1-pnts/">PNTS</a>(1) and <a HREF="/docs/linux/man/2-pnts/">PNTS</a>(2) are the latitude and longitude of the first point, <a HREF="/docs/linux/man/3-pnts/">PNTS</a>(3) and <a HREF="/docs/linux/man/4-pnts/">PNTS</a>(4) the latitude and longitude of the second point, ... PNTS(2*NPTS-1) and PNTS(2*NPTS) the latitude and longitude of the last point. All values are in degrees. Longitudes are all between -180 and +180; no segment crosses the meridian at -180 (+180) degrees.</dl><h2>Usage</h2>MAPEOD is called by MAPLOT to examine each segment in an outline dataset just before it is plotted and by MAPBLA to examine each segment in an outline dataset just before it is added to an area map. The default version of MAPEOD does nothing. A user-supplied version may cause selected segments to be deleted (to reduce the clutter in northern Canada, for example).
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: mpex03, mpex05, mpex09.
<h2>Access</h2>To use MAPEOD, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
