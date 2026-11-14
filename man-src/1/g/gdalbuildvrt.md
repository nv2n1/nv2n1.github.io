---
title: "gdalbuildvrt(1)"
name: "gdalbuildvrt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdalbuildvrt/"
description: "gdalbuildvrt – gdalbuildvrt Builds a VRT from a list of datasets. (compiled by default since GDAL 1.6.1)"
---

<h2 class="name">NAME</h2>
<p> gdalbuildvrt &#8211; gdalbuildvrt Builds a VRT from a list of datasets. (compiled by default since GDAL 1.6.1) </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdalbuildvrt[-tileindex field_name]
            [-resolution{highest | lowest | average | user}]
            [-te xmin ymin xmax ymax][-tr xres yres][-tap]
            [-separate][-b band][-sd subdataset]
            [-allow_projection_difference][-q]
            [-addalpha][-hidenodata]
            [-srcnodata "value [value...]"][-vrtnodata "value [value...]"]
            [-a_srs srs_def]
            [-input_file_list my_liste.txt][-overwrite] output.vrt[gdalfile] *
</code></pre>
<h2>DESCRIPTION</h2>
<p> This program builds a VRT (Virtual Dataset) that is a mosaic of the list of input GDAL datasets. The list of input GDAL datasets can be specified at the end of the command line, or put in a text file (one filename per line) for very long lists, or it can be a MapServer tileindex (see <code>gdaltindex</code> utility). In the later case, all entries in the tile index will be added to the VRT. </p>
<p> With -separate, each files goes into a separate <i>stacked</i> band in the VRT band. Otherwise, the files are considered as tiles of a larger mosaic and the VRT file has as many bands as one of the input files. </p>
<p> If one GDAL dataset is made of several subdatasets and has 0 raster bands, all the subdatasets will be added to the VRT rather than the dataset itself. </p>
<p> gdalbuildvrt does some amount of checks to assure that all files that will be put in the resulting VRT have similar characteristics : number of bands, projection, color interpretation&#8230; If not, files that do not match the common characteristics will be skipped. (This is only true in the default mode, and not when using the -separate option) </p>
<p> If there is some amount of spatial overlapping between files, the order may depend on the order they are inserted in the VRT file, but this behaviour should not be relied on. </p>
<p> This utility is somehow equivalent to the gdal_vrtmerge.py utility and is build by default in GDAL 1.6.1. </p>
<dl>
<dt><code>-tileindex</code>:</p>
<dd> Use the specified value as the tile index field, instead of the default value with is &#8216;location&#8217;.</dl>
<dl>
<dt><code>-resolution</code> {highest|lowest|average|user}:</p>
<dd> In case the resolution of all input files is not the same, the -resolution flag enables the user to control the way the output resolution is computed. &#8216;average&#8217; is the default. &#8216;highest&#8217; will pick the smallest values of pixel dimensions within the set of source rasters. &#8216;lowest&#8217; will pick the largest values of pixel dimensions within the set of source rasters. &#8216;average&#8217; will compute an average of pixel dimensions within the set of source rasters. &#8216;user&#8217; is new in GDAL 1.7.0 and must be used in combination with the -tr option to specify the target resolution.</dl>
<dl>
<dt><code>-tr</code> xres yres :</p>
<dd> (starting with GDAL 1.7.0) set target resolution. The values must be expressed in georeferenced units. Both must be positive values. Specifying those values is of course incompatible with highest|lowest|average values for -resolution option.</dl>
<dl>
<dt><code>-tap</code>:</p>
<dd> (GDAL &gt;= 1.8.0) (target aligned pixels) align the coordinates of the extent of the output file to the values of the -tr, such that the aligned extent includes the minimum extent.</dl>
<dl>
<dt><code>-te</code> xmin ymin xmax ymax :</p>
<dd> (starting with GDAL 1.7.0) set georeferenced extents of VRT file. The values must be expressed in georeferenced units. If not specified, the extent of the VRT is the minimum bounding box of the set of source rasters.</dl>
<dl>
<dt><code>-addalpha</code>:</p>
<dd> (starting with GDAL 1.7.0) Adds an alpha mask band to the VRT when the source raster have none. Mainly useful for RGB sources (or grey-level sources). The alpha band is filled on-the-fly with the value 0 in areas without any source raster, and with value 255 in areas with source raster. The effect is that a RGBA viewer will render the areas without source rasters as transparent and areas with source rasters as opaque. This option is not compatible with -separate.</dl>
<dl>
<dt><code>-hidenodata</code>:</p>
<dd> (starting with GDAL 1.7.0) Even if any band contains nodata value, giving this option makes the VRT band not report the NoData. Useful when you want to control the background color of the dataset. By using along with the -addalpha option, you can prepare a dataset which doesn&#8217;t report nodata value but is transparent in areas with no data.</dl>
<dl>
<dt><code>-srcnodata</code> <i>value [value&#8230;]</i>:</p>
<dd> (starting with GDAL 1.7.0) Set nodata values for input bands (different values can be supplied for each band). If more than one value is supplied all values should be quoted to keep them together as a single operating system argument. If the option is not specified, the intrinsic nodata settings on the source datasets will be used (if they exist). The value set by this option is written in the NODATA element of each ComplexSource element. Use a value of None to ignore intrinsic nodata settings on the source datasets.</dl>
<dl>
<dt><code>-b</code> <i>band</i>:</p>
<dd> (GDAL &gt;= 1.10.0) Select an input <i>band</i> to be processed. Bands are numbered from 1. If input bands not set all bands will be added to vrt</dl>
<dl>
<dt><code>-sd</code> <i>subdataset</i></p>
<dd> (GDAL &gt;= 1.10.0) If the input dataset contains several subdatasets use a subdataset with the specified number (starting from 1). This is an alternative of giving the full subdataset name as an input.</dl>
<dl>
<dt><code>-vrtnodata</code> <i>value [value&#8230;]</i>:</p>
<dd> (starting with GDAL 1.7.0) Set nodata values at the VRT band level (different values can be supplied for each band). If more than one value is supplied all values should be quoted to keep them together as a single operating system argument. If the option is not specified, intrinsic nodata settings on the first dataset will be used (if they exist). The value set by this option is written in the NoDataValue element of each VRTRasterBand element. Use a value of None to ignore intrinsic nodata settings on the source datasets.</dl>
<dl>
<dt><code>-separate</code>:</p>
<dd> (starting with GDAL 1.7.0) Place each input file into a separate <i>stacked</i> band. In that case, only the first band of each dataset will be placed into a new band. Contrary to the default mode, it is not required that all bands have the same datatype.</dl>
<dl>
<dt><code>-allow_projection_difference</code>:</p>
<dd> (starting with GDAL 1.7.0) When this option is specified, the utility will accept to make a VRT even if the input datasets have not the same projection. Note: this does not mean that they will be reprojected. Their projection will just be ignored.</dl>
<dl>
<dt><code>-a_srs</code> <i>srs_def</i>:</p>
<dd> (starting with GDAL 1.10) Override the projection for the output file. The <i>srs_def</i> may be any of the usual GDAL/OGR forms, complete WKT, PROJ.4, EPSG:n or a file containing the WKT.</dl>
<dl>
<dt><code>-input_file_list</code>:</p>
<dd> To specify a text file with an input filename on each line</dl>
<dl>
<dt><code>-q</code>:</p>
<dd> (starting with GDAL 1.7.0) To disable the progress bar on the console</dl>
<dl>
<dt><code>-overwrite</code>:</p>
<dd> Overwrite the VRT if it already exists.</dl>
<h2>EXAMPLE</h2>
<p> Make a virtual mosaic from all TIFF files contained in a directory : </p>
<pre>
gdalbuildvrt doq_index.vrt doq/*.tif
</pre>
<p> Make a virtual mosaic from files whose name is specified in a text file : </p>
<pre>
gdalbuildvrt -input_file_list my_liste.txt doq_index.vrt
</pre>
<p> Make a RGB virtual mosaic from 3 single-band input files : </p>
<pre>
gdalbuildvrt -separate rgb.vrt red.tif green.tif blue.tif
</pre>
<p> Make a virtual mosaic with blue background colour (RGB: 0 0 255) : </p>
<pre>
gdalbuildvrt -hidenodata -vrtnodata &quot;0 0 255&quot; doq_index.vrt doq/*.tif
</pre>
<h2>AUTHOR</h2>
<p> Even Rouault even.rouault [at] mines-paris.org </p>
<h2>Index</h2>
