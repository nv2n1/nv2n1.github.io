---
title: "obgrep(1)"
name: "obgrep"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obgrep/"
description: "obgrep – an advanced molecular search program using SMARTS"
---

<h2>NAME</h2>
<p> <code>obgrep</code> &#8211; an advanced molecular search program using SMARTS</p>
<h2>SYNOPSIS</h2>
<p> [<i>OPTIONS</i> ] <i>&#8216;SMARTS-pattern&#8217; </i> <i>filename</i></p>
<h2>DESCRIPTION</h2>
<p> The obgrep tool can be used to search for molecules inside multi-molecule database files (e.g., SMILES, SDF, etc.) or across multiple files.</p>
<h2>OPTIONS</h2>
<p> If only a filename is given, obgrep will attempt to guess the file type from the filename extension.</p>
<dl>
<dt><code>-c</code></p>
<dd> Print the number of matches</p>
<dt><code>-f</code></p>
<dd> Full match, print matching-molecules only when the number of heavy atoms is also equal to the number of atoms in the SMARTS pattern</p>
<dt><code>-i </code><i>format</i></p>
<dd> Specifies input and output format, see <a href="/docs/linux/man/1-babel/">babel</a>(1) for available formats</p>
<dt><code>-n</code></p>
<dd> Only print the name of the molecules</p>
<dt><code>-t </code><i>file &#8230;</i></p>
<dd> Print a molecule only if the pattern occurs # times inside the molecule</p>
<dt><code>-v</code></p>
<dd> Invert the matching, print non-matching molecules</dl>
<h2>EXAMPLES</h2>
<p> Note that in all examples, the SMARTS pattern is enclosed in single quotes &#8216;&#8230;&#8217; to ensure it is not changed by the shell. </p>
<p> Print all the molecules with a methylamine group: </p>
<blockquote><p><tt>&quot;obgrep 'CN' database.smi&quot;</tt></p></blockquote>
<p> Print all the molecules without a methylamine group: </p>
<blockquote><p><tt>&quot;obgrep -v 'CN' database.smi&quot;</tt></p></blockquote>
<p> Print the number of molecules without a methylamine group: </p>
<blockquote><p><tt>&quot;obgrep -v -c 'CN' database.smi&quot;</tt></p></blockquote>
<p> Print methylamine (if it exists in the file): </p>
<blockquote><p><tt>&quot;obgrep -f 'CN' database.smi&quot;</tt></p></blockquote>
<p> Print methylamine and/or methanol (if they exist): </p>
<blockquote><p><tt>&quot;obgrep -f 'C[N,O]' database.smi&quot;</tt></p></blockquote>
<p> Print all molecules with aromatic carbon in all SMILES files in the directory (i.e., *.smi) </p>
<blockquote><p><tt>&quot;obgrep 'c' *.smi&quot;</tt></p></blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-babel/">babel</a>(1), <a href="/docs/linux/man/1-obfit/">obfit</a>(1), <a href="/docs/linux/man/1-obrotate/">obrotate</a>(1). </p>
<p> The web pages for Open Babel can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/">http://openbabel.org/</a></code>&gt; </p>
<p> A guide for constructing SMARTS patterns can be found at: &lt;<code><a rel="nofollow" href="http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html">http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html</a></code>&gt;</p>
<h2>AUTHORS</h2>
<p> The obgrep program was contributed by An Fabien Fontaine </p>
<p> An -nosplit Open Babel is developed by a cast of many, including currrent maintainers An Geoff Hutchison , An Chris Morley , An Michael Banck , and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/THANKS">http://openbabel.org/wiki/THANKS</a></code>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2001 by OpenEye Scientific Software, Inc.<br />
 Some portions Copyright (C) 2001-2007 by Geoffrey R. Hutchison and other contributors. </p>
<p>&nbsp;<wbr>This program is free software;&nbsp;<wbr>you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation version 2 of the License. </p>
<p>&nbsp;<wbr>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
