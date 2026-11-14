---
title: "grid-matching(1)"
name: "grid-matching"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grid-matching/"
description: "grid-matching – Executes occupancy grid matching techniques"
---

<h2 class="name">NAME</h2>
<p> grid-matching &#8211; Executes occupancy grid matching techniques </p>
<h2>SYNOPSIS</h2>
<p> grid-matching &#8211;match &#8211;map1=<i>grid1.simplemap</i> &#8211;map2=<i>grid1.simplemap</i> [<i>options</i>] grid-matching &#8211;detect-test &#8211;map1=<i>grid1.simplemap</i> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>grid-matching</code> is a command-line application which takes two maps as input and computes a Sum-Of-Gaussians (<font SIZE="-1">SOG</font>) density distribution for the 2D transformation between them, if they are found to match.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;match</code> Operation: match two maps <code>&#8211;detect-test</code> Operation: Quality of match with one map <code>&#8211;map1</code> arg Map #1 to align (*.simplemap) <code>&#8211;map2</code> arg Map #2 to align (*.simplemap) <code>&#8211;out</code> arg (=gridmatching_out.txt) Output file for the results <code>&#8211;config</code> arg Optional config. file with more params <code>&#8211;save-sog-3d</code> Save a 3D view of all the <font SIZE="-1">SOG</font> modes <code>&#8211;save-sog-all</code> Save all the map overlaps <code>&#8211;noise-xy</code> arg (=0) In detect-test mode,std. noise in <font SIZE="-1">XY</font> <code>&#8211;noise-phi</code> arg (=0) In detect-test mode,std. noise in <font SIZE="-1">PHI</font> (deg) <code>&#8211;Ax</code> arg (=4) In detect-test mode, displacement in X <code>&#8211;Ay</code> arg (=2) In detect-test mode, displacement in Y <code>&#8211;Aphi</code> arg (=30) In detect-test mode, displ. in <font SIZE="-1">PHI</font> (deg) <code>&#8211;verbose</code> verbose output <code>&#8211;nologo</code> skip the logo at startup <code>&#8211;help</code> produce help message</p>
<h2>BUGS</h2>
<p> Please report bugs at <a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=205280">http://sourceforge.net/tracker/?group_id=205280</a>&amp;atid=993006</p>
<h2>SEE ALSO</h2>
<p> The application wiki page at <a rel="nofollow" href="http://babel.isa.uma.es/mrpt/index.php/Applications">http://babel.isa.uma.es/mrpt/index.php/Applications</a></p>
<h2>AUTHORS</h2>
<p> <code>grid-matching</code> is part of the Mobile Robot Programming Toolkit (<font SIZE="-1">MRPT</font>), and was originally written by the <font SIZE="-1">MAPIR</font> laboratory (University of Malaga). </p>
<p> This manual page was written by Jose Luis Blanco &lt;joseluisblancoc [at] gmail.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 3, or (at your option) any later version. </p>
<p> On Debian GNU/Linux systems, the complete text of the <font SIZE="-1">GNU</font> General Public License can be found in `/usr/share/common-licenses/GPL&#8217;. </p>
<h2>Index</h2>
