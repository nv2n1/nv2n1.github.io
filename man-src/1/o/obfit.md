---
title: "obfit(1)"
name: "obfit"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obfit/"
description: "obfit – superimpose two molecules based on a pattern"
---

<h2>NAME</h2>
<p> <code>obfit</code> &#8211; superimpose two molecules based on a pattern</p>
<h2>SYNOPSIS</h2>
<p> <i>SMARTS-pattern</i> <i>fixed-file</i> <i>outfile</i></p>
<h2>DESCRIPTION</h2>
<p> Superimpose two molecules using a quaternion fit. The atoms used to fit the two molecules are defined by the SMARTS pattern given by the user. It is useful to align congeneric series of molecules on a common structural scaffold for 3D-QSAR studies. It can also be useful for displaying the results of conformational generation. </p>
<p> Any molecules matching the supplied SMARTS pattern will be rotated and translated to provide the smallest possible RMSD between the matching regions. If a molecule does not match the SMARTS pattern, it will be output with no transformation.</p>
<h2>EXAMPLES</h2>
<p> Align all the molecules in &#8216;testmv.sdf&#8217; on a single molecule of &#8216;testref.sdf&#8217; by superimposing them on its N-methylpiperidyl portion (and outputting a new SD file to the standard output): </p>
<blockquote><p><tt>&quot;obfit '[nh]1c2c(=O)n(C)c(=O)n(C)c2cc1' testref.sdf testmv.sdf&quot;</tt></p></blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-babel/">babel</a>(1), <a href="/docs/linux/man/1-obchiral/">obchiral</a>(1), <a href="/docs/linux/man/1-obfit/">obfit</a>(1), <a href="/docs/linux/man/1-obgrep/">obgrep</a>(1), <a href="/docs/linux/man/1-obrotate/">obrotate</a>(1). </p>
<p> The web pages for Open Babel can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/">http://openbabel.org/</a></code>&gt; </p>
<p> A guide for constructing SMARTS patterns can be found at: &lt;<code><a rel="nofollow" href="http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html">http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html</a></code>&gt;</p>
<h2>AUTHORS</h2>
<p> The obfit program was contributed by An Fabien Fontaine </p>
<p> An -nosplit Open Babel is developed by a cast of many, including currrent maintainers An Geoff Hutchison , An Chris Morley , An Michael Banck , and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/THANKS">http://openbabel.org/wiki/THANKS</a></code>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2001 by OpenEye Scientific Software, Inc.<br />
 Some portions Copyright (C) 2001-2007 by Geoffrey R. Hutchison and other contributors. </p>
<p>&nbsp;<wbr>This program is free software;&nbsp;<wbr>you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation version 2 of the License. </p>
<p>&nbsp;<wbr>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
