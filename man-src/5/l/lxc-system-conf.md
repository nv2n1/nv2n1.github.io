---
title: "lxc-system-conf(5)"
name: "lxc-system-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lxc-system-conf/"
description: "lxc.system.conf – LXC system configuration file"
---

<p>lxc.system.conf &#8211; LXC system configuration file</p>
<h2>Description</h2>
<p>The system configuration is located at <i>/etc/lxc/lxc.conf</i> or <i>~/.config/lxc/lxc.conf</i> for unprivileged containers. </p>
<p> This configuration file is used to set values such as default lookup paths and storage backend settings for LXC.</p>
<h3>Configuration Paths</h3>
<dl>
<dt><code>lxc.lxcpath</code></p>
<dd>The location in which all containers are stored.</p>
<dt><code>lxc.default_config</code></p>
<dd>The path to the default container configuration.</dl>
<h3>Control Groups</h3>
<dl>
<dt><code>lxc.cgroup.use</code></p>
<dd>Comma separated list of cgroup controllers to setup. Currently this configration will be ignored when LXC uses cgmanager to manage cgroups.</p>
<dt><code>lxc.cgroup.pattern</code></p>
<dd>Format string used to generate the cgroup path (e.g. lxc/%n).</dl>
<h3>Lvm</h3>
<dl>
<dt><code>lxc.bdev.lvm.vg</code></p>
<dd>Default LVM volume group name.</p>
<dt><code>lxc.bdev.lvm.thin_pool</code></p>
<dd>Default LVM thin pool name.</dl>
<h3>Zfs</h3>
<dl>
<dt><code>lxc.bdev.zfs.root</code></p>
<dd>Default ZFS root name.</dl>
<h2><code><a href="/docs/linux/man/1-lxc/">lxc</a></code>(1),</h2>
<p><code><a href="/docs/linux/man/5-lxc-container-conf/">lxc.container.conf</a></code>(5), <code><a href="/docs/linux/man/5-lxc-system-conf/">lxc.system.conf</a></code>(5), <code><a href="/docs/linux/man/5-lxc-usernet/">lxc-usernet</a></code>(5)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>Author</h2>
<p>St&eacute;phane Graber &lt;stgraber [at] ubuntu.com&gt;</p>
