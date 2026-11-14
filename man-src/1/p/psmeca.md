---
title: "psmeca(1)"
name: "psmeca"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psmeca/"
description: "psmeca – Plot focal mechanisms on maps"
---

<h2>NAME</h2>
<p> psmeca &#8211; Plot focal mechanisms on maps</p>
<h2>SYNOPSIS</h2>
<p> psmeca [ <i>table</i> ] <i>parameters</i> <i>region</i> [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ [<i>pen</i>][<code>P</code><i>pointsize</i>] ] [ <i>depmin</i>/<i>depmax</i> ] [ <i>fill</i>] [ <i>mode</i>[<i>args</i>] ] [ <i>fill</i>] [ ] [ [<i>pen</i>] ] [ ] [ ] [ ] [ ] [ <i>&lt;format&gt;&lt;scale&gt;</i>[/<code>d</code>]] [ <i>num_of_plane</i>[<i>pen</i>] ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>pen</i> ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <i>cpt</i>] [ <code>-c</code><i>copies</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>psmeca</code> reads data values from <i>files</i> [or standard input] and generates PostScript code that will plot focal mechanisms on a map. Most options are the same as for <code>psxy</code>. The PostScript code is written to standard output.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. </p>
<p> <code>-S</code><i>&lt;format&gt;&lt;scale&gt;</i>[/<code>d</code>] </p>
<p> Selects the meaning of the columns in the data file . In order to use the same file to plot cross-sections, depth is in third column. Nevertheless, it is possible to use &quot;old style&quot; <code>psvelomeca</code> input files without depth in third column using the <code>-o</code> option. </p>
<p> <code>-Sa</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]] </p>
<p> Focal mechanisms in Aki and Richards convention. <i>scale</i> adjusts the scaling of the radius of the &quot;beach ball&quot;, which will be proportional to the magnitude. Scale is the size for magnitude = 5 in inch (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended). Use the <code>-T</code> option to render the beach ball transparent by drawing only the nodal planes and the circumference. The color or shade of the compressive quadrants can be specified with the <code>-G</code> option. The color or shade of the extensive quadrants can be specified with the <code>-E</code> option. Append <code>u</code> to have the text appear below the beach ball (default is above). Parameters are expected to be in the following columns: <code>1</code>,<code>2</code>: longitude, latitude of event (<code>-:</code> option interchanges order) <code>3</code>: depth of event in kilometers <code>4</code>,<code>5</code>,<code>6</code>: strike, dip and rake in degrees <code>7</code>: magnitude <code>8</code>,<code>9</code>: longitude, latitude at which to place beach ball. Entries in these columns are necessary with the <code>-C</code> option. Using 0,0 in columns 8 and 9 will plot the beach ball at the longitude, latitude given in columns 1 and 2. The <code>-:</code> option will interchange the order of columns (1,2) and (8,9). <code>10</code>: Text string to appear above or below the beach ball (optional). </p>
<p> <code>-Sc</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]] </p>
<p> Focal mechanisms in Harvard CMT convention. <i>scale</i> adjusts the scaling of the radius of the &quot;beach ball&quot;, which will be proportional to the magnitude. Scale is the size for magnitude = 5 (that is M0 = 4.0E23 dynes-cm) in inch (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended). Use the <code>-T</code> option to render the beach ball transparent by drawing only the nodal planes and the circumference. The color or shade of the compressive quadrants can be specified with the <code>-G</code> option. The color or shade of the extensive quadrants can be specified with the <code>-E</code> option. Append <code>u</code> to have the text appear below the beach ball (default is above). Parameters are expected to be in the following columns: <code>1</code>,<code>2</code>: longitude, latitude of event (<code>-:</code> option interchanges order) <code>3</code>: depth of event in kilometers <code>4</code>,<code>5</code>,<code>6</code>: strike, dip, and rake of plane 1 <code>7</code>,<code>8</code>,<code>9</code>: strike, dip, and rake of plane 2 <code>10</code>,<code>11</code>: mantissa and exponent of moment in dyne-cm <code>12</code>,<code>13</code>: longitude, latitude at which to place beach ball. Entries in these columns are necessary with the <code>-C</code> option. Using (0,0) in columns 12 and 13 will plot the beach ball at the longitude, latitude given in columns 1 and 2. The <code>-:</code> option will interchange the order of columns (1,2) and (12,13). <code>14</code>: Text string to appear above or below the beach ball (optional). </p>
<p> <code>-Sm|d|z</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]] </p>
<p> Seismic moment tensor (Harvard CMT, with zero trace). <i>scale</i> adjusts the scaling of the radius of the &quot;beach ball&quot;, which will be proportional to the magnitude. Scale is the size for magnitude = 5 (that is scalar seismic moment = 4.0E23 dynes-cm) in inch (unless <code>c</code>, <code>i</code>, <code>m</code>, or <code>p</code> is appended). (<code>-T</code><i>0</i> option overlays best double couple transparently.) Use <code>-Sm</code> to plot the Harvard CMT seismic moment tensor with zero trace. Use <code>-Sd</code> to plot only the double couple part of moment tensor. Use <code>-Sz</code> to plot the anisotropic part of moment tensor (zero trace). The color or shade of the compressive quadrants can be specified with the <code>-G</code> option. The color or shade of the extensive quadrants can be specified with the <code>-E</code> option. Append <code>u</code> to have the text appear below the beach ball (default is above). Parameters are expected to be in the following columns: <code>1</code>,<code>2</code>: longitude, latitude of event (<code>-:</code> option interchanges order) <code>3</code>: depth of event in kilometers <code>4</code>,<code>5</code>,<code>6</code>,<code>7</code>,<code>8</code>,<code>9</code>: mrr, mtt, mff, mrt, mrf, mtf in 10*exponent dynes-cm <code>10</code>: exponent <code>11</code>,<code>12</code>: longitude, latitude at which to place beach ball. Entries in these columns are necessary with the <code>-C</code> option. Using (0,0) in columns 11 and 12 will plot the beach ball at the longitude, latitude given in columns 1 and 2. The <code>-:</code> option will interchange the order of columns (1,2) and (11,12). <code>13</code>: Text string to appear above or below the beach ball (optional). </p>
<p> <code>-Sp</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]] </p>
<p> Focal mechanisms given with partial data on both planes. <i>scale</i> adjusts the scaling of the radius of the &quot;beach ball&quot;, which will be proportional to the magnitude. Scale is the size for magnitude = 5 in inch (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended). The color or shade of the compressive quadrants can be specified with the <code>-G</code> option. The color or shade of the extensive quadrants can be specified with the <code>-E</code> option. Append <code>u</code> to have the text appear below the beach ball (default is above). Parameters are expected to be in the following columns: <code>1</code>,<code>2</code>: longitude, latitude of event (<code>-:</code> option interchanges order) <code>3</code>: depth of event in kilometers <code>4</code>,<code>5</code>: strike, dip of plane 1 <code>6</code>: strike of plane 2 <code>7</code>: must be -1/+1 for a normal/inverse fault <code>8</code>: magnitude <code>9</code>,<code>10</code>: longitude, latitude at which to place beach ball. Entries in these columns are necessary with the <code>-C</code> option. Using (0,0) in columns 9 and 10 will plot the beach ball at the longitude, latitude given in columns 1 and 2. The <code>-:</code> option will interchange the order of columns (1,2) and (9,10). <code>11</code>: Text string to appear above or below the beach ball (optional). </p>
<p> <code>-Sx|y|t</code><i>scale[/fontsize[/offset</i>[<code>u</code>]]] </p>
<p> Principal axis. <i>scale</i> adjusts the scaling of the radius of the &quot;beach ball&quot;, which will be proportional to the magnitude. Scale is the size for magnitude = 5 (that is seismic scalar moment = 4*10e+23 dynes-cm) in inch (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended). (<code>-T</code><i>0</i> option overlays best double couple transparently.) Use <code>-Sx</code> to plot standard Harvard CMT. Use <code>-Sy</code> to plot only the double couple part of moment tensor. Use <code>-St</code> to plot zero trace moment tensor. The color or shade of the compressive quadrants can be specified with the <code>-G</code> option. The color or shade of the extensive quadrants can be specified with the <code>-E</code> option. Append <code>u</code> to have the text appear below the beach ball (default is above). Parameters are expected to be in the following columns: <code>1</code>,<code>2</code>: longitude, latitude of event (<code>-:</code> option interchanges order) <code>3</code>: depth of event in kilometers <code>4</code>,<code>5</code>,<code>6</code>,<code>7</code>,<code>8</code>,<code>9</code>,<code>10</code>,<code>11</code>,<code>12</code>: value (in 10*exponent dynes-cm), azimuth, plunge of T, N, P axis. <code>13</code>: exponent <code>14</code>,<code>15</code>: longitude, latitude at which to place beach ball. Entries in these columns are necessary with the <code>-C</code> option. Using (0,0) in columns 14 and 15 will plot the beach ball at the longitude, latitude given in columns 1 and 2. The <code>-:</code> option will interchange the order of columns (1,2) and (14,15). <code>16</code>: Text string to appear above or below the beach ball (optional).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code>[<i>pen</i>][<code>P</code><i>pointsize</i>]</p>
<dd> Offsets focal mechanisms to the longitude, latitude specified in the last two columns of the input file before the (optional) text string. A small circle is plotted at the initial location and a line connects the beachball to the circle. Specify <i>pen</i> and/or <i>pointsize</i> to change the line style and/or size of the circle. [Defaults: <i>pen</i> as given by <code>-W</code>; <i>pointsize</i> 0].</p>
<dt><code>-D</code><i>depmin/depmax</i></p>
<dd> Plots events between depmin and depmax.</p>
<dt><code>-E</code><i>fill</i></p>
<dd> Selects filling of extensive quadrants. Usually white. Set the color [Default is white].</p>
<dt><code>-F</code><i>mode</i>[<i>args</i>]</p>
<dd> Sets one or more attributes; repeatable. The various combinations are</p>
<dt><code>-Fa</code>[<i>size</i>][/<i>P_axis_symbol</i>[<i>T_axis_symbol</i>]]</p>
<dd> Computes and plots P and T axes with symbols. Optionally specify <i>size</i> and (separate) P and T axis symbols from the following: (<code>c</code>) circle, (<code>d</code>) diamond, (<code>h</code>) hexagon, (<code>i</code>) inverse triangle, (<code>p</code>) point, (<code>s</code>) square, (<code>t</code>) triangle, (<code>x</code>) cross. [Default: 6<code>p</code>/<code>cc</code>]</p>
<dt><code>-Fe</code><i>fill</i></p>
<dd> Sets the color or fill pattern for the T axis symbol. [Default as set by <code>-E</code>]</p>
<dt><code>-Fg</code><i>fill</i></p>
<dd> Sets the color or fill pattern for the P axis symbol. [Default as set by <code>-G</code>]</p>
<dt><code>-Fo</code></p>
<dd> Use the <code>psvelomeca</code> input format without depth in the third column.</p>
<dt><code>-Fp</code>[<i>pen</i>]</p>
<dd> Draws the P axis outline using default pen (see <code>-W</code>), or sets pen attributes.</p>
<dt><code>-Fr</code>[<i>fill</i>]</p>
<dd> Draw a box behind the label (if any). [Default fill is white]</p>
<dt><code>-Ft</code>[<i>pen</i>]</p>
<dd> Draws the T axis outline using default pen (see <code>-W</code>), or sets pen attributes.</p>
<dt><code>-Fz</code>[<i>pen</i>]</p>
<dd> Overlay zero trace moment tensor using default pen (see <code>-W</code>), or sets pen attributes.</p>
<dt><code>-G</code><i>fill</i></p>
<dd> Selects filling of focal mechanisms. By convention, the compressional quadrants of the focal mechanism beach balls are shaded. Set the color [Default is black].</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code><i>pen</i></p>
<dd> Draws the &quot;beach ball&quot; outline with <i>pen</i> attributes instead of with the default pen set by <code>-W</code>.</p>
<dt><code>-M</code></p>
<dd> Use the same size for any magnitude. Size is given with <code>-S</code>.</p>
<dt><code>-N</code></p>
<dd> Does <code>not</code> skip symbols that fall outside frame boundary specified by <code>-R</code> [Default plots symbols inside frame only].</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-T</code>[<i>num_of_planes</i>][<code>/</code><i>pen</i>]</p>
<dd> Plots the nodal planes and outlines the bubble which is transparent. If <i>num_of_planes</i> is </p>
<p> <i>0</i>: both nodal planes are plotted; </p>
<p> <i>1</i>: only the first nodal plane is plotted; </p>
<p> <i>2</i>: only the second nodal plane is plotted. </p>
<p> Append <code>/</code><i>pen</i> to set the pen attributes for this feature. Default pen is as set by <code>-W</code>.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code><i>pen</i></p>
<dd> Set pen attributes for all lines and the outline of symbols [Defaults: width = default, color = black, style = solid]. This setting applies to <code>-C</code>, <code>-L</code>, <code>-T</code>, <code>-p</code>, <code>-t</code>, and <code>-z</code>, unless overruled by options to those arguments. </p>
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
<h2>EXAMPLES</h2>
<p> The following file should give a normal-faulting CMT mechanism: </p>
<pre>
gmt psmeca -R239/240/34/35.2 -Jm4c -Sc0.4 -h1 &lt;&lt; END &gt; test.ps
lon lat depth str dip slip st dip slip mant exp plon plat
239.384 34.556 12. 180 18 -88 0 72 -90 5.5 0 0 0
END
</pre>
<h2>SEE ALSO</h2>
<p> <code>pspolar</code>, <code>psvelo</code>, <code>pscoupe</code>, <code>gmt</code>, <code>psbasemap</code>, <code>psxy</code></p>
<h2>REFERENCES</h2>
<p> Bomford, G., Geodesy, 4th ed., Oxford University Press, 1980. </p>
<p> Aki, K. and P. Richards, Quantitative Seismology, Freeman, 1980. </p>
<p> F. A. Dahlen and Jeroen Tromp, Theoretical Seismology, Princeton, 1998, p.167. </p>
<p> Cliff Frohlich, Cliff&#8217;s Nodes Concerning Plotting Nodal Lines for P, Sh and Sv </p>
<p> Seismological Research Letters, Volume 67, Number 1, January-February, 1996 </p>
<p> Thorne Lay, Terry C. Wallace, Modern Global Seismology, Academic Press, 1995, p.384. </p>
<p> W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery, Numerical Recipes in C, Cambridge University press (routine jacobi)</p>
<h2>AUTHORS</h2>
<p> Genevieve Patau, <i>Laboratory of Seismogenesis &lt;<a rel="nofollow" href="http://www.ipgp.fr/rech/sismogenese/">http://www.ipgp.fr/rech/sismogenese/</a>&gt;</i>, Institut de Physique du Globe de Paris, Departement de Sismologie, Paris, France</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
