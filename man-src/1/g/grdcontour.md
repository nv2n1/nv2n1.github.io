---
title: "grdcontour(1)"
name: "grdcontour"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdcontour/"
description: "grdcontour – Make contour map using a grid"
---

<h2>NAME</h2>
<p> grdcontour &#8211; Make contour map using a grid</p>
<h2>SYNOPSIS</h2>
<p> <code>grdcontour</code> <i>grid</i> [+]<i>cont_int</i>|<i>cpt</i> <i>parameters</i> [ [<code>&#8211;</code>|[+]<i>annot_int</i>][<i>labelinfo</i>] ] [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ <i>&lt;template&gt;</i> ] [ [<code>l</code>|<code>r</code>] ] [ [<code>d</code>|<code>f</code>|<code>n</code>|<code>l</code>|<code>L</code>|<code>x</code>|<code>X</code>]<i>params</i> ] [ <code>z</code>|<code>Z</code><i>parameters</i> ] [ ] [ <i>low/high</i> ] [ ] [ ] [ <i>cut</i> ] [ <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] ] [ <i>smoothfactor</i> ] [ [<code>+|-</code>][<code>+d</code><i>gap</i>[/<i>length</i>]][<code>+l</code>[<i>labels</i>]] ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ [<code>+</code>][<i>type</i>]<i>pen</i> ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ [<i>factor</i>[/<i>shift</i>]][<code>p</code>] ] [ <code>-bo</code><i>&lt;binary&gt;</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-do</code><i>&lt;nodata&gt;</i> ] [ <code>-ho</code>[<i>n</i>] ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdcontour</code> reads a 2-D grid file and produces a contour map by tracing each contour through the grid. PostScript code is generated and sent to standard output. Various options that affect the plotting are available. Alternatively, the x/y/z positions of the contour lines may be saved to one or more output files (or stdout) and no plot is produced.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>grid</i></p>
<dd> 2-D gridded data set to be contoured. (See GRID FILE FORMATS below).</p>
<dt><code>-C</code>[+]<i>cont_int</i></p>
<dd> The contours to be drawn may be specified in one of three possible ways:</p>
<dt>1.</p>
<dd> If <i>cont_int</i> has the suffix &quot;.cpt&quot; and can be opened as a file, it is assumed to be a CPT file. The color boundaries are then used as contour levels. If the CPT file has annotation flags in the last column then those contours will be annotated. By default all contours are labeled; use <code>-A-</code> to disable all annotations.</p>
<dt>2.</p>
<dd> If <i>cont_int</i> is a file but not a CPT file, it is expected to contain contour levels in column 1 and a C(ontour) OR A(nnotate) in col 2. The levels marked C (or c) are contoured, the levels marked A (or a) are contoured and annotated. Optionally, a third column may be present and contain the fixed annotation angle for this contour level.</p>
<dt>3.</p>
<dd> If no file is found, then <i>cont_int</i> is interpreted as a constant contour interval. However, if prepended with the + sign the <i>cont_int</i> is taken as meaning draw that single contour. The <code>-A</code> option offers the same possibility so they may be used together to plot a single annotated contour and another single non-annotated contour, as in &#8216;&#8230; -A+10 -C+5&#8217; that plots an annotated 10 contour and an non-annotated 5 contour. If <code>-A</code> is set and <code>-C</code> is not, then the contour interval is set equal to the specified annotation interval. </p>
<p> If a file is given and <code>-T</code> is set, then only contours marked with upper case C or A will have tick-marks. In all cases the contour values have the same units as the grid.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<code>&#8211;</code>|[+]<i>annot_int</i>][<i>labelinfo</i>]</p>
<dd> <i>annot_int</i> is annotation interval in data units; it is ignored if contour levels are given in a file. [Default is no annotations]. Append <code>&#8211;</code> to disable all annotations implied by <code>-C</code>. Alternatively prepend + to the annotation interval to plot that as a single contour. The optional <i>labelinfo</i> controls the specifics of the label formatting and consists of a concatenated string made up of any of the following control arguments:</p>
<dt><code>+a</code><i>angle</i></p>
<dd> For annotations at a fixed angle, <code>+an</code> for contour-normal, or <code>+ap</code> for contour-parallel [Default]. For <code>+ap</code>, you may optionally append <code>u</code> for up-hill and <code>d</code> for down-hill cartographic annotations.</p>
<dt><code>+c</code><i>dx</i>[/<i>dy</i>]</p>
<dd> Sets the clearance between label and optional text box. Append <code>c</code>|<code>i</code>|<code>p</code> to specify the unit or % to indicate a percentage of the label font size [15%].</p>
<dt><code>+d</code></p>
<dd> Turns on debug which will draw helper points and lines to illustrate the workings of the contour line setup.</p>
<dt><code>+e</code></p>
<dd> Delay the plotting of the text. This is used to build a clip path based on the text, then lay down other overlays while that clip path is in effect, then turning of clipping with psclip <code>-Cs</code> which finally plots the original text.</p>
<dt><code>+f</code><i>font</i></p>
<dd> Sets the desired font [Default <code>FONT_ANNOT_PRIMARY</code> with its size changed to 9p].</p>
<dt><code>+g</code>[<i>color</i>]</p>
<dd> Selects opaque text boxes [Default is transparent]; optionally specify the color [Default is <code>PS_PAGE_COLOR</code>].</p>
<dt><code>+j</code><i>just</i></p>
<dd> Sets label justification [Default is MC].</p>
<dt><code>+n</code><i>dx</i>[/<i>dy</i>]</p>
<dd> Nudges the placement of labels by the specified amount (append <code>c</code>|<code>i</code>|<code>p</code> to specify the units). Increments are considered in the coordinate system defined by the orientation of the contour; use <code>+N</code> to force increments in the plot x/y coordinates system [no nudging]. Not allowed with <code>+v</code>.</p>
<dt><code>+o</code></p>
<dd> Selects rounded rectangular text box [Default is rectangular]. Not applicable for curved text (<code>+v</code>) and only makes sense for opaque text boxes.</p>
<dt><code>+p</code>[<i>pen</i>]</p>
<dd> Draws the outline of text boxes [Default is no outline]; optionally specify pen for outline [Default is width = 0.25p, color = black, style = solid].</p>
<dt><code>+r</code><i>min_rad</i></p>
<dd> Will not place labels where the contours&#8217;s radius of curvature is less than <i>min_rad</i> [Default is 0].</p>
<dt><code>+t</code>[<i>file</i>]</p>
<dd> Saves contour label x, y, and text to <i>file</i> [Contour_labels.txt]. Use <code>+T</code> to save x, y, angle, text instead.</p>
<dt><code>+u</code><i>unit</i></p>
<dd> Appends <i>unit</i> to all contour labels. [Default is no unit]. If <code>z</code> is appended we use the z-unit from the grdfile.</p>
<dt><code>+v</code></p>
<dd> Specifies curved labels following the contour [Default is straight labels].</p>
<dt><code>+w</code></p>
<dd> Specifies how many (<i>x</i>,<i>y</i>) points will be used to estimate label angles [automatic].</p>
<dt><code>+=</code><i>prefix</i></p>
<dd> Prepends <i>prefix</i> to all contour labels. [Default is no prefix].</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-D</code><i>&lt;template&gt;</i></p>
<dd> Dump contours as data line segments; no plotting takes place. Append filename template which may contain C-format specifiers. If no filename template is given we write all lines to stdout. If filename has no specifiers then we write all lines to a single file. If a float format (e.g., %6.2f) is found we substitute the contour z-value. If an integer format (e.g., %06d) is found we substitute a running segment count. If an char format (%c) is found we substitute C or O for closed and open contours. The 1-3 specifiers may be combined and appear in any order to produce the the desired number of output files (e.g., just %c gives two files, just %f would. separate segments into one file per contour level, and %d would write all segments. to individual files; see manual page for more examples.</p>
<dt><code>-F</code>[<code>l</code>|<code>r</code>]</p>
<dd> Force dumped contours to be oriented so that higher z-values are to the left (<code>-Fl</code> [Default]) or right (<code>-Fr</code>) as we move along the contour [Default is arbitrary orientation]. Requires <code>-D</code>. </p>
<p> <code>-G</code>[<code>d</code>|<code>f</code>|<code>n</code>|<code>l</code>|<code>L</code>|<code>x</code>|<code>X</code>]<i>params</i> The required argument controls the placement of labels along the quoted lines. Choose among five controlling algorithms:</p>
<dt><code>d</code><i>dist</i>[<code>c</code>|<code>i</code>|<code>p</code>] or <code>D</code><i>dist</i>[<code>d</code>|<code>e</code>|<code>f</code>|<code>k</code>|<code>m</code>|<code>M</code>|<code>n</code>|<code>s</code>]</p>
<dd> For lower case <code>d</code>, give distances between labels on the plot in your preferred measurement unit <code>c</code> (cm), <code>i</code> (inch), or <code>p</code> (points), while for upper case <code>D</code>, specify distances in map units and append the unit; choose among <code>e</code> (m), <code>f</code> (foot), <code>k</code> (km), <code>M</code> (mile), <code>n</code> (nautical mile) or <code>u</code> (US survey foot), and <code>d</code> (arc degree), <code>m</code> (arc minute), or <code>s</code> (arc second). [Default is 10<code>c</code> or 4<code>i</code>]. As an option, you can append /<i>fraction</i> which is used to place the very first label for each contour when the cumulative along-contour distance equals <i>fraction * dist</i> [0.25].</p>
<dt><code>f</code><i>ffile.d</i></p>
<dd> Reads the ASCII file <i>ffile.d</i> and places labels at locations in the file that matches locations along the quoted lines. Inexact matches and points outside the region are skipped.</p>
<dt><code>l|L</code><i>line1</i>[,<i>line2</i>,&#8230;]</p>
<dd> Give <i>start</i> and <i>stop</i> coordinates for one or more comma-separated straight line segments. Labels will be placed where these lines intersect the quoted lines. The format of each <i>line</i> specification is <i>start/stop</i>, where <i>start</i> and <i>stop</i> are either a specified point <i>lon/lat</i> or a 2-character <code>XY</code> key that uses the justification format employed in <code>pstext</code> to indicate a point on the map, given as [LCR][BMT]. In addition, you can use Z-, Z+ to mean the global minimum and maximum locations in the grid. <code>L</code> will interpret the point pairs as defining great circles [Default is straight line].</p>
<dt><code>n</code><i>n_label</i></p>
<dd> Specifies the number of equidistant labels for quoted lines line [1]. Upper case <code>N</code> starts labeling exactly at the start of the line [Default centers them along the line]. <code>N</code>-1 places one justified label at start, while <code>N</code>+1 places one justified label at the end of quoted lines. Optionally, append /<i>min_dist</i>[<code>c</code>|<code>i</code>|<code>p</code>] to enforce that a minimum distance separation between successive labels is enforced.</p>
<dt><code>x|X</code><i>xfile.d</i></p>
<dd> Reads the multisegment file <i>xfile.d</i> and places labels at the intersections between the quoted lines and the lines in <i>xfile.d</i>. <code>X</code> will resample the lines first along great-circle arcs. </p>
<p> In addition, you may optionally append <code>+r</code><i>radius</i>[<code>c</code>|<code>i</code>|<code>p</code>] to set a minimum label separation in the x-y plane [no limitation].</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code><i>low/high</i></p>
<dd> Limit range: Do not draw contours for data values below <i>low</i> or above <i>high</i>.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code><i>cut</i></p>
<dd> Do not draw contours with less than <i>cut</i> number of points [Draw all contours].</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i> [Default is region defined in the grid file].</p>
<dt><code>-S</code><i>smoothfactor</i></p>
<dd> Used to resample the contour lines at roughly every (gridbox_size/<i>smoothfactor</i>) interval.</p>
<dt><code>-T</code>[<code>+|-</code>][<code>+d</code><i>gap</i>[/<i>length</i>]][<code>+l</code>[<i>labels</i>]]</p>
<dd> Will draw tick marks pointing in the downward direction every <i>gap</i> along the innermost closed contours. Append <code>+d</code><i>gap</i> and optionally tick mark <i>length</i> (append units as <code>c</code>, <code>i</code>, or <code>p</code>) or use defaults [15<code>p</code>/3<code>p</code>]. User may choose to tick only local highs or local lows by specifying <code>-T+</code> or <code>-T-</code>, respectively. Append <code>+l</code><i>labels</i> to annotate the centers of closed innermost contours (i.e., the local lows and highs). If no <i>labels</i> is appended we use &#8211; and + as the labels. Appending exactly two characters, e.g., <code>+l</code><i>LH</i>, will plot the two characters (here, L and H) as labels. For more elaborate labels, separate the low and hight label strings with a comma (e.g., <code>+l</code><i>lo</i>,<i>hi</i>). If a file is given by <code>-C</code> and <code>-T</code> is set, then only contours marked with upper case C or A will have tick marks [and annotations].</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<code>+</code>][<i>type</i>]<i>pen</i> <i>(more &#8230;)</i></p>
<dd> <i>type</i>, if present, can be <code>a</code> for annotated contours or <code>c</code> for regular contours [Default]. <i>pen</i> sets the attributes for the particular line. Default pen for annotated contours: 0.75p,black. Regular contours use pen 0.25p,black. If the <code>+</code> flag is prepended then the color of the contour lines are taken from the CPT file (see <code>-C</code>). If the <code>&#8211;</code> flag is prepended then the color from the cpt file is applied both to the contours and the contour annotations. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-Z</code>[<i>factor</i>[/<i>shift</i>]][<code>p</code>]</p>
<dd> Use to subtract <i>shift</i> from the data and multiply the results by <i>factor</i> before contouring starts [1/0]. (Numbers in <code>-A</code>, <code>-C</code>, <code>-L</code> refer to values after this scaling has occurred.) Append <code>p</code> to indicate that this grid file contains z-values that are periodic in 360 degrees (e.g., phase data, angular distributions) and that special precautions must be taken when determining 0-contours.</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output.</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-do</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace output columns that equal NaN with <i>nodata</i>.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
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
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>EXAMPLES</h2>
<p> To contour the file hawaii_grav.nc every 25 mGal on a Mercator map at 0.5 inch/degree, annotate every 50 mGal (using fontsize = 10p), using 1 degree tickmarks, and draw 30 minute gridlines: </p>
<pre>
gmt grdcontour hawaii_grav.nc -Jm0.5i -C25 -A50+f10p -B1g30m &gt; hawaii_grav.ps
</pre>
<p> To contour the file image.nc using the levels in the file cont.d on a linear projection at 0.1 cm/x-unit and 50 cm/y-unit, using 20 (x) and 0.1 (y) tickmarks, smooth the contours a bit, use &quot;RMS Misfit&quot; as plot-title, use a thick red pen for annotated contours, and a thin, dashed, blue pen for the rest, and send the output to the default printer: </p>
<pre>
gmt grdcontour image.nc -Jx0.1c/50.0c -Ccont.d -S4 -Bx20 -By0.1 \
           -B+t&quot;RMS Misfit&quot; -Wathick,red -Wcthinnest,blue,- | lp
</pre>
<p> The labeling of local highs and lows may plot outside the innermost contour since only the mean value of the contour coordinates is used to position the label. </p>
<p> To save the smoothed 100-m contour lines in topo.nc and separate them into two multisegment files: contours_C.txt for closed and contours_O.txt for open contours, try </p>
<pre>
gmt grdcontour topo.nc -C100 -S4 -Dcontours_%c.txt
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtcolors</code>, <code>psbasemap</code>, <code>grdimage</code>, <code>grdview</code>, <code>pscontour</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
