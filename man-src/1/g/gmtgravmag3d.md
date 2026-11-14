---
title: "gmtgravmag3d(1)"
name: "gmtgravmag3d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtgravmag3d/"
description: "gmtgravmag3d – Compute the gravity/magnetic effect of a body by the method of Okabe"
---

<h2>NAME</h2>
<p> gmtgravmag3d &#8211; Compute the gravity/magnetic effect of a body by the method of Okabe</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtgravmag3d</code> [[<i>d</i>]<i>xyz_file</i>/<i>vert_file</i>[<i>/m</i>]]|[<i>r|s</i>]<i>raw_file</i> [ <i>density</i> ] [ ] [ <i>thickness</i> ] [ <i>xy_file</i> ] [ <i>outputgrid</i> ] [ <i>f_dec</i>/<i>f_dip</i>/<i>m_int</i>/<i>m_dec</i>/<i>m_dip</i> ] [ <i>z_observation</i> ] [ <i>radius</i> ] [ <i>level</i> ] [ [<i>level</i>] ] [ <code>-fg</code>] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtgravmag3d</code> will compute the gravity or magnetic anomaly of a body described by a set of triangles. The output can either be along a given set of xy locations or on a grid. This method is not particularly fast but allows computing the anomaly of arbitrarily complex shapes.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-C</code><i>density</i></p>
<dd> Sets body density in SI. This option is mutually exclusive with <code>-H</code>.</p>
<dt><code>-H</code><i>f_dec</i>/<i>f_dip</i>/<i>m_int</i>/<i>m_dec</i>/<i>m_dip</i></p>
<dd> Sets parameters for computing a magnetic anomaly. Use <i>f_dec</i>/<i>f_dip</i> to set the geomagnetic declination/inclination in degrees. <i>m_int</i>/<i>m_dec</i>/<i>m_dip</i> are the body magnetic intensity declination and inclination.</p>
<dt><code>-F</code><i>xy_file</i></p>
<dd> Provide locations where the anomaly will be computed. Note this option is mutually exlusive with <code>-G</code>.</p>
<dt><code>-G</code><i>outgrid</i></p>
<dd> Output the gravity or magnetic anomaly at nodes of this grid file.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</p>
<dt><code>-T</code>[[<i>d</i>]<i>xyz_file</i>/<i>vert_file</i>[<i>/m</i>]]|[<i>r|s</i>]<i>raw_file</i>]</p>
<dd> Give either names of xyz[m] and <i>vertex</i> files or of a <i>raw</i> or <i>stl</i> file defining a close surface. In the first case append a <i>d</i> immediately after <code>-T</code> and optionally a <i>/m</i> after the vertex file name. In the second case append a <i>r</i> or a <i>s</i> immediately after <code>-T</code> and before the file name. A <i>vertex</i> file is a file with N rows (one per triangle) and 3 columns with integers defining the order by which the points in the <i>xyz</i> file are to be connected to form a triangle. The output of the program triangulate comes in this format. The optional <i>/m</i> instructs the program that the xyzm file has four columns and that the fourth column contains the magnetization intensity (plus signal), which needs not to be constant. In this case the third argument of the <code>-H</code> option is ignored. A <i>raw</i> format (selected by the <code>r</code> flag is a file with N rows (one per triangle) and 9 columns corresponding to the x,y,x coordinates of each of the three vertex of each triangle. Alternatively, the <code>s</code> flag indicates that the surface file is in the ASCII STL (Stereo Lithographic) format. These two type of files are used to provide a closed surface.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-E</code>[<i>thickness</i>]</p>
<dd> give layer thickness in m [Default = 0 m]. Use this option only when the triangles describe a non-closed surface and you want the anomaly of a constant thickness layer.</p>
<dt><code>-L</code>[<i>z_observation</i>]</p>
<dd> sets level of observation [Default = 0]. That is the height (z) at which anomalies are computed.</p>
<dt><code>-S</code><i>radius</i></p>
<dd> search radius in km. Triangle centroids that are further away than <i>radius</i> from current output point will not be taken into account. Use this option to speed up computation at expenses of a less accurate result.</p>
<dt><code>-Z</code>[<i>level</i>]</p>
<dd> level of reference plane [Default = 0]. Use this option when the triangles describe a non-closed surface and the volume is defined from each triangle and this reference level. An example will be the hater depth to compute a Bouguer anomaly.</p>
<dt><code>-fg</code></p>
<dd> Geographic grids (dimensions of longitude, latitude) will be converted to meters via a &quot;Flat Earth&quot; approximation using the current ellipsoid parameters.</p>
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
<p> Suppose you &#8230; </p>
<pre>
gmt gmtgravmag3d ...
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdgravmag3d</code>, <code>talwani2d</code>, <code>talwani3d</code></p>
<h2>REFERENCE</h2>
<p> Okabe, M., Analytical expressions for gravity anomalies due to polyhedral bodies and translation into magnetic anomalies, <i>Geophysics</i>, 44, (1979), p 730-741.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
