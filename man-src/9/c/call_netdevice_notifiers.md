---
title: "call_netdevice_notifiers(9)"
name: "call_netdevice_notifiers"
section: "9"
letter: "c"
url: "/docs/linux/man/9-call_netdevice_notifiers/"
description: "call_netdevice_notifiers – call all network notifier blocks"
---

<p>call_netdevice_notifiers &#8211; call all network notifier blocks</p>
<h2>Synopsis</h2>
<pre><code>int call_netdevice_notifiers(unsigned long val, struct net_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>val</i></p>
<dl>
<dd>
<dd>value passed unmodified to notifier function</dl>
<p> <i>dev</i></p>
<dl>
<dd>net_device pointer passed unmodified to notifier function</dl>
<h2>Description</h2>
<p>Call all network notifier blocks. Parameters and return value are as for <code>raw_notifier_call_chain</code>.</p>
<h2>Copyright</h2>
