---
title: "g_lie_d(1)"
name: "g_lie_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_lie_d/"
description: "g_lie – free energy estimate from linear combinations"
---

<h2>NAME</h2>
<p> g_lie &#8211; free energy estimate from linear combinations </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_lie</code> <code>-f</code><i> ener.edr </i> <code>-o</code><i> lie.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-Elj</code><i> real </i> <code>-Eqq</code><i> real </i> <code>-Clj</code><i> real </i> <code>-Cqq</code><i> real </i> <code>-ligand</code><i> string </i></p>
<h2>DESCRIPTION</h2>
<p> g_lie computes a free energy estimate based on an energy analysis from. One needs an energy file with the following components: Coul (A-B) LJ-SR (A-B) etc.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> ener.edr</i> <code>Input</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<p> <code>-o</code><i> lie.xvg</i> <code>Output</code><br />
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
<p> <code>-Elj</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Lennard-Jones interaction between ligand and solvent </p>
<p> <code>-Eqq</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Coulomb interaction between ligand and solvent </p>
<p> <code>-Clj</code><i> real</i><code> 0.181 </code><br />
&nbsp;<wbr>Factor in the LIE equation for Lennard-Jones component of energy </p>
<p> <code>-Cqq</code><i> real</i><code> 0.5 </code><br />
&nbsp;<wbr>Factor in the LIE equation for Coulomb component of energy </p>
<p> <code>-ligand</code><i> string</i><code> none</code><br />
&nbsp;<wbr>Name of the ligand in the energy file </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
