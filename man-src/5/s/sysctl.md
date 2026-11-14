---
title: "sysctl(5)"
name: "sysctl"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sysctl/"
description: "sysctl.d – Configure kernel parameters at boot"
---

<p>sysctl.d &#8211; Configure kernel parameters at boot</p>
<h2>Synopsis</h2>
<p>/etc/sysctl.d/*.conf </p>
<p> /run/sysctl.d/*.conf </p>
<p> /usr/lib/sysctl.d/*.conf</p>
<h2>Description</h2>
<p>At boot, <code><a href="/docs/linux/man/8-systemd-sysctl-service/">systemd-sysctl.service</a></code>(8) reads configuration files from the above directories to configure <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8) kernel parameters.</p>
<h2>Configuration Format</h2>
<p>The configuration files contain a list of variable assignments, separated by newlines. Empty lines and lines whose first non-whitespace character is &quot;#&quot; or &quot;;&quot; are ignored. </p>
<p> Each configuration file shall be named in the style of <i>program</i>.conf. Files in /etc/ override files with the same name in /usr/lib/ and /run/. Files in /run/ override files with the same name in /usr/lib/. Packages should install their configuration files in /usr/lib/. Files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same variable name, the entry in the file with the lexicographically latest name will be applied. It is recommended to prefix all filenames with a two-digit number and a dash, to simplify the ordering of the files. </p>
<p> Note that either &quot;/&quot; or &quot;.&quot; may be used as separators within sysctl variable names. If the first separator is a slash, remaining slashes and dots are left intact. If the first separator is a dot, dots and slashes are interchanged. &quot;kernel.domainname=foo&quot; and &quot;kernel/domainname=foo&quot; are equivalent and will cause &quot;foo&quot; to be written to /proc/sys/kernel/domainname. Either &quot;net.ipv4.conf.enp3s0/200.forwarding&quot; or &quot;net/ipv4/conf/enp3s0.200/forwarding&quot; may be used to refer to /proc/sys/net/ipv4/conf/enp3s0.200/forwarding. </p>
<p> If the administrator wants to disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in /etc/sysctl.d/ bearing the same filename. </p>
<p> The settings configured with sysctl.d files will be applied early on boot. The network interface-specific options will also be applied individually for each network interface as it shows up in the system. (More specifically, net.ipv4.conf.*, net.ipv6.conf.*, net.ipv4.neigh.* and net.ipv6.neigh.*). </p>
<p> Many sysctl parameters only become available when certain kernel modules are loaded. Modules are usually loaded on demand, e.g. when certain hardware is plugged in or network brought up. This means that <code><a href="/docs/linux/man/8-systemd-sysctl-service/">systemd-sysctl.service</a></code>(8) which runs during early boot will not configure such parameters if they become available after it has run. To set such parameters, it is recommended to add an <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) rule to set those parameters when they become available. Alternatively, a slightly simpler and less efficient option is to add the module to <code><a href="/docs/linux/man/5-modules-load-d/">modules-load.d</a></code>(5), causing it to be loaded statically before sysctl settings are applied (see example below).</p>
<h2>Examples</h2>
<p><code>Example 1. Set kernel YP domain name</code> /etc/sysctl.d/domain-name.conf:</p>
<dl>
<dd>
<pre>kernel.domainname=example.com</pre>
</dl>
<p> <code>Example 2. Disable packet filter on bridged packets (method one)</code> /etc/udev/rules.d/99-bridge.rules: </p>
<pre><code>ACTION==&quot;add&quot;, SUBSYSTEM==&quot;module&quot;, KERNEL==&quot;bridge&quot;, RUN+=&quot;/usr/lib/systemd/systemd-sysctl --prefix=/net/bridge&quot;</code></pre>
<p> /etc/sysctl.d/bridge.conf:</p>
<dl>
<dd>
<pre>net.bridge.bridge-nf-call-ip6tables = 0
net.bridge.bridge-nf-call-iptables = 0
net.bridge.bridge-nf-call-arptables = 0</pre>
</dl>
<p> <code>Example 3. Disable packet filter on bridged packets (method two)</code> /etc/modules-load.d/bridge.conf:</p>
<dl>
<dd>
<pre>bridge</pre>
</dl>
<p> /etc/sysctl.d/bridge.conf:</p>
<dl>
<dd>
<pre>net.bridge.bridge-nf-call-ip6tables = 0
net.bridge.bridge-nf-call-iptables = 0
net.bridge.bridge-nf-call-arptables = 0</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-sysctl-service/">systemd-sysctl.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-delta/">systemd-delta</a></code>(1), <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8), <code><a href="/docs/linux/man/5-sysctl-conf/">sysctl.conf</a></code>(5), <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8) </p>
