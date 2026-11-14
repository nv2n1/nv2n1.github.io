---
title: "ro-localization(1)"
name: "ro-localization"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ro-localization/"
description: "ro-localization – Monte-Carlo localization for beacon range-only measurements"
---

<h2 class="name">NAME</h2>
<p> ro-localization &#8211; Monte-Carlo localization for beacon range-only measurements </p>
<h2>SYNOPSIS</h2>
<p> ro-localization <i>config_file.ini</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ro-localization</code> is a command-line application which processes a rawlog and tracks a mobile robot pose from the sequence of odometry and observations. It can also perform global localization. </p>
<p> This program is a specialization of pf-localization, with an extended model to cope with unknown, dynamic biases in the beacon ranges. It also shows a real-time visualization in 3D of the particles, the beacons, and the measurements.</p>
<h2>BUGS</h2>
<p> Please report bugs at <a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=205280">http://sourceforge.net/tracker/?group_id=205280</a>&amp;atid=993006</p>
<h2>SEE ALSO</h2>
<p> The application wiki page at <a rel="nofollow" href="http://babel.isa.uma.es/mrpt/index.php/Applications">http://babel.isa.uma.es/mrpt/index.php/Applications</a> </p>
<p> <code>pf-localization</code></p>
<h2>AUTHORS</h2>
<p> <code>ro-localization</code> is part of the Mobile Robot Programming Toolkit (<font SIZE="-1">MRPT</font>), and was originally written by the <font SIZE="-1">MAPIR</font> laboratory (University of Malaga). </p>
<p> This manual page was written by Jose Luis Blanco &lt;joseluisblancoc [at] gmail.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 3, or (at your option) any later version. </p>
<p> On Debian GNU/Linux systems, the complete text of the <font SIZE="-1">GNU</font> General Public License can be found in `/usr/share/common-licenses/GPL&#8217;. </p>
<h2>Index</h2>
