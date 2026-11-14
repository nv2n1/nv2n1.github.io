---
title: "rio_setup_device(9)"
name: "rio_setup_device"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_setup_device/"
description: "rio_setup_device – Allocates and sets up a RIO device"
---

<p>rio_setup_device &#8211; Allocates and sets up a RIO device</p>
<h2>Synopsis</h2>
<pre><code>struct rio_dev *rio_setup_device(struct rio_net *net, struct rio_mport *port, u16 destid, u8 hopcount, int do_enum);</code></pre>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>RIO network</dl>
<p> <i>port</i></p>
<dl>
<dd>Master port to send transactions</dl>
<p> <i>destid</i></p>
<dl>
<dd>Current destination ID</dl>
<p> <i>hopcount</i></p>
<dl>
<dd>Current hopcount</dl>
<p> <i>do_enum</i></p>
<dl>
<dd>Enumeration/Discovery mode flag</dl>
<h2>Description</h2>
<p>Allocates a RIO device and configures fields based on configuration space contents. If device has a destination ID register, a destination ID is either assigned in enumeration mode or read from configuration space in discovery mode. If the device has switch capabilities, then a switch is allocated and configured appropriately. Returns a pointer to a RIO device on success or NULL on failure.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
