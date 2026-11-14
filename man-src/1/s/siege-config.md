---
title: "siege-config(1)"
name: "siege-config"
section: "1"
letter: "s"
url: "/docs/linux/man/1-siege-config/"
---

<h3><font SIZE="-1">NAME</font></h3><tt>siege</tt>.config - builds a siege.conf template in the user's home directory.
<h3><font SIZE="-1">INTRODUCTION</font></h3><tt>siege</tt>'s default settings are stored in <tt>$HOME</tt>/.siege/siege.conf. This utility will create a new <tt>siege</tt>.conf if one does not already exist. Generally speaking you should not have to run this command with <tt>siege</tt> releases equal or later to 4.0.0. 

 At start up, <tt>siege</tt> checks for a <tt>$HOME</tt>/.siege/siege.conf. If one does not exist, <tt>siege</tt> will run this command to create a new one then read that file to configure itself.
<h3><font SIZE="-1">INVOCATION</font></h3>The format for invoking siege.config is this: 

 <pre> siege.config [no arguments]</pre><h3><font SIZE="-1">AUTHOR</font></h3><tt>Jeffrey Fulmer, et al.</tt> &lt;jeff [at] joedog.org&gt;
<h3><font SIZE="-1">COPYRIGHT</font></h3>Copyright <tt></tt> <tt>Jeffrey Fulmer, et al.</tt> &lt;jeff [at] joedog.org&gt; 

 This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA</font> 02139, <font SIZE="-1">USA</font>.
<h3><font SIZE="-1">AVAILABILITY</font></h3><tt>siege</tt>.config is distributed as part of <tt>siege</tt>
<h3><font SIZE="-1">SEE</font> <font SIZE="-1">ALSO</font></h3>$<i><a HREF="/docs/linux/man/1-_program/">_PROGRAM</a></i>(1)
