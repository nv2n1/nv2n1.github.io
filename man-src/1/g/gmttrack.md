---
title: "gmttrack(1)"
name: "gmttrack"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmttrack/"
description: "gmttrack – A shiptrack plotting program"
---

<h2>NAME</h2>
<p> gmttrack &#8211; A shiptrack plotting program</p>
<h2>SYNOPSIS</h2>
<p> <code>gmttrack</code> <i>leg-ids</i> <code>-R</code><i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[<code>r</code>] <code>-J</code><i>parameters</i> [ <code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> ] [ <code>-M</code><i>trackticks</i> ] [ <code>-W</code><i>pen</i>[<i>red/green/blue</i>][<code>OA</code>] ] [ <code>-A</code>[<i>size</i>] ] [ <code>-K</code> ] [ <code>-O</code> ] [ <code>-P</code> ] [ <code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ <code>-V</code> ] [ <code>-X</code>[<code>a</code>|<code>c</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]] ] [ <code>-Y</code>[<code>a</code>|<code>c</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] ] [ <code>-c</code><i>copies</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gmttrack</code> reads gmt cruises and creates <i>PostScript</i> code that will plot one or more ship tracks on a map using the specified projection. The <i>PostScript</i> code is written to standard output.</p>
<dl>
<dt><i>leg-ids</i></p>
<dd> Can be one or more gmtleg-names, like c2104 v3206 etc.</p>
<dt><code>-J</code></p>
<dd> Selects the map projection. Scale is UNIT/degree, 1:xxxxx, or width in UNIT (upper case modifier). UNIT is cm, inch, or m, depending on the <code>MEASURE_UNIT</code> setting in .gmtdefaults4, but this can be overridden on the command line by appending <code>c</code>, <code>i</code>, or <code>m</code> to the scale/width value. When central meridian is optional, default is center of longitude range on <code>-R</code> option. Default standard parallel is the equator. For map height, max dimension, or min dimension, append <code>h</code>, <code>+</code>, or <code>&#8211;</code> to the width, respectively.<br />
 More details can be found in the <code>psbasemap</code> man pages. </p>
<p> <code>CYLINDRICAL PROJECTIONS:</code> </p>
<p> <code>-Jc</code><i>lon0/lat0/scale</i> (Cassini)<br />
 <code>-Jcyl_stere</code>/[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> (Cylindrical Stereographic)<br />
 <code>-Jj</code>[<i>lon0/</i>]<i>scale</i> (Miller)<br />
 <code>-Jm</code>[<i>lon0</i>/[<i>lat0/</i>]]<i>scale</i> (Mercator)<br />
 <code>-Jm</code><i>lon0/lat0/scale</i> (Mercator &#8211; Give meridian and standard parallel)<br />
 <code>-Jo</code>[<code>a</code>]<i>lon0/lat0/azimuth/scale</i> (Oblique Mercator &#8211; point and azimuth)<br />
 <code>-Jo</code>[<code>b</code>]<i>lon0/lat0/lon1/lat1/scale</i> (Oblique Mercator &#8211; two points)<br />
 <code>-Joc</code><i>lon0/lat0/lonp/latp/scale</i> (Oblique Mercator &#8211; point and pole)<br />
 <code>-Jq</code>[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> (Cylindrical Equidistant)<br />
 <code>-Jt</code><i>lon0/</i>[<i>lat0/</i>]<i>scale</i> (TM &#8211; Transverse Mercator)<br />
 <code>-Ju</code><i>zone/scale</i> (UTM &#8211; Universal Transverse Mercator)<br />
 <code>-Jy</code>[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> (Cylindrical Equal-Area) </p>
<p> <code>CONIC PROJECTIONS:</code> </p>
<p> <code>-Jb</code><i>lon0/lat0/lat1/lat2/scale</i> (Albers)<br />
 <code>-Jd</code><i>lon0/lat0/lat1/lat2/scale</i> (Conic Equidistant)<br />
 <code>-Jl</code><i>lon0/lat0/lat1/lat2/scale</i> (Lambert Conic Conformal)<br />
 <code>-Jpoly</code>/[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> ((American) Polyconic) </p>
<p> <code>AZIMUTHAL PROJECTIONS:</code> </p>
<p> <code>-Ja</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> (Lambert Azimuthal Equal-Area)<br />
 <code>-Je</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> (Azimuthal Equidistant)<br />
 <code>-Jf</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> (Gnomonic)<br />
 <code>-Jg</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> (Orthographic)<br />
 <code>-Jg</code><i>lon0/lat0/altitude/azimuth/tilt/twist/Width/Height/scale</i> (General Perspective).<br />
 <code>-Js</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> (General Stereographic) </p>
<p> <code>MISCELLANEOUS PROJECTIONS:</code> </p>
<p> <code>-Jh</code>[<i>lon0/</i>]<i>scale</i> (Hammer)<br />
 <code>-Ji</code>[<i>lon0/</i>]<i>scale</i> (Sinusoidal)<br />
 <code>-Jkf</code>[<i>lon0/</i>]<i>scale</i> (Eckert IV)<br />
 <code>-Jk</code>[<code>s</code>][<i>lon0/</i>]<i>scale</i> (Eckert IV)<br />
 <code>-Jn</code>[<i>lon0/</i>]<i>scale</i> (Robinson)<br />
 <code>-Jr</code>[<i>lon0/</i>]<i>scale</i> (Winkel Tripel)<br />
 <code>-Jv</code>[<i>lon0/</i>]<i>scale</i> (Van der Grinten)<br />
 <code>-Jw</code>[<i>lon0/</i>]<i>scale</i> (Mollweide) </p>
<p> <code>NON-GEOGRAPHICAL PROJECTIONS:</code> </p>
<p> <code>-Jp</code>[<code>a</code>]<i>scale</i>[<i>/origin</i>][<code>r</code>|<code>z</code>] (Polar coordinates (theta,r))<br />
 <code>-Jx</code><i>x-scale</i>[<code>d</code>|<code>l</code>|<code>p</code><i>pow</i>|<code>t</code>|<code>T</code>][<i>/y-scale</i>[<code>d</code>|<code>l</code>|<code>p</code><i>pow</i>|<code>t</code>|<code>T</code>]] (Linear, log, and power scaling) </p>
<dt><code>-R</code></p>
<dd> <i>west, east, south,</i> and <i>north</i> specify the Region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid.</dl>
<h2>OPTIONS</h2>
<p> No space between the option flag and the associated arguments.</p>
<dl>
<dt><code>-B</code></p>
<dd> Sets map boundary annotation and tickmark intervals; see the <code>psbasemap</code> man page for all the details.</p>
<dt><code>-A</code></p>
<dd> Annotate each leg every time it enters the plot. Optional <i>size</i> is character size in points.</p>
<dt><code>-Da</code></p>
<dd> Do not plot data collected before <i>startdate</i> (mm/dd/yyyy/hh:mm) [Default is first day].</p>
<dt><code>-Db</code></p>
<dd> Do not plot data collected after <i>stopdate</i> (mm/dd/yyyy/hh:mm). [Default is last day].</p>
<dt><code>-K</code></p>
<dd> More <i>PostScript</i> code will be appended later [Default terminates the plot system].</p>
<dt><code>-M</code></p>
<dd> To put time/distance Marks on the track. E.g. <code>a</code>500<code>ka</code>24<code>ht</code>6<code>h</code> means (<code>a</code>)nnotate every 500 km (<code>k</code>) and 24 <code>h</code>(ours), with (<code>t</code>)ickmarks every 500 km and 6 hours.</p>
<dt><code>-O</code></p>
<dd> Selects Overlay plot mode [Default initializes a new plot system].</p>
<dt><code>-P</code></p>
<dd> Selects Portrait plotting mode [Default is Landscape, see <code>gmtdefaults</code> to change this].</p>
<dt><code>-Sa</code></p>
<dd> Do not plot data that are less than <i>startdist</i> km along track from port of departure. [Default is 0].</p>
<dt><code>-Sb</code></p>
<dd> Do not plot data that are more than <i>stopdist</i> km along track from port of departure. [Default is length of track].</p>
<dt><code>-U</code></p>
<dd> Draw Unix System time stamp on plot. By adding <i>just/dx/dy/</i>, the user may specify the justification of the stamp and where the stamp should fall on the page relative to lower left corner of the plot. For example, BL/0/0 will align the lower left corner of the time stamp with the lower left corner of the plot. Optionally, append a <i>label</i>, or <code>c</code> (which will plot the command string.). The <code>GMT</code> parameters <code>UNIX_TIME</code>, <code>UNIX_TIME_POS</code>, and <code>UNIX_TIME_FORMAT</code> can affect the appearance; see the <code>gmtdefaults</code> man page for details. The time string will be in the locale set by the environment variable <code>TZ</code> (generally local time).</p>
<dt><code>-W</code></p>
<dd> <i>pen</i> is thickness of the trackline. [Default is 1]. Optionally, specify the rgb combination to obtain a colored trackline [Default is black]. Append <code>o</code> for d<code>o</code>tted line, <code>a</code> for d<code>a</code>shed. [Default is solid].</p>
<dt><code>-X</code> <code>-Y</code></p>
<dd> Shift plot origin relative to the current origin by (<i>x-shift,y-shift</i>) and optionally append the length unit (<code>c</code>, <code>i</code>, <code>m</code>, <code>p</code>). You can prepend <code>a</code> to shift the origin back to the original position after plotting, or prepend <code>r</code> [Default] to reset the current origin to the new location. If <code>-O</code> is used then the default (<i>x-shift,y-shift</i>) is (0,0), otherwise it is (r1i, r1i) or (r2.5c, r2.5c). Alternatively, give <code>c</code> to align the center coordinate (x or y) of the plot with the center of the page based on current page size.</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</p>
<dt><code>-c</code></p>
<dd> Specifies the number of plot copies. [Default is 1].</dl>
<h2>EXAMPLES</h2>
<p> To generate a Mercator plot of the track of cruises C2610 and V1512 in the area 150E to 154E, 18N to 23N, using a Mercator scale of 1.5inch/degree, label the tracks with 10 points characters, annotate the boundaries every degree, and draw gridlines every 30 minutes, and send the plot to the default printer, enter the following command: </p>
<p> <code>gmttrack</code> c2610 v1512 <code>-R</code>150/154/18/23 <code>-Jm</code>1.5 <code>-B</code>1<code>g</code>30<code>m -A</code>10 | lpr</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-psbasemap/">psbasemap</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P., and W. H. F. Smith, 2009, The Generic Mapping Tools (GMT) version 4.5.0 Technical Reference &amp; Cookbook, SOEST/NOAA.<br />
 Wessel, P., and W. H. F. Smith, 1998, New, Improved Version of Generic Mapping Tools Released, EOS Trans., AGU, 79 (47), p. 579.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, EOS Trans., AGU, 76 (33), p. 329.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, <a rel="nofollow" href="http://www.agu.org/eos_elec/95154e.html,">http://www.agu.org/eos_elec/95154e.html,</a> Copyright 1995 by the American Geophysical Union.<br />
 Wessel, P., and W. H. F. Smith, 1991, Free Software Helps Map and Display Data, EOS Trans., AGU, 72 (41), p. 441. </p>
<h2>Index</h2>
