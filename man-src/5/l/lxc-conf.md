---
title: "lxc-conf(5)"
name: "lxc-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lxc-conf/"
description: "lxc.conf – Configuration files for LXC."
---

<p>lxc.conf &#8211; Configuration files for LXC.</p>
<h2>Description</h2>
<p>LXC configuration is split in two parts. Container configuration and system configuration.</p>
<h3>Container Configuration</h3>
<p>The container configuration is held in the <i>config</i> stored in the container&#8217;s directory. </p>
<p> A basic configuration is generated at container creation time with the default&#8217;s recommended for the chosen template as well as extra default keys coming from the <i>default.conf</i> file. </p>
<p> That <i>default.conf</i> file is either located at <i>/etc/lxc/default.conf</i> or for unprivileged containers at <i>~/.config/lxc/default.conf</i>. </p>
<p> Details about the syntax of this file can be found in: <code><a href="/docs/linux/man/5-lxc-container-conf/">lxc.container.conf</a></code>(5)</p>
<h3>System Configuration</h3>
<p>The system configuration is located at <i>/etc/lxc/lxc.conf</i> or <i>~/.config/lxc/lxc.conf</i> for unprivileged containers. </p>
<p> This configuration file is used to set values such as default lookup paths and storage backend settings for LXC. </p>
<p> Details about the syntax of this file can be found in: <code><a href="/docs/linux/man/5-lxc-system-conf/">lxc.system.conf</a></code>(5)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lxc/">lxc</a></code>(1), <code><a href="/docs/linux/man/5-lxc-container-conf/">lxc.container.conf</a></code>(5), <code><a href="/docs/linux/man/5-lxc-system-conf/">lxc.system.conf</a></code>(5), <code><a href="/docs/linux/man/5-lxc-usernet/">lxc-usernet</a></code>(5)</p>
<h2>Author</h2>
<p>St&eacute;phane Graber &lt;stgraber [at] ubuntu.com&gt;</p>
