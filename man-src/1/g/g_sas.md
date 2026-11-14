---
title: "g_sas(1)"
name: "g_sas"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_sas/"
description: "g_sas – computes solvent accessible surface area"
---

<h2>NAME</h2>
<p> g_sas &#8211; computes solvent accessible surface area </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_sas</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-o</code><i> area.xvg </i> <code>-or</code><i> resarea.xvg </i> <code>-oa</code><i> atomarea.xvg </i> <code>-tv</code><i> volume.xvg </i> <code>-q</code><i> connelly.pdb </i> <code>-n</code><i> index.ndx </i> <code>-i</code><i> surfat.itp </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-probe</code><i> real </i> <code>-ndots</code><i> int </i> <code>-qmax</code><i> real </i> <code>-[no]f_index</code><i></i> <code>-minarea</code><i> real </i> <code>-[no]pbc</code><i></i> <code>-[no]prot</code><i></i> <code>-dgs</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_sas computes hydrophobic, hydrophilic and total solvent accessible surface area. As a side effect the Connolly surface can be generated as well in a pdb file where the nodes are represented as atoms and the vertices connecting the nearest nodes as CONECT records. The program will ask for a group for the surface calculation and a group for the output. The calculation group should always consists of all the non-solvent atoms in the system. The output group can be the whole or part of the calculation group. The area can be plotted per residue and atom as well (options <code> -or</code> and <code> -oa</code>). In combination with the latter option an <code> itp</code> file can be generated (option <code> -i</code>) which can be used to restrain surface atoms. </p>
<p> By default, periodic boundary conditions are taken into account, this can be turned off using the <code> -nopbc</code> option. </p>
<p> With the <code> -tv</code> option the total volume and density of the molecule can be computed. Please consider whether the normal probe radius is appropriate in this case or whether you would rather use e.g. 0. It is good to keep in mind that the results for volume and density are very approximate, in e.g. ice Ih one can easily fit water molecules in the pores which would yield too low volume, too high surface area and too high density.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> area.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-or</code><i> resarea.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oa</code><i> atomarea.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-tv</code><i> volume.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-q</code><i> connelly.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-i</code><i> surfat.itp</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Include file for topology&nbsp;<wbr> </p>
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
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-probe</code><i> real</i><code> 0.14 </code><br />
&nbsp;<wbr>Radius of the solvent probe&nbsp;<wbr>(nm) </p>
<p> <code>-ndots</code><i> int</i><code> 24</code><br />
&nbsp;<wbr>Number of dots per sphere, more dots means more accuracy </p>
<p> <code>-qmax</code><i> real</i><code> 0.2 </code><br />
&nbsp;<wbr>The maximum charge&nbsp;<wbr>(e, absolute value)&nbsp;<wbr>of a hydrophobic atom </p>
<p> <code>-[no]f_index</code><i>no </i><br />
&nbsp;<wbr>Determine from a group in the index file what are the hydrophobic atoms rather than from the charge </p>
<p> <code>-minarea</code><i> real</i><code> 0.5 </code><br />
&nbsp;<wbr>The minimum area&nbsp;<wbr>(nm2)&nbsp;<wbr>to count an atom as a surface atom when writing a position restraint file&nbsp;<wbr>&nbsp;<wbr>(see help) </p>
<p> <code>-[no]pbc</code><i>yes </i><br />
&nbsp;<wbr>Take periodicity into account </p>
<p> <code>-[no]prot</code><i>yes </i><br />
&nbsp;<wbr>Output the protein to the connelly pdb file too </p>
<p> <code>-dgs</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>default value for solvation free energy per area&nbsp;<wbr>(kJ/mol/nm2) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
