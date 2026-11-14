---
title: "docker-swarm-update(1)"
name: "docker-swarm-update"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-swarm-update/"
description: "docker-swarm-update – Update the swarm"
---

<h2 class="name">NAME</h2>
<p> docker-swarm-update &#8211; Update the swarm </p>
<h2>SYNOPSIS</h2>
<p> <code>docker swarm update [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> Update the swarm </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;autolock</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Change manager autolocking setting (true|false)</p>
<p> <code>&#8211;cert-expiry</code>=2160h0m0s <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Validity period for node certificates (ns|us|ms|s|m|h)</p>
<p> <code>&#8211;dispatcher-heartbeat</code>=5s <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Dispatcher heartbeat period (ns|us|ms|s|m|h)</p>
<p> <code>&#8211;external-ca</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Specifications of one or more certificate signing endpoints</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for update</p>
<p> <code>&#8211;max-snapshots</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Number of additional Raft snapshots to retain</p>
<p> <code>&#8211;snapshot-interval</code>=10000 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Number of log entries between Raft snapshots</p>
<p> <code>&#8211;task-history-limit</code>=5 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Task history retention limit</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-swarm/">docker-swarm</a>(1)</code> </p>
<h2>Index</h2>
