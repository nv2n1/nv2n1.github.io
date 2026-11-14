---
title: "munin-limits(8)"
name: "munin-limits"
section: "8"
letter: "m"
url: "/docs/linux/man/8-munin-limits/"
description: "munin-limits – A program to check for any off-limit values"
---

<p>munin-limits &#8211; A program to check for any off-limit values</p>
<h2>Synopsis</h2>
<p>munin-limits [options]</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;service &lt;service&gt;</code></p>
<dd>Limit services to those of &lt;service&gt;. Multiple &#8211;service options may be supplied. [unset]</p>
<dt><code>&#8211;host &lt;host&gt;</code></p>
<dd>Limit hosts to those of &lt;host&lt;gt&gt;. Multiple &#8211;host options may be supplied. [unset]</p>
<dt><code>&#8211;contact &lt;contact&gt;</code></p>
<dd>Limit contacts to those of &lt;contact&lt;gt&gt;. Multiple &#8211;contact options may be supplied. [unset]</p>
<dt><code>&#8211;config &lt;file&gt;</code></p>
<dd>Use &lt;file&gt; as configuration file. [/etc/munin/munin.conf]</p>
<dt><code>&#8211;always-send &lt;severity list&gt;</code></p>
<dd>Force sending of messages even if you normally wouldn&#8217;t. </p>
<p> The &lt;severity list&gt; can be a whitespace or comma separated list of the values &#8220;ok&#8221;, &#8220;warning&#8221;, &#8220;critical&#8221; or &#8220;unknown&#8221;. </p>
<p> This option may be specified several times, to add more values. </p>
<p> Use of &#8220;&#8211;always-send&#8221; overrides the &#8220;always_send&#8221; value in munin.conf for configured contacts. See also &#8211;force.</p>
<dt><code>&#8211;force</code></p>
<dd>Alias for &#8220;&#8211;always-send ok,warning,critical,unknown&#8221;</p>
<dt><code>&#8211;[no]force-run-as-root</code></p>
<dd>Force running as root (stupid and unnecessary). [&#8211;noforce-root]</p>
<dt><code>&#8211;help</code></p>
<dd>View help message.</p>
<dt><code>&#8211;[no]debug</code></p>
<dd>If set, view debug messages. [&#8211;nodebug]</dl>
<h2>Description</h2>
<p>Munin-limits is a part of the package Munin, which is used in combination with Munin&#8217;s node. Munin is a group of programs to gather data from Munin&#8217;s nodes, graph them, create html-pages, and optionally warn Nagios about any off-limit values. </p>
<p> Munin-limits checks if any values are above or below the set limits, and saves these notes to a file. This file is later used by programs like munin-nagios (to warn nagios) and munin-html (to incorporate them in the web display). </p>
<p> If a service has fields with &#8220;warning&#8221; or &#8220;critical&#8221;-options (e.g. &#8220;load.warning 10&#8221;), and the munin-server configuration file contains the necessary configuration options, munin-limits will check its value.</p>
<h2>Files</h2>
<pre> /etc/munin/munin.conf
 /var/lib/munin/*
 /var/run/munin/*</pre>
<h2>Version</h2>
<p>This is munin-limits version 2.0.29</p>
<h2>Authors</h2>
<p>Knut Haugen, Audun Ytterdal and Jimmy Olsen.</p>
<h2>Bugs</h2>
<p>munin-limits does, as of now, not check the syntax of the configuration file. </p>
<p> Please report other bugs in the bug tracker at &lt;<a rel="nofollow" href="http://munin-monitoring.org/">http://munin-monitoring.org/</a>&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2002-2006 Knut Haugen, Audun Ytterdal, and Jimmy Olsen / Linpro <font SIZE="-1">AS.</font> </p>
<p> This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> </p>
<p> This program is released under the <font SIZE="-1">GNU</font> General Public License</p>
<h2>See Also</h2>
<p>For information on configuration options, please refer to the man page for <i>munin.conf</i>. </p>
