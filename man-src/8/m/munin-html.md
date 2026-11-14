---
title: "munin-html(8)"
name: "munin-html"
section: "8"
letter: "m"
url: "/docs/linux/man/8-munin-html/"
description: "munin-html – A program to generate html-pages in an Munin installation"
---

<p>munin-html &#8211; A program to generate html-pages in an Munin installation</p>
<h2>Synopsis</h2>
<p>munin-html [options]</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;service &lt;service&gt;</code></p>
<dd>Limit services to those of &lt;service&gt;. Multiple &#8211;service options may be supplied. [unset]</p>
<dt><code>&#8211;host &lt;host&gt;</code></p>
<dd>Limit hosts to those of &lt;host&lt;gt&gt;. Multiple &#8211;host options may be supplied. [unset]</p>
<dt><code>&#8211;config &lt;file&gt;</code></p>
<dd>Use &lt;file&gt; as configuration file. [/etc/munin/munin.conf]</p>
<dt><code>&#8211;help</code></p>
<dd>View help message.</p>
<dt><code>&#8211;[no]debug</code></p>
<dd>If set, view debug messages. [&#8211;nodebug]</dl>
<h2>Description</h2>
<p>Munin-html is a part of the package Munin, which is used in combination with Munin&#8217;s node. Munin is a group of programs to gather data from Munin&#8217;s nodes, graph them, create html-pages, and optionally warn Nagios about any off-limit values. </p>
<p> Munin-html creates the html pages.</p>
<h2>Files</h2>
<pre> /etc/munin/munin.conf
 /var/lib/munin/datafile
 /var/log/munin/munin-html
 /var/cache/munin/www/*
 /var/run/munin/*</pre>
<h2>Version</h2>
<p>This is munin-html version svn-trunk-r4007</p>
<h2>Authors</h2>
<p>Knut Haugen, Audun Ytterdal and Jimmy Olsen.</p>
<h2>Bugs</h2>
<p>munin-html does, as of now, not check the syntax of the configuration file. </p>
<p> Please report other bugs in the bug tracker at &lt;<a rel="nofollow" href="http://munin-monitoring.org/">http://munin-monitoring.org/</a>&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2002-2009 Knut Haugen, Audun Ytterdal, and Jimmy Olsen / Linpro <font SIZE="-1">AS.</font> </p>
<p> This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> </p>
<p> This program is released under the <font SIZE="-1">GNU</font> General Public License</p>
<h2>See Also</h2>
<p>For information on configuration options, please refer to the man page for <i>munin.conf</i>. </p>
