---
title: "g_rmsdist(1)"
name: "g_rmsdist"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_rmsdist/"
description: "g_rmsdist – calculates atom pair distances averaged with power 2, -3 or -6"
---

<h2>NAME</h2>
<p> g_rmsdist &#8211; calculates atom pair distances averaged with power 2, -3 or -6 </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_rmsdist</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-equiv</code><i> equiv.dat </i> <code>-o</code><i> distrmsd.xvg </i> <code>-rms</code><i> rmsdist.xpm </i> <code>-scl</code><i> rmsscale.xpm </i> <code>-mean</code><i> rmsmean.xpm </i> <code>-nmr3</code><i> nmr3.xpm </i> <code>-nmr6</code><i> nmr6.xpm </i> <code>-noe</code><i> noe.dat </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-nlevels</code><i> int </i> <code>-max</code><i> real </i> <code>-[no]sumh</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_rmsdist computes the root mean square deviation of atom distances, which has the advantage that no fit is needed like in standard RMS deviation as computed by g_rms. The reference structure is taken from the structure file. The rmsd at time t is calculated as the rms of the differences in distance between atom-pairs in the reference structure and the structure at time t. </p>
<p> g_rmsdist can also produce matrices of the rms distances, rms distances scaled with the mean distance and the mean distances and matrices with NMR averaged distances (1/r3 and 1/r6 averaging). Finally, lists of atom pairs with 1/r3 and 1/r6 averaged distance below the maximum distance (<code> -max</code>, which will default to 0.6 in this case) can be generated, by default averaging over equivalent hydrogens (all triplets of hydrogens named *[123]). Additionally a list of equivalent atoms can be supplied (<code> -equiv</code>), each line containing a set of equivalent atoms specified as residue number and name and atom name; e.g.: </p>
<p> <code> 3 SER HB1 3 SER HB2</code> </p>
<p> Residue and atom names must exactly match those in the structure file, including case. Specifying non-sequential atoms is undefined.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-equiv</code><i> equiv.dat</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-o</code><i> distrmsd.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-rms</code><i> rmsdist.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-scl</code><i> rmsscale.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-mean</code><i> rmsmean.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-nmr3</code><i> nmr3.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-nmr6</code><i> nmr6.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-noe</code><i> noe.dat</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
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
<p> <code>-nlevels</code><i> int</i><code> 40</code><br />
&nbsp;<wbr>Discretize rms in&nbsp;<wbr>&nbsp;<wbr>levels </p>
<p> <code>-max</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Maximum level in matrices </p>
<p> <code>-[no]sumh</code><i>yes </i><br />
&nbsp;<wbr>average distance over equivalent hydrogens </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
