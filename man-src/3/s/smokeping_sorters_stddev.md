---
title: "smokeping_sorters_stddev(3)"
name: "smokeping_sorters_stddev"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_sorters_stddev/"
---

Smokeping::sorters::StdDev - Order the target charts by StdDev 

<h2>Overview</h2>Find the charts with the highest standard deviation among the Pings sent to a single target. The more smoke - higher the standard deviation.
<h2>Description</h2>Call the sorter in the charts section of the config file 

 <pre> + charts
 menu = Charts
 title = The most interesting destinations
 ++ stddev
 sorter = StdDev(entries=&gt;4)
 title = Top StdDev
 menu = Std Deviation
 format = Standard Deviation %f</pre><h2>Copyright</h2>Copyright (c) 2007 by <font SIZE="-1">OETIKER+PARTNER AG.</font> All rights reserved.
<h2>License</h2>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font>
<h2>Author</h2>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;
