---
title: "gdal2tiles(1)"
name: "gdal2tiles"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal2tiles/"
description: "gdal2tiles – gdal2tiles.py generates directory with TMS tiles, KMLs and simple web viewers"
---

<h2 class="name">NAME</h2>
<p> gdal2tiles &#8211; gdal2tiles.py generates directory with TMS tiles, KMLs and simple web viewers </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdal2tiles.py[-p profile][-r resampling][-s srs][-z zoom]
             [-e][-a nodata][-v][-h][-k][-n][-u url]
             [-w webviewer][-t title][-c copyright]
             [-g googlekey][-b bingkey] input_file[output_dir]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This utility generates a directory with small tiles and metadata, following the OSGeo Tile Map Service Specification. Simple web pages with viewers based on Google Maps and OpenLayers are generated as well &#8211; so anybody can comfortably explore your maps on-line and you do not need to install or configure any special software (like MapServer) and the map displays very fast in the web browser. You only need to upload the generated directory onto a web server. </p>
<p> GDAL2Tiles also creates the necessary metadata for Google Earth (KML SuperOverlay), in case the supplied map uses EPSG:4326 projection. </p>
<p> World files and embedded georeferencing is used during tile generation, but you can publish a picture without proper georeferencing too. </p>
<dl>
<dt><code>-p</code> <i>PROFILE</i>, &#8211;profile=<i>PROFILE</i>:</p>
<dd> Tile cutting profile (mercator,geodetic,raster) &#8211; default &#8216;mercator&#8217; (Google Maps compatible).</p>
<dt><code>-r</code> <i>RESAMPLING</i>, &#8211;resampling=<i>RESAMPLING</i>:</p>
<dd> Resampling method (average,near,bilinear,cubic,cubicspline,lanczos,antialias) &#8211; default &#8216;average&#8217;.</p>
<dt><code>-s</code> <i>SRS</i>, &#8211;s_srs=<i>SRS</i>:</p>
<dd> The spatial reference system used for the source input data.</p>
<dt><code>-z</code> <i>ZOOM</i>, &#8211;zoom=<i>ZOOM</i>:</p>
<dd> Zoom levels to render (format:&#8217;2-5&#8242; or &#8217;10&#8217;).</p>
<dt><code>-e</code>, &#8211;resume:</p>
<dd> Resume mode. Generate only missing files.</p>
<dt><code>-a</code> <i>NODATA</i>, &#8211;srcnodata=<i>NODATA</i>:</p>
<dd> NODATA transparency value to assign to the input data.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Generate verbose output of tile generation.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show help message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show program&#8217;s version number and exit.</dl>
<p> <code>KML (Google Earth) options:</code> </p>
<p> Options for generated Google Earth SuperOverlay metadata</p>
<dl>
<dt><code>-k, &#8211;force-kml</code></p>
<dd> Generate KML for Google Earth &#8211; default for &#8216;geodetic&#8217; profile and &#8216;raster&#8217; in EPSG:4326. For a dataset with different projection use with caution!</p>
<dt><code>-n, &#8211;no-kml</code>:</p>
<dd> Avoid automatic generation of KML files for EPSG:4326.</p>
<dt><code>-u</code> <i>URL</i>, &#8211;url=<i>URL</i>:</p>
<dd> URL address where the generated tiles are going to be published.</dl>
<p> <code>Web viewer options:</code> </p>
<p> Options for generated HTML viewers a la Google Maps</p>
<dl>
<dt><code>-w</code> <i>WEBVIEWER</i>, &#8211;webviewer=<i>WEBVIEWER</i>:</p>
<dd> Web viewer to generate (all,google,openlayers,none) &#8211; default &#8216;all&#8217;.</p>
<dt><code>-t</code> <i>TITLE</i>, &#8211;title=<i>TITLE</i>:</p>
<dd> Title of the map.</p>
<dt><code>-c</code> <i>COPYRIGHT</i>, &#8211;copyright=<i>COPYRIGHT</i>:</p>
<dd> Copyright for the map.</p>
<dt><code>-g</code> <i>GOOGLEKEY</i>, &#8211;googlekey=<i>GOOGLEKEY</i>:</p>
<dd> Google Maps API key from <a rel="nofollow" href="http://code.google.com/apis/maps/signup.html.">http://code.google.com/apis/maps/signup.html.</a></p>
<dt><code>-b</code> <i>BINGKEY</i>, &#8211;bingkey=<i>BINGKEY</i>:</p>
<dd> Bing Maps API key from <a rel="nofollow" href="https://www.bingmapsportal.com/">https://www.bingmapsportal.com/</a></dl>
<p> NOTE: gdal2tiles.py is a Python script that needs to be run against &#8216;new generation&#8217; Python GDAL binding.</p>
<h2>AUTHORS</h2>
<p> Klokan Petr Pridal klokan [at] klokan.cz as a Google SoC 2007 Project. </p>
<h2>Index</h2>
