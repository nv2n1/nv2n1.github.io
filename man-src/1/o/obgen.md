---
title: "obgen(1)"
name: "obgen"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obgen/"
description: "obgen – generate 3D coordinates for a molecule"
---

<h2>NAME</h2>
<p> <code>obgen</code> &#8211; generate 3D coordinates for a molecule</p>
<h2>SYNOPSIS</h2>
<p> [<i>OPTIONS</i> ] <i>filename</i></p>
<h2>DESCRIPTION</h2>
<p> The obgen tool will generate 3D coordinates for molecules in a file (e.g. multi-molecule SMILES files). The resulting structure will be optimized using the given forcefield and checked for the lowest-energy conformer using a Monte Carlo search. Output will be sent to standard output in the SDF file format.</p>
<h2>OPTIONS</h2>
<p> If no filename is given, obgen will give all options including the available forcefields.</p>
<dl>
<dt><code>-ff </code><i>forcefield</i></p>
<dd> Select the forcefield</dl>
<h2>EXAMPLES</h2>
<p> View the possible options, including available forcefields: </p>
<blockquote><p><tt>&quot;obgen&quot;</tt></p></blockquote>
<p> Generate 3D coordinates for the molecule(s) in file test.smi: </p>
<blockquote><p><tt>&quot;obgen test.smi&quot;</tt></p></blockquote>
<p> Generate 3D coordinates for the molecule(s) in file test.smi using the UFF forcefield: </p>
<blockquote><p><tt>&quot;obgen -ff UFF test.smi&quot;</tt></p></blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-babel/">babel</a>(1), <a href="/docs/linux/man/1-obminimize/">obminimize</a>(1), <a href="/docs/linux/man/1-obconformer/">obconformer</a>(1). </p>
<p> The web pages for Open Babel can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/">http://openbabel.org/</a></code>&gt; </p>
<p> The web pages for Open Babel Molecular Mechanics can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/Molecular_mechanics">http://openbabel.org/wiki/Molecular_mechanics</a></code>&gt;</p>
<h2>AUTHORS</h2>
<p> The obgen program was contributed by An Tim Vandermeersch. </p>
<p> An -nosplit Open Babel is developed by a cast of many, including currrent maintainers An Geoff Hutchison , An Chris Morley , An Michael Banck , and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/THANKS">http://openbabel.org/wiki/THANKS</a></code>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007-2008 by Tim Vandermeersch. </p>
<p>&nbsp;<wbr>This program is free software;&nbsp;<wbr>you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation version 2 of the License. </p>
<p>&nbsp;<wbr>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
