---
title: "simul-gridmap(1)"
name: "simul-gridmap"
section: "1"
letter: "s"
url: "/docs/linux/man/1-simul-gridmap/"
description: "simul-gridmap – Robot dataset simulator from a gridmap and a predefined robot path"
---

<h2 class="name">NAME</h2>
<p> simul-gridmap &#8211; Robot dataset simulator from a gridmap and a predefined robot path </p>
<h2>SYNOPSIS</h2>
<p> simul-gridmap <i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i></p>
<h2>DESCRIPTION</h2>
<p> <code>simul-gridmap</code> is a command-line application which generates a synthetic rawlog of a simulated robot as it follows a path (given by the <i>poses.txt</i> file) and takes measurements from a laser scanner in a world defined through an occupancy grid map.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code> produce help message </p>
<p> <code>&#8211;grid</code> arg grid map file (*.gridmap or *.gridmap.gz) </p>
<p> <code>&#8211;poses</code> arg poses text file, one &#8216;time x y phi&#8217; line per pose </p>
<p> <code>&#8211;out-rawlog</code> arg the output rawlog to generate from which to take noisy<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>odometry </p>
<p> <code>&#8211;in-rawlog</code> arg (optional) the rawlog from which to take noisy odometry </p>
<p> <code>&#8211;ranges</code> arg (=361) number of laser ranges per scan (default=361) </p>
<p> <code>&#8211;span</code> arg (=180) span of the laser scans (default=180 degrees) </p>
<p> <code>&#8211;std_r</code> arg (=0.01) range noise sigma (default=0.01 meters) </p>
<p> <code>&#8211;std_b</code> arg (=0.05) bearing noise sigma (default=0.05 degrees) </p>
<p> <code>&#8211;nologo</code> skip the logo at startup</p>
<h2>BUGS</h2>
<p> Please report bugs at <a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=205280">http://sourceforge.net/tracker/?group_id=205280</a>&amp;atid=993006</p>
<h2>SEE ALSO</h2>
<p> The application wiki page at <a rel="nofollow" href="http://babel.isa.uma.es/mrpt/index.php/Applications">http://babel.isa.uma.es/mrpt/index.php/Applications</a></p>
<h2>AUTHORS</h2>
<p> <code>simul-gridmap</code> is part of the Mobile Robot Programming Toolkit (<font SIZE="-1">MRPT</font>), and was originally written by the <font SIZE="-1">MAPIR</font> laboratory (University of Malaga). </p>
<p> This manual page was written by Jose Luis Blanco &lt;joseluisblancoc [at] gmail.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 3, or (at your option) any later version. </p>
<p> On Debian GNU/Linux systems, the complete text of the <font SIZE="-1">GNU</font> General Public License can be found in `/usr/share/common-licenses/GPL&#8217;. </p>
<h2>Index</h2>
