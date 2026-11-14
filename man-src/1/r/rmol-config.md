---
title: "rmol-config(1)"
name: "rmol-config"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmol-config/"
description: "rmol-config –"
---

<h2 class="name">NAME</h2>
<p> rmol-config &#8211; </p>
<pre>
    Configuration Script for the C++ Revenue Management Optimisation Library
</pre>
<h2>SYNOPSIS</h2>
<p> <code>rmol-config</code> [&#8211;prefix] [&#8211;version] [&#8211;libs] [&#8211;cflags]</p>
<h2>DESCRIPTION</h2>
<p> <i>rmol-config</i> is a tool that is used by configure to determine the compiler and linker flags that should be used to compile and link programs that use <i>RMOL</i>. It is also used internally by the .m4 macros, that are included with <i>RMOL</i>, for GNU autoconf.</p>
<h2>OPTIONS</h2>
<p> <i>rmol-config</i> accepts the following options: </p>
<p> <code>&#8211;version</code> </p>
<p>&nbsp;<wbr>Print the currently installed version of RMOL on the standard output. </p>
<p> <code>&#8211;sampledir</code> </p>
<p>&nbsp;<wbr>Show where the&nbsp;<wbr>(CSV)&nbsp;<wbr>sample files are located. </p>
<p> <code>&#8211;libs</code> </p>
<p>&nbsp;<wbr>Print the linker flags that are necessary to link with the RMOL library. </p>
<p> <code>&#8211;cflags</code> </p>
<p>&nbsp;<wbr>Print the compiler flags that are necessary to compile with the RMOL library. </p>
<p> <code>&#8211;prefix</code> </p>
<p>&nbsp;<wbr>Show the RMOL installation prefix.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rmol/">rmol</a>(1)</code>, <code><a href="/docs/linux/man/1-rmol-config/">rmol-config</a></code>(1), <code><a href="/docs/linux/man/1-boost-config/">boost-config</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright © 2007-2013 Denis Arnaud </p>
<p> See the COPYING file for more information on the (LGPLv2+) license, or directly on Internet: </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html</a>&nbsp;<wbr> </p>
<h2>Index</h2>
