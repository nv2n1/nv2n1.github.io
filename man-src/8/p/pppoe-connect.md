---
title: "pppoe-connect(8)"
name: "pppoe-connect"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppoe-connect/"
description: "pppoe-connect – Shell script to manage a PPPoE link"
---

<p>pppoe-connect &#8211; Shell script to manage a PPPoE link</p>
<h2>Synopsis</h2>
<p><code>pppoe-connect </code>[<i>config_file</i>] <code>pppoe-connect </code><i>interface user</i> [<i>config_file</i>] </p>
<h2>Description</h2>
<p><code>pppoe-connect</code> is a shell script which manages a PPPoE connection using the Roaring Penguin user-space PPPoE client. If you omit <i>config_file</i>, the default file <code>/etc/sysconfig/network-scripts/ifcfg-ppp0</code> is used. If you supply <i>interface</i> and <i>user</i>, then they override the Ethernet interface and user-name settings in the configuration file. Note that normally, you should <i>not</i> invoke <code>pppoe-connect</code> directly. Instead, use <code>pppoe-start</code> to bring up the PPPoE connection. <code>pppoe-connect</code> first reads a configuration file. It then brings up a PPPoE connection. If the connection ever drops, a message is logged to syslog, and <code>pppoe-connect</code> re-establishes the connection. In addition, each time the connection is dropped or cannot be established, <code>pppoe-connect</code> executes the script <code>/etc/ppp/pppoe-lost</code> if it exists and is executable. The shell script <code>pppoe-stop</code> causes <code>pppoe-connect</code> to break out of its loop, bring the connection down, and exit. </p>
<h2>Technical Details</h2>
<p><code>pppoe-connect</code> uses the following shell variables from the configuration file: </p>
<dl>
<dt><code>ETH</code></p>
<dd>The Ethernet interface connected to the DSL modem (for example, eth0). </p>
<dt><code>USER</code></p>
<dd>The PPPoE user-id (for example, b1xxnxnx [at] sympatico.ca). </p>
<dt><code>PIDFILE</code></p>
<dd>A file in which to write the process-ID of the pppoe-connect process (for example, <code>/var/run/pppoe.pid</code>). Two additional files ($PIDFILE.pppd and $PIDFILE.pppoe) hold the process-ID&#8217;s of the <code>pppd</code> and <code>pppoe</code> processes, respectively. </p>
</dl>
<p> By using different configuration files with different PIDFILE settings, you can manage multiple PPPoE connections. Just specify the configuration file as an argument to <code>pppoe-start</code> and <code>pppoe-stop</code>.</p>
<h2>Author</h2>
<p><code>pppoe-connect</code> was written by David F. Skoll &lt;dfs [at] roaringpenguin.com&gt;. </p>
<p> The <code>pppoe</code> home page is <i><a rel="nofollow" href="http://www.roaringpenguin.com/pppoe/">http://www.roaringpenguin.com/pppoe/</a></i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pppoe/">pppoe</a>(8), <a href="/docs/linux/man/8-pppoe-start/">pppoe-start</a>(8), <a href="/docs/linux/man/8-pppoe-stop/">pppoe-stop</a>(8), <a href="/docs/linux/man/8-pppd/">pppd</a>(8), <a href="/docs/linux/man/5-pppoe-conf/">pppoe.conf</a>(5), <a href="/docs/linux/man/8-pppoe-setup/">pppoe-setup</a>(8), <a href="/docs/linux/man/8-pppoe-status/">pppoe-status</a>(8), <a href="/docs/linux/man/8-pppoe-sniff/">pppoe-sniff</a>(8), <a href="/docs/linux/man/8-pppoe-server/">pppoe-server</a>(8), <a href="/docs/linux/man/8-pppoe-relay/">pppoe-relay</a>(8) </p>
