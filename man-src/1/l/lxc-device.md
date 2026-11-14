---
title: "lxc-device(1)"
name: "lxc-device"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-device/"
description: "lxc-device – manage devices of running containers"
---

<h2>NAME</h2>
<p> lxc-device &#8211; manage devices of running containers</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-device</code> [-h] [-n <i>name</i>] [add] [DEVICE] [NAME]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-device</code> manages devices in running container.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>[-h]</code></p>
<dd> The full command help message.</p>
<dt><code>-n</code></p>
<dd> The name of the target container.</p>
<dt><code>action</code></p>
<dd> What action to perform. Only &#8216;add&#8217; is supported at this point.</p>
<dt><code>DEVICE</code></p>
<dd> The device to add to the container. It can either be the path to a device under /dev or a network interface name.</p>
<dt><code>[NAME]</code></p>
<dd> Name for the device within the container.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>lxc-device -n p1 add /dev/video0</p>
<dd> Creates a /dev/video0 device in container p1 based on the matching device on the host.</p>
<dt>lxc-device -n p1 add eth0 eth1</p>
<dd> Moves eth0 from the host as eth1 in p1.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> St&eacute;phane Graber &lt;stgraber [at] ubuntu.com&gt; </p>
<h2>Index</h2>
