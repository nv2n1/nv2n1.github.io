---
title: "g_xrama(1)"
name: "g_xrama"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_xrama/"
description: "xrama – shows animated Ramachandran plots"
---

<h2>NAME</h2>
<p> xrama &#8211; shows animated Ramachandran plots </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>xrama</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i></p>
<h2>DESCRIPTION</h2>
<p> xrama shows a Ramachandran movie, that is, it shows the Phi/Psi angles as a function of time in an X-Window. </p>
<p> Static Phi/Psi plots for printing can be made with g_rama. </p>
<p> Some of the more common X command line options can be used: </p>
<p> -bg, -fg change colors, -font fontname, changes the font.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-b</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>First frame&nbsp;<wbr>(ps)&nbsp;<wbr>to read from trajectory </p>
<p> <code>-e</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Last frame&nbsp;<wbr>(ps)&nbsp;<wbr>to read from trajectory </p>
<p> <code>-dt</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Only use frame when t MOD dt&nbsp;<wbr>=&nbsp;<wbr>first time&nbsp;<wbr>(ps) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
