---
title: "grdgravmag3d(1)"
name: "grdgravmag3d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdgravmag3d/"
description: "grdgravmag3d – Compute the gravity effect of a grid by the method of Okabe"
---

<h2>NAME</h2>
<p> grdgravmag3d &#8211; Compute the gravity effect of a grid by the method of Okabe</p>
<h2>SYNOPSIS</h2>
<p> <code>grdgravmag3d</code> <i>grdfile_top</i> [<i>grdfile_bot</i>] [ <i>density</i> ] [ <i>thick</i> ] [ <i>xy_file</i> ] [ <i>outgrid</i> ] [ <i>&lt;&#8230;&gt;</i> ] [ <i>increment</i> ] [ <i>z_obs</i> ] [ [<code>n</code><i>n_pad</i>]|[<i>pad_dist</i>]|[&lt;w/e/s/n&gt;] ] [ <i>region</i> ] [ <i>radius</i> ] [ [<i>level</i>] ] [ <i>level</i>[<code>b</code>|<code>t</code>] ] [ <code>-fg</code> ] [ <code>-x</code><i>+a|n|-n</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdgravmag3d</code> will compute the gravity anomaly of a body described by one or (optionally) two grids The output can either be along a given set of xy locations or on a grid. This method is not particularly fast but allows computing the anomaly of arbitrarily complex shapes.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>grdfile_top</i> [<i>grdfile_bot</i>]</p>
<dd> Grid file whose gravity efect is going to be computed. If two grids are provided then the gravity/magnetic effect of the volume between them is computed.</p>
<dt><code>-C</code><i>density</i></p>
<dd> Sets body density in SI. This option is mutually exclusive with <code>-H</code></p>
<dt><code>-F</code><i>xy_file</i></p>
<dd> Provide locations where the anomaly will be computed. Note this option is mutually exclusive with <code>-G</code>.</p>
<dt><code>-G</code><i>outgrid</i></p>
<dd> Output the gravity anomaly at nodes of this grid file.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-E</code><i>thickness</i></p>
<dd> To provide the layer thickness in m [Default = 500 m].</p>
<dt><code>-H</code><i>f_dec/f_dip/m_int/m_dec/m_dip</i> <code>-H</code><i>+m&lt;magfile&gt;</i> <code>-H</code><i>x|y|z|h|t</i> <code>-H</code><i>+i|+g|+r|+f|+n</i></p>
<dd> Sets parameters for computation of magnetic anomaly (Can be used multiple times). f_dec/f_dip -&gt; geomagnetic declination/inclination </p>
<p> m_int/m_dec/m_dip -&gt; body magnetic intensity/declination/inclination </p>
<p> OR for a grid mode +m&lt;magfile&gt; where &#8216;magfile&#8217; is the name of the magnetic intensity file. </p>
<p> To compute a component, specify any of: x|X|e|E to compute the E-W component. </p>
<p> y|Y|n|N to compute the N-S component. </p>
<p> z|Z to compute the Vertical component. </p>
<p> h|H to compute the Horizontal component. </p>
<p> t|T|f|F to compute the total field. </p>
<p> For a variable inclination and declination use IGRF. Set any of <code>-H</code><i>+i|+g|+r|+f|+n</i> to do that</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-L</code><i>z_obs</i></p>
<dd> Sets level of observation [Default = 0]. That is the height (z) at which anomalies are computed.</p>
<dt><code>-Q</code>[<code>n</code><i>n_pad</i>]|[<i>pad_dist</i>]|[&lt;w/e/s/n&gt;]</p>
<dd>
<dt><code>Extend the domain of computation with respect to output -R</code> region.</p>
<dd> <code>-Qn</code><i>n_pad</i> artificially extends the width of the outer rim of cells to have a fake width of <i>n_pad</i> * dx[/dy]. </p>
<p> <code>-Q</code><i>pad_dist</i> extend the region by west-pad, east+pad, etc. </p>
<p> <code>-Q</code><i>region</i> Same syntax as <code>-R</code>.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. Note: this overrides the source grid region (Default: use same region as input)</p>
<dt><code>-S</code><i>radius</i></p>
<dd> Set search radius in km (valid only in the two grids mode OR when <code>-E</code>) [Default = 30 km]. This option serves to speed up the computation by not computing the effect of prisms that are further away than <i>radius</i> from the current node.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-Z</code><i>level</i>[<code>b</code>|<code>t</code>]</p>
<dd> level of reference plane [Default = 0]. Use this option when the triangles describe a non-closed surface and the volume is defined from each triangle and this reference level. An example will be the water depth to compute a Bouguer anomaly. Use <code>-Zb</code> or <code>Zt</code> to close the body at its bottom (for example, to compute the effect of a dome) or at its top (to compute the effect of a <i>spoon</i>).</p>
<dt><code>-fg</code></p>
<dd> Geographic grids (dimensions of longitude, latitude) will be converted to meters via a &quot;Flat Earth&quot; approximation using the current ellipsoid parameters.</p>
<dt><code>-x</code><i>+a|n|-n</i></p>
<dd> Choose the number of processors used in multi-threading (Only available with multi-threading builds). <i>+a</i> Use all available processors. </p>
<p> <i>n</i> Use n processors (not more than max available off course). </p>
<p> <i>-n</i> Use (all &#8211; n) processors.</p>
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
<h2>GRID DISTANCE UNITS</h2>
<p> If the grid does not have meter as the horizontal unit, append <code>+u</code><i>unit</i> to the input file name to convert from the specified unit to meter. If your grid is geographic, convert distances to meters by supplying <code>-fg</code> instead.</p>
<h2>EXAMPLES</h2>
<p> Suppose you want to compute the gravity effect of the phantom &quot;Sandy Island&quot; together with its not phantom seamount </p>
<pre>
gmt grdgravmag3d sandy_bat.grd -C1700 -Z-4300 -fg -I1m -Gsandy_okb.grd -V
</pre>
<p> To compute the vertical component due to a magnetization stored in <i>mag.grd</i> over a zone defined by the surface <i>bat.grd</i>, using variable declination and inclination provided the the IGRF and using 4 processors, do: </p>
<pre>
gmt grdgravmag3d bat.grd -E10000 -Gcomp_Z.grd -Hz -H+n -H+mmag.grd -x4 -V -S50
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtgravmag3d</code>, <code>talwani2d</code>, <code>talwani3d</code></p>
<h2>REFERENCE</h2>
<p> Okabe, M., Analytical expressions for gravity anomalies due to polyhedral bodies and translation into magnetic anomalies, <i>Geophysics</i>, 44, (1979), p 730-741.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
