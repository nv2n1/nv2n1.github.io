---

title: "gdal_edit(1)"
name: "gdal_edit"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal_edit/"
description: "gdal_edit – gdal_edit.py Edit in place various information of an existing GDAL dataset"
---

<pre><code>
gdal_edit[--help - general][-ro][-a_srs srs_def][-a_ullr ulx uly lrx lry]
         [-tr xres yres][-unsetgt][-a_nodata value]
         [-gcp pixel line easting northing[elevation]] *
    [-mo "META-TAG=VALUE"] * datasetname
</code></pre>
<p> The gdal_edit.py script can be used to allows to edit in place various information of an existing GDAL dataset (projection, geotransform, nodata, metadata). </p>
<p> It works only with raster formats that support update access to existing datasets.</p>
<dl>
<dt><code>&#8211;help-general</code>:</dt>
<dd> Gives a brief usage message for the generic GDAL commandline options and exit.</dd></dl>
<dl>
<dt><code>-ro</code>:</dt>
<dd> (GDAL &gt;= 1.11) Open the dataset in read-only. Might be usefull for drivers refusing to use the dataset in update-mode. In which case, updated information will go into PAM .aux.xml files.</dd></dl>
<dl>
<dt><code>-a_srs</code> <i>srs_def</i>:</dt>
<dd></dd></dl>
<p> Defines the target coordinate system. This coordinate system will be written to the dataset. </p>
<dl>
<dt><code>-a_ullr</code> <i>ulx uly lrx lry</i>:</dt>
<dd> Assign/override the georeferenced bounds of the dataset.</dd></dl>
<dl>
<dt><code>-tr</code> xres yres :</dt>
<dd> Set target resolution. The values must be expressed in georeferenced units. Both must be positive values.</dd></dl>
<dl>
<dt><code>-unsetgt</code>:</dt>
<dd> Remove the georeference information.</dd></dl>
<dl>
<dt><code>-a_nodata</code> <i>value</i>:</dt>
<dd> Assign a specified nodata value to output bands.</dd></dl>
<dl>
<dt><code>-gcp</code> <i>pixel line easting northing [elevation]</i>:</dt>
<dd> Add the indicated ground control point to the dataset. This option may be provided multiple times to provide a set of GCPs.</dd></dl>
<dl>
<dt><code>-mo</code> <i>&#8216;META-TAG=VALUE&#8217;</i>:</dt>
<dd> Passes a metadata key and value to set on the output dataset if possible.</dd></dl>
<p> -a_ullr, -tr and -unsetgt options are exclusive.</p>
<h2>EXAMPLE</h2>
<pre>
gdal_edit -mo DATUM=WGS84 -mo PROJ=GEODETIC -a_ullr 7 47 8 46 test.ecw
</pre>
<h2>AUTHORS</h2>
<p> Even Rouault &lt;even dot=&#8221; rouault=&#8221; at=&#8221; mines=&#8221; dash=&#8221; paris=&#8221; dot=&#8221; org&gt;=&#8221;&gt; </p>
