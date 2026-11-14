---
title: "grdlandmask(1)"
name: "grdlandmask"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdlandmask/"
description: "grdlandmask – \"Create a \"\"wet-dry\"\" mask grid from shoreline data base\""
---

<h2>NAME</h2>
<p> grdlandmask &#8211; &quot;Create a &quot;&quot;wet-dry&quot;&quot; mask grid from shoreline data base&quot;</p>
<h2>SYNOPSIS</h2>
<p> <code>grdlandmask</code> <i>mask_grd_file</i> <i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]] <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[<code>r</code>] [ <i>min_area</i>[/<i>min_level</i>/<i>max_level</i>][<code>+ag</code>|<code>i</code>|<code>s</code> |<code>S</code>][<code>+r</code>|<code>l</code>][<code>p</code><i>percent</i>] ] [ <i>resolution</i>[<code>+</code>] ] [ <i>maskvalues</i>[<code>o</code>] ] [ [<i>level</i>] ] [ <code>-r</code> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdlandmask</code> reads the selected shoreline database and uses that information to decide which nodes in the specified grid are over land or over water. The nodes defined by the selected region and lattice spacing will be set according to one of two criteria: (1) land vs water, or (2) the more detailed (hierarchical) ocean vs land vs lake vs island vs pond. The resulting mask may be used in subsequent operations involving <code>grdmath</code> to mask out data from land [or water] areas.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-G</code><i>mask_grd_file</i>]</p>
<dd> Name of resulting output mask grid file. (See GRID FILE FORMATS below).</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>min_area</i>[/<i>min_level</i>/<i>max_level</i>][<code>+ag</code>|<code>i</code>|<code>s</code>|<code>S</code>][<code>+r</code>|<code>l</code>][<code>+p</code><i>percent</i>]</p>
<dd> Features with an area smaller than <i>min_area</i> in km^2 or of hierarchical level that is lower than <i>min_level</i> or higher than <i>max_level</i> will not be plotted [Default is 0/0/4 (all features)]. Level 2 (lakes) contains regular lakes and wide river bodies which we normally include as lakes; append <code>+r</code> to just get river-lakes or <code>+l</code> to just get regular lakes. By default (<code>+ai</code>) we select the ice shelf boundary as the coastline for Antarctica; append <code>+ag</code> to instead select the ice grounding line as coastline. For expert users who wish to print their own Antarctica coastline and islands via <i>psxy</i> you can use <code>+as</code> to skip all GSHHG features below 60S or <code>+aS</code> to instead skip all features north of 60S. Finally, append <code>+p</code><i>percent</i> to exclude polygons whose percentage area of the corresponding full-resolution feature is less than <i>percent</i>. See GSHHG INFORMATION below for more details.</p>
<dt><code>-D</code><i>resolution</i>[<code>+</code>]</p>
<dd> Selects the resolution of the data set to use ((<code>f</code>)ull, (<code>h</code>)igh, (<code>i</code>)ntermediate, (<code>l</code>)ow, or (<code>c</code>)rude). The resolution drops off by ~80% between data sets. [Default is <code>l</code>]. Append <code>+</code> to automatically select a lower resolution should the one requested not be available [abort if not found]. Alternatively, choose (<code>a</code>)uto to automatically select the best resolution given the chosen region. Note that because the coastlines differ in details a node in a mask file using one resolution is not guaranteed to remain inside [or outside] when a different resolution is selected.</p>
<dt><code>-N</code><i>maskvalues</i>[<code>o</code>]</p>
<dd> Sets the values that will be assigned to nodes. Values can be any number, including the textstring NaN. Append <code>o</code> to let nodes exactly on feature boundaries be considered outside [Default is inside]. Specify this information using 1 of 2 formats: </p>
<p> <code>-N</code><i>wet/dry</i>. </p>
<p> <code>-N</code><i>ocean/land/lake/island/pond</i>. </p>
<p> [Default is 0/1/0/1/0 (i.e., 0/1)].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline].</p>
<dt><code>-^</code> or just <code>&#8211;</code></p>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</p>
<dt><code>-+</code> or just <code>+</code></p>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</p>
<dt><code>-?</code> or no arguments</p>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print GMT version and exit.</p>
<dt><code>&#8211;</code><code>-show-datadir</code></p>
<dd> Print full path to GMT share directory and exit.</dl>
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When writing a netCDF file, the grid is stored by default with the variable name &quot;z&quot;. To specify another variable name <i>varname</i>, append <code>?</code><i>varname</i> to the file name. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes.</p>
<h2>EXAMPLES</h2>
<p> To set all nodes on land to NaN, and nodes over water to 1, using the high resolution data set, do </p>
<pre>
gmt grdlandmask -R-60/-40/-40/-30 -Dh -I5m -N1/NaN -Gland_mask.nc -V
</pre>
<p> To make a 1&#215;1 degree global grid with the hierarchical levels of the nodes based on the low resolution data: </p>
<pre>
gmt grdlandmask -R0/360/-90/90 -Dl -I1 -N0/1/2/3/4 -Glevels.nc -V
</pre>
<h2>GSHHS INFORMATION</h2>
<p> The coastline database is GSHHG (formerly GSHHS) which is compiled from three sources: World Vector Shorelines (WVS), CIA World Data Bank II (WDBII), and Atlas of the Cryosphere (AC, for Antarctica only). Apart from Antarctica, all level-1 polygons (ocean-land boundary) are derived from the more accurate WVS while all higher level polygons (level 2-4, representing land/lake, lake/island-in-lake, and island-in-lake/lake-in-island-in-lake boundaries) are taken from WDBII. The Antarctica coastlines come in two flavors: ice-front or grounding line, selectable via the <code>-A</code> option. Much processing has taken place to convert WVS, WDBII, and AC data into usable form for GMT: assembling closed polygons from line segments, checking for duplicates, and correcting for crossings between polygons. The area of each polygon has been determined so that the user may choose not to draw features smaller than a minimum area (see <code>-A</code>); one may also limit the highest hierarchical level of polygons to be included (4 is the maximum). The 4 lower-resolution databases were derived from the full resolution database using the Douglas-Peucker line-simplification algorithm. The classification of rivers and borders follow that of the WDBII. See the GMT Cookbook and Technical Reference Appendix K for further details.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdmath</code>, <code>grdclip</code>, <code>psmask</code>, <code>psclip</code>, <code>pscoast</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
