---
title: "g_bond(1)"
name: "g_bond"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_bond/"
description: "g_bond – calculates distances between atoms"
---

<h2>NAME</h2>
<p> g_bond &#8211; calculates distances between atoms </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_bond</code> <code>-f</code><i> traj.xtc </i> <code>-n</code><i> index.ndx </i> <code>-s</code><i> topol.tpr </i> <code>-o</code><i> bonds.xvg </i> <code>-l</code><i> bonds.log </i> <code>-d</code><i> distance.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-blen</code><i> real </i> <code>-tol</code><i> real </i> <code>-[no]aver</code><i></i> <code>-[no]averdist</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> g_bond makes a distribution of bond lengths. If all is well a gaussian distribution should be made when using a harmonic potential. bonds are read from a single group in the index file in order i1-j1 i2-j2 thru in-jn. </p>
<p> <code> -tol</code> gives the half-width of the distribution as a fraction of the bondlength (<code> -blen</code>). That means, for a bond of 0.2 a tol of 0.1 gives a distribution from 0.18 to 0.22. </p>
<p> Option <code> -d</code> plots all the distances as a function of time. This requires a structure file for the atom and residue names in the output. If however the option <code> -averdist</code> is given (as well or separately) the average bond length is plotted instead.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-o</code><i> bonds.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-l</code><i> bonds.log</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
<p> <code>-d</code><i> distance.xvg</i> <code>Output, Opt.</code><br />
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
<p> <code>-blen</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Bond length. By default length of first bond </p>
<p> <code>-tol</code><i> real</i><code> 0.1 </code><br />
&nbsp;<wbr>Half width of distribution as fraction of blen </p>
<p> <code>-[no]aver</code><i>yes </i><br />
&nbsp;<wbr>Average bond length distributions </p>
<p> <code>-[no]averdist</code><i>yes </i><br />
&nbsp;<wbr>Average distances&nbsp;<wbr>(turns on -d) </p>
<h2>KNOWN PROBLEMS</h2>
<p> &#8211; It should be possible to get bond information from the topology. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
