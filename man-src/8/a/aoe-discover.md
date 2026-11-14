---
title: "aoe-discover(8)"
name: "aoe-discover"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aoe-discover/"
description: "aoe-discover – tell aoe driver to discover AoE devices"
---

<p>aoe-discover &#8211; tell aoe driver to discover AoE devices</p>
<h2>Synopsis</h2>
<pre><code>aoe-discover</code></pre>
<h2>Description</h2>
<p>The <i>aoe-discover</i> command tells the aoe driver to discover ATA over Ethernet (AoE) devices on the network. All network interfaces will be probed with a AoE config query broadcast. </p>
<p> If the <i>aoe-interfaces</i> command has limited the allowable network interfaces, only devices discovered via allowable interfaces will become available. The default is to make available all AoE devices found on all accessible ethernet networks. </p>
<p> It&#8217;s good to run the <i>aoe-discover</i> command after running <i>aoe-interfaces</i>.</p>
<h2>Example</h2>
<p>In this example, the root user on a host named <i>nai</i> loads the aoe module with only eth0 allowable for AoE traffic. After remembering that shelf 7 is on eth3, this sysadmin uses <i>aoe-interfaces</i> to add eth3 to the list of allowable network interfaces and then calls <i>aoe-discover</i> to ask the aoe driver to look for new AoE devices.</p>
<dl>
<dd>
<pre>nai:~# modprobe aoe aoe_iflist=&quot;eth0&quot;
nai:~# aoe-stat
 e10.9 eth0 up
nai:~# aoe-interfaces eth0 eth3
nai:~# aoe-discover
nai:~# aoe-stat
 e7.0 eth3 up
 e7.1 eth3 up
 e7.2 eth3 up
 e7.3 eth3 up
 e7.4 eth3 up
 e7.5 eth3 up
 e7.6 eth3 up
 e7.7 eth3 up
 e7.8 eth3 up
 e7.9 eth3 up
 e10.9 eth0 up</pre>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-aoe-interfaces/">aoe-interfaces</a></i>(8), <i><a href="/docs/linux/man/8-aoe-stat/">aoe-stat</a></i>(8), <i><a href="/docs/linux/man/8-aoetools/">aoetools</a></i>(8).</p>
<h2>Author</h2>
<p>Ed L. Cashin (ecashin [at] coraid.com)</p>
