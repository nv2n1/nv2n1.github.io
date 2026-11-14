---
title: "g_protonate(1)"
name: "g_protonate"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_protonate/"
description: "protonate – protonates structures"
---

<h2>NAME</h2>
<p> protonate &#8211; protonates structures </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>protonate</code> <code>-s</code><i> topol.tpr </i> <code>-f</code><i> traj.xtc </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> protonated.xtc </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i></p>
<h2>DESCRIPTION</h2>
<p> <code> protonate</code> reads (a) conformation(s) and adds all missing hydrogens as defined in <code> ffgmx2.hdb</code>. If only <code> -s</code> is specified, this conformation will be protonated, if also <code> -f</code> is specified, the conformation(s) will be read from this file which can be either a single conformation or a trajectory. </p>
<p> If a pdb file is supplied, residue names might not correspond to to the GROMACS naming conventions, in which case these residues will probably not be properly protonated. </p>
<p> If an index file is specified, please note that the atom numbers should correspond to the <code> protonated</code> state.</p>
<h2>FILES</h2>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-f</code><i> traj.xtc</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> protonated.xtc</i> <code>Output</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-b</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>First frame&nbsp;<wbr>(ps)&nbsp;<wbr>to read from trajectory </p>
<p> <code>-e</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Last frame&nbsp;<wbr>(ps)&nbsp;<wbr>to read from trajectory </p>
<p> <code>-dt</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Only use frame when t MOD dt&nbsp;<wbr>=&nbsp;<wbr>first time&nbsp;<wbr>(ps) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
