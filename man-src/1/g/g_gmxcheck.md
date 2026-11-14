---
title: "g_gmxcheck(1)"
name: "g_gmxcheck"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_gmxcheck/"
description: "gmxcheck – checks and compares files"
---

<h2>NAME</h2>
<p> gmxcheck &#8211; checks and compares files </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>gmxcheck</code> <code>-f</code><i> traj.xtc </i> <code>-f2</code><i> traj.xtc </i> <code>-s1</code><i> top1.tpr </i> <code>-s2</code><i> top2.tpr </i> <code>-c</code><i> topol.tpr </i> <code>-e</code><i> ener.edr </i> <code>-e2</code><i> ener2.edr </i> <code>-n</code><i> index.ndx </i> <code>-m</code><i> doc.tex </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-vdwfac</code><i> real </i> <code>-bonlo</code><i> real </i> <code>-bonhi</code><i> real </i> <code>-tol</code><i> real </i> <code>-[no]ab</code><i></i> <code>-lastener</code><i> string </i></p>
<h2>DESCRIPTION</h2>
<p> gmxcheck reads a trajectory (<code> .trj</code>, <code> .trr</code> or <code> .xtc</code>), an energy file (<code> .ene</code> or <code> .edr</code>) or an index file (<code> .ndx</code>) and prints out useful information about them. </p>
<p> Option <code> -c</code> checks for presence of coordinates, velocities and box in the file, for close contacts (smaller than <code> -vdwfac</code> and not bonded, i.e. not between <code> -bonlo</code> and <code> -bonhi</code>, all relative to the sum of both Van der Waals radii) and atoms outside the box (these may occur often and are no problem). If velocities are present, an estimated temperature will be calculated from them. </p>
<p> If an index file is given it&#8217;s contents will be sumamrized. </p>
<p> If both a trajectory and a tpr file are given (with <code> -s1</code>) the program will check whether the bond lengths defined in the tpr file are indeed correct in the trajectory. If not you may have non-matching files due to e.g. deshuffling or due to problems with virtual sites. With these flags, gmxcheck provides a quick check for such problems. </p>
<p> The program can compare run two input (<code> .tpr</code>, <code> .tpb</code> or <code> .tpa</code>) files when both <code> -s1</code> and <code> -s2</code> are supplied. Similarly a pair of trajectory files can be compared (using the <code> -f2</code> option), or a pair of energy files (using the <code> -e2</code> option). </p>
<p> For free energy simulations the A and B state topology from one run input file can be compared with options <code> -s1</code> and <code> -ab</code>. </p>
<p> In case the <code> -m</code> flag is given a LaTeX file will be written consisting a rough outline for a methods section for a paper.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-f2</code><i> traj.xtc</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s1</code><i> top1.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-s2</code><i> top2.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-c</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-e</code><i> ener.edr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<p> <code>-e2</code><i> ener2.edr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-m</code><i> doc.tex</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>LaTeX file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-vdwfac</code><i> real</i><code> 0.8 </code><br />
&nbsp;<wbr>Fraction of sum of VdW radii used as warning cutoff </p>
<p> <code>-bonlo</code><i> real</i><code> 0.4 </code><br />
&nbsp;<wbr>Min. fract. of sum of VdW radii for bonded atoms </p>
<p> <code>-bonhi</code><i> real</i><code> 0.7 </code><br />
&nbsp;<wbr>Max. fract. of sum of VdW radii for bonded atoms </p>
<p> <code>-tol</code><i> real</i><code> 0.001 </code><br />
&nbsp;<wbr>Relative tolerance for comparing real values defined as 2*(a-b)/(|a|+|b|) </p>
<p> <code>-[no]ab</code><i>no </i><br />
&nbsp;<wbr>Compare the A and B topology from one file </p>
<p> <code>-lastener</code><i> string</i><br />
&nbsp;<wbr>Last energy term to compare&nbsp;<wbr>(if not given all are tested). It makes sense to go up until the Pressure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
