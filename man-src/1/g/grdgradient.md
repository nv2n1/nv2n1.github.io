---
title: "grdgradient(1)"
name: "grdgradient"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdgradient/"
description: "grdgradient – Compute directional derivative or gradient from a grid"
---

<h2>NAME</h2>
<p> grdgradient &#8211; Compute directional derivative or gradient from a grid</p>
<h2>SYNOPSIS</h2>
<p> <code>grdgradient</code> <i>in_grdfile</i> <i>out_grdfile</i> [ <i>azim</i>[/<i>azim2</i>] ] [ [<code>a</code>][<code>c</code>][<code>o</code>][<code>n</code>] ] [ [<code>s|p</code>]<i>azim/elev</i>[/<i>ambient</i>/<i>diffuse</i>/<i>specular</i>/<i>shine</i>] ] [ <i>flag</i> ] [ [<code>e</code>][<code>t</code>][<i>amp</i>][/<i>sigma</i>[/<i>offset</i>]] ] [ <i>region</i> ] [ <i>slopefile</i> ] [ [<i>level</i>] ] [ <code>-fg</code> ] [ <code>-n</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdgradient</code> may be used to compute the directional derivative in a given direction (<code>-A</code>), or the direction (<code>-S</code>) [and the magnitude (<code>-D</code>)] of the vector gradient of the data. </p>
<p> Estimated values in the first/last row/column of output depend on boundary conditions (see <code>-L</code>).</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>in_grdfile</i></p>
<dd> 2-D grid file from which to compute directional derivative. (See GRID FILE FORMATS below).</p>
<dt><code>-G</code><i>out_grdfile</i></p>
<dd> Name of the output grid file for the directional derivative. (See GRID FILE FORMATS below).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>azim</i>[/<i>azim2</i>]</p>
<dd> Azimuthal direction for a directional derivative; <i>azim</i> is the angle in the x,y plane measured in degrees positive clockwise from north (the +y direction) toward east (the +x direction). The negative of the directional derivative, -[dz/dx*sin(<i>azim</i>) + dz/dy*cos(<i>azim</i>)], is found; negation yields positive values when the slope of z(x,y) is downhill in the <i>azim</i> direction, the correct sense for shading the illumination of an image (see <code>grdimage</code> and <code>grdview</code>) by a light source above the x,y plane shining from the <i>azim</i> direction. Optionally, supply two azimuths, <code>-A</code><i>azim</i>/<i>azim2</i>, in which case the gradients in each of these directions are calculated and the one larger in magnitude is retained; this is useful for illuminating data with two directions of lineated structures, e.g., <code>-A</code><i>0</i>/<i>270</i> illuminates from the north (top) and west (left).</p>
<dt><code>-D</code>[<code>a</code>][<code>c</code>][<code>o</code>][<code>n</code>]</p>
<dd> Find the direction of the positive (up-slope) gradient of the data. To instead find the aspect (the down-slope direction), use <code>-Da</code>. By default, directions are measured clockwise from north, as <i>azim</i> in <code>-A</code> above. Append <code>c</code> to use conventional Cartesian angles measured counterclockwise from the positive x (east) direction. Append <code>o</code> to report orientations (0-180) rather than directions (0-360). Append <code>n</code> to add 90 degrees to all angles (e.g., to give local strikes of the surface ).</p>
<dt><code>-E</code>[<code>s|p</code>]<i>azim/elev</i>[/<i>ambient</i>/<i>diffuse</i>/<i>specular</i>/<i>shine</i>]</p>
<dd> Compute Lambertian radiance appropriate to use with <code>grdimage</code> and <code>grdview</code>. The Lambertian Reflection assumes an ideal surface that reflects all the light that strikes it and the surface appears equally bright from all viewing directions. <i>azim</i> and <i>elev</i> are the azimuth and elevation of light vector. Optionally, supply <i>ambient</i> <i>diffuse</i> <i>specular</i> <i>shine</i> which are parameters that control the reflectance properties of the surface. Default values are: <i>0.55</i>/<i>0.6</i>/<i>0.4</i>/<i>10</i> To leave some of the values untouched, specify = as the new value. For example <code>-E</code><i>60</i>/<i>30</i>/<i>=</i>/<i>0.5</i> sets the <i>azim</i> <i>elev</i> and <i>diffuse</i> to 60, 30 and 0.5 and leaves the other reflectance parameters untouched. Append <code>s</code> to use a simpler Lambertian algorithm. Note that with this form you only have to provide the azimuth and elevation parameters. Append <code>p</code> to use the Peucker piecewise linear approximation (simpler but faster algorithm; in this case the <i>azim</i> and <i>elev</i> are hardwired to 315 and 45 degrees. This means that even if you provide other values they will be ignored.)</p>
<dt><code>-L</code><i>flag</i></p>
<dd> Boundary condition <i>flag</i> may be <i>x</i> or <i>y</i> or <i>xy</i> indicating data is periodic in range of x or y or both, or <i>flag</i> may be <i>g</i> indicating geographical conditions (x and y are lon and lat). [Default uses &quot;natural&quot; conditions (second partial derivative normal to edge is zero).]</p>
<dt><code>-N</code>[<code>e</code>][<code>t</code>][<i>amp</i>][/<i>sigma</i>[/<i>offset</i>]]</p>
<dd> Normalization. [Default: no normalization.] The actual gradients <i>g</i> are offset and scaled to produce normalized gradients <i>gn</i> with a maximum output magnitude of <i>amp</i>. If <i>amp</i> is not given, default <i>amp</i> = 1. If <i>offset</i> is not given, it is set to the average of <i>g</i>. <code>-N</code> yields <i>gn</i> = <i>amp</i> * (<i>g</i> &#8211; <i>offset</i>)/max(abs(<i>g</i> &#8211; <i>offset</i>)). <code>-Ne</code> normalizes using a cumulative Laplace distribution yielding <i>gn</i> = <i>amp</i> * (1.0 &#8211; exp(<a href="/docs/linux/man/2-sqrt/">sqrt</a>(2) * (<i>g</i> &#8211; <i>offset</i>)/ <i>sigma</i>)) where <i>sigma</i> is estimated using the L1 norm of (<i>g</i> &#8211; <i>offset</i>) if it is not given. <code>-Nt</code> normalizes using a cumulative Cauchy distribution yielding <i>gn</i> = (2 * <i>amp</i> / PI) * atan( (<i>g</i> &#8211; <i>offset</i>)/ <i>sigma</i>) where <i>sigma</i> is estimated using the L2 norm of (<i>g</i> &#8211; <i>offset</i>) if it is not given.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. Using the <code>-R</code> option will select a subsection of <i>in_grdfile</i> grid. If this subsection exceeds the boundaries of the grid, only the common region will be extracted.</p>
<dt><code>-S</code><i>slopefile</i></p>
<dd> Name of output grid file with scalar magnitudes of gradient vectors. Requires <code>-D</code> but makes <code>-G</code> optional.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-fg</code></p>
<dd> Geographic grids (dimensions of longitude, latitude) will be converted to meters via a &quot;Flat Earth&quot; approximation using the current ellipsoid parameters.</p>
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
<h2>GRID DISTANCE UNITS</h2>
<p> If the grid does not have meter as the horizontal unit, append <code>+u</code><i>unit</i> to the input file name to convert from the specified unit to meter. If your grid is geographic, convert distances to meters by supplying <code>-fg</code> instead.</p>
<h2>HINTS</h2>
<p> If you don&#8217;t know what <code>-N</code> options to use to make an intensity file for <code>grdimage</code> or <code>grdview</code>, a good first try is <code>-Ne</code>0.6. </p>
<p> Usually 255 shades are more than enough for visualization purposes. You can save 75% disk space by appending =nb/a to the output filename <i>out_grdfile</i>. </p>
<p> If you want to make several illuminated maps of subregions of a large data set, and you need the illumination effects to be consistent across all the maps, use the <code>-N</code> option and supply the same value of <i>sigma</i> and <i>offset</i> to <code>grdgradient</code> for each map. A good guess is <i>offset</i> = 0 and <i>sigma</i> found by <code>grdinfo</code> <code>-L2</code> or <code>-L1</code> applied to an unnormalized gradient grd. </p>
<p> If you simply need the <i>x</i>&#8211; or <i>y</i>-derivatives of the grid, use <code>grdmath</code>.</p>
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>EXAMPLES</h2>
<p> To make a file for illuminating the data in geoid.nc using exp- normalized gradients in the range [-0.6,0.6] imitating light sources in the north and west directions: </p>
<pre>
gmt grdgradient geoid.nc -A0/270 -Ggradients.nc=nb/a -Ne0.6 -V
</pre>
<p> To find the azimuth orientations of seafloor fabric in the file topo.nc: </p>
<pre>
gmt grdgradient topo.nc -Dno -Gazimuths.nc -V
</pre>
<h2>REFERENCES</h2>
<p> Horn, B.K.P., Hill-Shading and the Reflectance Map, Proceedings of the IEEE, Vol. 69, No. 1, January 1981, pp. 14-47. (<i><a rel="nofollow" href="http://people.csail.mit.edu/bkph/papers/Hill-Shading.pdf">http://people.csail.mit.edu/bkph/papers/Hill-Shading.pdf</a></i>)</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code> <code>grdhisteq</code>, <code>grdmath</code>, <code>grdimage</code>, <code>grdview</code>, <code>grdvector</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
