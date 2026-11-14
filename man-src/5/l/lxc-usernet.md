---
title: "lxc-usernet(5)"
name: "lxc-usernet"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lxc-usernet/"
description: "lxc-usernet – unprivileged user network administration file."
---

<p>lxc-usernet &#8211; unprivileged user network administration file.</p>
<h2>Description</h2>
<p><i>/etc/lxc/lxc-usernet</i> controls the limits which the program <code>lxc-user-nic</code> places on network interfaces which an unprivileged user may create.</p>
<h3>Configuration</h3>
<p>This file consists of multiple entries, one per line, of the form: </p>
<p> <code>user</code> <code>type</code> <code>bridge</code> <code>number</code> </p>
<p> Where</p>
<dl>
<dt><code>user</code></p>
<dd>is the username to whom this entry applies.</p>
<dt><code>type</code></p>
<dd>is the type of network interface being allowed. Only veth is currently supported.</p>
<dt><code>bridge</code></p>
<dd>is the bridge to which the network interfaces may be attached, for instance <i>lxcbr0</i>.</p>
<dt><code>number</code></p>
<dd>is the number of network interfaces of the given type which the given user may attach to the given bridge, for instance <i>2</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lxc/">lxc</a></code>(1), <code><a href="/docs/linux/man/1-lxc-user-nic/">lxc-user-nic</a></code>(1)</p>
<h2>Author</h2>
<p>Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt;</p>
