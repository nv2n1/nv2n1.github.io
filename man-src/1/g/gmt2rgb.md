---
title: "gmt2rgb(1)"
name: "gmt2rgb"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmt2rgb/"
description: "gmt2rgb – Converting a grid file, a raw, or a Sun raster file to r/g/b grids"
---

<h2>NAME</h2>
<p> gmt2rgb &#8211; Converting a grid file, a raw, or a Sun raster file to r/g/b grids</p>
<h2>SYNOPSIS</h2>
<p> <code>gmt2rgb</code> <i>infile</i> <code>-G</code><i>template</i> [ <code>-C</code><i>cptfile</i> ] [ <code>-F</code> ] [ <code>-I</code><i>xinc</i>[<code>m</code>|<code>c</code>][/<i>yinc</i>[<code>m</code>|<code>c</code>]] ] [ <code>-L</code><i>layer</i> ] [ <code>-R</code><i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] ] [ <code>-V</code> ] [ <code>-W</code><i>width</i>/<i>height</i>[/<i>n_bytes</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>gmt2rgb</code> reads one of three types of input files: (1) A Sun 8-, 24-, or 32-bit raster file; we the write out the red, green, and blue components (0-255 range) to separate grid files. Since the raster file header is limited you may use the <code>-R</code>, <code>-F</code>, <code>-I</code> options to set a complete header record [Default is simply based on the number of rows and columns]. (2) A binary 2-D grid file; we then convert the z-values to red, green, blue via the provided cpt file. Optionally, only write out one of the r, g, b, layers. (3) A RGB or RGBA raw raster file. Since raw rasterfiles have no header, you have to give the image dimensions via the <code>-W</code> option.</p>
<dl>
<dt><i>infile</i></p>
<dd> The (1) Sun raster file, (2) 2-D binary grid file, or (3) raw raster file to be converted.</p>
<dt><code>-G</code></p>
<dd> Provide an output name template for the three output grids. The template should be a regular grid file name except it must contain the string %c which on output will be replaced by r, g, or b.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code></p>
<dd> name of the color palette table (for 2-D binary input grid only).</p>
<dt><code>-F</code></p>
<dd> Force pixel node registration [Default is gridline registration]. (Node registrations are defined in <code>GMT</code> Cookbook Appendix B on grid file formats.)</p>
<dt><code>-I</code></p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>c</code> to indicate arc seconds. If one of the units <code>e</code>, <code>k</code>, <code>i</code>, or <code>n</code> is appended instead, the increment is assumed to be given in meter, km, miles, or nautical miles, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <code>ELLIPSOID</code>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see Appendix B for details. Note: if <code>-R</code><i>grdfile</i> is used then grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-L</code></p>
<dd> Output only the specified layer (r, g, or b). [Default outputs all 3 layers].</p>
<dt><code>-R</code></p>
<dd> <i>xmin</i>, <i>xmax</i>, <i>ymin</i>, and <i>ymax</i> specify the Region of interest. For geographic regions, these limits correspond to <i>west, east, south,</i> and <i>north</i> and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. For calendar time coordinates you may either give (a) relative time (relative to the selected <code>TIME_EPOCH</code> and in the selected <code>TIME_UNIT</code>; append <code>t</code> to <code>-JX</code>|<code>x</code>), or (b) absolute time of the form [<i>date</i>]<code>T</code>[<i>clock</i>] (append <code>T</code> to <code>-JX</code>|<code>x</code>). At least one of <i>date</i> and <i>clock</i> must be present; the <code>T</code> is always required. The <i>date</i> string must be of the form [-]yyyy[-mm[-dd]] (Gregorian calendar) or yyyy[-Www[-d]] (ISO week calendar), while the <i>clock</i> string must be of the form hh:mm:ss[.xxx]. The use of delimiters and their type and positions must be exactly as indicated (however, input, output and plot formats are customizable; see <code>gmtdefaults</code>).</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</p>
<dt><code>-W</code></p>
<dd> Sets the size of the raw raster file. By default an RGB file (which has 3 bytes/pixel) is assumed. For RGBA files use <i>n_bytes</i> = 4. Use <code>-W</code> for guessing the image size of a RGB raw file, and <code>-W</code><i>=/=/4</i> if the raw image is of the RGBA type. Notice that this might be a bit slow because the guessing algorithm makes uses of FFTs.</dl>
<h2>EXAMPLES</h2>
<p> To use the color palette topo.cpt to create r, g, b component grids from hawaii_grv.grd file, use </p>
<p> <code>gmt2rgb</code> hawaii_grv.grd <code>-C</code>topo.cpt <code>-G</code>hawaii_grv_%c.grd </p>
<p> To output the red component from the Sun raster radiation.ras file, use </p>
<p> <code>gmt2rgb</code> radiation.ras <code>-L</code>r <code>-G</code>comp_%c.grd</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmtdefaults/">gmtdefaults</a></i>(1), <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-grdedit/">grdedit</a></i>(1), <i><a href="/docs/linux/man/1-grdimage/">grdimage</a></i>(1), <i><a href="/docs/linux/man/1-grdmath/">grdmath</a></i>(1), <i><a href="/docs/linux/man/1-grdview/">grdview</a></i>(1) </p>
<h2>Index</h2>
