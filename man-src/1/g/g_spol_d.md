---
title: "g_spol_d(1)"
name: "g_spol_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_spol_d/"
description: "g_spol – analyzes solvent dipole orientation and polarization around solutes"
---

<h2>NAME</h2>
<p> g_spol &#8211; analyzes solvent dipole orientation and polarization around solutes </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_spol</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> scdist.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]com</code><i></i> <code>-refat</code><i> int </i> <code>-rmin</code><i> real </i> <code>-rmax</code><i> real </i> <code>-dip</code><i> real </i> <code>-bw</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_spol analyzes dipoles around a solute; it is especially useful for polarizable water. A group of reference atoms, or a center of mass reference (option <code> -com</code>) and a group of solvent atoms is required. The program splits the group of solvent atoms into molecules. For each solvent molecule the distance to the closest atom in reference group or to the COM is determined. A cumulative distribution of these distances is plotted. For each distance between <code> -rmin</code> and <code> -rmax</code> the inner product of the distance vector and the dipole of the solvent molecule is determined. The average of these dipole components is printed. The same is done for the polarization, where the average dipole is subtracted from the instantaneous dipole. The magnitude of the average dipole is set with the option <code> -dip</code>, the direction is defined by the vector from the first atom in the selected solvent group to the midpoint between the second and the third atom.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> scdist.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
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
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-[no]com</code><i>no </i><br />
&nbsp;<wbr>Use the center of mass as the reference postion </p>
<p> <code>-refat</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>The reference atom of the solvent molecule </p>
<p> <code>-rmin</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum distance&nbsp;<wbr>(nm) </p>
<p> <code>-rmax</code><i> real</i><code> 0.32 </code><br />
&nbsp;<wbr>Maximum distance&nbsp;<wbr>(nm) </p>
<p> <code>-dip</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>The average dipole&nbsp;<wbr>(D) </p>
<p> <code>-bw</code><i> real</i><code> 0.01 </code><br />
&nbsp;<wbr>The bin width </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
