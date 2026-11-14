---
title: "g_nmeig_d(1)"
name: "g_nmeig_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_nmeig_d/"
description: "g_nmeig – diagonalizes the Hessian"
---

<h2>NAME</h2>
<p> g_nmeig &#8211; diagonalizes the Hessian </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_nmeig</code> <code>-f</code><i> hessian.mtx </i> <code>-s</code><i> topol.tpr </i> <code>-of</code><i> eigenfreq.xvg </i> <code>-ol</code><i> eigenval.xvg </i> <code>-v</code><i> eigenvec.trr </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]xvgr</code><i></i> <code>-[no]m</code><i></i> <code>-first</code><i> int </i> <code>-last</code><i> int </i></p>
<h2>DESCRIPTION</h2>
<p> g_nmeig calculates the eigenvectors/values of a (Hessian) matrix, which can be calculated with <code> mdrun</code>. The eigenvectors are written to a trajectory file (<code> -v</code>). The structure is written first with t=0. The eigenvectors are written as frames with the eigenvector number as timestamp. The eigenvectors can be analyzed with <code> g_anaeig</code>. An ensemble of structures can be generated from the eigenvectors with <code> g_nmens</code>. When mass weighting is used, the generated eigenvectors will be scaled back to plain cartesian coordinates before generating the output &#8211; in this case they will no longer be exactly orthogonal in the standard cartesian norm (But in the mass weighted norm they would be).</p>
<h2>FILES</h2>
<p> <code>-f</code><i> hessian.mtx</i> <code>Input</code><br />
&nbsp;<wbr>Hessian matrix&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-of</code><i> eigenfreq.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ol</code><i> eigenval.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-v</code><i> eigenvec.trr</i> <code>Output</code><br />
&nbsp;<wbr>Full precision trajectory: trr trj cpt&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-[no]m</code><i>yes </i><br />
&nbsp;<wbr>Divide elements of Hessian by product of sqrt(mass)&nbsp;<wbr>of involved atoms prior to diagonalization. This should be used for&nbsp;<wbr>&#8216;Normal Modes&#8217;&nbsp;<wbr>analysis </p>
<p> <code>-first</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>First eigenvector to write away </p>
<p> <code>-last</code><i> int</i><code> 50</code><br />
&nbsp;<wbr>Last eigenvector to write away </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
