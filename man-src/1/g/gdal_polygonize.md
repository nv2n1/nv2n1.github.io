---

title: "gdal_polygonize(1)"
name: "gdal_polygonize"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_polygonize/"
description: "gdal_polygonize – gdal_polygonize.py produces a polygon feature layer from a raster"
---

<pre><code>
gdal_polygonize.py[-8][-nomask][-mask filename] raster_file[-b band]
                                                           [-q][-f ogr_format] out_file[layer][fieldname]
</code></pre>
<p> This utility creates vector polygons for all connected regions of pixels in the raster sharing a common pixel value. Each polygon is created with an attribute indicating the pixel value of that polygon. A raster mask may also be provided to determine which pixels are eligible for processing. </p>
<p> The utility will create the output vector datasource if it does not already exist, defaulting to GML format. </p>
<p> The utility is based on the GDALPolygonize() function which has additional details on the algorithm. </p>
<dl>
<dt><code>-8</code>:</dt>
<dd> (GDAL &gt;= 1.10) Use 8 connectedness. Default is 4 connectedness.</dd></dl>
<dl>
<dt><code>-nomask</code>:</dt>
<dd> Do not use the default validity mask for the input band (such as nodata, or alpha masks).</dd></dl>
<dl>
<dt><code>-mask</code> <i>filename</i>:</dt>
<dd> Use the first band of the specified file as a validity mask (zero is invalid, non-zero is valid).</dd></dl>
<dl>
<dt><i>raster_file</i></dt>
<dd> The source raster file from which polygons are derived.</dd></dl>
<dl>
<dt><code>-b</code> <i>band</i>:</dt>
<dd> The band on <i>raster_file</i> to build the polygons from.</dd></dl>
<dl>
<dt><code>-f</code> <i>ogr_format</i></dt>
<dd> Select the output format of the file to be created. Default is GML.</dd></dl>
<dl>
<dt><i>out_file</i></dt>
<dd> The destination vector file to which the polygons will be written.</dd></dl>
<dl>
<dt><i>layer</i></dt>
<dd> The name of the layer created to hold the polygon features.</dd></dl>
<dl>
<dt><i>fieldname</i></dt>
<dd> The name of the field to create (defaults to &#8216;DN&#8217;).</dd></dl>
<dl>
<dt><code>-q</code>:</dt>
<dd> The script runs in quiet mode. The progress monitor is supressed and routine messages are not displayed.</dd></dl>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com </p>
