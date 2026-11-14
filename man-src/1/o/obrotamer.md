---
title: "obrotamer(1)"
name: "obrotamer"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obrotamer/"
description: "obrotamer – generate conformer/rotamer coordinates"
---

<h2>NAME</h2>
<p> <code>obrotamer</code> &#8211; generate conformer/rotamer coordinates</p>
<h2>SYNOPSIS</h2>
<p> <i>filename</i></p>
<h2>DESCRIPTION</h2>
<p> The obrotamer tool can be used as part of a conformational search by generating random isomers based on rotating dihedral angles. These rotamers are not conformers &#8212; that is, obrotamer does not perform geometry optimization after generating the rotamer structure. The obminimize tool can do geometry optimization using molecular mechanics.</p>
<h2>EXAMPLES</h2>
<blockquote><p><tt>&quot;obrotamer baseconformer.sdf &gt;rotamer1.sdf&quot;</tt></p></blockquote>
<p> Generate a random rotational isomer of baseconformer.sdf and write it to rotamer1.sdf</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-babel/">babel</a>(1), <a href="/docs/linux/man/1-obenergy/">obenergy</a>(1), <a href="/docs/linux/man/1-obfit/">obfit</a>(1), <a href="/docs/linux/man/1-obgrep/">obgrep</a>(1), <a href="/docs/linux/man/1-obminimize/">obminimize</a>(1), <a href="/docs/linux/man/1-obrotate/">obrotate</a>(1). </p>
<p> The web pages for Open Babel can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/">http://openbabel.org/</a></code>&gt;</p>
<h2>AUTHORS</h2>
<p> An -nosplit Open Babel is developed by a cast of many, including currrent maintainers An Geoff Hutchison , An Chris Morley , An Michael Banck , and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/THANKS">http://openbabel.org/wiki/THANKS</a></code>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2001 by OpenEye Scientific Software, Inc.<br />
 Some portions Copyright (C) 2001-2007 by Geoffrey R. Hutchison and other contributors. </p>
<p>&nbsp;<wbr>This program is free software;&nbsp;<wbr>you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation version 2 of the License. </p>
<p>&nbsp;<wbr>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
