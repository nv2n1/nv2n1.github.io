---
title: "g_order(1)"
name: "g_order"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_order/"
description: "g_order – computes the order parameter per atom for carbon tails"
---

<h2>NAME</h2>
<p> g_order &#8211; computes the order parameter per atom for carbon tails </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_order</code> <code>-f</code><i> traj.xtc </i> <code>-n</code><i> index.ndx </i> <code>-s</code><i> topol.tpr </i> <code>-o</code><i> order.xvg </i> <code>-od</code><i> deuter.xvg </i> <code>-os</code><i> sliced.xvg </i> <code>-Sg</code><i> sg-ang.xvg </i> <code>-Sk</code><i> sk-dist.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-d</code><i> enum </i> <code>-sl</code><i> int </i> <code>-[no]szonly</code><i></i> <code>-[no]unsat</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> Compute the order parameter per atom for carbon tails. For atom i the vector i-1, i+1 is used together with an axis. The index file has to contain a group with all equivalent atoms in all tails for each atom the order parameter has to be calculated for. The program can also give all diagonal elements of the order tensor and even calculate the deuterium order parameter Scd (default). If the option -szonly is given, only one order tensor component (specified by the -d option) is given and the order parameter per slice is calculated as well. If -szonly is not selected, all diagonal elements and the deuterium order parameter is given. </p>
<p> The tetrahedrality order parameters can be determined around an atom. Both angle an distance order parameters are calculated. See P.-L. Chau and A.J. Hardwick, Mol. Phys., 93, (1998), 511-518. for more details. </p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> order.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-od</code><i> deuter.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-os</code><i> sliced.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-Sg</code><i> sg-ang.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-Sk</code><i> sk-dist.xvg</i> <code>Output</code><br />
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
<p> <code>-d</code><i> enum</i><code> z</code><br />
&nbsp;<wbr>Direction of the normal on the membrane:&nbsp;<wbr><code>&nbsp;<wbr>z</code>,&nbsp;<wbr><code>&nbsp;<wbr>x</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>y</code> </p>
<p> <code>-sl</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Calculate order parameter as function of boxlength, dividing the box in nr slices. </p>
<p> <code>-[no]szonly</code><i>no </i><br />
&nbsp;<wbr>Only give Sz element of order tensor.&nbsp;<wbr>(axis can be specified with -d) </p>
<p> <code>-[no]unsat</code><i>no </i><br />
&nbsp;<wbr>Calculate order parameters for unsaturated carbons. Note that this cannot be mixed with normal order parameters. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
