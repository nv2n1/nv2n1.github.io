---
title: "rasterintro(1)"
name: "rasterintro"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rasterintro/"
---

<h2>Raster data processing in GRASS GIS</h2>
<h3>Raster maps in general</h3>
<p> The geographic boundaries of the raster map are described by the north, south, east, and west fields. These values describe the lines which bound the map at its edges. These lines do NOT pass through the center of the grid cells at the edge of the map, but along the edge of the map itself. </p>
<p> As a general rule in GRASS:</p>
<dl>
<dt><code>1</code></p>
<dd>
&nbsp;<wbr>Raster output maps have their bounds and resolution equal to those of the current region.</p>
<dt><code>2</code></p>
<dd>
&nbsp;<wbr>Raster input maps are automatically cropped/padded and rescaled (using nearest-neighbour resampling) to match the current region.</p>
<dt><code>3</code></p>
<dd>
&nbsp;<wbr>Raster input maps are automatically masked if a raster map named MASK exists.</dl>
<p> There are a few exceptions to this: r.in.* programs read the data cell-for-cell, with no resampling. When reading non-georeferenced data, the imported map will usually have its lower-left corner at (0,0) in the location&#8217;s coordinate system; the user needs to use r.region to &quot;place&quot; the imported map. </p>
<p> Some programs which need to perform specific types of resampling (e.g. r.resamp.rst) read the input maps at their original resolution then do the resampling themselves. </p>
<p> r.proj has to deal with two regions (source and destination) simultaneously; both will have an impact upon the final result.</p>
<h3>Raster import and export</h3>
<p> The module r.in.gdal offers a common interface for many different raster formats. Additionally, it also offers options such as on-the-fly location creation or extension of the default region to match the extent of the imported raster map. For special cases, other import modules are available. Always the full map is imported. </p>
<p> For importing scanned maps, the user will need to create a x,y-location, scan the map in the desired resolution and save it into an appropriate raster format (e.g. tiff, jpeg, png, pbm) and then use r.in.gdal to import it. Based on reference points the scanned map can be recified to obtain geocoded data. </p>
<p> Raster maps are exported with r.out.gdal into common formats. Also r.out.bin, r.out.vtk and other export modules are available.</p>
<h3>Metadata</h3>
<p> The r.info module displays general information about a map such as region extent, data range, data type, creation history, and other metadata. Metadata such as map title, units, vertical datum etc. can be updated with r.support. Timestamps are managed with r.timestamp. Region extent and resolution are mangaged with r.region.</p>
<h3>Raster map operations</h3>
<p> GRASS raster map processing is always performed in the current region settings (see g.region), i.e. the current region extent and current raster resolution is used. If the resolution differs from that of the input raster map(s), on-the-fly resampling is performed (nearest neighbor resampling). If this is not desired, the input map(s) has/have to be resampled beforehand with one of the dedicated modules. </p>
<p> If a raster map named &quot;MASK&quot; exists, most GRASS raster modules will operate only on data falling inside the masked area, and treat any data falling outside of the mask as if its value were NULL. The mask is only applied when <i>reading</i> an existing GRASS raster map, for example when used in a module as an input map. (see r.mask)</p>
<h3>Raster map statistics</h3>
<p> A couple of commands are available to calculate local statistics (r.neighbors), and global statistics (r.surf.area, r.sum). Profiles and transects can be generated (r.profile, r.transect) as well as histograms (d.histogram) and polar diagrams (d.polar). Univariate statistics (r.univar) and reports are also available (r.report,&lt;a href=&quot;r.stats.html&quot;&gt;r.stats, r.volume).</p>
<h3>Raster map algebra and aggregation</h3>
<p> The r.mapcalc command provides raster map algebra methods. The r.resamp.stats command resamples raster map layers using various aggregation methods, the r.average command aggregates one map based on a second map. r.resamp.interp resamples raster map layers using interpolation.</p>
<h3>Raster map resampling and interpolation methods</h3>
<p> GRASS offers various raster resampling and interpolation methods:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
&nbsp;<wbr>Resampling with nearest neighbor, bilinear, and bicubic method (r.resamp.interp)</p>
<dt>
<dd>
&nbsp;<wbr>Inverse distance weighted average&nbsp;<wbr>(IDW)&nbsp;<wbr>interpolation (r.surf.idw2)</p>
<dt>
<dd>
&nbsp;<wbr>Regularized spline with tension&nbsp;<wbr>(RST)&nbsp;<wbr>interpolation 2D (r.resamp.rst)</p>
<dt>
<dd>
&nbsp;<wbr>Bilinear interpolation&nbsp;<wbr>(r.bilinear)</p>
<dt>
<dd>
&nbsp;<wbr>Interpolating from contour lines&nbsp;<wbr>(r.contour)</dl>
</dl>
<h3>Hydrologic modeling toolbox</h3>
<p> Watershed modeling related modules are r.basins.fill, r.water.outlet, r.watershed, and r.terraflow. Water flow related modules are r.carve, r.drain, r.fill.dir, r.fillnulls, r.flow, and r.topidx. Flooding can be simulated with r.lake. Hydrologic simulation model are available as r.sim.sediment, r.sim.water, and r.topmodel.</p>
<h3>Raster format</h3>
<p> Raster data can be stored in GRASS as a 2D integer grid, 2D floating point grid (single or double precision), or as a 3D floating point grid (single or double precision). The internal raster format is architecture independent and portable between 32bit and 64bit machines. Internally, the integer format is called CELL, single precision floating point is called FCELL, double precision floating point is DCELL, and 3D raster is called GRID3D. The choice of the integer or floating point data depends on the application. </p>
<p> GRASS distinguishes NULL and zero. When working with NULL data, it is important to know that operations on NULL cells lead to NULL cells.</p>
<h3>See also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Introduction to GRASS vector map processing</p>
<dt>
<dd> Introduction to GRASS 3D raster map (voxel) processing</dl>
</dl>
<p> raster index &#8211; full index </p>
<h2>Index</h2>
