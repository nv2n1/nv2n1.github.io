---
title: "ncl_ezmapa(3)"
name: "ncl_ezmapa"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ezmapa/"
---

EZMAP - Allows one to plot maps of the earth according to any of ten different projections, with parallels, meridians, and continental, international, and/or U.S. state outlines. 

 EZMAPA is the name of a supplement to the EZMAP utility that allows users to produce solid-filled maps of the earth. The EZMAPA routines are discussed as part of the EZMAP utility. 

 EZMAPB is the name of a supplement to the EZMAP utility that provides access to improved map databases (principally one called &quot;Earth..1&quot;, which contains a unified higher-resolution version of everything that was in the old outline datasets). The EZMAPB routines are discussed as part of the EZMAP utility. 

<h2>Synopsis</h2><dl COMPACT><dt>Routines Used to Draw a Simple Map
<dd>To draw the simple map defined by the current values of EZMAP's internal parameters (assuming no area fills and no access to the new, improved, map database &quot;Earth..1&quot;, which was created in 1998), one need only execute the single FORTRAN statement &quot;CALL MAPDRW&quot;:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MAPDRW - Draws a complete simple map.</dl></dl><dd>All that MAPDRW does is call four lower-level routines. In some situations, the user may wish to call these routines directly; they are as follows (in the order in which they are called by MAPDRW):
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MAPINT - Initializes. MAPINT must be called at least once before calling any routine that depends on mapping lat/lon coordinates into u/v coordinates. After one or more of MAPPOS, MAPROJ, and MAPSET has been called, MAPINT must be called again. MAPINT does the call to the SPPS routine SET that defines the mapping from the u/v (projection) plane to the x/y (plotter) plane.
<dt>&bull;
<dd>MAPGRD - Draws selected parallels and meridians.
<dt>&bull;
<dd>MAPLBL - Labels the international date line, the equator, the Greenwich meridian, and the poles, and draws the perimeter.
<dt>&bull;
<dd>MAPLOT - Draws selected geographic outlines. Note that this routine uses whichever old outline dataset is selected by the value of the internal parameter 'OU'; to access the new map database &quot;Earth..1&quot;, which was created in 1998, one must call instead the EZMAPB routine MPLNDR.</dl></dl><dt>Routines Used to Change the Values of Internal Parameters
<dd>The following routines are called to change the values of internal parameters of EZMAP, and thus change the behavior of other EZMAP routines:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MAPPOS - Determines what portion of the plotter frame is to be used.
<dt>&bull;
<dd>MAPROJ - Determines the projection to be used.
<dt>&bull;
<dd>MAPSET - Determines what portion of the u/v plane is to be viewed.
<dt>&bull;
<dd>MAPSTC - Sets a parameter value of type CHARACTER.
<dt>&bull;
<dd>MAPSTI - Sets a parameter value of type INTEGER.
<dt>&bull;
<dd>MAPSTL - Sets a parameter value of type LOGICAL.
<dt>&bull;
<dd>MAPSTR - Sets a parameter value of type REAL.</dl></dl><dt>Routines Used to Retrieve the Values of Internal Parameters
<dd>The following routines are used to retrieve the current values of EZMAP parameters:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MAPGTC - Gets a parameter value of type CHARACTER.
<dt>&bull;
<dd>MAPGTI - Gets a parameter value of type INTEGER.
<dt>&bull;
<dd>MAPGTL - Gets a parameter value of type LOGICAL.
<dt>&bull;
<dd>MAPGTR - Gets a parameter value of type REAL.</dl></dl><dt>Routines Used to Save and Restore Internal Parameters
<dd>To save/restore the current values of the internal parameters of EZMAP, use the following:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MAPSAV - Saves the values (by writing a record on a user-specified unit).
<dt>&bull;
<dd>MAPRST - Restores saved values (by reading a record from a user-specified unit).</dl></dl><dt>Routines Used to Draw Objects on a Map
<dd>To draw objects on the map, use the following routines:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MAPTRA - Computes the u/v coordinates of a point from its latitude and longitude. If the point is unprojectable or its projection lies outside the current perimeter, a special value is returned to signal this.
<dt>&bull;
<dd>MAPTRN - Computes the u/v coordinates of a point from its latitude and longitude. If the point is unprojectable, a special value is returned to signal this, but no check is made for the projected value being outside the perimeter.
<dt>&bull;
<dd>MAPFST - Does a &quot;pen-up&quot; move defining the start of a line to be projected and drawn. The line is defined by a series of lat/lon coordinates.
<dt>&bull;
<dd>MAPVEC - Does a &quot;pen-down&quot; move defining the continuation of a line to be projected and drawn. The line is defined by a series of lat/lon coordinates.
<dt>&bull;
<dd>MAPIT - Does &quot;pen-up&quot; or &quot;pen-down&quot; moves. This routine is called by MAPFST and MAPVEC.
<dt>&bull;
<dd>MAPIQ - Signals the end of a string of calls to MAPIT and causes its buffers to be flushed.
<dt>&bull;
<dd>MAPGCI - Given the latitudes and longitudes of two points on the surface of the globe, this routine returns the latitudes and longitudes of a specified number of points along the great circle route joining them.</dl></dl><dt>Routines Used to Do Inverse Transformations
<dd>The following routine was added to EZMAP early in 1992:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MAPTRI - Computes the latitude and longitude of a point from its u/v coordinates. If the point is outside the boundary of the map, a special value is returned.</dl></dl><dd>The example named &quot;mpex10&quot; shows one of the ways in which this routine may be used; it draws what is essentially a colored contour plot of a data field defined on the surface of the globe, using an orthographic projection.
<dt>Routines Used to Draw Solid-Filled Maps (EZMAPA)
<dd>In late 1986 or early 1987, a package of routines was written allowing a user to draw solid-filled maps of the globe. This package was named EZMAPA and was first advertised in the NCAR Graphics User's Guide (Version 2.00), published in August, 1987. Conceptually, the routines in this package are really part of EZMAP; they use the same common blocks and many of the same underlying low-level routines and they are affected by the same set of internal parameters as the routines in EZMAP proper. The routines of EZMAPA will be described in this document; to use them effectively, it will be necessary to understand also the package AREAS, which is described in a separate document. The EZMAPA routines are as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MAPBLA - Adds boundary lines to an existing area map. Routines in the package AREAS may then be used to process that area map in various ways. (Example: drawing a map of Europe with each country in a different color.) Note that this routine uses whichever old outline dataset is selected by the value of the internal parameter 'OU'; to access the new map database &quot;Earth..1&quot;, which was created in 1998, one must call instead the EZMAPB routine MPLNAM.
<dt>&bull;
<dd>MAPBLM - Draws boundary lines &quot;masked&quot; by an existing area map. (Example: drawing these lines only where they do not overlay CONPACK labels.) Note that this routine uses whichever old outline dataset is selected by the value of the internal parameter 'OU'; to access the new map database &quot;Earth..1&quot;, which was created in 1998, one must call instead the EZMAPB routine MPLNDM.
<dt>&bull;
<dd>MAPGRM - Draws lines of latitude and longitude &quot;masked&quot; by an existing area map. (Example: drawing these lines over water, but not over land.)
<dt>&bull;
<dd>MAPITA and MAPIQA - Adds to an area map the projections of arbitrary lines defined by lat/lon coordinates of points on the surface of the globe. MAPBLA uses these routines to add boundary lines to an area map; they may be called directly by the user to add his/her own set of boundary lines to the area map.
<dt>&bull;
<dd>MAPITM and MAPIQM - Draws, masked by an area map, the projections of arbitrary lines defined by lat/lon coordinates of points on the surface of the globe. MAPGRM uses these routines to draw masked lines of latitude and longitude; they may be called directly by the user to draw other masked lines.
<dt>&bull;
<dd>MAPACI - A function which, given the &quot;area identifier&quot; for a particular area defined by the boundaries in one of the old EZMAP outline datasets, returns a suggested color index for that area; it is guaranteed that, if the suggested color indices are used, no two areas having a boundary in common will have the same color. Note that this function should not be used to select color indices for areas defined by the new map database &quot;Earth..1&quot;, which was created in 1998; for that purpose, use EZMAPB functions instead (in particular, MPISCI).</dl></dl><dt>Routines Used to Access New Datasets (EZMAPB)
<dd>In early 1998, a new world map database, called &quot;Earth..1&quot;, was created for use with EZMAP; this database has higher-resolution coastlines, it has been updated to reflect many of the political changes that have taken place over the years since EZMAP came into existence, and it is structured differently, allowing for greater flexibility and ease of use and providing for easier changes and extensions in the future. 

 Each area defined by the database has 1) a &quot;area identifier&quot; (an integer uniquely identifying it), 2) an &quot;area type&quot; specifying its level in a hierarchy of areas, 3) a suggested color index, 4) an area identifier specifying its &quot;parent&quot; area (the area of which it is a part), and 5) a name. For example, there is an area named &quot;Madeline Island&quot; which is of type 4 (used for a state or a portion thereof) and has suggested color index 6. Its parent is an area named &quot;Wisconsin&quot;, which is also of type 4 and has suggested color index 6. The parent of &quot;Wisconsin&quot; is &quot;Conterminous US&quot;, which is of type 3 (used for a country or a portion thereof) and has suggested color index 3. The parent of &quot;Conterminous US&quot; is &quot;United States&quot;, which is also of type 3 and has suggested color index 3. The parent of &quot;United States&quot; is &quot;North America&quot;, which is of type 2 and has suggested color index 5. The parent of &quot;North America&quot; is &quot;Land&quot;, which is of type 1 and has suggested color index 2. The area named &quot;Land&quot; is at the top of the hierarchy and therefore has no parent (when you ask for the area identifier of its parent, you get a zero). 

 One may use the database at any of five specified hierarchical levels: 1 =&gt; land/water, 2 =&gt; continents, 3 =&gt; countries, 4 =&gt; states, and 5 =&gt; counties (so far, no counties are included). When the database is used at a particular level, entities that exist only at lower levels (larger level numbers) effectively disappear. 

 The new database was created from data available on the World Wide Web, using a new interactive editor based on NCAR Graphics. There are plans to make this editor available, so that a knowledgeable user can create a database tailored to his or her own needs: for example (assuming that one can obtain the necessary outline data), it should now be relatively easy to create and use a Pangaea database with EZMAP. 

 A new package of routines is used to access &quot;Earth..1&quot; and other databases in the same format; this package is called EZMAPB. Conceptually, the EZMAPB routines are just part of EZMAP; they use the same common blocks and many of the same underlying low-level routines and they are affected by the same set of internal parameters as the routines in EZMAP proper. 

 The principal EZMAPB routines are as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MPLNAM (MaP LiNes, to Area Map) - A routine to extract boundary lines from a specified database and send them to an area map.
<dt>&bull;
<dd>MPLNDM (MaP LiNes, Draw Masked) - A routine to extract boundary lines from a specified database and draw them, masked by the contents of an area map.
<dt>&bull;
<dd>MPLNDR (MaP LiNes, Draw) - A routine to extract boundary lines from a specified database and draw them.
<dt>&bull;
<dd>MPLNRI - A routine to force the reading of certain information from a database into labelled COMMON blocks inside EZMAP, so that subsequent references to some of the functions described below will have that information to work with. (Each of the routines MPLNAM, MPLNDM, and MPLNDR reads this data as a side effect; MPLNRI is provided for use in cases in which none of the other three routines has yet been called.)</dl></dl><dd>As each of the EZMAPB routines MPLNAM, MPLNDM, and MPLNDR processes boundary lines from a specified database, it calls an EZMAPB routine named MPCHLN (the default version of which does nothing):
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MPCHLN - A user-replaceable routine that can be made to change line style, color, line width, and so on as the boundary lines from a database are being drawn; it can also be made to delete particular lines or to change the area identifiers associated with them. The arguments of MPCHLN tell it which of the EZMAPB routines is calling it and whether it's being called before or after the line is processed; they also supply the &quot;line type&quot; of the line being drawn, the area identifiers of the areas on either side of it, and the actual coordinates defining the line. Line types are similar to area types (1 =&gt; land/water, 2 =&gt; continents, 3 =&gt; countries, 4 =&gt; states, and 5 =&gt; counties).</dl></dl><dd>Another EZMAPB routine, named MPGLTY, may be called by the user from within the line-processing routine specified by the final argument in a call to MPLNDM:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MPGLTY - Retrieves the line type of the line being drawn.</dl></dl><dd>There is a group of EZMAPB functions providing access to information about the areas defined by a database being used; these may be referenced at any time the appropriate information has been loaded into EZMAPB's common blocks (that is, after calling one of MPLNAM, MPLNDM, MPLNDR, or MPLNRI), but they are normally to be referenced from within the area-processing routine specified as the final argument in a call to the AREAS routine ARSCAM, in which they may be used to obtain information determining the manner in which the areas are to be rendered:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MPIPAI - A function whose value is non-zero if and only if the area with a specified area identifier is part of the area having a second specified area identifier.
<dt>&bull;
<dd>MPIPAN - A function whose value is non-zero if and only if the area with a specified area identifier is part of the area having a specified name.
<dt>&bull;
<dd>MPIOAR - A function whose value is the area identifier of the smallest area that is defined at or above a specified level in the area hierarchy and of which the area having a specified area identifier is a part.
<dt>&bull;
<dd>MPIATY - A function whose value is the type of the area having a specified area identifier.
<dt>&bull;
<dd>MPIPAR - A function whose value is the area identifier of the parent of the area having a specified area identifier.
<dt>&bull;
<dd>MPISCI - A function whose value is the suggested color index for an area having a specified area identifier.
<dt>&bull;
<dd>MPNAME - A function whose value is the name of the area having a particular area identifier.
<dt>&bull;
<dd>MPFNME - A function whose value is the full name of the area having a specified area identifier, up to a specified level in the hierarchy of areas; the full name of an area consists of its own name, preceded by the name of its parent, preceded by the name of its parent's parent, and so on; the various components of the name are separated by the 3-character string ' - ' (a blank, a dash, and another blank).</dl></dl><dd>Two additional EZMAPB functions are provided; these have nothing to do with mapping, really, but can be useful in dealing with character strings:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MPIFNB - A function whose value is the index of the first non-blank character in a character string.
<dt>&bull;
<dd>MPILNB - A function whose value is the index of the last non-blank character in a character string.</dl></dl><dt>Miscellaneous Other Routines
<dd>The following EZMAP routines are used for the purposes stated:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MAPRS - Re-executes the &quot;CALL SET&quot; done during the last call to MAPINT. This is useful when there has been an intervening call to a utility that calls SET. It is quite common for a background drawn by EZMAP to be placed in a flash buffer (as created by the package &quot;GFLASH&quot;). When the contents of the flash buffer are copied to the metafile being created, if it is desired to draw something on the EZMAP background, MAPRS may first have to be called to ensure that the correct SET call is in effect.
<dt>&bull;
<dd>MPRST - Resets the internal state of EZMAP/EZMAPA to the default.
<dt>&bull;
<dd>SUPMAP - Draws a map with a single call. An implementation of the routine from which EZMAP grew.</dl></dl>
</dl><h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 c_mapaci 
 c_mapbla 
 c_mapdrw 
 c_mapfst 
 c_mapgrd 
 c_mapgrm 
 c_mapgtc 
 c_mapgtc 
 c_mapgti 
 c_mapgtl 
 c_mapgtr 
 c_mapint 
 c_mapiq 
 c_mapiqa 
 c_mapiqm 
 c_mapit 
 c_mapita 
 c_mapitm 
 c_maplbl 
 c_maplot 
 c_mappos 
 c_maproj 
 c_maprs 
 c_maprst 
 c_mapsav 
 c_mapset 
 c_mapstc 
 c_mapsti 
 c_mapstl 
 c_mapstr 
 c_maptra 
 c_maptri 
 c_maptrn 
 c_mapvec 
 c_mpfnme 
 c_mpglty 
 c_mpiaty 
 c_mpifnb 
 c_mpilnb 
 c_mpiola 
 c_mpiosa 
 c_mpipai 
 c_mpipan 
 c_mpipar 
 c_mpisci 
 c_mplnam 
 c_mplndm 
 c_mplndr 
 c_mplnri 
 c_mpname 
 c_mprset 
 c_supmap
<h2>User-Modifiable Internal Routines</h2>The following EZMAP routines are used for the purposes stated:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>MAPUSR - This routine is called by various EZMAP routines just before and just after drawing parts of the map. By default, grid lines are drawn using software dashed lines and geographical outlines are drawn using either solid lines or dotted lines. The dash pattern used for the grid lines, the flag which says whether outlines are solid or dotted, and the color indices of various parts of the map are all user-settable parameters, but more complete control of color indices, spot size, dash pattern, etc., may be achieved by supplying one's own version of MAPUSR; a user version may be as complicated as is required to achieve a desired effect. Note that this routine is not called by any of the EZMAPB routines; they call MPCHLN instead.
<dt>&bull;
<dd>MAPEOD - This routine is called by the EZMAP routine MAPLOT and by the EZMAPA routines MAPBLA and MAPBLM; in each case, it is called once for each segment in the outline dataset. The user may supply a version which examines the segment to see if it ought to be plotted and, if not, to delete it. This can be used (for example) to reduce the clutter in northern Canada. Note that this routine is not called by any of the EZMAPB routines; they call MPCHLN instead.
<dt>&bull;
<dd>MPCHLN - This routine is called by the EZMAPB routines MPLNAM, MPLNDM, and MPLNDR; in each case, it is called just before and just after the processing of each segment in the map database. The default version does nothing; a user-supplied version can do for the new databases what MAPUSR and MAPEOD did for the old ones.</dl></dl><h2>Access</h2>To use EZMAP Fortran or C routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>When error conditions are detected, the support routine SETER is called. By default, SETER writes a message to the standard error file (as defined by <a HREF="/docs/linux/man/4-i1mach/">I1MACH</a>(4)) and then terminates execution. It is possible to put SETER into recovery mode and regain control after a recoverable error (which includes all of the possible errors). 

 The possible error messages are listed below. All errors are recoverable in the sense that a user program which has called ENTSR to set recovery mode will get control back after one of these errors occurs. 

 MAPBLA - UNCLEARED PRIOR ERROR 
 MAPCHI - ERROR EXIT FROM GQPLCI 
 MAPCHI - ERROR EXIT FROM GQPMCI 
 MAPCHI - ERROR EXIT FROM GQTXCI 
 MAPDRW - UNCLEARED PRIOR ERROR 
 MAPFST - UNCLEARED PRIOR ERROR 
 MAPGCI - UNCLEARED PRIOR ERROR 
 MAPGRD - UNCLEARED PRIOR ERROR 
 MAPGRM - UNCLEARED PRIOR ERROR 
 MAPGTC - UNCLEARED PRIOR ERROR 
 MAPGTC - UNKNOWN PARAMETER NAME 
 MAPGTI - UNCLEARED PRIOR ERROR 
 MAPGTI - UNKNOWN PARAMETER NAME 
 MAPGTL - UNCLEARED PRIOR ERROR 
 MAPGTL - UNKNOWN PARAMETER NAME 
 MAPGTR - UNCLEARED PRIOR ERROR 
 MAPGTR - UNKNOWN PARAMETER NAME 
 MAPINT - ANGULAR LIMITS TOO GREAT 
 MAPINT - ATTEMPT TO USE NON-EXISTENT PROJECTION 
 MAPINT - MAP HAS ZERO AREA 
 MAPINT - MAP LIMITS INAPPROPRIATE 
 MAPINT - UNCLEARED PRIOR ERROR 
 MAPIO - EOF ENCOUNTERED IN OUTLINE DATASET 
 MAPIO - ERROR ON READ OF OUTLINE DATASET 
 MAPIQ - UNCLEARED PRIOR ERROR 
 MAPIQA - UNCLEARED PRIOR ERROR 
 MAPIQM - UNCLEARED PRIOR ERROR 
 MAPIT - UNCLEARED PRIOR ERROR 
 MAPITA - UNCLEARED PRIOR ERROR 
 MAPITM - UNCLEARED PRIOR ERROR 
 MAPLBL - UNCLEARED PRIOR ERROR 
 MAPLMB - UNCLEARED PRIOR ERROR 
 MAPLOT - UNCLEARED PRIOR ERROR 
 MAPPOS - ARGUMENTS ARE INCORRECT 
 MAPPOS - UNCLEARED PRIOR ERROR 
 MAPROJ - UNCLEARED PRIOR ERROR 
 MAPROJ - UNKNOWN PROJECTION NAME 
 MAPRS - UNCLEARED PRIOR ERROR 
 MAPRST - EOF ON READ 
 MAPRST - ERROR ON READ 
 MAPRST - UNCLEARED PRIOR ERROR 
 MAPSAV - ERROR ON WRITE 
 MAPSAV - UNCLEARED PRIOR ERROR 
 MAPSET - UNCLEARED PRIOR ERROR 
 MAPSET - UNKNOWN MAP AREA SPECIFIER 
 MAPSTC - UNCLEARED PRIOR ERROR 
 MAPSTC - UNKNOWN OUTLINE NAME 
 MAPSTC - UNKNOWN PARAMETER NAME 
 MAPSTI - UNCLEARED PRIOR ERROR 
 MAPSTI - UNKNOWN PARAMETER NAME 
 MAPSTL - UNCLEARED PRIOR ERROR 
 MAPSTL - UNKNOWN PARAMETER NAME 
 MAPSTR - UNCLEARED PRIOR ERROR 
 MAPSTR - UNKNOWN PARAMETER NAME 
 MAPTRA - UNCLEARED PRIOR ERROR 
 MAPTRI - UNCLEARED PRIOR ERROR 
 MAPTRN - ATTEMPT TO USE NON-EXISTENT PROJECTION 
 MAPTRN - UNCLEARED PRIOR ERROR 
 MAPVEC - UNCLEARED PRIOR ERROR 
 MPGETC - UNCLEARED PRIOR ERROR 
 MPGETI - UNCLEARED PRIOR ERROR 
 MPGETL - UNCLEARED PRIOR ERROR 
 MPGETR - UNCLEARED PRIOR ERROR 
 MPLNAM - Can't form name of &quot;.names&quot; file 
 MPLNAM - Can't open the &quot;.lines&quot; file 
 MPLNAM - Can't open the &quot;.names&quot; file 
 MPLNAM - Read bad index from &quot;.names&quot; file 
 MPLNAM - Read error on &quot;.lines&quot; file 
 MPLNAM - Read error on &quot;.names&quot; file 
 MPLNAM - UNCLEARED PRIOR ERROR 
 MPLNDM - Can't form name of &quot;.names&quot; file 
 MPLNDM - Can't open the &quot;.lines&quot; file 
 MPLNDM - Can't open the &quot;.names&quot; file 
 MPLNDM - Read bad index from &quot;.names&quot; file 
 MPLNDM - Read error on &quot;.lines&quot; file 
 MPLNDM - Read error on &quot;.names&quot; file 
 MPLNDM - UNCLEARED PRIOR ERROR 
 MPLNDR - Can't form name of &quot;.names&quot; file 
 MPLNDR - Can't open the &quot;.lines&quot; file 
 MPLNDR - Can't open the &quot;.names&quot; file 
 MPLNDR - Read bad index from &quot;.names&quot; file 
 MPLNDR - Read error on &quot;.lines&quot; file 
 MPLNDR - Read error on &quot;.names&quot; file 
 MPLNDR - UNCLEARED PRIOR ERROR 
 MPLNRI - Can't form name of &quot;.names&quot; file 
 MPLNRI - Can't open the &quot;.names&quot; file 
 MPLNRI - Read bad index from &quot;.names&quot; file 
 MPLNRI - Read error on &quot;.names&quot; file 
 MPLNRI - UNCLEARED PRIOR ERROR 
 MPRSET - UNCLEARED PRIOR ERROR 
 MPSETC - UNCLEARED PRIOR ERROR 
 MPSETI - UNCLEARED PRIOR ERROR 
 MPSETL - UNCLEARED PRIOR ERROR 
 MPSETR - UNCLEARED PRIOR ERROR 
 SUPCON - UNCLEARED PRIOR ERROR 
 SUPMAP - UNCLEARED PRIOR ERROR 

<h2>See Also</h2>Online: ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
