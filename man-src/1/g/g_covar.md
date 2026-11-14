---
title: "g_covar(1)"
name: "g_covar"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_covar/"
description: "g_covar – calculates and diagonalizes the covariance matrix"
---

<h2>NAME</h2>
<p> g_covar &#8211; calculates and diagonalizes the covariance matrix </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_covar</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> eigenval.xvg </i> <code>-v</code><i> eigenvec.trr </i> <code>-av</code><i> average.pdb </i> <code>-l</code><i> covar.log </i> <code>-ascii</code><i> covar.dat </i> <code>-xpm</code><i> covar.xpm </i> <code>-xpma</code><i> covara.xpm </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-tu</code><i> enum </i> <code>-[no]xvgr</code><i></i> <code>-[no]fit</code><i></i> <code>-[no]ref</code><i></i> <code>-[no]mwa</code><i></i> <code>-last</code><i> int </i> <code>-[no]pbc</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> <code> g_covar</code> calculates and diagonalizes the (mass-weighted) covariance matrix. All structures are fitted to the structure in the structure file. When this is not a run input file periodicity will not be taken into account. When the fit and analysis groups are identical and the analysis is non mass-weighted, the fit will also be non mass-weighted. </p>
<p> The eigenvectors are written to a trajectory file (<code> -v</code>). When the same atoms are used for the fit and the covariance analysis, the reference structure for the fit is written first with t=-1. The average (or reference when <code> -ref</code> is used) structure is written with t=0, the eigenvectors are written as frames with the eigenvector number as timestamp. </p>
<p> The eigenvectors can be analyzed with <code> g_anaeig</code>. </p>
<p> Option <code> -ascii</code> writes the whole covariance matrix to an ASCII file. The order of the elements is: x1x1, x1y1, x1z1, x1x2, &#8230; </p>
<p> Option <code> -xpm</code> writes the whole covariance matrix to an xpm file. </p>
<p> Option <code> -xpma</code> writes the atomic covariance matrix to an xpm file, i.e. for each atom pair the sum of the xx, yy and zz covariances is written.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> eigenval.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-v</code><i> eigenvec.trr</i> <code>Output</code><br />
&nbsp;<wbr>Full precision trajectory: trr trj cpt&nbsp;<wbr> </p>
<p> <code>-av</code><i> average.pdb</i> <code>Output</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-l</code><i> covar.log</i> <code>Output</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
<p> <code>-ascii</code><i> covar.dat</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-xpm</code><i> covar.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-xpma</code><i> covara.xpm</i> <code>Output, Opt.</code><br />
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
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-[no]fit</code><i>yes </i><br />
&nbsp;<wbr>Fit to a reference structure </p>
<p> <code>-[no]ref</code><i>no </i><br />
&nbsp;<wbr>Use the deviation from the conformation in the structure file instead of from the average </p>
<p> <code>-[no]mwa</code><i>no </i><br />
&nbsp;<wbr>Mass-weighted covariance analysis </p>
<p> <code>-last</code><i> int</i><code> -1</code><br />
&nbsp;<wbr>Last eigenvector to write away&nbsp;<wbr>(-1 is till the last) </p>
<p> <code>-[no]pbc</code><i>yes </i><br />
&nbsp;<wbr>Apply corrections for periodic boundary conditions </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
