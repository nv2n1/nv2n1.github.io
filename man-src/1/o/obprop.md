---
title: "obprop(1)"
name: "obprop"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obprop/"
description: "obprop – print standard molecular properties"
---

<h2>NAME</h2>
<p> <code>obprop</code> &#8211; print standard molecular properties</p>
<h2>SYNOPSIS</h2>
<p> <i>filename</i></p>
<h2>DESCRIPTION</h2>
<p> The obprop program is a tool to print a set of standard molecular properties for all molecules in a file. It also serves as example code for using the Open Babel library (libopenbabel). </p>
<p> Output format includes:<br />
 name [<i>Name</i> ]<br />
 formula [<i>Formula</i> ]<br />
 mol_weight [<i>Molecular Weight</i> ]<br />
 exact_mass [<i>Isotopic Mass</i> ]<br />
 canonical_SMILES [<i>String</i> ]<br />
 num_atoms [<i>Number</i> ]<br />
 num_bonds [<i>Number</i> ]<br />
 num_residues [<i>Number</i> ]<br />
 sequence [<i>Residue Sequence</i> ]<br />
 num_rings [<i>Number of Rings (by SSSR)</i> ]<br />
 logP [<i>Number (octanol-water partition)</i> ]<br />
 PSA [<i>Number (topological polar surface area)</i> ]<br />
 MR [<i>Number (molar refractivity)</i> ]<br />
 $$$ </p>
<p> The &quot;$$$&quot; is the separator between multiple molecular entries in a file</p>
<h2>EXAMPLES</h2>
<blockquote><p><tt>&quot;obprop pyridines.sdf&quot;</tt></p></blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-babel/">babel</a>(1), <a href="/docs/linux/man/1-obchiral/">obchiral</a>(1), <a href="/docs/linux/man/1-obfit/">obfit</a>(1), <a href="/docs/linux/man/1-obgrep/">obgrep</a>(1), <a href="/docs/linux/man/1-obrotate/">obrotate</a>(1). </p>
<p> The web pages for Open Babel can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/">http://openbabel.org/</a></code>&gt;</p>
<h2>AUTHORS</h2>
<p> The obprop program was contributed by An Fabien Fontaine </p>
<p> An -nosplit Open Babel is developed by a cast of many, including currrent maintainers An Geoff Hutchison , An Chris Morley , An Michael Banck , and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/THANKS">http://openbabel.org/wiki/THANKS</a></code>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003 by Fabien Fontaine<br />
 Some portions Copyright (C) 2004-2007 by Geoffrey R. Hutchison and other contributors. </p>
<p>&nbsp;<wbr>This program is free software;&nbsp;<wbr>you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation version 2 of the License. </p>
<p>&nbsp;<wbr>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
