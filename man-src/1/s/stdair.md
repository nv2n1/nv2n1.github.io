---
title: "stdair(1)"
name: "stdair"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stdair/"
description: "stdair – C++ Standard Airline IT Object Library"
---

<h2 class="name">NAME</h2>
<p> stdair &#8211; C++ Standard Airline IT Object Library</p>
<h2>SYNOPSIS</h2>
<p> <code>stdair</code> [&#8211;prefix] [-v|&#8211;version] [-h|&#8211;help] [-b|&#8211;builtin] [-i|&#8211;input &lt;path-to-input&gt;] [-l|&#8211;log &lt;path-to-output-log-file&gt;]</p>
<h2>DESCRIPTION</h2>
<p> <i>stdair</i> is a small program showing how to use the StdAir library. </p>
<p> <i>stdair</i> accepts the following options: </p>
<p> <code>&#8211;prefix</code> </p>
<p>&nbsp;<wbr>Show the StdAir installation prefix. </p>
<p> <code>-v</code>, <code>&#8211;version</code> </p>
<p>&nbsp;<wbr>Print the currently installed version of StdAir on the standard output. </p>
<p> <code>-h</code>, <code>&#8211;help</code> </p>
<p>&nbsp;<wbr>Produce that message and show usage. </p>
<p> <code>-b</code>, <code>&#8211;builtin</code> </p>
<p>&nbsp;<wbr>The sample BOM tree can be either built-in or parsed from an input file. When that option is selected, an input file must then be given with the -i/&#8211;input option. When that option is not selected, the&nbsp;<wbr><code>stdair</code>&nbsp;<wbr>program builds a simple use case directly from internal hard-coded parameters&nbsp;<wbr>(demand distribution details and resource/cabin capacities). </p>
<p> <code>-r</code>, <code>&#8211;rmol</code> </p>
<p>&nbsp;<wbr>The sample BOM tree corresponds to a typical usage by RMOL </p>
<p> <code>-c</code>, <code>&#8211;crs</code> </p>
<p>&nbsp;<wbr>The sample BOM tree corresponds to a typical usage by SimCRS </p>
<p> <code>-i</code>, <code>&#8211;input</code> &lt;path-to-input-file&gt; </p>
<p>&nbsp;<wbr>Path&nbsp;<wbr>(absolute or relative)&nbsp;<wbr>of the&nbsp;<wbr>(CVS)&nbsp;<wbr>input file specifying the demand distribution parameters and resource&nbsp;<wbr>(cabin)&nbsp;<wbr>capacities. </p>
<p> <code>-l</code>, <code>&#8211;log</code> &lt;path-to-output-log-file&gt; </p>
<p>&nbsp;<wbr>Path&nbsp;<wbr>(absolute or relative)&nbsp;<wbr>of the output log file. </p>
<p> See the output of the `stdair &#8211;help&#8217; command for default options.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-stdair-config/">stdair-config</a></code>(1), <code><a href="/docs/linux/man/3-stdair-library/">stdair-library</a></code>(3)</p>
<h2>SUPPORT</h2>
<p> Please report any bugs to <a rel="nofollow" href="https://sourceforge.net/apps/trac/stdair/report">https://sourceforge.net/apps/trac/stdair/report</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright © 2009-2011 Denis Arnaud </p>
<p> See the COPYING file for more information on the (LGPLv2+) license, or directly on Internet: </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html</a>&nbsp;<wbr> </p>
<h2>Index</h2>
