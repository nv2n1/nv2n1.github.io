---
title: "ip6tables-save(8)"
name: "ip6tables-save"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip6tables-save/"
description: "iptables-save — dump iptables rules"
---

<p>iptables-save &#8212; dump iptables rules </p>
<p> ip6tables-save &#8212; dump iptables rules</p>
<h2>Synopsis</h2>
<p><code>iptables-save</code> [<code>-M</code> <i>modprobe</i>] [<code>-c</code>] [<code>-t</code> <i>table</i>] [<code>-f</code> <i>filename</i>] </p>
<p> <code>ip6tables-save</code> [<code>-M</code> <i>modprobe</i>] [<code>-c</code>] [<code>-t</code> <i>table</i>] [<code>-f</code> <i>filename</i>]</p>
<h2>Description</h2>
<p><code>iptables-save</code> and <code>ip6tables-save</code> are used to dump the contents of IP or IPv6 Table in easily parseable format either to STDOUT or to a specified file.</p>
<dl>
<dt><code>-M</code>, <code>&#8211;modprobe</code> <i>modprobe_program</i></p>
<dd>Specify the path to the modprobe program. By default, iptables-save will inspect /proc/sys/kernel/modprobe to determine the executable&#8217;s path.</p>
<dt><code>-f</code>, <code>&#8211;file</code> <i>filename</i></p>
<dd>Specify a filename to log the output to. If not specified, iptables-save will log to STDOUT.</p>
<dt><code>-c</code>, <code>&#8211;counters</code></p>
<dd>include the current values of all packet and byte counters in the output</p>
<dt><code>-t</code>, <code>&#8211;table</code> <i>tablename</i></p>
<dd>restrict output to only one table. If the kernel is configured with automatic module loading, an attempt will be made to load the appropriate module for that table if it is not already there.<br />
 If not specified, output includes all available tables.</dl>
<h2>Bugs</h2>
<p>None known as of iptables-1.2.1 release</p>
<h2>Authors</h2>
<p>Harald Welte &lt;laforge [at] gnumonks.org&gt;<br />
 Rusty Russell &lt;rusty [at] rustcorp.com.au&gt;<br />
 Andras Kis-Szabo &lt;kisza [at] sch.bme.hu&gt; contributed ip6tables-save.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iptables-apply/">iptables-apply</a></code>(8),<code><a href="/docs/linux/man/8-iptables-restore/">iptables-restore</a></code>(8), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) The iptables-HOWTO, which details more iptables usage, the NAT-HOWTO, which details NAT, and the netfilter-hacking-HOWTO which details the internals. </p>
