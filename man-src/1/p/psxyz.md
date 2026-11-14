---
title: "psxyz(1)"
name: "psxyz"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psxyz/"
description: "psxyz – Plot lines, polygons, and symbols in 3-D"
---

<h2>NAME</h2>
<p> psxyz &#8211; Plot lines, polygons, and symbols in 3-D</p>
<h2>SYNOPSIS</h2>
<p> <code>psxyz</code> [ <i>table</i> ] <i>parameters</i> <code>z</code>|<code>Z</code><i>parameters</i> <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ <i>dx</i>/<i>dy</i>[/<i>dz</i>] ] [ <i>fill</i> ] [ <i>intens</i> ] [ ] [ [<code>+b</code>|<code>d</code>|<code>D</code>][<code>+xl</code>|<code>r</code>|<i>x0</i>][<code>+yl</code>|<code>r</code>|<i>y0</i>][<code>+p</code><i>pen</i>] ] [ ] [ ] [ ] [ ] [ [<i>symbol</i>][<i>size</i>[<code>unit</code>]][/<i>size_y</i>] ] [ ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ [<code>&#8211;</code>|<code>+</code>][<i>pen</i>] ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-a</code><i>&lt;flags&gt;</i> ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>psxyz</code> reads (x,y,z) triplets from <i>files</i> [or standard input] and generates PostScript code that will plot lines, polygons, or symbols at those locations in 3-D. If a symbol is selected and no symbol size given, then <code>psxyz</code> will interpret the fourth column of the input data as symbol size. Symbols whose <i>size</i> is &lt;= 0 are skipped. If no symbols are specified then the symbol code (see <code>-S</code> below) must be present as last column in the input. If <code>-S</code> is not used, a line connecting the data points will be drawn instead. To explicitly close polygons, use <code>-L</code>. Select a fill with <code>-G</code>. If <code>-G</code> is set, <code>-W</code> will control whether the polygon outline is drawn or not. If a symbol is selected, <code>-G</code> and <code>-W</code> determines the fill and outline/no outline, respectively. The PostScript code is written to standard output.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i></dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code><i>cpt</i></p>
<dd> Give a CPT file or specify -Ccolor1,color2[,color3,&#8230;] to build a linear continuous CPT from those colors automatically. In this case <i>color</i><code>n</code> can be a r/g/b triplet, a color name, or an HTML hexadecimal color (e.g. #aabbcc ). If <code>-S</code> is set, let symbol fill color be determined by the t-value in the fourth column. Additional fields are shifted over by one column (optional size would be in 5th rather than 4th field, etc.). If <code>-S</code> is not set, then <code>psxyz</code> expects the user to supply a multisegment file (where each segment header contains a <code>-Z</code><i>val</i> string. The <i>val</i> will control the color of the line or polygon (if <code>-L</code> is set) via the CPT file.</p>
<dt><code>-D</code><i>dx</i>/<i>dy</i>[/<i>dz</i>]</p>
<dd> Offset the plot symbol or line locations by the given amounts <i>dx/dy</i>[<i>dz</i>] [Default is no offset].</p>
<dt><code>-G</code><i>fill</i></p>
<dd> Select color or pattern for filling of symbols or polygons [Default is no fill]. Note that <code>psxyz</code> will search for <code>-G</code> and <code>-W</code> strings in all the segment headers and let any values thus found over-ride the command line settings.</p>
<dt><code>-I</code><i>intens</i></p>
<dd> Use the supplied <i>intens</i> value (nominally in the -1 to + 1 range) to modulate the fill color by simulating illumination [none].</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code>[<code>+b</code>|<code>d</code>|<code>D</code>][<code>+xl</code>|<code>r</code>|<i>x0</i>][<code>+yl</code>|<code>r</code>|<i>y0</i>][<code>+p</code><i>pen</i>]</p>
<dd> Force closed polygons. Alternatively, append modifiers to build a polygon from a line segment. Append <code>+d</code> to build symmetrical envelope around y(x) using deviations dy(x) given in extra column 4. Append <code>+D</code> to build asymmetrical envelope around y(x) using deviations dy1(x) and dy2(x) from extra columns 4-5. Append <code>+b</code> to build asymmetrical envelope around y(x) using bounds yl(x) and yh(x) from extra columns 4-5. Append <code>+xl</code>|<code>r</code>|<i>x0</i> to connect first and last point to anchor points at either xmin, xmax, or x0, or append <code>+yb</code>|<code>t</code>|<i>y0</i> to connect first and last point to anchor points at either ymin, ymax, or y0. Polygon may be painted (<code>-G</code>) and optionally outlined by adding <code>+p</code><i>pen</i> [no outline]. All constructed polygons are assumed to have a constant z value.</p>
<dt><code>-N</code>[<code>c</code>|<code>r</code>]</p>
<dd> Do NOT clip symbols that fall outside map border [Default plots points whose coordinates are strictly inside the map border only]. The option does not apply to lines and polygons which are always clipped to the map region. For periodic (360-longitude) maps we must plot all symbols twice in case they are clipped by the repeating boundary. The <code>-N</code> will turn off clipping and not plot repeating symbols. Use <code>-Nr</code> to turn off clipping but retain the plotting of such repeating symbols, or use <code>-Nc</code> to retain clipping but turn off plotting of repeating symbols.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code></p>
<dd> Turn off the automatic sorting of items based on their distance from the viewer. The default is to sort the items so that items in the foreground are plotted after items in the background.</p>
<dt><code>-S</code>[<i>symbol</i>][<i>size</i>[<code>u</code>]][/<i>size_y</i>]</p>
<dd> Plot symbols. If present, <i>size</i> is symbol size in the unit set in <code>gmt.conf</code> (unless <code>c</code>, <code>i</code>, or <code>p</code> is appended). If the symbol code (see below) is not given it will be read from the last column in the input data; this cannot be used in conjunction with binary input. Optionally, append <code>c</code>, <code>i</code>, or <code>p</code> to indicate that the size information in the input data is in units of cm, inch, or point, respectively [Default is <code>PROJ_LENGTH_UNIT</code>]. Note: if you give <i>both</i> size and symbol via the input file you must use <code>PROJ_LENGTH_UNIT</code> to indicate the units used for the symbol size or append the units to the size in the file. Some 2-dimensional symbols optionally take a second size via <i>size_y</i>. If symbol sizes are expected via the fourth data column then you may convert those values to suitable symbol sizes via the <code>-i</code> mechanism. </p>
<p> The uppercase symbols <code>A</code>, <code>C</code>, <code>D</code>, <code>G</code>, <code>H</code>, <code>I</code>, <code>N</code>, <code>S</code>, <code>T</code> are normalized to have the same area as a circle with diameter <i>size</i>, while the size of the corresponding lowercase symbols refers to the diameter of a circumscribed circle. </p>
<p> You can change symbols by adding the required <code>-S</code> option to any of your multisegment headers. </p>
<p> Choose between these symbol codes:</p>
<dt><code>-S-</code></p>
<dd> x-dash (-). <i>size</i> is the length of a short horizontal (x-dir) line segment.</p>
<dt><code>-S+</code></p>
<dd> plus (+). <i>size</i> is diameter of circumscribing circle.</p>
<dt><code>-Sa</code></p>
<dd> st<code>a</code>r. <i>size</i> is diameter of circumscribing circle.</p>
<dt><code>-Sb</code></p>
<dd> Vertical <code>b</code>ar extending from <i>base</i> to y. <i>size</i> is bar width. Append <code>u</code> if <i>size</i> is in x-units [Default is plot-distance units]. By default, <i>base</i> = ymin. Append <code>b</code>[<i>base</i>] to change this value. If <i>base</i> is not appended then we read it from the last input data column.</p>
<dt><code>-SB</code></p>
<dd> Horizontal <code>b</code>ar extending from <i>base</i> to x. <i>size</i> is bar width. Append <code>u</code> if <i>size</i> is in y-units [Default is plot-distance units]. By default, <i>base</i> = xmin. Append <code>b</code>[<i>base</i>] to change this value. If <i>base</i> is not appended then we read it from the last input data column.</p>
<dt><code>-Sc</code></p>
<dd> <code>c</code>ircle. <i>size</i> is diameter of circle.</p>
<dt><code>-Sd</code></p>
<dd> <code>d</code>iamond. <i>size</i> is diameter of circumscribing circle.</p>
<dt><code>-Se</code></p>
<dd> <code>e</code>llipse. Direction (in degrees counter-clockwise from horizontal), major_axis, and minor_axis must be found in columns 4, 5, and 6.</p>
<dt><code>-SE</code></p>
<dd> Same as <code>-Se</code>, except azimuth (in degrees east of north) should be given instead of direction. The azimuth will be mapped into an angle based on the chosen map projection (<code>-Se</code> leaves the directions unchanged.) Furthermore, the axes lengths must be given in km instead of plot-distance units. An exception occurs for a linear projection in which we assume the ellipse axes are given in the same units as <code>-R</code>. For degenerate ellipses (circles) with diameter given in km, use <code>-SE-</code>. The diameter is excepted to be given in column 4. Alternatively, append the desired diameter in km to <code>-SE-</code> and this fixed diameter is used instead.</p>
<dt><code>-Sf</code></p>
<dd> <code>f</code>ront. <code>-Sf</code><i>gap</i>[/<i>size</i>][<code>+l</code>|<code>+r</code>][<code>+b+c+f+s+t</code>][<code>+o</code><i>offset</i>][<code>+p</code>[<i>pen</i>]]. Supply distance gap between symbols and symbol size. If <i>gap</i> is negative, it is interpreted to mean the number of symbols along the front instead. If <i>size</i> is missing it is set to 30% of the <i>gap</i>, except when <i>gap</i> is negative and <i>size</i> is thus required. Append <code>+l</code> or <code>+r</code> to plot symbols on the left or right side of the front [Default is centered]. Append <code>+</code><i>type</i> to specify which symbol to plot: <code>b</code>ox, <code>c</code>ircle, <code>f</code>ault, <code>s</code>lip, or <code>t</code>riangle. [Default is <code>f</code>ault]. Slip means left-lateral or right-lateral strike-slip arrows (centered is not an option). The <code>+s</code> modifier optionally accepts the angle used to draw the vector [30]. Append <code>+o</code><i>offset</i> to offset the first symbol from the beginning of the front by that amount [0]. The chosen symbol is drawn with the same pen as set for the line (i.e., via <code>-W</code>). The use an alternate pen, append <code>+p</code><i>pen</i>. To skip the outline, just use <code>+p</code>. Note: By placing <code>-Sf</code> options in the segment header you can change the front types on a segment-by-segment basis.</p>
<dt><code>-Sg</code></p>
<dd> octa<code>g</code>on. <i>size</i> is diameter of circumscribing circle.</p>
<dt><code>-Sh</code></p>
<dd> <code>h</code>exagon. <i>size</i> is diameter of circumscribing circle.</p>
<dt><code>-Si</code></p>
<dd> <code>i</code>nverted triangle. <i>size</i> is diameter of circumscribing circle.</p>
<dt><code>-Sj</code></p>
<dd> Rotated rectangle. Direction (in degrees counter-clockwise from horizontal), x-dimension, and y-dimension must be found in columns 4, 5, and 6.</p>
<dt><code>-SJ</code></p>
<dd> Same as <code>-Sj</code>, except azimuth (in degrees east of north) should be given instead of direction. The azimuth will be mapped into an angle based on the chosen map projection (<code>-Sj</code> leaves the directions unchanged.) Furthermore, the dimensions must be given in km instead of plot-distance units. An exception occurs for a linear projection in which we assume the dimensions are given in the same units as <code>-R</code>.</p>
<dt><code>-Sk</code></p>
<dd> <code>k</code>ustom symbol. Append &lt;name&gt;/<i>size</i>, and we will look for a definition file called &lt;name&gt;.def in (1) the current directory or (2) in ~/.gmt or (3) in <code>$GMT_SHAREDIR</code>/custom. The symbol as defined in that file is of size 1.0 by default; the appended <i>size</i> will scale symbol accordingly. The symbols are plotted in the <i>x-y</i> plane. Users may add their own custom *.def files; see CUSTOM SYMBOLS below.</p>
<dt><code>-Sl</code></p>
<dd> <code>l</code>etter or text string (less than 64 characters). Give size, and append /<i>string</i> after the size. Note that the size is only approximate; no individual scaling is done for different characters. Remember to escape special characters like *. Optionally, you may append %<i>font</i> to select a particular font [Default is <code>FONT_ANNOT_PRIMARY</code>].</p>
<dt><code>-Sm</code></p>
<dd> <code>m</code>ath angle arc, optionally with one or two arrow heads [Default is no arrow heads]. The <i>size</i> is the length of the vector head. Arc width is set by <code>-W</code>. The radius of the arc and its start and stop directions (in degrees counter-clockwise from horizontal) must be given in columns 4-6. See VECTOR ATTRIBUTES for specifying attributes.</p>
<dt><code>-SM</code></p>
<dd> Same as <code>-Sm</code> but switches to straight angle symbol if angles subtend 90 degrees exactly.</p>
<dt><code>-Sn</code></p>
<dd> pe<code>n</code>tagon. <i>size</i> is diameter of circumscribing circle.</p>
<dt><code>-So</code></p>
<dd> c<code>o</code>lumn (3-D) extending from <i>base</i> to z. The <i>size</i> sets base width (Use <i>xsize/ysize</i> if not the same). Append <code>u</code> if <i>size</i> is in x-units [Default is plot-distance units]. If no <i>size</i> is given we expect both <i>xsize</i> and <i>ysize</i> as two extra data columns. By default, <i>base</i> = 0. Append <code>b</code><i>base</i> to change this value. The facet colors will be modified to simulate shading. Use <code>-SO</code> to disable such 3-D illumination. If <i>base</i> is not appended then we read it from the last input data column.</p>
<dt><code>-Sp</code></p>
<dd> <code>p</code>oint. No size needs to be specified (1 pixel is used).</p>
<dt><code>-Sq</code></p>
<dd> <code>q</code>uoted line, i.e., lines with annotations such as contours. It is assumed that each individual line has a constant <i>z</i> level (i.e., each line must lie in the <i>x-y</i> plane). Append [<code>d</code>|<code>D</code>|<code>f</code>|<code>l</code>|<code>L</code>|<code>n</code>|<code>x</code>|<code>X</code>]<i>info</i>[:<i>labelinfo</i>]. The required argument controls the placement of labels along the quoted lines. Choose among five controlling algorithms: <code>d</code><i>dist</i>[<code>c</code>|<code>i</code>|<code>p</code>] or <code>D</code><i>dist</i>[<code>d</code>|<code>e</code>|<code>f</code>|<code>k</code>|<code>m</code>|<code>M</code>|<code>n</code>|<code>s</code>] For lower case <code>d</code>, give distances between labels on the plot in your preferred measurement unit <code>c</code> (cm), <code>i</code> (inch), or <code>p</code> (points), while for upper case <code>D</code>, specify distances in map units and append the unit; choose among <code>e</code> (m), <code>f</code> (foot), <code>k</code> (km), <code>M</code> (mile), <code>n</code> (nautical mile) or <code>u</code> (US survey foot), and <code>d</code> (arc degree), <code>m</code> (arc minute), or <code>s</code> (arc second). [Default is 10<code>c</code> or 4<code>i</code>]. As an option, you can append /<i>fraction</i> which is used to place the very first label for each contour when the cumulative along-contour distance equals <i>fraction * dist</i> [0.25]. <code>f</code><i>ffile.d</i> Reads the ASCII file <i>ffile.d</i> and places labels at locations in the file that matches locations along the quoted lines. Inexact matches and points outside the region are skipped. <code>l|L</code><i>line1</i>[,*line2*,&#8230;] Give <i>start</i> and <i>stop</i> coordinates for one or more comma-separated straight line segments. Labels will be placed where these lines intersect the quoted lines. The format of each <i>line</i> specification is <i>start/stop</i>, where <i>start</i> and <i>stop</i> are either a specified point <i>lon/lat</i> or a 2-character <code>XY</code> key that uses the justification format employed in <code>pstext</code> to indicate a point on the map, given as [LCR][BMT]. <code>L</code> will interpret the point pairs as defining great circles [Default is straight line]. <code>n</code><i>n_label</i> Specifies the number of equidistant labels for quoted lines line [1]. Upper case <code>N</code> starts labeling exactly at the start of the line [Default centers them along the line]. <code>N</code>-1 places one justified label at start, while <code>N</code>+1 places one justified label at the end of quoted lines. Optionally, append /<i>min_dist</i>[<code>c</code>|<code>i</code>|<code>p</code>] to enforce that a minimum distance separation between successive labels is enforced. <code>x|X</code><i>xfile.d</i> Reads the multisegment file <i>xfile.d</i> and places labels at the intersections between the quoted lines and the lines in <i>xfile.d</i>. <code>X</code> will resample the lines first along great-circle arcs. In addition, you may optionally append <code>+r</code><i>radius</i>[<code>c</code>|<code>i</code>|<code>p</code>] to set a minimum label separation in the x-y plane [no limitation]. </p>
<p> The optional <i>labelinfo</i> controls the specifics of the label formatting and consists of a concatenated string made up of any of the following control arguments:</p>
<dt><code>+a</code><i>angle</i></p>
<dd> For annotations at a fixed angle, <code>+an</code> for line-normal, or <code>+ap</code> for line-parallel [Default].</p>
<dt><code>+c</code><i>dx</i>[/<i>dy</i>]</p>
<dd> Sets the clearance between label and optional text box. Append <code>c</code>|<code>i</code>|<code>p</code> to specify the unit or % to indicate a percentage of the label font size [15%].</p>
<dt><code>+d</code></p>
<dd> Turns on debug which will draw helper points and lines to illustrate the workings of the quoted line setup.</p>
<dt><code>+e</code></p>
<dd> Delay the plotting of the text. This is used to build a clip path based on the text, then lay down other overlays while that clip path is in effect, then turning of clipping with psclip <code>-Cs</code> which finally plots the original text.</p>
<dt><code>+f</code><i>font</i></p>
<dd> Sets the desired font [Default <code>FONT_ANNOT_PRIMARY</code> with its size changed to 9p].</p>
<dt><code>+g</code>[<i>color</i>]</p>
<dd> Selects opaque text boxes [Default is transparent]; optionally specify the color [Default is <code>PS_PAGE_COLOR</code>].</p>
<dt><code>+j</code><i>just</i></p>
<dd> Sets label justification [Default is MC]. Ignored when <code>-SqN</code>|<code>n</code>+|-1 is used.</p>
<dt><code>+l</code><i>label</i></p>
<dd> Sets the constant label text.</p>
<dt><code>+L</code><i>flag</i></p>
<dd> Sets the label text according to the specified flag: </p>
<p> <code>+Lh</code> Take the label from the current segment header (first scan for an embedded <code>-L</code><i>label</i> option, if not use the first word following the segment flag). For multiple-word labels, enclose entire label in double quotes. <code>+Ld</code> Take the Cartesian plot distances along the line as the label; append <code>c</code>|<code>i</code>|<code>p</code> as the unit [Default is <code>PROJ_LENGTH_UNIT</code>]. <code>+LD</code> Calculate actual map distances; append <code>d|e|f|k|n|M|n|s</code> as the unit [Default is <code>d</code>(egrees), unless label placement was based on map distances along the lines in which case we use the same unit specified for that algorithm]. Requires a map projection to be used. <code>+Lf</code> Use text after the 2nd column in the fixed label location file as the label. Requires the fixed label location setting. <code>+Lx</code> As <code>+Lh</code> but use the headers in the <i>xfile.d</i> instead. Requires the crossing file option.</p>
<dt><code>+n</code><i>dx</i>[/<i>dy</i>]</p>
<dd> Nudges the placement of labels by the specified amount (append <code>c</code>|<code>i</code>|<code>p</code> to specify the units). Increments are considered in the coordinate system defined by the orientation of the line; use <code>+N</code> to force increments in the plot x/y coordinates system [no nudging]. Not allowed with <code>+v</code>.</p>
<dt><code>+o</code></p>
<dd> Selects rounded rectangular text box [Default is rectangular]. Not applicable for curved text (<code>+v</code>) and only makes sense for opaque text boxes.</p>
<dt><code>+p</code>[<i>pen</i>]</p>
<dd> Draws the outline of text boxes [Default is no outline]; optionally specify pen for outline [Default is width = 0.25p, color = black, style = solid].</p>
<dt><code>+r</code><i>min_rad</i></p>
<dd> Will not place labels where the line&#8217;s radius of curvature is less than <i>min_rad</i> [Default is 0].</p>
<dt><code>+t</code>[<i>file</i>]</p>
<dd> Saves line label x, y, and text to <i>file</i> [Line_labels.txt]. Use <code>+T</code> to save x, y, angle, text instead.</p>
<dt><code>+u</code><i>unit</i></p>
<dd> Appends <i>unit</i> to all line labels. If <i>unit</i> starts with a leading hyphen (-) then there will be no space between label value and the unit. [Default is no unit].</p>
<dt><code>+v</code></p>
<dd> Specifies curved labels following the path [Default is straight labels].</p>
<dt><code>+w</code></p>
<dd> Specifies how many (<i>x</i>,<i>y</i>) points will be used to estimate label angles [Default is 10].</p>
<dt><code>+=</code><i>prefix</i></p>
<dd> Prepends <i>prefix</i> to all line labels. If <i>prefix</i> starts with a leading hyphen (-) then there will be no space between label value and the prefix. [Default is no prefix]. </p>
<p> Note: By placing <code>-Sq</code> options in the segment header you can change the quoted text attributes on a segment-by-segment basis.</p>
<dt><code>-Sr</code></p>
<dd> <code>r</code>ectangle. No size needs to be specified, but the x- and y-dimensions must be found in columns 4 and 5.</p>
<dt><code>-SR</code></p>
<dd> <code>R</code>ounded rectangle. No size needs to be specified, but the x- and y-dimensions and corner radius must be found in columns 4, 5, and 6.</p>
<dt><code>-Ss</code></p>
<dd> <code>s</code>quare. <i>size</i> is diameter of circumscribing circle.</p>
<dt><code>-St</code></p>
<dd> <code>t</code>riangle. <i>size</i> is diameter of circumscribing circle.</p>
<dt><code>-Su</code></p>
<dd> c<code>u</code>be (3-D). The <i>size)</i> sets length of all sides. Append <code>u</code> if <i>size</i> is in x-units [Default is plot-distance units]. The facet colors will be modified to simulate shading. Use <code>-SU</code> to disable such 3-D illumination.</p>
<dt><code>-Sv</code></p>
<dd> <code>v</code>ector. Direction (in degrees counter-clockwise from horizontal) and length must be found in columns 4 and 5. The <i>size</i> is the length of the vector head. Vector width is set by <code>-W</code>. See VECTOR ATTRIBUTES for specifying attributes.</p>
<dt><code>-SV</code></p>
<dd> Same as <code>-Sv</code>, except azimuth (in degrees east of north) should be given instead of direction. The azimuth will be mapped into an angle based on the chosen map projection (<code>-Sv</code> leaves the directions unchanged.) See VECTOR ATTRIBUTES for specifying attributes.</p>
<dt><code>-Sw</code></p>
<dd> pie <code>w</code>edge. Start and stop directions (in degrees counter-clockwise from horizontal) for pie slice must be found in columns 4 and 5.</p>
<dt><code>-SW</code></p>
<dd> Same as <code>-Sw</code>, except azimuths (in degrees east of north) should be given instead of the two directions. The azimuths will be mapped into angles based on the chosen map projection (<code>-Sw</code> leaves the directions unchanged.)</p>
<dt><code>-Sx</code></p>
<dd> cross (x). <i>size</i> is diameter of circumscribing circle.</p>
<dt><code>-Sy</code></p>
<dd> y-dash (|). <i>size</i> is the length of a short horizontal (y-dir) line segment.</p>
<dt><code>-S=</code></p>
<dd> geovector. Azimuth (in degrees east from north) and length (in km) must be found in columns 4 and 5. The <i>size</i> is the length of the vector head. Vector width is set by <code>-W</code>. See VECTOR ATTRIBUTES for specifying attributes.</p>
<dt><code>-S~</code></p>
<dd> decorated line, i.e., lines with symbols along them. Append [<code>d</code>|<code>D</code>|<code>f</code>|<code>l</code>|<code>L</code>|<code>n</code>|<code>N</code>|<code>s</code>|<code>S</code>|<code>x</code>|<code>X</code>]<i>info</i>[:<i>symbolinfo</i>]. The required argument controls the placement of symbols along the decorated lines. Choose among six controlling algorithms:</p>
<dt><code>d</code><i>dist</i>[<code>c</code>|<code>i</code>|<code>p</code>] or <code>D</code><i>dist</i>[<code>d</code>|<code>e</code>|<code>f</code>|<code>k</code>|<code>m</code>|<code>M</code>|<code>n</code>|<code>s</code>]</p>
<dd> For lower case <code>d</code>, give distances between symbols on the plot in your preferred measurement unit <code>c</code> (cm), <code>i</code> (inch), or <code>p</code> (points), while for upper case <code>D</code>, specify distances in map units and append the unit; choose among <code>e</code> (m), <code>f</code> (foot), <code>k</code> (km), <code>M</code> (mile), <code>n</code> (nautical mile) or <code>u</code> (US survey foot), and <code>d</code> (arc degree), <code>m</code> (arc minute), or <code>s</code> (arc second). [Default is 10<code>c</code> or 4<code>i</code>]. As an option, you can append /<i>fraction</i> which is used to place the very first symbol for each line when the cumulative along-line distance equals <i>fraction * dist</i> [0.25].</p>
<dt><code>f</code><i>ffile.d</i></p>
<dd> Reads the ASCII file <i>ffile.d</i> and places symbols at locations in the file that matches locations along the decorated lines. Inexact matches and points outside the region are skipped.</p>
<dt><code>l</code>|<code>L</code><i>line1</i>[,<i>line2</i>,&#8230;]</p>
<dd> Give the coordinates of the end points for one or more comma-separated straight line segments. Symbols will be placed where these lines intersect the decorated lines. The format of each <i>line</i> specification is <i>start_lon</i>/<i>start_lat</i>/<i>stop_lon</i>/<i>stop_lat</i>. Both <i>start_lon</i>/<i>start_lat</i> and <i>stop_lon</i>/<i>stop_lat</i> can be replaced by a 2-character key that uses the justification format employed in <code>pstext</code> to indicate a point on the frame or center of the map, given as [LCR][BMT]. <code>L</code> will interpret the point pairs as defining great circles [Default is straight line].</p>
<dt><code>n</code>|<code>N</code><i>n_symbol</i></p>
<dd> Specifies the number of equidistant symbols for decorated lines [1]. Upper case <code>N</code> starts placing symbols exactly at the start of the line [Default centers them along the line]. <code>N</code>-1 places one symbol at start, while <code>N</code>+1 places one symbol at the end of decorated lines. Optionally, append /<i>min_dist</i>[<code>c</code>|<code>i</code>|<code>p</code>] to enforce that a minimum distance separation between successive symbols is enforced.</p>
<dt><code>s</code>|<code>S</code><i>n_symbol</i></p>
<dd> Same as <code>n</code>|<code>N</code><i>n_symbol</i> but implies that the input data are first to be converted into a series of 2-point line segments before plotting.</p>
<dt><code>x</code>|<code>X</code><i>xfile.d</i></p>
<dd> Reads the multisegment file <i>xfile.d</i> and places symbols at the intersections between the decorated lines and the lines in <i>xfile.d</i>. <code>X</code> will resample the lines first along great-circle arcs. </p>
<p> The optional <i>symbolinfo</i> controls the specifics of the symbol selection and formatting and consists of a concatenated string made up of any of the following control arguments:</p>
<dt><code>+a</code><i>angle</i></p>
<dd> For symbols at a fixed angle, <code>+an</code> for line-normal, or <code>+ap</code> for line-parallel [Default].</p>
<dt><code>+d</code></p>
<dd> Turns on debug which will draw helper points and lines to illustrate the workings of the decorated line setup.</p>
<dt><code>+g</code>[<i>fill</i>]</p>
<dd> Sets the symbol fill [no fill].</p>
<dt><code>+n</code><i>dx</i>[/<i>dy</i>]</p>
<dd> Nudges the placement of symbols by the specified amount (append <code>c</code>|<code>i</code>|<code>p</code> to specify the units). Increments are considered in the coordinate system defined by the orientation of the line; use <code>+N</code> to force increments in the plot x/y coordinates system [no nudging].</p>
<dt><code>+p</code>[<i>pen</i>]</p>
<dd> Draws the outline of symbols [Default is no outline]; optionally specify pen for outline [Default is width = 0.25p, color = black, style = solid].</p>
<dt><code>+w</code></p>
<dd> Specifies how many (<i>x</i>,<i>y</i>) points will be used to estimate symbol angles [Default is 10]. </p>
<p> Note: By placing <code>-S~</code> options in the segment header you can change the decorated lines on a segment-by-segment basis.</p>
<dt><code>-T</code></p>
<dd> Ignore all input files, including standard input. This is the same as specifying /dev/null (or NUL for Windows users) as input file. Use this to activate only the options that are not related to plotting of lines or symbols, such as <code>psxyz</code> <code>-R</code> <code>-J</code> <code>-O</code> <code>-T</code> to terminate a sequence of GMT plotting commands without producing any plotting output.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<code>&#8211;</code>|<code>+</code>][<i>pen</i>] <i>(more &#8230;)</i></p>
<dd> Set pen attributes for lines or the outline of symbols [Defaults: width = default, color = black, style = solid]. A leading <code>+</code> will use the lookup color (via <code>-C</code>) for both symbol fill and outline pen color, while a leading <code>&#8211;</code> will set outline pen color and turn off symbol fill. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-a</code><i>col</i>=<i>name</i>[<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Set aspatial column associations <i>col</i>=<i>name</i>.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is the required number of columns given the chosen settings].</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-g</code>[<code>a</code>]<code>x</code>|<code>y</code>|<code>d</code>|<code>X</code>|<code>Y</code>|<code>D</code>|[<i>col</i>]<code>z</code>[+|-]<i>gap</i>[<code>u</code>] <i>(more &#8230;)</i></p>
<dd> Determine data gaps and line breaks. The <code>-g</code> option is ignored if <code>-S</code> is set.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>] <i>(more &#8230;)</i></p>
<dd> Select perspective view.</p>
<dt><code>-t</code>[<i>transp</i>] <i>(more &#8230;)</i></p>
<dd> Set PDF transparency level in percent.</p>
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
<p> To plot blue columns (width = 1.25 cm) at the positions listed in the file heights.xyz on a 3-D projection of the space (0-10), (0-10), (0-100), with tickmarks every 2, 2, and 10, viewing it from the southeast at 30 degree elevation, use: </p>
<pre>
gmt psxyz heights.xyz -R0/10/0/10/0/100 -Jx1.25c -Jz0.125c -So1.25c \
          -Gblue -Bx2+lXLABEL -By2+lYLABEL -Bz10+lZLABEL -B+t&quot;3-D PLOT&quot; -p135/30 \
          -Uc -W -P &gt; heights.ps
</pre>
<h2>SEGMENT HEADER PARSING</h2>
<p> Segment header records may contain one of more of the following options:</p>
<dl>
<dt><code>-G</code><i>fill</i></p>
<dd> Use the new <i>fill</i> and turn filling on</p>
<dt><code>-G-</code></p>
<dd> Turn filling off</p>
<dt><code>-G</code></p>
<dd> Revert to default fill (none if not set on command line)</p>
<dt><code>-W</code><i>pen</i></p>
<dd> Use the new <i>pen</i> and turn outline on</p>
<dt><code>-W</code></p>
<dd> Revert to default pen <i>MAP_DEFAULT_PEN</i> (if not set on command line)</p>
<dt><code>-W-</code></p>
<dd> Turn outline off</p>
<dt><code>-Z</code><i>zval</i></p>
<dd> Obtain fill via cpt lookup using z-value <i>zval</i></p>
<dt><code>-Z</code><i>NaN</i></p>
<dd> Get the NaN color from the CPT file</dl>
<h2>CUSTOM SYMBOLS</h2>
<p> <code>psxyz</code> allows users to define and plot their own custom symbols. This is done by encoding the symbol using our custom symbol macro code described in Appendix N. Put all the macro codes for your new symbol in a file whose extension must be .def; you may then address the symbol without giving the extension (e.g., the symbol file tsunami.def is used by specifying <code>-Sk</code><i>tsunami/size</i>. The definition file can contain any number of plot code records, as well as blank lines and comment lines (starting with #). <code>psxyz</code> will look for the definition files in (1) the current directory, (2) the ~/.gmt directory, and (3) the <code>$GMT_SHAREDIR</code>/custom directory, in that order. Freeform polygons (made up of straight line segments and arcs of circles) can be designed &#8211; these polygons can be painted and filled with a pattern. Other standard geometric symbols can also be used. See Appendix <i>App-custom_symbols</i> for macro definitions.</p>
<h2>BUGS</h2>
<p> No hidden line removal is employed for polygons and lines. Symbols, however, are first sorted according to their distance from the viewpoint so that nearby symbols will overprint more distant ones should they project to the same x,y position. </p>
<p> <code>psxyz</code> cannot handle filling of polygons that contain the south or north pole. For such a polygon, make a copy and split it into two and make each explicitly contain the polar point. The two polygons will combine to give the desired effect when filled; to draw outline use the original polygon.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtcolors</code>, <code>psbasemap</code>, <code>psxy</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
