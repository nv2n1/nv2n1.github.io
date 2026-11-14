---
title: "gmtflexure(1)"
name: "gmtflexure"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtflexure/"
description: "gmtflexure – Compute flexural deformation of 2-D loads, forces, bending and moments"
---

<h2>NAME</h2>
<p> gmtflexure &#8211; Compute flexural deformation of 2-D loads, forces, bending and moments</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtflexure</code> <i>rm</i>/<i>rl</i>[/<i>ri</i>]/<i>rw</i> <code>-E</code><i>Te</i>[<code>u</code>]|<i>D</i>|<i>file</i> [ [<code>l</code>|<code>r</code>][/<i>args</i>] ] [ <code>p</code><i>Poisson</i> ] [ <code>y</code><i>Young</i> ] [ <i>force</i> ] [ <i>args</i>] [ ] [ <i>wfile</i>] [ [<i>level</i>] ] [ <i>wd</i>] [ <i>zm</i>] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtflexure</code> computes the flexural response to 2-D loads using a range of user-selectable options, such as boundary conditions, pre-existing deformations, variable rigidity and restoring force, and more. The solutions are obtained using finite difference approximations to the differential equations.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-D</code><i>rm</i>/<i>rl</i>[/<i>ri</i>]/<i>rw</i></p>
<dd> Sets density for mantle, load, infill (optionally, otherwise it is assumed to equal the load density), and water. If <i>ri</i> is not given then it defaults to <i>rl</i>.</p>
<dt><code>-E</code><i>Te</i>[<code>u</code>]|<i>D</i>|<i>file</i></p>
<dd> Sets the elastic plate thickness (in meter); append <code>k</code> for km. If the elastic thickness exceeds 1e10 it will be interpreted as a flexural rigidity <code>D</code> instead (by default <code>D</code> is computed from <i>Te</i>, Young&#8217;s modulus, and Poisson&#8217;s ratio; see <code>-C</code> to change these values). Alternatively, supply a <i>file</i> with variable plate thicknesses or rigidities. The file must be co-registered with any file given via <code>-Q</code>.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<code>l</code>|<code>r</code>]<i>bc</i>[/<i>args</i>]</p>
<dd> Sets the boundary conditions at the <code>l</code>eft and <code>r</code>ight boundary. The <i>bc</i> can be one of four codes: 0 selects the infinity condition, were both the deflection and its slope are set to zero. 1 selects the periodic condition where both the first and third derivatives of the deflection are set to zero. 2 selects the clamped condition where <i>args</i> (if given) sets the deflection value [0] (and its first derivative is set to zero), while 3 selects the free condition where <i>args</i> is given as <i>moment</i>/<i>force</i> which specify the end bending moment and vertical shear force [0/0]. Use SI units for any optional arguments.</p>
<dt><code>-Cp</code><i>Poisson</i></p>
<dd> Change the current value of Poisson&#8217;s ratio [0.25].</p>
<dt><code>-Cy</code><i>Young</i></p>
<dd> Change the current value of Young&#8217;s modulus [7.0e10 N/m^2].</p>
<dt><code>-F</code><i>force</i>]</p>
<dd> Set a constant horizontal in-plane force, in Pa m [0]</p>
<dt><code>-Qn</code>|<code>q</code>|<code>t</code>[<i>args</i>]</p>
<dd> Sets the vertical load specification. Choose among these three options: <code>-Qn</code> means there is no input load file and that any deformation is simply driven by the boundary conditions set via <code>-A</code>. If no rigidity or elastic thickness file is given via <code>-E</code> then you must also append <i>min</i>/<i>max</i>/<i>inc</i> to initiate the locations used for the calculations. Append <code>+</code> to <i>inc</i> to indicate the number of points instead. <code>-Qq</code>[<i>loadfile</i>] is a file (or stdin if not given) with (x,load in Pa) for all equidistant data locations. Finally, <code>-Qt</code>[<i>topofile</i>] is a file (or stdin if not given) with (x,load in m or km, positive up); see <code>-M</code> for topography unit used [m].</p>
<dt><code>-S</code></p>
<dd> Compute the curvature along with the deflections and report them via the third output column [none].</p>
<dt><code>-T</code><i>wfile</i></p>
<dd> Supply a file with pre-existing deformations [undeformed surface].</p>
<dt><code>-W</code><i>wd</i></p>
<dd> Specify water depth in m; append k for km. Must be positive [0]. Any subaerial topography will be scaled via the densities set in <code>-D</code> to compensate for the larger density contrast with air.</p>
<dt><code>-Z</code><i>zm</i></p>
<dd> Specify reference depth to flexed surface in m; append k for km. Must be positive [0]. We add this value to the flexed surface before output.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input.</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</p>
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
<h2>NOTE ON UNITS</h2>
<p> The <code>-M</code> option controls the units used in all input and output files. However, this option does <i>not</i> control values given on the command line to the <code>-E</code>, <code>-W</code>, and <code>-Z</code> options. These are assumed to be in meters unless an optional <code>k</code> for km is appended.</p>
<h2>PLATE FLEXURE NOTES</h2>
<p> We solve for plate flexure using a finite difference approach. This method can accommodate situations such as variable rigidity, restoring force that depends on the deflection being positive or negative, pre-existing deformation, and different boundary conditions.</p>
<h2>EXAMPLES</h2>
<p> To compute elastic plate flexure from the topography load in <i>topo.txt</i>, for a 10 km thick plate with typical densities, try </p>
<pre>
gmt flexure -Qttopo.txt -E10k -D2700/3300/1035 &gt; flex.txt
</pre>
<h2>REFERENCES</h2>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gravfft</code> <code>grdflexure</code><code>grdmath</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
