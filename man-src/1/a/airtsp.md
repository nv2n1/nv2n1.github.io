---
title: "airtsp(1)"
name: "airtsp"
section: "1"
letter: "a"
url: "/docs/linux/man/1-airtsp/"
description: "airtsp –"
---

<h2 class="name">NAME</h2>
<p> airtsp &#8211; </p>
<pre>
  Binary executable for the C++ Simulated Airline Schedule Manager Library
</pre>
<h2>SYNOPSIS</h2>
<p> <code>airtsp</code> [&#8211;prefix] [-v|&#8211;version] [-h|&#8211;help] [-b|&#8211;builtin] [-i|&#8211;input &lt;path-to-input&gt;] [-l|&#8211;log &lt;path-to-output-log-file&gt;]</p>
<h2>DESCRIPTION</h2>
<p> <i>airtsp</i> is a small program showing how to use the AirTSP library. </p>
<p> <i>airtsp</i> accepts the following options: </p>
<p> <code>&#8211;prefix</code> </p>
<p>&nbsp;<wbr>Show the AirTSP installation prefix. </p>
<p> <code>-v</code>, <code>&#8211;version</code> </p>
<p>&nbsp;<wbr>Print the currently installed version of AirTSP on the standard output. </p>
<p> <code>-h</code>, <code>&#8211;help</code> </p>
<p>&nbsp;<wbr>Produce that message and show usage. </p>
<p> <code>-b</code>, <code>&#8211;builtin</code> </p>
<p>&nbsp;<wbr>The sample BOM tree can be either built-in or parsed from input files. In that latter case, the -i/&#8211;input option must be specified as well </p>
<p> <code>-i</code>, <code>&#8211;input</code> &lt;path-to-input-file&gt; </p>
<p>&nbsp;<wbr>Path&nbsp;<wbr>(absolute or relative)&nbsp;<wbr>of the&nbsp;<wbr>(CSV)&nbsp;<wbr>input file specifying the schedule&nbsp;<wbr>(flight-period)&nbsp;<wbr>entries. </p>
<p> <code>-l</code>, <code>&#8211;log</code> &lt;path-to-output-log-file&gt; </p>
<p>&nbsp;<wbr>Path&nbsp;<wbr>(absolute or relative)&nbsp;<wbr>of the output log file. </p>
<p> <code>-r</code>, <code>&#8211;read_booking_request</code> </p>
<p>&nbsp;<wbr>Indicates that a booking request is given as a command-line option. That latter must then be given with the -b/&#8211;bkg_req option. </p>
<p> <code>-q</code>, <code>&#8211;bkg_req</code> &lt;booking-request&gt; </p>
<p>&nbsp;<wbr>Booking request word list&nbsp;<wbr>(e.g.&nbsp;<wbr>&#8216;NCE BKK NCE 2007-04-21 2007-04-21 10:00:00 C 1 DF RO 5 NONE 10:0:0 2000.0 20.0&#8217;), which should be located at the end of the command line&nbsp;<wbr>(otherwise, the other options would be interpreted as part of that booking request word list). </p>
<p> See the output of the `airtsp &#8211;help&#8217; command for default options.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-airtsp-config/">airtsp-config</a></code>(1), <code><a href="/docs/linux/man/3-airtsp-library/">airtsp-library</a></code>(3)</p>
<h2>SUPPORT</h2>
<p> Please report any bugs to <a rel="nofollow" href="https://sourceforge.net/apps/trac/airtsp/report">https://sourceforge.net/apps/trac/airtsp/report</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright © 2009-2013 Denis Arnaud </p>
<p> See the COPYING file for more information on the (LGPLv2+) license, or directly on Internet: </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html</a>&nbsp;<wbr> </p>
<h2>Index</h2>
