---
title: "g_morph(1)"
name: "g_morph"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_morph/"
description: "g_morph – linear interpolation of conformations"
---

<h2>NAME</h2>
<p> g_morph &#8211; linear interpolation of conformations </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_morph</code> <code>-f1</code><i> conf1.gro </i> <code>-f2</code><i> conf2.gro </i> <code>-o</code><i> interm.xtc </i> <code>-or</code><i> rms-interm.xvg </i> <code>-n</code><i> index.ndx </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-ninterm</code><i> int </i> <code>-first</code><i> real </i> <code>-last</code><i> real </i> <code>-[no]fit</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_morph does a linear interpolation of conformations in order to create intermediates. Of course these are completely unphysical, but that you may try to justify yourself. Output is in the form of a generic trajectory. The number of intermediates can be controlled with the -ninterm flag. The first and last flag correspond to the way of interpolating: 0 corresponds to input structure 1 while 1 corresponds to input strucutre 2. If you specify first 0 or last 1 extrapolation will be on the path from input structure x1 to x2. In general the coordinates of the intermediate x(i) out of N total intermidates correspond to: </p>
<p> x(i) = x1 + (first+(i/(N-1))*(last-first))*(x2-x1) </p>
<p> Finally the RMSD with respect to both input structures can be computed if explicitly selected (-or option). In that case an index file may be read to select what group RMS is computed from.</p>
<h2>FILES</h2>
<p> <code>-f1</code><i> conf1.gro</i> <code>Input</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-f2</code><i> conf2.gro</i> <code>Input</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> interm.xtc</i> <code>Output</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-or</code><i> rms-interm.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-ninterm</code><i> int</i><code> 11</code><br />
&nbsp;<wbr>Number of intermediates </p>
<p> <code>-first</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Corresponds to first generated structure&nbsp;<wbr>(0 is input x0, see above) </p>
<p> <code>-last</code><i> real</i><code> 1 </code><br />
&nbsp;<wbr>Corresponds to last generated structure&nbsp;<wbr>(1 is input x1, see above) </p>
<p> <code>-[no]fit</code><i>yes </i><br />
&nbsp;<wbr>Do a least squares fit of the second to the first structure before interpolating </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
