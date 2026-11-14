---
title: "g_saltbr(1)"
name: "g_saltbr"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_saltbr/"
description: "g_saltbr – computes salt bridges"
---

<h2>NAME</h2>
<p> g_saltbr &#8211; computes salt bridges </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_saltbr</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-t</code><i> real </i> <code>-[no]sep</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_saltbr plots the distance between all combination of charged groups as a function of time. The groups are combined in different ways.A minimum distance can be given, (eg. the cut-off), then groups that are never closer than that distance will not be plotted. </p>
<p> Output will be in a number of fixed filenames, min-min.xvg, plus-min.xvg and plus-plus.xvg, or files for every individual ion-pair if selected</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
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
<p> <code>-t</code><i> real</i><code> 1000 </code><br />
&nbsp;<wbr>trunc distance </p>
<p> <code>-[no]sep</code><i>no </i><br />
&nbsp;<wbr>Use separate files for each interaction&nbsp;<wbr>(may be MANY) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
