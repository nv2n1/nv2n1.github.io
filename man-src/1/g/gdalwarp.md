---
title: "gdalwarp(1)"
name: "gdalwarp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdalwarp/"
description: "gdalwarp – gdalwarp image reprojection and warping utility"
---

<h2 class="name">NAME</h2>
<p> gdalwarp &#8211; gdalwarp image reprojection and warping utility </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdalwarp[--help - general][--formats]
        [-s_srs srs_def][-t_srs srs_def][-to "NAME=VALUE"]
        [-order n | -tps | -rpc | -geoloc][-et err_threshold]
        [-refine_gcps tolerance[minimum_gcps]]
        [-te xmin ymin xmax ymax][-tr xres yres][-tap][-ts width height]
        [-wo "NAME=VALUE"][-ot Byte / Int16 / ...][-wt Byte / Int16]
        [-srcnodata "value [value...]"][-dstnodata "value [value...]"] -
    dstalpha
            [-r resampling_method][-wm memory_in_mb][-multi][-q]
            [-cutline datasource][-cl layer][-cwhere expression]
            [-csql statement][-cblend dist_in_pixels][-crop_to_cutline]
            [-of format][-co "NAME=VALUE"] *
        [-overwrite]
            [-nomd][-cvmd meta_conflict_value][-setci] srcfile *dstfile
</code></pre>
<h2>DESCRIPTION</h2>
<p> The gdalwarp utility is an image mosaicing, reprojection and warping utility. The program can reproject to any supported projection, and can also apply GCPs stored with the image if the image is &#8216;raw&#8217; with control information. </p>
<dl>
<dt><code>-s_srs</code> <i>srs def</i>:</p>
<dd> source spatial reference set. The coordinate systems that can be passed are anything supported by the OGRSpatialReference.SetFromUserInput() call, which includes EPSG PCS and GCSes (ie. EPSG:4296), PROJ.4 declarations (as above), or the name of a .prf file containing well known text.</p>
<dt><code>-t_srs</code> <i>srs_def</i>:</p>
<dd> target spatial reference set. The coordinate systems that can be passed are anything supported by the OGRSpatialReference.SetFromUserInput() call, which includes EPSG PCS and GCSes (ie. EPSG:4296), PROJ.4 declarations (as above), or the name of a .prf file containing well known text.</p>
<dt><code>-to</code> <i>NAME=VALUE</i>:</p>
<dd> set a transformer option suitable to pass to GDALCreateGenImgProjTransformer2().</p>
<dt><code>-order</code> <i>n</i>:</p>
<dd> order of polynomial used for warping (1 to 3). The default is to select a polynomial order based on the number of GCPs.</p>
<dt><code>-tps</code>:</p>
<dd> Force use of thin plate spline transformer based on available GCPs.</p>
<dt><code>-rpc</code>:</p>
<dd> Force use of RPCs.</p>
<dt><code>-geoloc</code>:</p>
<dd> Force use of Geolocation Arrays.</p>
<dt><code>-et</code> <i>err_threshold</i>:</p>
<dd> error threshold for transformation approximation (in pixel units &#8211; defaults to 0.125).</p>
<dt><code>-refine_gcps</code> <i>tolerance minimum_gcps</i>:</p>
<dd> (GDAL &gt;= 1.9.0) refines the GCPs by automatically eliminating outliers. Outliers will be eliminated until minimum_gcps are left or when no outliers can be detected. The tolerance is passed to adjust when a GCP will be eliminated. Not that GCP refinement only works with polynomial interpolation. The tolerance is in pixel units if no projection is available, otherwise it is in SRS units. If minimum_gcps is not provided, the minimum GCPs according to the polynomial model is used.</p>
<dt><code>-te</code> <i>xmin ymin xmax ymax</i>:</p>
<dd> set georeferenced extents of output file to be created (in target SRS).</p>
<dt><code>-tr</code> <i>xres yres</i>:</p>
<dd> set output file resolution (in target georeferenced units)</p>
<dt><code>-tap</code>:</p>
<dd> (GDAL &gt;= 1.8.0) (target aligned pixels) align the coordinates of the extent of the output file to the values of the -tr, such that the aligned extent includes the minimum extent.</p>
<dt><code>-ts</code> <i>width height</i>:</p>
<dd> set output file size in pixels and lines. If width or height is set to 0, the other dimension will be guessed from the computed resolution. Note that -ts cannot be used with -tr</p>
<dt><code>-wo</code> <i>&#8216;NAME=VALUE&#8217;</i>:</p>
<dd> Set a warp options. The GDALWarpOptions::papszWarpOptions docs show all options. Multiple <code>-wo</code> options may be listed.</p>
<dt><code>-ot</code> <i>type</i>:</p>
<dd> For the output bands to be of the indicated data type.</p>
<dt><code>-wt</code> <i>type</i>:</p>
<dd> Working pixel data type. The data type of pixels in the source image and destination image buffers.</p>
<dt><code>-r</code> <i>resampling_method</i>:</p>
<dd> Resampling method to use. Available methods are:</p>
<dt><code>near</code>:</p>
<dd> nearest neighbour resampling (default, fastest algorithm, worst interpolation quality).</p>
<dt><code>bilinear</code>:</p>
<dd> bilinear resampling.</p>
<dt><code>cubic</code>:</p>
<dd> cubic resampling.</p>
<dt><code>cubicspline</code>:</p>
<dd> cubic spline resampling.</p>
<dt><code>lanczos</code>:</p>
<dd> Lanczos windowed sinc resampling.</p>
<dt><code>average</code>:</p>
<dd> average resampling, computes the average of all non-NODATA contributing pixels. (GDAL &gt;= 1.10.0)</p>
<dt><code>mode</code>:</p>
<dd> mode resampling, selects the value which appears most often of all the sampled points. (GDAL &gt;= 1.10.0)</dl>
<dl>
<dt><code>-srcnodata</code> <i>value [value&#8230;]</i>:</p>
<dd> Set nodata masking values for input bands (different values can be supplied for each band). If more than one value is supplied all values should be quoted to keep them together as a single operating system argument. Masked values will not be used in interpolation. Use a value of None to ignore intrinsic nodata settings on the source dataset.</p>
<dt><code>-dstnodata</code> <i>value [value&#8230;]</i>:</p>
<dd> Set nodata values for output bands (different values can be supplied for each band). If more than one value is supplied all values should be quoted to keep them together as a single operating system argument. New files will be initialized to this value and if possible the nodata value will be recorded in the output file. Use a value of None to ensure that nodata is not defined (GDAL&gt;=2.0). If this argument is not used then nodata values will be copied from the source dataset (GDAL&gt;=2.0).</p>
<dt><code>-dstalpha</code>:</p>
<dd> Create an output alpha band to identify nodata (unset/transparent) pixels.</p>
<dt><code>-wm</code> <i>memory_in_mb</i>:</p>
<dd> Set the amount of memory (in megabytes) that the warp API is allowed to use for caching.</p>
<dt><code>-multi</code>:</p>
<dd> Use multithreaded warping implementation. Multiple threads will be used to process chunks of image and perform input/output operation simultaneously.</p>
<dt><code>-q</code>:</p>
<dd> Be quiet.</p>
<dt><code>-of</code> <i>format</i>:</p>
<dd> Select the output format. The default is GeoTIFF (GTiff). Use the short format name.</p>
<dt><code>-co</code> <i>&#8216;NAME=VALUE&#8217;</i>:</p>
<dd> passes a creation option to the output format driver. Multiple <code>-co</code> options may be listed. See format specific documentation for legal creation options for each format.</dl>
<dl>
<dt><code>-cutline</code> <i>datasource</i>:</p>
<dd> Enable use of a blend cutline from the name OGR support datasource.</p>
<dt><code>-cl</code> <i>layername</i>:</p>
<dd> Select the named layer from the cutline datasource.</p>
<dt><code>-cwhere</code> <i>expression</i>:</p>
<dd> Restrict desired cutline features based on attribute query.</p>
<dt><code>-csql</code> <i>query</i>:</p>
<dd> Select cutline features using an SQL query instead of from a layer with -cl.</p>
<dt><code>-cblend</code> <i>distance</i>:</p>
<dd> Set a blend distance to use to blend over cutlines (in pixels).</p>
<dt><code>-crop_to_cutline</code>:</p>
<dd> (GDAL &gt;= 1.8.0) Crop the extent of the target dataset to the extent of the cutline.</p>
<dt><code>-overwrite</code>:</p>
<dd> (GDAL &gt;= 1.8.0) Overwrite the target dataset if it already exists.</p>
<dt><code>-nomd</code>:</p>
<dd> (GDAL &gt;= 1.10.0) Do not copy metadata. Without this option, dataset and band metadata (as well as some band information) will be copied from the first source dataset. Items that differ between source datasets will be set to * (see -cvmd option).</p>
<dt><code>-cvmd</code> <i>meta_conflict_value</i>:</p>
<dd> (GDAL &gt;= 1.10.0) Value to set metadata items that conflict between source datasets (default is &#8216;*&#8217;). Use &#8221; to remove conflicting items.</p>
<dt><code>-setci</code>:</p>
<dd> (GDAL &gt;= 1.10.0) Set the color interpretation of the bands of the target dataset from the source dataset.</dl>
<dl>
<dt><i>srcfile</i>:</p>
<dd> The source file name(s).</p>
<dt><i>dstfile</i>:</p>
<dd> The destination file name.</dl>
<p> Mosaicing into an existing output file is supported if the output file already exists. The spatial extent of the existing file will not be modified to accomodate new data, so you may have to remove it in that case, or use the -overwrite option. </p>
<p> Polygon cutlines may be used as a mask to restrict the area of the destination file that may be updated, including blending. If the OGR layer containing the cutline features has no explicit SRS, the cutline features must be in the SRS of the destination file. When outputing to a not yet existing target dataset, its extent will be the one of the original raster unless -te or -crop_to_cutline are specified.</p>
<h2>EXAMPLE</h2>
<p> For instance, an eight bit spot scene stored in GeoTIFF with control points mapping the corners to lat/long could be warped to a UTM projection with a command like this: </p>
<pre>
gdalwarp -t_srs '+proj=utm +zone=11 +datum=WGS84' raw_spot.tif utm11.tif
</pre>
<p> For instance, the second channel of an ASTER image stored in HDF with control points mapping the corners to lat/long could be warped to a UTM projection with a command like this: </p>
<pre>
gdalwarp HDF4_SDS:ASTER_L1B:&quot;pg-PR1B0000-2002031402_100_001&quot;:2 pg-PR1B0000-2002031402_100_001_2.tif
</pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Silke Reimer silke [at] intevation.de </p>
<h2>Index</h2>
