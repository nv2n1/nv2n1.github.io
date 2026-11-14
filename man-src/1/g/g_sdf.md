---
title: "g_sdf(1)"
name: "g_sdf"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_sdf/"
description: "g_sdf – calculates the spatial distribution function (faster than g_spatial)"
---

<h2>NAME</h2>
<p> g_sdf &#8211; calculates the spatial distribution function (faster than g_spatial) </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_sdf</code> <code>-f</code><i> traj.xtc </i> <code>-n</code><i> index.ndx </i> <code>-s</code><i> topol.tpr </i> <code>-o</code><i> gom_plt.dat </i> <code>-r</code><i> refmol.gro </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-mode</code><i> int </i> <code>-triangle</code><i> vector </i> <code>-dtri</code><i> vector </i> <code>-bin</code><i> real </i> <code>-grid</code><i> vector </i></p>
<h2>DESCRIPTION</h2>
<p> g_sdf calculates the spatial distribution function (SDF) of a set of atoms within a coordinate system defined by three atoms. There is single body, two body and three body SDF implemented (select with option -mode). In the single body case the local coordinate system is defined by using a triple of atoms from one single molecule, for the two and three body case the configurations are dynamically searched complexes of two or three molecules (or residues) meeting certain distance consitions (see below). </p>
<p> The program needs a trajectory, a GROMACS run input file and an index file to work. You have to setup 4 groups in the index file before using g_sdf: </p>
<p> The first three groups are used to define the SDF coordinate system. The programm will dynamically generate the atom tripels according to the selected -mode: In -mode 1 the triples will be just the 1st, 2nd, 3rd, &#8230; atoms from groups 1, 2 and 3. Hence the nth entries in groups 1, 2 and 3 must be from the same residue. In -mode 2 the triples will be 1st, 2nd, 3rd, &#8230; atoms from groups 1 and 2 (with the nth entries in groups 1 and 2 having the same res-id). For each pair from groups 1 and 2 group 3 is searched for an atom meeting the distance conditions set with -triangle and -dtri relative to atoms 1 and 2. In -mode 3 for each atom in group 1 group 2 is searched for an atom meeting the distance condition and if a pair is found group 3 is searched for an atom meeting the further conditions. The triple will only be used if all three atoms have different res-id&#8217;s. </p>
<p> The local coordinate system is always defined using the following scheme: Atom 1 will be used as the point of origin for the SDF. Atom 1 and 2 will define the principle axis (Z) of the coordinate system. The other two axis will be defined inplane (Y) and normal (X) to the plane through Atoms 1, 2 and 3. The fourth group contains the atoms for which the SDF will be evaluated. </p>
<p> For -mode 2 and 3 you have to define the distance conditions for the 2 resp. 3 molecule complexes to be searched for using -triangle and -dtri. </p>
<p> The SDF will be sampled in cartesian coordinates. Use &#8216;-grid x y z&#8217; to define the size of the SDF grid around the reference molecule. The Volume of the SDF grid will be V=x*y*z (nm3). Use -bin to set the binwidth for grid. </p>
<p> The output will be a binary 3D-grid file (gom_plt.dat) in the .plt format that can be be read directly by gOpenMol. The option -r will generate a .gro file with the reference molecule(s) transfered to the SDF coordinate system. Load this file into gOpenMol and display the SDF as a contour plot (see <a rel="nofollow" href="http://www.csc.fi/gopenmol/index.phtml">http://www.csc.fi/gopenmol/index.phtml</a> for further documentation). </p>
<p> For further information about SDF&#8217;s have a look at: A. Vishnyakov, JPC A, 105, 2001, 1702 and the references cited within.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-o</code><i> gom_plt.dat</i> <code>Output</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-r</code><i> refmol.gro</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
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
<p> <code>-mode</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>SDF in&nbsp;<wbr>[1,2,3]&nbsp;<wbr>particle mode </p>
<p> <code>-triangle</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>r(1,3), r(2,3), r(1,2) </p>
<p> <code>-dtri</code><i> vector</i><code> 0.03 0.03 0.03</code><br />
&nbsp;<wbr>dr(1,3), dr(2,3), dr(1,2) </p>
<p> <code>-bin</code><i> real</i><code> 0.05 </code><br />
&nbsp;<wbr>Binwidth for the 3D-grid&nbsp;<wbr>(nm) </p>
<p> <code>-grid</code><i> vector</i><code> 1 1 1</code><br />
&nbsp;<wbr>Size of the 3D-grid&nbsp;<wbr>(nm,nm,nm) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
