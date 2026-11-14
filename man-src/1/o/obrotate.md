---
title: "obrotate(1)"
name: "obrotate"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obrotate/"
description: "obrotate – batch-rotate dihedral angles matching SMARTS patterns"
---

<h2>NAME</h2>
<p> <code>obrotate</code> &#8211; batch-rotate dihedral angles matching SMARTS patterns</p>
<h2>SYNOPSIS</h2>
<p> <i>&#8216;SMARTS-pattern&#8217;</i> <i>filename</i> <i>atom1</i> <i>atom2</i> <i>atom3</i> <i>atom4</i> <i>angle</i></p>
<h2>DESCRIPTION</h2>
<p> The obrotate program rotates the torsional (dihedral) angle of a specified bond in molecules to that defined by the user. In other words, it does the same as a user setting an angle in a molecular modelling package, but much faster and in batch mode (i.e. across multiple molecules in a file). </p>
<p> The four atom IDs required are indexes into the SMARTS pattern, which starts at atom 0 (zero). The angle supplied is in degrees. The two atoms used to set the dihedral angle &lt;atom1&gt; and &lt;atom4&gt; do not need to be connected to the atoms of the bond &lt;atom2&gt; and &lt;atom3&gt; in any way. </p>
<p> The order of the atoms matters &#8212; the portion of the molecule attached to &lt;atom1&gt; and &lt;atom2&gt; remain fixed, but the portion bonded to &lt;atom3&gt; and &amp; &lt;atom4&gt; moves.</p>
<h2>EXAMPLES</h2>
<p> Let&#8217;s say that you want to define the conformation of a large number of molecules with a pyridyl scaffold and substituted with an aliphatic chain at the 3-position, for example for docking or 3D-QSAR purposes. </p>
<p> To set the value of the first dihedral angle to 90 degrees: </p>
<blockquote><p><tt>&quot;obrotate 'c1ccncc1CCC' pyridines.sdf 5 6 7 8 90&quot;</tt></p></blockquote>
<p> Here 6 and 7 define the bond to rotate in the SMARTS patter, i.e., c1-C and atoms 5 and 8 define the particular dihedral angle to rotate. </p>
<p> Since the atoms to define the dihedral do not need to be directly connected, the nitrogen in the pyridine can be used: </p>
<blockquote><p><tt>&quot;obrotate 'c1ccncc1CCC' pyridines.sdf 4 6 7 8 90&quot;</tt></p></blockquote>
<p> Keep the pyridyl ring fixed and moves the aliphatic chain: </p>
<blockquote><p><tt>&quot;obrotate 'c1ccncc1CCC' pyridines.sdf 5 6 7 8 90&quot;</tt></p></blockquote>
<p> Keep the aliphatic chain fixed and move the pyridyl ring: </p>
<blockquote><p><tt>&quot;obrotate 'c1ccncc1CCC' pyridines.sdf 8 7 6 5 90&quot;</tt></p></blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-babel/">babel</a>(1), <a href="/docs/linux/man/1-obchiral/">obchiral</a>(1), <a href="/docs/linux/man/1-obfit/">obfit</a>(1), <a href="/docs/linux/man/1-obgrep/">obgrep</a>(1), <a href="/docs/linux/man/1-obprop/">obprop</a>(1), <a href="/docs/linux/man/1-obrotate/">obrotate</a>(1). </p>
<p> The web pages for Open Babel can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/">http://openbabel.org/</a></code>&gt; </p>
<p> A guide for constructing SMARTS patterns can be found at: &lt;<code><a rel="nofollow" href="http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html">http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html</a></code>&gt;</p>
<h2>AUTHORS</h2>
<p> The obgrep program was contributed by An Fabien Fontaine </p>
<p> An -nosplit Open Babel is developed by a cast of many, including currrent maintainers An Geoff Hutchison , An Chris Morley , An Michael Banck , and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/THANKS">http://openbabel.org/wiki/THANKS</a></code>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2001 by OpenEye Scientific Software, Inc.<br />
 Some portions Copyright (C) 2001-2005 by Geoffrey R. Hutchison and other contributors. </p>
<p>&nbsp;<wbr>This program is free software;&nbsp;<wbr>you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation version 2 of the License. </p>
<p>&nbsp;<wbr>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
