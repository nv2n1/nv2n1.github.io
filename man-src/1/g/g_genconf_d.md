---
title: "g_genconf_d(1)"
name: "g_genconf_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_genconf_d/"
description: "genconf – multiplies a conformation in ‘random’ orientations"
---

<h2>NAME</h2>
<p> genconf &#8211; multiplies a conformation in &#8216;random&#8217; orientations </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>genconf</code> <code>-f</code><i> conf.gro </i> <code>-o</code><i> out.gro </i> <code>-trj</code><i> traj.xtc </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-nbox</code><i> vector </i> <code>-dist</code><i> vector </i> <code>-seed</code><i> int </i> <code>-[no]rot</code><i></i> <code>-[no]shuffle</code><i></i> <code>-[no]sort</code><i></i> <code>-block</code><i> int </i> <code>-nmolat</code><i> int </i> <code>-maxrot</code><i> vector </i> <code>-[no]renumber</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> genconf multiplies a given coordinate file by simply stacking them on top of each other, like a small child playing with wooden blocks. The program makes a grid of <i> user defined</i> proportions (<code> -nbox</code>), and interspaces the grid point with an extra space <code> -dist</code>. </p>
<p> When option <code> -rot</code> is used the program does not check for overlap between molecules on grid points. It is recommended to make the box in the input file at least as big as the coordinates + Van der Waals radius. </p>
<p> If the optional trajectory file is given, conformations are not generated, but read from this file and translated appropriately to build the grid.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> conf.gro</i> <code>Input</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> out.gro</i> <code>Output</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-trj</code><i> traj.xtc</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-nbox</code><i> vector</i><code> 1 1 1</code><br />
&nbsp;<wbr>Number of boxes </p>
<p> <code>-dist</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>Distance between boxes </p>
<p> <code>-seed</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Random generator seed, if 0 generated from the time </p>
<p> <code>-[no]rot</code><i>no </i><br />
&nbsp;<wbr>Randomly rotate conformations </p>
<p> <code>-[no]shuffle</code><i>no </i><br />
&nbsp;<wbr>Random shuffling of molecules </p>
<p> <code>-[no]sort</code><i>no </i><br />
&nbsp;<wbr>Sort molecules on X coord </p>
<p> <code>-block</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Divide the box in blocks on this number of cpus </p>
<p> <code>-nmolat</code><i> int</i><code> 3</code><br />
&nbsp;<wbr>Number of atoms per molecule, assumed to start from 0. If you set this wrong, it will screw up your system! </p>
<p> <code>-maxrot</code><i> vector</i><code> 90 90 90</code><br />
&nbsp;<wbr>Maximum random rotation </p>
<p> <code>-[no]renumber</code><i>yes </i><br />
&nbsp;<wbr>Renumber residues </p>
<h2>KNOWN PROBLEMS</h2>
<p> &#8211; The program should allow for random displacement off lattice points. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
