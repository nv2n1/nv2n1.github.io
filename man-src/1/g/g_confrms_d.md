---
title: "g_confrms_d(1)"
name: "g_confrms_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_confrms_d/"
description: "g_confrms – fits two structures and calculates the rmsd"
---

<h2>NAME</h2>
<p> g_confrms &#8211; fits two structures and calculates the rmsd </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_confrms</code> <code>-f1</code><i> conf1.gro </i> <code>-f2</code><i> conf2.gro </i> <code>-o</code><i> fit.pdb </i> <code>-n1</code><i> fit1.ndx </i> <code>-n2</code><i> fit2.ndx </i> <code>-no</code><i> match.ndx </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]w</code><i></i> <code>-[no]one</code><i></i> <code>-[no]mw</code><i></i> <code>-[no]pbc</code><i></i> <code>-[no]fit</code><i></i> <code>-[no]name</code><i></i> <code>-[no]label</code><i></i> <code>-[no]bfac</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_confrms computes the root mean square deviation (RMSD) of two structures after LSQ fitting the second structure on the first one. The two structures do NOT need to have the same number of atoms, only the two index groups used for the fit need to be identical. With <code> -name</code> only matching atom names from the selected groups will be used for the fit and RMSD calculation. This can be useful when comparing mutants of a protein. </p>
<p> The superimposed structures are written to file. In a <code> .pdb</code> file the two structures will be written as separate models (use <code> rasmol -nmrpdb</code>). Also in a <code> .pdb</code> file, B-factors calculated from the atomic MSD values can be written with <code> -bfac</code>.</p>
<h2>FILES</h2>
<p> <code>-f1</code><i> conf1.gro</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-f2</code><i> conf2.gro</i> <code>Input</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> fit.pdb</i> <code>Output</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n1</code><i> fit1.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-n2</code><i> fit2.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-no</code><i> match.ndx</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]one</code><i>no </i><br />
&nbsp;<wbr>Only write the fitted structure to file </p>
<p> <code>-[no]mw</code><i>yes </i><br />
&nbsp;<wbr>Mass-weighted fitting and RMSD </p>
<p> <code>-[no]pbc</code><i>no </i><br />
&nbsp;<wbr>Try to make molecules whole again </p>
<p> <code>-[no]fit</code><i>yes </i><br />
&nbsp;<wbr>Do least squares superposition of the target structure to the reference </p>
<p> <code>-[no]name</code><i>no </i><br />
&nbsp;<wbr>Only compare matching atom names </p>
<p> <code>-[no]label</code><i>no </i><br />
&nbsp;<wbr>Added chain labels A for first and B for second structure </p>
<p> <code>-[no]bfac</code><i>no </i><br />
&nbsp;<wbr>Output B-factors from atomic MSD values </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
