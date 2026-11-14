---
title: "dev_change_net_namespace(9)"
name: "dev_change_net_namespace"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_change_net_namespace/"
---

dev_change_net_namespace - move device to different nethost namespace

<h2>Synopsis</h2>

<pre><code>int dev_change_net_namespace(struct net_device *dev, struct net *net, const char *pat);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>net</i>
<dl><dd>network namespace</dl>
 

 <i>pat</i>
<dl><dd>If not NULL name pattern to try if the current device name is already taken in the destination network namespace.</dl>

<h2>Description</h2>

This function shuts down a device interface and moves it to a new network namespace. On success 0 is returned, on a failure a netagive errno code is returned. 

 Callers must hold the rtnl semaphore.

<h2>Copyright</h2>


