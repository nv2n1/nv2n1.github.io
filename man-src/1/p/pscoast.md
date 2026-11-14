---
title: "pscoast(1)"
name: "pscoast"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pscoast/"
description: "pscoast – Plot continents, shorelines, rivers, and borders on maps"
---

<h2>NAME</h2>
<p> pscoast &#8211; Plot continents, shorelines, rivers, and borders on maps</p>
<h2>SYNOPSIS</h2>
<p> <code>pscoast</code> <i>parameters</i> <i>region</i> [ <i>area</i> ] [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ [<code>l</code>|<code>r</code>/]<i>fill</i> ] [ <i>resolution</i>[<code>+</code>] ] [ <i>dcw</i> ] [ <i>box</i> ] [ <i>fill</i>|<code>c</code> ] [ <i>river</i>[/<i>pen</i>] ] [ <code>z</code>|<code>Z</code><i>parameters</i> ] [ ] [ <i>ruler</i> ] [ ] [ <i>border</i>[/<i>pen</i>] ] [ ] [ ] [ ] [ <i>fill</i>|<code>c</code> ] [ <i>rose</i> ] [ <i>mag_rose</i> ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ [<i>level</i>/]<i>pen</i> ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-bo</code><i>&lt;binary&gt;</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>pscoast</code> plots grayshaded, colored, or textured land-masses [or water-masses] on maps and [optionally] draws coastlines, rivers, and political boundaries. Alternatively, it can (1) issue clip paths that will contain all land or all water areas, or (2) dump the data to an ASCII table. The data files come in 5 different resolutions: (<code>f</code>)ull, (<code>h</code>)igh, (<code>i</code>)ntermediate, (<code>l</code>)ow, and (<code>c</code>)rude. The full resolution files amount to more than 55 Mb of data and provide great detail; for maps of larger geographical extent it is more economical to use one of the other resolutions. If the user selects to paint the land-areas and does not specify fill of water-areas then the latter will be transparent (i.e., earlier graphics drawn in those areas will not be overwritten). Likewise, if the water-areas are painted and no land fill is set then the land-areas will be transparent. A map projection must be supplied. The PostScript code is written to standard output.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i></dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>min_area</i>[/<i>min_level</i>/<i>max_level</i>][<code>+ag</code>|<code>i</code>|<code>s</code>|<code>S</code>][<code>+r</code>|<code>l</code>][<code>+p</code><i>percent</i>]</p>
<dd> Features with an area smaller than <i>min_area</i> in km^2 or of hierarchical level that is lower than <i>min_level</i> or higher than <i>max_level</i> will not be plotted [Default is 0/0/4 (all features)]. Level 2 (lakes) contains regular lakes and wide river bodies which we normally include as lakes; append <code>+r</code> to just get river-lakes or <code>+l</code> to just get regular lakes. By default (<code>+ai</code>) we select the ice shelf boundary as the coastline for Antarctica; append <code>+ag</code> to instead select the ice grounding line as coastline. For expert users who wish to print their own Antarctica coastline and islands via <i>psxy</i> you can use <code>+as</code> to skip all GSHHG features below 60S or <code>+aS</code> to instead skip all features north of 60S. Finally, append <code>+p</code><i>percent</i> to exclude polygons whose percentage area of the corresponding full-resolution feature is less than <i>percent</i>. See GSHHG INFORMATION below for more details.</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code>[<code>l</code>|<code>r</code>/]<i>fill</i></p>
<dd> Set the shade, color, or pattern for lakes and river-lakes [Default is the fill chosen for &quot;wet&quot; areas (<code>-S</code>)]. Optionally, specify separate fills by prepending <code>l/</code> for lakes and <code>r/</code> for river-lakes, repeating the <code>-C</code> option as needed.</p>
<dt><code>-D</code><i>resolution</i>[<code>+</code>]</p>
<dd> Selects the resolution of the data set to use ((<code>f</code>)ull, (<code>h</code>)igh, (<code>i</code>)ntermediate, (<code>l</code>)ow, and (<code>c</code>)rude). The resolution drops off by 80% between data sets [Default is <code>l</code>]. Append <code>+</code> to automatically select a lower resolution should the one requested not be available [abort if not found]. Alternatively, choose (<code>a</code>)uto to automatically select the best resolution given the chosen map scale.</p>
<dt><code>-E</code><i>code1,code2,&#8230;</i>[<code>+l</code>|<code>L</code>][<code>+g</code><i>fill</i>][<code>+p</code><i>pen</i>][<code>+r</code>|<code>R</code>[<i>incs</i>]]</p>
<dd> Select painting or dumping country polygons from the Digital Chart of the World. This is another dataset independent of GSHHG and hence the <code>-A</code> and <code>-D</code> options do not apply. Append one or more comma-separated countries using the 2-character ISO 3166-1 alpha-2 convention. To select a state of a country (if available), append .state, e.g, US.TX for Texas. To specify a whole continent, prepend = to any of the continent codes AF (Africa), AN (Antarctica), AS (Asia), EU (Europe), OC (Oceania), NA (North America), or SA (South America). Append <code>+l</code> to just list the countries and their codes [no data extraction or plotting takes place]. Use <code>+L</code> to see states/territories for Argentina, Australia, Brazil, Canada, and the US. Use <code>+r</code> to obtain the bounding box coordinates from the polygon(s). Append <i>inc</i>, <i>xinc</i>/<i>yinc</i>, or <i>winc</i>/<i>einc</i>/<i>sinc</i>/<i>ninc</i> to adjust the region to be a multiple of these steps [no adjustment]. Use <code>+R</code> to extend the region outward by adding these increments instead [no extension]. Append <code>+p</code><i>pen</i> to draw polygon outlines [no outline] and <code>+g</code><i>fill</i> to fill them [no fill]. One of <code>+p</code>|<code>g</code> must be specified unless <code>+r</code>, <code>+R</code>, or <code>-M</code> is in effect, and only one <code>-E</code> option can be given. You may repeat <code>-E</code> to give different groups of items separate pen/fill settings. If modifiers <code>+r</code> or <code>+R</code> are used and neither <code>-J</code> nor <code>-M</code> is set then we just print the <code>-R</code><i>wesn</i> string.</p>
<dt><code>-F</code>[<code>+c</code><i>clearances</i>][<code>+g</code><i>fill</i>][<code>+i</code>[[<i>gap</i>/]<i>pen</i>]][<code>+p</code>[<i>pen</i>]][<code>+r</code>[<i>radius</i>]][<code>+s</code>[[<i>dx</i>/<i>dy</i>/][<i>shade</i>]]]</p>
<dd> Without further options, draws a rectangular border around the map scale or rose using <i>MAP_FRAME_PEN</i>; specify a different pen with <code>+p</code><i>pen</i>. Add <code>+g</code><i>fill</i> to fill the logo box [no fill]. Append <code>+c</code><i>clearance</i> where <i>clearance</i> is either <i>gap</i>, <i>xgap</i>/<i>ygap</i>, or <i>lgap</i>/<i>rgap</i>/<i>bgap</i>/<i>tgap</i> where these items are uniform, separate in x- and y-direction, or individual side spacings between logo and border. Append <code>+i</code> to draw a secondary, inner border as well. We use a uniform <i>gap</i> between borders of 2<code>p</code> and the <i>MAP_DEFAULT_PEN</i> unless other values are specified. Append <code>+r</code> to draw rounded rectangular borders instead, with a 6<code>p</code> corner radius. You can override this radius by appending another value. Finally, append <code>+s</code> to draw an offset background shaded region. Here, <i>dx</i>/<i>dy</i> indicates the shift relative to the foreground frame [4<code>p</code>/-4<code>p</code>] and <i>shade</i> sets the fill style to use for shading [gray50]. Requires <code>-L</code> or <code>-T</code>. If both <code>-L</code> or <code>-T</code>, you may repeat <code>-F</code> after each of these.</p>
<dt><code>-G</code><i>fill</i>|<code>c</code></p>
<dd> Select filling or clipping of &quot;dry&quot; areas. Append the shade, color, or pattern; or use <code>-Gc</code> for clipping [Default is no fill].</p>
<dt><code>-I</code><i>river</i>[/<i>pen</i>]</p>
<dd> Draw rivers. Specify the type of rivers and [optionally] append pen attributes [Default pen: width = default, color = black, style = solid]. </p>
<p> Choose from the list of river types below; repeat option <code>-I</code> as often as necessary. </p>
<p> 0 = Double-lined rivers (river-lakes) </p>
<p> 1 = Permanent major rivers </p>
<p> 2 = Additional major rivers </p>
<p> 3 = Additional rivers </p>
<p> 4 = Minor rivers </p>
<p> 5 = Intermittent rivers &#8211; major </p>
<p> 6 = Intermittent rivers &#8211; additional </p>
<p> 7 = Intermittent rivers &#8211; minor </p>
<p> 8 = Major canals </p>
<p> 9 = Minor canals </p>
<p> 10 = Irrigation canals </p>
<p> You can also choose from several preconfigured river groups: </p>
<p> a = All rivers and canals (0-10) </p>
<p> A = All rivers and canals except river-lakes (1-10) </p>
<p> r = All permanent rivers (0-4) </p>
<p> R = All permanent rivers except river-lakes (1-4) </p>
<p> i = All intermittent rivers (5-7) </p>
<p> c = All canals (8-10)</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code>[<code>g</code>|<code>j</code>|<code>J</code>|<code>n</code>|<code>x</code>]<i>refpoint</i><code>+c</code>[<i>slon</i>/]<i>slat</i><code>+w</code><i>length</i>[<code>e</code>|<code>f</code>|<code>k</code>|<code>M</code>|<code>n</code>|<code>u</code>][<code>+a</code><i>align</i>][<code>+f</code>][<code>+l</code>[<i>label</i>]][<code>+u</code>]</p>
<dd> Draws a simple map scale centered on the reference point specified using one of four coordinate systems: (1) Use <code>-Dg</code> for map (user) coordinates, (2) use <code>-Dj</code> or <code>-DJ</code> for setting <i>refpoint</i> via a 2-char justification code that refers to the (invisible) map domain rectangle, (3) use <code>-Dn</code> for normalized (0-1) coordinates, or (4) use <code>-Dx</code> for plot coordinates (inches, cm, etc.). Scale is calculated for latitude <i>slat</i> (optionally supply longitude <i>slon</i> for oblique projections [Default is central meridian]), <i>length</i> is in km, or append unit from <code>e</code>|<code>f</code>|<code>k</code>|<code>M</code>|<code>n</code>|<code>u</code>. Change the label alignment with <code>+a</code><i>align</i> (choose among <code>l</code>(eft), <code>r</code>(ight), <code>t</code>(op), and <code>b</code>(ottom)). Append <code>+f</code> to get a &quot;fancy&quot; scale [Default is plain]. Append <code>+l</code> to select the default label, which equals the distance unit (meter, foot, km, mile, nautical mile, US survey foot) and is justified on top of the scale [t]. Change this by giving your own label (append <code>+l</code><i>label</i>). Select <code>+u</code> to append the unit to all distance annotations along the scale (for the plain scale, <code>+u</code> will instead select the unit to be appended to the distance length). Note: Use <i>FONT_LABEL</i> to change the label font and <i>FONT_ANNOT_PRIMARY</i> to change the annotation font. The height of the map scale is controlled by <i>MAP_SCALE_HEIGHT</i>, and the pen thickness is set by <i>MAP_TICK_PEN_PRIMARY</i>. See <code>-F</code> on how to place a panel behind the scale.</p>
<dt><code>-M</code></p>
<dd> Dumps a single multisegment ASCII (or binary, see <code>-bo</code>) file to standard output. No plotting occurs. Specify one of <code>-E</code>, <code>-I</code>, <code>-N</code> or <code>-W</code>. Note: if <code>-M</code> is used with <code>-E</code> then <code>-R</code> or the <code>+r</code> modifier to <code>-E</code> are not required as we automatically determine the region given the selected geographic entities.</p>
<dt><code>-N</code><i>border</i>[/<i>pen</i>]</p>
<dd> Draw political boundaries. Specify the type of boundary and [optionally] append pen attributes [Default pen: width = default, color = black, style = solid]. </p>
<p> Choose from the list of boundaries below. Repeat option <code>-N</code> as often as necessary. </p>
<p> 1 = National boundaries </p>
<p> 2 = State boundaries within the Americas </p>
<p> 3 = Marine boundaries </p>
<p> a = All boundaries (1-3)</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code></p>
<dd> Mark end of existing clip path. No projection information is needed. Also supply <code>-X</code> and <code>-Y</code> settings if you have moved since the clip started.</p>
<dt><code>-S</code><i>fill</i>|<code>c</code></p>
<dd> Select filling or clipping of &quot;wet&quot; areas. Append the shade, color, or pattern; or use <code>-Sc</code> for clipping [Default is no fill].</p>
<dt><code>-Td</code>[<code>g</code>|<code>j</code>|<code>J</code>|<code>n</code>|<code>x</code>]<i>refpoint</i><code>+w</code><i>width</i>[<code>+f</code>[<i>level</i>]][<code>+j</code><i>justify</i>][<code>+l</code><i>w,e,s,n</i>][<code>+o</code><i>dx</i>[/<i>dy</i>]]</p>
<dd> <code>-Td</code> draws a map directional rose on the map at the location defined by the reference and anchor points: Give the reference point on the map for the rose using one of four coordinate systems: (1) Use <code>g</code> for map (user) coordinates, (2) use <code>j</code> for setting <i>refpoint</i> via a 2-char justification code that refers to the (invisible) map domain rectangle, (3) use <code>n</code> for normalized (0-1) coordinates, or (4) use <code>x</code> for plot coordinates (inches, cm, etc.) [Default]. You can offset the reference point by <i>dx</i>/<i>dy</i> in the direction implied by <i>justify</i>. By default, the anchor point on the scale is assumed to be the center of the rose (MC), but this can be changed by appending <code>+j</code> followed by a 2-char justification code <i>justify</i> (see <code>pstext</code>). Note: If <code>-Dj</code> is used then <i>justify</i> defaults to the same as <i>refpoint</i>, if <code>-DJ</code> is used then <i>justify</i> defaults to the mirror opposite of <i>refpoint</i>. Add <code>+o</code> to offset the color scale by <i>dx</i>/<i>dy</i> away from the <i>refpoint</i> point in the direction implied by <i>justify</i> (or the direction implied by <code>-Dj</code> or <code>-DJ</code>). Append <code>+w</code><i>width</i>to set the width of the rose in plot coordinates (inches, cm, etc.). Add <code>+f</code> to get a &quot;fancy&quot; rose, and specify in <i>level</i> what you want drawn. The default [1] draws the two principal E-W, N-S orientations, 2 adds the two intermediate NW-SE and NE-SW orientations, while 3 adds the eight minor orientations WNW-ESE, NNW-SSE, NNE-SSW, and ENE-WSW. Label the cardinal points W,E,S,N by adding <code>+l</code> and append your own four comma-separated strings to override the default. See <code>-F</code> on how to place a panel behind the scale. </p>
<p> <code>-Tm</code>[<code>g</code>|<code>j</code>|<code>J</code>|<code>n</code>|<code>x</code>]<i>refpoint</i><code>+w</code><i>width</i>[<code>+d</code><i>dec</i>[/<i>dlabel</i>]]][<code>+i</code><i>pen</i>][<code>+j</code><i>justify</i>][<code>+l</code><i>w,e,s,n</i>][<code>+p</code><i>pen</i>][<code>+t</code><i>ints</i>][<code>+o</code><i>dx</i>[/<i>dy</i>]] <code>-Tm</code> draws a map magnetic rose on the map at the location defined by the reference and anchor points: Give the reference point on the map for the rose using one of four coordinate systems: (1) Use <code>g</code> for map (user) coordinates, (2) use <code>j</code> for setting <i>refpoint</i> via a 2-char justification code that refers to the (invisible) map domain rectangle, (3) use <code>n</code> for normalized (0-1) coordinates, or (4) use <code>x</code> for plot coordinates (inches, cm, etc.) [Default]. You can offset the reference point by <i>dx</i>/<i>dy</i> in the direction implied by <i>justify</i>. By default, the anchor point on the scale is assumed to be the center of the rose (MC), but this can be changed by appending <code>+j</code> followed by a 2-char justification code <i>justify</i> (see <code>pstext</code>). Note: If <code>-Dj</code> is used then <i>justify</i> defaults to the same as <i>refpoint</i>, if <code>-DJ</code> is used then <i>justify</i> defaults to the mirror opposite of <i>refpoint</i>. Add <code>+o</code> to offset the color scale by <i>dx</i>/<i>dy</i> away from the <i>refpoint</i> point in the direction implied by <i>justify</i> (or the direction implied by <code>-Dj</code> or <code>-DJ</code>). Append <code>+w</code><i>width</i>to set the width of the rose in plot coordinates (inches, cm, etc.). Use <code>+d</code> to assign the magnetic declination and set <i>dlabel</i>, which is a label for the magnetic compass needle (Leave empty to format a label from <i>dec</i>, or give &#8211; to bypass labeling). With <code>+d</code>, both directions to geographic and magnetic north are plotted [Default is geographic only]. If the north label is <code>*</code> then a north star is plotted instead of the north label. Annotation and two levels of tick intervals for both geographic and magnetic directions are 30/5/1 degrees; override these settings by appending <code>+t</code><i>ints</i>, and append six intervals to set both the geographic and magnetic intervals. Number GMT default parameters control pens, fonts, and color; see the Map Embellishment section in the Cookbook. See <code>-F</code> on how to place a panel behind the scale.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<i>level</i>/]<i>pen</i> <i>(more &#8230;)</i></p>
<dd> Draw shorelines [Default is no shorelines]. Append pen attributes [Defaults: width = default, color = black, style = solid] which apply to all four levels. To set the pen for each level differently, prepend <i>level</i>/, where <i>level</i> is 1-4 and represent coastline, lakeshore, island-in-lake shore, and lake-in-island-in-lake shore. Repeat <code>-W</code> as needed. When specific level pens are set, those not listed will not be drawn [Default draws all levels; but see <code>-A</code>]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output.</p>
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
<h2>EXAMPLES</h2>
<p> To plot a green Africa with white outline on blue background, with permanent major rivers in thick blue pen, additional major rivers in thin blue pen, and national borders as dashed lines on a Mercator map at scale 0.1 inch/degree, use </p>
<pre>
gmt pscoast -R-30/30/-40/40 -Jm0.1i -B5 -I1/1p,blue -N1/0.25p,- \
            -I2/0.25p,blue -W0.25p,white -Ggreen -Sblue -P &gt; africa.ps
</pre>
<p> To plot Iceland using the lava pattern (# 28) at 100 dots per inch, on a Mercator map at scale 1 cm/degree, run </p>
<pre>
gmt pscoast -R-30/-10/60/65 -Jm1c -B5 -Gp100/28 &gt; iceland.ps
</pre>
<p> To initiate a clip path for Africa so that the subsequent colorimage of gridded topography is only seen over land, using a Mercator map at scale 0.1 inch/degree, use </p>
<pre>
gmt pscoast  -R-30/30/-40/40 -Jm0.1i -B5 -Gc -P -K &gt; africa.ps
gmt grdimage -Jm0.1i etopo5.nc -Ccolors.cpt -O -K &gt;&gt; africa.ps
gmt pscoast  -Q -O &gt;&gt; africa.ps
</pre>
<p> To plot Great Britain, Italy, and France in blue with a red outline and Spain, Portugal and Greece in yellow (no outline), and pick up the plot domain form the extents of these countries, use </p>
<pre>
gmt pscoast  -JM6i -P -Baf -EGB,IT,FR+gblue+p0.25p,red+r -EES,PT,GR+gyellow &gt; map.ps
</pre>
<p> To extract a high-resolution coastline data table for Iceland to be used in your analysis, try </p>
<pre>
gmt pscoast -R-26/-12/62/68 -Dh -W -M &gt; iceland.txt
</pre>
<p> <code>pscoast</code> will first look for coastline files in directory <code>$GMT_SHAREDIR</code>/coast If the desired file is not found, it will look for the file <code>$GMT_SHAREDIR</code>/coastline.conf. This file may contain any number of records that each holds the full pathname of an alternative directory. Comment lines (#) and blank lines are allowed. The desired file is then sought for in the alternate directories.</p>
<h2>GSHHS INFORMATION</h2>
<p> The coastline database is GSHHG (formerly GSHHS) which is compiled from three sources: World Vector Shorelines (WVS), CIA World Data Bank II (WDBII), and Atlas of the Cryosphere (AC, for Antarctica only). Apart from Antarctica, all level-1 polygons (ocean-land boundary) are derived from the more accurate WVS while all higher level polygons (level 2-4, representing land/lake, lake/island-in-lake, and island-in-lake/lake-in-island-in-lake boundaries) are taken from WDBII. The Antarctica coastlines come in two flavors: ice-front or grounding line, selectable via the <code>-A</code> option. Much processing has taken place to convert WVS, WDBII, and AC data into usable form for GMT: assembling closed polygons from line segments, checking for duplicates, and correcting for crossings between polygons. The area of each polygon has been determined so that the user may choose not to draw features smaller than a minimum area (see <code>-A</code>); one may also limit the highest hierarchical level of polygons to be included (4 is the maximum). The 4 lower-resolution databases were derived from the full resolution database using the Douglas-Peucker line-simplification algorithm. The classification of rivers and borders follow that of the WDBII. See the GMT Cookbook and Technical Reference Appendix K for further details.</p>
<h2>BUGS</h2>
<p> The options to fill (<code>-C</code> <code>-G</code> <code>-S</code>) may not always work if the Azimuthal equidistant projection is chosen (<code>-Je</code>|<code>E</code>). If the antipole of the projection is in the oceans it will most likely work. If not, try to avoid using projection center coordinates that are even multiples of the coastline bin size (1, 2, 5, 10, and 20 degrees for <code>f</code>, <code>h</code>, <code>i</code>, <code>l</code>, <code>c</code>, respectively). This projection is not supported for clipping. </p>
<p> The political borders are for the most part 1970s-style but have been updated to reflect more recent border rearrangements in Europe and elsewhere. Let us know if you find something out of date. </p>
<p> The full-resolution coastlines are also from a digitizing effort in the 1970-80s and it is difficult to assess the accuracy. Users who zoom in close enough may find that the GSHHG coastline is not matching other data, e.g., satellite images, more recent coastline data, etc. We are aware of such mismatches but cannot undertake band-aid solutions each time this occurs. </p>
<p> Some users of <code>pscoast</code> will not be satisfied with what they find for the Antarctic shoreline. In Antarctica, the boundary between ice and ocean varies seasonally and inter-annually. There are some areas of permanent shelf ice. In addition to these time-varying ice-ocean boundaries, there are also shelf ice grounding lines where ice goes from floating on the sea to sitting on land, and lines delimiting areas of rock outcrop. For consistency&#8217;s sake, we have used the World Vector Shoreline throughout the world in <code>pscoast</code>, as described in the GMT Cookbook Appendix K. Users who need specific boundaries in Antarctica should get the Antarctic Digital Database, prepared by the British Antarctic Survey, Scott Polar Research Institute, World Conservation Monitoring Centre, under the auspices of the Scientific Committee on Antarctic Research. This data base contains various kinds of limiting lines for Antarctica and is available on CD-ROM. It is published by the Scientific Committee on Antarctic Research, Scott Polar Research Institute, Lensfield Road, Cambridge CB2 1ER, United Kingdom.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtcolors</code>, <code>grdlandmask</code>, <code>psbasemap</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
