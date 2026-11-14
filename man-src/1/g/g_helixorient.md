---
title: "g_helixorient(1)"
name: "g_helixorient"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_helixorient/"
description: "g_helixorient – calculates local pitch/bending/rotation/orientation inside helices"
---

<h2>NAME</h2>
<p> g_helixorient &#8211; calculates local pitch/bending/rotation/orientation inside helices </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_helixorient</code> <code>-s</code><i> topol.tpr </i> <code>-f</code><i> traj.xtc </i> <code>-n</code><i> index.ndx </i> <code>-oaxis</code><i> helixaxis.dat </i> <code>-ocenter</code><i> center.dat </i> <code>-orise</code><i> rise.xvg </i> <code>-oradius</code><i> radius.xvg </i> <code>-otwist</code><i> twist.xvg </i> <code>-obending</code><i> bending.xvg </i> <code>-otilt</code><i> tilt.xvg </i> <code>-orot</code><i> rotation.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]xvgr</code><i></i> <code>-[no]sidechain</code><i></i> <code>-[no]incremental</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_helixorient calculates coordinates and direction of the average axis inside an alpha helix, and the direction/vectors of both the alpha carbon and (optionally) a sidechain atom relative to the axis. </p>
<p> As input, you need to specify an index group with alpha carbon atoms corresponding to an alpha helix of continuous residues. Sidechain directions require a second index group of the same size, containing the heavy atom in each residue that should represent the sidechain. </p>
<p> Note that this program does not do any fitting of structures. </p>
<p> We need four Calpha coordinates to define the local direction of the helix axis. </p>
<p> The tilt/rotation is calculated from Euler rotations, where we define the helix axis as the local X axis, the residues/CA-vector as Y, and the Z axis from their cross product. We use the Euler Y-Z-X rotation, meaning we first tilt the helix axis (1) around and (2) orthogonal to the residues vector, and finally apply the (3) rotation around it. For debugging or other purposes, we also write out the actual Euler rotation angles as theta1-3.xvg</p>
<h2>FILES</h2>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-oaxis</code><i> helixaxis.dat</i> <code>Output</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-ocenter</code><i> center.dat</i> <code>Output</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-orise</code><i> rise.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oradius</code><i> radius.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-otwist</code><i> twist.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-obending</code><i> bending.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-otilt</code><i> tilt.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-orot</code><i> rotation.xvg</i> <code>Output</code><br />
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
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-[no]sidechain</code><i>no </i><br />
&nbsp;<wbr>Calculate sidechain directions relative to helix axis too. </p>
<p> <code>-[no]incremental</code><i>no </i><br />
&nbsp;<wbr>Calculate incremental rather than total rotation/tilt. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
