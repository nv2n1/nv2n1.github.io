---
title: "gm_profile(1)"
name: "gm_profile"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gm_profile/"
---

<h2>PROFILE TOOL (gis.m)</h2>
<p> The Profile Tool will draw a 2-dimensional profile of the surface of any raster map. The profile will be calculated along a transect line, drawn with a mouse on a map display. The transect line can be a simple line (i.e., with only a beginning and ending node) or a complex polyline (i.e., with multiple segments, delineated by multiple nodes). </p>
<h3>Using the Profile Tool</h3>
<p> The Profile Tool is started by clicking on the profile button () on the toolbar of a map display window. </p>
<dl>
<dt><code>1</code></p>
<dd> Click the map button on the Profile Tool toolbar to select a raster map to profile. The map to profile can be different from the one displayed.</p>
<dt><code>2</code></p>
<dd> Click the transect button to begin drawing a transect to profile with a mouse the current map display (i.e., the map display from which you launched the Profile Tool). Draw by holding down the left button to make a dqrubber-band&quot; line for each segment of the transect. A transect can have a single, straight segment or multiple segment. There is no need to &quot;end&quot; the drawing. The Profile Tool will profile the drawn transect at any time. You can also extend an existing transect and draw a profile of the new transect.</p>
<dt><code>3</code></p>
<dd> Click the profile button to create the profile.</dl>
<p> The profile extends from left to right in the profile display. The horizontal (x-axis) scale represents the total distance along the transect to be profiled. Vertical lines mark each node on a multi-segment transect and show the total distance along the transect to the node. The vertical (y-axis) scale is in units of the map that is being profiled. All scaling and axis labels are created automatically, and cannot be changed by the user.<br />
 &amp;bull; The erase button will erase the current transect and profile.<br />
 &amp;bull; The save button will save the profile to an Encapsulated PostScript (.eps) file. </p>
<h2>SEE ALSO</h2>
<p> <i> gis.m manual<br />
 gis.m: ANIMATION TOOL<br />
 gis.m: GEORECTIFY TOOL </p>
<p> d.profile<br />
 d.geodesic<br />
 d.rhumbline<br />
 m.cogo<br />
 r.profile<br />
 r.transect<br />
 </i></p>
<h2>AUTHORS</h2>
<p> Michael Barton, Arizona State University, Tempe, Arizona, USA<br />
 Hamish Bowman, University of Otago, Dunedin, New Zealand </p>
<p> <i>Last changed: $Date: 2007-11-18 21:17:33 +0100 (Sun, 18 Nov 2007) $</i> </p>
<p> Full index </p>
<h2>Index</h2>
