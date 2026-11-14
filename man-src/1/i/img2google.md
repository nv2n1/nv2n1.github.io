---
title: "img2google(1)"
name: "img2google"
section: "1"
letter: "i"
url: "/docs/linux/man/1-img2google/"
description: "img2google – Create Google Earth KML overlay tiles from bathymetry Mercator img grid"
---

<h2>NAME</h2>
<p> img2google &#8211; Create Google Earth KML overlay tiles from bathymetry Mercator img grid</p>
<h2>SYNOPSIS</h2>
<p> <code>img2google</code> <code>-R</code><i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[<code>r</code>] [ <i>imgfile</i> ] [ <code>-A</code><i>mode</i>[<i>altitude</i>] ] [ <code>-C</code> ] [ <code>-F</code><i>fademin/fademax</i>] [ <code>-G</code><i>prefix</i> ] [ <code>-L</code><i>LODmin/LODmax</i>] [ [ <code>-N</code><i>layername</i> ] ] [ [ <code>-T</code><i>doctitle</i> ] [ <code>-U</code><i>URL</i> ] [ <code>-V</code> ] [ <code>-Z</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>img2google</code> reads a 1&#215;1 minute Mercator surface relief img file and creates a Google Earth overlay KML file and associated PNG tile for the specified region. If no input file is given we use topo.11.1.img.</p>
<dl>
<dt><code>-R</code></p>
<dd> <i>west, east, south,</i> and <i>north</i> specify the Region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><i>imgfile</i></p>
<dd> An img format bathymetry/topography file such as those created by Sandwell and Smith. If this files does not exist in the current directory and the user has set the environment variable <code>$GMT_DATADIR</code>, then <code>img2mercgrd</code> will try to find <i>imgfile</i> in <code>$GMT_DATADIR</code>.</p>
<dt><code>-A</code></p>
<dd> Selects one of 5 altitude modes recognized by Google Earth that determines the altitude (in m) of the image: <code>G</code> clamped to the ground, <code>g</code> append altitude relative to ground, <code>a</code> append absolute altitude, <code>s</code> append altitude relative to seafloor, and <code>S</code> clamp it to the seafloor [Default].</p>
<dt><code>-C</code></p>
<dd> Turn on clipping so that only portions below sea level will be visible in the image [no clipping].</p>
<dt><code>-F</code></p>
<dd> Sets the distance over which the geometry fades, from fully opaque to fully transparent. These ramp values, expressed in screen pixels, are applied at the minimum and maximum end of the LOD (visibility) limits, respectively. [no fading (0/0)].</p>
<dt><code>-G</code></p>
<dd> Specify the prefix for the output image file (the extensions are set automatically). Default uses the naming topoN|S<i>&lt;north&gt;</i>E|W&lt;<i>west</i>&gt;.</p>
<dt><code>-L</code></p>
<dd> Measurement in screen pixels that represents the minimum limit of the visibility range for a given Region Google Earth calculates the size of the Region when projected onto screen space. Then it computes the square root of the Region&#8217;s area (if, for example, the Region is square and the viewpoint is directly above the Region, and the Region is not tilted, this measurement is equal to the width of the projected Region). If this measurement falls within the limits defined by <i>LODmin</i> and <i>LODmax</i> (and if the region is in view), the Region is active. If this limit is not reached, the associated geometry is considered to be too far from the user&#8217;s viewpoint to be drawn. <i>LODmax</i> represents the maximum limit of the visibility range for a given Region. A value of −1, the default, indicates &quot;active to infinite size.&quot; [always active].</p>
<dt><code>-N</code></p>
<dd> Append the layername of the image (use quotes if strings contain spaces) [topoN|S<i>&lt;north&gt;</i>E|W&lt;<i>west</i>&gt;].</p>
<dt><code>-T</code></p>
<dd> Append the document title (use quotes if strings contain spaces) [&quot;Predicted bathymetry&quot;].</p>
<dt><code>-U</code></p>
<dd> By default, images are referenced locally relative to the KML file. Specify an URL to prepend a server address to the image name reference [local].</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</p>
<dt><code>-Z</code></p>
<dd> Uses zip (which must be installed) to create a *.kmz file for easy distribution; append <code>+</code> to delete the KML and PNG file after zipping [No zipping].</dl>
<h2>EXAMPLES</h2>
<p> To create a 10&#215;10 degree Google Earth KML tile for the region <code>-R</code>170/180/20/30 using the default <i>topo.11.1.img</i> and output naming convention, try </p>
<p> <code>img2google</code> <code>-R</code>170/180/20/30 </p>
<p> To make the same tile with the previous <i>topo.10.1.img</i>, run in verbose mode, clip so only oceanic areas are visible, name the output oldimage, specify the KML metadata directly (including setting the image altitude to 10 km), and make a single *.kmz file, try </p>
<p> <code>img2google</code> <i>topo.10.1.img</i> <code>-R</code>170/180/20/30 <code>-A</code><code>A</code>10000 <code>-C</code> <code>-G</code><i>oldimage</i> <code>-N</code>&quot;My KML title&quot; <code>-T</code>&quot;My KML title&quot; <code>-U</code><a rel="nofollow" href="http://my.server.com/images">http://my.server.com/images</a> <code>-V</code> <code>-Z</code> </p>
<h2>DATA SETS</h2>
<p> For topo.11.1.img and other Sandwell/Smith altimetry-derived Mercator grids, visit <a rel="nofollow" href="http://topex.ucsd.edu.">http://topex.ucsd.edu.</a></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-img2grd/">img2grd</a></i>(1) <i><a href="/docs/linux/man/1-img2mercgrd/">img2mercgrd</a></i>(1) <i><a href="/docs/linux/man/1-ps2raster/">ps2raster</a></i>(1) </p>
<h2>Index</h2>
