---
title: "g_genion_d(1)"
name: "g_genion_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_genion_d/"
description: "genion – generates mono atomic ions on energetically favorable positions"
---

<h2>NAME</h2>
<p> genion &#8211; generates mono atomic ions on energetically favorable positions </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>genion</code> <code>-s</code><i> topol.tpr </i> <code>-table</code><i> table.xvg </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> out.gro </i> <code>-g</code><i> genion.log </i> <code>-pot</code><i> pot.pdb </i> <code>-p</code><i> topol.top </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]xvgr</code><i></i> <code>-np</code><i> int </i> <code>-pname</code><i> string </i> <code>-pq</code><i> int </i> <code>-nn</code><i> int </i> <code>-nname</code><i> string </i> <code>-nq</code><i> int </i> <code>-rmin</code><i> real </i> <code>-[no]random</code><i></i> <code>-seed</code><i> int </i> <code>-scale</code><i> real </i> <code>-conc</code><i> real </i> <code>-[no]neutral</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> genion replaces solvent molecules by monoatomic ions at the position of the first atoms with the most favorable electrostatic potential or at random. The potential is calculated on all atoms, using normal GROMACS particle based methods (in contrast to other methods based on solving the Poisson-Boltzmann equation). The potential is recalculated after every ion insertion. If specified in the run input file, a reaction field, shift function or user function can be used. For the user function a table file can be specified with the option <code> -table</code>. The group of solvent molecules should be continuous and all molecules should have the same number of atoms. The user should add the ion molecules to the topology file and include the file <code> ions.itp</code>. Ion names for Gromos96 should include the charge. </p>
<p> With the option <code> -pot</code> the potential can be written as B-factors in a pdb file (for visualisation using e.g. rasmol). The unit of the potential is 1000 kJ/(mol e), the scaling be changed with the <code> -scale</code> option. </p>
<p> For larger ions, e.g. sulfate we recommended to use genbox.</p>
<h2>FILES</h2>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-table</code><i> table.xvg</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> out.gro</i> <code>Output</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-g</code><i> genion.log</i> <code>Output</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
<p> <code>-pot</code><i> pot.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-p</code><i> topol.top</i> <code>In/Out, Opt.</code><br />
&nbsp;<wbr>Topology file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-np</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Number of positive ions </p>
<p> <code>-pname</code><i> string</i><code> Na</code><br />
&nbsp;<wbr>Name of the positive ion </p>
<p> <code>-pq</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Charge of the positive ion </p>
<p> <code>-nn</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Number of negative ions </p>
<p> <code>-nname</code><i> string</i><code> Cl</code><br />
&nbsp;<wbr>Name of the negative ion </p>
<p> <code>-nq</code><i> int</i><code> -1</code><br />
&nbsp;<wbr>Charge of the negative ion </p>
<p> <code>-rmin</code><i> real</i><code> 0.6 </code><br />
&nbsp;<wbr>Minimum distance between ions </p>
<p> <code>-[no]random</code><i>yes </i><br />
&nbsp;<wbr>Use random placement of ions instead of based on potential. The rmin option should still work </p>
<p> <code>-seed</code><i> int</i><code> 1993</code><br />
&nbsp;<wbr>Seed for random number generator </p>
<p> <code>-scale</code><i> real</i><code> 0.001 </code><br />
&nbsp;<wbr>Scaling factor for the potential for -pot </p>
<p> <code>-conc</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Specify salt concentration&nbsp;<wbr>(mol/liter). This will add sufficient ions to reach up to the specified concentration as computed from the volume of the cell in the input tpr file. Overrides the -np and&nbsp;<wbr>&nbsp;<wbr>nn options. </p>
<p> <code>-[no]neutral</code><i>no </i><br />
&nbsp;<wbr>This option will add enough ions to neutralize the system. In combination with the concentration option a neutral system at a given salt concentration will be generated. </p>
<h2>KNOWN PROBLEMS</h2>
<p> &#8211; Calculation of the potential is not reliable, therefore the <code> -random</code> option is now turned on by default. </p>
<p> &#8211; If you specify a salt concentration existing ions are not taken into account. In effect you therefore specify the amount of salt to be added. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
