---
title: "gshhs(1)"
name: "gshhs"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gshhs/"
description: "gshhs – Extract ASCII listings from binary GSHHS or WDBII data files"
---

<h2>NAME</h2>
<p> gshhs &#8211; Extract ASCII listings from binary GSHHS or WDBII data files</p>
<h2>SYNOPSIS</h2>
<p> <code>gshhs</code> <i>binaryfile.b</i> [ <code>-I</code><i>id</i> ] [ <code>-L</code> ] [ <code>-M</code> ] &gt; <i>asciifile.txt</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gshhs</code> reads the binary coastline (GSHHS) or political boundary or river (WDBII) files and extracts an ASCII listing. It automatically handles byte-swabbing between different architectures. Optionally, only segment header info can be displayed. The header info has the format <i>ID npoints hierarchical-level source area f_area west east south north container ancestor</i>, where hierarchical levels for coastline polygons go from 1 (shoreline) to 4 (lake inside island inside lake inside land). Source is either W (World Vector Shoreline) or C (CIA World Data Bank II); lower case is used if a lake is a river-lake. The <i>west east south north</i> is the enclosing rectangle, area is the polygon area in km^2 while f_area is the actual area of the ancestor polygon, container is the ID of the polygon that contains this polygon (-1 if none), and ancestor is the ID of the polygon in the full resolution set that was reduced to yield this polygon (-1 if full resolution). For line data the header is simply <i>ID npoints hierarchical-level source west east south north</i></p>
<dl>
<dt><i>binaryfile.b</i></p>
<dd> GSHHS or WDBII binary data file as distributed with the GSHHS data supplement. Any of the 5 standard resolutions (full, high, intermediate, low, crude) can be used.</p>
<dt><code>-I</code></p>
<dd> Only output information for the polygon that matches <i>id</i> [default outputs all polygons].</p>
<dt><code>-L</code></p>
<dd> Only output a listing of polygon or line segment headers [default outputs headers and data records].</p>
<dt><code>-M</code></p>
<dd> Start all header records with the GMT multiple segment indicator &#8216;&gt;&#8217; [Default uses P for polygons and L for lines].</dl>
<h2>EXAMPLES</h2>
<p> To convert the entire intermediate GSHHS binary data to ASCII, run </p>
<p> <code>gshhs</code> gshhs_i.b &gt; gshhs_i.txt </p>
<p> To only get a listing of the headers for the river data set at full resolution, try </p>
<p> <code>gshhs</code> wdb_rivers_f.b <code>-L</code> &gt; riverlisting.txt</p>
<h2>BUGS</h2>
<p> While the GSHHS data is organized as a set of closed polygons, the rivers and boundary data are just a set of line segments in no particular order. Thus, it is not possible to extract information pertaining to just one river or one country.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-gshhs_dp/">gshhs_dp</a></i>(1) <i><a href="/docs/linux/man/1-gshhstograss/">gshhstograss</a></i>(1) </p>
<h2>Index</h2>
