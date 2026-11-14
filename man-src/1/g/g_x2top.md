---
title: "g_x2top(1)"
name: "g_x2top"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_x2top/"
description: "x2top – generates a primitive topology from coordinates"
---

<h2>NAME</h2>
<p> x2top &#8211; generates a primitive topology from coordinates </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>x2top</code> <code>-f</code><i> conf.gro </i> <code>-o</code><i> out.top </i> <code>-r</code><i> out.rtp </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-ff</code><i> string </i> <code>-[no]v</code><i></i> <code>-nexcl</code><i> int </i> <code>-[no]H14</code><i></i> <code>-[no]alldih</code><i></i> <code>-[no]remdih</code><i></i> <code>-[no]pairs</code><i></i> <code>-name</code><i> string </i> <code>-[no]pbc</code><i></i> <code>-[no]pdbq</code><i></i> <code>-[no]param</code><i></i> <code>-[no]round</code><i></i> <code>-kb</code><i> real </i> <code>-kt</code><i> real </i> <code>-kp</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> x2top generates a primitive topology from a coordinate file. The program assumes all hydrogens are present when defining the hybridization from the atom name and the number of bonds. The program can also make an rtp entry, which you can then add to the rtp database. </p>
<p> When <code> -param</code> is set, equilibrium distances and angles and force constants will be printed in the topology for all interactions. The equilibrium distances and angles are taken from the input coordinates, the force constant are set with command line options.The force fields supported currently are: </p>
<p> G43a1 GROMOS96 43a1 Forcefield (official distribution) </p>
<p> oplsaa OPLS-AA/L all-atom force field (2001 aminoacid dihedrals) </p>
<p> G43b1 GROMOS96 43b1 Vacuum Forcefield (official distribution) </p>
<p> gmx Gromacs Forcefield (a modified GROMOS87, see manual) </p>
<p> G43a2 GROMOS96 43a2 Forcefield (development) (improved alkane dihedrals) </p>
<p> The corresponding data files can be found in the library directory with names like ffXXXX.YYY. Check chapter 5 of the manual for more information about file formats. By default the forcefield selection is interactive, but you can use the <code> -ff</code> option to specify one of the short names above on the command line instead. In that case pdb2gmx just looks for the corresponding file. </p>
<h2>FILES</h2>
<p> <code>-f</code><i> conf.gro</i> <code>Input</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> out.top</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Topology file&nbsp;<wbr> </p>
<p> <code>-r</code><i> out.rtp</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Residue Type file used by pdb2gmx&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-ff</code><i> string</i><code> oplsaa</code><br />
&nbsp;<wbr>Force field for your simulation. Type&nbsp;<wbr>&quot;select&quot;&nbsp;<wbr>for interactive selcection. </p>
<p> <code>-[no]v</code><i>no </i><br />
&nbsp;<wbr>Generate verbose output in the top file. </p>
<p> <code>-nexcl</code><i> int</i><code> 3</code><br />
&nbsp;<wbr>Number of exclusions </p>
<p> <code>-[no]H14</code><i>yes </i><br />
&nbsp;<wbr>Use 3rd neighbour interactions for hydrogen atoms </p>
<p> <code>-[no]alldih</code><i>no </i><br />
&nbsp;<wbr>Generate all proper dihedrals </p>
<p> <code>-[no]remdih</code><i>no </i><br />
&nbsp;<wbr>Remove dihedrals on the same bond as an improper </p>
<p> <code>-[no]pairs</code><i>yes </i><br />
&nbsp;<wbr>Output 1-4 interactions&nbsp;<wbr>(pairs)&nbsp;<wbr>in topology file </p>
<p> <code>-name</code><i> string</i><code> ICE</code><br />
&nbsp;<wbr>Name of your molecule </p>
<p> <code>-[no]pbc</code><i>yes </i><br />
&nbsp;<wbr>Use periodic boundary conditions. </p>
<p> <code>-[no]pdbq</code><i>no </i><br />
&nbsp;<wbr>Use the B-factor supplied in a pdb file for the atomic charges </p>
<p> <code>-[no]param</code><i>yes </i><br />
&nbsp;<wbr>Print parameters in the output </p>
<p> <code>-[no]round</code><i>yes </i><br />
&nbsp;<wbr>Round off measured values </p>
<p> <code>-kb</code><i> real</i><code> 400000</code><br />
&nbsp;<wbr>Bonded force constant&nbsp;<wbr>(kJ/mol/nm2) </p>
<p> <code>-kt</code><i> real</i><code> 400 </code><br />
&nbsp;<wbr>Angle force constant&nbsp;<wbr>(kJ/mol/rad2) </p>
<p> <code>-kp</code><i> real</i><code> 5 </code><br />
&nbsp;<wbr>Dihedral angle force constant&nbsp;<wbr>(kJ/mol/rad2) </p>
<h2>KNOWN PROBLEMS</h2>
<p> &#8211; The atom type selection is primitive. Virtually no chemical knowledge is used </p>
<p> &#8211; Periodic boundary conditions screw up the bonding </p>
<p> &#8211; No improper dihedrals are generated </p>
<p> &#8211; The atoms to atomtype translation table is incomplete (ffG43a1.n2t file in the $GMXLIB directory). Please extend it and send the results back to the GROMACS crew. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
