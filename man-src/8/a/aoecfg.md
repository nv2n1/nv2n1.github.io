---
title: "aoecfg(8)"
name: "aoecfg"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aoecfg/"
description: "aoecfg – manipulate AoE configuration strings"
---

<p>aoecfg &#8211; manipulate AoE configuration strings</p>
<h2>Synopsis</h2>
<p><code>aoecfg</code> [-c <i>cmd</i>] [-s <i>cfgstr</i>] [-t <i>timeout</i>] [<i>shelf slot</i>] [<i>netif</i>]</p>
<h2>Description</h2>
<p><i><a href="/docs/linux/man/8-aoecfg/">Aoecfg</a></i>(8) sends AoE configuration commands that control the retrivial, conditional or unconditional setting of AoE configuration strings. Since configuration happens before the MAC address of the target is known, the packet is broadcast. AoE targets with a matching shelf and slot respond. Since the default shelf and slot are the wildcard values 0xffff and 0xff, with no arguments <i><a href="/docs/linux/man/8-aoecfg/">aoecfg</a></i>(8) will return configuration strings from all targets visible on the default interface, <i>eth0</i>.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i> cmd</i></dt>
<dd>specify the AoE configuration command. The default is <i>read</i>. The available commands are</dd>
<dt> <code>read</code></dt>
<dd>Read the server config string without performing any test and respond.</dd>
<dt> <code>test</code></dt>
<dd>Respond only if the specified string exactly matches the server configuration string.</dd>
<dt> <code>prefix</code></dt>
<dd>Respond only if the specified string is a prefix of the server configuration string.</dd>
<dt> <code>set</code></dt>
<dd>If the current server config string is empty, set the server config string to the argument string and respond. If the current server config string is not empty, return a response with Flags bit E set and Error set to 4.</dd>
<dt> <code>fset</code></dt>
<dd>Force set the server config string to the argument string and respond.</dd>
<dt><code>-s</code><i> cfgstr</i></dt>
<dd>specify the config string.</dd>
<dt><code>-t</code><i> timeout</i></dt>
<dd>specify the timeout in seconds. The default is no timeout. If neither the shelf nor the slot are specified, <i><a href="/docs/linux/man/8-aoecfg/">aoecfg</a></i>(8) will exit after the first result. Otherwise, <i><a href="/docs/linux/man/8-aoecfg/">aoecfg</a></i>(8) will exit only after the timeout has expired since it does not know how many responses to expect.</dd>
<dt><code>shelf slot</code></dt>
<dd>specify the shelf and slot used in the query. If unspecified, they default to broadcast.</dd>
<dt><code>netif</code></dt>
<dd>specifiy the network interface. The default is <i>eth0</i>.</dd></dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-aoe-discover/">aoe-discover</a></i>(8), <i><a href="/docs/linux/man/8-aoe-interfaces/">aoe-interfaces</a></i>(8), <i><a href="/docs/linux/man/8-aoe-mkdevs/">aoe-mkdevs</a></i>(8), <i><a href="/docs/linux/man/8-aoe-mkshelf/">aoe-mkshelf</a></i>(8), <i><a href="/docs/linux/man/8-aoe-stat/">aoe-stat</a></i>(8), <i><a href="/docs/linux/man/8-aoeping/">aoeping</a></i>(8), <i>AoE (ATA over Ethernet)</i>: <a rel="nofollow" href="http://www.coraid.com/documents/AoEr10.txt,">http://www.coraid.com/documents/AoEr10.txt,</a> <i>ATA specification</i></p>
<h2>Author</h2>
<p>Erik Quanstrom (quanstro [at] coraid.com)</p>
