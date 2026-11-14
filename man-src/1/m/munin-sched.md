---
title: "munin-sched(1)"
name: "munin-sched"
section: "1"
letter: "m"
url: "/docs/linux/man/1-munin-sched/"
description: "munin-sched – A daemon to gather information in cooperation with the main Munin program"
---

<h2 class="name">NAME</h2>
<p> munin-sched &#8211; A daemon to gather information in cooperation with the main Munin program </p>
<h2>SYNOPSIS</h2>
<p> munin-sched [&#8211;options]</p>
<h2>DESCRIPTION</h2>
<p> munin-sched is a daemon for reporting statistics on system performance. </p>
<p> It doesn&#8217;t produce these itself, but instead relies on a number of plugins which are responsible for gathering the data they require, and describing how this should be graphed. In fact, it does little more than fielding requests from the Munin master, running the appropriate plugins, and returning the output they produce.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;config &lt;configfile&gt;</code></p>
<dd> Use &lt;file&gt; as configuration file. [/etc/munin/munin-node.conf]</p>
<dt><code> &#8211;[no]paranoia </code></p>
<dd> Only run plugins owned by root. Check permissions as well. [&#8211;noparanoia]</p>
<dt><code> &#8211;help </code></p>
<dd> View this help message.</p>
<dt><code> &#8211;debug </code></p>
<dd> View debug messages. This can be very verbose.</dl>
<h2>FILES</h2>
<pre>
    /etc/munin/munin-node.conf
    /etc/munin/plugins/*
    /etc/munin/plugin-conf.d/*
    /var/run/munin/munin-sched.pid
    /var/log/munin/munin-sched.log
</pre>
<h2>VERSION</h2>
<p> This is munin-sched v2.0.29 </p>
<p> <tt>$Id</tt>$</p>
<h2>AUTHORS</h2>
<p> Audun Ytterdal, Jimmy Olsen, and Tore Anderson.</p>
<h2>BUGS</h2>
<p> Please see &lt;<a rel="nofollow" href="http://munin-monitoring.org/report/1">http://munin-monitoring.org/report/1</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002-2006 Audun Ytterdal, Jimmy Olsen, and Tore Anderson / Linpro <font SIZE="-1">AS.</font> </p>
<p> This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> </p>
<p> This program is released under the <font SIZE="-1">GNU</font> General Public License</p>
<h2>SEE ALSO</h2>
<p> For information on configuration options, please refer to the man page for <i>munin-node.conf</i>. </p>
<p> Many plugins can report whether or not they can reasonably be used on the node. <tt>&quot;munin-node-configure&quot;</tt> can use this information to help manage installed plugins. </p>
<p> The network protocol is documented at &lt;<a rel="nofollow" href="http://munin-monitoring.org/wiki/network-protocol">http://munin-monitoring.org/wiki/network-protocol</a>&gt; </p>
<h2>Index</h2>
