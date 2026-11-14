---
title: "g_enemat_d(1)"
name: "g_enemat_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_enemat_d/"
description: "g_enemat – extracts an energy matrix from an energy file"
---

<h2>NAME</h2>
<p> g_enemat &#8211; extracts an energy matrix from an energy file </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_enemat</code> <code>-f</code><i> ener.edr </i> <code>-groups</code><i> groups.dat </i> <code>-eref</code><i> eref.dat </i> <code>-emat</code><i> emat.xpm </i> <code>-etot</code><i> energy.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]sum</code><i></i> <code>-skip</code><i> int </i> <code>-[no]mean</code><i></i> <code>-nlevels</code><i> int </i> <code>-max</code><i> real </i> <code>-min</code><i> real </i> <code>-[no]coul</code><i></i> <code>-[no]coulr</code><i></i> <code>-[no]coul14</code><i></i> <code>-[no]lj</code><i></i> <code>-[no]lj</code><i></i> <code>-[no]lj14</code><i></i> <code>-[no]bhamsr</code><i></i> <code>-[no]bhamlr</code><i></i> <code>-[no]free</code><i></i> <code>-temp</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_enemat extracts an energy matrix from the energy file (<code> -f</code>). With <code> -groups</code> a file must be supplied with on each line a group of atoms to be used. For these groups matrix of interaction energies will be extracted from the energy file by looking for energy groups with names corresponding to pairs of groups of atoms. E.g. if your <code> -groups</code> file contains: </p>
<p> <code> 2</code> </p>
<p> <code> Protein</code> </p>
<p> <code> SOL</code> </p>
<p> then energy groups with names like &#8216;Coul-SR:Protein-SOL&#8217; and &#8216;LJ:Protein-SOL&#8217; are expected in the energy file (although <code> g_enemat</code> is most useful if many groups are analyzed simultaneously). Matrices for different energy types are written out separately, as controlled by the <code> -[no]coul</code>, <code> -[no]coulr</code>, <code> -[no]coul14</code>, <code> -[no]lj</code>, <code> -[no]lj14</code>, <code> -[no]bham</code> and <code> -[no]free</code> options. Finally, the total interaction energy energy per group can be calculated (<code> -etot</code>). </p>
<p> An approximation of the free energy can be calculated using: E(free) = E0 + kT log( exp((E-E0)/kT) ), where &#8221; stands for time-average. A file with reference free energies can be supplied to calculate the free energy difference with some reference state. Group names (e.g. residue names) in the reference file should correspond to the group names as used in the <code> -groups</code> file, but a appended number (e.g. residue number) in the <code> -groups</code> will be ignored in the comparison.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> ener.edr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<p> <code>-groups</code><i> groups.dat</i> <code>Input</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-eref</code><i> eref.dat</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-emat</code><i> emat.xpm</i> <code>Output</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-etot</code><i> energy.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
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
<p> <code>-[no]sum</code><i>no </i><br />
&nbsp;<wbr>Sum the energy terms selected rather than display them all </p>
<p> <code>-skip</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Skip number of frames between data points </p>
<p> <code>-[no]mean</code><i>yes </i><br />
&nbsp;<wbr>with -groups extracts matrix of mean energies in stead of matrix for each timestep </p>
<p> <code>-nlevels</code><i> int</i><code> 20</code><br />
&nbsp;<wbr>number of levels for matrix colors </p>
<p> <code>-max</code><i> real</i><code> 1e+20 </code><br />
&nbsp;<wbr>max value for energies </p>
<p> <code>-min</code><i> real</i><code> -1e+20</code><br />
&nbsp;<wbr>min value for energies </p>
<p> <code>-[no]coul</code><i>yes </i><br />
&nbsp;<wbr>extract Coulomb SR energies </p>
<p> <code>-[no]coulr</code><i>no </i><br />
&nbsp;<wbr>extract Coulomb LR energies </p>
<p> <code>-[no]coul14</code><i>no </i><br />
&nbsp;<wbr>extract Coulomb 1-4 energies </p>
<p> <code>-[no]lj</code><i>yes </i><br />
&nbsp;<wbr>extract Lennard-Jones SR energies </p>
<p> <code>-[no]lj</code><i>no </i><br />
&nbsp;<wbr>extract Lennard-Jones LR energies </p>
<p> <code>-[no]lj14</code><i>no </i><br />
&nbsp;<wbr>extract Lennard-Jones 1-4 energies </p>
<p> <code>-[no]bhamsr</code><i>no </i><br />
&nbsp;<wbr>extract Buckingham SR energies </p>
<p> <code>-[no]bhamlr</code><i>no </i><br />
&nbsp;<wbr>extract Buckingham LR energies </p>
<p> <code>-[no]free</code><i>yes </i><br />
&nbsp;<wbr>calculate free energy </p>
<p> <code>-temp</code><i> real</i><code> 300 </code><br />
&nbsp;<wbr>reference temperature for free energy calculation </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
