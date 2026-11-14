---
title: "g_rms(1)"
name: "g_rms"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_rms/"
description: "g_rms – calculates rmsd’s with a reference structure and rmsd matrices"
---

<h2>NAME</h2>
<p> g_rms &#8211; calculates rmsd&#8217;s with a reference structure and rmsd matrices </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_rms</code> <code>-s</code><i> topol.tpr </i> <code>-f</code><i> traj.xtc </i> <code>-f2</code><i> traj.xtc </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> rmsd.xvg </i> <code>-mir</code><i> rmsdmir.xvg </i> <code>-a</code><i> avgrp.xvg </i> <code>-dist</code><i> rmsd-dist.xvg </i> <code>-m</code><i> rmsd.xpm </i> <code>-bin</code><i> rmsd.dat </i> <code>-bm</code><i> bond.xpm </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-tu</code><i> enum </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-what</code><i> enum </i> <code>-[no]pbc</code><i></i> <code>-fit</code><i> enum </i> <code>-prev</code><i> int </i> <code>-[no]split</code><i></i> <code>-skip</code><i> int </i> <code>-skip2</code><i> int </i> <code>-max</code><i> real </i> <code>-min</code><i> real </i> <code>-bmax</code><i> real </i> <code>-bmin</code><i> real </i> <code>-[no]mw</code><i></i> <code>-nlevels</code><i> int </i> <code>-ng</code><i> int </i></p>
<h2>DESCRIPTION</h2>
<p> g_rms compares two structures by computing the root mean square deviation (RMSD), the size-independent &#8216;rho&#8217; similarity parameter (rho) or the scaled rho (rhosc), see Maiorov &amp; Crippen, PROTEINS <code> 22</code>, 273 (1995). This is selected by <code> -what</code>. </p>
<p> Each structure from a trajectory (<code> -f</code>) is compared to a reference structure. The reference structure is taken from the structure file (<code> -s</code>). </p>
<p> With option <code> -mir</code> also a comparison with the mirror image of the reference structure is calculated. This is useful as a reference for &#8216;significant&#8217; values, see Maiorov &amp; Crippen, PROTEINS <code> 22</code>, 273 (1995). </p>
<p> Option <code> -prev</code> produces the comparison with a previous frame the specified number of frames ago. </p>
<p> Option <code> -m</code> produces a matrix in <code> .xpm</code> format of comparison values of each structure in the trajectory with respect to each other structure. This file can be visualized with for instance <code> xv</code> and can be converted to postscript with <code> xpm2ps</code>. </p>
<p> Option <code> -fit</code> controls the least-squares fitting of the structures on top of each other: complete fit (rotation and translation), translation only, or no fitting at all. </p>
<p> Option <code> -mw</code> controls whether mass weighting is done or not. If you select the option (default) and supply a valid tpr file masses will be taken from there, otherwise the masses will be deduced from the atommass.dat file in the GROMACS library directory. This is fine for proteins but not necessarily for other molecules. A default mass of 12.011 amu (Carbon) is assigned to unknown atoms. You can check whether this happend by turning on the <code> -debug</code> flag and inspecting the log file. </p>
<p> With <code> -f2</code>, the &#8216;other structures&#8217; are taken from a second trajectory, this generates a comparison matrix of one trajectory versus the other. </p>
<p> Option <code> -bin</code> does a binary dump of the comparison matrix. </p>
<p> Option <code> -bm</code> produces a matrix of average bond angle deviations analogously to the <code> -m</code> option. Only bonds between atoms in the comparison group are considered.</p>
<h2>FILES</h2>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-f2</code><i> traj.xtc</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> rmsd.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-mir</code><i> rmsdmir.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-a</code><i> avgrp.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-dist</code><i> rmsd-dist.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-m</code><i> rmsd.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-bin</code><i> rmsd.dat</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-bm</code><i> bond.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
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
<p> <code>-what</code><i> enum</i><code> rmsd</code><br />
&nbsp;<wbr>Structural difference measure:&nbsp;<wbr><code>&nbsp;<wbr>rmsd</code>,&nbsp;<wbr><code>&nbsp;<wbr>rho</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>rhosc</code> </p>
<p> <code>-[no]pbc</code><i>yes </i><br />
&nbsp;<wbr>PBC check </p>
<p> <code>-fit</code><i> enum</i><code> rot+trans</code><br />
&nbsp;<wbr>Fit to reference structure:&nbsp;<wbr><code>&nbsp;<wbr>rot+trans</code>,&nbsp;<wbr><code>&nbsp;<wbr>translation</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>none</code> </p>
<p> <code>-prev</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Compare with previous frame </p>
<p> <code>-[no]split</code><i>no </i><br />
&nbsp;<wbr>Split graph where time is zero </p>
<p> <code>-skip</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Only write every nr-th frame to matrix </p>
<p> <code>-skip2</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Only write every nr-th frame to matrix </p>
<p> <code>-max</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Maximum level in comparison matrix </p>
<p> <code>-min</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Minimum level in comparison matrix </p>
<p> <code>-bmax</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Maximum level in bond angle matrix </p>
<p> <code>-bmin</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Minimum level in bond angle matrix </p>
<p> <code>-[no]mw</code><i>yes </i><br />
&nbsp;<wbr>Use mass weighting for superposition </p>
<p> <code>-nlevels</code><i> int</i><code> 80</code><br />
&nbsp;<wbr>Number of levels in the matrices </p>
<p> <code>-ng</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Number of groups to compute RMS between </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
