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
<dt><code>lxc.lxcpath</code></dt>
<dd>The location in which all containers are stored.</dd>
<dt><code>lxc.default_config</code></dt>
<dd>The path to the default container configuration.</dd></dl>
<h3>Control Groups</h3>
<dl>
<dt><code>lxc.cgroup.use</code></dt>
<dd>Comma separated list of cgroup controllers to setup. Currently this configration will be ignored when LXC uses cgmanager to manage cgroups.</dd>
<dt><code>lxc.cgroup.pattern</code></dt>
<dd>Format string used to generate the cgroup path (e.g. lxc/%n).</dd></dl>
<h3>Lvm</h3>
<dl>
<dt><code>lxc.bdev.lvm.vg</code></dt>
<dd>Default LVM volume group name.</dd>
<dt><code>lxc.bdev.lvm.thin_pool</code></dt>
<dd>Default LVM thin pool name.</dd></dl>
<h3>Zfs</h3>
<dl>
<dt><code>lxc.bdev.zfs.root</code></dt>
<dd>Default ZFS root name.</dd></dl>
<h2><code>lxc</code>(1),</h2>
<p><code><a href="/docs/linux/man/5-lxc-container-conf/">lxc.container.conf</a></code>(5), <code><a href="/docs/linux/man/5-lxc-system-conf/">lxc.system.conf</a></code>(5), <code><a href="/docs/linux/man/5-lxc-usernet/">lxc-usernet</a></code>(5)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>Author</h2>
<p>St&eacute;phane Graber &lt;stgraber [at] ubuntu.com&gt;</p>
