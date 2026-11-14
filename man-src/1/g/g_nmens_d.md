---
title: "g_nmens_d(1)"
name: "g_nmens_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_nmens_d/"
description: "g_nmens – generates an ensemble of structures from the normal modes"
---

<h2>NAME</h2>
<p> g_nmens &#8211; generates an ensemble of structures from the normal modes </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_nmens</code> <code>-v</code><i> eigenvec.trr </i> <code>-e</code><i> eigenval.xvg </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> ensemble.xtc </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]xvgr</code><i></i> <code>-temp</code><i> real </i> <code>-seed</code><i> int </i> <code>-num</code><i> int </i> <code>-first</code><i> int </i> <code>-last</code><i> int </i></p>
<h2>DESCRIPTION</h2>
<p> <code> g_nmens</code> generates an ensemble around an average structure in a subspace which is defined by a set of normal modes (eigenvectors). The eigenvectors are assumed to be mass-weighted. The position along each eigenvector is randomly taken from a Gaussian distribution with variance kT/eigenvalue. </p>
<p> By default the starting eigenvector is set to 7, since the first six normal modes are the translational and rotational degrees of freedom.</p>
<h2>FILES</h2>
<p> <code>-v</code><i> eigenvec.trr</i> <code>Input</code><br />
&nbsp;<wbr>Full precision trajectory: trr trj cpt&nbsp;<wbr> </p>
<p> <code>-e</code><i> eigenval.xvg</i> <code>Input</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> ensemble.xtc</i> <code>Output</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-temp</code><i> real</i><code> 300 </code><br />
&nbsp;<wbr>Temperature in Kelvin </p>
<p> <code>-seed</code><i> int</i><code> -1</code><br />
&nbsp;<wbr>Random seed, -1 generates a seed from time and pid </p>
<p> <code>-num</code><i> int</i><code> 100</code><br />
&nbsp;<wbr>Number of structures to generate </p>
<p> <code>-first</code><i> int</i><code> 7</code><br />
&nbsp;<wbr>First eigenvector to use&nbsp;<wbr>(-1 is select) </p>
<p> <code>-last</code><i> int</i><code> -1</code><br />
&nbsp;<wbr>Last eigenvector to use&nbsp;<wbr>(-1 is till the last) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
