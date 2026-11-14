---
title: "gmond(1)"
name: "gmond"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmond/"
description: "gmond – manual page for Ganglia Monitor Daemon"
---

<h2>NAME</h2>
<p> gmond &#8211; manual page for Ganglia Monitor Daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>gmond</code> [<i>OPTIONS</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The Ganglia Monitoring Daemon (gmond) listens to the cluster message channel, stores the data in-memory and when requested will output an XML description of the state of the cluster</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit</p>
<dt><code>-c</code>, <code>&#8211;conf</code>=<i>STRING</i></p>
<dd> Location of gmond configuration file (default= `/etc/ganglia/gmond.conf&#8217;)</p>
<dt><code>-l</code>, <code>&#8211;location</code>=<i>STRING</i></p>
<dd> Location of this host in the cluster &#8216;rack,rank,plane&#8217;. (default=`0,0,0&#8242;)</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>INT</i></p>
<dd> Debug level. If greater than zero, daemon will stay in foreground. (default=`0&#8242;)</p>
<dt><code>-f</code>, <code>&#8211;foreground</code></p>
<dd> Run in foreground (don&#8217;t daemonize) (default=off)</p>
<dt><code>-t</code>, <code>&#8211;default_config</code></p>
<dd> Print the default configuration to stdout and exit (default=off)</p>
<dt><code>-m</code>, <code>&#8211;metrics</code></p>
<dd> Print the list of metrics this gmond supports (default=off)</p>
<dt><code>-b</code>, <code>&#8211;bandwidth</code></p>
<dd> Calculate minimum bandwidth use for configuration (default=off)</p>
<dt><code>-r</code>, <code>&#8211;convert</code>=<i>STRING</i></p>
<dd> Convert a 2.5.x configuration file to the new 3.x format</p>
<dt><code>-p</code>, <code>&#8211;pid-file</code>=<i>STRING</i></p>
<dd> Write process-id to file</dl>
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
