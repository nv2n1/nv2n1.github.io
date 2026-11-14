---
title: "htmlmapdriver(1)"
name: "htmlmapdriver"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htmlmapdriver/"
description: "htmlmapdriver"
---

<h2>NAME</h2>
<p> <i></i><code>htmlmapdriver</code></p>
<h2 class="name">NAME</h2>
<p> <i></i><code>HTMLMAP driver</code> &#8211; driver to create HTML image maps<br />
 <i>(drivers)</i> </p>
<h2>DESCRIPTION</h2>
<p> The HTMLMAP driver allows the generation of HTML image maps for area vector data. HTML image maps are used in conjunction with images to provide unique URL targets for different portions of an image. The HTMLMAP driver can create both client-side image maps embedded into HTML files, or server-side image maps used by web server software. </p>
<p> Note that GRASS display commands that require the MOUSE will not work correctly (or at all!) </p>
<p> Polygons can at most have 100 vertices (this limit imposed by HTML image map formats, see <code>GRASS_HTMLMAXPOINTS </code> below.) The driver will attempt to trim polygons that have more that 100 vertices by removing vertices with the least amount of angle to the next vertice. Also, any polygon that is entirely bounded by another polygon will be discarded. </p>
<p> Text written to the driver before polygons are used as the href tag for all subsequent polygons written. All polygons that exist in a vector map will have the same href tag. </p>
<p> The only GRASS display commands that should be used with this driver are:</p>
<dl>
<dt>
<dd> d.text &#8211; pass href information for resulting image maps. d.vect &#8211; draw polygons from a vector map.</dl>
<h2>USAGE</h2>
<h3>Environment variablesSeveral environment variables effect the operation</h3>
<p> of HTMLMAP.</p>
<dl>
<dt>
<dd> <code>GRASS_WIDTH=xxx</code><br />
 the width of the image map (default is 640).<br />
 <code>GRASS_HEIGHT=yyy</code><br />
 the height of the image map (default is 480).<br />
 <code>GRASS_HTMLTYPE=type</code><br />
 the type of image mape to create (default is CLIENT):</p>
<dl>
<dt>
<dd>
 <code>CLIENT</code> Netscape/IE client-side image map. (NAME=&quot;map&quot;) </p>
<p> <code>APACHE</code> Apache/NCSA server-side image map. </p>
<p> <code>RAW</code> Raw url and polygon vertices ( <i>url x1 y1 x2 y2 format with user supplied conversion program.</dl>
<p> </i><code>GRASS_HTMLFILE=filename</code><br />
 specifies the resulting file to store the html image map, default is <code>htmlmap</code>. Files without absolute path names are written in the current directory where the driver was started.<br />
 <i>Any existing file of the same name is overwritten without warning.</i> </p>
<p>&nbsp;<wbr> <code>GRASS_HTMLMINDIST=n</code><br />
 specifies the minimum distance in pixels that a point must change from the previous point to keep in the list of vertices for a polygon. The default is <code>2</code>, which means that a point&#8217;s x and y difference from the previous point must change by a number of pixels greater than this value. This parameter helps to eliminate closely spaced points.<br />
 <code>GRASS_HTMLMINBBOX=n</code><br />
 specifies the minimum bounding box dimensions to record a polygon as a clickable area. The default is <code>2</code>, which means that a polygon with a bounding box of less than this value is not included. This parameter helps to eliminate polygons than are a point or line.<br />
 <code>GRASS_HTMLMAXPOINTS=n</code><br />
 specifies the maximum number of vertices included in a polygon&#8217;s clickable area. The default is <code>99</code>. Some browsers can only accomodate polygons of 100 vertices or less. The HTMLMAP driver automatically ensures that a polygon is closed by making the last point the same as the first point.
</dl>
<h3>Typical usage</h3>
<dl>
<dt>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.mon select=HTMLMAP<br />
 Display text strings (href&#8217;s) and polygons </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>echo&nbsp;<wbr>&quot;<a rel="nofollow" href="http://www.no-such-place.net/area51/">http://www.no-such-place.net/area51/</a>&quot;&nbsp;<wbr>| d.text </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.vect map=area51 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>echo&nbsp;<wbr>&quot;<a rel="nofollow" href="http://www.roswell-nm.net/little/green/men.html">http://www.roswell-nm.net/little/green/men.html</a>&quot;&nbsp;<wbr>| d.text </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.vect map=roswell<br />
 Stop the driver when all polygon have been displayed. This will cause a file named &#8216;htmlmap&#8217; to be created in your current directory. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.mon stop=HTMLMAP<br />
 You will also want to create an image for your image map. Use the PNG driver and other utilities to create .gif or .jpg files. <i>The following example is somewhat out of date and refers to options available in GRASS 5.</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>using previous GRASS_WIDTH&nbsp;<wbr>&amp;&nbsp;<wbr>GRASS_HEIGHT </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.mon start=PNG </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.mon select=PNG </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.rast map=terrain </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.vect map=area51&nbsp;<wbr>&nbsp;<wbr>fillcolor=white&nbsp;<wbr>&nbsp;<wbr>linecolor=blue </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.vect map=roswell fillcolor=yellow linecolor=blue </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.vect map=states&nbsp;<wbr>&nbsp;<wbr>color=green </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.vect map=roads&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>color=black </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.mon stop=PNG </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>make the region the same as the newly created cell for ppm export </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>g.region save=saved.reg </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>g.region raster=D_cell </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r.out.ppm -q input=D_cell output=alien.ppm </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>use the netpbm utilities to create a gif&nbsp;<wbr>(quantize if needed) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ppmquant 128&nbsp;<wbr>&lt;alien.ppm |&nbsp;<wbr>&nbsp;<wbr>ppmtogif&nbsp;<wbr>&gt;alien.gif&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>assemble some html with the image and the image map </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cat htmlmap&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&gt;&gt;alien.html </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>don&#8217;t forget to reset your region </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>g.region region=saved.reg </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>take a look and test it out </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>netscape file:`pwd`/alien.html&nbsp;<wbr>&amp; </p>
</dl>
<h2>NOTES</h2>
<p> HTMLMAP was adapted from the CELL driver in GRASS 4.3. Point-in-polygon test code was lifted from Randolph Franklin&#8217;s web page, see</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.ecse.rpi.edu/Homepages/wrf/">http://www.ecse.rpi.edu/Homepages/wrf/</a><br />
 <a rel="nofollow" href="http://www.ecse.rpi.edu/Homepages/wrf/research/geom/pnpoly.html">http://www.ecse.rpi.edu/Homepages/wrf/research/geom/pnpoly.html</a></dl>
<p> If you create an HTML file with two or more images and image maps, you will need to edit the map names. The HTMLMAP driver creates its map with the name <i>map</i>. A small sed script can easily change the map name: </p>
<h2>SEE ALSO</h2>
<p> <i> PNG driver, PostScript driver, XDRIVER<br />
 d.frame, d.mon, d.rast, d.text, d.vect </i> </p>
<p> <i>Last changed: $Date: 2007-05-14 08:26:06 +0200 (Mon, 14 May 2007) $</i> </p>
<p> Full index </p>
<p> � 2003-2008 GRASS Development Team </p>
<h2>Index</h2>
