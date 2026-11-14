---
title: "g_density(1)"
name: "g_density"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_density/"
description: "g_density – calculates the density of the system"
---

<h2>NAME</h2>
<p> g_density &#8211; calculates the density of the system </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_density</code> <code>-f</code><i> traj.xtc </i> <code>-n</code><i> index.ndx </i> <code>-s</code><i> topol.tpr </i> <code>-ei</code><i> electrons.dat </i> <code>-o</code><i> density.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-d</code><i> string </i> <code>-sl</code><i> int </i> <code>-dens</code><i> enum </i> <code>-ng</code><i> int </i> <code>-[no]symm</code><i></i> <code>-[no]center</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> Compute partial densities across the box, using an index file. Densities in kg/m3, number densities or electron densities can be calculated. For electron densities, a file describing the number of electrons for each type of atom should be provided using <code> -ei</code>. It should look like: </p>
<p> 2 </p>
<p> atomname = nrelectrons </p>
<p> atomname = nrelectrons </p>
<p> The first line contains the number of lines to read from the file. There should be one line for each unique atom name in your system. The number of electrons for each atom is modified by its atomic partial charge.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-ei</code><i> electrons.dat</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-o</code><i> density.xvg</i> <code>Output</code><br />
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
<p> <code>-sl</code><i> int</i><code> 50</code><br />
&nbsp;<wbr>Divide the box in nr slices. </p>
<p> <code>-dens</code><i> enum</i><code> mass</code><br />
&nbsp;<wbr>Density:&nbsp;<wbr><code>&nbsp;<wbr>mass</code>,&nbsp;<wbr><code>&nbsp;<wbr>number</code>,&nbsp;<wbr><code>&nbsp;<wbr>charge</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>electron</code> </p>
<p> <code>-ng</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Number of groups to compute densities of </p>
<p> <code>-[no]symm</code><i>no </i><br />
&nbsp;<wbr>Symmetrize the density along the axis, with respect to the center. Useful for bilayers. </p>
<p> <code>-[no]center</code><i>no </i><br />
&nbsp;<wbr>Shift the center of mass along the axis to zero. This means if your axis is Z and your box is bX, bY, bZ, the center of mass will be at bX/2, bY/2, 0. </p>
<h2>KNOWN PROBLEMS</h2>
<p> &#8211; When calculating electron densities, atomnames are used instead of types. This is bad. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
