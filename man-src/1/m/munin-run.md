---
title: "munin-run(1)"
name: "munin-run"
section: "1"
letter: "m"
url: "/docs/linux/man/1-munin-run/"
description: "munin-run – A program to run Munin plugins from the command line"
---

<h2 class="name">NAME</h2>
<p> munin-run &#8211; A program to run Munin plugins from the command line </p>
<h2>SYNOPSIS</h2>
<p> munin-run [options] &lt;plugin&gt; [ config | autoconf | snmpconf | suggest ]</p>
<h2>DESCRIPTION</h2>
<p> munin-run is a script to run Munin plugins from the command-line. It&#8217;s useful when debugging plugins, as they are run in the same conditions as they are under munin-node.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;config &lt;configfile&gt;</code></p>
<dd> Use &lt;file&gt; as configuration file. [/etc/munin/munin-node.conf]</p>
<dt><code>&#8211;servicedir &lt;dir&gt;</code></p>
<dd> Use &lt;dir&gt; as plugin dir. [/etc/munin/plugins/]</p>
<dt><code>&#8211;sconfdir &lt;dir&gt;</code></p>
<dd> Use &lt;dir&gt; as plugin configuration dir. [/etc/munin/plugin-conf.d/]</p>
<dt><code>&#8211;sconffile &lt;file&gt;</code></p>
<dd> Use &lt;file&gt; as plugin configuration. Overrides sconfdir. [undefined]</p>
<dt><code>&#8211;paranoia </code></p>
<dd> Only run plugins owned by root and check permissions. [disabled]</p>
<dt><code>&#8211;help </code></p>
<dd> View this help message.</p>
<dt><code>&#8211;debug </code></p>
<dd> Print debug messages. Debug messages are sent to <font SIZE="-1">STDOUT</font> and are prefixed with &#8220;#&#8221; (this makes it easier for other parts of munin to use munin-run and still have &#8211;debug on). Only errors go to <font SIZE="-1">STDERR.</font></p>
<dt><code>&#8211;pidebug </code></p>
<dd> Plugin debug. Sets the environment variable <font SIZE="-1">MUNIN_DEBUG</font> to 1 so that plugins may enable debugging. [disabled]</p>
<dt><code>&#8211;version </code></p>
<dd> Show version information.</dl>
<h2>FILES</h2>
<pre>
    /etc/munin/munin-node.conf
    /etc/munin/plugins/*
    /etc/munin/plugin-conf.d/*
    /var/run/munin/munin-node.pid
    /var/log/munin/munin-node.log
</pre>
<h2>VERSION</h2>
<p> This is munin-run (munin-node) v2.0.29 </p>
<p> <tt>$Id</tt>$</p>
<h2>AUTHORS</h2>
<p> Audun Ytterdal, Jimmy Olsen, Tore Anderson, Nicolai Langfeldt.</p>
<h2>BUGS</h2>
<p> Please see &lt;<a rel="nofollow" href="http://munin-monitoring.org/report/1">http://munin-monitoring.org/report/1</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002-2009 Audun Ytterdal, Jimmy Olsen, Tore Anderson, Nicolai Langfeldt / Linpro <font SIZE="-1">AS.</font> </p>
<p> This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> </p>
<p> This program is released under the <font SIZE="-1">GNU</font> General Public License </p>
<h2>Index</h2>
