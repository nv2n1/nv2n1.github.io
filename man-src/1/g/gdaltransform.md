---
title: "gdaltransform(1)"
name: "gdaltransform"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdaltransform/"
description: "gdaltransform – gdaltransform transforms coordinates"
---

<h2 class="name">NAME</h2>
<p> gdaltransform &#8211; gdaltransform transforms coordinates </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdaltransform[--help - general]
             [-i][-s_srs srs_def][-t_srs srs_def][-to "NAME=VALUE"]
             [-order n][-tps][-rpc][-geoloc]
             [-gcp pixel line easting northing[elevation]] *
    [srcfile[dstfile]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The gdaltransform utility reprojects a list of coordinates into any supported projection,including GCP-based transformations. </p>
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
<dt><code>-i</code></p>
<dd> Inverse transformation: from destination to source.</p>
<dt><code>-gcp</code><i>pixel line easting northing [elevation]</i>:</p>
<dd> Provide a GCP to be used for transformation (generally three or more are required)</p>
<dt><i>srcfile</i>:</p>
<dd> File with source projection definition or GCP&#8217;s. If not given, source projection is read from the command-line -s_srs or -gcp parameters</p>
<dt><i>dstfile</i>:</p>
<dd> File with destination projection definition.</dl>
<p> Coordinates are read as pairs (or triples) of numbers per line from standard input, transformed, and written out to standard output in the same way. All transformations offered by gdalwarp are handled, including gcp-based ones. </p>
<p> Note that input and output must always be in decimal form. There is currently no support for DMS input or output. </p>
<p> If an input image file is provided, input is in pixel/line coordinates on that image. If an output file is provided, output is in pixel/line coordinates on that image.</p>
<h2>Image RPC Example</h2>
<p> Simple reprojection from one projected coordinate system to another: </p>
<pre>
gdaltransform -s_srs EPSG:28992 -t_srs EPSG:31370
177502 311865
</pre>
<p> Produces the following output in meters in the &#8216;Belge 1972 / Belgian Lambert 72&#8217; projection: </p>
<pre>
244510.77404604 166154.532871342 -1046.79270555763
</pre>
<h2>Image RPC Example</h2>
<p> The following command requests an RPC based transformation using the RPC model associated with the named file. Because the -i (inverse) flag is used, the transformation is from output georeferenced (WGS84) coordinates back to image coordinates. </p>
<pre>
gdaltransform -i -rpc 06OCT20025052-P2AS-005553965230_01_P001.TIF
125.67206 39.85307 50                    
</pre>
<p> Produces this output measured in pixels and lines on the image: </p>
<pre>
3499.49282422381 2910.83892848414 50
</pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Jan Hartmann j.l.h.hartmann [at] uva.nl </p>
<h2>Index</h2>
