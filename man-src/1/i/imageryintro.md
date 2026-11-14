---
title: "imageryintro(1)"
name: "imageryintro"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imageryintro/"
---

<h2>Image processing in GRASS GIS</h2>
<h3>Image data in general</h3>
<p> In GRASS, image data are identical to raster data. However, a couple of commands are explicitly dedicated to image processing. The geographic boundaries of the raster/imagery file are described by the north, south, east, and west fields. These values describe the lines which bound the map at its edges. These lines do NOT pass through the center of the grid cells at the edge of the map, but along the edge of the map itself. </p>
<p> As a general rule in GRASS:</p>
<dl>
<dt><code>1</code></p>
<dd>
&nbsp;<wbr>Raster/imagery output maps have their bounds and resolution equal to those of the current region.</p>
<dt><code>2</code></p>
<dd>
&nbsp;<wbr>Raster/imagery input maps are automatically cropped/padded and rescaled (using nearest-neighbor resampling) to match the current region.</dl>
<h3>Raster import</h3>
<p> The module r.in.gdal offers a common interface for many different raster and satellite image formats. Additionally, it also offers options such as on-the-fly location creation or extension of the default region to match the extent of the imported raster map. For special cases, other import modules are available. Always the full map is imported. Imagery data can be group (e.g. channel-wise) with i.group. </p>
<p> For importing scanned maps, the user will need to create a x,y-location, scan the map in the desired resolution and save it into an appropriate raster format (e.g. tiff, jpeg, png, pbm) and then use r.in.gdal to import it. Based on reference points the scanned map can be rectified to obtain geocoded data.</p>
<h3>Image processing operations</h3>
<p> GRASS raster/imagery map processing is always performed in the current region settings (see g.region), i.e. the current region extent and current raster resolution is used. If the resolution differs from that of the input raster map(s), on-the-fly resampling is performed (nearest neighbor resampling). If this is not desired, the input map(s) has/have to be resampled beforehand with one of the dedicated modules.</p>
<h3>Geocoding of imagery data</h3>
<p> GRASS is able to geocode raster and image data of various types:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> unreferenced scanned maps by defining four corner points (i.target, i.rectify)</p>
<dt>
<dd> unreferenced satellite data from optical and Radar sensors by defining a certain number of ground control points (i.target, i.rectify)</p>
<dt>
<dd> orthophoto based on DEM: i.ortho.photo</p>
<dt>
<dd> digital handheld camera geocoding: modified procedure for i.ortho.photo</dl>
</dl>
<h3>Visualizing (true) color composites</h3>
<p> To quickly combine the first three channels to a near natural color image, the GRASS command d.rgb can be used or the graphical GIS manager (gis.m). It assigns each channel to a color which is then mixed while displayed. With a bit more work of tuning the grey scales of the channels, nearly perfect colors can be achieved. Channel histograms can be shown with d.histogram.</p>
<h3>Calculation of vegetation indices</h3>
<p> An example for indices derived from multispectral data is the NDVI (normalized difference vegetation index). To study the vegetation status with NDVI, the Red and the Near Infrared channels (NIR) are taken as used as input for simple map algebra in the GRASS command r.mapcalc (ndvi = 1.0 * (nir &#8211; red)/(nir + red)). With r.colors an optimized &quot;ndvi&quot; color table can be assigned afterward. Also other vegetation indices can be generated likewise.</p>
<h3>Calibration of thermal channel</h3>
<p> The encoded digital numbers of a thermal infrared channel can be transformed to degree Celsius (or other temperature units) which represent the temperature of the observed land surface. This requires a few algebraic steps with r.mapcalc which are outlined in the literature to apply gain and bias values from the image metadata.</p>
<h3>Image classification</h3>
<p> Single and multispectral data can be classified to user defined land use/land cover classes. In case of a single channel, segmentation will be used. GRASS supports the following methods:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
&nbsp;<wbr>Radiometric classification:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
&nbsp;<wbr>Unsupervised classification&nbsp;<wbr>(i.cluster, i.maxlik) using the Maximum Likelihood classification method</p>
<dt>
<dd>
&nbsp;<wbr>Supervised classification&nbsp;<wbr>(i.gensig or i.maxlik) using the Maximum Likelihood classification method</dl>
</dl>
<p> Combined radiometric/geometric (segmentation based) supervised classification (i.gensigset, i.smap)</dl>
</dl>
<p> Kappa statistic can be calculated to validate the results (r.kappa).</p>
<h3>Image fusion</h3>
<p> In case of using multispectral data, improvements of the resolution can be gained by merging the panchromatic channel with color channels. GRASS provides the HIS (i.rgb.his, i.his.rgb) and the Brovey transform (i.fusion.brovey) methods.</p>
<h3>Time series processing</h3>
<p> GRASS also offers support for time series processing (&lt;a href=&quot;r.series.html&quot;&gt;r.series). Statistics can be derived from a set of coregistered input maps such as multitemporal satellite data. The common univariate statistics and also linear regression can be calculated.</p>
<h3>See also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The GRASS 4 <i>Image Processing manual</i></p>
<dt>
<dd> Introduction to GRASS 2D raster map processing</p>
<dt>
<dd> Introduction to GRASS 3D raster map (voxel) processing</p>
<dt>
<dd> Introduction to GRASS vector map processing</dl>
</dl>
<p> imagery index &#8211; full index </p>
<h2>Index</h2>
