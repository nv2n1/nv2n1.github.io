---
title: "grdvolume(1)"
name: "grdvolume"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdvolume/"
description: "grdvolume – Calculate grid volume and area constrained by a contour"
---

<h2>NAME</h2>
<p> grdvolume &#8211; Calculate grid volume and area constrained by a contour</p>
<h2>SYNOPSIS</h2>
<p> <code>grdvolume</code> <i>grdfile</i> [ <i>cval</i> or <i>low/high/delta</i> or <code>r</code><i>low/high</i> ] [ <i>base</i> ] [ <i>region</i> ] [ [<i>unit</i>] ] [ [<code>c</code>|<code>h</code>] ] [ [<i>level</i>] ] [ <i>fact</i>[/<i>shift</i>] ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdvolume</code> reads a 2-D binary grid file and calculates the volume contained between the surface and the plane specified by the given contour (or zero if not given) and reports the area, volume, and maximum mean height (volume/area). Alternatively, specify a range of contours to be tried and <code>grdvolume</code> will determine the volume and area inside the contour for all contour values. Using <code>-T</code>, the contour that produced the maximum mean height (or maximum curvature of heights vs contour value) is reported as well. This feature may be used with <code>grdfilter</code> in designing an Optimal Robust Separator [<i>Wessel</i>, 1998].</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>grdfile</i></p>
<dd> The name of the input 2-D binary grid file. (See GRID FILE FORMAT below.)</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-C</code><i>cval</i> or <code>-C</code><i>low/high/delta</i> or <code>-Cr</code><i>low/high</i></p>
<dd> find area, volume and mean height (volume/area) inside the <i>cval</i> contour. Alternatively, search using all contours from <i>low</i> to <i>high</i> in steps of <i>delta</i>. [Default returns area, volume and mean height of the entire grid]. The area is measured in the plane of the contour. The <code>Cr</code> form on the other hand computes volume between the grid surface and the plans defined by <i>low</i> and <i>high</i>. Note that this is an <i>outside</i> volume whilst the other forms compute an <i>inside</i> (below the surface) area volume. Use this form to compute for example the volume of water between two contours.</p>
<dt><code>-L</code><i>base</i></p>
<dd> Also add in the volume from the level of the contour down to <i>base</i> [Default base is contour].</p>
<dt><code>-S</code>[<i>unit</i>]</p>
<dd> Convert degrees to Flat Earth distances, append a unit from <code>e</code>|<code>f</code>|<code>k</code>|<code>M</code>|<code>n</code>|<code>u</code> [Default is Cartesian].</p>
<dt><code>-T</code>[<code>c</code>|<code>h</code>]</p>
<dd> Determine the single contour that maximized the average height (= volume/area). Select <code>-Tc</code> to use the maximum curvature of heights versus contour value rather than the contour with the maximum height to pick the best contour value (requires <code>-C</code>).</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-Z</code><i>fact</i>[/<i>shift</i>]</p>
<dd> Optionally subtract <i>shift</i> before scaling data by <i>fact</i>. [Default is no scaling]. (Numbers in <code>-C</code>, <code>-L</code> refer to values after this scaling has occurred).</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</p>
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
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>EXAMPLES</h2>
<p> To determine the volume in km^3 under the surface hawaii_topo.nc (height in km), use </p>
<pre>
gmt grdvolume hawaii_topo.nc -Sk
</pre>
<p> To find the volume between the surface peaks.nc and the contour z = 250, use </p>
<pre>
gmt grdvolume peaks.nc -Sk -C250
</pre>
<p> To search for the contour, between 100 and 300 in steps of 10, that maximizes the ratio of volume to surface area for the file peaks.nc, use </p>
<pre>
gmt grdvolume peaks.nc -Sk -C100/300/10 -Th &gt; results.d
</pre>
<p> To see the areas and volumes for all the contours in the previous example, use </p>
<pre>
gmt grdvolume peaks.nc -Sk -C100/300/10 &gt; results.d
</pre>
<p> To find the volume of water in a lake with its free surface at 0 and max depth of 300 meters, use </p>
<pre>
gmt grdvolume lake.nc -Cr-300/0
</pre>
<h2>NOTES</h2>
<p> <code>grdvolume</code> distinguishes between gridline and pixel-registered grids. In both cases the area and volume are computed up to the grid boundaries. That means that in the first case the grid cells on the boundary only contribute half their area (and volume), whereas in the second case all grid cells are fully used. The exception is when the <code>-C</code> flag is used: since contours do not extend beyond the outermost grid point, both grid types are treated the same. That means the outer rim in pixel oriented grids is ignored when using the <code>-C</code> flag.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdfilter</code>, <code>grdmask</code>, <code>grdmath</code></p>
<h2>REFERENCES</h2>
<p> Wessel, P., 1998, An empirical method for optimal robust regional-residual separation of geophysical data, <i>Math. Geol.</i>, <code><a href="/docs/linux/man/4-30/">30</a></code>(4), 391-408.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
