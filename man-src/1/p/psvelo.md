---
title: "psvelo(1)"
name: "psvelo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psvelo/"
description: "psvelo – Plot velocity vectors, crosses, and wedges on maps"
---

<h2>NAME</h2>
<p> psvelo &#8211; Plot velocity vectors, crosses, and wedges on maps</p>
<h2>SYNOPSIS</h2>
<p> <code>psvelo</code> [ <i>table</i> ] <i>parameters</i> <i>region</i> [ <i>parameters</i> ] [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ <i>color</i> ] [ <i>color</i> ] [ <i>color</i> ] [ ] [ ] [ ] [ ] [ ] [ <i>symbol</i>/<i>scale</i>/<i>conf</i>/<i>font_size</i> ] [ [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>pen</i> ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>psvelo</code> reads data values from <i>files</i> [or standard input] and generates PostScript code that will plot velocity arrows on a map. Most options are the same as for <code>psxy</code>, except <code>-S</code>. The PostScript code is written to standard output. The previous version (<code>psvelomeca</code>) is now obsolete. It has been replaced by <code>psvelo</code> and <code>psmeca</code>.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. </p>
<p> <code>-S</code> </p>
<p> Selects the meaning of the columns in the data file and the figure to be plotted. <code>-Se</code><i>velscale/confidence/fontsize</i>. Velocity ellipses in (N,E) convention. <i>Vscale</i> sets the scaling of the velocity arrows. This scaling gives inches (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended). <i>Confidence</i> sets the 2-dimensional confidence limit for the ellipse, e.g., 0.95 for 95% confidence ellipse. <i>Fontsize</i> sets the size of the text in points. The ellipse will be filled with the color or shade specified by the option [default transparent]. The arrow and the circumference of the ellipse will be drawn with the pen attributes specified by the option. Parameters are expected to be in the following columns: <code>1</code>,<code>2</code>: longitude, latitude of station (<code>-:</code> option interchanges order) <code>3</code>,<code>4</code>: eastward, northward velocity (<code>-:</code> option interchanges order) <code>5</code>,<code>6</code>: uncertainty of eastward, northward velocities (1-sigma) (<code>-:</code> option interchanges order) <code>7</code>: correlation between eastward and northward components <code>8</code>: name of station (optional). </p>
<p> <code>-Sn</code><i>barscale.</i> Anisotropy bars. <i>Barscale</i> sets the scaling of the bars This scaling gives inches (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended). Parameters are expected to be in the following columns: <code>1</code>,<code>2</code>: longitude, latitude of station (<code>-:</code> option interchanges order) <code>3</code>,<code>4</code>: eastward, northward components of anisotropy vector (<code>-:</code> option interchanges order) </p>
<p> <code>-Sr</code><i>velscale/confidence/fontsize</i> Velocity ellipses in rotated convention. <i>Vscale</i> sets the scaling of the velocity arrows. This scaling gives inches (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended). <i>Confidence</i> sets the 2-dimensional confidence limit for the ellipse, e.g., 0.95 for 95% confidence ellipse. <i>Fontsize</i> sets the size of the text in points. The ellipse will be filled with the color or shade specified by the option [default transparent]. The arrow and the circumference of the ellipse will be drawn with the pen attributes specified by the option. Parameters are expected to be in the following columns: <code>1</code>,<code>2</code>: longitude, latitude, of station (<code>-:</code> option interchanges order) <code>3</code>,<code>4</code>: eastward, northward velocity (<code>-:</code> option interchanges order) <code>5</code>,<code>6</code>: semi-major, semi-minor axes <code>7</code>: counter-clockwise angle, in degrees, from horizontal axis to major axis of ellipse. <code>8</code>: name of station (optional) </p>
<p> <code>-Sw</code><i>wedge_scale/wedge_mag</i>. Rotational wedges. <i>Wedge_scale</i> sets the size of the wedges in inches (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended). Values are multiplied by <i>Wedge_mag</i> before plotting. For example, setting <i>Wedge_mag</i> to 1.e7 works well for rotations of the order of 100 nanoradians/yr. Use <code>-G</code> to set the fill color or shade for the wedge, and <code>-E</code> to set the color or shade for the uncertainty. Parameters are expected to be in the following columns: <code>1</code>,<code>2</code>: longitude, latitude, of station (<code>-:</code> option interchanges order) <code>3</code>: rotation in radians <code>4</code>: rotation uncertainty in radians </p>
<p> <code>-Sx</code><i>cross_scale</i> gives Strain crosses. <i>Cross_scale</i> sets the size of the cross in inches (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended). Parameters are expected to be in the following columns: <code>1</code>,<code>2</code>: longitude, latitude, of station (<code>-:</code> option interchanges order) <code>3</code>: eps1, the most extensional eigenvalue of strain tensor, with extension taken positive. <code>4</code>: eps2, the most compressional eigenvalue of strain tensor, with extension taken positive. <code>5</code>: azimuth of eps2 in degrees CW from North.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>parameters</i></p>
<dd> Modify vector parameters. For vector heads, append vector head <i>size</i> [Default is 9p]. See <i>Vector Attributes</i> for specifying additional attributes.</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-D</code><i>Sigma_scale</i></p>
<dd> can be used to rescale the uncertainties of velocities (<code>-Se</code> and <code>-Sr</code>) and rotations (<code>-Sw</code>). Can be combined with the <i>confidence</i> variable.</p>
<dt><code>-F</code><i>fill</i></p>
<dd> Sets the color or shade used for frame and annotation. [Default is black]</p>
<dt><code>-E</code><i>fill</i></p>
<dd> Sets the color or shade used for filling uncertainty wedges (<code>-Sw</code>) or velocity error ellipses (<code>-Se</code> or <code>-Sr</code>). [If <code>-E</code> is not specified, the uncertainty regions will be transparent.]</p>
<dt><code>-G</code><i>fill</i></p>
<dd> Specify color (for symbols/polygons) or pattern (for polygons) [Default is black]. Optionally, specify <code>-Gp</code><i>icon_size/pattern</i>, where <i>pattern</i> gives the number of the image pattern (1-90) OR the name of a icon-format file. <i>icon_size</i> sets the unit size in inches. To invert black and white pixels, use <code>-GP</code> instead of <code>-Gp</code>. See the CookBook for information on individual patterns.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code></p>
<dd> Draw lines. Ellipses and fault planes will have their outlines drawn using current pen (see <code>-W</code>).</p>
<dt><code>-N</code></p>
<dd> Do <code>NOT</code> skip symbols that fall outside the frame boundary specified by <code>-R</code>. [Default plots symbols inside frame only].</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code></p>
<dd> Set pen attributes for velocity arrows, ellipse circumference and fault plane edges. [Defaults: width = default, color = black, style = solid]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
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
<p> The following should make big red arrows with green ellipses, outlined in red. Note that the 39% confidence scaling will give an ellipse which fits inside a rectangle of dimension Esig by Nsig. </p>
<pre>
gmt psvelo &lt;&lt; END -h2 -R-10/10/-10/10 -W0.25p,red -Ggreen -L -Se0.2/0.39/18 \
    -B1g1 -Jx0.4/0.4 -A0.3p -P -V &gt; test.ps
#Long. Lat. Evel Nvel Esig Nsig CorEN SITE
#(deg) (deg) (mm/yr) (mm/yr)
0. -8. 0.0 0.0 4.0 6.0 0.500 4x6
-8. 5. 3.0 3.0 0.0 0.0 0.500 3x3
0. 0. 4.0 6.0 4.0 6.0 0.500
-5. -5. 6.0 4.0 6.0 4.0 0.500 6x4
5. 0. -6.0 4.0 6.0 4.0 -0.500 -6x4
0. -5. 6.0 -4.0 6.0 4.0 -0.500 6x-4
END
</pre>
<p> This example should plot some residual rates of rotation in the Western Transverse Ranges, California. The wedges will be dark gray, with light gray wedges to represent the 2-sigma uncertainties. </p>
<pre>
gmt psvelo &lt;&lt; END -Sw0.4/1.e7 -W0.75p -Gdarkgray -Elightgray -h1 -D2 -Jm2.2 \
    -R240./243./32.5/34.75 -Bf10ma60m/WeSn -P &gt; test.ps
#lon lat spin(rad/yr) spin_sigma (rad/yr)
241.4806 34.2073 5.65E-08 1.17E-08
241.6024 34.4468 -4.85E-08 1.85E-08
241.0952 34.4079 4.46E-09 3.07E-08
241.2542 34.2581 1.28E-07 1.59E-08
242.0593 34.0773 -6.62E-08 1.74E-08
241.0553 34.5369 -2.38E-07 4.27E-08
241.1993 33.1894 -2.99E-10 7.64E-09
241.1084 34.2565 2.17E-08 3.53E-08
END
</pre>
<h2>SEE ALSO</h2>
<p> <code>psmeca</code>, <code>pspolar</code>, <code>pscoupe</code>, <code>gmt</code>, <code>psbasemap</code>, <code>psxy</code></p>
<h2>REFERENCES</h2>
<p> Bomford, G., Geodesy, 4th ed., Oxford University Press, 1980.</p>
<h2>AUTHORS</h2>
<p> <i>Kurt L. Feigl</i>, Department of Geology and Geophysics at University of Wisconsin-Madison, Madison, Wisconsin, USA </p>
<p> Genevieve Patau, <i>Laboratory of Seismogenesis</i>, Institut de Physique du Globe de Paris, Departement de Sismologie, Paris, France</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
