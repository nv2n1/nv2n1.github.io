---
title: "obprobe(1)"
name: "obprobe"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obprobe/"
description: "obprobe – create electrostatic probe grid"
---

<h2>NAME</h2>
<p> <code>obprobe</code> &#8211; create electrostatic probe grid</p>
<h2>SYNOPSIS</h2>
<p> [<i>OPTIONS</i> ] <i>type</i> <i>pchg</i> <i>filename</i></p>
<h2>DESCRIPTION</h2>
<p> The obprobe tool creates a grid around a molecule, placing a probe atom with a specified atom type and partial charge at each point to calculate the MMFF94 energy. This can be used for docking experiments to test hydrogen-bond affinity, electrostatic potential, etc. Output is sent to standard output using the Gaussian Cube format.</p>
<h2>OPTIONS</h2>
<p> If no filename is given, obprobe will give all options including the example probes.</p>
<dl>
<dt><code>-s </code><i>stepsize</i></p>
<dd> Set the resolution of the grid (stepsize)</p>
<dt><code>-p </code><i>padding</i></p>
<dd> Set the padding &#8212; extra distance on each side of the box formed by the molecule.</p>
<dt><i>type</i></p>
<dd> MMFF94 atom type</p>
<dt><i>pchg</i></p>
<dd> MMFF94 partial charge</dl>
<h2>EXAMPLES</h2>
<p> Probe the file pyridines.sdf using a carbonyl oxygen &#8212; a hydrogen bond acceptor with partial charge -0.57: </p>
<blockquote><p><tt>&quot;obprobe 7 -0.57 pyridines.sdf&quot;</tt></p></blockquote>
<p> Probe the file pyridines.sdf using a phenyl carbon atom &#8212; a hydrophobic atom with no partial charge: </p>
<blockquote><p><tt>&quot;obprobe 37 0.0 pyridines.sdf&quot;</tt></p></blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-babel/">babel</a>(1). </p>
<p> The web pages for Open Babel can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/">http://openbabel.org/</a></code>&gt;</p>
<h2>AUTHORS</h2>
<p> The obprobe program was contributed by An Tim Vandermeersch. </p>
<p> An -nosplit Open Babel is developed by a cast of many, including currrent maintainers An Geoff Hutchison , An Chris Morley , An Michael Banck , and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/THANKS">http://openbabel.org/wiki/THANKS</a></code>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2006-2008 by Tim Vandermeersch<br />
 Some portions Copyright (C) 2004-2008 by Geoffrey R. Hutchison and other contributors. </p>
<p>&nbsp;<wbr>This program is free software;&nbsp;<wbr>you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation version 2 of the License. </p>
<p>&nbsp;<wbr>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
