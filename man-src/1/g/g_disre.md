---
title: "g_disre(1)"
name: "g_disre"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_disre/"
description: "g_disre – analyzes distance restraints"
---

<h2>NAME</h2>
<p> g_disre &#8211; analyzes distance restraints </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_disre</code> <code>-s</code><i> topol.tpr </i> <code>-f</code><i> traj.xtc </i> <code>-ds</code><i> drsum.xvg </i> <code>-da</code><i> draver.xvg </i> <code>-dn</code><i> drnum.xvg </i> <code>-dm</code><i> drmax.xvg </i> <code>-dr</code><i> restr.xvg </i> <code>-l</code><i> disres.log </i> <code>-n</code><i> viol.ndx </i> <code>-q</code><i> viol.pdb </i> <code>-c</code><i> clust.ndx </i> <code>-x</code><i> matrix.xpm </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-ntop</code><i> int </i> <code>-maxdr</code><i> real </i> <code>-nlevels</code><i> int </i> <code>-[no]third</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_disre computes violations of distance restraints. If necessary all protons can be added to a protein molecule using the protonate program. </p>
<p> The program always computes the instantaneous violations rather than time-averaged, because this analysis is done from a trajectory file afterwards it does not make sense to use time averaging. However, the time averaged values per restraint are given in the log file. </p>
<p> An index file may be used to select specific restraints for printing. </p>
<p> When the optional<code> -q</code> flag is given a pdb file coloured by the amount of average violations. </p>
<p> When the <code> -c</code> option is given, an index file will be read containing the frames in your trajectory corresponding to the clusters (defined in another manner) that you want to analyze. For these clusters the program will compute average violations using the third power averaging algorithm and print them in the log file.</p>
<h2>FILES</h2>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-ds</code><i> drsum.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-da</code><i> draver.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-dn</code><i> drnum.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-dm</code><i> drmax.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-dr</code><i> restr.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-l</code><i> disres.log</i> <code>Output</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
<p> <code>-n</code><i> viol.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-q</code><i> viol.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-c</code><i> clust.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-x</code><i> matrix.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
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
<p> <code>-ntop</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Number of large violations that are stored in the log file every step </p>
<p> <code>-maxdr</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum distance violation in matrix output. If less than or equal to 0 the maximum will be determined by the data. </p>
<p> <code>-nlevels</code><i> int</i><code> 20</code><br />
&nbsp;<wbr>Number of levels in the matrix output </p>
<p> <code>-[no]third</code><i>yes </i><br />
&nbsp;<wbr>Use inverse third power averaging or linear for matrix output </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
