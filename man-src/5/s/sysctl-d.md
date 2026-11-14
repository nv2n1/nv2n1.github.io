---
title: "sysctl-d(5)"
name: "sysctl-d"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sysctl-d/"
description: "sysctl.d – Configure kernel parameters at boot"
---

<p>sysctl.d &#8211; Configure kernel parameters at boot</p>
<h2>Synopsis</h2>
<p>/etc/sysctl.d/*.conf </p>
<p> /run/sysctl.d/*.conf </p>
<p> /usr/lib/sysctl.d/*.conf </p>
<pre>key.name.under.proc.sys = some value
key/name/under/proc/sys = some value
key/middle.part.with.dots/foo = 123
key.middle/part/with/dots.foo = 123
-key.that.will.not.fail = value
key.pattern.*.with.glob = whatever
-key.pattern.excluded.with.glob
key.pattern.overridden.with.glob = custom</pre>
<h2>Description</h2>
<p>At boot, <code><a href="/docs/linux/man/8-systemd-sysctl-service/">systemd-sysctl.service</a></code>(8) reads configuration files from the above directories to configure <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8) kernel parameters.</p>
<h2>Configuration Format</h2>
<p>The configuration files contain a list of variable assignments, separated by newlines. Empty lines and lines whose first non-whitespace character is &quot;#&quot; or &quot;;&quot; are ignored. </p>
<p> Note that either &quot;/&quot; or &quot;.&quot; may be used as separators within sysctl variable names. If the first separator is a slash, remaining slashes and dots are left intact. If the first separator is a dot, dots and slashes are interchanged. &quot;kernel.domainname=foo&quot; and &quot;kernel/domainname=foo&quot; are equivalent and will cause &quot;foo&quot; to be written to /proc/sys/kernel/domainname. Either &quot;net.ipv4.conf.enp3s0/200.forwarding&quot; or &quot;net/ipv4/conf/enp3s0.200/forwarding&quot; may be used to refer to /proc/sys/net/ipv4/conf/enp3s0.200/forwarding. A glob <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7) pattern may be used to write the same value to all matching keys. Keys for which an explicit pattern exists will be excluded from any glob matching. In addition, a key may be explicitly excluded from being set by any matching glob patterns by specifying the key name prefixed with a &quot;-&quot; character and not followed by &quot;=&quot;, see SYNOPSIS. </p>
<p> Any access permission errors and attempts to write variables not present on the local system are logged at debug level and do not cause the service to fail. Other types of errors when setting variables are logged with higher priority and cause the service to return failure at the end (after processing other variables). As an exception, if a variable assignment is prefixed with a single &quot;-&quot; character, failure to set the variable for any reason will be logged at debug level and will not cause the service to fail. </p>
<p> The settings configured with sysctl.d files will be applied early on boot. The network interface-specific options will also be applied individually for each network interface as it shows up in the system. (More specifically, net.ipv4.conf.*, net.ipv6.conf.*, net.ipv4.neigh.* and net.ipv6.neigh.*). </p>
<p> Many sysctl parameters only become available when certain kernel modules are loaded. Modules are usually loaded on demand, e.g. when certain hardware is plugged in or network brought up. This means that <code><a href="/docs/linux/man/8-systemd-sysctl-service/">systemd-sysctl.service</a></code>(8) which runs during early boot will not configure such parameters if they become available after it has run. To set such parameters, it is recommended to add an <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) rule to set those parameters when they become available. Alternatively, a slightly simpler and less efficient option is to add the module to <code><a href="/docs/linux/man/5-modules-load-d/">modules-load.d</a></code>(5), causing it to be loaded statically before sysctl settings are applied (see example below).</p>
<h2>Configuration Directories And Precedence</h2>
<p>Configuration files are read from directories in /etc/, /run/, /usr/local/lib/, and /lib/, in order of precedence, as listed in the SYNOPSIS section above. Files must have the &quot;.conf&quot; extension. Files in /etc/ override files with the same name in /run/, /usr/local/lib/, and /lib/. Files in /run/ override files with the same name under /usr/. </p>
<p> All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Thus, the configuration in a certain file may either be replaced completely (by placing a file with the same name in a directory with higher priority), or individual settings might be changed (by specifying additional settings in a file with a different name that is ordered later). </p>
<p> Packages should install their configuration files in /usr/lib/ (distribution packages) or /usr/local/lib/ (local installs). Files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. It is recommended to prefix all filenames with a two-digit number and a dash, to simplify the ordering of the files. </p>
<p> If the administrator wants to disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in the configuration directory in /etc/, with the same filename as the vendor configuration file. If the vendor configuration file is included in the initrd image, the image has to be regenerated.</p>
<h2>Examples</h2>
<p><code>Example 1. Set kernel YP domain name</code> /etc/sysctl.d/domain-name.conf:</p>
<dl>
<dd>
<pre>kernel.domainname=example.com</pre>
</dl>
<p> <code>Example 2. Apply settings available only when a certain module is loaded (method one)</code> /etc/udev/rules.d/99-bridge.rules: </p>
<pre><code>ACTION==&quot;add&quot;, SUBSYSTEM==&quot;module&quot;, KERNEL==&quot;br_netfilter&quot;, \
RUN+=&quot;/lib/systemd/systemd-sysctl --prefix=/net/bridge&quot;</code></pre>
<p> /etc/sysctl.d/bridge.conf:</p>
<dl>
<dd>
<pre>net.bridge.bridge-nf-call-ip6tables = 0
net.bridge.bridge-nf-call-iptables = 0
net.bridge.bridge-nf-call-arptables = 0</pre>
</dl>
<p> This method applies settings when the module is loaded. Please note that, unless the br_netfilter module is loaded, bridged packets will not be filtered by Netfilter (starting with kernel 3.18), so simply not loading the module is sufficient to avoid filtering. <code>Example 3. Apply settings available only when a certain module is loaded (method two)</code> /etc/modules-load.d/bridge.conf:</p>
<dl>
<dd>
<pre>br_netfilter</pre>
</dl>
<p> /etc/sysctl.d/bridge.conf:</p>
<dl>
<dd>
<pre>net.bridge.bridge-nf-call-ip6tables = 0
net.bridge.bridge-nf-call-iptables = 0
net.bridge.bridge-nf-call-arptables = 0</pre>
</dl>
<p> This method forces the module to be always loaded. Please note that, unless the br_netfilter module is loaded, bridged packets will not be filtered with Netfilter (starting with kernel 3.18), so simply not loading the module is sufficient to avoid filtering. <code>Example 4. Set network routing properties for all interfaces</code> /etc/sysctl.d/20-rp_filter.conf:</p>
<dl>
<dd>
<pre>net.ipv4.conf.default.rp_filter = 2
net.ipv4.conf.*.rp_filter = 2
-net.ipv4.conf.all.rp_filter
net.ipv4.conf.hub0.rp_filter = 1</pre>
</dl>
<p> The <code>rp_filter</code> key will be set to &quot;2&quot; for all interfaces, except &quot;hub0&quot;. We set net.ipv4.conf.default.rp_filter first, so any interfaces which are added <i>later</i> will get this value (this also covers any interfaces detected while we&#8217;re running). The glob matches any interfaces which were detected <i>earlier</i>. The glob will also match net.ipv4.conf.all.rp_filter, which we don&#8217;t want to set at all, so it is explicitly excluded. And &quot;hub0&quot; is excluded from the glob because it has an explicit setting.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-sysctl-service/">systemd-sysctl.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-delta/">systemd-delta</a></code>(1), <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8), <code><a href="/docs/linux/man/5-sysctl-conf/">sysctl.conf</a></code>(5), <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8) </p>
