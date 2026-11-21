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
<dt>&bull;</dt>
<dd> create linear reference file from input data</dd>
<dt>&bull;</dt>
<dd> return the &#8216;linear referenced&#8217; distance for the projection of the input coordinates (point) on the path</dd>
<dt>&bull;</dt>
<dd> return the coordinates (point) on the path according to the &#8216;linear referenced&#8217; distance</dd>
<dt>&bull;</dt>
<dd> return the portion of the path according to the &#8216;linear referenced&#8217; begin and end distances</dd></dl>
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
<dt><code>&#8211;help-general</code>:</dt>
<dd> Show the usage.</dd>
<dt><code>-progress</code>:</dt>
<dd> Show progress.</dd>
<dt><code>-quiet</code>:</dt>
<dd> Supress all messages except errors and results.</dd>
<dt><code>-f</code> <i>format_name</i>:</dt>
<dd> Select an output format name. The default is to create a shapefile.</dd>
<dt><code>-dsco</code> <i>NAME=VALUE</i>:</dt>
<dd> Dataset creation option (format specific)</dd>
<dt><code>-lco</code><i> NAME=VALUE</i>:</dt>
<dd> Layer creation option (format specific)</dd>
<dt><code>-create</code>:</dt>
<dd> Create the linear reference file (linestring of parts).</dd>
<dt><code>-l</code><i>src_line_datasource_name</i>:</dt>
<dd> The path to input linestring datasource (e.g. the road)</dd>
<dt><code>-ln</code><i>layer_name</i>:</dt>
<dd> The layer name in datasource</dd>
<dt><code>-lf</code><i>field_name</i>:</dt>
<dd> The field name of uniq values to separate the input lines (e.g. the set of roads)</dd>
<dt><code>-p</code><i>src_repers_datasource_name</i>:</dt>
<dd> The path to linear references points (e.g. the road mile-stones)</dd>
<dt><code>-pn</code><i>layer_name</i>:</dt>
<dd> The layer name in datasource</dd>
<dt><code>-pm</code><i>pos_field_name</i>:</dt>
<dd> The field name of distances along path (e.g. mile-stones values)</dd>
<dt><code>-pf</code><i>field_name</i>:</dt>
<dd> The field name of uniq values to map input reference points to lines</dd>
<dt><code>-r</code><i>src_parts_datasource_name</i>:</dt>
<dd> The path to linear reference file</dd>
<dt><code>-rn</code><i>layer_name</i>:</dt>
<dd> The layer name in datasource</dd>
<dt><code>-o</code><i>dst_datasource_name</i>:</dt>
<dd> The path to output linear reference file (linestring datasource)</dd>
<dt><code>-on</code><i>layer_name</i>:</dt>
<dd> The layer name in datasource</dd>
<dt><code>-of</code><i>field_name</i>:</dt>
<dd> The field name for storing the uniq values of input lines</dd>
<dt><code>-s</code><i>step</i>:</dt>
<dd> The part size in linear units</dd>
<dt><code>-get_pos</code>:</dt>
<dd> Return linear referenced postion for input X, Y</dd>
<dt><code>-x</code><i>long</i>:</dt>
<dd> Input X coordinate</dd>
<dt><code>-y</code><i>lat</i>:</dt>
<dd> Input Y coordinate</dd>
<dt><code>-get_coord</code>:</dt>
<dd> Return point on path for input linear distance</dd>
<dt><code>-m</code><i>position</i>:</dt>
<dd> The input linear distance</dd>
<dt><code>-get_subline</code>:</dt>
<dd> Return the portion of the input path from and to input linear positions</dd>
<dt><code>-mb</code><i>position</i>:</dt>
<dd> The input begin linear distance</dd>
<dt><code>-me</code><i>position</i>:</dt>
<dd> The input end linear distance</dd></dl>
<h2>EXAMPLE</h2>
<p> This example would create a shapefile (parts.shp) containing a data needed for linear referencing (1 km parts): </p>
<pre>
% ogrlineref -create -l roads.shp -p references.shp -pm dist -o parts.shp -s 1000 -progress
</pre>
<h2>AUTHORS</h2>
<p> Dmitry Baryshnikov polimax [at] mail.ru </p>
