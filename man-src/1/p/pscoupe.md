---
title: "pscoupe(1)"
name: "pscoupe"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pscoupe/"
description: "pscoupe – Plot cross-sections of focal mechanisms"
---

<h2>NAME</h2>
<p> pscoupe &#8211; Plot cross-sections of focal mechanisms</p>
<h2>SYNOPSIS</h2>
<p> <code>pscoupe</code> [ <i>files</i> ] <i>parameters</i> <i>region</i> <i>parameters</i> [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ <i>color</i> ] [ <i>mode</i>[<i>args</i>] ] [ <i>color</i> ] [ ] [ <i>[pen]</i> ] [ ] [ ] [ ] [ ] [ <i>&lt;symbol&gt;&lt;scale&gt;</i>[/<code>d</code>] ] [ <i>n</i> ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>pen</i> ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <i>cpt</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>pscoupe</code> reads data values from <i>files</i> [or standard input] and generates PostScript code that will plot symbols, lines or polygons on a cross-section. Focal mechanisms may be specified and require additional columns of data. The PostScript code is written to standard output. </p>
<p> Unless is used, new file is created with the new coordinates (<code>x</code>, <code>y</code>) and the mechanism (from lower focal half-sphere for horizontal plane, to half-sphere behind a vertical plane). When the plane is not horizontal, &#8211; north direction becomes upwards steepest descent direction of the plane (u) &#8211; east direction becomes strike direction of the plane (s) &#8211; down direction (= north^east) becomes u^s Axis angles are defined in the same way as in horizontal plane in the new system. Moment tensor (initially in r, t, f system that is up, south, east) is defined in (-u^s, -u, s) system.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. If frame is defined from cross-section parameters (see <code>-A</code> this option is not taken into account, but must be present.</p>
<dt><code>-A</code></p>
<dd> selects the cross-section.</p>
<dt><code>-Aa</code><i>lon1/lat1/lon2/lat2/dip/p_width/dmin/dmax</i>[<code>f</code>]</p>
<dd> <i>lon</i> and <i>lat</i> are the longitude and latitude of points 1 and 2 limiting the length of the cross-section. <i>dip</i> is the dip of the plane on which the cross-section is made. <i>p_width</i> is the width of the cross-section on each side of a vertical plane or above and under an oblique plane. <i>dmin</i> and <i>dmax</i> are the distances min and max from horizontal plane, along steepest descent direction. Add <code>f</code> to get the frame from the cross-section parameters.</p>
<dt><code>-Ab</code><i>lon1/lat1/strike/p_length/dip/p_width/dmin/dmax</i>[<code>f</code>]</p>
<dd> <i>lon1</i> and <i>lat1</i> are the longitude and latitude of the beginning of the cross-section. <i>strike</i> is the azimuth of the direction of the cross-section. <i>p_length</i> is the length along which the cross-section is made. The other parameters are the same as for <code>-Aa</code> option.</p>
<dt><code>-Ac</code><i>x1/y1/x2/y2/dip/p_width/dmin/dmax</i>[<code>f</code>]</p>
<dd> The same as <code>-Aa</code> option with <i>x</i> and <i>y</i> cartesian coordinates.</p>
<dt><code>-Ad</code><i>x1/y1/strike/p_length/dip/p_width/dmin/dmax</i>[<code>f</code>]</p>
<dd> The same as <code>-Ab</code> option with <i>x</i> and <i>y</i> cartesian coordinates.</p>
<dt><code>-S</code></p>
<dd> selects the meaning of the columns in the data file and the figure to be plotted.</p>
<dt><code>-Sa</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]]</p>
<dd> Focal mechanisms in Aki and Richards convention. <i>scale</i> adjusts the scaling of the radius of the &quot;beach ball&quot;, which will be proportional to the magnitude. The <i>scale</i> is the size for magnitude = 5 in <code>PROJ_LENGTH_UNIT</code> (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended to indicate that the size information is in units of cm, inches, meters, or points, respectively). Use the <code>-T</code> option to render the beach ball transparent by drawing only the nodal planes and the circumference. The color or shade of the compressive quadrants can be specified with the <code>-G</code> option. The color or shade of the extensive quadrants can be specified with the <code>-E</code> option. Parameters are expected to be in the following columns:</p>
<dt><code>1</code>,<code>2</code>:</p>
<dd> longitude, latitude of event (<code>-:</code> option interchanges order)</p>
<dt><code>3</code>:</p>
<dd> depth of event in kilometers</p>
<dt><code>4</code>,<code>5</code>,<code>6</code>:</p>
<dd> strike, dip and rake</p>
<dt><code>7</code>:</p>
<dd> magnitude</p>
<dt><code>8</code>,<code>9</code>:</p>
<dd> not used; can be 0 0; allows use of the psmeca file format</p>
<dt><code>10</code>:</p>
<dd> text string to appear above the beach ball (default) or under (add <code>u</code>).</p>
<dt><code>-Sc</code><i>scale</i></p>
<dd> Focal mechanisms in Harvard CMT convention. <i>scale</i> adjusts the scaling of the radius of the &quot;beach ball&quot;, which will be proportional to the magnitude. The <i>scale</i> is the size for magnitude = 5 (that is M0 = 4E+23 dynes-cm.) in <code>PROJ_LENGTH_UNIT</code> (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended to indicate that the size information is in units of cm, inches, meters, or points, respectively). Use the <code>-T</code> option to render the beach ball transparent by drawing only the nodal planes and the circumference. The color or shade of the compressive quadrants can be specified with the <code>-G</code> option. The color or shade of the extensive quadrants can be specified with the <code>-E</code> option. Parameters are expected to be in the following columns:</p>
<dt><code>1</code>,<code>2</code>:</p>
<dd> longitude, latitude of event (<code>-:</code> option interchanges order)</p>
<dt><code>3</code>:</p>
<dd> depth of event in kilometers</p>
<dt><code>4</code>,<code>5</code>,<code>6</code>:</p>
<dd> strike, dip, and slip of plane 1</p>
<dt><code>7</code>,<code>8</code>,<code>9</code>:</p>
<dd> strike, dip, and slip of plane 2</p>
<dt><code>10</code>,<code>11</code>:</p>
<dd> mantissa and exponent of moment in dyne-cm (if magnitude is uses instead of scalar moment, magnitude is in column 10 and 0 must be in column 11)</p>
<dt><code>12</code>,<code>13</code>:</p>
<dd> not used; can be 0 0; allows use of the psmeca file format</p>
<dt><code>14</code>:</p>
<dd> text string to appear above the beach ball (default) or under (add <code>u</code>).</p>
<dt><code>-Sp</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]]</p>
<dd> Focal mechanisms given with partial data on both planes. <i>scale</i> adjusts the scaling of the radius of the &quot;beach ball&quot;, which will be proportional to the magnitude. The <i>scale</i> is the size for magnitude = 5 in <code>PROJ_LENGTH_UNIT</code> (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended to indicate that the size information is in units of cm, inches, meters, or points, respectively). The color or shade of the compressive quadrants can be specified with the <code>-G</code> option. The color or shade of the extensive quadrants can be specified with the <code>-E</code> option. Parameters are expected to be in the following columns:</p>
<dt><code>1</code>,<code>2</code>:</p>
<dd> longitude, latitude of event (<code>-:</code> option interchanges order)</p>
<dt><code>3</code>:</p>
<dd> depth</p>
<dt><code>4</code>,<code>5</code>:</p>
<dd> strike, dip of plane 1</p>
<dt><code>6</code>:</p>
<dd> strike of plane 2</p>
<dt><code>7</code>:</p>
<dd> must be -1/+1 for a normal/inverse fault</p>
<dt><code>8</code>:</p>
<dd> magnitude</p>
<dt><code>9</code>,<code>10</code>:</p>
<dd> not used; can be 0 0; allows use of the psmeca file format</p>
<dt><code>11</code>:</p>
<dd> text string to appear above the beach ball (default) or under (add <code>u</code>).</p>
<dt><code>-Sm|d|z</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]]</p>
<dd> Seismic moment tensor (Harvard CMT, with zero trace). <i>scale</i> adjusts the scaling of the radius of the &quot;beach ball&quot;, which will be proportional to the magnitude. The <i>scale</i> is the size for magnitude = 5 (that is seismic scalar moment = 4E+23 dynes-cm) in <code>PROJ_LENGTH_UNIT</code> (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended to indicate that the size information is in units of cm, inches, meters, or points, respectively). (<code>-T</code><i>0</i> option overlays best double couple transparently.)</p>
<dt><code>-Sd</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]]</p>
<dd> to plot the only double couple part of moment tensor.</p>
<dt><code>-Sz</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]]</p>
<dd> to plot anisotropic part of moment tensor (zero trace). The color or shade of the compressive quadrants can be specified with the <code>-G</code> option. The color or shade of the extensive quadrants can be specified with the <code>-E</code> option. Parameters are expected to be in the following columns:</p>
<dt><code>1</code>,<code>2</code>:</p>
<dd> longitude, latitude of event (<code>-:</code> option interchanges order)</p>
<dt><code>3</code>:</p>
<dd> depth of event in kilometers</p>
<dt><code>4</code>,<code>5</code>,<code>6</code>,<code>7</code>,<code>8</code>,<code>9</code>:</p>
<dd> mrr, mtt, mff, mrt, mrf, mtf in 10*exponent dynes-cm</p>
<dt><code>10</code>:</p>
<dd> exponent</p>
<dt><code>11</code>,<code>12</code>:</p>
<dd> Not used; can be 0 0; allows use of the psmeca file format</p>
<dt><code>13</code>:</p>
<dd> Text string to appear above the beach ball (default) or under (add <code>u</code>).</p>
<dt><code>-Sx</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]]</p>
<dd> Principal axis. <i>scale</i> adjusts the scaling of the radius of the &quot;beach ball&quot;, which will be proportional to the magnitude. The <i>scale</i> is the size for magnitude = 5 (that is seismic scalar moment = 4*10e+23 dynes-cm) in <code>PROJ_LENGTH_UNIT</code> (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended to indicate that the size information is in units of cm, inches, meters, or points, respectively). (<code>-T0</code> option overlays best double couple transparently.)</p>
<dt><code>-Sy</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]]</p>
<dd> to plot the only double couple part of moment tensor.</p>
<dt><code>-St</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]]</p>
<dd> to plot anisotropic part of moment tensor (zero trace). The color or shade of the compressive quadrants can be specified with the <code>-G</code> option. The color or shade of the extensive quadrants can be specified with the <code>-E</code> option. Parameters are expected to be in the following columns:</p>
<dt><code>1</code>,<code>2</code>:</p>
<dd> longitude, latitude of event (<code>-:</code> option interchanges order)</p>
<dt><code>3</code>:</p>
<dd> depth of event in kilometers</p>
<dt><code>4</code>,<code>5</code>,<code>6</code>,<code>7</code>,<code>8</code>,<code>9</code>,<code>10</code>,<code>11</code>,<code>12</code>:</p>
<dd> value (in 10*exponent dynes-cm), azimuth, plunge of the T, N, and P axes.</p>
<dt><code>13</code>:</p>
<dd> exponent</p>
<dt><code>14</code>,<code>15</code>:</p>
<dd> longitude, latitude at which to place beach ball. Entries in these columns are necessary with the <code>-C</code> option. Using 0,0 in columns 9 and 10 will plot the beach ball at the longitude, latitude given in columns 1 and 2. The <code>-:</code> option will interchange the order of columns (1,2) and (9,10).</p>
<dt><code>16</code>:</p>
<dd> Text string to appear above the beach ball (optional).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-E</code><i>color</i></p>
<dd> Sets color or fill pattern for extensive quadrants [Default is white].</p>
<dt><code>-F</code><i>mode</i>[<i>args</i>]</p>
<dd> Sets one or more attributes; repeatable. The various combinations are</p>
<dt><code>-Fs</code><i>symbol[size[/fontsize[/offset</i>[<code>u</code>]]]</p>
<dd> selects a symbol instead of mechanism. Choose from the following: (<code>c</code>) circle, (<code>d</code>) diamond, (<code>i</code>) itriangle, (<code>s</code>) square, (<code>t</code>) triangle, (<code>x</code>) cross. <i>size</i> is the symbol size in <code>PROJ_LENGTH_UNIT</code> (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended to indicate that the size information is in units of cm, inches, meters, or points, respectively). If <i>size</i> must be read, it must be in column 4 and the text string will start in column 5. Parameters are expected to be in the following columns:</p>
<dt><code>1</code>,<code>2</code>:</p>
<dd> longitude, latitude of event (<code>-:</code> option interchanges order)</p>
<dt><code>3</code>:</p>
<dd> depth of event in kilometers</p>
<dt><code>4</code>:</p>
<dd> Text string to appear above the beach ball (default) or under (add <code>u</code>).</p>
<dt><code>-Fa</code>[<i>size</i>][/<i>P_symbol</i>[/<i>T_symbol</i>]]</p>
<dd> Computes and plots P and T axes with symbols. Optionally specify <i>size</i> and (separate) P and T axis symbols from the following: (<code>c</code>) circle, (<code>d</code>) diamond, (<code>h</code>) hexagon, (<code>i</code>) inverse triangle, (<code>p</code>) point, (<code>s</code>) square, (<code>t</code>) triangle, (<code>x</code>) cross. [Default: 6<code>p</code>/<code>cc</code>]</p>
<dt><code>-Fe</code><i>color</i></p>
<dd> Sets the color or fill pattern for the T axis symbol. [Default as set by ]</p>
<dt><code>-Fg</code><i>color</i></p>
<dd> Sets the color or fill pattern for the P axis symbol. [Default as set by ]</p>
<dt><code>-Fp</code>[<i>pen</i>]</p>
<dd> Draws the P axis outline using current pen (see ), or sets pen attributes.</p>
<dt><code>-Fr</code>[<i>color</i>]</p>
<dd> Draw a box behind the label (if any). [Default fill is white]</p>
<dt><code>-Ft</code>[<i>pen</i>]</p>
<dd> Draws the T axis outline using current pen (see <code>-W</code>), or sets pen attributes.</p>
<dt><code>-G</code><i>color</i></p>
<dd> Sets color or fill pattern for compressional quadrants [Default is black].</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code>[<i>pen</i>]</p>
<dd> Draws the &quot;beach ball&quot; outline using current pen (see ) or sets pen attributes.</p>
<dt><code>-M</code></p>
<dd> Same size for any magnitude.</p>
<dt><code>-N</code></p>
<dd> Does <code>not</code> skip symbols that fall outside map border [Default plots points inside border only].</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code></p>
<dd> Suppress the production of files with cross-section and mechanism information.</p>
<dt><code>-T</code>[<i>num_of_planes</i>]</p>
<dd> Plots the nodal planes and outlines the bubble which is transparent. If <i>num_of_planes</i> is <i>0</i>: both nodal planes are plotted; <i>1</i>: only the first nodal plane is plotted; <i>2</i>: only the second nodal plane is plotted [Default: 0].</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<code>&#8211;</code>|<code>+</code>][<i>pen</i>][<i>attr</i>] <i>(more &#8230;)</i></p>
<dd> set pen attributes for text string or default pen attributes for fault plane edges. [Defaults: width = default, color = black, style = solid]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-Z</code><i>cpt</i></p>
<dd> Give a CPT file and let compressive part color be determined by the z-value in the third column.</p>
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
<h2>SEE ALSO</h2>
<p> <code>psmeca</code>, <code>psvelo</code>, <code>pspolar</code>, <code>gmt</code>, <code>psbasemap</code>, <code>psxy</code></p>
<h2>REFERENCES</h2>
<p> Bomford, G., Geodesy, 4th ed., Oxford University Press, 1980. </p>
<p> Aki, K. and P. Richards, Quantitative Seismology, Freeman, 1980. </p>
<p> F. A. Dahlen and Jeroen Tromp, Theoretical Seismology, Princeton, 1998, p.167. Definition of scalar moment. </p>
<p> Cliff Frohlich, Cliff&#8217;s Nodes Concerning Plotting Nodal Lines for P, Sh and Sv </p>
<p> Seismological Research Letters, Volume 67, Number 1, January-February, 1996 </p>
<p> Thorne Lay, Terry C. Wallace, Modern Global Seismology, Academic Press, 1995, p.384. </p>
<p> W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery, Numerical Recipes in C, Cambridge University press (routine jacobi)</p>
<h2>AUTHOR</h2>
<p> Genevieve Patau, <i>Laboratory of Seismogenesis &lt;<a rel="nofollow" href="http://www.ipgp.fr/rech/sismogenese/">http://www.ipgp.fr/rech/sismogenese/</a>&gt;</i>, Institut de Physique du Globe de Paris, Departement de Sismologie, Paris, France</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
