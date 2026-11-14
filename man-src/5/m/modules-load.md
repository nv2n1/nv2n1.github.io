---
title: "modules-load(5)"
name: "modules-load"
section: "5"
letter: "m"
url: "/docs/linux/man/5-modules-load/"
description: "modules-load.d – Configure kernel modules to load at boot"
---

<p>modules-load.d &#8211; Configure kernel modules to load at boot</p>
<h2>Synopsis</h2>
<p>/etc/modules-load.d/*.conf </p>
<p> /run/modules-load.d/*.conf </p>
<p> /usr/lib/modules-load.d/*.conf</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/8-systemd-modules-load-service/">systemd-modules-load.service</a></code>(8) reads files from the above directories which contain kernel modules to load during boot in a static list. Each configuration file is named in the style of /etc/modules-load.d/<i>program</i>.conf. Note that it is usually a better idea to rely on the automatic module loading by PCI IDs, USB IDs, DMI IDs or similar triggers encoded in the kernel modules themselves instead of static configuration like this. In fact, most modern kernel modules are prepared for automatic loading already.</p>
<h2>Configuration Format</h2>
<p>The configuration files should simply contain a list of kernel module names to load, separated by newlines. Empty lines and lines whose first non-whitespace character is # or ; are ignored. </p>
<p> Each configuration file shall be named in the style of <i>program</i>.conf. Files in /etc/ override files with the same name in /usr/lib/ and /run/. Files in /run/ override files with the same name in /usr/lib/. Packages should install their configuration files in /usr/lib/, files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed from vendor packages. </p>
<p> If the administrator wants to disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in /etc/modules-load.d/ bearing the same filename.</p>
<h2>Example</h2>
<p><code>Example 1.&nbsp;<wbr>/etc/modules-load.d/virtio-net.conf example:</code> </p>
<dl>
<dd>
<pre># Load virtio-net.ko at boot
virtio-net</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-modules-load-service/">systemd-modules-load.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-delta/">systemd-delta</a></code>(1), <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8) </p>
