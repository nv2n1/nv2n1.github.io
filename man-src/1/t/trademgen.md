---
title: "trademgen(1)"
name: "trademgen"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trademgen/"
description: "trademgen –"
---

<h2 class="name">NAME</h2>
<p> trademgen &#8211; </p>
<pre>
  Interactive command-line utility for the C++ Simulated Travel Demand Generation Library
</pre>
<h2>SYNOPSIS</h2>
<p> <code>trademgen</code> [&#8211;prefix] [-v|&#8211;version] [-h|&#8211;help] [-b|&#8211;builtin] [-i|&#8211;input &lt;path-to-input&gt;] [-l|&#8211;log &lt;path-to-output-log-file&gt;]</p>
<h2>DESCRIPTION</h2>
<p> <i>trademgen</i> is a small interactive program showing how to use the TraDemGen library. </p>
<p> <i>trademgen</i> accepts the following options: </p>
<p> <code>&#8211;prefix</code> </p>
<p>&nbsp;<wbr>Show the TraDemGen installation prefix. </p>
<p> <code>-v</code>, <code>&#8211;version</code> </p>
<p>&nbsp;<wbr>Print the currently installed version of TraDemGen on the standard output. </p>
<p> <code>-h</code>, <code>&#8211;help</code> </p>
<p>&nbsp;<wbr>Produce that message and show usage. </p>
<p> <code>-b</code>, <code>&#8211;builtin</code> </p>
<p>&nbsp;<wbr>The sample BOM tree can be either built-in or parsed from an input file. That latter must then be given with the -i/&#8211;input option. </p>
<p> <code>-s</code>, <code>&#8211;see</code> </p>
<p>&nbsp;<wbr>Seed for the random generation. It allows to reproduce exactly any demand generation. </p>
<p> <code>-d</code>, <code>&#8211;draws</code> Number of runs for the demand generation. </p>
<p> <code>-G</code>, <code>&#8211;demandgeneration</code> Method used to generate the demand (i.e., the booking requests): Poisson Process (P) or Order Statistics (S). </p>
<p> <code>-i</code>, <code>&#8211;input</code> &lt;path-to-input-file&gt; </p>
<p>&nbsp;<wbr>Path&nbsp;<wbr>(absolute or relative)&nbsp;<wbr>of the&nbsp;<wbr>(CSV)&nbsp;<wbr>input file specifying the demand distributions. </p>
<p> <code>-o</code>, <code>&#8211;output</code> &lt;path-to-output-file&gt; </p>
<p>&nbsp;<wbr>Path&nbsp;<wbr>(absolute or relative)&nbsp;<wbr>of the&nbsp;<wbr>(CSV)&nbsp;<wbr>output file for the generated booking requests. </p>
<p> <code>-l</code>, <code>&#8211;log</code> &lt;path-to-output-log-file&gt; </p>
<p>&nbsp;<wbr>Path&nbsp;<wbr>(absolute or relative)&nbsp;<wbr>of the output log file. </p>
<p> See the output of the `trademgen &#8211;help&#8217; command for default options.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-trademgen_generatedemand/">trademgen_generateDemand</a>(1)</code>, <code><a href="/docs/linux/man/1-trademgen_with_db/">trademgen_with_db</a>(1)</code>, <code><a href="/docs/linux/man/1-pytrademgen/">pytrademgen</a>(1)</code>, <code><a href="/docs/linux/man/1-trademgen-config/">trademgen-config</a></code>(1), <code><a href="/docs/linux/man/3-trademgen-library/">trademgen-library</a></code>(3)</p>
<h2>SUPPORT</h2>
<p> Please report any bugs to <a rel="nofollow" href="http://github.com/airsim/trademgen/issues">http://github.com/airsim/trademgen/issues</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright © 2009-2013 Denis Arnaud </p>
<p> See the COPYING file for more information on the (LGPLv2+) license, or directly on Internet: </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html</a>&nbsp;<wbr> </p>
<h2>Index</h2>
