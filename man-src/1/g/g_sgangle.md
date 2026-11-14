---
title: "g_sgangle(1)"
name: "g_sgangle"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_sgangle/"
description: "g_sgangle – computes the angle and distance between two groups"
---

<h2>NAME</h2>
<p> g_sgangle &#8211; computes the angle and distance between two groups </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_sgangle</code> <code>-f</code><i> traj.xtc </i> <code>-n</code><i> index.ndx </i> <code>-s</code><i> topol.tpr </i> <code>-oa</code><i> sg_angle.xvg </i> <code>-od</code><i> sg_dist.xvg </i> <code>-od1</code><i> sg_dist1.xvg </i> <code>-od2</code><i> sg_dist2.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]one</code><i></i> <code>-[no]z</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> Compute the angle and distance between two groups. The groups are defined by a number of atoms given in an index file and may be two or three atoms in size. If -one is set, only one group should be specified in the index file and the angle between this group at time 0 and t will be computed. The angles calculated depend on the order in which the atoms are given. Giving for instance 5 6 will rotate the vector 5-6 with 180 degrees compared to giving 6 5. </p>
<p> If three atoms are given, the normal on the plane spanned by those three atoms will be calculated, using the formula P1P2 x P1P3. The cos of the angle is calculated, using the inproduct of the two normalized vectors. </p>
<p> Here is what some of the file options do: </p>
<p> -oa: Angle between the two groups specified in the index file. If a group contains three atoms the normal to the plane defined by those three atoms will be used. If a group contains two atoms, the vector defined by those two atoms will be used. </p>
<p> -od: Distance between two groups. Distance is taken from the center of one group to the center of the other group. </p>
<p> -od1: If one plane and one vector is given, the distances for each of the atoms from the center of the plane is given seperately. </p>
<p> -od2: For two planes this option has no meaning.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-oa</code><i> sg_angle.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-od</code><i> sg_dist.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-od1</code><i> sg_dist1.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-od2</code><i> sg_dist2.xvg</i> <code>Output, Opt.</code><br />
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
<p> <code>-[no]one</code><i>no </i><br />
&nbsp;<wbr>Only one group compute angle between vector at time zero and time t </p>
<p> <code>-[no]z</code><i>no </i><br />
&nbsp;<wbr>Use the Z-axis as reference </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
