---
title: "g_densmap_d(1)"
name: "g_densmap_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_densmap_d/"
description: "g_densmap – calculates 2D planar or axial-radial density maps"
---

<h2>NAME</h2>
<p> g_densmap &#8211; calculates 2D planar or axial-radial density maps </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_densmap</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> densmap.xpm </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-bin</code><i> real </i> <code>-aver</code><i> enum </i> <code>-xmin</code><i> real </i> <code>-xmax</code><i> real </i> <code>-n1</code><i> int </i> <code>-n2</code><i> int </i> <code>-amax</code><i> real </i> <code>-rmax</code><i> real </i> <code>-[no]mirror</code><i></i> <code>-unit</code><i> enum </i> <code>-dmin</code><i> real </i> <code>-dmax</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_densmap computes 2D number-density maps. It can make planar and axial-radial density maps. The output <code> .xpm</code> file can be visualized with for instance xv and can be converted to postscript with xpm2ps. </p>
<p> The default analysis is a 2-D number-density map for a selected group of atoms in the x-y plane. The averaging direction can be changed with the option <code> -aver</code>. When <code> -xmin</code> and/or <code> -xmax</code> are set only atoms that are within the limit(s) in the averaging direction are taken into account. The grid spacing is set with the option <code> -bin</code>. When <code> -n1</code> or <code> -n2</code> is non-zero, the grid size is set by this option. Box size fluctuations are properly taken into account. </p>
<p> When options <code> -amax</code> and <code> -rmax</code> are set, an axial-radial number-density map is made. Three groups should be supplied, the centers of mass of the first two groups define the axis, the third defines the analysis group. The axial direction goes from -amax to +amax, where the center is defined as the midpoint between the centers of mass and the positive direction goes from the first to the second center of mass. The radial direction goes from 0 to rmax or from -rmax to +rmax when the <code> -mirror</code> option has been set. </p>
<p> The normalization of the output is set with the <code> -unit</code> option. The default produces a true number density. Unit <code> nm-2</code> leaves out the normalization for the averaging or the angular direction. Option <code> count</code> produces the count for each grid cell. When you do not want the scale in the output to go from zero to the maximum density, you can set the maximum with the option <code> -dmax</code>.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> densmap.xpm</i> <code>Output</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-b</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>First frame&nbsp;<wbr>(ps)&nbsp;<wbr>to read from trajectory </p>
<p> <code>-e</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Last frame&nbsp;<wbr>(ps)&nbsp;<wbr>to read from trajectory </p>
<p> <code>-dt</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Only use frame when t MOD dt&nbsp;<wbr>=&nbsp;<wbr>first time&nbsp;<wbr>(ps) </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-bin</code><i> real</i><code> 0.02 </code><br />
&nbsp;<wbr>Grid size&nbsp;<wbr>(nm) </p>
<p> <code>-aver</code><i> enum</i><code> z</code><br />
&nbsp;<wbr>The direction to average over:&nbsp;<wbr><code>&nbsp;<wbr>z</code>,&nbsp;<wbr><code>&nbsp;<wbr>y</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>x</code> </p>
<p> <code>-xmin</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Minimum coordinate for averaging </p>
<p> <code>-xmax</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Maximum coordinate for averaging </p>
<p> <code>-n1</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Number of grid cells in the first direction </p>
<p> <code>-n2</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Number of grid cells in the second direction </p>
<p> <code>-amax</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum axial distance from the center </p>
<p> <code>-rmax</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum radial distance </p>
<p> <code>-[no]mirror</code><i>no </i><br />
&nbsp;<wbr>Add the mirror image below the axial axis </p>
<p> <code>-unit</code><i> enum</i><code> nm-3</code><br />
&nbsp;<wbr>Unit for the output:&nbsp;<wbr><code>&nbsp;<wbr>nm-3</code>,&nbsp;<wbr><code>&nbsp;<wbr>nm-2</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>count</code> </p>
<p> <code>-dmin</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Minimum density in output </p>
<p> <code>-dmax</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum density in output&nbsp;<wbr>(0 means calculate it) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
