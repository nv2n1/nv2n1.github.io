---
title: "smokeping_sorters_median(3)"
name: "smokeping_sorters_median"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_sorters_median/"
---

Smokeping::sorters::Median - Order the target charts by Median RTT 

<h2>Overview</h2>Find the charts with the highest Median round trip time.
<h2>Description</h2>Call the sorter in the charts section of the config file 

 <pre> + charts
 menu = Charts
 title = The most interesting destinations
 ++ median
 sorter = Median(entries=&gt;10)
 title = Top Median round trip time
 menu = Median RTT
 format = Median round trip time %f seconds</pre><h2>Copyright</h2>Copyright (c) 2007 by <font SIZE="-1">OETIKER+PARTNER AG.</font> All rights reserved.
<h2>License</h2>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font>
<h2>Author</h2>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;
