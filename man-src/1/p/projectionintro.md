---
title: "projectionintro(1)"
name: "projectionintro"
section: "1"
letter: "p"
url: "/docs/linux/man/1-projectionintro/"
---

<h2>Projections and spatial transformations in GRASS GIS</h2>

<h3>Introduction</h3>

 A GRASS location is referenced with a single projection and coordinate system (or unreferenced as XY location). When creating a new location from an existing raster or vector map using the tools available from the startup screen or the map import commands, projection and coordinate system are defined. To change the projection of maps, a new location has to be created and the desired maps have to be reprojected into it from the source location as explained below.

<h3>Raster map projections</h3>

 Raster maps are backward projected in GRASS. This means that the user has to run the raster projection command (r.proj) in the target location and &quot;pull&quot; the map from the source location. Both locations need to have a projection defined.

<h3>Raster map transformation</h3>

 To transform an unprojected map from a XY location into a projected location (or another XY location), a forward transformation is performed. The unreferenced map is geocoded within the XY location by defining four corner points or by seeking several ground control points (i.target, i.points) and then transformed into the target location (i.rectify). Polynomial transformation of 1st, 2nd and 3rd order are supported. 

 A graphical user interface is provided by gis.m. 

 To simply translate a raster map (without stretching or rotation), the r.region command can be used.

<h3>Vector map projections</h3>

 Vector maps are backward projected in GRASS. This means that the user has to run the vector projection command (v.proj) in the target location and &quot;pull&quot; the map from the source location. Both locations need to have a projection defined.

<h3>Vector map transformation</h3>

 To transform an unprojected map (e.g. CAD map) into projected coordinates, a forward transformation is performed. The unreferenced map is imported into the location with projection and geocoded within this location by defining four corner points or by seeking several ground control points. These points are stored into an ASCII file and then transformed within the same location (v.transform). 

 A graphical user interface is provided by gis.m.

<h3>References</h3>

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 
&nbsp;<wbr>ASPRS Grids and Datum
<dt>
<dd> 
&nbsp;<wbr>Projections Transform List&nbsp;<wbr>(PROJ4)
<dt>
<dd> 
&nbsp;<wbr>MapRef - The Collection of Map Projections and Reference Systems for Europe
<dt>
<dd> 
&nbsp;<wbr>Information and Service System for European Coordinate Reference Systems - CRS</dl>
</dl>

<h3>See also</h3>

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Introduction to GRASS raster map processing
<dt>
<dd> Introduction to GRASS image processing
<dt>
<dd> Introduction to GRASS vector map processing</dl>
</dl>
 

 full index 

<h2>Index</h2>


