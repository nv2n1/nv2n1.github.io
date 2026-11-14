---
title: "g_sorient_d(1)"
name: "g_sorient_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_sorient_d/"
description: "g_sorient – analyzes solvent orientation around solutes"
---

<h2>NAME</h2>
<p> g_sorient &#8211; analyzes solvent orientation around solutes </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_sorient</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> sori.xvg </i> <code>-no</code><i> snor.xvg </i> <code>-ro</code><i> sord.xvg </i> <code>-co</code><i> scum.xvg </i> <code>-rc</code><i> scount.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]com</code><i></i> <code>-[no]v23</code><i></i> <code>-rmin</code><i> real </i> <code>-rmax</code><i> real </i> <code>-cbin</code><i> real </i> <code>-rbin</code><i> real </i> <code>-[no]pbc</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_sorient analyzes solvent orientation around solutes. It calculates two angles between the vector from one or more reference positions to the first atom of each solvent molecule: theta1: the angle with the vector from the first atom of the solvent molecule to the midpoint between atoms 2 and 3. </p>
<p> theta2: the angle with the normal of the solvent plane, defined by the same three atoms, or when the option <code> -v23</code> is set the angle with the vector between atoms 2 and 3. </p>
<p> The reference can be a set of atoms or the center of mass of a set of atoms. The group of solvent atoms should consist of 3 atoms per solvent molecule. Only solvent molecules between <code> -rmin</code> and <code> -rmax</code> are considered for <code> -o</code> and <code> -no</code> each frame. </p>
<p> <code> -o</code>: distribtion of cos(theta1) for rmin=r=rmax. </p>
<p> <code> -no</code>: distribution of cos(theta2) for rmin=r=rmax. </p>
<p> <code> -ro</code>: cos(theta1) and 3cos2(theta2)-1 as a function of the distance. </p>
<p> <code> -co</code>: the sum over all solvent molecules within distance r of cos(theta1) and 3cos2(theta2)-1 as a function of r. </p>
<p> <code> -rc</code>: the distribution of the solvent molecules as a function of r</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> sori.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-no</code><i> snor.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ro</code><i> sord.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-co</code><i> scum.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-rc</code><i> scount.xvg</i> <code>Output</code><br />
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
<p> <code>-[no]v23</code><i>no </i><br />
&nbsp;<wbr>Use the vector between atoms 2 and 3 </p>
<p> <code>-rmin</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Minimum distance&nbsp;<wbr>(nm) </p>
<p> <code>-rmax</code><i> real</i><code> 0.5 </code><br />
&nbsp;<wbr>Maximum distance&nbsp;<wbr>(nm) </p>
<p> <code>-cbin</code><i> real</i><code> 0.02 </code><br />
&nbsp;<wbr>Binwidth for the cosine </p>
<p> <code>-rbin</code><i> real</i><code> 0.02 </code><br />
&nbsp;<wbr>Binwidth for r&nbsp;<wbr>(nm) </p>
<p> <code>-[no]pbc</code><i>no </i><br />
&nbsp;<wbr>Check PBC for the center of mass calculation. Only necessary when your reference group consists of several molecules. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
