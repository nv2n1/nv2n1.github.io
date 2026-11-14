---
title: "gmetric(1)"
name: "gmetric"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmetric/"
description: "gmetric – manual page for Ganglia Custom Metric Utility"
---

<h2>NAME</h2>
<p> gmetric &#8211; manual page for Ganglia Custom Metric Utility</p>
<h2>SYNOPSIS</h2>
<p> <code>gmetric</code> [<i>OPTIONS</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The Ganglia Metric Client (gmetric) announces a metric on the list of defined send channels defined in a configuration file</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit</p>
<dt><code>-c</code>, <code>&#8211;conf</code>=<i>STRING</i></p>
<dd> The configuration file to use for finding send channels (default=`/etc/ganglia/gmond.conf&#8217;)</p>
<dt><code>-n</code>, <code>&#8211;name</code>=<i>STRING</i></p>
<dd> Name of the metric</p>
<dt><code>-v</code>, <code>&#8211;value</code>=<i>STRING</i></p>
<dd> Value of the metric</p>
<dt><code>-t</code>, <code>&#8211;type</code>=<i>STRING</i></p>
<dd> Either string|int8|uint8|int16|uint16|int32|uint32|float|double</p>
<dt><code>-u</code>, <code>&#8211;units</code>=<i>STRING</i></p>
<dd> Unit of measure for the value e.g. Kilobytes, Celcius (default=`&#8217;)</p>
<dt><code>-s</code>, <code>&#8211;slope</code>=<i>STRING</i></p>
<dd> Either zero|positive|negative|both (default=`both&#8217;)</p>
<dt><code>-x</code>, <code>&#8211;tmax</code>=<i>INT</i></p>
<dd> The maximum time in seconds between gmetric calls (default=`60&#8242;)</p>
<dt><code>-d</code>, <code>&#8211;dmax</code>=<i>INT</i></p>
<dd> The lifetime in seconds of this metric (default=`0&#8242;)</p>
<dt><code>-g</code>, <code>&#8211;group</code>=<i>STRING</i></p>
<dd> Group of the metric</p>
<dt><code>-D</code>, <code>&#8211;desc</code>=<i>STRING</i></p>
<dd> Description of the metric</p>
<dt><code>-T</code>, <code>&#8211;title</code>=<i>STRING</i></p>
<dd> Title of the metric</p>
<dt><code>-S</code>, <code>&#8211;spoof</code>=<i>STRING</i></p>
<dd> IP address and name of host/device (colon separated) we are spoofing (default=`&#8217;)</p>
<dt><code>-H</code>, <code>&#8211;heartbeat</code></p>
<dd> spoof a heartbeat message (use with spoof option)</dl>
<h2>AUTHOR</h2>
<p> Matt Massie &lt;massie [at] cs.berkeley.edu&gt;</p>
<h2>REPORTING BUGS</h2>
<p> Report all bugs to the Ganglia Github project at </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://github.com/ganglia/monitor-core/issues">https://github.com/ganglia/monitor-core/issues</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001, 2002, 2003, 2004, 2005 by The Regents of the University of California. All rights reserved. </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose, without fee, and without written agreement is hereby granted, provided that the above copyright notice and the following two paragraphs appear in all copies of this software. </p>
<p> IN NO EVENT SHALL THE UNIVERSITY OF CALIFORNIA BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF THE UNIVERSITY OF CALIFORNIA HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. </p>
<p> THE UNIVERSITY OF CALIFORNIA SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS ON AN &quot;AS IS&quot; BASIS, AND THE UNIVERSITY OF CALIFORNIA HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS. </p>
<h2>Index</h2>
