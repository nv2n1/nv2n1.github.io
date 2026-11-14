---
title: "psbasemap(1)"
name: "psbasemap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psbasemap/"
description: "psbasemap – Plot PostScript base maps"
---

<h2>NAME</h2>
<p> psbasemap &#8211; Plot PostScript base maps</p>
<h2>SYNOPSIS</h2>
<p> <code>psbasemap</code> <i>parameters</i> <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ [<i>file</i>] ] [ <i>insert box</i> ] [ <i>box</i> ] [ ] [ <code>z</code>|<code>Z</code><i>parameters</i> ] [ <i>ruler</i> ] [ ] [ ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ <i>rose</i> ] [ <i>mag_rose</i> ] [ [<i>level</i>] ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>psbasemap</code> creates PostScript code that will produce a basemap. Several map projections are available, and the user may specify separate tick-mark intervals for boundary annotation, ticking, and [optionally] gridlines. A simple map scale or directional rose may also be plotted. At least one of the options <code>-B</code>, <code>-L</code>, or <code>-T</code> must be specified.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i></dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<i>file</i>]</p>
<dd> No plotting is performed. Instead, we determine the geographical coordinates of the polygon outline for the (possibly oblique) rectangular map domain. The plot domain must be given via <code>-R</code> and <code>-J</code>, with no other options allowed. The sampling interval is controlled via <code>MAP_LINE_STEP</code> parameter. The coordinates are written to <i>file</i> or to standard output if no file is specified.</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-D</code>[<i>unit</i>]<i>xmin/xmax/ymin/ymax</i>[<code>r</code>][<code>+s</code><i>file</i>] | <code>-D</code>[<code>g</code>|<code>j</code>|<code>J</code>|<code>n</code>|<code>x</code>]<i>refpoint</i><code>+w</code><i>width</i>[/<i>height</i>][<code>+j</code><i>justify</i>][<code>+o</code><i>dx</i>[/<i>dy</i>]][<code>+s</code><i>file</i>]</p>
<dd> Draw a simple map insert box on the map. Requires <code>-F</code>. Specify the box in one of three ways: (a) Give <i>west/east/south/north</i> of geographic rectangle bounded by parallels and meridians; append <code>r</code> if the coordinates instead are the lower left and upper right corners of the desired rectangle. (b) Give <code>u</code><i>xmin/xmax/ymin/ymax</i> of bounding rectangle in projected coordinates (here, <code>u</code> is the coordinate unit). (c) Give the reference point on the map for the insert using one of four coordinate systems: (1) Use <code>-Dg</code> for map (user) coordinates, (2) use <code>-Dj</code> or <code>-DJ</code> for setting <i>refpoint</i> via a 2-char justification code that refers to the (invisible) map domain rectangle, (3) use <code>-Dn</code> for normalized (0-1) coordinates, or (4) use <code>-Dx</code> for plot coordinates (inches, cm, etc.). Append <code>+w</code><i>width</i>[/<i>height</i>] of bounding rectangle or box in plot coordinates (inches, cm, etc.). By default, the anchor point on the scale is assumed to be the bottom left corner (BL), but this can be changed by appending <code>+j</code> followed by a 2-char justification code <i>justify</i> (see <code>pstext</code>). Note: If <code>-Dj</code> is used then <i>justify</i> defaults to the same as <i>refpoint</i>, if <code>-DJ</code> is used then <i>justify</i> defaults to the mirror opposite of <i>refpoint</i>. Add <code>+o</code> to offset the color scale by <i>dx</i>/<i>dy</i> away from the <i>refpoint</i> point in the direction implied by <i>justify</i> (or the direction implied by <code>-Dj</code> or <code>-DJ</code>). If you need access to the placement of the lower left corner of the map insert and its dimensions in the current map unit, use <code>s</code><i>file</i> to write this information to <i>file</i>. Specify insert box attributes via the <code>-F</code> option [outline only].</p>
<dt><code>-F</code>[<code>d</code>|<code>l</code>|<code>t</code>][<code>+c</code><i>clearances</i>][<code>+g</code><i>fill</i>][<code>+i</code>[[<i>gap</i>/]<i>pen</i>]][<code>+p</code>[<i>pen</i>]][<code>+r</code>[<i>radius</i>]][<code>+s</code>[[<i>dx</i>/<i>dy</i>/][<i>shade</i>]]]</p>
<dd> Without further options, draws a rectangular border around any map insert (<code>-D</code>), map scale (<code>-L</code>) or map rose (<code>-T</code>) using <code>MAP_FRAME_PEN</code>; specify a different pen with <code>+p</code><i>pen</i>. Add <code>+g</code><i>fill</i> to fill the logo box [no fill]. Append <code>+c</code><i>clearance</i> where <i>clearance</i> is either <i>gap</i>, <i>xgap</i>/<i>ygap</i>, or <i>lgap</i>/<i>rgap</i>/<i>bgap</i>/<i>tgap</i> where these items are uniform, separate in x- and y-direction, or individual side spacings between logo and border. Append <code>+i</code> to draw a secondary, inner border as well. We use a uniform <i>gap</i> between borders of 2<code>p</code> and the <code>MAP_DEFAULTS_PEN</code> unless other values are specified. Append <code>+r</code> to draw rounded rectangular borders instead, with a 6<code>p</code> corner radius. You can override this radius by appending another value. Finally, append <code>+s</code> to draw an offset background shaded region. Here, <i>dx</i>/<i>dy</i> indicates the shift relative to the foreground frame [4<code>p</code>/-4<code>p</code>] and <i>shade</i> sets the fill style to use for shading [gray50]. Used in combination with <code>-D</code>, <code>-L</code> or <code>-T</code>. To specify separate parameters for the various map features, append <code>d</code>|<code>l</code>|<code>t</code> to <code>-F</code> to specify panel parameters for just that panel [Default uses the same panel parameters for all selected map features].</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code>[<code>g</code>|<code>j</code>|<code>J</code>|<code>n</code>|<code>x</code>]<i>refpoint</i><code>+c</code>[<i>slon</i>/]<i>slat</i><code>+w</code><i>length</i>[<code>e</code>|<code>f</code>|<code>k</code>|<code>M</code>|<code>n</code>|<code>u</code>][<code>+a</code><i>align</i>][<code>+f</code>][<code>+l</code>[<i>label</i>]][<code>+u</code>]</p>
<dd> Draws a simple map scale centered on the reference point specified using one of four coordinate systems: (1) Use <code>-Dg</code> for map (user) coordinates, (2) use <code>-Dj</code> or <code>-DJ</code> for setting <i>refpoint</i> via a 2-char justification code that refers to the (invisible) map domain rectangle, (3) use <code>-Dn</code> for normalized (0-1) coordinates, or (4) use <code>-Dx</code> for plot coordinates (inches, cm, etc.). Scale is calculated for latitude <i>slat</i> (optionally supply longitude <i>slon</i> for oblique projections [Default is central meridian]), <i>length</i> is in km, or append unit from <code>e</code>|<code>f</code>|<code>k</code>|<code>M</code>|<code>n</code>|<code>u</code>. Change the label alignment with <code>+a</code><i>align</i> (choose among <code>l</code>(eft), <code>r</code>(ight), <code>t</code>(op), and <code>b</code>(ottom)). Append <code>+f</code> to get a &quot;fancy&quot; scale [Default is plain]. Append <code>+l</code> to select the default label, which equals the distance unit (meter, foot, km, mile, nautical mile, US survey foot) and is justified on top of the scale [t]. Change this by giving your own label (append <code>+l</code><i>label</i>). Select <code>+u</code> to append the unit to all distance annotations along the scale (for the plain scale, <code>+u</code> will instead select the unit to be appended to the distance length). Note: Use <i>FONT_LABEL</i> to change the label font and <i>FONT_ANNOT_PRIMARY</i> to change the annotation font. The height of the map scale is controlled by <i>MAP_SCALE_HEIGHT</i>, and the pen thickness is set by <i>MAP_TICK_PEN_PRIMARY</i>. See <code>-F</code> on how to place a panel behind the scale.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Td</code>[<code>g</code>|<code>j</code>|<code>J</code>|<code>n</code>|<code>x</code>]<i>refpoint</i><code>+w</code><i>width</i>[<code>+f</code>[<i>level</i>]][<code>+j</code><i>justify</i>][<code>+l</code><i>w,e,s,n</i>][<code>+o</code><i>dx</i>[/<i>dy</i>]]</p>
<dd> <code>-Td</code> draws a map directional rose on the map at the location defined by the reference and anchor points: Give the reference point on the map for the rose using one of four coordinate systems: (1) Use <code>g</code> for map (user) coordinates, (2) use <code>j</code> for setting <i>refpoint</i> via a 2-char justification code that refers to the (invisible) map domain rectangle, (3) use <code>n</code> for normalized (0-1) coordinates, or (4) use <code>x</code> for plot coordinates (inches, cm, etc.) [Default]. You can offset the reference point by <i>dx</i>/<i>dy</i> in the direction implied by <i>justify</i>. By default, the anchor point on the scale is assumed to be the center of the rose (MC), but this can be changed by appending <code>+j</code> followed by a 2-char justification code <i>justify</i> (see <code>pstext</code>). Note: If <code>-Dj</code> is used then <i>justify</i> defaults to the same as <i>refpoint</i>, if <code>-DJ</code> is used then <i>justify</i> defaults to the mirror opposite of <i>refpoint</i>. Add <code>+o</code> to offset the color scale by <i>dx</i>/<i>dy</i> away from the <i>refpoint</i> point in the direction implied by <i>justify</i> (or the direction implied by <code>-Dj</code> or <code>-DJ</code>). Append <code>+w</code><i>width</i>to set the width of the rose in plot coordinates (inches, cm, etc.). Add <code>+f</code> to get a &quot;fancy&quot; rose, and specify in <i>level</i> what you want drawn. The default [1] draws the two principal E-W, N-S orientations, 2 adds the two intermediate NW-SE and NE-SW orientations, while 3 adds the eight minor orientations WNW-ESE, NNW-SSE, NNE-SSW, and ENE-WSW. Label the cardinal points W,E,S,N by adding <code>+l</code> and append your own four comma-separated strings to override the default. See <code>-F</code> on how to place a panel behind the scale. </p>
<p> <code>-Tm</code>[<code>g</code>|<code>j</code>|<code>J</code>|<code>n</code>|<code>x</code>]<i>refpoint</i><code>+w</code><i>width</i>[<code>+d</code><i>dec</i>[/<i>dlabel</i>]]][<code>+i</code><i>pen</i>][<code>+j</code><i>justify</i>][<code>+l</code><i>w,e,s,n</i>][<code>+p</code><i>pen</i>][<code>+t</code><i>ints</i>][<code>+o</code><i>dx</i>[/<i>dy</i>]] <code>-Tm</code> draws a map magnetic rose on the map at the location defined by the reference and anchor points: Give the reference point on the map for the rose using one of four coordinate systems: (1) Use <code>g</code> for map (user) coordinates, (2) use <code>j</code> for setting <i>refpoint</i> via a 2-char justification code that refers to the (invisible) map domain rectangle, (3) use <code>n</code> for normalized (0-1) coordinates, or (4) use <code>x</code> for plot coordinates (inches, cm, etc.) [Default]. You can offset the reference point by <i>dx</i>/<i>dy</i> in the direction implied by <i>justify</i>. By default, the anchor point on the scale is assumed to be the center of the rose (MC), but this can be changed by appending <code>+j</code> followed by a 2-char justification code <i>justify</i> (see <code>pstext</code>). Note: If <code>-Dj</code> is used then <i>justify</i> defaults to the same as <i>refpoint</i>, if <code>-DJ</code> is used then <i>justify</i> defaults to the mirror opposite of <i>refpoint</i>. Add <code>+o</code> to offset the color scale by <i>dx</i>/<i>dy</i> away from the <i>refpoint</i> point in the direction implied by <i>justify</i> (or the direction implied by <code>-Dj</code> or <code>-DJ</code>). Append <code>+w</code><i>width</i>to set the width of the rose in plot coordinates (inches, cm, etc.). Use <code>+d</code> to assign the magnetic declination and set <i>dlabel</i>, which is a label for the magnetic compass needle (Leave empty to format a label from <i>dec</i>, or give &#8211; to bypass labeling). With <code>+d</code>, both directions to geographic and magnetic north are plotted [Default is geographic only]. If the north label is <code>*</code> then a north star is plotted instead of the north label. Annotation and two levels of tick intervals for both geographic and magnetic directions are 30/5/1 degrees; override these settings by appending <code>+t</code><i>ints</i>, and append six intervals to set both the geographic and magnetic intervals. Number GMT default parameters control pens, fonts, and color; see the Map Embellishment section in the Cookbook. See <code>-F</code> on how to place a panel behind the scale.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns. This applies only to the coordinates specified in the <code>-R</code> option.</p>
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
<p> The following section illustrates the use of the options by giving some examples for the available map projections. Note how scales may be given in several different ways depending on the projection. Also note the use of upper case letters to specify map width instead of map scale.</p>
<h2>NON-GEOGRAPHICAL PROJECTIONS</h2>
<h3>Linear x-y plot</h3>
<p> To make a linear x/y frame with all axes, but with only left and bottom axes annotated, using xscale = yscale = 1.0, ticking every 1 unit and annotating every 2, and using xlabel = &quot;Distance&quot; and ylabel = &quot;No of samples&quot;, use </p>
<pre>
gmt psbasemap -R0/9/0/5 -Jx1 -Bf1a2 -Bx+lDistance -By+l&quot;No of samples&quot; -BWeSn &gt; linear.ps
</pre>
<h3>Log-log plot</h3>
<p> To make a log-log frame with only the left and bottom axes, where the x-axis is 25 cm and annotated every 1-2-5 and the y-axis is 15 cm and annotated every power of 10 but has tick-marks every 0.1, run </p>
<pre>
gmt psbasemap -R1/10000/1e20/1e25 -JX25cl/15cl -Bx2+lWavelength -Bya1pf3+lPower -BWS &gt; loglog.ps
</pre>
<h3>Power axes</h3>
<p> To design an axis system to be used for a depth-sqrt(age) plot with depth positive down, ticked and annotated every 500m, and ages annotated at 1 my, 4 my, 9 my etc, use </p>
<pre>
gmt psbasemap -R0/100/0/5000 -Jx1p0.5/-0.001 -Bx1p+l&quot;Crustal age&quot; -By500+lDepth &gt; power.ps
</pre>
<h3>Polar (theta,r) plot</h3>
<p> For a base map for use with polar coordinates, where the radius from 0 to 1000 should correspond to 3 inch and with gridlines and ticks intervals automatically determined, use </p>
<pre>
gmt psbasemap -R0/360/0/1000 -JP6i -Bafg &gt; polar.ps
</pre>
<h2>CYLINDRICAL MAP PROJECTIONS</h2>
<h3>Cassini</h3>
<p> A 10-cm-wide basemap using the Cassini projection may be obtained by </p>
<pre>
gmt psbasemap -R20/50/20/35 -JC35/28/10c -P -Bafg -B+tCassini &gt; cassini.ps
</pre>
<h3>Mercator [conformal]</h3>
<p> A Mercator map with scale 0.025 inch/degree along equator, and showing the length of 5000 km along the equator (centered on 1/1 inch), may be plotted as </p>
<pre>
gmt psbasemap -R90/180/-50/50 -Jm0.025i -Bafg -B+tMercator -Lx1i/1i+c0+w5000k &gt; mercator.ps
</pre>
<h3>Miller</h3>
<p> A global Miller cylindrical map with scale 1:200,000,000 may be plotted as </p>
<pre>
gmt psbasemap -Rg -Jj180/1:200000000 -Bafg -B+tMiller &gt; miller.ps
</pre>
<h3>Oblique Mercator [conformal]</h3>
<p> To create a page-size global oblique Mercator basemap for a pole at (90,30) with gridlines every 30 degrees, run </p>
<pre>
gmt psbasemap -R0/360/-70/70 -Joc0/0/90/30/0.064cd -B30g30 -B+t&quot;Oblique Mercator&quot; &gt; oblmerc.ps
</pre>
<h3>Transverse Mercator [conformal]</h3>
<p> A regular Transverse Mercator basemap for some region may look like </p>
<pre>
gmt psbasemap -R69:30/71:45/-17/-15:15 -Jt70/1:1000000 -Bafg -B+t&quot;Survey area&quot; -P &gt; transmerc.ps
</pre>
<h3>Equidistant Cylindrical Projection</h3>
<p> This projection only needs the central meridian and scale. A 25 cm wide global basemap centered on the 130E meridian is made by </p>
<pre>
gmt psbasemap -R-50/310/-90/90 -JQ130/25c -Bafg -B+t&quot;Equidistant Cylindrical&quot; &gt; cyl_eqdist.ps
</pre>
<h3>Universal Transverse Mercator [conformal]</h3>
<p> To use this projection you must know the UTM zone number, which defines the central meridian. A UTM basemap for Indo-China can be plotted as </p>
<pre>
gmt psbasemap -R95/5/108/20r -Ju46/1:10000000 -Bafg -B+tUTM &gt; utm.ps
</pre>
<h3>Cylindrical Equal-Area</h3>
<p> First select which of the cylindrical equal-area projections you want by deciding on the standard parallel. Here we will use 45 degrees which gives the Gall-Peters projection. A 9 inch wide global basemap centered on the Pacific is made by </p>
<pre>
gmt psbasemap -Rg -JY180/45/9i -Bafg -B+tGall-Peters &gt; gall-peters.ps
</pre>
<h2>CONIC MAP PROJECTIONS</h2>
<h3>Albers [equal-area]</h3>
<p> A basemap for middle Europe may be created by </p>
<pre>
gmt psbasemap -R0/90/25/55 -Jb45/20/32/45/0.25c -Bafg -B+t&quot;Albers Equal-area&quot; &gt; albers.ps
</pre>
<h3>Lambert [conformal]</h3>
<p> Another basemap for middle Europe may be created by </p>
<pre>
gmt psbasemap -R0/90/25/55 -Jl45/20/32/45/0.1i -Bafg -B+t&quot;Lambert Conformal Conic&quot; &gt; lambertc.ps
</pre>
<h3>Equidistant</h3>
<p> Yet another basemap of width 6 inch for middle Europe may be created by </p>
<pre>
gmt psbasemap -R0/90/25/55 -JD45/20/32/45/6i -Bafg -B+t&quot;Equidistant conic&quot; &gt; econic.ps
</pre>
<h3>Polyconic</h3>
<p> A basemap for north America may be created by </p>
<pre>
gmt psbasemap -R-180/-20/0/90 -JPoly/4i -Bafg -B+tPolyconic &gt; polyconic.ps
</pre>
<h2>AZIMUTHAL MAP PROJECTIONS</h2>
<h3>Lambert [equal-area]</h3>
<p> A 15-cm-wide global view of the world from the vantage point -80/-30 will give the following basemap: </p>
<pre>
gmt psbasemap -Rg -JA-80/-30/15c -Bafg -B+t&quot;Lambert Azimuthal&quot; &gt; lamberta.ps
</pre>
<p> Follow the instructions for stereographic projection if you want to impose rectangular boundaries on the azimuthal equal-area map but substitute <code>-Ja</code> for <code>-Js</code>.</p>
<h3>Equidistant</h3>
<p> A 15-cm-wide global map in which distances from the center (here 125/10) to any point is true can be obtained by: </p>
<pre>
gmt psbasemap -Rg -JE125/10/15c -Bafg -B+tEquidistant &gt; equi.ps
</pre>
<h3>Gnomonic</h3>
<p> A view of the world from the vantage point -100/40 out to a horizon of 60 degrees from the center can be made using the Gnomonic projection: </p>
<pre>
gmt psbasemap -Rg -JF-100/40/60/6i -Bafg -B+tGnomonic &gt; gnomonic.ps
</pre>
<h3>Orthographic</h3>
<p> A global perspective (from infinite distance) view of the world from the vantage point 125/10 will give the following 6-inch-wide basemap: </p>
<pre>
gmt psbasemap -Rg -JG125/10/6i -Bafg -B+tOrthographic &gt; ortho.ps
</pre>
<h3>General Perspective</h3>
<p> The <code>-JG</code> option can be used in a more generalized form, specifying altitude above the surface, width and height of the view point, and twist and tilt. A view from 160 km above -74/41.5 with a tilt of 55 and azimuth of 210 degrees, and limiting the viewpoint to 30 degrees width and height will product a 6-inch-wide basemap: </p>
<pre>
gmt psbasemap -Rg -JG-74/41.5/160/210/55/30/30/6i -Bafg -B+t&quot;General Perspective&quot; &gt; genper.ps
</pre>
<h3>Stereographic [conformal]</h3>
<p> To make a polar stereographic projection basemap with radius = 12 cm to -60 degree latitude, with plot title &quot;Salinity measurements&quot;, using 5 degrees annotation/tick interval and 1 degree gridlines, run </p>
<pre>
gmt psbasemap -R-45/45/-90/-60 -Js0/-90/12c/-60 -B5g1 -B+t&quot;Salinity measurements&quot; &gt; stereo1.ps
</pre>
<p> To make a 12-cm-wide stereographic basemap for Australia from an arbitrary view point (not the poles), and use a rectangular boundary, we must give the pole for the new projection and use the <code>-R</code> option to indicate the lower left and upper right corners (in lon/lat) that will define our rectangle. We choose a pole at 130/-30 and use 100/-45 and 160/-5 as our corners. The command becomes </p>
<pre>
gmt psbasemap -R100/-45/160/-5r -JS130/-30/12c -Bafg -B+t&quot;General Stereographic View&quot; &gt; stereo2.ps
</pre>
<h2>MISCELLANEOUS MAP PROJECTIONS</h2>
<h3>Hammer [equal-area]</h3>
<p> The Hammer projection is mostly used for global maps and thus the spherical form is used. To get a world map centered on Greenwich at a scale of 1:200000000, use </p>
<pre>
gmt psbasemap -Rd -Jh0/1:200000000 -Bafg -B+tHammer &gt; hammer.ps
</pre>
<h3>Sinusoidal [equal-area]</h3>
<p> To make a sinusoidal world map centered on Greenwich, with a scale along the equator of 0.02 inch/degree, use </p>
<pre>
gmt psbasemap -Rd -Ji0/0.02i -Bafg -B+tSinusoidal &gt; sinus1.ps
</pre>
<p> To make an interrupted sinusoidal world map with breaks at 160W, 20W, and 60E, with a scale along the equator of 0.02 inch/degree, run the following sequence of commands: </p>
<pre>
gmt psbasemap -R-160/-20/-90/90 -Ji-90/0.02i -Bx30g30 -By15g15 -BWesn -K &gt; sinus_i.ps
gmt psbasemap -R-20/60/-90/90 -Ji20/0.02i -Bx30g30 -By15g15 -Bwesn -O -K -X2.8i &gt;&gt; sinus_i.ps
gmt psbasemap -R60/200/-90/90 -Ji130/0.02i -Bx30g30 -By15g15 -BwEsn -O -X1.6i &gt;&gt; sinus_i.ps
</pre>
<h3>Eckert IV [equal-area]</h3>
<p> Pseudo-cylindrical projection typically used for global maps only. Set the central longitude and scale, e.g., </p>
<pre>
gmt psbasemap -Rg -Jkf180/0.064c -Bafg -B+t&quot;Eckert IV&quot; &gt; eckert4.ps
</pre>
<h3>Eckert VI [equal-area]</h3>
<p> Another pseudo-cylindrical projection typically used for global maps only. Set the central longitude and scale, e.g., </p>
<pre>
gmt psbasemap -Rg -Jks180/0.064c -Bafg -B+t&quot;Eckert VI&quot; &gt; eckert6.ps
</pre>
<h3>Robinson</h3>
<p> Projection designed to make global maps &quot;look right&quot;. Set the central longitude and width, e.g., </p>
<pre>
gmt psbasemap -Rd -JN0/8i -Bafg -B+tRobinson &gt; robinson.ps
</pre>
<h3>Winkel Tripel</h3>
<p> Yet another projection typically used for global maps only. You can set the central longitude, e.g., </p>
<pre>
gmt psbasemap -R90/450/-90/90 -JR270/25c -Bafg -B+t&quot;Winkel Tripel&quot; &gt; winkel.ps
</pre>
<h3>Mollweide [equal-area]</h3>
<p> The Mollweide projection is also mostly used for global maps and thus the spherical form is used. To get a 25-cm-wide world map centered on the Dateline: </p>
<pre>
psbasemap -Rg -JW180/25c -Bafg -B+tMollweide &gt; mollweide.ps
</pre>
<h3>Van der Grinten</h3>
<p> The Van der Grinten projection is also mostly used for global maps and thus the spherical form is used. To get a 18-cm-wide world map centered on the Dateline: </p>
<pre>
gmt psbasemap -Rg -JV180/18c -Bafg -B+t&quot;Van der Grinten&quot; &gt; grinten.ps
</pre>
<h2>CUSTOM LABELS OR INTERVALS</h2>
<p> The <code>-B</code> option sets up a regular annotation interval and the annotations derive from the corresponding <i>x</i>, <i>y</i>, or <i>z</i> coordinates. However, some applications requires special control on which annotations to plot and even replace the annotation with other labels. This is achieved by using <code>c</code><i>intfile</i> in the <code>-B</code> option, where <i>intfile</i> contains all the information about annotations, ticks, and even gridlines. Each record is of the form <i>coord</i> <i>type</i> [<i>label</i>], where <i>coord</i> is the coordinate for this annotation (or tick or gridline), <i>type</i> is one or more letters from <code>a</code> (annotation), <code>i</code> interval annotation, <code>f</code> tickmark, and <code>g</code> gridline. Note that <code>a</code> and <code>i</code> are mutually exclusive and cannot both appear in the same <i>intfile</i>. Both <code>a</code> and <code>i</code> requires you to supply a <i>label</i> which is used as the plot annotation. If not given then a regular formatted annotation based on the coordinate will occur.</p>
<h2>RESTRICTIONS</h2>
<p> For some projections, a spherical earth is implicitly assumed. A warning will notify the user if <code>-V</code> is set.</p>
<h2>BUGS</h2>
<p> The <code>-B</code> option is somewhat complicated to explain and comprehend. However, it is fairly simple for most applications (see examples).</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtcolors</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
