---
title: "dev_alloc_name(9)"
name: "dev_alloc_name"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_alloc_name/"
description: "dev_alloc_name – allocate a name for a device"
---

<p>dev_alloc_name &#8211; allocate a name for a device</p>
<h2>Synopsis</h2>
<pre><code>int dev_alloc_name(struct net_device *dev, const char *name);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device</dl>
<p> <i>name</i></p>
<dl>
<dd>name format string</dl>
<h2>Description</h2>
<p>Passed a format string &#8211; eg &#8220;lt<code>d</code>&#8221; it will try and find a suitable id. It scans list of devices to build up a free map, then chooses the first empty slot. The caller must hold the dev_base or rtnl lock while allocating the name and adding the device in order to avoid duplicates. Limited to bits_per_byte * page size devices (ie 32K on most platforms). Returns the number of the unit assigned or a negative errno code.</p>
<h2>Copyright</h2>
