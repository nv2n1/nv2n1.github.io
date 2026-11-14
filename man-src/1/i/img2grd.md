---
title: "img2grd(1)"
name: "img2grd"
section: "1"
letter: "i"
url: "/docs/linux/man/1-img2grd/"
description: "img2grd – Extract subset of img file in Mercator or Geographic format"
---

<h2>NAME</h2>
<p> img2grd &#8211; Extract subset of img file in Mercator or Geographic format</p>
<h2>SYNOPSIS</h2>
<p> <code>img2grd</code> <i>imgfile</i> <i>grdfile</i> <i>region</i> <i>type</i> [ ] [ [<i>minlat/maxlat</i>] ] [ ] [ <i>minutes</i> ] [ ] [ <i>navg</i> ] [ [<i>scale</i>] ] [ [<i>level</i>] ] [ <i>maxlon</i> ] [ <code>-n</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>img2grd</code> reads an img format file, extracts a subset, and writes it to a grid file. The <code>-M</code> option dictates whether or not the Spherical Mercator projection of the img file is preserved or if a Geographic grid should be written by undoing the Mercator projection. If geographic grid is selected you can also request a resampling onto the exact <code>-R</code> given.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>imgfile</i></p>
<dd> A Mercator img format file such as the marine gravity or seafloor topography fields estimated from satellite altimeter data by Sandwell and Smith. If the user has set an environment variable <code>$GMT_DATADIR</code>, then <code>img2grd</code> will try to find <i>imgfile</i> in <code>$GMT_DATADIR</code>; else it will try to open <i>imgfile</i> directly.</p>
<dt><code>-G</code><i>grdfile</i></p>
<dd> <i>grdfile</i> is the name of the output grid file.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-C</code></p>
<dd> Set the x and y Mercator coordinates relative to projection center [Default is relative to lower left corner of grid]. Requires <code>-M</code>.</p>
<dt><code>-D</code>[<i>minlat/maxlat</i>]</p>
<dd> Use the extended latitude range -80.738/+80.738. Alternatively, append <i>minlat/maxlat</i> as the latitude extent of the input img file. [Default is -72.006/72.006]. Not usually required since we can determine the extent from inspection of the file size.</p>
<dt><code>-E</code></p>
<dd> Can be used when <code>-M</code> is not set to force the final grid to have the exact same region as requested with <code>-R</code>. By default, the final region is a direct projection of the original Mercator region and will typically extend slightly beyond the requested latitude range, and furthermore the grid increment in latitude does not match the longitude increment. However, the extra resampling introduces small interpolation errors and should only be used if the output grid must match the requested region and have x_inc = y_inc. In this case the region set by <code>-R</code> must be given in multiples of the increment (.e.g, <code>-R</code>0/45/45/72).</p>
<dt><code>-I</code></p>
<dd> Indicate <i>minutes</i> as the width of an input img pixel in minutes of longitude. [Default is 2.0]. Not usually required since we can determine the pixel size from inspection of the size.</p>
<dt><code>-M</code></p>
<dd> Output a Spherical Mercator grid [Default is a geographic lon/lat grid]. The Spherical Mercator projection of the img file is preserved, so that the region <code>-R</code> set by the user is modified slightly; the modified region corresponds to the edges of pixels [or groups of <i>navg</i> pixels]. The grid file header is set so that the x and y axis lengths represent distance from the west and south edges of the image, measured in user default units, with <code>-Jm</code>1 and the adjusted <code>-R</code>. By setting the default <code>PROJ_ ELLIPSOID</code> = Sphere, the user can make overlays with the adjusted <code>-R</code> so that they match. See <code>EXAMPLES</code> below. The adjusted <code>-R</code> is also written in the grid header remark, so it can be found later. See <code>-C</code> to set coordinates relative to projection center.</p>
<dt><code>-N</code><i>navg</i></p>
<dd> Average the values in the input img pixels into <i>navg</i> by <i>navg</i> squares, and create one output pixel for each such square. If used with <code>-T</code><i>3</i> it will report an average constraint between 0 and 1. If used with <code>-T</code><i>2</i> the output will be average data value or NaN according to whether average constraint is &gt; 0.5. <i>navg</i> must evenly divide into the dimensions of the imgfile in pixels. [Default <i>1</i> does no averaging].</p>
<dt><code>-S</code>[<i>scale</i>]</p>
<dd> Multiply the img file values by <i>scale</i> before storing in grid file. [Default is 1.0]. For recent img files: img topo files are stored in (corrected) meters [<code>-S</code>1]; free-air gravity files in mGal*10 [<code>-S</code>0.1 to get mGal]; vertical deflection files in micro-radians*10 [<code>-S</code>0.1 to get micro-radians], vertical gravity gradient files in Eotvos*50 [<code>-S</code>0.02 to get Eotvos, or <code>-S</code>0.002 to get mGal/km]). If no <i>scale</i> is given we try to determine the scale by examining the file name for clues.</p>
<dt><code>-T</code><i>type</i></p>
<dd> <i>type</i> handles the encoding of constraint information. <i>type</i> = 0 indicates that no such information is encoded in the img file (used for pre-1995 versions of the gravity data) and gets all data. <i>type</i> &gt; 0 indicates that constraint information is encoded (1995 and later (current) versions of the img files) so that one may produce a grid file as follows: <code>-T</code><i>1</i> gets data values at all points, <code>-T</code><i>2</i> gets data values at constrained points and NaN at interpolated points; <code>-T</code><i>3</i> gets 1 at constrained points and 0 at interpolated points [Default is 1].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. Particularly recommended here, as it is helpful to see how the coordinates are adjusted.</p>
<dt><code>-W</code><i>maxlon</i></p>
<dd> Indicate <i>maxlon</i> as the maximum longitude extent of the input img file. Versions since 1995 have had <i>maxlon</i> = 360.0, while some earlier files had <i>maxlon</i> = 390.0. [Default is 360.0].</p>
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
<h2>GEOGRAPHIC EXAMPLES</h2>
<p> The <code>-M</code> option should be excluded if you need the output grid to be in geographic coordinates. To extract data in the region <code>-R</code>-40/40/-70/-30 from <i>world_grav.img.7.2</i> and reproject to yield geographic coordinates, you can try </p>
<pre>
img2grd world_grav.img.16.1 -Gmerc_grav.nc -R-40/40/-70/-30 -V
</pre>
<p> Because the latitude spacing in the img file is equidistant in Mercator units, the resulting grid will not match the specified <code>-R</code> exactly, and the latitude spacing will not equal the longitude spacing. If you need an exact match with your <code>-R</code> and the same spacing in longitude and latitude, use the <code>-E</code> option: </p>
<pre>
img2grd world_grav.img.16.1 -Gmerc_grav.nc -R-40/40/-70/-30 -E -V
</pre>
<h2>MERCATOR EXAMPLES</h2>
<p> Since the img files are in a Mercator projection, you should NOT extract a geographic grid if your plan is to make a Mercator map. If you did that you end of projecting and reprojection the grid, loosing short-wavelength detail. Better to use <code>-M</code> and plot the grid using a linear projection with the same scale as the desired Mercator projection (see GMT Example 29). To extract data in the region <code>-R</code>-40/40/-70/-30 from <i>world_grav.img.7.2</i>, run </p>
<pre>
gmt img2grd -M world_grav.img.7.2 -Gmerc_grav.nc -R-40/40/-70/-30 -V
</pre>
<p> Note that the <code>-V</code> option tells us that the range was adjusted to <code>-R</code>-40/40/-70.0004681551/-29.9945810754. We can also use <code>grdinfo</code> to find that the grid file header shows its region to be <code>-R</code>0/80/0/67.9666667 This is the range of x,y we will get from a Spherical Mercator projection using <code>-R</code>-40/40/-70.0004681551/-29.9945810754 and <code>-Jm</code>1. Thus, to take ship.lonlatgrav and use it to sample the merc_grav.nc, we can do this: </p>
<pre>
gmt set PROJ_ELLIPSOID Sphere
gmt mapproject -R-40/40/-70.0004681551/-29.9945810754 -Jm1i ship.lonlatgrav | \
          gmt grdtrack -Gmerc_grav.nc | gmt mapproject \
          -R-40/40/-70.0004681551/-29.9945810754 -Jm1i -I &gt; ship.lonlatgravsat
</pre>
<p> It is recommended to use the above method of projecting and unprojecting the data in such an application, because then there is only one interpolation step (in <code>grdtrack</code>). If one first tries to convert the grid file to lon,lat and then sample it, there are two interpolation steps (in conversion and in sampling). </p>
<p> To make a lon,lat grid from the above grid we can use </p>
<pre>
gmt grdproject merc_grav.nc -R-40/40/-70.0004681551/-29.9945810754 -Jm1i -I -D2m -Ggrav.nc
</pre>
<p> In some cases this will not be easy as the <code>-R</code> in the two coordinate systems may not align well. When this happens, we can also use (in fact, it may be always better to use) </p>
<pre>
gmt grd2xyz merc_grav.nc | gmt mapproject \
    -R-40/40/-70.0004681551/-29.994581075 -Jm1i -I | \
    gmt surface -R-40/40/-70/70 -I2m -Ggrav.nc
</pre>
<p> To make a Mercator map of the above region, suppose our gmt.conf value for <i>PROJ_LENGTH_UNIT</i> is inch. Then since the above merc_grav.nc file is projected with <code>-Jm</code>1i it is 80 inches wide. We can make a map 8 inches wide by using <code>-Jx</code>0.1i on any map programs applied to this grid (e.g., <code>grdcontour</code>, <code>grdimage</code>, <code>grdview</code>), and then for overlays which work in lon,lat (e.g., <code>psxy</code>, <code>pscoast</code>) we can use the above adjusted <code>-R</code> and <code>-Jm</code>0.1 to get the two systems to match up. </p>
<p> However, we can be smarter than this. Realizing that the input img file had pixels 2.0 minutes wide (or checking the nx and ny with grdinfo merc_grav.nc) we realize that merc_grav.nc used the full resolution of the img file and it has 2400 by 2039 pixels, and at 8 inches wide this is 300 pixels per inch. We decide we do not need that many and we will be satisfied with 100 pixels per inch, so we want to average the data into 3 by 3 squares. (If we want a contour plot we will probably choose to average the data much more (e.g., 6 by 6) to get smooth contours.) Since 2039 isn&#8217;t divisible by 3 we will get a different adjusted <code>-R</code> this time: </p>
<pre>
gmt img2grd -M world_grav.img.7.2 -Gmerc_grav_2.nc -R-40/40/-70/-30 -N3 -V
</pre>
<p> This time we find the adjusted region is <code>-R</code>-40/40/-70.023256525/-29.9368261101 and the output is 800 by 601 pixels, a better size for us. Now we can create an artificial illumination file for this using <code>grdgradient</code>: </p>
<pre>
gmt grdgradient merc_grav_2.nc -Gillum.nc -A0/270 -Ne0.6
</pre>
<p> and if we also have a CPT file called &quot;grav.cpt&quot; we can create a color shaded relief map like this: </p>
<pre>
gmt grdimage merc_grav_2.nc -Iillum.nc -Cgrav.cpt -Jx0.1i -K &gt; map.ps
gmt psbasemap -R-40/40/-70.023256525/-29.9368261101 -Jm0.1i -Ba10 -O &gt;&gt; map.ps
</pre>
<p> Suppose you want to obtain only the constrained data values from an img file, in lat/lon coordinates. Then run <code>img2grd</code> with the <code>-T</code>2 option, use <code>grd2xyz</code> to dump the values, pipe through grep -v NaN to eliminate NaNs, and pipe through <code>mapproject</code> with the inverse projection as above.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
