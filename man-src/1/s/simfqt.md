---
title: "simfqt(1)"
name: "simfqt"
section: "1"
letter: "s"
url: "/docs/linux/man/1-simfqt/"
description: "simfqt –"
---

<h2 class="name">NAME</h2>
<p> simfqt &#8211; </p>
<pre>
  Command-line interpreter for the C++ Simulated Fare Quote System Library
</pre>
<h2>SYNOPSIS</h2>
<p> <code>simfqt</code> [&#8211;prefix] [-v|&#8211;version] [-h|&#8211;help] [-b|&#8211;builtin] [-i|&#8211;input &lt;path-to-input&gt;] [-l|&#8211;log &lt;path-to-output-log-file&gt;]</p>
<h2>DESCRIPTION</h2>
<p> <i>simfqt</i> is a small program showing how to use the SimFQT library. </p>
<p> <i>simfqt</i> accepts the following options: </p>
<p> <code>&#8211;prefix</code> </p>
<p>&nbsp;<wbr>Show the SimFQT installation prefix. </p>
<p> <code>-v</code>, <code>&#8211;version</code> </p>
<p>&nbsp;<wbr>Print the currently installed version of SimFQT on the standard output. </p>
<p> <code>-h</code>, <code>&#8211;help</code> </p>
<p>&nbsp;<wbr>Produce that message and show usage. </p>
<p> <code>-b</code>, <code>&#8211;builtin</code> </p>
<p>&nbsp;<wbr>The sample BOM tree can be either built-in or parsed from an input file. That latter must then be given with the -f/&#8211;fare option </p>
<p> <code>-f</code>, <code>&#8211;fare</code> &lt;path-to-fare-input-file&gt; </p>
<p>&nbsp;<wbr>Path&nbsp;<wbr>(absolute or relative)&nbsp;<wbr>of the&nbsp;<wbr>(CSV)&nbsp;<wbr>input file specifying the fare rules. </p>
<p> <code>-l</code>, <code>&#8211;log</code> &lt;path-to-output-log-file&gt; </p>
<p>&nbsp;<wbr>Path&nbsp;<wbr>(absolute or relative)&nbsp;<wbr>of the output log file. </p>
<p> See the output of the `simfqt &#8211;help&#8217; command for default options.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-simfqt-config/">simfqt-config</a></code>(1), <code><a href="/docs/linux/man/1-simfqt-parsefarerules/">simfqt-parseFareRules</a></code>(1), <code><a href="/docs/linux/man/3-simfqt-library/">simfqt-library</a></code>(3)</p>
<h2>SUPPORT</h2>
<p> Please report any bugs to <a rel="nofollow" href="https://sourceforge.net/apps/trac/simfqt/report">https://sourceforge.net/apps/trac/simfqt/report</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright © 2009-2011 Denis Arnaud </p>
<p> See the COPYING file for more information on the (LGPLv2+) license, or directly on Internet: </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html</a>&nbsp;<wbr> </p>
<h2>Index</h2>
