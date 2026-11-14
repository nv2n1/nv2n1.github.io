---
title: "g_editconf_d(1)"
name: "g_editconf_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_editconf_d/"
description: "editconf – edits the box and writes subgroups"
---

<h2>NAME</h2>
<p> editconf &#8211; edits the box and writes subgroups </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>editconf</code> <code>-f</code><i> conf.gro </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> out.gro </i> <code>-mead</code><i> mead.pqr </i> <code>-bf</code><i> bfact.dat </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]w</code><i></i> <code>-[no]ndef</code><i></i> <code>-bt</code><i> enum </i> <code>-box</code><i> vector </i> <code>-angles</code><i> vector </i> <code>-d</code><i> real </i> <code>-[no]c</code><i></i> <code>-center</code><i> vector </i> <code>-translate</code><i> vector </i> <code>-rotate</code><i> vector </i> <code>-[no]princ</code><i></i> <code>-scale</code><i> vector </i> <code>-density</code><i> real </i> <code>-[no]vol</code><i></i> <code>-[no]pbc</code><i></i> <code>-[no]grasp</code><i></i> <code>-rvdw</code><i> real </i> <code>-sig56</code><i> real </i> <code>-[no]vdwread</code><i></i> <code>-[no]atom</code><i></i> <code>-[no]legend</code><i></i> <code>-label</code><i> string </i></p>
<h2>DESCRIPTION</h2>
<p> editconf converts generic structure format to <code> .gro</code>, <code> .g96</code> or <code> .pdb</code>. </p>
<p> The box can be modified with options <code> -box</code>, <code> -d</code> and <code> -angles</code>. Both <code> -box</code> and <code> -d</code> will center the system in the box. </p>
<p> Option <code> -bt</code> determines the box type: <code> triclinic</code> is a triclinic box, <code> cubic</code> is a rectangular box with all sides equal <code> dodecahedron</code> represents a rhombic dodecahedron and <code> octahedron</code> is a truncated octahedron. The last two are special cases of a triclinic box. The length of the three box vectors of the truncated octahedron is the shortest distance between two opposite hexagons. The volume of a dodecahedron is 0.71 and that of a truncated octahedron is 0.77 of that of a cubic box with the same periodic image distance. </p>
<p> Option <code> -box</code> requires only one value for a cubic box, dodecahedron and a truncated octahedron. </p>
<p> With <code> -d</code> and a <code> triclinic</code> box the size of the system in the x, y and z directions is used. With <code> -d</code> and <code> cubic</code>, <code> dodecahedron</code> or <code> octahedron</code> boxes, the dimensions are set to the diameter of the system (largest distance between atoms) plus twice the specified distance. </p>
<p> Option <code> -angles</code> is only meaningful with option <code> -box</code> and a triclinic box and can not be used with option <code> -d</code>. </p>
<p> When <code> -n</code> or <code> -ndef</code> is set, a group can be selected for calculating the size and the geometric center, otherwise the whole system is used. </p>
<p> <code> -rotate</code> rotates the coordinates and velocities. </p>
<p> <code> -princ</code> aligns the principal axes of the system along the coordinate axes, this may allow you to decrease the box volume, but beware that molecules can rotate significantly in a nanosecond. </p>
<p> Scaling is applied before any of the other operations are performed. Boxes and coordinates can be scaled to give a certain density (option <code> -density</code>). Note that this may be inaccurate in case a gro file is given as input. A special feature of the scaling option, when the factor -1 is given in one dimension, one obtains a mirror image, mirrored in one of the plains, when one uses -1 in three dimensions a point-mirror image is obtained. </p>
<p> Groups are selected after all operations have been applied. </p>
<p> Periodicity can be removed in a crude manner. It is important that the box sizes at the bottom of your input file are correct when the periodicity is to be removed. </p>
<p> When writing <code> .pdb</code> files, B-factors can be added with the <code> -bf</code> option. B-factors are read from a file with with following format: first line states number of entries in the file, next lines state an index followed by a B-factor. The B-factors will be attached per residue unless an index is larger than the number of residues or unless the <code> -atom</code> option is set. Obviously, any type of numeric data can be added instead of B-factors. <code> -legend</code> will produce a row of CA atoms with B-factors ranging from the minimum to the maximum value found, effectively making a legend for viewing. </p>
<p> With the option -mead a special pdb (pqr) file for the MEAD electrostatics program (Poisson-Boltzmann solver) can be made. A further prerequisite is that the input file is a run input file. The B-factor field is then filled with the Van der Waals radius of the atoms while the occupancy field will hold the charge. </p>
<p> The option -grasp is similar, but it puts the charges in the B-factor and the radius in the occupancy. </p>
<p> Finally with option <code> -label</code> editconf can add a chain identifier to a pdb file, which can be useful for analysis with e.g. rasmol. </p>
<p> To convert a truncated octrahedron file produced by a package which uses a cubic box with the corners cut off (such as Gromos) use: </p>
<p> <code> editconf -f in -rotate 0 45 35.264 -bt o -box veclen -o out</code> </p>
<p> where <code> veclen</code> is the size of the cubic box times <a href="/docs/linux/man/3-sqrt/">sqrt</a>(3)/2.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> conf.gro</i> <code>Input</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> out.gro</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-mead</code><i> mead.pqr</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Coordinate file for MEAD&nbsp;<wbr> </p>
<p> <code>-bf</code><i> bfact.dat</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]ndef</code><i>no </i><br />
&nbsp;<wbr>Choose output from default index groups </p>
<p> <code>-bt</code><i> enum</i><code> triclinic</code><br />
&nbsp;<wbr>Box type for -box and -d:&nbsp;<wbr><code>&nbsp;<wbr>triclinic</code>,&nbsp;<wbr><code>&nbsp;<wbr>cubic</code>,&nbsp;<wbr><code>&nbsp;<wbr>dodecahedron</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>octahedron</code> </p>
<p> <code>-box</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>Box vector lengths&nbsp;<wbr>(a,b,c) </p>
<p> <code>-angles</code><i> vector</i><code> 90 90 90</code><br />
&nbsp;<wbr>Angles between the box vectors&nbsp;<wbr>(bc,ac,ab) </p>
<p> <code>-d</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Distance between the solute and the box </p>
<p> <code>-[no]c</code><i>no </i><br />
&nbsp;<wbr>Center molecule in box&nbsp;<wbr>(implied by -box and -d) </p>
<p> <code>-center</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>Coordinates of geometrical center </p>
<p> <code>-translate</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>Translation </p>
<p> <code>-rotate</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>Rotation around the X, Y and Z axes in degrees </p>
<p> <code>-[no]princ</code><i>no </i><br />
&nbsp;<wbr>Orient molecule(s)&nbsp;<wbr>along their principal axes </p>
<p> <code>-scale</code><i> vector</i><code> 1 1 1</code><br />
&nbsp;<wbr>Scaling factor </p>
<p> <code>-density</code><i> real</i><code> 1000 </code><br />
&nbsp;<wbr>Density&nbsp;<wbr>(g/l)&nbsp;<wbr>of the output box achieved by scaling </p>
<p> <code>-[no]vol</code><i>yes </i><br />
&nbsp;<wbr>Compute and print volume of the box </p>
<p> <code>-[no]pbc</code><i>no </i><br />
&nbsp;<wbr>Remove the periodicity&nbsp;<wbr>(make molecule whole again) </p>
<p> <code>-[no]grasp</code><i>no </i><br />
&nbsp;<wbr>Store the charge of the atom in the B-factor field and the radius of the atom in the occupancy field </p>
<p> <code>-rvdw</code><i> real</i><code> 0.12 </code><br />
&nbsp;<wbr>Default Van der Waals radius&nbsp;<wbr>(in nm)&nbsp;<wbr>if one can not be found in the database or if no parameters are present in the topology file </p>
<p> <code>-sig56</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Use rmin/2&nbsp;<wbr>(minimum in the Van der Waals potential)&nbsp;<wbr>rather than sigma/2&nbsp;<wbr> </p>
<p> <code>-[no]vdwread</code><i>no </i><br />
&nbsp;<wbr>Read the Van der Waals radii from the file vdwradii.dat rather than computing the radii based on the force field </p>
<p> <code>-[no]atom</code><i>no </i><br />
&nbsp;<wbr>Force B-factor attachment per atom </p>
<p> <code>-[no]legend</code><i>no </i><br />
&nbsp;<wbr>Make B-factor legend </p>
<p> <code>-label</code><i> string</i><code> A</code><br />
&nbsp;<wbr>Add chain label for all residues </p>
<h2>KNOWN PROBLEMS</h2>
<p> &#8211; For complex molecules, the periodicity removal routine may break down, in that case you can use trjconv </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
