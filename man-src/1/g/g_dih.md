---
title: "g_dih(1)"
name: "g_dih"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_dih/"
description: "g_dih – analyzes dihedral transitions"
---

<h2>NAME</h2>
<p> g_dih &#8211; analyzes dihedral transitions </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_dih</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-o</code><i> hello.out </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]sa</code><i></i> <code>-mult</code><i> int </i></p>
<h2>DESCRIPTION</h2>
<p> g_dih can do two things. The default is to analyze dihedral transitions by merely computing all the dihedral angles defined in your topology for the whole trajectory. When a dihedral flips over to another minimum an angle/time plot is made. </p>
<p> The opther option is to discretize the dihedral space into a number of bins, and group each conformation in dihedral space in the appropriate bin. The output is then given as a number of dihedral conformations sorted according to occupancy.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> hello.out</i> <code>Output</code><br />
&nbsp;<wbr>Generic output file&nbsp;<wbr> </p>
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
<p> <code>-[no]sa</code><i>no </i><br />
&nbsp;<wbr>Perform cluster analysis in dihedral space instead of analysing dihedral transitions. </p>
<p> <code>-mult</code><i> int</i><code> -1</code><br />
&nbsp;<wbr>mulitiplicity for dihedral angles&nbsp;<wbr>(by default read from topology) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
