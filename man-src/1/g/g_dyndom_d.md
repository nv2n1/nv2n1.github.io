---
title: "g_dyndom_d(1)"
name: "g_dyndom_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_dyndom_d/"
description: "g_dyndom – interpolate and extrapolate structure rotations"
---

<h2>NAME</h2>
<p> g_dyndom &#8211; interpolate and extrapolate structure rotations </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_dyndom</code> <code>-f</code><i> dyndom.pdb </i> <code>-o</code><i> rotated.xtc </i> <code>-n</code><i> domains.ndx </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-firstangle</code><i> real </i> <code>-lastangle</code><i> real </i> <code>-nframe</code><i> int </i> <code>-maxangle</code><i> real </i> <code>-trans</code><i> real </i> <code>-head</code><i> vector </i> <code>-tail</code><i> vector </i></p>
<h2>DESCRIPTION</h2>
<p> g_dyndom reads a pdb file output from DynDom <a rel="nofollow" href="http://www.cmp.uea.ac.uk/dyndom/">http://www.cmp.uea.ac.uk/dyndom/</a> It reads the coordinates, and the coordinates of the rotation axis furthermore it reads an index file containing the domains. Furthermore it takes the first and last atom of the arrow file as command line arguments (head and tail) and finally it takes the translation vector (given in DynDom info file) and the angle of rotation (also as command line arguments). If the angle determined by DynDom is given, one should be able to recover the second structure used for generating the DynDom output. Because of limited numerical accuracy this should be verified by computing an all-atom RMSD (using <code> g_confrms</code>) rather than by file comparison (using diff). </p>
<p> The purpose of this program is to interpolate and extrapolate the rotation as found by DynDom. As a result unphysical structures with long or short bonds, or overlapping atoms may be produced. Visual inspection, and energy minimization may be necessary to validate the structure.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> dyndom.pdb</i> <code>Input</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-o</code><i> rotated.xtc</i> <code>Output</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> domains.ndx</i> <code>Input</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-firstangle</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Angle of rotation about rotation vector </p>
<p> <code>-lastangle</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Angle of rotation about rotation vector </p>
<p> <code>-nframe</code><i> int</i><code> 11</code><br />
&nbsp;<wbr>Number of steps on the pathway </p>
<p> <code>-maxangle</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>DymDom dtermined angle of rotation about rotation vector </p>
<p> <code>-trans</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Translation&nbsp;<wbr>(Aangstroem)&nbsp;<wbr>along rotation vector&nbsp;<wbr>(see DynDom info file) </p>
<p> <code>-head</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>First atom of the arrow vector </p>
<p> <code>-tail</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>Last atom of the arrow vector </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
