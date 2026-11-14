---
title: "ogrtindex(1)"
name: "ogrtindex"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ogrtindex/"
description: "ogrtindex – ogrtindex creates a tileindex"
---

<h2 class="name">NAME</h2>
<p> ogrtindex &#8211; ogrtindex creates a tileindex </p>
<h2>SYNOPSIS</h2>
<pre><code>
ogrtindex[-lnum n]...[-lname name]...[-f output_format]
                                     [-write_absolute_path][-skip_different_projection] output_dataset src_dataset...
</code></pre>
<h2>DESCRIPTION</h2>
<p> The ogrtindex program can be used to create a tileindex &#8211; a file containing a list of the identities of a bunch of other files along with there spatial extents. This is primarily intended to be used with MapServer for tiled access to layers using the OGR connection type. </p>
<dl>
<dt><code>-lnum</code> <i>n</i>:</p>
<dd> Add layer number &#8216;n&#8217; from each source file in the tile index.</p>
<dt><code>-lname</code> <i>name</i>:</p>
<dd> Add the layer named &#8216;name&#8217; from each source file in the tile index.</p>
<dt><code>-f</code> <i>output_format</i>:</p>
<dd> Select an output format name. The default is to create a shapefile.</p>
<dt><code>-tileindex</code> <i>field_name</i>:</p>
<dd> The name to use for the dataset name. Defaults to LOCATION.</p>
<dt><code>-write_absolute_path</code>:</p>
<dd> Filenames are written with absolute paths</p>
<dt><code>-skip_different_projection</code>:</p>
<dd> Only layers with same projection ref as layers already inserted in the tileindex will be inserted.</dl>
<p> If no -lnum or -lname arguments are given it is assumed that all layers in source datasets should be added to the tile index as independent records. </p>
<p> If the tile index already exists it will be appended to, otherwise it will be created. </p>
<p> It is a flaw of the current ogrtindex program that no attempt is made to copy the coordinate system definition from the source datasets to the tile index (as is expected by MapServer when PROJECTION AUTO is in use).</p>
<h2>EXAMPLE</h2>
<p> This example would create a shapefile (tindex.shp) containing a tile index of the BL2000_LINK layers in all the NTF files in the wrk directory: </p>
<pre>
% ogrtindex tindex.shp wrk/*.NTF
</pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Silke Reimer silke [at] intevation.de </p>
<h2>Index</h2>
