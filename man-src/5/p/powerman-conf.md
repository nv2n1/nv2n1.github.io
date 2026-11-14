---
title: "powerman-conf(5)"
name: "powerman-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-powerman-conf/"
description: "powerman.conf – configuration file for PowerMan"
---

<p>powerman.conf &#8211; configuration file for PowerMan</p>
<h2>Description</h2>
<p>The powerman.conf file typically includes one or more of the remote power controller (RPC) device files provided in the /etc/powerman directory; sets a few global options; instantiates RPC devices with unique names, hostnames, and ports; and maps node names to RPC&#8217;s and plug numbers. </p>
<p> Network-attached RPC&#8217;s are instantiated with device lines of the form:</p>
<dl>
<dd>device &quot;name&quot; &quot;type&quot; &quot;host:port&quot;</dl>
<p> Serial-attached RPC&#8217;s are instantiated with device lines of the form:</p>
<dl>
<dd>device &quot;name&quot; &quot;type&quot; &quot;special file&quot; &quot;flags&quot;</dl>
<p> where special file is the full path to a tty device, and flags is a serial parameter specification in a form similar to that used by lilo, e.g. &quot;9600,8n1&quot;. RPC&#8217;s that are accessed via coprocesses are instantiated as follows:</p>
<dl>
<dd>device &quot;name&quot; &quot;type&quot; &quot;process |&amp;&quot;</dl>
<p> where process is the full path to a process whose standard output and input will be controlled by powerman, e.g. &quot;/usr/bin/conman -Q -j rpc0 |&amp;&quot;.</p>
<h2>Example</h2>
<p>The following example is a 16-node cluster that uses two 8-plug Baytech RPC-3 remote power controllers. </p>
<pre>include &quot;/etc/powerman/baytech.dev&quot; # include def for &quot;baytech&quot; RPC
tcpwrappers yes # enable TCP wrappers
# listen &quot;0.0.0.0:10101&quot; # uncomment to listen on all interfaces
# Alias example - alias can be used in target specifications
alias &quot;pengra_service&quot; &quot;pengra[0-1]&quot;
alias &quot;pengra_compute&quot; &quot;pengra[2-15]&quot;
# Power controller: device &lt;name&gt; &lt;type&gt; &lt;hostname:port&gt; [&lt;flags&gt;]
device &quot;pow0&quot; &quot;baytech&quot; &quot;pow0:23&quot; # instantiate pow0
device &quot;pow1&quot; &quot;baytech&quot; &quot;pow1:23&quot; # instantiate pow1
# Plugs: node &lt;name&gt; &lt;device&gt; [&lt;plug&gt;]
node &quot;pengra[0-7]&quot; &quot;pow0&quot; &quot;[1-8]&quot; # map pengra0...pengra7 to pow0 plug 1-8
node &quot;pengra[8-15]&quot; &quot;pow1&quot; &quot;[1-8]&quot; # map pengra8...pengra15 to pow1 plug 1-8</pre>
<h2>Files</h2>
<p>/etc/powerman/powerman.conf<br />
 /etc/powerman/*.dev</p>
<h2>Origin</h2>
<p>PowerMan was originally developed by Andrew Uselton on LLNL&#8217;s Linux clusters. This software is open source and distributed under the terms of the GNU GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-powerman/">powerman</a></code>(1), <code><a href="/docs/linux/man/8-powermand/">powermand</a></code>(8), <code><a href="/docs/linux/man/8-httppower/">httppower</a></code>(8), <code><a href="/docs/linux/man/8-plmpower/">plmpower</a></code>(8), <code><a href="/docs/linux/man/8-vpcd/">vpcd</a></code>(8), <code><a href="/docs/linux/man/5-powerman-conf/">powerman.conf</a></code>(5), <code><a href="/docs/linux/man/5-powerman-dev/">powerman.dev</a></code>(5). <code><a rel="nofollow" href="http://code.google.com/p/powerman">http://code.google.com/p/powerman</a></code> </p>
