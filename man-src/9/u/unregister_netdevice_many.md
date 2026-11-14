---
title: "unregister_netdevice_many(9)"
name: "unregister_netdevice_many"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unregister_netdevice_many/"
description: "unregister_netdevice_many – unregister many devices"
---

<p>unregister_netdevice_many &#8211; unregister many devices</p>
<h2>Synopsis</h2>
<pre><code>void unregister_netdevice_many(struct list_head *head);</code></pre>
<h2>Arguments</h2>
<p><i>head</i></p>
<dl>
<dd>
<dd>list of devices</dl>
<h2>Note</h2>
<p>As most callers use a stack allocated list_head, we force a <code>list_del</code> to make sure stack wont be corrupted later.</p>
<h2>Copyright</h2>
