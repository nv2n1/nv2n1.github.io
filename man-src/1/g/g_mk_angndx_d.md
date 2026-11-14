---
title: "g_mk_angndx_d(1)"
name: "g_mk_angndx_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_mk_angndx_d/"
description: "mk_angndx – generates index files for g_angle"
---

<h2>NAME</h2>
<p> mk_angndx &#8211; generates index files for g_angle </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>mk_angndx</code> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> angle.ndx </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-type</code><i> enum </i> <code>-[no]hyd</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> mk_angndx makes an index file for calculation of angle distributions etc. It uses a run input file (<code> .tpx</code>) for the definitions of the angles, dihedrals etc.</p>
<h2>FILES</h2>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-n</code><i> angle.ndx</i> <code>Output</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-type</code><i> enum</i><code> angle</code><br />
&nbsp;<wbr>Type of angle:&nbsp;<wbr><code>&nbsp;<wbr>angle</code>,&nbsp;<wbr><code>&nbsp;<wbr>dihedral</code>,&nbsp;<wbr><code>&nbsp;<wbr>improper</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>ryckaert-bellemans</code> </p>
<p> <code>-[no]hyd</code><i>yes </i><br />
&nbsp;<wbr>Include angles with atoms with mass&nbsp;<wbr>&nbsp;<wbr>1.5 </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
