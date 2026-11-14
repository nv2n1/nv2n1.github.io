---
title: "psscale(1)"
name: "psscale"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psscale/"
description: "psscale – Plot a gray or color scale-bar on maps"
---

<h2>NAME</h2>
<p> psscale &#8211; Plot a gray or color scale-bar on maps</p>
<h2>SYNOPSIS</h2>
<p> <code>psscale</code> <i>refpoint</i> [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ <i>cpt</i> ] [ <i>box</i> ] [ <i>zlo</i>/<i>zhi</i> ] [ [<i>max_intens</i>|<i>low_i</i>/<i>high_i</i>] ] [ <i>parameters</i> ] [ <code>z</code>|<code>Z</code><i>parameters</i> ] [ ] [ [<code>i</code>][<i>gap</i>] ] [ ] [ [<code>p</code>|<i>dpi</i> ]] [ ] [ ] [ ] [ <i>region</i> ] [ ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <i>zfile</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>psscale</code> plots gray scales or color scales on maps. Both horizontal and vertical scales are supported. For CPT files with gradational colors (i.e., the lower and upper boundary of an interval have different colors) <code>psscale</code> will interpolate to give a continuous scale. Variations in intensity due to shading/illumination may be displayed by setting the option <code>-I</code>. Colors may be spaced according to a linear scale, all be equal size, or by providing a file with individual tile widths. The font used for the annotations along the scale and optional units is specified by <i>FONT_ANNOT_PRIMARY</i>. If a label is requested, it is plotted with <i>FONT_LABEL</i>.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-D</code>[<code>g</code>|<code>j</code>|<code>J</code>|<code>n</code>|<code>x</code>]<i>refpoint</i><code>+w</code><i>length</i>/<i>width</i>[<code>+e</code>[<code>b</code>|<code>f</code>][<i>length</i>]][<code>+h</code>][<code>+j</code><i>justify</i>][<code>+m</code>[<code>a</code>|<code>c</code>|<code>l</code>|<code>u</code>]][<code>+n</code>[<i>txt</i>]][<code>+o</code><i>dx</i>[/<i>dy</i>]]</p>
<dd> Defines the reference point on the map for the color scale using one of four coordinate systems: (1) Use <code>-Dg</code> for map (user) coordinates, (2) use <code>-Dj</code> or <code>-DJ</code> for setting <i>refpoint</i> via a 2-char justification code that refers to the (invisible) map domain rectangle, (3) use <code>-Dn</code> for normalized (0-1) coordinates, or (4) use <code>-Dx</code> for plot coordinates (inches, cm, etc.). All but <code>-Dx</code> requires both <code>-R</code> and <code>-J</code> to be specified. Append <code>+w</code> followed by the <i>length</i> and <i>width</i> of the color bar. Give a negative <i>length</i> to reverse the scale bar. Append <code>+h</code> to get a horizontal scale [Default is vertical]. By default, the anchor point on the scale is assumed to be the bottom left corner (BL), but this can be changed by appending <code>+j</code> followed by a 2-char justification code <i>justify</i> (see <code>pstext</code>). Note: If <code>-Dj</code> is used then <i>justify</i> defaults to the same as <i>refpoint</i>, if <code>-DJ</code> is used then <i>justify</i> defaults to the mirror opposite of <i>refpoint</i>. Finally, add <code>+o</code> to offset the color scale by <i>dx</i>/<i>dy</i> away from the <i>refpoint</i> point in the direction implied by <i>justify</i> (or the direction implied by <code>-Dj</code> or <code>-DJ</code>). Add sidebar triangles for back- and/or foreground colors with <code>+e</code>. Append <code>f</code> (foreground) or <code>b</code> (background) for only one sidebar triangle [Default gives both]. Optionally, append triangle height [Default is half the barwidth]. Move text to opposite side with <code>+m</code>[<code>a</code>|<code>c</code>|<code>l</code>|<code>u</code>]. Horizontal scale bars: Move annotations and labels above the scale bar [Default is below]; the unit remains on the left. Vertical scale bars: Move annotations and labels to the left of the scale bar [Default is to the right]; the unit remains below. Append one or more of <code>a</code>, <code>l</code> or <code>u</code> to control which of the annotations, label, and unit that will be moved to the opposite side. Append <code>c</code> if you want to print a vertical label as a column of characters (does not work with special characters). Append <code>+n</code> to plot a rectangle with the NaN color at the start of the bar, append <i>text</i> to change label from NaN.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i></p>
<dd> Set annotation, tick, and gridline interval for the colorbar. The x-axis label will plot beneath a horizontal bar (or vertically to the right of a vertical bar), except when using <code>-A</code>. As an option, use the y-axis label to plot the data unit to the right of a horizontal bar (and above a vertical bar). When using <code>-Ba</code> or <code>-Baf</code> annotation and/or minor tick intervals are chosen automatically. If <code>-B</code> is omitted, or no annotation intervals are provided, the default is to annotate every color level based on the numerical entries in the CPT file (which may be overridden by ULB flags in the CPT file). To specify custom text annotations for intervals, you must append ;<i>annotation</i> to each z-slice in the CPT file.</p>
<dt><code>-C</code><i>cpt</i></p>
<dd> <i>cpt</i> is the CPT file to be used. By default all color changes are annotated. To use a subset, add an extra column to the CPT file with a L, U, or B to annotate Lower, Upper, or Both color segment boundaries (but see <code>-B</code>). If not given, <code>psscale</code> will read stdin. Like <code>grdview</code>, <code>psscale</code> can understand pattern specifications in the CPT file. For CPT files where the <i>z</i> range is in meters, it may be useful to change to another unit when plotting. To do so, append <code>+U</code><i>unit</i> to the file name. Likewise, if the CPT file uses another unit than meter and you wish to plot the CPT versus meters, append <code>+u</code><i>unit</i>.</p>
<dt><code>-F</code>[<code>+c</code><i>clearances</i>][<code>+g</code><i>fill</i>][<code>+i</code>[[<i>gap</i>/]<i>pen</i>]][<code>+p</code>[<i>pen</i>]][<code>+r</code>[<i>radius</i>]][<code>+s</code>[[<i>dx</i>/<i>dy</i>/][<i>shade</i>]]]</p>
<dd> Without further options, draws a rectangular border around the scale using <code>MAP_FRAME_PEN</code>; specify a different pen with <code>+p</code><i>pen</i>. Add <code>+g</code><i>fill</i> to fill the scale box [no fill]. Append <code>+c</code><i>clearance</i> where <i>clearance</i> is either <i>gap</i>, <i>xgap</i>/<i>ygap</i>, or <i>lgap</i>/<i>rgap</i>/<i>bgap</i>/<i>tgap</i> where these items are uniform, separate in x- and y-direction, or individual side spacings between scale and border. Append <code>+i</code> to draw a secondary, inner border as well. We use a uniform <i>gap</i> between borders of 2<code>p</code> and the <code>MAP_DEFAULTS_PEN</code> unless other values are specified. Append <code>+r</code> to draw rounded rectangular borders instead, with a 6<code>p</code> corner radius. You can override this radius by appending another value. Finally, append <code>+s</code> to draw an offset background shaded region. Here, <i>dx</i>/<i>dy</i> indicates the shift relative to the foreground frame [4<code>p</code>/-4<code>p</code>] and <i>shade</i> sets the fill style to use for shading [gray50].</p>
<dt><code>-G</code><i>zlo</i>/<i>zhi</i></p>
<dd> Truncate the incoming CPT so that the lowest and highest z-levels are to <i>zlo</i> and <i>zhi</i>. If one of these equal NaN then we leave that end of the CPT alone. The truncation takes place before the plotting.</p>
<dt><code>-I</code>[<i>max_intens</i>|<i>low_i</i>/<i>high_i</i>]</p>
<dd> Add illumination effects. Optionally, set the range of intensities from &#8211; to + <i>max_intens</i>. If not specified, 1 is used. Alternatively, append <i>low/high</i> intensities to specify an asymmetric range [Default is no illumination].</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code>[<code>i</code>][<i>gap</i>]</p>
<dd> Gives equal-sized color rectangles. Default scales rectangles according to the z-range in the CPT file (Also see <code>-Z</code>). If set, any equal interval annotation set with <code>-B</code> will be ignored. If <i>gap</i> is appended and the CPT file is discrete we will center each annotation on each rectangle, using the lower boundary z-value for the annotation. If <code>i</code> is prepended we annotate the interval range instead. If <code>-I</code> is used then each rectangle will have its constant color modified by the specified intensity.</p>
<dt><code>-M</code></p>
<dd> Force a monochrome graybar using the (television) YIQ transformation.</p>
<dt><code>-N</code>[<code>p</code>|<i>dpi</i>]</p>
<dd> Controls how the color scale is represented by the PostScript language. To preferentially draw color rectangles (e.g., for discrete colors), append <code>p</code>. Otherwise we will preferentially draw images (e.g., for continuous colors). Optionally append effective dots-per-inch for rasterization of color scales [600].</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code></p>
<dd> Select logarithmic scale and power of ten annotations. All z-values in the CPT file will be converted to p = log10(z) and only integer p values will be annotated using the 10^p format [Default is linear scale].</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i></p>
<dt><code>-S</code></p>
<dd> Do not separate different color intervals with black grid lines.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-Z</code><i>zfile</i></p>
<dd> File with colorbar-width per color entry. By default, width of entry is scaled to color range, i.e., z = 0-100 gives twice the width as z = 100-150 (Also see <code>-L</code>).</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>] <i>(more &#8230;)</i></p>
<dd> Select perspective view. (Required <code>-R</code> and <code>-J</code> for proper functioning).</p>
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
<h2>EXAMPLES</h2>
<p> To plot a a horizontal color scale (12 cm long; 0.5 cm wide) at the reference point (8,1) (paper coordinates) with justification at top center and automatic annotation interval, do </p>
<pre>
gmt makecpt -T-200/1000/100 -Crainbow &gt; t.cpt
gmt psscale -Ct.cpt -Dx8c/1c+w12c/0.5c+jTC+h -Bxaf+l&quot;topography&quot; -By+lkm &gt; map.ps
</pre>
<p> To append a vertical color scale (7.5 cm long; 1.25 cm wide) to the right of a plot that is 6 inch wide and 4 inch high, using illumination, and show back- and foreground colors, and annotating every 5 units, we provide the reference point and select the left-mid anchor point via </p>
<pre>
gmt psscale -Dx6.5i+jLM/2i+w7.5c/1.25c+e -O -Ccolors.cpt -I -Bx5+lBATHYMETRY -By+lm &gt;&gt; map.ps
</pre>
<p> To overlay a horizontal color scale (4 inches long; 1 cm wide) above a Mercator map produced by a previous call, ensuring a 2 cm offset from the map frame, use </p>
<pre>
gmt psscale -DjCT+w4i/1c+o0/2c+h -O -Ccolors.cpt -Baf -R -J &gt;&gt; map.ps
</pre>
<h2>NOTES</h2>
<p> When the CPT file is discrete and no illumination is specified, the color bar will be painted using polygons. For all other cases we must paint with an image. Some color printers may give slightly different colors for the two methods given identical RGB values.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>makecpt</code> <code>gmtlogo</code>, <code>grd2cpt</code> <code>psimage</code>, <code>pslegend</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
