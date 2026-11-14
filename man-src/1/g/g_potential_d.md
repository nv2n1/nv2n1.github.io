---
title: "g_potential_d(1)"
name: "g_potential_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_potential_d/"
description: "g_potential – calculates the electrostatic potential across the box"
---

<h2>NAME</h2>
<p> g_potential &#8211; calculates the electrostatic potential across the box </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_potential</code> <code>-f</code><i> traj.xtc </i> <code>-n</code><i> index.ndx </i> <code>-s</code><i> topol.tpr </i> <code>-o</code><i> potential.xvg </i> <code>-oc</code><i> charge.xvg </i> <code>-of</code><i> field.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-d</code><i> string </i> <code>-sl</code><i> int </i> <code>-cb</code><i> int </i> <code>-ce</code><i> int </i> <code>-tz</code><i> real </i> <code>-[no]spherical</code><i></i> <code>-ng</code><i> int </i> <code>-[no]correct</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> Compute the electrostatical potential across the box. The potential iscalculated by first summing the charges per slice and then integratingtwice of this charge distribution. Periodic boundaries are not taken into account. Reference of potential is taken to be the left side ofthe box. It&#8217;s also possible to calculate the potential in sphericalcoordinates as function of r by calculating a charge distribution inspherical slices and twice integrating them. epsilon_r is taken as 1,2 is more appropriate in many cases</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> potential.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oc</code><i> charge.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-of</code><i> field.xvg</i> <code>Output</code><br />
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
<p> <code>-sl</code><i> int</i><code> 10</code><br />
&nbsp;<wbr>Calculate potential as function of boxlength, dividing the box in nr slices. </p>
<p> <code>-cb</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Discard first nr slices of box for integration </p>
<p> <code>-ce</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Discard last nr slices of box for integration </p>
<p> <code>-tz</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Translate all coordinates distance in the direction of the box </p>
<p> <code>-[no]spherical</code><i>no </i><br />
&nbsp;<wbr>Calculate spherical thingie </p>
<p> <code>-ng</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Number of groups to consider </p>
<p> <code>-[no]correct</code><i>no </i><br />
&nbsp;<wbr>Assume net zero charge of groups to improve accuracy </p>
<h2>KNOWN PROBLEMS</h2>
<p> &#8211; Discarding slices for integration should not be necessary. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
