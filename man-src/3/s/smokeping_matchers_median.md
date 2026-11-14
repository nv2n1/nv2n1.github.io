---
title: "smokeping_matchers_median(3)"
name: "smokeping_matchers_median"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_matchers_median/"
---

Smokeping::matchers::Median - Find persistant changes in latency 

<h2>Overview</h2>The idea behind this matcher is to find sustained changes in latency. 

 The median matcher takes a number of past median latencies. It splits the latencies into two groups (old and new) and again finds the median for each groups. If the difference between the two medians is bigger than a certain value, it will give a match.
<h2>Description</h2>Call the matcher with the following sequence: 

 <pre> type = matcher
 pattern = Median(old=&gt;x,new=&gt;y,diff=&gt;z)</pre>This will create a matcher which consumes x+y latency-datapoints, builds the two medians and the matches if the difference between the median latency is larger than z seconds.
<h2>Copyright</h2>Copyright (c) 2004 by <font SIZE="-1">OETIKER+PARTNER AG.</font> All rights reserved.
<h2>License</h2>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font>
<h2>Author</h2>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;
