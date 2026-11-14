---
title: "g_mindist(1)"
name: "g_mindist"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_mindist/"
description: "g_mindist – calculates the minimum distance between two groups"
---

<h2>NAME</h2>
<p> g_mindist &#8211; calculates the minimum distance between two groups </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_mindist</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-od</code><i> mindist.xvg </i> <code>-on</code><i> numcont.xvg </i> <code>-o</code><i> atm-pair.out </i> <code>-ox</code><i> mindist.xtc </i> <code>-or</code><i> mindistres.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-tu</code><i> enum </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]matrix</code><i></i> <code>-[no]max</code><i></i> <code>-d</code><i> real </i> <code>-[no]pi</code><i></i> <code>-[no]split</code><i></i> <code>-ng</code><i> int </i> <code>-[no]pbc</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_mindist computes the distance between one group and a number of other groups. Both the minimum distance (between any pair of atoms from the respective groups) and the number of contacts within a given distance are written to two separate output files. With <code> -or</code>, minimum distances to each residue in the first group are determined and plotted as a function of reisdue number. </p>
<p> With option <code> -pi</code> the minimum distance of a group to its periodic image is plotted. This is useful for checking if a protein has seen its periodic image during a simulation. Only one shift in each direction is considered, giving a total of 26 shifts. It also plots the maximum distance within the group and the lengths of the three box vectors. </p>
<p> Other programs that calculate distances are <code> g_dist</code> and <code> g_bond</code>.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-od</code><i> mindist.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-on</code><i> numcont.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-o</code><i> atm-pair.out</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Generic output file&nbsp;<wbr> </p>
<p> <code>-ox</code><i> mindist.xtc</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-or</code><i> mindistres.xvg</i> <code>Output, Opt.</code><br />
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
<p> <code>-tu</code><i> enum</i><code> ps</code><br />
&nbsp;<wbr>Time unit:&nbsp;<wbr><code>&nbsp;<wbr>ps</code>,&nbsp;<wbr><code>&nbsp;<wbr>fs</code>,&nbsp;<wbr><code>&nbsp;<wbr>ns</code>,&nbsp;<wbr><code>&nbsp;<wbr>us</code>,&nbsp;<wbr><code>&nbsp;<wbr>ms</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>s</code> </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-[no]matrix</code><i>no </i><br />
&nbsp;<wbr>Calculate half a matrix of group-group distances </p>
<p> <code>-[no]max</code><i>no </i><br />
&nbsp;<wbr>Calculate&nbsp;<wbr>*maximum*&nbsp;<wbr>distance instead of minimum </p>
<p> <code>-d</code><i> real</i><code> 0.6 </code><br />
&nbsp;<wbr>Distance for contacts </p>
<p> <code>-[no]pi</code><i>no </i><br />
&nbsp;<wbr>Calculate minimum distance with periodic images </p>
<p> <code>-[no]split</code><i>no </i><br />
&nbsp;<wbr>Split graph where time is zero </p>
<p> <code>-ng</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Number of secondary groups to compute distance to a central group </p>
<p> <code>-[no]pbc</code><i>yes </i><br />
&nbsp;<wbr>Take periodic boundary conditions into account </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
