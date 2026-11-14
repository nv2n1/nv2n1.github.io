---
title: "g_genrestr_d(1)"
name: "g_genrestr_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_genrestr_d/"
description: "genrestr – generates position restraints or distance restraints for index groups"
---

<h2>NAME</h2>
<p> genrestr &#8211; generates position restraints or distance restraints for index groups </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>genrestr</code> <code>-f</code><i> conf.gro </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> posre.itp </i> <code>-of</code><i> freeze.ndx </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-fc</code><i> vector </i> <code>-freeze</code><i> real </i> <code>-[no]disre</code><i></i> <code>-disre_dist</code><i> real </i> <code>-disre_frac</code><i> real </i> <code>-disre_up2</code><i> real </i> <code>-[no]constr</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> genrestr produces an include file for a topology containing a list of atom numbers and three force constants for the X, Y and Z direction. A single isotropic force constant may be given on the command line instead of three components. </p>
<p> WARNING: position restraints only work for the one molecule at a time. Position restraints are interactions within molecules, therefore they should be included within the correct <code> [ moleculetype ]</code> block in the topology. Since the atom numbers in every moleculetype in the topology start at 1 and the numbers in the input file for genpr number consecutively from 1, genpr will only produce a useful file for the first molecule. </p>
<p> The -of option produces an index file that can be used for freezing atoms. In this case the input file must be a pdb file. </p>
<p> With the <code> -disre</code> option half a matrix of distance restraints is generated instead of position restraints. With this matrix, that one typically would apply to C-alpha atoms in a protein, one can maintain the overall conformation of a protein without tieing it to a specific position (as with position restraints).</p>
<h2>FILES</h2>
<p> <code>-f</code><i> conf.gro</i> <code>Input</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> posre.itp</i> <code>Output</code><br />
&nbsp;<wbr>Include file for topology&nbsp;<wbr> </p>
<p> <code>-of</code><i> freeze.ndx</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-fc</code><i> vector</i><code> 1000 1000 1000</code><br />
&nbsp;<wbr>force constants&nbsp;<wbr>(kJ mol-1 nm-2) </p>
<p> <code>-freeze</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>if the -of option or this one is given an index file will be written containing atom numbers of all atoms that have a B-factor less than the level given here </p>
<p> <code>-[no]disre</code><i>no </i><br />
&nbsp;<wbr>Generate a distance restraint matrix for all the atoms in index </p>
<p> <code>-disre_dist</code><i> real</i><code> 0.1 </code><br />
&nbsp;<wbr>Distance range around the actual distance for generating distance restraints </p>
<p> <code>-disre_frac</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Fraction of distance to be used as interval rather than a fixed distance. If the fraction of the distance that you specify here is less than the distance given in the previous option, that one is used instead. </p>
<p> <code>-disre_up2</code><i> real</i><code> 1 </code><br />
&nbsp;<wbr>Distance between upper bound for distance restraints, and the distance at which the force becomes constant&nbsp;<wbr>(see manual) </p>
<p> <code>-[no]constr</code><i>no </i><br />
&nbsp;<wbr>Generate a constraint matrix rather than distance restraints </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
