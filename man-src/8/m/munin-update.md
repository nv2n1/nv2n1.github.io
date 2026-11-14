---
title: "munin-update(8)"
name: "munin-update"
section: "8"
letter: "m"
url: "/docs/linux/man/8-munin-update/"
description: "munin-update – A program to gather data from machines running munin-node"
---

<p>munin-update &#8211; A program to gather data from machines running munin-node</p>
<h2>Synopsis</h2>
<p>munin-update [options] </p>
<pre> Options:
 --config_file=&lt;file&gt; Use &lt;file&gt; as configuration file. 
 --[no]debug Enable [or disable] debug messages. [--nodebug]
 --[no]fork Query hosts in parallell (--fork), or 
 sequentially (--nofork). [--fork]
 --host &lt;host&gt; Limit graphed hosts to &lt;host&gt;. Multiple --host 
 options may be supplied.
 --service &lt;service&gt; Limit graphed services to &lt;service&gt;. Multiple
 --service options may be supplied.
 --timeout=&lt;seconds&gt; TCP timeout when talking to clients. [$timeout]
 --help View this message.
 --version View version information.</pre>
<h2>Options</h2>
<dl>
<dt><code>&#8211;config_file=&lt;file&gt;</code></p>
<dd>Use &lt;file&gt; as the configuration file. [/etc/munin/munin.conf]</p>
<dt><code>&#8211;[no]debug</code></p>
<dd>If set, log debug messages. [&#8211;nodebug]</p>
<dt><code>&#8211;[no]fork</code></p>
<dd>If set, will fork off one process for each host. [&#8211;fork]</p>
<dt><code>&#8211;host &lt;host&gt;</code></p>
<dd>Limit fetched data to those from &lt;host&lt;gt&gt;. Multiple &#8211;host options may be supplied. [unset]</p>
<dt><code>&#8211;service &lt;service&gt;</code></p>
<dd>Limit fetched data to those of &lt;service&gt;. Multiple &#8211;service options may be supplied. [unset]</p>
<dt><code>&#8211;timeout &lt;seconds&gt;</code></p>
<dd>Set the network timeout to &lt;seconds&gt;. [180]</p>
<dt><code>&#8211;help</code></p>
<dd>Print the help message then exit.</p>
<dt><code>&#8211;version</code></p>
<dd>Print version information then exit.</dl>
<h2>Description</h2>
<p>Munin-update is a part of the package Munin, which is used in combination with Munin&#8217;s node. Munin is a group of programs to gather data from Munin&#8217;s nodes, graph them, create html-pages, and optionally warn Nagios about any off-limit values. </p>
<p> Munin-update does the gathering. It is usually only used from within munin-cron. </p>
<p> It contacts each host&#8217;s munin-node in turn, gathers data from it, and stores them in .rrd-files. If necessary, it will create the rrd-files and the directories to store them in.</p>
<h2>Files</h2>
<pre> /etc/munin/munin.conf
 /var/lib/munin/*
 /var/log/munin/munin-update
 /var/run/munin/*</pre>
<h2>Bugs</h2>
<p>For a list of bugs concerning munin-update, see <font SIZE="-1">FI</font>. </p>
<p> Please report bugs in the bug tracker at &lt;<a rel="nofollow" href="http://munin-monitoring.org/">http://munin-monitoring.org/</a>&gt;.</p>
<h2>Authors</h2>
<p>The Munin Team. <font SIZE="-1">FIX</font></p>
<h2>Copyright</h2>
<p>Copyright X 2002-2009 Jimmy Olsen, Audun Ytterdal, Tore Andersson, Kjell-Magne Oierud, Linpro <font SIZE="-1">AS,</font> Redpill Linpro <font SIZE="-1">AS</font> </p>
<p> This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> </p>
<p> This program is released under the <font SIZE="-1">GNU</font> General Public License.</p>
