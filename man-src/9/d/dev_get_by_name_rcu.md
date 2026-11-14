---
title: "dev_get_by_name_rcu(9)"
name: "dev_get_by_name_rcu"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_get_by_name_rcu/"
description: "dev_get_by_name_rcu – find a device by its name"
---

<p>dev_get_by_name_rcu &#8211; find a device by its name</p>
<h2>Synopsis</h2>
<pre><code>struct net_device *dev_get_by_name_rcu(struct net *net, const char *name);</code></pre>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>the applicable net namespace</dl>
<p> <i>name</i></p>
<dl>
<dd>name to find</dl>
<h2>Description</h2>
<p>Find an interface by name. If the name is found a pointer to the device is returned. If the name is not found then <code>NULL</code> is returned. The reference counters are not incremented so the caller must be careful with locks. The caller must hold RCU lock.</p>
<h2>Copyright</h2>
