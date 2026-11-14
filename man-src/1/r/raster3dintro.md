---
title: "raster3dintro(1)"
name: "raster3dintro"
section: "1"
letter: "r"
url: "/docs/linux/man/1-raster3dintro/"
---

<h2>3D Raster data (voxel) in GRASS GIS</h2>

<h3>3D Raster (voxel) import</h3>

 The module r3.in.ascii supports generic x,y,z import. Alternatively, voxels can be generated from 3D point vector data (v.to.rast3). Always the full map is imported. Volumes can also be created based on 2D elevation map(s) and value raster map(s) (r.to.rast3elev). Alternatively, a volume can be composed of several 2D raster map slices which are merged into one 3D raster volume map (r.to.rast3).

<h3>Voxel region settings and 3D MASK</h3>

 GRASS 3D raster map processing is always performed in the current 3D region settings (see g.region, <i>-p3</i> flags), i.e. the current region extent, vertical extent and current 3D resolution are used. If the 3D resolution differs from that of the input raster map(s), on-the-fly resampling is performed (nearest neighbor resampling). If this is not desired, the input map(s) has/have to be reinterpolated beforehand with one of the dedicated modules. Masks can be set (r3.mask).

<h3>Voxel operations</h3>

 Powerful 3D map algebra is implemented in r3.mapcalc.

<h3>Voxel conversion to vector or 2D raster maps</h3>

 3D vector point data can be converted to a GRASS 3D raster map (v.to.rast3). Layers from a 3D raster map can be converted to a 2D raster map (r3.to.rast). Cross sectional 2D raster map can be extracted from 3D raster map based on a 2D elevation map (r3.cross.rast).

<h3>Voxel statistics</h3>

 Volume statistics can be calculated with r3.stats and r3.univar.

<h3>Voxel interpolation</h3>

 From 3D vector points, GRASS 3D raster maps can be interpolated (v.vol.rst). Results are volumes, or 2D raster maps can be also extracted.

<h3>Voxel export</h3>

 GRASS 3D raster maps can be exported to VTK (r3.out.vtk). VTK files can be visualized with the <i>VTK Toolkit</i>, <i>Paraview</i> and <i>MayaVi</i>. GRASS 2D raster maps can be exported to VTK with r.out.vtk, GRASS vector maps can be exported to VTK with v.out.vtk. 

 Alternatively, GRASS 3D raster maps can be imported and exported from/to Vis5D (r3.out.v5d). Note that Vis5D is limited in the number of supported voxels. 

 Finally, export to 3D ASCII is also available (r3.out.ascii).

<h3>See also</h3>

 Introduction to GRASS raster map processing 

 full index 

<h2>Index</h2>


