---
title: "g_h2order(1)"
name: "g_h2order"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_h2order/"
description: "g_h2order – computes the orientation of water molecules"
---

<h2>NAME</h2>
<p> g_h2order &#8211; computes the orientation of water molecules </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_h2order</code> <code>-f</code><i> traj.xtc </i> <code>-n</code><i> index.ndx </i> <code>-nm</code><i> index.ndx </i> <code>-s</code><i> topol.tpr </i> <code>-o</code><i> order.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-d</code><i> string </i> <code>-sl</code><i> int </i></p>
<h2>DESCRIPTION</h2>
<p> Compute the orientation of water molecules with respect to the normal of the box. The program determines the average cosine of the angle between de dipole moment of water and an axis of the box. The box is divided in slices and the average orientation per slice is printed. Each water molecule is assigned to a slice, per time frame, based on the position of the oxygen. When -nm is used the angle between the water dipole and the axis from the center of mass to the oxygen is calculated instead of the angle between the dipole and a box axis.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-nm</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> order.xvg</i> <code>Output</code><br />
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
<p> <code>-d</code><i> string</i><code> Z</code><br />
&nbsp;<wbr>Take the normal on the membrane in direction X, Y or Z. </p>
<p> <code>-sl</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Calculate order parameter as function of boxlength, dividing the box in nr slices. </p>
<h2>KNOWN PROBLEMS</h2>
<p> &#8211; The program assigns whole water molecules to a slice, based on the firstatom of three in the index file group. It assumes an order O,H,H.Name is not important, but the order is. If this demand is not met,assigning molecules to slices is different. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
