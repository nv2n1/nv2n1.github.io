---
title: "g_pdb2gmx_d(1)"
name: "g_pdb2gmx_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_pdb2gmx_d/"
description: "pdb2gmx – converts pdb files to topology and coordinate files"
---

<h2>NAME</h2>
<p> pdb2gmx &#8211; converts pdb files to topology and coordinate files </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>pdb2gmx</code> <code>-f</code><i> eiwit.pdb </i> <code>-o</code><i> conf.gro </i> <code>-p</code><i> topol.top </i> <code>-i</code><i> posre.itp </i> <code>-n</code><i> clean.ndx </i> <code>-q</code><i> clean.pdb </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]merge</code><i></i> <code>-ff</code><i> string </i> <code>-water</code><i> enum </i> <code>-[no]inter</code><i></i> <code>-[no]ss</code><i></i> <code>-[no]ter</code><i></i> <code>-[no]lys</code><i></i> <code>-[no]arg</code><i></i> <code>-[no]asp</code><i></i> <code>-[no]glu</code><i></i> <code>-[no]gln</code><i></i> <code>-[no]his</code><i></i> <code>-angle</code><i> real </i> <code>-dist</code><i> real </i> <code>-[no]una</code><i></i> <code>-[no]ignh</code><i></i> <code>-[no]missing</code><i></i> <code>-[no]v</code><i></i> <code>-posrefc</code><i> real </i> <code>-vsite</code><i> enum </i> <code>-[no]heavyh</code><i></i> <code>-[no]deuterate</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> This program reads a pdb file, reads some database files, adds hydrogens to the molecules and generates coordinates in Gromacs (Gromos) format and a topology in Gromacs format. These files can subsequently be processed to generate a run input file. </p>
<p> The force fields in the distribution are currently: </p>
<p> oplsaa OPLS-AA/L all-atom force field (2001 aminoacid dihedrals) </p>
<p> G43b1 GROMOS96 43b1 Vacuum Forcefield </p>
<p> G43a1 GROMOS96 43a1 Forcefield </p>
<p> G43a2 GROMOS96 43a2 Forcefield (improved alkane dihedrals) </p>
<p> G45a3 GROMOS96 45a3 Forcefield </p>
<p> G53a5 GROMOS96 53a5 Forcefield </p>
<p> G53a6 GROMOS96 53a6 Forcefield </p>
<p> gmx Gromacs Forcefield (a modified GROMOS87, see manual) </p>
<p> encads Encad all-atom force field, using scaled-down vacuum charges </p>
<p> encadv Encad all-atom force field, using full solvent charges </p>
<p> The corresponding data files can be found in the library directory with names like ffXXXX.YYY. Check chapter 5 of the manual for more information about file formats. By default the forcefield selection is interactive, but you can use the <code> -ff</code> option to specify one of the short names above on the command line instead. In that case pdb2gmx just looks for the corresponding file. </p>
<p> Note that a pdb file is nothing more than a file format, and it need not necessarily contain a protein structure. Every kind of molecule for which there is support in the database can be converted. If there is no support in the database, you can add it yourself. </p>
<p> The program has limited intelligence, it reads a number of database files, that allow it to make special bonds (Cys-Cys, Heme-His, etc.), if necessary this can be done manually. The program can prompt the user to select which kind of LYS, ASP, GLU, CYS or HIS residue she wants. For LYS the choice is between LYS (two protons on NZ) or LYSH (three protons, default), for ASP and GLU unprotonated (default) or protonated, for HIS the proton can be either on ND1 (HISA), on NE2 (HISB) or on both (HISH). By default these selections are done automatically. For His, this is based on an optimal hydrogen bonding conformation. Hydrogen bonds are defined based on a simple geometric criterium, specified by the maximum hydrogen-donor-acceptor angle and donor-acceptor distance, which are set by <code> -angle</code> and <code> -dist</code> respectively. </p>
<p> Option <code> -merge</code> will ask if you want to merge consecutive chains into one molecule definition, this can be useful for connecting chains with a disulfide brigde or intermolecular distance restraints. </p>
<p> pdb2gmx will also check the occupancy field of the pdb file. If any of the occupanccies are not one, indicating that the atom is not resolved well in the structure, a warning message is issued. When a pdb file does not originate from an X-Ray structure determination all occupancy fields may be zero. Either way, it is up to the user to verify the correctness of the input data (read the article!). </p>
<p> During processing the atoms will be reordered according to Gromacs conventions. With <code> -n</code> an index file can be generated that contains one group reordered in the same way. This allows you to convert a Gromos trajectory and coordinate file to Gromos. There is one limitation: reordering is done after the hydrogens are stripped from the input and before new hydrogens are added. This means that you should not use <code> -ignh</code>. </p>
<p> The <code> .gro</code> and <code> .g96</code> file formats do not support chain identifiers. Therefore it is useful to enter a pdb file name at the <code> -o</code> option when you want to convert a multichain pdb file. </p>
<p> The option <code> -vsite</code> removes hydrogen and fast improper dihedral motions. Angular and out-of-plane motions can be removed by changing hydrogens into virtual sites and fixing angles, which fixes their position relative to neighboring atoms. Additionally, all atoms in the aromatic rings of the standard amino acids (i.e. PHE, TRP, TYR and HIS) can be converted into virtual sites, elminating the fast improper dihedral fluctuations in these rings. Note that in this case all other hydrogen atoms are also converted to virtual sites. The mass of all atoms that are converted into virtual sites, is added to the heavy atoms. </p>
<p> Also slowing down of dihedral motion can be done with <code> -heavyh</code> done by increasing the hydrogen-mass by a factor of 4. This is also done for water hydrogens to slow down the rotational motion of water. The increase in mass of the hydrogens is subtracted from the bonded (heavy) atom so that the total mass of the system remains the same.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> eiwit.pdb</i> <code>Input</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> conf.gro</i> <code>Output</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-p</code><i> topol.top</i> <code>Output</code><br />
&nbsp;<wbr>Topology file&nbsp;<wbr> </p>
<p> <code>-i</code><i> posre.itp</i> <code>Output</code><br />
&nbsp;<wbr>Include file for topology&nbsp;<wbr> </p>
<p> <code>-n</code><i> clean.ndx</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-q</code><i> clean.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]merge</code><i>no </i><br />
&nbsp;<wbr>Merge chains into one molecule definition </p>
<p> <code>-ff</code><i> string</i><code> select</code><br />
&nbsp;<wbr>Force field, interactive by default. Use -h for information. </p>
<p> <code>-water</code><i> enum</i><code> spc</code><br />
&nbsp;<wbr>Water model to use: with GROMOS we recommend SPC, with OPLS, TIP4P:&nbsp;<wbr><code>&nbsp;<wbr>spc</code>,&nbsp;<wbr><code>&nbsp;<wbr>spce</code>,&nbsp;<wbr><code>&nbsp;<wbr>tip3p</code>,&nbsp;<wbr><code>&nbsp;<wbr>tip4p</code>,&nbsp;<wbr><code>&nbsp;<wbr>tip5p</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>f3c</code> </p>
<p> <code>-[no]inter</code><i>no </i><br />
&nbsp;<wbr>Set the next 8 options to interactive </p>
<p> <code>-[no]ss</code><i>no </i><br />
&nbsp;<wbr>Interactive SS bridge selection </p>
<p> <code>-[no]ter</code><i>no </i><br />
&nbsp;<wbr>Interactive termini selection, iso charged </p>
<p> <code>-[no]lys</code><i>no </i><br />
&nbsp;<wbr>Interactive Lysine selection, iso charged </p>
<p> <code>-[no]arg</code><i>no </i><br />
&nbsp;<wbr>Interactive Arganine selection, iso charged </p>
<p> <code>-[no]asp</code><i>no </i><br />
&nbsp;<wbr>Interactive Aspartic Acid selection, iso charged </p>
<p> <code>-[no]glu</code><i>no </i><br />
&nbsp;<wbr>Interactive Glutamic Acid selection, iso charged </p>
<p> <code>-[no]gln</code><i>no </i><br />
&nbsp;<wbr>Interactive Glutamine selection, iso neutral </p>
<p> <code>-[no]his</code><i>no </i><br />
&nbsp;<wbr>Interactive Histidine selection, iso checking H-bonds </p>
<p> <code>-angle</code><i> real</i><code> 135 </code><br />
&nbsp;<wbr>Minimum hydrogen-donor-acceptor angle for a H-bond&nbsp;<wbr>(degrees) </p>
<p> <code>-dist</code><i> real</i><code> 0.3 </code><br />
&nbsp;<wbr>Maximum donor-acceptor distance for a H-bond&nbsp;<wbr>(nm) </p>
<p> <code>-[no]una</code><i>no </i><br />
&nbsp;<wbr>Select aromatic rings with united CH atoms on Phenylalanine, Tryptophane and Tyrosine </p>
<p> <code>-[no]ignh</code><i>no </i><br />
&nbsp;<wbr>Ignore hydrogen atoms that are in the pdb file </p>
<p> <code>-[no]missing</code><i>no </i><br />
&nbsp;<wbr>Continue when atoms are missing, dangerous </p>
<p> <code>-[no]v</code><i>no </i><br />
&nbsp;<wbr>Be slightly more verbose in messages </p>
<p> <code>-posrefc</code><i> real</i><code> 1000 </code><br />
&nbsp;<wbr>Force constant for position restraints </p>
<p> <code>-vsite</code><i> enum</i><code> none</code><br />
&nbsp;<wbr>Convert atoms to virtual sites:&nbsp;<wbr><code>&nbsp;<wbr>none</code>,&nbsp;<wbr><code>&nbsp;<wbr>hydrogens</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>aromatics</code> </p>
<p> <code>-[no]heavyh</code><i>no </i><br />
&nbsp;<wbr>Make hydrogen atoms heavy </p>
<p> <code>-[no]deuterate</code><i>no </i><br />
&nbsp;<wbr>Change the mass of hydrogens to 2 amu </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
