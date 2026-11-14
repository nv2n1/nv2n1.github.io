---
title: "pslegend(1)"
name: "pslegend"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pslegend/"
description: "pslegend – Plot legends on maps"
---

<h2>NAME</h2>
<p> pslegend &#8211; Plot legends on maps</p>
<h2>SYNOPSIS</h2>
<p> <code>pslegend</code> [ <i>specfile</i> ] <i>refpoint</i> ] [ <i>dx</i>/<i>dy</i> ] [ <i>box</i> ] [ <i>parameters</i> ] [ ] [ ] [ ] [ <i>region</i> ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>pslegend</code> will make legends that can be overlaid on maps. It reads specific legend-related information from an input file [or stdin]. Unless otherwise noted, annotations will be made using the primary annotation font and size in effect (i.e., FONT_ANNOT_PRIMARY)</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-D</code>[<code>g</code>|<code>j</code>|<code>J</code>|<code>n</code>|<code>x</code>]<i>refpoint</i><code>+w</code><i>width</i>[/<i>height</i>][<code>+j</code><i>justify</i>][<code>+l</code><i>spacing</i>][<code>+o</code><i>dx</i>[/<i>dy</i>]]</p>
<dd> Defines the reference point on the map for the legend using one of four coordinate systems: (1) Use <code>-Dg</code> for map (user) coordinates, (2) use <code>-Dj</code> or <code>-DJ</code> for setting <i>refpoint</i> via a 2-char justification code that refers to the (invisible) map domain rectangle, (3) use <code>-Dn</code> for normalized (0-1) coordinates, or (4) use <code>-Dx</code> for plot coordinates (inches, cm, etc.). All but <code>-Dx</code> requires both <code>-R</code> and <code>-J</code> to be specified. Append <code>+w</code><i>width</i>[/<i>height</i>] to set the width (and height) of the legend box in plot coordinates (inches, cm, etc.). If <i>height</i> is zero or not given then we estimate <i>height</i> based the expected vertical extent of the items to be placed. By default, the anchor point on the legend is assumed to be the bottom left corner (BL), but this can be changed by appending <code>+j</code> followed by a 2-char justification code <i>justify</i> (see <code>pstext</code>). Note: If <code>-Dj</code> is used then <i>justify</i> defaults to the same as <i>refpoint</i>, if <code>-DJ</code> is used then <i>justify</i> defaults to the mirror opposite of <i>refpoint</i>. Use <code>+l</code><i>spacing</i> to change the line-spacing factor in units of the current font size [1.1]. Finally, add <code>+o</code> to offset the color scale by <i>dx</i>/<i>dy</i> away from the <i>refpoint</i> point in the direction implied by <i>justify</i> (or the direction implied by <code>-Dj</code> or <code>-DJ</code>).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code><i>dx</i>/<i>dy</i></p>
<dd> Sets the clearance between the legend frame and the internal items [4<code>p</code>/4<code>p</code>].</p>
<dt><code>-F</code>[<code>+c</code><i>clearances</i>][<code>+g</code><i>fill</i>][<code>+i</code>[[<i>gap</i>/]<i>pen</i>]][<code>+p</code>[<i>pen</i>]][<code>+r</code>[<i>radius</i>]][<code>+s</code>[[<i>dx</i>/<i>dy</i>/][<i>shade</i>]]]</p>
<dd> Without further options, draws a rectangular border around the legend using <code>MAP_FRAME_PEN</code>; specify a different pen with <code>+p</code><i>pen</i>. Add <code>+g</code><i>fill</i> to fill the legend box [no fill]. Append <code>+c</code><i>clearance</i> where <i>clearance</i> is either <i>gap</i>, <i>xgap</i>/<i>ygap</i>, or <i>lgap</i>/<i>rgap</i>/<i>bgap</i>/<i>tgap</i> where these items are uniform, separate in x- and y-direction, or individual side spacings between scale and border. Append <code>+i</code> to draw a secondary, inner border as well. We use a uniform <i>gap</i> between borders of 2<code>p</code> and the <code>MAP_DEFAULTS_PEN</code> unless other values are specified. Append <code>+r</code> to draw rounded rectangular borders instead, with a 6<code>p</code> corner radius. You can override this radius by appending another value. Finally, append <code>+s</code> to draw an offset background shaded region. Here, <i>dx</i>/<i>dy</i> indicates the shift relative to the foreground frame [4<code>p</code>/-4<code>p</code>] and <i>shade</i> sets the fill style to use for shading [gray50].</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
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
<h2>PSLEGEND CODES</h2>
<dl>
<dt><i>specfile</i></p>
<dd> This ASCII file contains instructions for the layout of items in the legend. Each legend item is described by a unique record. All records begin with a unique character that is common to all records of the same kind. The order of the legend items is implied by the order of the records. Fourteen different record types are recognized, and the syntax for each of these records are presented below:</p>
<dt><code>#</code> <i>comment</i></p>
<dd> Records starting with # and blank lines are skipped.</p>
<dt><code>A</code> <i>cptname</i></p>
<dd> Symbol or cell color fills may be given indirectly via a <i>z</i>-value which can be used for the color look-up via the given CPT file <i>cptname</i>. You may switch to other <i>cptname</i> by repeating this command.</p>
<dt><code>B</code> <i>cptname offset height</i> [ <i>optional arguments</i> ]</p>
<dd> The <code>B</code> record will plot a horizontal color bar, <code>psscale</code>-style in the middle, starting at <i>offset</i> from the left edge, and of the given <i>height</i>. You may add any additional <code>psscale</code> options as well. Any of the modifiers [+e[b|f][&lt;length&gt;]][+h][+ma|c|l|u][+n[&lt;txt&gt;]] may be appended to the <i>height</i> argument, while other module options <code>-B</code> <code>-I</code> <code>-L</code> <code>-M</code> <code>-N</code> <code>-S</code> <code>-Z</code> and <code>-p</code> may be appended as <i>optional arguments</i> at the end of the record. See <code>psscale</code> for details on all modifiers and options.</p>
<dt><code>C</code> <i>textcolor</i></p>
<dd> The <code>C</code> record specifies the color with which the remaining text is to be printed. <i>textcolor</i> can be in the form <i>r/g/b</i>, <i>c/m/y/k</i>, a named color, or an indirect color via z=*value* (requires the <code>A</code> command). Use <code>&#8211;</code> to reset to default color.</p>
<dt><code>D</code> [<i>offset</i>] <i>pen</i> [<code>&#8211;</code>|<code>+</code>|<code>=</code>]</p>
<dd> The <code>D</code> record results in a horizontal line with specified <i>pen</i> across the legend with one quarter of the line-spacing left blank above and below the line. Two gaps of <i>offset</i> units are left blank between the horizontal line and the left and right frame sides [0]. If no pen is given we use MAP_GRID_PEN_PRIMARY, and if <i>pen</i> is set to <code>&#8211;</code> then no visible line is drawn (we just remember the location as a possible start/stop point for a vertical line; see <code>V</code>). To <i>not</i> add the quarter line-spacing before the line, add <code>&#8211;</code>. To <i>not</i> add the spacing after the line, add <code>+</code>. For no spacing at all, add <code>=</code> [Default places a quarter line-spacing both before and after the line].</p>
<dt><code>F</code> <i>fill1 fill2 &#8230; filln</i></p>
<dd> Specify fill (color of pattern) for cells. Alternatively, you can specify an indirect color via z=*value* (requires the <code>A</code> command). If only <i>fill1</i> is given then it is used to fill the entire row, otherwise give one fill value for each active column (see <code>N</code>). If any fill is &#8211; then no fill takes place [Default].</p>
<dt><code>G</code> <i>gap</i></p>
<dd> The <code>G</code> record specifies a vertical gap of the given length. In addition to the standard units (<code>i</code>, <code>c</code>, <code>p</code>) you may use <code>l</code> for lines. A negative <i>gap</i> will move the current line upwards (thus closing a gap).</p>
<dt><code>H</code> <i>fontsize</i>|<code>&#8211;</code> <i>font</i>|<code>&#8211;</code> <i>header</i></p>
<dd> The <code>H</code> record plots a centered text string using the specified font parameters. Use <code>&#8211;</code> to default to size and type of <code>FONT_TITLE</code>.</p>
<dt><code>I</code> <i>imagefile width justification</i></p>
<dd> Place an EPS or raster image in the legend justified relative to the current point. The image <i>width</i> determines the size of the image on the page.</p>
<dt><code>L</code> <i>fontsize</i>|<code>&#8211;</code> <i>font</i>|<code>&#8211;</code> <i>justification label</i></p>
<dd> The <code>L</code> record plots a (L)eft, (C)entered, or (R)ight-justified text string within a column using the specified font parameters. Use <code>&#8211;</code> to default to the size and type of <code>FONT_LABEL</code>.</p>
<dt><code>M</code> <i>slon</i>|<code>&#8211;</code> <i>slat length</i> [<code>+f</code>][<code>+l</code>[<i>label</i>]][<code>+u</code>] [<code>-F</code><i>param</i>] [ <code>-R</code><i>w/e/s/n</i> <code>-J</code><i>param</i> ]</p>
<dd> Place a map scale in the legend. Specify <i>slon slat</i>, the point on the map where the scale applies (<i>slon</i> is only meaningful for certain oblique projections. If not needed, you must specify <code>&#8211;</code> instead). Give <i>length</i>, the length of the scale in km (for other units append <code>e</code> (meter), <code>f</code> (foot), <code>M</code> (mile), <code>n</code> (nautical mile), or <code>u</code> (survey foot)). Append <code>+f</code> for a fancy map scale [Default is plain]. Append <code>+l</code> to the <i>length</i> to select the default label which equals the distance unit (meter, feet, km, miles, nautical miles, survey feet) and is justified on top of the scale [t]. Change this by giving your own label (append <code>+l</code><i>label</i>). Change label alignment with <code>+a</code><i>align</i> (choose among <code>l</code>(eft), <code>r</code>(ight), <code>t</code>(op) , and <code>b</code>(ottom)). Apply <code>+u</code> to append the unit to all distance annotations along the scale. If you want to place a map panel behind the scale, add a suitable <code>-F</code> panel option (see <code>psbasemap</code> for details on panels as well as map scale modifiers). All <code>+</code><i>modifiers</i> must be appended to <i>length</i> to make a single string argument. If the <code>-R</code> <code>-J</code> supplied to <code>pslegend</code> is different than the projection needed for the scale (or not given at all, e.g., with <code>-Dx</code>), supply the two optional <code>-R</code> <code>-J</code> settings as well.</p>
<dt><code>N</code> [<i>ncolumns</i> or <i>relwidth1 relwidth2 &#8230; relwidthn</i>]</p>
<dd> Change the number of columns in the legend [1]. This only affects the printing of symbols (<code>S</code>) and labels (<code>L</code>). The number of columns stay in effect until <code>N</code> is used again. To get columns of unequal width, instead provide the relative width of each column separated by whitespace. The sum of these widths are equated to the legend width set via <code>-D</code>. If no argument is given the we set <i>n_columns</i> to 1.</p>
<dt><code>P</code> <i>paragraph-mode-header-for-pstext</i></p>
<dd> Start a new text paragraph by specifying all the parameters needed (see <code>pstext -M</code> record description). Note that <code>pslegend</code> knows what all those values should be, so normally you can leave the entire record (after P) blank or leave it out all together. If you need to set at least one of the parameters directly, you must specify all and set the ones you want to leave at their default value to <code>&#8211;</code>.</p>
<dt><code>S</code> [<i>dx1 symbol size fill pen</i> [ <i>dx2 text</i> ]]</p>
<dd> Plots the selected symbol with specified diameter, fill, and outline (see <code>psxy</code>). The symbol is centered at <i>dx1</i> from the left margin of the column, with the optional explanatory <i>text</i> starting <i>dx2</i> from the margin, printed with <code>FONT_ANNOT_PRIMARY</code>. Use <code>&#8211;</code> if no <i>fill</i> or outline (<i>pen</i>) is required. Alternatively, the <i>fill</i> may be specified indirectly via z=*value* and the color is assigned vi the CPT look-up (requires the <code>A</code> command). When plotting just a symbol, without text, <i>dx2</i> and <i>text</i> can be omitted. The <i>dx1</i> value can also be given as a justification code L, C, R which justifies the symbol with respect to the current column. If no arguments are given to <code>S</code> then we simply skip to the next column. Three <code>psxy</code> symbols may take special modifiers: front (<code>f</code>), quoted line (<code>q</code>) and vector (<code>v</code>). You can append modifiers to the symbol and affect how the fronts, quoted lines and vectors are presented (see <code>psxy</code> man page for modifiers). <code>pslegend</code> will determine default settings for all modifiers and secondary arguments if not provided. A few other symbols (the rectangles, ellipse, wedge, mathangle) may take more than a single argument size. Note that for a line segment you should use the horizontal dash symbol (<code>&#8211;</code>). If just a single size if given then <code>pslegend</code> will provide reasonable arguments to plot the symbol (See <i>Defaults</i>). Alternatively, combine the required arguments into a single, comma-separated string and use that as the symbol size (again, see <code>psxy</code> for details on the arguments needed).</p>
<dt><code>T</code> <i>paragraph-text</i></p>
<dd> One or more of these <code>T</code> records with <i>paragraph-text</i> printed with <code>FONT_ANNOT_PRIMARY</code>. To specify special positioning and typesetting arrangements, or to enter a paragraph break, use the optional <code>P</code> record.</p>
<dt><code>V</code> [<i>offset</i>] <i>pen</i></p>
<dd> The <code>V</code> record draws a vertical line between columns (if more than one) using the selected <i>pen</i>. Here, <i>offset</i> is analogous to the offset for the <code>D</code> records but in the vertical direction [0]. The first time <code>V</code> is used we remember the vertical position of the last <code>D</code> line, and the second time <code>V</code> is set we draw from that past location to the most recent location of the <code>D</code> line. Thus, <code>D</code> must be used to mark the start and stop of a vertical line (so <code>V</code> must follow <code>D</code>). If no horizontal line is desired simply give &#8211; as <i>pen</i> to <code>D</code>.</dl>
<h2>DEFAULTS</h2>
<p> When attributes are not provided, or extended symbol information (for symbols taking more than just an overall size) are not given as comma-separated quantities, <code>pslegend</code> will provide the following defaults: </p>
<p> Front: Front symbol is left-side (here, that means upper side) box, with dimensions 30% of the given symbol size. </p>
<p> Vector: Head size is 30% of given symbol size. </p>
<p> Ellipse: Minor axis is 65% of major axis (the symbol size), with an azimuth of 0 degrees. </p>
<p> Rectangle: Height is 65% of width (the symbol size). </p>
<p> Rotated rectangle: Same, with a rotation of 30 degrees. </p>
<p> Rounded rectangle: Same as rectangle, but with corner radius of 10% of width. </p>
<p> Mathangle: Angles are -10 and 45 degrees, with arrow head size 30% of symbol size. </p>
<p> Wedge: Angles are -30 and 30 degrees.</p>
<h2>EXAMPLES</h2>
<p> To add an example of a legend to a Mercator plot (map.ps) with the given specifications, use </p>
<pre>
gmt pslegend -R-10/10/-10/10 -JM6i -F+gazure1 -Dx0.5i/0.5i+w5i/3.3i+jBL+l1.2 \
-C0.1i/0.1i -B5f1 &lt;&lt; EOF &gt;&gt; map.ps
# Legend test for pslegend
# G is vertical gap, V is vertical line, N sets # of columns, D draws horizontal line.
# H is header, L is label, S is symbol, T is paragraph text, M is map scale.
#
G -0.1i
H 24 Times-Roman My Map Legend
D 0.2i 1p
N 2
V 0 1p
S 0.1i c 0.15i p300/12 0.25p 0.3i This circle is hachured
S 0.1i e 0.15i yellow 0.25p 0.3i This ellipse is yellow
S 0.1i w 0.15i green 0.25p 0.3i This wedge is green
S 0.1i f0.1i+l+t 0.25i blue 0.25p 0.3i This is a fault
S 0.1i - 0.15i - 0.25p,- 0.3i A dashed contour
S 0.1i v0.1i+a40+e 0.25i magenta 0.25p 0.3i This is a vector
S 0.1i i 0.15i cyan 0.25p 0.3i This triangle is boring
V 0 1p
D 0.2i 1p
N 1
M 5 5 600+u f
G 0.05i
I SOEST_logo.ras 3i CT
G 0.05i
B colors.cpt 0.2i 0.2i
G 0.05i L 9 4 R Smith et al., @%5%J. Geophys. Res., 99@%%, 2000
G 0.1i
P
T Let us just try some simple text that can go on a few lines.
T There is no easy way to predetermine how many lines will be required,
T so we may have to adjust the box height to get the right size box.
EOF
</pre>
<h2>NOTE ON LEGEND HEIGHT</h2>
<p> As <code>-D</code> suggests, leaving the <i>height</i> off forces a calculation of the expected height. This is an exact calculation except in the case of legends that place paragraph text. Here we simply do a first-order estimate of how many typeset lines might appear. Without access to font metrics this estimate will occasionally be off by 1 line. If so, note the reported height (with <code>-V</code>) and specify a slightly larger or smaller height in <code>-D</code>.</p>
<h2>WINDOWS REMARKS</h2>
<p> Note that under Windows, the percent sign (%) is a variable indicator (like $ under Unix). To indicate a plain percentage sign in a batch script you need to repeat it (%%); hence the font switching mechanism (@%*font*% and @%%) may require twice the number of percent signs. This only applies to text inside a script or that otherwise is processed by DOS. Data files that are opened and read by <code>pslegend</code> do not need such duplication.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtcolors</code>, <code>gmtlogo</code> <code>psbasemap</code>, <code>pstext</code>, <code>psxy</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
