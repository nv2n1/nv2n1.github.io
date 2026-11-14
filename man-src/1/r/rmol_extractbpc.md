---
title: "rmol_extractbpc(1)"
name: "rmol_extractbpc"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmol_extractbpc/"
description: "rmol_extractBPC –"
---

<p>rmol_extractBPC &#8211; </p>
<pre> Command-line utility for the C++ Revenue Management Optimisation Library</pre>
<h2>Synopsis</h2>
<p><code>rmol_extractBPC</code> [&#8211;prefix] [-v|&#8211;version] [-h|&#8211;help] [-b|&#8211;builtin] [-i|&#8211;input &lt;path-to-input&gt;] [-l|&#8211;log &lt;path-to-output-log-file&gt;]</p>
<h2>Description</h2>
<p><i>rmol_extractBPC</i> is a small program showing how to use the RMOL library. </p>
<p> <i>rmol_extractBPC</i> accepts the following options: </p>
<p> <code>&#8211;prefix</code> </p>
<p>&nbsp;<wbr>Show the RMOL installation prefix. </p>
<p> <code>-v</code>, <code>&#8211;version</code> </p>
<p>&nbsp;<wbr>Print the currently installed version of RMOL on the standard output. </p>
<p> <code>-h</code>, <code>&#8211;help</code> </p>
<p>&nbsp;<wbr>Produce that message and show usage. </p>
<p> <code>-d</code>, <code>&#8211;draws</code> </p>
<p>&nbsp;<wbr>Number of to-be-generated random draws. </p>
<p> <code>-c</code>, <code>&#8211;capacity</code> </p>
<p>&nbsp;<wbr>Resource capacity&nbsp;<wbr>(e.g., for a flight leg-cabin). </p>
<p> <code>-m</code>, <code>&#8211;method</code> </p>
<p>&nbsp;<wbr>Revenue Management method to be used&nbsp;<wbr>(0&nbsp;<wbr>=&nbsp;<wbr>Monte-Carlo, 1&nbsp;<wbr>=&nbsp;<wbr>Dynamic Programming, 2&nbsp;<wbr>=&nbsp;<wbr>EMSR, 3&nbsp;<wbr>=&nbsp;<wbr>EMSR-a, 4&nbsp;<wbr>=&nbsp;<wbr>EMSR-b) </p>
<p> <code>-b</code>, <code>&#8211;builtin</code> </p>
<p>&nbsp;<wbr>The leg-cabin set up can be either built-in or parsed from an input file. That latter must then be given with the -i/&#8211;input option. In any case, a sample&nbsp;<wbr>(&#8216;dummy&#8217;)&nbsp;<wbr>BOM tree is built from hard-coded parameters to wrap the leg-cabin set-up and allow the usage of classical StdAir API&nbsp;<wbr>(e.g, stdair::BomDisplay::csvDisplay()). </p>
<p> <code>-i</code>, <code>&#8211;input</code> &lt;path-to-input-file&gt; </p>
<p>&nbsp;<wbr>Path&nbsp;<wbr>(absolute or relative)&nbsp;<wbr>of the&nbsp;<wbr>(CSV)&nbsp;<wbr>input file specifying the demand distribution parameters and resource&nbsp;<wbr>(leg-cabin)&nbsp;<wbr>capacities. </p>
<p> <code>-l</code>, <code>&#8211;log</code> &lt;path-to-output-log-file&gt; </p>
<p>&nbsp;<wbr>Path&nbsp;<wbr>(absolute or relative)&nbsp;<wbr>of the output log file. </p>
<p> See the output of the `rmol_extractBPC &#8211;help&#8217; command for default options.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-rmol/">rmol</a>(1)</code>, <code><a href="/docs/linux/man/1-rmol-config/">rmol-config</a></code>(1), <code><a href="/docs/linux/man/3-rmol-library/">rmol-library</a></code>(3)</p>
<h2>Support</h2>
<p>Please report any bugs to <a rel="nofollow" href="http://github.com/airsim/rmol/issues">http://github.com/airsim/rmol/issues</a></p>
<h2>Copyright</h2>
<p>Copyright © 2007-2013 Denis Arnaud </p>
<p> See the COPYING file for more information on the (LGPLv2+) license, or directly on Internet: </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html</a>&nbsp;<wbr></p>
