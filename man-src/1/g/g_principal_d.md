---
title: "g_principal_d(1)"
name: "g_principal_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_principal_d/"
description: "g_principal – calculates axes of inertia for a group of atoms"
---

<h2>NAME</h2>
<p> g_principal &#8211; calculates axes of inertia for a group of atoms </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_principal</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-a1</code><i> axis1.dat </i> <code>-a2</code><i> axis2.dat </i> <code>-a3</code><i> axis3.dat </i> <code>-om</code><i> moi.dat </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-tu</code><i> enum </i> <code>-[no]w</code><i></i> <code>-[no]foo</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_principal calculates the three principal axes of inertia for a group of atoms.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-a1</code><i> axis1.dat</i> <code>Output</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-a2</code><i> axis2.dat</i> <code>Output</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-a3</code><i> axis3.dat</i> <code>Output</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-om</code><i> moi.dat</i> <code>Output</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
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
<p> <code>-[no]foo</code><i>no </i><br />
&nbsp;<wbr>Dummy option to avoid empty array </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
