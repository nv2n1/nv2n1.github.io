---
title: "grd2rgb(1)"
name: "grd2rgb"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grd2rgb/"
description: "grd2rgb – Write r/g/b grid files from a grid file, a raw RGB file, or SUN rasterfile"
---

<h2>NAME</h2>
<p> grd2rgb &#8211; Write r/g/b grid files from a grid file, a raw RGB file, or SUN rasterfile</p>
<h2>SYNOPSIS</h2>
<p> <code>grd2rgb</code> <i>infile</i> <i>template</i> [ <i>cpt</i> ] [ <i>xinc</i>[<code>m</code>|<code>s</code>][/<i>yinc</i>[<code>m</code>|<code>s</code>]] ] [ <i>layer</i> ] <i>region</i> [<i>level</i>] [ <i>width</i>/<i>height</i>[/<i>n_bytes</i>] ] [ <code>-r</code> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grd2rgb</code> reads one of three types of input files: (1) A Sun 8-, 24-, or 32-bit raster file; we the write out the red, green, and blue components (0-255 range) to separate grid files. Since the raster file header is limited you may use the <code>-R</code>, <code>-I</code>, <code>-r</code> options to set a complete header record [Default is simply based on the number of rows and columns]. (2) A binary 2-D grid file; we then convert the z-values to red, green, blue via the provided CPT file. Optionally, only write out one of the r, g, b, layers. (3) A RGB or RGBA raw raster file. Since raw rasterfiles have no header, you have to give the image dimensions via the <code>-W</code> option.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>infile</i></p>
<dd> The (1) Sun raster file, (2) 2-D binary grid file, or (3) raw raster file to be converted.</p>
<dt><code>-G</code><i>template</i></p>
<dd> Provide an output name template for the three output grids. The template should be a regular grid file name except it must contain the string %c which on output will be replaced by r, g, or b.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-C</code><i>cpt</i></p>
<dd> name of the color palette table (for 2-D binary input grid only).</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-L</code><i>layer</i></p>
<dd> Output only the specified layer (r, g, or b). [Default outputs all 3 layers].</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code><i>width</i>/<i>height</i>[/<i>n_bytes</i>]</p>
<dd> Sets the size of the raw raster file. By default an RGB file (which has 3 bytes/pixel) is assumed. For RGBA files use <i>n_bytes</i> = 4. Use <code>-W</code> for guessing the image size of a RGB raw file, and <code>-W</code><i>=/=/4</i> if the raw image is of the RGBA type. Notice that this might be a bit slow because the guessing algorithm makes uses of FFTs.</p>
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
<h2>EXAMPLES</h2>
<p> To use the color palette topo.cpt to create r, g, b component grids from hawaii_grv.nc file, use </p>
<pre>
gmt grd2rgb hawaii_grv.nc -Ctopo.cpt -Ghawaii_grv_%c.nc
</pre>
<p> To output the red component from the Sun raster radiation.ras file, use </p>
<pre>
gmt grd2rgb radiation.ras -Lr -Gcomp_%c.nc
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>grdedit</code>, <code>grdimage</code>, <code>grdmath</code> , <code>grdview</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
