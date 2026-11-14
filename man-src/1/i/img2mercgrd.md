---
title: "img2mercgrd(1)"
name: "img2mercgrd"
section: "1"
letter: "i"
url: "/docs/linux/man/1-img2mercgrd/"
description: "img2mercgrd – Extract region of img, preserving Mercator, save as grd"
---

<h2>NAME</h2>
<p> img2mercgrd &#8211; Extract region of img, preserving Mercator, save as grd</p>
<h2>SYNOPSIS</h2>
<p> <code>img2mercgrd</code> <i>imgfile</i> <code>-G</code><i>grdfile</i> <code>-R</code><i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[<code>r</code>] <code>-T</code><i>type</i> [ <code>-C</code> ] [ <code>-D</code><i>minlat/maxlat</i> ] [ <code>-N</code><i>navg</i> ] [ <code>-S</code><i>scale</i> ] [ <code>-V</code> ] [ <code>-W</code><i>maxlon</i> ] [ <code>-m</code><i>minutes</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>img2mercgrd</code> reads an img format file and creates a grid file. The Spherical Mercator projection of the img file is preserved, so that the region <code>-R</code> set by the user is modified slightly; the modified region corresponds to the edges of pixels [or groups of <i>navg</i> pixels]. The grid file header is set so that the x and y axis lengths represent distance from the west and south edges of the image, measured in user default units, with <code>-Jm</code>1 and the adjusted <code>-R</code>. By setting the default <code>ELLIPSOID</code> = Sphere, the user can make overlays with the adjusted <code>-R</code> so that they match. See <code>EXAMPLES</code> below. The adjusted <code>-R</code> is also written in the grdheader remark, so it can be found later. The <code>-T</code><i>type</i> selects all data or only data at constrained pixels, and can be used to create a grid of 1s and 0s indicating constraint locations. The output grid file is pixel registered; it inherits this from the img file.</p>
<dl>
<dt><i>imgfile</i></p>
<dd> An img format file such as the marine gravity or seafloor topography fields estimated from satellite altimeter data by Sandwell and Smith. If the user has set an environment variable <code>$GMT_IMGDIR</code>, then <code>img2mercgrd</code> will try to find <i>imgfile</i> in <code>$GMT_IMGDIR</code>; else it will try to open <i>imgfile</i> directly.</p>
<dt><code>-G</code></p>
<dd> <i>grdfile</i> is the name of the output grid file.</p>
<dt><code>-R</code></p>
<dd> <i>west, east, south,</i> and <i>north</i> specify the Region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid.</p>
<dt><code>-T</code></p>
<dd> <i>type</i> handles the encoding of constraint information. <i>type</i> = 0 indicates that no such information is encoded in the img file (used for pre-1995 versions of the gravity data; all more recent files do not support this choice) and gets all data. <i>type</i> &gt; 0 indicates that constraint information is encoded (1995 and later (current) versions of the img files) so that one may produce a grid file as follows: <code>-T</code><i>1</i> gets data values at all points, <code>-T</code><i>2</i> gets data values at constrained points and NaN at interpolated points; <code>-T</code><i>3</i> gets 1 at constrained points and 0 at interpolated points.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code></p>
<dd> Set the x and y Mercator coordinates relative to projection center (lon = lat = 0) [Default is relative to lower left corner of grid].</p>
<dt><code>-D</code></p>
<dd> Use the extended latitude range -80.738/+80.738. Alternatively, append <i>minlat/maxlat</i> as the latitude extent of the input img file. [Default is -72.006/72.006].</p>
<dt><code>-N</code></p>
<dd> Average the values in the input img pixels into <i>navg</i> by <i>navg</i> squares, and create one output pixel for each such square. If used with <code>-T</code><i>3</i> it will report an average constraint between 0 and 1. If used with <code>-T</code><i>2</i> the output will be average data value or NaN according to whether average constraint is &gt; 0.5. <i>navg</i> must evenly divide into the dimensions of the imgfile in pixels. [Default <i>1</i> does no averaging].</p>
<dt><code>-S</code></p>
<dd> Multiply the img file values by <i>scale</i> before storing in grid file. [Default is 1.0]. (img topo files are stored in (corrected) meters; gravity files in mGal*10; vertical deflection files in microradians*10, vertical gravity gradient files in Eotvos*10. Use <code>-S</code>0.1 for those files.)</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;]. Particularly recommended here, as it is helpful to see how the coordinates are adjusted.</p>
<dt><code>-m</code></p>
<dd> Indicate <i>minutes</i> as the width of an input img pixel in minutes of longitude. [Default is 2.0].</p>
<dt><code>-W</code></p>
<dd> Indicate <i>maxlon</i> as the maximum longitude extent of the input img file. Versions since 1995 have had <i>maxlon</i> = 360.0, while some earlier files had <i>maxlon</i> = 390.0. [Default is 360.0].</dl>
<h2>EXAMPLES</h2>
<p> To extract data in the region <code>-R</code>-40/40/-70/-30 from <i>world_grav.img.7.2</i>, run </p>
<p> <code>img2mercgrd</code> world_grav.img.7.2 <code>-G</code>merc_grav.grd <code>-R</code>-40/40/-70/-30 <code>-T</code>1 <code>-V</code> </p>
<p> Note that the <code>-V</code> option tells us that the range was adjusted to <code>-R</code>-40/40/-70.0004681551/-29.9945810754. We can also use <code>grdinfo</code> to find that the grid file header shows its region to be <code>-R</code>0/80/0/67.9666667 This is the range of x,y we will get from a Spherical Mercator projection using <code>-R</code>-40/40/-70.0004681551/-29.9945810754 and <code>-Jm</code>1. Thus, to take ship.lonlatgrav and use it to sample the merc_grav.grd, we can do this: </p>
<p> <code>gmtset</code> <code>ELLIPSOID</code> Sphere<br />
 <code>mapproject</code> <code>-R</code>-40/40/-70.0004681551/-29.9945810754 <code>-Jm</code>1 ship.lonlatgrav | <code>grdtrack</code> <code>-G</code>merc_grav.grd | <code>mapproject</code> <code>-R</code>-40/40/-70.0004681551/-29.9945810754 <code>-Jm</code>1 <code>-I</code> &gt; ship.lonlatgravsat </p>
<p> It is recommended to use the above method of projecting and unprojecting the data in such an application, because then there is only one interpolation step (in <code>grdtrack</code>). If one first tries to convert the grid file to lon,lat and then sample it, there are two interpolation steps (in conversion and in sampling). </p>
<p> To make a lon,lat grid from the above grid we can use </p>
<p> <code>grdproject</code> merc_grav.grd <code>-R</code>-40/40/-70.0004681551/-29.9945810754 <code>-Jm</code>1 <code>-I</code> <code>-F</code> <code>-D</code>2m <code>-G</code>grav.grd </p>
<p> In some cases this will not be easy as the <code>-R</code> in the two coordinate systems may not align well. When this happens, we can also use (in fact, it may be always better to use) </p>
<p> <code>grd2xyz</code> merc_grav.grd | <code>mapproject</code> <code>-R</code>-40/40/-70.0004681551/-29.994581075 <code>-Jm</code>1 <code>-I</code> | <code>surface</code> <code>-R</code>-40/40/-70/70 <code>-I</code>2m <code>-G</code>grav.grd </p>
<p> To make a Mercator map of the above region, suppose our .gmtdefaults4 <code>MEASURE_UNIT</code> is inch. Then since the above merc_grav.grd file is projected with <code>-Jm</code>1 it is 80 inches wide. We can make a map 8 inches wide by using <code>-Jx</code>0.1 on any map programs applied to this grid (e.g., <code>grdcontour</code>, <code>grdimage</code>, <code>grdview</code>), and then for overlays which work in lon,lat (e.g., <code>psxy</code>, <code>pscoast</code>) we can use the above adjusted <code>-R</code> and <code>-Jm</code>0.1 to get the two systems to match up. </p>
<p> However, we can be smarter than this. Realizing that the input img file had pixels 2.0 minutes wide (or checking the nx and ny with grdinfo merc_grav.grd) we realize that merc_grav.grd used the full resolution of the img file and it has 2400 by 2039 pixels, and at 8 inches wide this is 300 pixels per inch. We decide we don&#8217;t need that many and we will be satisfied with 100pixels per inch, so we want to average the data into 3 by 3 squares. (If we want a contour plot we will probably choose to average the data much more (e.g. 6 by 6) to get smooth contours.) Since 2039 isn&#8217;t divisible by 3 we will get a different adjusted OPT(R) this time:</p>
<p> <code>img2mercgrd</code> world_grav.img.7.2 <code>-G</code>merc_grav_2.grd <code>-R</code>-40/40/-70/-30 <code>-T</code>1 <code>-N</code>3 <code>-V</code> </p>
<p> This time we find the adjusted region is <code>-R</code>-40/40/-70.023256525/-29.9368261101 and the output is 800 by 601 pixels, a better size for us. Now we can create an artificial illumination file for this using <code>grdgradient</code>: </p>
<p> <code>grdgradient</code> merc_grav_2.grd <code>-G</code>illum.grd <code>-A</code>0/270 <code>-N</code>e0.6 </p>
<p> and if we also have a cpt file called &quot;grav.cpt&quot; we can create a color shaded relief map like this: </p>
<p> <code>grdimage</code> merc_grav_2.grd <code>-I</code>illum.grd <code>-C</code>grav.cpt <code>-Jx</code>0.1 <code>-K</code> &gt; map.ps<br />
 <code>psbasemap</code> <code>-R</code>-40/40/-70.023256525/-29.9368261101 <code>-Jm</code>0.1 <code>-B</code>a10 <code>-O</code> &gt;&gt; map.ps </p>
<p> Suppose you want to obtain only the constrained data values from an img file, in lat/lon coordinates. Then run <code>img2mercgrd</code> with the <code>-T</code>2 option, use <code>grd2xyz</code> to dump the values, pipe through grep -v NaN to eliminate NaNs, and pipe through <code>mapproject</code> with the inverse projection as above.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-grdproject/">grdproject</a></i>(1), <i><a href="/docs/linux/man/1-mapproject/">mapproject</a></i>(1) </p>
<h2>Index</h2>
