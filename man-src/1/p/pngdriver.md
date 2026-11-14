---
title: "pngdriver(1)"
name: "pngdriver"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pngdriver/"
description: "PNG driver – driver to create PNG and PPM images (drivers)"
---

<h2>NAME</h2>
<p> <i></i><code> PNG driver</code> &#8211; driver to create PNG and PPM images<br />
 <i>(drivers)</i></p>
<h2>DESCRIPTION</h2>
<p> The PNG driver generates PNG and PPM images from GRASS display commands. Per default PNG files are written with this driver. It is started as &#8216;pseudo&#8217; monitor (image file instead) and when stopped, all output from previously used display commands are written to the PNG image file.</p>
<h2>USAGE</h2>
<h3>Environment variables</h3>
<p> Several environment variables effect the operation of the PNG driver.</p>
<dl>
<dt>
<dd> <code>GRASS_WIDTH=xxx</code><br />
 the width of the image map (default is 640).<br />
 <code>GRASS_HEIGHT=yyy</code><br />
 the height of the image map (default is 480).<br />
 <code>GRASS_PNGFILE=filename</code><br />
 the filename to put the resulting image in, default is <code>map.png</code>. If you set GRASS_PNGFILE to a filename which ends in &quot;.ppm&quot;, a PPM file will be created. </p>
<p>&nbsp;<wbr> <code>GRASS_BACKGROUNDCOLOR=RRGGBB</code><br />
 specifies the background color to use in RGB notation (hex values). Default is <code>000000</code> (black).<br />
 <code>GRASS_TRANSPARENT=[TRUE|FALSE]</code><br />
 sets transparent background on (TRUE) or off (FALSE, default).<br />
 <code>GRASS_TRUECOLOR=[TRUE|FALSE]</code><br />
 sets true-color support<br />
 <code>GRASS_PNG_COMPRESSION=[0|1|9]</code><br />
 compression level of PNG files (0 = none, 1 = fastest, 9 = best, default is 6)<br />
 <code>GRASS_PNG_AUTO_WRITE=[TRUE|FALSE]</code><br />
 if set to &quot;TRUE&quot;, the image file will be written after each operation (i.e. whenever a client disconnects), rather than only being written out when the driver terminates.<br />
 <code>GRASS_PNG_READ</code><br />
 if &quot;TRUE&quot;, the PNG driver will initialize the image from the contents of $GRASS_PNGFILE.<br />
 <code>GRASS_PNG_MAPPED</code><br />
 if &quot;TRUE&quot;, the PNG driver will map $GRASS_PNGFILE as its framebuffer, rather than using memory. This only works with BMP files.<br />
 <code>GRASS_RENDER_IMMEDIATE=[TRUE|FALSE]</code><br />
 tells the raster library to use its built-in PNG driver rather than connecting to an external monitor process using sockets. If dqTRUE&quot;, there is no need to run &quot;d.mon start=PNG&quot;</dl>
<h3>Example</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>export GRASS_RENDER_IMMEDIATE=TRUE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>export GRASS_TRUECOLOR=TRUE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.mon start=PNG<br />
 Display raster map and vector polygons </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.rast&nbsp;<wbr><i>somerastermap</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.vect&nbsp;<wbr><i>somevectormap</i>&nbsp;<wbr>color=red<br />
 Stop the driver subsequently. This will write a file named <i>map.png</i> to be created in your current directory: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.mon stop=PNG </p>
<h2>NOTES</h2>
<p> The PNG driver uses the libpng (see the libpng home page) and zlib (see the info-zip home page), all which needs to be installed for the PNG driver to work (it&#8217;s worth it). </p>
<p> The resolution of the <i>PNG</i> raster map is defined by the map extents. Use <i>g.region -p</i> to get the number of rows and cols and use the environment variables to set the PNG size. If you would like a larger image, multiply both rows and cols by the same whole number to preserve the aspect ratio. </p>
<p> Further PNG file processing (e.g. quantization to 1 bit for monochrome images) can be done with &#8216;pnmquant&#8217; of the netpbm tools.</p>
<h2>SEE ALSO</h2>
<p> <i> HTML map driver, PostScript driver, XDRIVER<br />
 d.frame, d.mon, d.rast, d.vect </i></p>
<h2>AUTHOR</h2>
<p> Original version:<br />
 Per Henrik Johansen </p>
<p>&nbsp;<wbr> <i>NORGIT AS</i> </p>
<p> Rewritten by Glynn Clements, 2003 </p>
<p> <i>Last changed: $Date: 2007-09-01 19:40:57 +0200 (Sat, 01 Sep 2007) $</i> </p>
<p> Full index </p>
<p> � 2003-2008 GRASS Development Team </p>
<h2>Index</h2>
