---
title: "grdrotater(1)"
name: "grdrotater"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdrotater/"
description: "grdrotater – Finite rotation reconstruction of geographic grid"
---

<h2>NAME</h2>
<p> grdrotater &#8211; Finite rotation reconstruction of geographic grid</p>
<h2>SYNOPSIS</h2>
<p> <code>grdrotate</code> <i>ingrdfile</i> <i>rot_file</i>|<i>lon</i>/<i>lat</i>/<i>angle</i> <i>outgrdfile</i> [ <i>rotoutline</i> ] [ <i>polygonfile</i> ] [ ] [ <i>region</i> ] [ ] [ <i>ages</i> ] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-n</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdrotater</code> reads a geographical grid and reconstructs it given total reconstruction rotations. Optionally, the user may supply a clipping polygon in multiple-segment format; then, only the part of the grid inside the polygon is used to determine the reconstructed region. The outlines of the reconstructed region is also returned provided the rotated region is not the entire globe.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>ingrdfile</i></p>
<dd> Name of a grid file in geographical (lon, lat) coordinates.</p>
<dt><code>-E</code><i>rotfile</i></p>
<dd> Give file with rotation parameters. This file must contain one record for each rotation; each record must be of the following format: </p>
<p> <i>lon lat tstart [tstop] angle</i> [ <i>khat a b c d e f g df</i> ] </p>
<p> where <i>tstart</i> and <i>tstop</i> are in Myr and <i>lon lat angle</i> are in degrees. <i>tstart</i> and <i>tstop</i> are the ages of the old and young ends of a stage. If <i>tstop</i> is not present in the record then a total reconstruction rotation is expected and <i>tstop</i> is implicitly set to 0 and should not be specified for any of the records in the file. If a covariance matrix <code>C</code> for the rotation is available it must be specified in a format using the nine optional terms listed in brackets. Here, <code>C</code> = (<i>g</i>/<i>khat</i>)*[ <i>a b d; b c e; d e f</i> ] which shows <code>C</code> made up of three row vectors. If the degrees of freedom (<i>df</i>) in fitting the rotation is 0 or not given it is set to 10000. Blank lines and records whose first column contains # will be ignored. You may prepend a leading + to the filename to indicate you wish to invert the rotations. Alternative 1: Give the filename composed of two plate IDs separated by a hyphen (e.g., PAC-MBL) and we will instead extract that rotation from the GPlates rotation database. We return an error if the rotation cannot be found. Alternative 2: Specify <i>lon</i>/<i>lat</i>/<i>angle</i>, i.e., the longitude, latitude, and opening angle (all in degrees and separated by /) for a single total reconstruction rotation.</p>
<dt><code>-G</code><i>outgrdfile</i></p>
<dd> Name of output grid. This is the grid with the data reconstructed according to the specified rotation. If more than one reconstruction time is implied then <i>outgrdfile</i> must contain a C-format specifier to format a floating point number (reconstruction time) to text.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-D</code><i>rotoutline</i></p>
<dd> Name of the grid polygon outline file. This represents the outline of the grid reconstructed to the specified time. If more than one reconstruction time is implied then <i>rotoutline</i> must contain a C-format specifier to format a floating point number (reconstruction time) to text. If only one time is implied and <code>-D</code> is not set then we write the polygon to stdout (but see <code>-N</code>).</p>
<dt><code>-F</code><i>polygonfile</i></p>
<dd> Specify a multisegment closed polygon file that describes the inside area of the grid that should be projected [Default projects entire grid].</p>
<dt><code>-N</code></p>
<dd> Do Not output the rotated polygon outline [Default will write it to stdout, or to a file via <code>-D</code>].</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension.</p>
<dt><code>-S</code></p>
<dd> Skip the rotation of the grid, just rotate the polygon outline (requires <code>-F</code> if no grid is provided).</p>
<dt><code>-T</code><i>ages</i></p>
<dd> Sets the desired reconstruction times. For a single time append the desired time. For an equidistant range of reconstruction times give <code>-T</code><i>start</i>/<i>stop</i>/<i>inc</i> or <code>-T</code><i>start</i>/<i>stop</i>/<i>npoints</i><code>+</code>. For an non-equidistant set of reconstruction times please pass them via the first column in a file, e.g., <code>-T</code><i>agefile</i>. If no <code>-T</code> option is given and <code>-E</code> specified a rotation file then we equate the rotation file times with the reconstruction times.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is same as input].</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-:</code>[<code>i</code>|<code>o</code>] <i>(more &#8230;)</i></p>
<dd> Swap 1st and 2nd column on input and/or output.</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-n</code>[<code>b</code>|<code>c</code>|<code>l</code>|<code>n</code>][<code>+a</code>][<code>+b</code><i>BC</i>][<code>+c</code>][<code>+t</code><i>threshold</i>] <i>(more &#8230;)</i></p>
<dd> Select interpolation mode for grids.</p>
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
<h2>CONSEQUENCES OF GRID RESAMPLING</h2>
<p> Resample or sampling of grids will use various algorithms (see <code>-n</code>) that may lead to possible distortions or unexpected results in the resampled values. One expected effect of resampling with splines is the tendency for the new resampled values to slightly exceed the global min/max limits of the original grid. If this is unacceptable, you can impose clipping of the resampled values values so they do not exceed the input min/max values by adding <code>+c</code> to your <code>-n</code> option.</p>
<h2>GEODETIC VERSUS GEOCENTRIC COORDIINATES</h2>
<p> All spherical rotations are applied to geocentric coordinates. This means that incoming data points and grids are considered to represent geodetic coordinates and must first be converted to geocentric coordinates. Rotations are then applied, and the final reconstructed points are converted back to geodetic coordinates. This default behavior can be bypassed if the ellipsoid setting <i>PROJ_ELLIPSOID</i> is changed to Sphere.</p>
<h2>EXAMPLES</h2>
<p> To rotate the data defined by grid topo.nc and the polygon outline clip_path.d, using a total reconstruction rotation with pole at (135.5, -33.0) and a rotation angle of 37.3 degrees and bicubic interpolation, try </p>
<pre>
gmt grdrotater topo.nc -E135.5/-33/37.3 -V -Fclip_path.d -Grot_topo.nc &gt; rot_clip_path.d
</pre>
<p> To rotate the entire grid faa.nc back to 32 Ma using the rotation file <i>rotations.txt</i> and a bilinear interpolation, try </p>
<pre>
gmt grdrotater faa.nc -Erotations.txt -T32 -V -Grot_faa.nc -nl &gt; rot_faa_path.d
</pre>
<p> To just see how the outline of the grid large.nc will plot after the same rotation, try </p>
<pre>
gmt grdrotater large.nc -Erotations.txt -T32 -V -S \| psxy -Rg -JH180/6i -B30 -W0.5p \| gv -
</pre>
<p> To rotate the grid topo.nc back to 100 Ma using the rotation file <i>rotations.txt</i> and request a reconstruction every 10 Myr, saving both grids and outlines to filenames that derive from templates, try </p>
<pre>
gmt grdrotater topo.nc -Erotations.txt -T10/100/10 -V -Grot_topo_%g.nc -Drot_topo_path_%g.d
</pre>
<p> Let say you have rotated gridA.nc and gridB.nc, restricting each rotation to nodes inside polygons polyA.d and polyB.d, respectively, using rotation A = (123W,22S,16,4) and rotation B = (108W, 16S, -14.5), yielding rotated grids rot_gridA.nc and rot_gridB.nc. To determine the region of overlap between the rotated grids, we use grdmath: </p>
<pre>
gmt grdmath 1 rot_gridA.nc ISNAN SUB 1 rot_gridB.nc ISNAN SUB 2 EQ = overlap.nc
</pre>
<p> The grid overlap.nc now has 1s in the regions of overlap and 0 elsewhere. You can use it as a mask or use grdcontour <code>-D</code> to extract a polygon (i.e., a contour).</p>
<h2>NOTES</h2>
<p> GMT distributes the EarthByte rotation model Global_EarthByte_230-0Ma_GK07_AREPS.rot. To use an alternate rotation file, create an environmental parameters named <code>GPLATES_ROTATIONS</code> that points to an alternate rotation file.</p>
<h2>SEE ALSO</h2>
<p> <code>backtracker</code>, <code>grdspotter</code>, <code>hotspotter</code>, <code>originator</code>, <code>rotconverter</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
