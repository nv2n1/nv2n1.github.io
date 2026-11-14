---
title: "grdvector(1)"
name: "grdvector"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdvector/"
description: "grdvector – Plot vector field from two component grids"
---

<h2>NAME</h2>
<p> grdvector &#8211; Plot vector field from two component grids</p>
<h2>SYNOPSIS</h2>
<p> <code>grdvector</code> <i>compx.nc</i> <i>compy.nc</i> <code>-J</code><i>parameters</i> [ ] [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ <i>cpt</i> ] [ <i>fill</i> ] [ [<code>x</code>]<i>dx</i>[/<i>dy</i>] ] [ ] [ ] [ ] [ ] [ <i>parameters</i> ] [ <i>region</i> ] [ [<code>i</code>|<code>l</code>]<i>scale</i> ] [ ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ <i>pen</i> ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ ] [ <code>-c</code><i>copies</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdvector</code> reads two 2-D grid files which represents the <i>x</i>&#8211; and <i>y</i>-components of a vector field and produces a vector field plot by drawing vectors with orientation and length according to the information in the files. Alternatively, polar coordinate <i>r</i>, <i>theta</i> grids may be given instead.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>compx.nc</i></p>
<dd> Contains the x-components of the vector field.</p>
<dt><i>compy.nc</i></p>
<dd> Contains the y-components of the vector field. (See GRID FILE FORMATS below.)</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code></p>
<dd> The grid files contain polar (r, theta) components instead of Cartesian (x, y) [Default is Cartesian components].</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code>[<i>cpt</i>]</p>
<dd> Use <i>cpt</i> to assign colors based on vector length. Alternatively, supply the name of a GMT color master CPT [rainbow] and let <code>grdvector</code> automatically determine a 16-level continuous CPT from the grid&#8217;s z-range. Yet another option is to specify -Ccolor1,color2[,color3,&#8230;] to build a linear continuous cpt from those colors automatically. In this case <i>color</i><code>n</code> can be a r/g/b triplet, a color name, or an HTML hexadecimal color (e.g. #aabbcc ).</p>
<dt><code>-G</code><i>fill</i></p>
<dd> Sets color or shade for vector interiors [Default is no fill].</p>
<dt><code>-I</code>[<code>x</code>]<i>dx</i>[/<i>dy</i>]</p>
<dd> Only plot vectors at nodes every <i>x_inc</i>, <i>y_inc</i> apart (must be multiples of original grid spacing). Append <code>m</code> for arc minutes or <code>s</code> for arc seconds. Alternatively, use <code>-Ix</code> to specify the multiples <i>multx</i>[/<i>multy</i>] directly [Default plots every node].</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-N</code></p>
<dd> Do NOT clip vectors at map boundaries [Default will clip].</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code><i>parameters</i></p>
<dd> Modify vector parameters. For vector heads, append vector head <i>size</i> [Default is 0, i.e., stick-plot]. See VECTOR ATTRIBUTES for specifying additional attributes.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. Specify a subset of the grid.</p>
<dt><code>-S</code>[<code>i</code>|<code>l</code>]<i>scale</i></p>
<dd> Sets scale for Cartesian vector length in data units per distance measurement unit [1]. Append <code>c</code>, <code>i</code>, or <code>p</code> to indicate the measurement unit (cm, inch,or point). Prepend <code>l</code> to indicate a fixed length for all vectors. For Geographic data, give scale in data units per km. Use <code>-Si</code> if it is simpler to give the reciprocal scale in measurement unit per data unit or km per data unit.</p>
<dt><code>-T</code></p>
<dd> Means the azimuths of Cartesian data sets should be adjusted according to the signs of the scales in the x- and y-directions [Leave alone]. This option can be used to convert vector azimuths in cases when a negative scale is used in one of both directions (e.g., positive down).</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code><i>pen</i></p>
<dd> Set pen attributes used for vector outlines [Default: width = default, color = black, style = solid]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-Z</code></p>
<dd> The theta grid provided contains azimuths rather than directions (requires <code>-A</code>).</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>] <i>(more &#8230;)</i></p>
<dd> Select perspective view.</p>
<dt><code>-t</code>[<i>transp</i>] <i>(more &#8230;)</i></p>
<dd> Set PDF transparency level in percent.</p>
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
<h2>VECTOR ATTRIBUTES</h2>
<p> Several modifiers may be appended to the vector-producing options to specify the placement of vector heads, their shapes, and the justification of the vector. Below, left and right refers to the side of the vector line when viewed from the start point to the end point of the segment: <code>+a</code><i>angle</i> sets the angle of the vector head apex [30]. </p>
<p> <code>+b</code> places a vector head at the beginning of the vector path [none]. Optionally, append <code>t</code> for a terminal line, <code>c</code> for a circle, or <code>a</code> for arrow [Default]. Further append <code>l</code>|<code>r</code> to only draw the left or right side of this head [both sides]. </p>
<p> <code>+e</code> places a vector head at the end of the vector path [none]. Optionally, append <code>t</code> for a terminal line, <code>c</code> for a circle, or <code>a</code> for arrow [Default]. Further append <code>l</code>|<code>r</code> to only draw the left or right side of this head [both sides]. </p>
<p> <code>+g</code>-|<i>fill</i> turns off vector head fill (if -) or sets the vector head fill [Default fill is used, which may be no fill]. </p>
<p> <code>+l</code> draws half-arrows, using only the left side of specified heads [both sides]. </p>
<p> <code>+m</code> places a vector head at the mid-point the vector path [none]. Append <code>f</code> or <code>r</code> for forward or reverse direction of the vector [forward]. Optionally, append <code>t</code> for a terminal line, <code>c</code> for a circle, or <code>a</code> for arrow head [Default]. Further append <code>l</code>|<code>r</code> to only draw the left or right side of this head [both sides]. Cannot be combined with <code>+b</code> or <code>+e</code>. </p>
<p> <code>+n</code><i>norm</i> scales down vector attributes (pen thickness, head size) with decreasing length, where vectors shorter than <i>norm</i> will have their attributes scaled by length/<i>norm</i> [arrow attributes remains invariant to length]. </p>
<p> <code>+o</code><i>plon</i>/<i>plat</i> specifies the oblique pole for the great or small circles. Only needed for great circles if <code>+q</code> is given. </p>
<p> <code>+p</code>[-][<i>pen</i>] sets the vector pen attributes. If <i>pen</i> has a leading &#8211; then the head outline is not drawn. [Default pen is used, and head outline is drawn] </p>
<p> <code>+q</code> means the input <i>angle</i>, <i>length</i> data instead represent the <i>start</i> and <i>stop</i> opening angles of the arc segment relative to the given point. </p>
<p> <code>+r</code> draws half-arrows, using only the right side of specified heads [both sides]. </p>
<p> <code>t</code>[<code>b</code>|<code>e</code>]<i>trim</i> will shift the beginning or end point (or both) along the vector segment by the given <i>trim</i>; append suitable unit. If the modifiers <code>b</code>|<code>e</code> are not used then <i>trim</i> may be two values separated by a slash, which is used to specify different trims for the two ends. Positive trims will shorted the vector while negative trims will lengthen it [no trim]. </p>
<p> In addition, all but circular vectors may take these modifiers: <code>+j</code><i>just</i> determines how the input <i>x</i>,<i>y</i> point relates to the vector. Choose from <code>b</code>eginning [default], <code>e</code>nd, or <code>c</code>enter. </p>
<p> <code>+s</code> means the input <i>angle</i>, <i>length</i> is instead the <i>x</i>, <i>y</i> coordinates of the vector end point. </p>
<p> Finally, Cartesian vectors may take these modifiers: <code>+z</code><i>scale</i>[<i>unit</i>] expects input <i>dx</i>,<i>dy</i> vector components and uses the <i>scale</i> to convert to polar coordinates with length in given unit.</p>
<h2>EXAMPLES</h2>
<p> To draw the vector field given by the files r.nc and theta.nc on a linear plot with scale 5 cm per data unit, using vector rather than stick plot, scale vector magnitudes so that 10 units equal 1 inch, and center vectors on the node locations, run </p>
<pre>
gmt grdvector r.nc theta.nc -Jx5c -A -Q0.1i+e+jc -S10i &gt; gradient.ps
</pre>
<p> To plot a geographic data sets given the files com_x.nc and comp_y.nc, using a scale of 200 km per data unit and only plot every 3rd node in either direction, try </p>
<pre>
gmt grdvector comp_x.nc comp_y.nc -Ix3 -JH0/20c -Q0.1i+e+jc -S200 &gt; globe.ps
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtcolors</code>, <code>grdcontour</code>, <code>psxy</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
