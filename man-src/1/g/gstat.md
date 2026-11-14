---
title: "gstat(1)"
name: "gstat"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gstat/"
description: "gstat – manual page for Ganglia Status Tool"
---

<h2>NAME</h2>
<p> gstat &#8211; manual page for Ganglia Status Tool</p>
<h2>SYNOPSIS</h2>
<p> <code>gstat</code> [<i>OPTIONS</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The Ganglia Status Client (gstat) connects with a Ganglia Monitoring Daemon (gmond) and outputs a load-balanced list of hosts</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> List all hosts. Not just hosts running gexec (default=off)</p>
<dt><code>-d</code>, <code>&#8211;dead</code></p>
<dd> Print only the hosts which are dead (default=off)</p>
<dt><code>-m</code>, <code>&#8211;mpifile</code></p>
<dd> Print a load-balanced mpifile (default=off)</p>
<dt><code>-1</code>, <code>&#8211;single_line</code></p>
<dd> Print host and information all on one line (default= off)</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> Print ONLY the host list (default=off)</p>
<dt><code>-n</code>, <code>&#8211;numeric</code></p>
<dd> Print numeric addresses instead of hostnames (default=off)</p>
<dt><code>-i</code>, <code>&#8211;gmond_ip</code>=<i>STRING</i></p>
<dd> Specify the ip address of the gmond to query (default=`localhost&#8217;)</p>
<dt><code>-p</code>, <code>&#8211;gmond_port</code>=<i>INT</i></p>
<dd> Specify the gmond port to query (default=`8649&#8242;)</dl>
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
