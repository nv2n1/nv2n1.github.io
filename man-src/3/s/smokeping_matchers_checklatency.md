---
title: "smokeping_matchers_checklatency(3)"
name: "smokeping_matchers_checklatency"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_matchers_checklatency/"
---

Smokeping::matchers::CheckLatency - Edge triggered alert to check latency is under a value for x number of samples 

<h2>Description</h2>Call the matcher with the following sequence: 

 <pre> type = matcher
 edgetrigger = yes
 pattern = CheckLatency(l=&gt;latency to check against,x=&gt;num samples required for a match)</pre>This will create a matcher which checks for ``l'' latency or greater over ``x'' samples before raising, and will hold the alert until ``x'' samples under ``l'' before clearing
<h2>Copyright</h2>Copyright (c) 2006 Dylan C Vanderhoof, Semaphore Corporation
<h2>License</h2>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font>
<h2>Author</h2>Dylan Vanderhoof &lt;dylanv [at] semaphore.com&gt;
