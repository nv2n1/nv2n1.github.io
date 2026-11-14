---
title: "netplan-apply(8)"
name: "netplan-apply"
section: "8"
letter: "n"
url: "/docs/linux/man/8-netplan-apply/"
description: "netplan-apply – apply configuration from netplan YAML files to a running system"
---

<p>netplan-apply &#8211; apply configuration from netplan YAML files to a running system</p>
<h2>Synopsis</h2>
<p>netplan [-debug] apply -h | -help </p>
<p> netplan [-debug] apply</p>
<h2>Description</h2>
<p>netplan apply applies the current netplan configuration to a running system. </p>
<p> The process works as follows:</p>
<dl>
<dt>1.</p>
<dd>The backend configuration is generated from netplan YAML files.</p>
<dt>2.</p>
<dd>The appropriate backends (<a href="/docs/linux/man/8-systemd-networkd/">systemd-networkd</a>(8) or <a href="/docs/linux/man/8-networkmanager/">NetworkManager</a>(8)) are invoked to bring up configured interfaces.</p>
<dt>3.</p>
<dd>netplan apply iterates through interfaces that are still down, unbinding them from their drivers, and rebinding them. This gives <a href="/docs/linux/man/7-udev/">udev</a>(7) renaming rules the opportunity to run.</p>
<dt>4.</p>
<dd>If any devices have been rebound, the appropriate backends are re-invoked in case more matches can be done.</dl>
<p> For information about the generation step, see <a href="/docs/linux/man/8-netplan-generate/">netplan-generate</a>(8). For details of the configuration file format, see <a href="/docs/linux/man/5-netplan/">netplan</a>(5).</p>
<h2>Options</h2>
<dl>
<dt><code>-h, -help</code></p>
<dd>Print basic help.</p>
<dt><code>-debug</code></p>
<dd>Print debugging output during the process.</dl>
<h2>Known Issues</h2>
<p>netplan apply will not remove virtual devices such as bridges and bonds that have been created, even if they are no longer described in the netplan configuration. </p>
<p> This can be resolved by manually removing the virtual device (for example ip link delete dev bond0) and then running netplan apply, or by rebooting.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-netplan/">netplan</a>(5), <a href="/docs/linux/man/8-netplan-generate/">netplan-generate</a>(8), <a href="/docs/linux/man/8-netplan-try/">netplan-try</a>(8), <a href="/docs/linux/man/7-udev/">udev</a>(7), <a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a>(8), <a href="/docs/linux/man/8-networkmanager/">NetworkManager</a>(8)</p>
<h2>Authors</h2>
<p>Daniel Axtens (&lt;daniel.axtens [at] canonical.com&gt;).</p>
