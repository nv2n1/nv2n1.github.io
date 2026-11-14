---
title: "pppoe-start(8)"
name: "pppoe-start"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppoe-start/"
description: "pppoe-start – Shell script to bring up a PPPoE link"
---

<p>pppoe-start &#8211; Shell script to bring up a PPPoE link</p>
<h2>Synopsis</h2>
<p><code>pppoe-start </code>[<i>config_file</i>] <code>pppoe-start </code><i>interface user</i> [<i>config_file</i>] </p>
<h2>Description</h2>
<p><code>pppoe-start</code> is a shell script which starts the Roaring Penguin user-space PPPoE client. If you omit <i>config_file</i>, the default file <code>/etc/sysconfig/network-scripts/ifcfg-ppp0</code> is used. If you supply <i>interface</i> and <i>user</i>, then they override the Ethernet interface and user-name settings in the configuration file. </p>
<h2>Author</h2>
<p><code>pppoe-start</code> was written by David F. Skoll &lt;dfs [at] roaringpenguin.com&gt;. </p>
<p> The <code>pppoe</code> home page is <i><a rel="nofollow" href="http://www.roaringpenguin.com/pppoe/">http://www.roaringpenguin.com/pppoe/</a></i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pppoe/">pppoe</a>(8), <a href="/docs/linux/man/8-pppoe-stop/">pppoe-stop</a>(8), <a href="/docs/linux/man/8-pppoe-connect/">pppoe-connect</a>(8), <a href="/docs/linux/man/8-pppd/">pppd</a>(8), <a href="/docs/linux/man/5-pppoe-conf/">pppoe.conf</a>(5), <a href="/docs/linux/man/8-pppoe-setup/">pppoe-setup</a>(8), <a href="/docs/linux/man/8-pppoe-status/">pppoe-status</a>(8), <a href="/docs/linux/man/8-pppoe-sniff/">pppoe-sniff</a>(8), <a href="/docs/linux/man/8-pppoe-relay/">pppoe-relay</a>(8), <a href="/docs/linux/man/8-pppoe-server/">pppoe-server</a>(8) </p>
