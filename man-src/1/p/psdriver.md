---
title: "psdriver(1)"
name: "psdriver"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psdriver/"
description: "PS driver – driver to create PostScript files (drivers)"
---

<h2>NAME</h2>
<p> <i></i><code> PS driver</code> &#8211; driver to create PostScript files<br />
 <i>(drivers)</i></p>
<h2>DESCRIPTION</h2>
<p> The PS driver generates a PostScript file from GRASS display commands. The driver is started as &#8216;pseudo&#8217; monitor (PS file instead) and when stopped, all output from previously used display commands are written to the PostScript file.</p>
<h2>USAGE</h2>
<h3>Environment variables</h3>
<p> Several environment variables effect the operation of the PS driver: </p>
<p> GRASS_PSFILE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>name of output file. If it ends with&nbsp;<wbr>&quot;.eps&quot;&nbsp;<wbr>an EPS file will be created. </p>
<p> GRASS_PAPER </p>
<p>&nbsp;<wbr>&nbsp;<wbr>sets the screen dimensions and margins to fit a standard paper size, see also GRASS_WIDTH, GRASS_HEIGHT. </p>
<p> GRASS_WIDTH </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defines the width of the screen, see also GRASS_HEIGHT </p>
<p> GRASS_HEIGHT </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defines the height of the screen, see also GRASS_WIDTH </p>
<p> GRASS_TRUECOLOR </p>
<p>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>&quot;TRUE&quot;, the PS driver generates color output, otherwise monochrome. </p>
<p> GRASS_LANDSCAPE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>&quot;TRUE&quot;, the screen is rotated 90 degrees counter-clockwise so that a &quot;landscape&quot; screen fits better on dqportrait&quot; paper. </p>
<p> GRASS_PS_HEADER </p>
<p>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>&quot;FALSE&quot;, the output is appended to any existing file, and no prolog or setup sections are generated. </p>
<p> GRASS_PS_TRAILER </p>
<p>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>&quot;FALSE&quot;, no trailer section is generated.</p>
<h3>Example</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.mon start=PS<br />
 Display raster map and vector polygons </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.rast&nbsp;<wbr><i>somerastermap</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.vect map=<i>somevectormap</i>&nbsp;<wbr>color=red<br />
 Stop the driver subsequently. This will write a file named <i>map.ps</i> to be created in your current directory: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>d.mon stop=PS </p>
<h2>NOTES</h2>
<p> The resolution of the <i>PS</i> raster map is defined by the map extents. Use <i>g.region -p</i> to get the number of rows and cols and use the environment variables to set the PS size. If you would like a larger image, multiply both rows and cols by the same whole number to preserve the aspect ratio. </p>
<p> GRASS_TRUECOLOR requires either PostScript level 2 or level 1 plus the colorimage and setrgbcolor operators (this is the case for colour printers which pre-date level 2 PostScript). </p>
<p> Only masked images (d.rast -o, d.rgb -o, d.his -n) require PostScript level 3.</p>
<h2>SEE ALSO</h2>
<p> <i> HTML map driver, PNG driver, XDRIVER<br />
 d.frame, d.out.file, d.mon, d.rast, d.vect </i></p>
<h2>AUTHOR</h2>
<p> Glynn Clements, 2007 </p>
<p> <i>Last changed: $Date: 2007-08-23 15:39:39 +0200 (Thu, 23 Aug 2007) $</i> </p>
<p> Full index </p>
<p> � 2003-2008 GRASS Development Team </p>
<h2>Index</h2>
