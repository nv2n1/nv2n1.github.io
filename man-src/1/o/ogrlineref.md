---
title: "ogrlineref(1)"
name: "ogrlineref"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ogrlineref/"
description: "ogrlineref – ogrlineref The utility can be used for:"
---

<h2 class="name">NAME</h2>
<p> ogrlineref &#8211; ogrlineref The utility can be used for:</p>
<dl>
<dt>&bull;</p>
<dd> create linear reference file from input data</p>
<dt>&bull;</p>
<dd> return the &#8216;linear referenced&#8217; distance for the projection of the input coordinates (point) on the path</p>
<dt>&bull;</p>
<dd> return the coordinates (point) on the path according to the &#8216;linear referenced&#8217; distance</p>
<dt>&bull;</p>
<dd> return the portion of the path according to the &#8216;linear referenced&#8217; begin and end distances</dl>
<h2>SYNOPSIS</h2>
<pre><code>
ogrlineref[--help - general][-progress][-quiet]
          [-f format_name][[-dsco NAME = VALUE]...][[-lco NAME = VALUE]...]
          [-create]
          [-l src_line_datasource_name][-ln layer_name][-lf field_name]
          [-p src_repers_datasource_name][-pn layer_name][-pm pos_field_name][-pf field_name]
          [-r src_parts_datasource_name][-rn layer_name]
          [-o dst_datasource_name][-on layer_name][-of field_name][-s step]
          [-get_pos][-x long][-y lat]
          [-get_coord][-m position]
          [-get_subline][-mb position][-me position]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The ogrlineref program can be used to create a linear reference &#8211; a file containing a segments of special length (e.g. 1 km in reference units) and get coordinates, linear referenced distances or sublines (subpaths) from this file. The utility not required the M or Z values in geometry. The results can be stored in any OGR supported format. Also some information writed to the stdout. </p>
<dl>
<dt><code>&#8211;help-general</code>:</p>
<dd> Show the usage.</p>
<dt><code>-progress</code>:</p>
<dd> Show progress.</p>
<dt><code>-quiet</code>:</p>
<dd> Supress all messages except errors and results.</p>
<dt><code>-f</code> <i>format_name</i>:</p>
<dd> Select an output format name. The default is to create a shapefile.</p>
<dt><code>-dsco</code> <i>NAME=VALUE</i>:</p>
<dd> Dataset creation option (format specific)</p>
<dt><code>-lco</code><i> NAME=VALUE</i>:</p>
<dd> Layer creation option (format specific)</p>
<dt><code>-create</code>:</p>
<dd> Create the linear reference file (linestring of parts).</p>
<dt><code>-l</code><i>src_line_datasource_name</i>:</p>
<dd> The path to input linestring datasource (e.g. the road)</p>
<dt><code>-ln</code><i>layer_name</i>:</p>
<dd> The layer name in datasource</p>
<dt><code>-lf</code><i>field_name</i>:</p>
<dd> The field name of uniq values to separate the input lines (e.g. the set of roads)</p>
<dt><code>-p</code><i>src_repers_datasource_name</i>:</p>
<dd> The path to linear references points (e.g. the road mile-stones)</p>
<dt><code>-pn</code><i>layer_name</i>:</p>
<dd> The layer name in datasource</p>
<dt><code>-pm</code><i>pos_field_name</i>:</p>
<dd> The field name of distances along path (e.g. mile-stones values)</p>
<dt><code>-pf</code><i>field_name</i>:</p>
<dd> The field name of uniq values to map input reference points to lines</p>
<dt><code>-r</code><i>src_parts_datasource_name</i>:</p>
<dd> The path to linear reference file</p>
<dt><code>-rn</code><i>layer_name</i>:</p>
<dd> The layer name in datasource</p>
<dt><code>-o</code><i>dst_datasource_name</i>:</p>
<dd> The path to output linear reference file (linestring datasource)</p>
<dt><code>-on</code><i>layer_name</i>:</p>
<dd> The layer name in datasource</p>
<dt><code>-of</code><i>field_name</i>:</p>
<dd> The field name for storing the uniq values of input lines</p>
<dt><code>-s</code><i>step</i>:</p>
<dd> The part size in linear units</p>
<dt><code>-get_pos</code>:</p>
<dd> Return linear referenced postion for input X, Y</p>
<dt><code>-x</code><i>long</i>:</p>
<dd> Input X coordinate</p>
<dt><code>-y</code><i>lat</i>:</p>
<dd> Input Y coordinate</p>
<dt><code>-get_coord</code>:</p>
<dd> Return point on path for input linear distance</p>
<dt><code>-m</code><i>position</i>:</p>
<dd> The input linear distance</p>
<dt><code>-get_subline</code>:</p>
<dd> Return the portion of the input path from and to input linear positions</p>
<dt><code>-mb</code><i>position</i>:</p>
<dd> The input begin linear distance</p>
<dt><code>-me</code><i>position</i>:</p>
<dd> The input end linear distance</dl>
<h2>EXAMPLE</h2>
<p> This example would create a shapefile (parts.shp) containing a data needed for linear referencing (1 km parts): </p>
<pre>
% ogrlineref -create -l roads.shp -p references.shp -pm dist -o parts.shp -s 1000 -progress
</pre>
<h2>AUTHORS</h2>
<p> Dmitry Baryshnikov polimax [at] mail.ru </p>
<h2>Index</h2>
