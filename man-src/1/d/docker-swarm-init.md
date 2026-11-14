---
title: "docker-swarm-init(1)"
name: "docker-swarm-init"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-swarm-init/"
description: "docker-swarm-init – Initialize a swarm"
---

<h2 class="name">NAME</h2>
<p> docker-swarm-init &#8211; Initialize a swarm </p>
<h2>SYNOPSIS</h2>
<p> <code>docker swarm init [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> Initialize a swarm </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;advertise-addr</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Advertised address (format: [:port])</p>
<p> <code>&#8211;autolock</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Enable manager autolocking (requiring an unlock key to start a stopped manager)</p>
<p> <code>&#8211;availability</code>=&quot;active&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Availability of the node (&quot;active&quot;|&quot;pause&quot;|&quot;drain&quot;)</p>
<p> <code>&#8211;cert-expiry</code>=2160h0m0s <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Validity period for node certificates (ns|us|ms|s|m|h)</p>
<p> <code>&#8211;data-path-addr</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Address or interface to use for data path traffic (format: )</p>
<p> <code>&#8211;data-path-port</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Port number to use for data path traffic (1024 &#8211; 49151). If no value is set or is set to 0, the default port (4789) is used.</p>
<p> <code>&#8211;default-addr-pool</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>default address pool in CIDR format</p>
<p> <code>&#8211;default-addr-pool-mask-length</code>=24 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>default address pool subnet mask length</p>
<p> <code>&#8211;dispatcher-heartbeat</code>=5s <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Dispatcher heartbeat period (ns|us|ms|s|m|h)</p>
<p> <code>&#8211;external-ca</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Specifications of one or more certificate signing endpoints</p>
<p> <code>&#8211;force-new-cluster</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Force create a new cluster from current state</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for init</p>
<p> <code>&#8211;listen-addr</code>=0.0.0.0:2377 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Listen address (format: [:port])</p>
<p> <code>&#8211;max-snapshots</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Number of additional Raft snapshots to retain</p>
<p> <code>&#8211;snapshot-interval</code>=10000 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Number of log entries between Raft snapshots</p>
<p> <code>&#8211;task-history-limit</code>=5 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Task history retention limit</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-swarm/">docker-swarm</a>(1)</code> </p>
<h2>Index</h2>
