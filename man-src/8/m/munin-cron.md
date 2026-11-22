---
title: "munin-cron(8)"
name: "munin-cron"
section: "8"
letter: "m"
url: "/docs/linux/man/8-munin-cron/"
description: "munin-cron – A program to batch other Munin master programs"
---

<p>munin-cron &#8211; A program to batch other Munin master programs</p>
<h2>Synopsis</h2>
<p>munin-cron [&#8211;options]</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;service &lt;service&gt;</code></dt>
<dd>Limit services to &lt;service&gt;. Multiple &#8211;service options may be supplied. [unset]</dd>
<dt><code>&#8211;host &lt;host&gt;</code></dt>
<dd>Limit hosts to &lt;host&gt;. Multiple &#8211;host options may be supplied. [unset]</dd>
<dt><code>&#8211;config &lt;file&gt;</code></dt>
<dd>Use &lt;file&gt; as configuration file. [<i>/etc/munin/munin.conf</i>]</dd></dl>
<h2>Description</h2>
<p>Munin-cron is a part of the package Munin, which is used in combination with Munin&#8217;s node. Munin is a group of programs to gather data from Munin&#8217;s nodes, graph them, create html-pages, and optionally warn Nagios about any off-limit values. </p>
<p> Munin-cron batches all the above tasks by running their respective programs. All parameters are passed directly to the underlying programs, so only use parameters that are understood by all the other programs.</p>
<h2>Authors</h2>
<p>Audun Ytterdal and Jimmy Olsen.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2002-2008 Audun Ytterdal and Jimmy Olsen / Linpro AS. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<p> This program is released under the GNU General Public License</p>
