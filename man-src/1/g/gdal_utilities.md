---
title: "gdal_utilities(1)"
name: "gdal_utilities"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_utilities/"
description: "gdal_utilities – GDAL Utilities The following utility programs are distributed with GDAL."
---

<h2 class="name">NAME</h2>
<p> gdal_utilities &#8211; GDAL Utilities The following utility programs are distributed with GDAL. </p>
<dl>
<dt>&bull;</p>
<dd> <code>gdalinfo</code> &#8211; report information about a file.</p>
<dt>&bull;</p>
<dd> <code>gdal_translate</code> &#8211; Copy a raster file, with control of output format.</p>
<dt>&bull;</p>
<dd> <code>gdaladdo</code> &#8211; Add overviews to a file.</p>
<dt>&bull;</p>
<dd> <code>gdalwarp</code> &#8211; Warp an image into a new coordinate system.</p>
<dt>&bull;</p>
<dd> <code>gdaltindex</code> &#8211; Build a MapServer raster tileindex.</p>
<dt>&bull;</p>
<dd> <code>gdalbuildvrt</code> &#8211; Build a VRT from a list of datasets.</p>
<dt>&bull;</p>
<dd> <code>gdal_contour</code> &#8211; Contours from DEM.</p>
<dt>&bull;</p>
<dd> <code>gdaldem</code> &#8211; Tools to analyze and visualize DEMs.</p>
<dt>&bull;</p>
<dd> <code>rgb2pct.py</code> &#8211; Convert a 24bit RGB image to 8bit paletted.</p>
<dt>&bull;</p>
<dd> <code>pct2rgb.py</code> &#8211; Convert an 8bit paletted image to 24bit RGB.</p>
<dt>&bull;</p>
<dd> <code>gdal_merge.py</code> &#8211; Build a quick mosaic from a set of images.</p>
<dt>&bull;</p>
<dd> <code>gdal2tiles.py</code> &#8211; Create a TMS tile structure, KML and simple web viewer.</p>
<dt>&bull;</p>
<dd> <code>gdal_rasterize</code> &#8211; Rasterize vectors into raster file.</p>
<dt>&bull;</p>
<dd> <code>gdaltransform</code> &#8211; Transform coordinates.</p>
<dt>&bull;</p>
<dd> <code>nearblack</code> &#8211; Convert nearly black/white borders to exact value.</p>
<dt>&bull;</p>
<dd> <code>gdal_retile.py</code> &#8211; Retiles a set of tiles and/or build tiled pyramid levels.</p>
<dt>&bull;</p>
<dd> <code>gdal_grid</code> &#8211; Create raster from the scattered data.</p>
<dt>&bull;</p>
<dd> <code>gdal_proximity.py</code> &#8211; Compute a raster proximity map.</p>
<dt>&bull;</p>
<dd> <code>gdal_polygonize.py</code> &#8211; Generate polygons from raster.</p>
<dt>&bull;</p>
<dd> <code>gdal_sieve.py</code> &#8211; Raster Sieve filter.</p>
<dt>&bull;</p>
<dd> <code>gdal_fillnodata.py</code> &#8211; Interpolate in nodata regions.</p>
<dt>&bull;</p>
<dd> <code>gdallocationinfo</code> &#8211; Query raster at a location.</p>
<dt>&bull;</p>
<dd> <code>gdalsrsinfo</code> &#8211; Report a given SRS in different formats. (GDAL &gt;= 1.9.0)</p>
<dt>&bull;</p>
<dd> <code>gdalmove.py</code> &#8211; Transform the coordinate system of a file (GDAL &gt;= 1.10)</p>
<dt>&bull;</p>
<dd> <code>gdal_edit.py</code> &#8211; Edit in place various information of an existing GDAL dataset (projection, geotransform, nodata, metadata)</p>
<dt>&bull;</p>
<dd> <code>gdal_calc.py</code> &#8211; Command line raster calculator with numpy syntax</p>
<dt>&bull;</p>
<dd> <code>gdal-config</code> &#8211; Get options required to build software using GDAL.</p>
<dt>&bull;</p>
<dd> <code>gdalmanage</code> &#8211; Identify, copy, rename and delete raster.</p>
<dt>&bull;</p>
<dd> <code>gdalcompare.py</code> &#8211; Compare two images and report on differences.</dl>
<h2>Creating New Files</h2>
<p> Access an existing file to read it is generally quite simple. Just indicate the name of the file or dataset on the commandline. However, creating a file is more complicated. It may be necessary to indicate the the format to create, various creation options affecting how it will be created and perhaps a coordinate system to be assigned. Many of these options are handled similarly by different GDAL utilities, and are introduced here. </p>
<dl>
<dt><code>-of</code> <i>format</i></p>
<dd> Select the format to create the new file as. The formats are assigned short names such as GTiff (for GeoTIFF) or HFA (for Erdas Imagine). The list of all format codes can be listed with the <code>&#8211;formats</code> switch. Only formats list as &#8216;(rw)&#8217; (read-write) can be written.</dl>
<p> Many utilities default to creating GeoTIFF files if a format is not specified. File extensions are not used to guess output format, nor are extensions generally added by GDAL if not indicated in the filename by the user. </p>
<dl>
<dt><code>-co</code> <i>NAME=VALUE</i></p>
<dd> Many formats have one or more optional creation options that can be used to control particulars about the file created. For instance, the GeoTIFF driver supports creation options to control compression, and whether the file should be tiled.</dl>
<p> The creation options available vary by format driver, and some simple formats have no creation options at all. A list of options supported for a format can be listed with the &#8216;&#8211;format &lt;format&gt;&#8217; commandline option but the web page for the format is the definitive source of information on driver creation options. </p>
<dl>
<dt><code>-a_srs</code> <i>SRS</i></p>
<dd> Several utilities, (gdal_translate and gdalwarp) include the ability to specify coordinate systems with commandline options like <code>-a_srs</code> (assign SRS to output), <code>-s_srs</code> (source SRS) and <code>-t_srs</code> (target SRS).</dl>
<p> These utilities allow the coordinate system (SRS = spatial reference system) to be assigned in a variety of formats. </p>
<dl>
<dt>&bull;</p>
<dd> <code>NAD27</code>/<code>NAD83</code>/<code>WGS84</code>/<code>WGS72</code>: These common geographic (lat/long) coordinate systems can be used directly by these names.</dl>
<dl>
<dt>&bull;</p>
<dd> <code>EPSG:</code><i>n</i>: Coordinate systems (projected or geographic) can be selected based on their EPSG codes, for instance EPSG:27700 is the British National Grid. A list of EPSG coordinate systems can be found in the GDAL data files gcs.csv and pcs.csv.</dl>
<dl>
<dt>&bull;</p>
<dd> <i>PROJ.4 Definitions</i>: A PROJ.4 definition string can be used as a coordinate system. For instance &#8216;+proj=utm +zone=11 +datum=WGS84&#8217;. Take care to keep the proj.4 string together as a single argument to the command (usually by double quoting).</dl>
<dl>
<dt>&bull;</p>
<dd> <i>OpenGIS Well Known Text</i>: The Open GIS Consortium has defined a textual format for describing coordinate systems as part of the Simple Features specifications. This format is the internal working format for coordinate systems used in GDAL. The name of a file containing a WKT coordinate system definition may be used a coordinate system argument, or the entire coordinate system itself may be used as a commandline option (though escaping all the quotes in WKT is quite challenging).</dl>
<dl>
<dt>&bull;</p>
<dd> <i>ESRI Well Known Text</i>: ESRI uses a slight variation on OGC WKT format in their ArcGIS product (ArcGIS .prj files), and these may be used in a similar manner to WKT files, but the filename should be prefixed with <code>ESRI::</code>. For example <code>&#8216;ESRI::NAD 1927 StatePlane Wyoming West FIPS 4904.prj&#8217;</code>.</dl>
<dl>
<dt>&bull;</p>
<dd> <i>Spatial References from URLs</i>: For example <a rel="nofollow" href="http://spatialreference.org/ref/user/north-pacific-albers-conic-equal-area/.">http://spatialreference.org/ref/user/north-pacific-albers-conic-equal-area/.</a></dl>
<dl>
<dt>&bull;</p>
<dd> <i>filename</i>: The name of a file containing WKT, PROJ.4 strings, or XML/GML coordinate system definitions can be provided.</dl>
<h2>General Command Line Switches</h2>
<p> All GDAL command line utility programs support the following &#8216;general&#8217; options. </p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Report the version of GDAL and exit.</dl>
<dl>
<dt><code>&#8211;formats</code></p>
<dd> List all raster formats supported by this GDAL build (read-only and read-write) and exit. The format support is indicated as follows: &#8216;ro&#8217; is read-only driver; &#8216;rw&#8217; is read or write (ie. supports CreateCopy); &#8216;rw+&#8217; is read, write and update (ie. supports Create). A &#8216;v&#8217; is appended for formats supporting virtual IO (/vsimem, /vsigzip, /vsizip, etc). A &#8216;s&#8217; is appended for formats supporting subdatasets. Note: The valid formats for the output of gdalwarp are formats that support the Create() method (marked as rw+), not just the CreateCopy() method.</dl>
<dl>
<dt><code>&#8211;format</code> <i>format</i></p>
<dd> List detailed information about a single format driver. The <i>format</i> should be the short name reported in the <code>&#8211;formats</code> list, such as GTiff.</dl>
<dl>
<dt><code>&#8211;optfile</code> <i>file</i></p>
<dd> Read the named file and substitute the contents into the commandline options list. Lines beginning with # will be ignored. Multi-word arguments may be kept together with double quotes.</dl>
<dl>
<dt><code>&#8211;config</code> <i>key value</i></p>
<dd> Sets the named configuration keyword to the given value, as opposed to setting them as environment variables. Some common configuration keywords are GDAL_CACHEMAX (memory used internally for caching in megabytes) and GDAL_DATA (path of the GDAL &#8216;data&#8217; directory). Individual drivers may be influenced by other configuration options.</dl>
<dl>
<dt><code>&#8211;debug</code> <i>value</i></p>
<dd> Control what debugging messages are emitted. A value of <i>ON</i> will enable all debug messages. A value of <i>OFF</i> will disable all debug messages. Another value will select only debug messages containing that string in the debug prefix code.</dl>
<dl>
<dt><code>&#8211;help-general</code></p>
<dd> Gives a brief usage message for the generic GDAL commandline options and exit.</dl>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
