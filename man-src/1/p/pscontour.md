---
title: "pscontour(1)"
name: "pscontour"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pscontour/"
description: "pscontour – Contour table data by direct triangulation [method]"
---

<h2>NAME</h2>
<p> pscontour &#8211; Contour table data by direct triangulation [method]</p>
<h2>SYNOPSIS</h2>
<p> <code>pscontour</code> [ <i>table</i> ] [+]<i>cpt</i> <i>parameters</i> <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] [ [<code>&#8211;</code>|[+]<i>annot_int</i>][<i>labelinfo</i>] ] [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ [<i>template</i>] ] [ <i>indexfile</i> ] [ [<code>d</code>|<code>f</code>|<code>n</code>|<code>l</code>|<code>L</code>|<code>x</code>|<code>X</code>]<i>params</i> ] [ ] [ <code>z</code>|<code>Z</code><i>parameters</i> ] [ ] [ <i>pen</i> ] [ ] [ ] [ ] [ <i>cut</i> ] [ [<i>p</i>|<i>t</i>] ] [ [<code>+|-</code>][<code>+d</code><i>gap</i>[/<i>length</i>]][<code>+l</code>[<i>labels</i>]] ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ [<code>+</code>]<i>pen</i> ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>pscontour</code> reads an ASCII [or binary] <i>table</i> and produces a raw contour plot by triangulation. By default, the optimal Delaunay triangulation is performed (using either Shewchuk&#8217;s [1996] or Watson&#8217;s [1982] method as selected during GMT installation; type <code>pscontour &#8211;</code> to see which method is selected), but the user may optionally provide a second file with network information, such as a triangular mesh used for finite element modeling. In addition to contours, the area between contours may be painted according to the CPT file. Alternatively, the x/y/z positions of the contour lines may be saved to one or more output files (or stdout) and no plot is produced.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-C</code>[+]<i>cont_int</i></p>
<dd> The contours to be drawn may be specified in one of three possible ways:</p>
<dt>1.</p>
<dd> If <i>cont_int</i> has the suffix &quot;.cpt&quot; and can be opened as a file, it is assumed to be a CPT file. The color boundaries are then used as contour levels. If the CPT file has annotation flags in the last column then those contours will be annotated. By default all contours are labeled; use <code>-A-</code> to disable all annotations.</p>
<dt>2.</p>
<dd> If <i>cont_int</i> is a file but not a CPT file, it is expected to contain contour levels in column 1 and a C(ontour) OR A(nnotate) in col 2. The levels marked C (or c) are contoured, the levels marked A (or a) are contoured and annotated. Optionally, a third column may be present and contain the fixed annotation angle for this contour level.</p>
<dt>3.</p>
<dd> If no file is found, then <i>cont_int</i> is interpreted as a constant contour interval. However, if prepended with the + sign the <i>cont_int</i> is taken as meaning draw that single contour. The <code>-A</code> option offers the same possibility so they may be used together to plot only one annotated and one non-annotated contour. If <code>-A</code> is set and <code>-C</code> is not, then the contour interval is set equal to the specified annotation interval. </p>
<p> If a file is given and <code>-T</code> is set, then only contours marked with upper case C or A will have tick-marks. In all cases the contour values have the same units as the file.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i></dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
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
<dd> Set map boundary intervals. </p>
<p> <code>-D</code>[<i>template</i>] Dump the (x,y,z) coordinates of each contour to one or more output files (or <i>stdout</i> if <i>template</i> is not given). No plotting will take place. If <i>template</i> contains one or more of the C-format specifiers %d, %f, %c then line segments will be written to different files; otherwise all lines are written to the specified file (<i>template</i>). The use of the C-format specifiers controls how many files are created and how the contours are organized. If the float format %f is present (standard modifications to width and precision are allowed, e.g., %f7.3f), then the filenames will contain the contour value and lines are thus separated into files based on a common contour value. If the integer format %d is present (including modifications like %05d), then all contours are written to individual segment files; if any of the other specifiers are present they just affect the file names. Finally, if the character format %c is present it is replaced with the letters C (for closed) or O (for open), reflecting the nature of each contour. Any combination of one, two, or all three modifiers are valid, resulting in different filenames and number of files. For instance, if %c appears by itself, then only two files are created, separating the open from the closed contours (assuming both kinds are present). If just %f is used, then all segments for the same contour level will be written to the same file, resulting in <i>N</i> multi-segment files. If both %f and %c were combined then each contour level would be further subdivided into closed and open contours. Any combination involving %d will result in one individual file for each segment; %c, %f only modifies the file names. The files are ASCII unless <code>-bo</code> is used.</p>
<dt><code>-E</code><i>indexfile</i></p>
<dd> Give name of file with network information. Each record must contain triplets of node numbers for a triangle [Default computes these using Delaunay triangulation (see <code>triangulate</code>)]. </p>
<p> <code>-G</code> The required argument controls the placement of labels along the quoted lines. Choose among five controlling algorithms:</p>
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
<dt><code>-I</code></p>
<dd> Color the triangles using the CPT file.</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code><i>pen</i> <i>(more &#8230;)</i></p>
<dd> Draw the underlying triangular mesh using the specified pen attributes [Default is no mesh].</p>
<dt><code>-N</code></p>
<dd> Do NOT clip contours or image at the boundaries [Default will clip to fit inside region <code>-R</code>].</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code><i>cut</i></p>
<dd> Do not draw contours with less than <i>cut</i> number of points [Draw all contours].</p>
<dt><code>-S</code>[<i>p</i>|<i>t</i>]</p>
<dd> Skip all input <i>xyz</i> points that fall outside the region [Default uses all the data in the triangulation]. Alternatively, use <code>-St</code> to skip triangles whose three vertices are all outside the region. <code>-S</code> with no modifier is interpreted as <code>-Sp</code>.</p>
<dt><code>-T</code>[<code>+|-</code>][<code>+d</code><i>gap</i>[/<i>length</i>]][<code>+l</code>[<i>labels</i>]]</p>
<dd> Will draw tick marks pointing in the downward direction every <i>gap</i> along the innermost closed contours. Append <code>+d</code><i>gap</i> and optionally tick mark <i>length</i> (append units as <code>c</code>, <code>i</code>, or <code>p</code>) or use defaults [15<code>p</code>/3<code>p</code>]. User may choose to tick only local highs or local lows by specifying <code>-T+</code> or <code>-T-</code>, respectively. Append <code>+l</code><i>labels</i> to annotate the centers of closed innermost contours (i.e., the local lows and highs). If no <i>labels</i> is appended we use &#8211; and + as the labels. Appending exactly two characters, e.g., <code>+l</code><i>LH</i>, will plot the two characters (here, L and H) as labels. For more elaborate labels, separate the low and hight label strings with a comma (e.g., <code>+l</code><i>lo</i>,<i>hi</i>). If a file is given by <code>-C</code> and <code>-T</code> is set, then only contours marked with upper case C or A will have tick marks [and annotations].</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<code>+</code>]<i>pen</i> <i>(more &#8230;)</i></p>
<dd> Select contouring and set contour pen attributes. If the <code>+</code> flag is prepended then the color of the contour lines are taken from the CPT file (see <code>-C</code>). If the <code>&#8211;</code> flag is prepended then the color from the CPT file is applied both to the contours and the contour annotations. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 3 input columns]. Use 4-byte integer triplets for node ids (<code>-E</code>).</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is 3 output columns].</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-:</code>[<code>i</code>|<code>o</code>] <i>(more &#8230;)</i></p>
<dd> Swap 1st and 2nd column on input and/or output.</p>
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
<h2>EXAMPLES</h2>
<p> To make a raw contour plot from the file topo.xyz and drawing the contours (pen = 2) given in the CPT file topo.cpt on a Lambert map at 0.5 inch/degree along the standard parallels 18 and 24, use </p>
<pre>
gmt pscontour topo.xyz -R320/330/20/30 -Jl18/24/0.5i -Ctopo.cpt -W0.5p &gt; topo.ps
</pre>
<p> To create a color PostScript plot of the numerical temperature solution obtained on a triangular mesh whose node coordinates and temperatures are stored in temp.xyz and mesh arrangement is given by the file mesh.ijk, using the colors in temp.cpt, run </p>
<pre>
gmt pscontour temp.xyz -R0/150/0/100 -Jx0.1i -Ctemp.cpt -G -W0.25p &gt; temp.ps
</pre>
<p> To save the triangulated 100-m contour lines in topo.txt and separate them into multisegment files (one for each contour level), try </p>
<pre>
gmt pscontour topo.txt -C100 -Dcontours_%.0f.txt
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtcolors</code>, <code>grdcontour</code>, <code>grdimage</code>, <code>nearneighbor</code>, <code>psbasemap</code>, <code>psscale</code>, <code>surface</code>, <code>triangulate</code></p>
<h2>REFERENCES</h2>
<p> Watson, D. F., 1982, Acord: Automatic contouring of raw data, <i>Comp. &amp; Geosci.</i>, <code>8</code>, 97-101. </p>
<p> Shewchuk, J. R., 1996, Triangle: Engineering a 2D Quality Mesh Generator and Delaunay Triangulator, First Workshop on Applied Computational Geometry (Philadelphia, PA), 124-133, ACM, May 1996. </p>
<p> <i><a rel="nofollow" href="http://www.cs.cmu.edu/~quake/triangle.html">http://www.cs.cmu.edu/~quake/triangle.html</a></i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
