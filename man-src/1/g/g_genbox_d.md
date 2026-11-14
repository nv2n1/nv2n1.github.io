---
title: "g_genbox_d(1)"
name: "g_genbox_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_genbox_d/"
description: "genbox – solvates a system"
---

<h2>NAME</h2>
<p> genbox &#8211; solvates a system </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>genbox</code> <code>-cp</code><i> protein.gro </i> <code>-cs</code><i> spc216.gro </i> <code>-ci</code><i> insert.gro </i> <code>-o</code><i> out.gro </i> <code>-p</code><i> topol.top </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-box</code><i> vector </i> <code>-nmol</code><i> int </i> <code>-try</code><i> int </i> <code>-seed</code><i> int </i> <code>-vdwd</code><i> real </i> <code>-shell</code><i> real </i> <code>-maxsol</code><i> int </i> <code>-[no]vel</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> Genbox can do one of 3 things: </p>
<p> 1) Generate a box of solvent. Specify -cs and -box. Or specify -cs and -cp with a structure file with a box, but without atoms. </p>
<p> 2) Solvate a solute configuration, eg. a protein, in a bath of solvent molecules. Specify <code> -cp</code> (solute) and <code> -cs</code> (solvent). The box specified in the solute coordinate file (<code> -cp</code>) is used, unless <code> -box</code> is set. If you want the solute to be centered in the box, the program <code> editconf</code> has sophisticated options to change the box dimensions and center the solute. Solvent molecules are removed from the box where the distance between any atom of the solute molecule(s) and any atom of the solvent molecule is less than the sum of the VanderWaals radii of both atoms. A database (<code> vdwradii.dat</code>) of VanderWaals radii is read by the program, atoms not in the database are assigned a default distance <code> -vdw</code>. </p>
<p> 3) Insert a number (<code> -nmol</code>) of extra molecules (<code> -ci</code>) at random positions. The program iterates until <code> nmol</code> molecules have been inserted in the box. To test whether an insertion is successful the same VanderWaals criterium is used as for removal of solvent molecules. When no appropriately sized holes (holes that can hold an extra molecule) are available the program tries for <code> -nmol</code> * <code> -try</code> times before giving up. Increase -try if you have several small holes to fill. </p>
<p> The default solvent is Simple Point Charge water (SPC), with coordinates from <code> $GMXLIB/spc216.gro</code>. Other solvents are also supported, as well as mixed solvents. The only restriction to solvent types is that a solvent molecule consists of exactly one residue. The residue information in the coordinate files is used, and should therefore be more or less consistent. In practice this means that two subsequent solvent molecules in the solvent coordinate file should have different residue number. The box of solute is built by stacking the coordinates read from the coordinate file. This means that these coordinates should be equlibrated in periodic boundary conditions to ensure a good alignment of molecules on the stacking interfaces. </p>
<p> The program can optionally rotate the solute molecule to align the longest molecule axis along a box edge. This way the amount of solvent molecules necessary is reduced. It should be kept in mind that this only works for short simulations, as eg. an alpha-helical peptide in solution can rotate over 90 degrees, within 500 ps. In general it is therefore better to make a more or less cubic box. </p>
<p> Setting -shell larger than zero will place a layer of water of the specified thickness (nm) around the solute. Hint: it is a good idea to put the protein in the center of a box first (using editconf). </p>
<p> Finally, genbox will optionally remove lines from your topology file in which a number of solvent molecules is already added, and adds a line with the total number of solvent molecules in your coordinate file.</p>
<h2>FILES</h2>
<p> <code>-cp</code><i> protein.gro</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-cs</code><i> spc216.gro</i> <code>Input, Opt., Lib.</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-ci</code><i> insert.gro</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> out.gro</i> <code>Output</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-p</code><i> topol.top</i> <code>In/Out, Opt.</code><br />
&nbsp;<wbr>Topology file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-box</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>box size </p>
<p> <code>-nmol</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>no of extra molecules to insert </p>
<p> <code>-try</code><i> int</i><code> 10</code><br />
&nbsp;<wbr>try inserting -nmol*-try times </p>
<p> <code>-seed</code><i> int</i><code> 1997</code><br />
&nbsp;<wbr>random generator seed </p>
<p> <code>-vdwd</code><i> real</i><code> 0.105 </code><br />
&nbsp;<wbr>default vdwaals distance </p>
<p> <code>-shell</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>thickness of optional water layer around solute </p>
<p> <code>-maxsol</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>maximum number of solvent molecules to add if they fit in the box. If zero&nbsp;<wbr>(default)&nbsp;<wbr>this is ignored </p>
<p> <code>-[no]vel</code><i>no </i><br />
&nbsp;<wbr>keep velocities from input solute and solvent </p>
<h2>KNOWN PROBLEMS</h2>
<p> &#8211; Molecules must be whole in the initial configurations. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
