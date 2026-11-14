---
title: "grdspotter(1)"
name: "grdspotter"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdspotter/"
description: "grdspotter – Create CVA image from a gravity or topography grid"
---

<h2>NAME</h2>
<p> grdspotter &#8211; Create CVA image from a gravity or topography grid</p>
<h2>SYNOPSIS</h2>
<p> <code>grdspotter</code> [<i>grdfile</i>] <i>rotfile</i> <i>CVAgrid</i> <i>increment</i> <i>region</i> [ <i>agegrid</i> ] [ <i>DIgrid</i> ] [ <i>IDgrid</i> ] [ ] [ <i>upper_age</i> ] [ <i>PAgrid</i> ] [ <i>IDinfo</i> ] [ ] [ <code>t</code>|<code>u</code><i>fixed_val</i> ] [ [ [<i>level</i>] ] [ <i>n_try</i> ]] [ <code>-Z</code><i>z_min</i>[/<i>z_max</i>[/<i>z_inc</i>]] ] [ <code>-r</code> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdspotter</code> reads a grid file with residual bathymetry or gravity and calculates flowlines from each node that exceeds a minimum value using the specified rotations file. These flowlines are then convolved with the volume of the prism represented by each grid node and added up to give a Cumulative Volcano Amplitude grid (CVA).</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>grdfile</i></p>
<dd> Data grid to be processed, typically residual bathymetry or free-air anomalies.</p>
<dt><code>-E</code><i>rotfile</i></p>
<dd> Give file with rotation parameters. This file must contain one record for each rotation; each record must be of the following format: </p>
<p> <i>lon lat tstart [tstop] angle</i> [ <i>khat a b c d e f g df</i> ] </p>
<p> where <i>tstart</i> and <i>tstop</i> are in Myr and <i>lon lat angle</i> are in degrees. <i>tstart</i> and <i>tstop</i> are the ages of the old and young ends of a stage. If <i>tstop</i> is not present in the record then a total reconstruction rotation is expected and <i>tstop</i> is implicitly set to 0 and should not be specified for any of the records in the file. If a covariance matrix <code>C</code> for the rotation is available it must be specified in a format using the nine optional terms listed in brackets. Here, <code>C</code> = (<i>g</i>/<i>khat</i>)*[ <i>a b d; b c e; d e f</i> ] which shows <code>C</code> made up of three row vectors. If the degrees of freedom (<i>df</i>) in fitting the rotation is 0 or not given it is set to 10000. Blank lines and records whose first column contains # will be ignored. You may prepend a leading + to the filename to indicate you wish to invert the rotations. Alternatively, give the filename composed of two plate IDs separated by a hyphen (e.g., PAC-MBL) and we will instead extract that rotation from the GPlates rotation database. We return an error if the rotation cannot be found.</p>
<dt><code>-G</code></p>
<dd> Specify name for output CVA grid file.</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>agegrid</i></p>
<dd> Supply a crustal age grid that is co-registered with the input data grid. These ages become the upper ages to use when constructing flowlines [Default extend flowlines back to oldest age found in the rotation file; but see ].</p>
<dt><code>-D</code><i>DIgrid</i></p>
<dd> Use flowlines to determine the maximum CVA encountered along each flowline and create a Data Importance (DI) grid with these values at the originating nodes.</p>
<dt><code>-L</code><i>IDgrid</i></p>
<dd> Supply a co-registered grid with seamount chain IDs for each node. This option requires that you also use .</p>
<dt><code>-M</code></p>
<dd> Do not attempt to keep all flowlines in memory when using <code>-D</code> and/or <code>-P</code>. Should you run out of memory you can use this option to compute flowlines on-the-fly. It will be slower as we no longer can reuse the flowlines calculated for the CVA step. Cannot be used with <code>-W</code> or the multi-slice mode in <code>-Z</code>.</p>
<dt><code>-N</code><i>upper_age</i></p>
<dd> Set the upper age to assign to nodes whose crustal age is unknown (i.e., NaN) [no upper age]. Also see .</p>
<dt><code>-P</code><i>PAgrid</i></p>
<dd> Use flowlines to determine the flowline age at the CVA maximum for each node and create a Predicted Age (PA) grid with these values at the originating nodes.</p>
<dt><code>-Q</code><i>IDinfo</i></p>
<dd> Either give (1) a single ID to use or (2) the name of a file with a list of IDs to use [Default uses all IDs]. Each line would be TAG ID [w e s n]. The <i>w/e/s/n</i> zoom box is optional; if specified it means we only trace the flowline if inside this region [Default uses region set by <code>-R</code>]. Requires <code>-L</code>.</p>
<dt><code>-S</code></p>
<dd> Normalize the resulting CVA grid to percentages of the CVA maximum. This also normalizes the DI grid (if requested).</p>
<dt><code>-T</code><code>t</code>|<code>u</code><i>fixed_val</i></p>
<dd> Selects ways to adjust ages; repeatable. Choose from <code>-Tt</code> to truncate crustal ages given via the option that exceed the upper age set with [no truncation], or <code>u</code><i>fixed_val</i> which means that after a node passes the test implied by , we use this <i>fixed_val</i> instead in the calculations. [Default uses individual node values].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code><i>n_try</i></p>
<dd> Get <i>n_try</i> bootstrap estimates of the maximum CVA location; the longitude and latitude results are written to stdout [Default is no bootstrapping]. Cannot be used with <code>-M</code>.</p>
<dt><code>-Z</code><i>z_min</i>[/<i>z_max</i>[/<i>z_inc</i>]]</p>
<dd> Ignore nodes with z-values lower than <i>z_min</i> [0] and optionally larger than <i>z_max</i> [Inf]. Give <i>z_min/z_max/z_inc</i> to make separate CVA grids for each <i>z</i>-slice [Default makes one CVA grid]. Multi-slicing cannot be used with <code>-M</code>.</p>
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
<h2>GEODETIC VERSUS GEOCENTRIC COORDIINATES</h2>
<p> All spherical rotations are applied to geocentric coordinates. This means that incoming data points and grids are considered to represent geodetic coordinates and must first be converted to geocentric coordinates. Rotations are then applied, and the final reconstructed points are converted back to geodetic coordinates. This default behavior can be bypassed if the ellipsoid setting <i>PROJ_ELLIPSOID</i> is changed to Sphere.</p>
<h2>EXAMPLES</h2>
<p> To create a CVA image from the Pacific topography grid Pac_res_topo.nc, using the DC85.d Euler poles, and only output a grid for the specified domain, run </p>
<pre>
gmt grdspotter Pac_res_topo.nc -EDC85.d -GCVA.nc -R190/220/15/25 -I2m -N145 -Tt -V
</pre>
<p> This file can then be plotted with <code>grdimage</code>.</p>
<h2>NOTES</h2>
<p> GMT distributes the EarthByte rotation model Global_EarthByte_230-0Ma_GK07_AREPS.rot. To use an alternate rotation file, create an environmental parameters named <code>GPLATES_ROTATIONS</code> that points to an alternate rotation file.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdimage</code>, <code>project</code>, <code>mapproject</code>, <code>backtracker</code>, <code>hotspotter</code>, <code>originator</code></p>
<h2>REFERENCES</h2>
<p> Wessel, P., 1999, &quot;Hotspotting&quot; tools released, EOS Trans. AGU, 80 (29), p. 319. </p>
<p> Wessel, P., 2008, Hotspotting: Principles and properties of a plate tectonic Hough transform, Geochem. Geophys. Geosyst. 9(Q08004): doi:10.1029/2008GC002058.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
