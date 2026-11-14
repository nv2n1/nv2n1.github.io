---
title: "gdal_contour(1)"
name: "gdal_contour"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_contour/"
description: "gdal_contour – gdal_contour builds vector contour lines from a raster elevation model"
---

<h2 class="name">NAME</h2>
<p> gdal_contour &#8211; gdal_contour builds vector contour lines from a raster elevation model </p>
<h2>SYNOPSIS</h2>
<pre><code>
Usage : gdal_contour[-b&lt;band&gt;][-a&lt;attribute_name&gt;][-3d][-inodata]
                    [-snodata n][-i&lt;interval&gt;]
                    [-f&lt;formatname&gt;][[-dsco NAME = VALUE]...][[-lco NAME = VALUE]...]
                    [-off&lt;offset&gt;][-fl&lt;level&gt;&lt;level&gt;...]
                    [-nln&lt;outlayername&gt;]&lt;src_filename&gt;&lt;dst_filename&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> This program generates a vector contour file from the input raster elevation model (DEM). </p>
<p> Starting from version 1.7 the contour line-strings will be oriented consistently. The high side will be on the right, i.e. a line string goes clockwise around a top. </p>
<dl>
<dt><code>-b</code> <i>band</i>:</p>
<dd> picks a particular band to get the DEM from. Defaults to band 1.</dl>
<dl>
<dt><code>-a</code> <i>name</i>:</p>
<dd> provides a name for the attribute in which to put the elevation. If not provided no elevation attribute is attached.</p>
<dt><code>-3d</code>:</p>
<dd> Force production of 3D vectors instead of 2D. Includes elevation at every vertex.</dl>
<dl>
<dt><code>-inodata</code>:</p>
<dd> Ignore any nodata value implied in the dataset &#8211; treat all values as valid.</dl>
<dl>
<dt><code>-snodata</code> <i>value</i>:</p>
<dd> Input pixel value to treat as &#8216;nodata&#8217;.</dl>
<dl>
<dt><code>-f</code> <i>format</i>:</p>
<dd> create output in a particular format, default is shapefiles.</dl>
<dl>
<dt><code>-dsco</code> <i>NAME=VALUE</i>:</p>
<dd> Dataset creation option (format specific)</p>
<dt><code>-lco</code> <i>NAME=VALUE</i>:</p>
<dd> Layer creation option (format specific)</dl>
<dl>
<dt><code>-i</code> <i>interval</i>:</p>
<dd> elevation interval between contours.</dl>
<dl>
<dt><code>-off</code> <i>offset</i>:</p>
<dd> Offset from zero relative to which to interpret intervals.</dl>
<dl>
<dt><code>-fl</code> <i>level</i>:</p>
<dd> Name one or more &#8216;fixed levels&#8217; to extract.</p>
<dt><code>-nln</code> <i>outlayername</i>:</p>
<dd> Provide a name for the output vector layer. Defaults to &#8216;contour&#8217;.</dl>
<h2>EXAMPLE</h2>
<p> This would create 10meter contours from the DEM data in dem.tif and produce a shapefile in contour.shp/shx/dbf with the contour elevations in the &#8216;elev&#8217; attribute. </p>
<pre>
gdal_contour -a elev dem.tif contour.shp -i 10.0
</pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Silke Reimer silke [at] intevation.de </p>
<h2>Index</h2>
