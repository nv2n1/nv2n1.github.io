---
title: "aoe-interfaces(8)"
name: "aoe-interfaces"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aoe-interfaces/"
description: "aoe-interfaces – restrict aoe driver to specified network interfaces"
---

<p>aoe-interfaces &#8211; restrict aoe driver to specified network interfaces</p>
<h2>Synopsis</h2>
<pre><code>aoe-interfaces [dev1] [dev2 ...]</code>
<code>aoe-interfaces -c</code></pre>
<h2>Description</h2>
<p>The <i>aoe-interfaces</i> command tells the aoe driver to ignore ATA over Ethernet (AoE) traffic on all but the specified network interfaces. It is analogous to the <i>aoe_iflist</i> module load option. </p>
<p> If neither the <i>aoe_iflist</i> module load option nor the <i>aoe-interfaces</i> command are used, the aoe driver will use any network interface for AoE traffic. </p>
<p> If the aoe driver is a module, then calling <i>aoe-interfaces</i> without arguments will display the current interfaces list. If it hasn&#8217;t been set then the output will be blank. </p>
<p> It&#8217;s good to run the <i>aoe-discover</i> command after setting the AoE interfaces list.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>The <code>-c</code> flag will clear the interface access list, permitting any interface to be used.</dl>
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
 e10.9 eth0 up
nai:~# aoe-interfaces
eth0 eth3</pre>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-aoe-discover/">aoe-discover</a></i>(8), <i><a href="/docs/linux/man/8-aoe-stat/">aoe-stat</a></i>(8), <i><a href="/docs/linux/man/8-aoetools/">aoetools</a></i>(8).</p>
<h2>Author</h2>
<p>Ed L. Cashin (ecashin [at] coraid.com)</p>
