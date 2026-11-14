---
title: "pspolar(1)"
name: "pspolar"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pspolar/"
description: "pspolar – Plot polarities on the inferior focal half-sphere on maps"
---

<h2>NAME</h2>
<p> pspolar &#8211; Plot polarities on the inferior focal half-sphere on maps</p>
<h2>SYNOPSIS</h2>
<p> pspolar [ <i>table</i> ] <i>lon/lat</i> <i>parameters</i> <i>region</i> <i>size</i> <i>&lt;symbol&gt;&lt;size&gt;</i> [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ <i>lon</i>/<i>lat</i>[/<i>dash_width</i>/<i>pointsize</i>] ] [ <i>color</i> ] [ <i>color</i> ] [ <i>color</i> ] [ ] [ ] [ ] [ ] [ <i>mode</i>[<i>args</i>] ] [ <i>angle</i>/<i>form</i>/<i>justify</i>/<i>fontsize</i> ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>pen</i> ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>pspolar</code> reads data values from <i>files</i> [or standard input] and generates PostScript code that will plot stations on focal mechanisms on a map. The PostScript code is written to standard output. </p>
<p> Parameters are expected to be in the following columns:</p>
<dl>
<dt><code>1</code>,<code>2</code>,<code>3</code>:</p>
<dd> station_code, azimuth, take-off angle</p>
<dt><code>4</code>:</p>
<dd> polarity:</p>
<dt>&bull;</p>
<dd> compression can be c,C,u,U,+</p>
<dt>&bull;</p>
<dd> rarefaction can be d,D,r,R,-</p>
<dt>&bull;</p>
<dd> not defined is anything else</dl>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension.</p>
<dt><code>-D</code><i>longitude/latitude</i></p>
<dd> Maps the bubble at given longitude and latitude point.</p>
<dt><code>-M</code><i>size</i></p>
<dd> Sets the size of the beach ball to plot polarities in. <i>Size</i> is in default units (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended).</p>
<dt><code>-S</code><i>&lt;symbol_type&gt;&lt;size&gt;</i></p>
<dd> Selects <i>symbol_type</i> and symbol <i>size</i>. Size is in default inits (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended). Choose symbol type from st(<i>a</i>)r, (<i>c</i>)ircle, (<i>d</i>)iamond, (<i>h</i>)exagon, (<i>i</i>)nverted triangle, (<i>p</i>)oint, (<i>s</i>)quare, (<i>t</i>)riangle, (<i>x</i>)cross.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code></p>
<dd> Offsets focal mechanisms to the latitude and longitude specified in the last two columns of the input file.</p>
<dt><code>-E</code>color</p>
<dd> Selects filling of symbols for stations in extensive quadrants. Set the color [Default is 250]. If <code>-E</code><i>color</i> is the same as <code>-F</code><i>color</i>, use <code>-e</code> to outline.</p>
<dt><code>-F</code><i>color</i></p>
<dd> Sets background color of the beach ball. Default is no fill.</p>
<dt><code>-G</code><i>color</i></p>
<dd> Selects filling of symbols for stations in compressional quadrants. Set the color [Default is black].</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-N</code></p>
<dd> Does <code>not</code> skip symbols that fall outside map border [Default plots points inside border only].</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code><i>mode</i>[<i>args</i>]</p>
<dd> Sets one or more attributes; repeatable. The various combinations are</p>
<dt><code>-Qe</code>[pen]</p>
<dd> Outline symbols in extensive quadrants using <i>pen</i> or the default pen (see ).</p>
<dt><code>-Qf</code>[pen]</p>
<dd> Outline the beach ball using <i>pen</i> or the default pen (see ).</p>
<dt><code>-Qg</code>[pen]</p>
<dd> Outline symbols in compressional quadrants using <i>pen</i> or the default pen (see ).</p>
<dt><code>-Qh</code></p>
<dd> Use special format derived from HYPO71 output</p>
<dt><code>-Qs</code><i>half-size</i>/[<code>V</code>[<i>v_width/h_length/h_width/shape</i>]][<code>G</code><i>color</i>][<code>L</code>]</p>
<dd> Plots S polarity azimuth. S polarity is in last column. It may be a vector (<code>V</code> flag) or a segment. Give <i>half-size,v_width,h_length,h_width</i> in default units (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended). [<code>L</code>] flag is for outline. See <i>Vector Attributes</i> for specifying additional attributes.</p>
<dt><code>-Qt</code><i>pen</i></p>
<dd> Set pen color to write station code. Default uses the default pen (see ).</p>
<dt><code>-T</code><i>angle/form/justify/fontsize in points</i></p>
<dd> To write station code. [Default is 0.0/0/5/12].</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<code>&#8211;</code>|<code>+</code>][<i>pen</i>][<i>attr</i>] <i>(more &#8230;)</i></p>
<dd> Set current pen attributes [Defaults: width = default, color = black, style = solid]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
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
<pre>
gmt pspolar -R239/240/34/35.2 -JM8c -N -Sc0.4 -h1 -D39.5/34.5 -M5 &lt;&lt; END &gt; test.ps
#stat azim ih pol
0481 11 147 c
6185 247 120 d
0485 288 114 +
0490 223 112 -
0487 212 109 .
END
</pre>
<p> or </p>
<pre>
gmt pspolar -R239/240/34/35.2 -JM8c -N -Sc0.4 -h1 -D239.5/34.5 -M5 &lt;&lt;END &gt; test.ps
#Date Or. time stat azim ih
910223 1 22 0481 11 147 ipu0
910223 1 22 6185 247 120 ipd0
910223 1 22 0485 288 114 epu0
910223 1 22 0490 223 112 epd0
910223 1 22 0487 212 109 epu0
END
</pre>
<h2>SEE ALSO</h2>
<p> <code>psmeca</code>, <code>psvelo</code>, <code>pscoupe</code>, <code>gmt</code>, <code>psbasemap</code>, <code>psxy</code></p>
<h2>REFERENCES</h2>
<p> Bomford, G., Geodesy, 4th ed., Oxford University Press, 1980. </p>
<p> Aki, K. and P. Richards, Quantitative Seismology, Freeman, 1980.</p>
<h2>AUTHORS</h2>
<p> Genevieve Patau, <i>Laboratory of Seismogenesis &lt;<a rel="nofollow" href="http://www.ipgp.fr/rech/sismogenese/">http://www.ipgp.fr/rech/sismogenese/</a>&gt;</i>, Institut de Physique du Globe de Paris, Departement de Sismologie, Paris, France</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
