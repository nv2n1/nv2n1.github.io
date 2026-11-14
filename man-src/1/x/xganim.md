---
title: "xganim(1)"
name: "xganim"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xganim/"
description: "xganim"
---

<h2>NAME</h2>
<p> <i></i><code>xganim</code></p>
<h2>DESCRIPTION</h2>
<p> <i>xganim</i> is a tool for animating a series of GRASS raster files. At startup, a graphics window is opened containing VCR-like button controls for: rewind, reverse play, step back, stop, step forward, forward play, loop, swing, slower, faster, show filenames, current frame number, and Exit. The image is displayed above or to the left of the controls. Each raster map is read into memory, then the animation is played once beginning to end. The user may then replay the series or play continuous animation by using the buttons. </p>
<p> The user may define up to four &quot;views&quot;, or sub-windows, to animate simultaneously. e.g., View 1 could be rainfall, View 2 flooded areas, View 3 damage to bridges or levees, View 4 other economic damage, all animated as a time series. There is an arbitrary limit of 400 files per view (400 animation frames), but the practical limit may be less depending on the window size and amount of available RAM. </p>
<p> The environment variable XGANIM_SIZE is checked for a value to use as the dimension, in pixels, of the longest dimension of the animation window. If XGANIM_SIZE is not set, the animation size defaults to the rows &amp; columns in the current GRASS region, scaling if necessary to a default minimum size of 600 and maximum of 900. The resolution of the current GRASS region is maintained, independent of window size. Resizing the window after the program is running will have no effect on the animation size. </p>
<p> UNIX &#8211; style wild cards may be used with the command line version in place of a raster map name, but it must be quoted. </p>
<p> If the number of files differs for each view, the view with the fewest files will determine the number of frames in the animation.</p>
<h2>EXAMPLE</h2>
<p> export XGANIM_SIZE=800<br />
 xganim view1=&quot;rain[1-9]&quot;,&quot;rain1[0-2]&quot; view2=&quot;temp*&quot; </p>
<h2>NOTES</h2>
<p> For wildcard matching, <i>xganim</i> understands whatever the shell understands (as it invokes &quot;ls&quot; via the shell to expand wildcards). E.g., a user can use &quot;rast[0-9][0-9]&quot; to match &quot;rast00&quot; through &quot;rast99&quot; inclusive. If the maps if interest have varying numbers of digits, multiple patterns can be combined, e.g.:<br />
 export XGANIM_SIZE=1000<br />
 xganim view1=rast[0-9],rast[1-9][0-9]<br />
 to match rast0 through rast99 inclusive.</p>
<h2>BUGS</h2>
<p> On some displays that need to use private colormaps, the interface buttons may become difficult to see.</p>
<h2>SEE ALSO</h2>
<p> <i>d.slide.show</i>, <i>gis.m: ANIMATE TOOL</i></p>
<h2>AUTHOR</h2>
<p> Bill Brown, U.S. Army Construction Engineering Research Laboratories </p>
<p> <i>Last changed: $Date: 2007-12-17 14:53:55 +0100 (Mon, 17 Dec 2007) $</i> </p>
<p> Full index </p>
<p> � 2003-2008 GRASS Development Team </p>
<h2>Index</h2>
