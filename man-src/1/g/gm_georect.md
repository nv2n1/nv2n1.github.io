---
title: "gm_georect(1)"
name: "gm_georect"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gm_georect/"
---

<h2>GEORECTIFY TOOL (gis.m)</h2>
<p> In order to use and overlay different forms of geospatial data in a GIS, they must use the same coordinate systems and be projected identically. The Georectify Tool uses multiple GRASS modules to <i>georectify</i> spatial data (map or image) that is not originally coded in an earth-based coordinate system (e.g., latitude/longitude or UTM). The Georectify Tool can transform the simple x/y coordinates of the original data by shifting, rotating, and warping them as needed for the original data to match other georectified data from the same location on earth. </p>
<p> The basic procedure is to identify a set of <i>ground control points</i> (GCPs) in the ungeorectified data. The georectified coordinates for the points are identified. A mathematical transformation is calculated by regressing the original x/y coordinates against the georectified coordinates for the same points. This transformation is then applied to all the data. </p>
<p> The Georectify Tool can georectify both raster and vector maps. Raster maps can be transformed using 1st, 2nd, and 3rd order polynomial transformations; vector maps are transformed only with a 1st order polynomial transformation. The georectified coordinates of GCPs can be entered by typing or can be extracted by clicking the equivalent locations with a mouse in a displayed georectified map. </p>
<h3>Using the Georectify Tool</h3>
<h3>Map Preparation</h3>
<p> The unrectified map or image (e.g., scanned image or CAD drawing) must be imported into a GRASS XY location. </p>
<p> In order to be georectified, the unrectified map or image must be added to a <i>imagery group</i>. An <i>imagery group</i> holds a single map/image or a set of maps/images that represent different views of exactly the same locale. All maps or images in a single <i>imagery group</i> must be exactly aligned (e.g., as in the different spectral bands of a multi-channel satellite image or layers of a single CAD drawing). You can create an <i>imagery group</i> from within the Georectify Tool if desired. </p>
<h3>Setup</h3>
<p> Restart GRASS, selecting the location/mapset where you want the map you will georectify to END UP (i.e., the projected TARGET location). Open any map display (or displays) that you want to use for extracting geographic coordinates by clicking with a mouse. Make sure that the computational region extents and resolution are set to the values you want for the newly georectified map. </p>
<p> Select <i></i><code>Georectify</code> from the <i></i><code>File</code> menu. </p>
<p> The Georectify Tool startup lets you select the type of map to georectify, the location/mapset of the map to georectify, the <i>image group</i> of the map to georectify, and a map to use for marking GCPs. </p>
<dl>
<dt><code>1</code></p>
<dd>
&nbsp;<wbr>click the radio button to georectify either raster or vector maps (you can only georectify raster <code>OR</code> vector maps in a single georectification session),</p>
<dt><code>2</code></p>
<dd>
&nbsp;<wbr>select the source&nbsp;<wbr>(XY)&nbsp;<wbr>location/mapset of the map to be georectified,</p>
<dt><code>3</code></p>
<dd> if needed, create an <i>imagery group</i> for the map to georectify. (the <i>imagery group </i><code>target</code> is automatically set to the current location and mapset),</p>
<dt><code>4</code></p>
<dd>
&nbsp;<wbr>select the&nbsp;<wbr><i>imagery group</i>&nbsp;<wbr>containing the map to georectify,</p>
<dt><code>5</code></p>
<dd>
&nbsp;<wbr>select the map/image to display for marking GCPs interactively (a raster or vector in the group you want to georectify),</p>
<dt><code>6</code></p>
<dd>
&nbsp;<wbr>click the&nbsp;<wbr>&quot;<code>Start Georectifying</code>&quot;&nbsp;<wbr>button to begin marking GCPs.</dl>
<h3>GCP Marking</h3>
<p> This opens a special map display with an ungeorectified map to use for marking GCPs, and a GCP manager window. The GCP map display can be zoomed and panned like a normal map display. </p>
<p> The GCP manager window holds the x/y coordinates and geographic coordinates of each GCP, and displays the <i>error</i> for each GCP (i.e., the distance that the actual GCP marked deviates from its expected placement using a transformation equation). </p>
<dl>
<dt><code>1</code></p>
<dd>
&nbsp;<wbr>Click in an empty x/y entry box in the GCP manager to begin marking a new GCP,</p>
<dt><code>2</code></p>
<dd>
&nbsp;<wbr>Click on the ungeorectified map to mark a GCP and automatically enter its x/y coordinates in the entry box. (Your cursor will automatically jump to the corresponding geographic coordinate entry box for the same GCP),</p>
<dt><code>3</code></p>
<dd> Enter the corresponding geographic coordinates for the GCP <code>OR</code> click on the same place in a georectified map (in a normal map display) to automatically extract the geographic coordinates and enter them into the geographic coordinate entry box in the GCP manager window (Note: use the <code>pointer tool</code> in the map display window)</dl>
<h3><code>GCP Management</code>Continue marking GCPs until you</h3>
<p> have enough for an accurate georectification. At least 3 GCPs are needed for a simple 1st order (affine) transformation that can shift and rotate a map; at least 6 GCPs are needed for a 2nd order (polynomial) transformation that will do simple warping in addition to shifting and rotating; at least 10 GCPs are needed for a 3rd order (polynomial) transformation that will do complex warping.<br />
 Any GCP can be edited by typing new values or by selecting the appropriate entry box and clicking on the GCP-marking display or georectified map display.<br />
 GCPs can be excluded and not used for calculating the transformation equation or the total RMS error by unchecking the box in the &quot;use&quot; column at the left of each GCP entry line. Only active GCPs (i.e., with the &quot;use&quot; box checked) will be used for computing the georectification and total error.<br />
 You can delete all inactive GCPs (i.e., with unchecked &quot;use&quot; boxes) by clicking the <code>eraser tool</code> in the GCP manager tool bar.<br />
 Total <i>RMS (</i>root mean square) error is calculated from all active GCPs. Click the <code>RMS tool</code> in the GCP manager tool bar to update the total RMS error after changing or including/excluding a GCP. Excluding a GCP with an especially high individual error can reduce overall RMS error, but will also change the individual errors of all other GCPs. The lower the RMS error, the more accurate the final georectification will be. </p>
<p> All active GCPs can be saved to a <i>POINTS</i> file, associated with the <i>imagery group</i> for the map(s) to be georectified. If a saved <i>POINTS</i> file exists, prior to a georectification session the GCP values in the <i>POINTS</i> file will automatically be entered into the GCP manager window when a georectification session is started. </p>
<h3>Georectification</h3>
<p> When you are satisfied with your selection of GCPs and RMS error&#8230; </p>
<dl>
<dt><code>1</code></p>
<dd> Select the type of georectification you want to perform (1st, 2nd, or 3rd order for rasters; 1st order only for vectors). Remember, at least 3 points are needed for 1st order georectification, 6 points for 2nd order, and 10 points for 3rd order.</p>
<dt><code>2</code></p>
<dd> Press the <code>Georectification button</code> on the GCP manager tool bar. Depending on the number of cells in a raster map or nodes in a vector map, georectification may take some time.</dl>
<h2>SEE ALSO</h2>
<p> <i> gis.m manual<br />
 gis.m: ANIMATION TOOL<br />
 gis.m: PROFILE TOOL </p>
<p> i.points<br />
 i.vpoints<br />
 i.rectify<br />
 g.proj<br />
 g.setproj<br />
 m.proj<br />
 r.proj<br />
 v.proj </i></p>
<h2>AUTHORS</h2>
<p> Michael Barton, Arizona State University, Tempe, Arizona, USA </p>
<p> <i>Last changed: $Date: 2007-11-18 21:17:33 +0100 (Sun, 18 Nov 2007) $</i> </p>
<p> Full index </p>
<h2>Index</h2>
<dt><a href="#lbAI">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAJ">AUTHORS</a></p>
<dd></dl>
