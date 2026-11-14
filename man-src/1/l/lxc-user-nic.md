---
title: "lxc-user-nic(1)"
name: "lxc-user-nic"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-user-nic/"
description: "lxc-user-nic – Create and attach a nic to another network namespace."
---

<h2>NAME</h2>
<p> lxc-user-nic &#8211; Create and attach a nic to another network namespace.</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-user-nic</code> {<i>pid</i>} {<i>type</i>} {<i>bridge</i>} [<i>nicname</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-user-nic</code> is a setuid-root program with which unprivileged users may create network interfaces for use by a lxc container. </p>
<p> It will consult the configuration file <i>/etc/lxc/lxc-usernet</i> to determine the number of interfaces which the calling user is allowed to create, and which bridge he may attach them to. It tracks the number of interfaces each user has created using the file <i>/run/lxc/nics</i>. It ensures that the calling user is privileged over the network namespace to which the interface will be attached.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>pid</i></p>
<dd> The process id for the task to whose network namespace the interface should be attached.</p>
<dt><i>type</i></p>
<dd> The network interface type to attach. Currently only veth is supported. With this type, two interfaces representing each tunnel endpoint are created. One endpoint will be attached to the specified bridge, while the other will be passed into the container.</p>
<dt><i>bridge</i></p>
<dd> The bridge to which to attach the network interface, for instance <i>lxcbr0</i>.</p>
<dt><i>nicname</i></p>
<dd> The desired interface name in the container. This will be <i>eth0</i> if unspecified.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lxc/">lxc</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/5-lxc-usernet/">lxc-usernet</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt; </p>
<h2>Index</h2>
