---
title: "obminimize(1)"
name: "obminimize"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obminimize/"
description: "obminimize – optimize the geometry, minimize the energy for a molecule"
---

<h2>NAME</h2>
<p> <code>obminimize</code> &#8211; optimize the geometry, minimize the energy for a molecule</p>
<h2>SYNOPSIS</h2>
<p> [<i>OPTIONS</i> ] <i>filename</i></p>
<h2>DESCRIPTION</h2>
<p> The obminimize tool can be used to minimize the energy for molecules inside (multi-)molecule files (e.g., MOL2, etc.)</p>
<h2>OPTIONS</h2>
<p> If no filename is given, obminimize will give all options including the available forcefields.</p>
<dl>
<dt><code>-n </code><i>steps</i></p>
<dd> Specify the maximum number of steps (default=2500)</p>
<dt><code>-cg</code></p>
<dd> Use conjugate gradients algorithm (default)</p>
<dt><code>-sd</code></p>
<dd> Use steepest descent algorithm</p>
<dt><code>-c </code><i>criteria</i></p>
<dd> Set convergence criteria (default=1e-6)</p>
<dt><code>-ff </code><i>forcefield</i></p>
<dd> Select the forcefield</dl>
<h2>EXAMPLES</h2>
<p> View the possible options, including available forcefields: </p>
<blockquote><p><tt>&quot;obminimize&quot;</tt></p></blockquote>
<p> Minimize the energy for the molecule(s) in file test.mol2: </p>
<blockquote><p><tt>&quot;obminimize test.mol2&quot;</tt></p></blockquote>
<p> Minimize the energy for the molecule(s) in file test.mol2 using the Ghemical forcefield: </p>
<blockquote><p><tt>&quot;obminimize -ff Ghemical test.mol2&quot;</tt></p></blockquote>
<p> Minimize the energy for the molecule(s) in file test.mol2 by taking at most 300 geometry optimization steps </p>
<blockquote><p><tt>&quot;obminimize -n 300 test.mol2&quot;</tt></p></blockquote>
<p> Minimize the energy for the molecule(s) in file test.mol2 using the steepest descent algorithm and convergence criteria 1e-5: </p>
<blockquote><p><tt>&quot;obminimize -sd -c 1e-5 test.mol2&quot;</tt></p></blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-babel/">babel</a>(1), <a href="/docs/linux/man/1-obenergy/">obenergy</a>(1), <a href="/docs/linux/man/1-obrotamer/">obrotamer</a>(1). </p>
<p> The web pages for Open Babel can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/">http://openbabel.org/</a></code>&gt; </p>
<p> The web pages for Open Babel Molecular Mechanics can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/Molecular_mechanics">http://openbabel.org/wiki/Molecular_mechanics</a></code>&gt;</p>
<h2>AUTHORS</h2>
<p> The minimize program was contributed by An Tim Vandermeersch. </p>
<p> An -nosplit Open Babel is developed by a cast of many, including currrent maintainers An Geoff Hutchison , An Chris Morley , An Michael Banck , and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/THANKS">http://openbabel.org/wiki/THANKS</a></code>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007 by Tim Vandermeersch. </p>
<p>&nbsp;<wbr>This program is free software;&nbsp;<wbr>you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation version 2 of the License. </p>
<p>&nbsp;<wbr>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
