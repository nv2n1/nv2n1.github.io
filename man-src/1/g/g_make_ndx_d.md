---
title: "g_make_ndx_d(1)"
name: "g_make_ndx_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_make_ndx_d/"
description: "make_ndx – makes index files"
---

<h2>NAME</h2>
<p> make_ndx &#8211; makes index files </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>make_ndx</code> <code>-f</code><i> conf.gro </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> index.ndx </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-natoms</code><i> int </i></p>
<h2>DESCRIPTION</h2>
<p> Index groups are necessary for almost every gromacs program. All these programs can generate default index groups. You ONLY have to use make_ndx when you need SPECIAL index groups. There is a default index group for the whole system, 9 default index groups are generated for proteins, a default index group is generated for every other residue name. </p>
<p> When no index file is supplied, also make_ndx will generate the default groups. With the index editor you can select on atom, residue and chain names and numbers. When a run input file is supplied you can also select on atom type. You can use NOT, AND and OR, you can split groups into chains, residues or atoms. You can delete and rename groups. </p>
<p> The atom numbering in the editor and the index file starts at 1.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> conf.gro</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt., Mult.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> index.ndx</i> <code>Output</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-natoms</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>set number of atoms&nbsp;<wbr>(default: read from coordinate or index file) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
