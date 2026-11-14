---
title: "gdallocationinfo(1)"
name: "gdallocationinfo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdallocationinfo/"
description: "gdallocationinfo – gdallocationinfo raster query tool"
---

<h2 class="name">NAME</h2>
<p> gdallocationinfo &#8211; gdallocationinfo raster query tool </p>
<h2>SYNOPSIS</h2>
<pre><code>
Usage : gdallocationinfo[--help - general][-xml][-lifonly][-valonly]
                        [-b band] *
        [-overview overview_level]
            [-l_srs srs_def][-geoloc][-wgs84] srcfile[x y]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The gdallocationinfo utility provide a mechanism to query information about a pixel given it&#8217;s location in one of a variety of coordinate systems. Several reporting options are provided. </p>
<dl>
<dt><code>-xml</code>:</p>
<dd> The output report will be XML formatted for convenient post processing.</dl>
<dl>
<dt><code>-lifonly</code>:</p>
<dd> The only output is filenames production from the LocationInfo request against the database (ie. for identifying impacted file from VRT).</dl>
<dl>
<dt><code>-valonly</code>:</p>
<dd> The only output is the pixel values of the selected pixel on each of the selected bands.</dl>
<dl>
<dt><code>-b</code> <i>band</i>:</p>
<dd> Selects a band to query. Multiple bands can be listed. By default all bands are queried.</dl>
<dl>
<dt><code>-overview</code> <i>overview_level</i>:</p>
<dd> Query the (overview_level)th overview (overview_level=1 is the 1st overview), instead of the base band. Note that the x,y location (if the coordinate system is pixel/line) must still be given with respect to the base band.</dl>
<dl>
<dt><code>-l_srs</code> <i>srs def</i>:</p>
<dd> The coordinate system of the input x, y location.</dl>
<dl>
<dt><code>-geoloc</code>:</p>
<dd> Indicates input x,y points are in the georeferencing system of the image.</dl>
<dl>
<dt><code>-wgs84</code>:</p>
<dd> Indicates input x,y points are WGS84 long, lat.</dl>
<dl>
<dt><i>srcfile</i>:</p>
<dd> The source GDAL raster datasource name.</dl>
<dl>
<dt><i>x</i>:</p>
<dd> X location of target pixel. By default the coordinate system is pixel/line unless -l_srs, -wgs84 or -geoloc supplied.</dl>
<dl>
<dt><i>y</i>:</p>
<dd> Y location of target pixel. By default the coordinate system is pixel/line unless -l_srs, -wgs84 or -geoloc supplied.</dl>
<p> This utility is intended to provide a variety of information about a pixel. Currently it reports three things: </p>
<dl>
<dt>&bull;</p>
<dd> The location of the pixel in pixel/line space.</p>
<dt>&bull;</p>
<dd> The result of a LocationInfo metadata query against the datasource &#8211; currently this is only implemented for VRT files which will report the file(s) used to satisfy requests for that pixel.</p>
<dt>&bull;</p>
<dd> The raster pixel value of that pixel for all or a subset of the bands.</p>
<dt>&bull;</p>
<dd> The unscaled pixel value if a Scale and/or Offset apply to the band.</dl>
<p> The pixel selected is requested by x/y coordinate on the commandline, or read from stdin. More than one coordinate pair can be supplied when reading coordinatesis from stdin. By default pixel/line coordinates are expected. However with use of the -geoloc, -wgs84, or -l_srs switches it is possible to specify the location in other coordinate systems. </p>
<p> The default report is in a human readable text format. It is possible to instead request xml output with the -xml switch. </p>
<p> For scripting purposes, the -valonly and -lifonly switches are provided to restrict output to the actual pixel values, or the LocationInfo files identified for the pixel. </p>
<p> It is anticipated that additional reporting capabilities will be added to gdallocationinfo in the future.</p>
<h2>EXAMPLE</h2>
<p> Simple example reporting on pixel (256,256) on the file utm.tif. </p>
<pre>
$ gdallocationinfo utm.tif 256 256
Report:
  Location: (256P,256L)
  Band 1:
    Value: 115
</pre>
<p> Query a VRT file providing the location in WGS84, and getting the result in xml. </p>
<pre>
$ gdallocationinfo -xml -wgs84 utm.vrt -117.5 33.75
&lt;Report pixel=&quot;217&quot; line=&quot;282&quot;&gt;
  &lt;BandReport band=&quot;1&quot;&gt;
    &lt;LocationInfo&gt;
      &lt;File&gt;utm.tif&lt;/File&gt;
    &lt;/LocationInfo&gt;
    &lt;Value&gt;16&lt;/Value&gt;
  &lt;/BandReport&gt;
&lt;/Report&gt;
</pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com </p>
<h2>Index</h2>
