---
title: "g_gmxdump(1)"
name: "g_gmxdump"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_gmxdump/"
description: "gmxdump – makes binary files human readable"
---

<h2>NAME</h2>
<p> gmxdump &#8211; makes binary files human readable </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>gmxdump</code> <code>-s</code><i> topol.tpr </i> <code>-f</code><i> traj.xtc </i> <code>-e</code><i> ener.edr </i> <code>-cp</code><i> state.cpt </i> <code>-om</code><i> grompp.mdp </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]nr</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> gmxdump reads a run input file (<code> .tpa</code>/<code> .tpr</code>/<code> .tpb</code>), a trajectory (<code> .trj</code>/<code> .trr</code>/<code> .xtc</code>) or an energy file (<code> .ene</code>/<code> .edr</code>) and prints that to standard output in a readable format. This program is essential for checking your run input file in case of problems. </p>
<p> When requesting to dump a topology file the program will dump the processed topology, since not all original information is maintained in tpr files.</p>
<h2>FILES</h2>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-f</code><i> traj.xtc</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-e</code><i> ener.edr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<p> <code>-cp</code><i> state.cpt</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Checkpoint file&nbsp;<wbr> </p>
<p> <code>-om</code><i> grompp.mdp</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>grompp input file with MD parameters&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]nr</code><i>yes </i><br />
&nbsp;<wbr>Show index numbers in output&nbsp;<wbr>(leaving them out makes comparison easier, but creates a useless topology) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
