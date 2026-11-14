---
title: "obconformer(1)"
name: "obconformer"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obconformer/"
description: "obconformer – generate conformer coordinates"
---

<h2>NAME</h2>
<p> <code>obconformer</code> &#8211; generate conformer coordinates</p>
<h2>SYNOPSIS</h2>
<p> <i># of conformers</i> <i># of optimization steps</i> <i>filename</i></p>
<h2>DESCRIPTION</h2>
<p> The obconformer tool can be used as part of a conformational study by generating random conformers using a Monte Carlo search. The best conformer out of the batch of conformers will be output, after taking the supplied number of geometry optimization steps. By default, obconformer uses the MMFF94 force field.</p>
<h2>EXAMPLES</h2>
<blockquote><p><tt>&quot;obconformer 250 100 baseconformer.sdf &gt;rotamer1.sdf&quot;</tt></p></blockquote>
<p> Generate the best conformer (out of 250) of baseconformer.sdf and write it to rotamer1.sdf after 100 geometry optimization steps</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-babel/">babel</a>(1), <a href="/docs/linux/man/1-obenergy/">obenergy</a>(1), <a href="/docs/linux/man/1-obfit/">obfit</a>(1), <a href="/docs/linux/man/1-obgrep/">obgrep</a>(1), <a href="/docs/linux/man/1-obminimize/">obminimize</a>(1), <a href="/docs/linux/man/1-obrotate/">obrotate</a>(1). </p>
<p> The web pages for Open Babel can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/">http://openbabel.org/</a></code>&gt;</p>
<h2>AUTHORS</h2>
<p> An -nosplit Open Babel is developed by a cast of many, including currrent maintainers An Geoff Hutchison , An Chris Morley , An Michael Banck , and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/THANKS">http://openbabel.org/wiki/THANKS</a></code>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2001 by OpenEye Scientific Software, Inc.<br />
 Some portions Copyright (C) 2001-2008 by Geoffrey R. Hutchison and other contributors. </p>
<p>&nbsp;<wbr>This program is free software;&nbsp;<wbr>you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation version 2 of the License. </p>
<p>&nbsp;<wbr>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
