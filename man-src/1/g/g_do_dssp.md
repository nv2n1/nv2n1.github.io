---
title: "g_do_dssp(1)"
name: "g_do_dssp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_do_dssp/"
description: "do_dssp – assigns secondary structure and calculates solvent accessible surface area"
---

<h2>NAME</h2>
<p> do_dssp &#8211; assigns secondary structure and calculates solvent accessible surface area </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>do_dssp</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-ssdump</code><i> ssdump.dat </i> <code>-map</code><i> ss.map </i> <code>-o</code><i> ss.xpm </i> <code>-sc</code><i> scount.xvg </i> <code>-a</code><i> area.xpm </i> <code>-ta</code><i> totarea.xvg </i> <code>-aa</code><i> averarea.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-tu</code><i> enum </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-sss</code><i> string </i></p>
<h2>DESCRIPTION</h2>
<p> do_dssp reads a trajectory file and computes the secondary structure for each time frame calling the dssp program. If you do not have the dssp program, get it. do_dssp assumes that the dssp executable is /usr/local/bin/dssp. If this is not the case, then you should set an environment variable <code> DSSP</code> pointing to the dssp executable, e.g.: </p>
<p> <code> setenv DSSP /opt/dssp/bin/dssp</code> </p>
<p> The structure assignment for each residue and time is written to an <code> .xpm</code> matrix file. This file can be visualized with for instance <code> xv</code> and can be converted to postscript with <code> xpm2ps</code>. The number of residues with each secondary structure type and the total secondary structure (<code> -sss</code>) count as a function of time are also written to file (<code> -sc</code>). </p>
<p> Solvent accessible surface (SAS) per residue can be calculated, both in absolute values (A2) and in fractions of the maximal accessible surface of a residue. The maximal accessible surface is defined as the accessible surface of a residue in a chain of glycines. <code> Note</code> that the program <code> g_sas</code> can also compute SAS and that is more efficient. </p>
<p> Finally, this program can dump the secondary structure in a special file <code> ssdump.dat</code> for usage in the program <code> g_chi</code>. Together these two programs can be used to analyze dihedral properties as a function of secondary structure type.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-ssdump</code><i> ssdump.dat</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-map</code><i> ss.map</i> <code>Input, Lib.</code><br />
&nbsp;<wbr>File that maps matrix data to colors&nbsp;<wbr> </p>
<p> <code>-o</code><i> ss.xpm</i> <code>Output</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-sc</code><i> scount.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-a</code><i> area.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-ta</code><i> totarea.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-aa</code><i> averarea.xvg</i> <code>Output, Opt.</code><br />
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
<p> <code>-tu</code><i> enum</i><code> ps</code><br />
&nbsp;<wbr>Time unit:&nbsp;<wbr><code>&nbsp;<wbr>ps</code>,&nbsp;<wbr><code>&nbsp;<wbr>fs</code>,&nbsp;<wbr><code>&nbsp;<wbr>ns</code>,&nbsp;<wbr><code>&nbsp;<wbr>us</code>,&nbsp;<wbr><code>&nbsp;<wbr>ms</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>s</code> </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-sss</code><i> string</i><code> HEBT</code><br />
&nbsp;<wbr>Secondary structures for structure count </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
