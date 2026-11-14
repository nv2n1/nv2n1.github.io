---
title: "gshhg(1)"
name: "gshhg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gshhg/"
description: "gshhg – Extract data tables from binary GSHHG or WDBII data files"
---

<h2>NAME</h2>
<p> gshhg &#8211; Extract data tables from binary GSHHG or WDBII data files</p>
<h2>SYNOPSIS</h2>
<p> <code>gshhg</code> <i>binaryfile.b</i> [ <i>min</i> ] [ ] [ <i>id</i> ] [ ] [ <i>level</i> ] [ <code>e</code>|<code>i</code> ] [ <code>-bo</code><i>&lt;binary&gt;</i> ] [ <code>-do</code><i>&lt;nodata&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] &gt; <i>asciifile.txt</i> </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gshhg</code> reads the binary coastline (GSHHG) or political boundary or river (WDBII) files and extracts an ASCII listing. It automatically handles byte-swabbing between different architectures. Optionally, only segment header info can be displayed. The header info has the format <i>ID npoints hierarchical-level source area f_area west east south north container ancestor</i>, where hierarchical levels for coastline polygons go from 1 (shoreline) to 4 (lake inside island inside lake inside land). Source is either W (World Vector Shoreline) or C (CIA World Data Bank II); lower case is used if a lake is a river-lake. The <i>west east south north</i> is the enclosing rectangle, <i>area</i> is the polygon area in km^2 while <i>f_area</i> is the actual area of the ancestor polygon, <i>container</i> is the ID of the polygon that contains this polygon (-1 if none), and <i>ancestor</i> is the ID of the polygon in the full resolution set that was reduced to yield this polygon (-1 if full resolution since there is no ancestor). For line data the header is simply <i>ID npoints hierarchical-level source west east south north</i>. For more information about the file formats, see TECHNICAL INFORMATION below.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>binaryfile.b</i></p>
<dd> GSHHG or WDBII binary data file as distributed with the GSHHG data supplement. Any of the 5 standard resolutions (full, high, intermediate, low, crude) can be used.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>min</i></p>
<dd> Only output information for the polygon if its area equals or exceeds <i>min</i> [Default outputs all polygons].</p>
<dt><code>-G</code></p>
<dd> Write output that can be imported into GNU Octave or Matlab by ending segments with a NaN-record.</p>
<dt><code>-I</code><i>id</i></p>
<dd> Only output information for the polygon that matches <i>id</i>. Use <code>-Ic</code> to get all the continents only [Default outputs all polygons].</p>
<dt><code>-L</code></p>
<dd> Only output a listing of polygon or line segment headers [Default outputs headers and data records].</p>
<dt><code>-N</code></p>
<dd> Only output features whose level matches the given <i>level</i> [Default will output all levels].</p>
<dt><code>-Qe</code>|<code>i</code></p>
<dd> Control what to do with river-lakes (river sections large enough to be stored as closed polygons). Use <code>-Qe</code> to exclude them and <code>-Qi</code> to exclude everything else instead [Default outputs all polygons].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output.</p>
<dt><code>-do</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace output columns that equal NaN with <i>nodata</i>.</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</dl>
<h2>EXAMPLES</h2>
<p> To convert the entire intermediate GSHHG binary data to ASCII files for Octave/Matlab, run </p>
<pre>
gmt gshhg gshhs_i.b --IO_SEGMENT_MARKER=N &gt; gshhs_i.txt
</pre>
<p> To only get a listing of the headers for the river data set at full resolution, try </p>
<pre>
gmt gshhg wdb_rivers_f.b -L &gt; riverlisting.txt
</pre>
<p> To only extract lakes, excluding river-lakes, from the high resolution file, try </p>
<pre>
gmt gshhg gshhs_h.b -Ee -N2 &gt; all_lakes.txt
</pre>
<h2>TECHNICAL INFORMATION</h2>
<p> Users who wish to access the GSHHG or WDBII data directly from their custom programs should consult the gshhg.c and gshhg.h source code and familiarize themselves with the data format and how various information flags are packed into a single 4-byte integer. While we do not maintain any Octave/Matlab code to read these files we are aware that both MathWorks and IDL have made such tools available to their users. However, they tend not to update their code and our file structure has evolved considerably over time, breaking their code. Here, some general technical comments on the binary data files are given. <code>GSHHG</code>: These files contain completely closed polygons of continents and islands (level 1), lakes (level 2), islands-in-lakes (level 3) and ponds-in-islands-in-lakes (level 4); a particular level can be extracted using the <code>-N</code> option. Continents are identified as the first 6 polygons and can be extracted via the <code>-Ic</code> option. The IDs for the continents are Eurasia (0), Africa (1), North America (2), South America (3), Antarctica (4), and Australia (5). Files are sorted on area from large to small. There are two sub-groups for level 2: Regular lakes and the so-called &quot;river-lakes&quot;, the latter being sections of a river that are so wide to warrant a polygon representation. These river-lakes are flagged in the header (also see <code>-Q</code>). All five resolutions are free of self-intersections. Areas of all features have been computed using a Lambert azimuthal equal-area projection centered on the polygon centroids, using WGS-84 as the ellipsoid. GMT use the GSHHG as a starting point but then partition the polygons into pieces using a resolution-dependent binning system; parts of the world are then rebuilt into closed polygons on the fly as needed. For more information on GSHHG processing, see Wessel and Smith (1996). <code>WDBII</code>. These files contain sets of line segments not necessarily in any particular order. Thus, it is not possible to extract information pertaining to just one river or one country. Furthermore, the 4 lower resolutions derive directly from the full resolution by application of the Douglas-Peucker algorithm (see gshhg_dp), hence self-intersections are increasingly likely as the resolution is degraded. Note that the river-lakes included in GSHHG are also duplicated in the WDBII river files so that each data set can be a stand-alone representation. Users who wish to access both data sets can recognize the river-lakes features by examining the header structure (see the source code for details); they are also the only closed polygons in the WDBII river file. There are many levels (classes) in the river file: River-lakes (0), Permanent major rivers (1), Additional major rivers (2), Additional rivers (3), Minor rivers (4), Intermittent rivers &#8212; major (6), Intermittent rivers &#8212; additional (7), Intermittent rivers &#8212; minor (8), Major canals (10), Canals of lesser importance (11), and Canals &#8212; irrigation type (12). For the border file there are three levels: National boundaries (1), Internal domestic boundaries (2), and international maritime boundaries (3). Individual levels or classes may be extracted via <code>-N</code>.</p>
<h2>REFERENCES</h2>
<p> Douglas, D. H., and T. K. Peucker, 1973, Algorithms for the reduction of the number of points required to represent a digitized line of its caricature, <i>Can. Cartogr., 10</i>, 112-122. </p>
<p> Gorny, A. J., 1977, <i>World Data Bank II General User GuideRep. PB 271869</i>, 10pp, Central Intelligence Agency, Washington, DC. </p>
<p> Soluri, E. A., and V. A. Woodson, 1990, World Vector Shoreline, <i>Int. Hydrograph. Rev., <a href="/docs/linux/man/1-lxvii/">LXVII</a>(1), 27-35.</i> </p>
<p> Wessel, P., and W. H. F. Smith, 1996, A global, self-consistent, hierarchical, high-resolution shoreline database, <i>J. Geophys. Res., 101(B4)</i>, 8741-8743.*</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
