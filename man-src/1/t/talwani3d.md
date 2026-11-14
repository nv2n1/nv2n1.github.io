---
title: "talwani3d(1)"
name: "talwani3d"
section: "1"
letter: "t"
url: "/docs/linux/man/1-talwani3d/"
description: "talwani3d – Compute free-air, geoid or vertical gravity gradients anomalies over 3-D bodies"
---

<h2>NAME</h2>
<p> talwani3d &#8211; Compute free-air, geoid or vertical gravity gradients anomalies over 3-D bodies</p>
<h2>SYNOPSIS</h2>
<p> <code>talwani3d</code> [ <i>modeltable</i> ] [ ] [ <i>rho</i> ] ] [ <code>f</code>|<code>n</code>|<code>v</code> ] [ <i>grdfile</i> ] [ <i>increment</i> ] [ [<code>h</code>][<code>v</code>] ] [ <i>trackfile</i> ] [ <i>region</i> ] [ <i>level</i>|<i>obsgrid</i> ] [ [<i>level</i>] ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-fg</code> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] [ <code>-x</code>[[-]<i>n</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>talwani3d</code> will read the multi-segment <i>modeltable</i> from file or standard input. This file contains contours of a 3-D body at different <i>z</i>-levels, with one contour per segment. The segment header must contain the parameters <i>zlevel rho</i>, which states the <i>z</i> contour level and the density of this slice (individual slice densities may be overridden by a fixed density contrast given via <code>-D</code>). We can compute anomalies on an equidistant grid (by specifying a new grid with <code>-R</code> and <code>-I</code> or provide an observation grid with elevations) or at arbitrary output points specified via <code>-N</code>. Chose from free-air anomalies, vertical gravity gradient anomalies, or geoid anomalies. Options are available to control axes units and direction.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>modeltable</i></p>
<dd> The file describing the horizontal contours of the bodies. Contours will be automatically closed if not already closed, and repeated vertices will be eliminated.</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code></p>
<dd> The <i>z</i>-axis should be positive upwards [Default is down].</p>
<dt><code>-D</code><i>unit</i></p>
<dd> Sets fixed density contrast that overrides any setting in model file, in kg/m^3.</p>
<dt><code>-F</code><code>f</code>|<code>n</code>|<code>v</code></p>
<dd> Specify desired gravitational field component. Choose between <code>f</code> (free-air anomaly) [Default], <code>n</code> (geoid) or <code>v</code> (vertical gravity gradient).</p>
<dt><code>-G</code><i>grdfile</i></p>
<dd> Specify the name of the output grid file; see GRID FILE FORMATS below). Required when an equidistant grid is implied for output. If <code>-N</code> is used then the output is written to stdout.</p>
<dt><code>-M</code>[<code>h</code>][<code>v</code>]</p>
<dd> Sets units used. Append <code>h</code> to indicate horizontal distances are in km [m], and append <code>z</code> to indicate vertical distances are in km [m].</p>
<dt><code>-N</code><i>trackfile</i></p>
<dd> Specifies locations where we wish to compute the predicted value. When this option is used there are no grids and the output data records are written to stdout.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-Z</code><i>level</i>|<i>obsgrid</i></p>
<dd> Set observation level either as a constant or give the name of a grid with observation levels. If the latter is used the the grid determines the output grid region [0].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-fg</code></p>
<dd> Geographic grids (dimensions of longitude, latitude) will be converted to km via a &quot;Flat Earth&quot; approximation using the current ellipsoid parameters.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s). Not used with binary data.</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</p>
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline].</p>
<dt><code>-x</code>[[-]<i>n</i>] <i>(more &#8230;)</i></p>
<dd> Limit number of cores used in multi-threaded algorithms (OpenMP required).</p>
<dt><code>-:</code>[<code>i</code>|<code>o</code>] <i>(more &#8230;)</i></p>
<dd> Swap 1st and 2nd column on input and/or output.</p>
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
<h2>UNITS</h2>
<p> For map distance unit, append <i>unit</i> <code>d</code> for arc degree, <code>m</code> for arc minute, and <code>s</code> for arc second, or <code>e</code> for meter [Default], <code>f</code> for foot, <code>k</code> for km, <code>M</code> for statute mile, <code>n</code> for nautical mile, and <code>u</code> for US survey foot. By default we compute such distances using a spherical approximation with great circles. Prepend <code>&#8211;</code> to a distance (or the unit is no distance is given) to perform &quot;Flat Earth&quot; calculations (quicker but less accurate) or prepend <code>+</code> to perform exact geodesic calculations (slower but more accurate).</p>
<h2>EXAMPLES</h2>
<p> To compute the free-air anomalies on a grid over a 3-D body that has been contoured and saved to body.txt, using 1.7 g/cm^3 as the density contrast, try </p>
<pre>
gmt talwani3d -R-200/200/-200/200 -I2 -G3dgrav.nc body.txt -D1700 -Fg
</pre>
<p> To obtain the vertical gravity gradient anomaly along the track in crossing.txt for the same model, try </p>
<pre>
gmt talwani3d -Ncrossing.txt body.txt -D1700 -Fv &gt; vgg_crossing.txt
</pre>
<p> Finally, the geoid anomaly along the same track in crossing.txt for the same model is returned by </p>
<pre>
gmt talwani3d -Ncrossing.txt body.txt -D1700 -Fn &gt; n_crossing.txt
</pre>
<h2>REFERENCES</h2>
<p> Talwani, M., and M. Ewing (1960), Rapid computation of gravitational attraction of three-dimensional bodies of arbitrary shape, Geophysics, 25(203-225).</p>
<h2>SEE ALSO</h2>
<p> <code>gmt.conf</code>, <code>gmt</code>, <code>grdmath</code>, <code>gravfft</code>, <code>gmtgravmag3d</code>, <code>grdgravmag3d</code>, <code>talwani2d</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
