---
title: "g_trjorder(1)"
name: "g_trjorder"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_trjorder/"
description: "trjorder – orders molecules according to their distance to a group"
---

<h2>NAME</h2>
<p> trjorder &#8211; orders molecules according to their distance to a group </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>trjorder</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> ordered.xtc </i> <code>-nshell</code><i> nshell.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]xvgr</code><i></i> <code>-na</code><i> int </i> <code>-da</code><i> int </i> <code>-[no]com</code><i></i> <code>-r</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> trjorder orders molecules according to the smallest distance to atoms in a reference group. It will ask for a group of reference atoms and a group of molecules. For each frame of the trajectory the selected molecules will be reordered according to the shortest distance between atom number <code> -da</code> in the molecule and all the atoms in the reference group. All atoms in the trajectory are written to the output trajectory. </p>
<p> trjorder can be useful for e.g. analyzing the n waters closest to a protein. In that case the reference group would be the protein and the group of molecules would consist of all the water atoms. When an index group of the first n waters is made, the ordered trajectory can be used with any Gromacs program to analyze the n closest waters. </p>
<p> If the output file is a pdb file, the distance to the reference target will be stored in the B-factor field in order to color with e.g. rasmol. </p>
<p> With option <code> -nshell</code> the number of molecules within a shell of radius <code> -r</code> around the refernce group are printed.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> ordered.xtc</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-nshell</code><i> nshell.xvg</i> <code>Output, Opt.</code><br />
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
<p> <code>-na</code><i> int</i><code> 3</code><br />
&nbsp;<wbr>Number of atoms in a molecule </p>
<p> <code>-da</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Atom used for the distance calculation </p>
<p> <code>-[no]com</code><i>no </i><br />
&nbsp;<wbr>Use the distance to the center of mass of the reference group </p>
<p> <code>-r</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Cutoff used for the distance calculation when computing the number of molecules in a shell around e.g. a protein </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
