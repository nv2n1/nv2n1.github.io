---
title: "systemd-sysctl-service(8)"
name: "systemd-sysctl-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-sysctl-service/"
description: "systemd-sysctl.service, systemd-sysctl – Configure kernel parameters at boot"
---

<p>systemd-sysctl.service, systemd-sysctl &#8211; Configure kernel parameters at boot</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/lib/systemd/systemd-sysctl</code> [OPTIONS&#8230;] [<i>CONFIGFILE</i>&#8230;]</dl>
<dd>systemd-sysctl.service</p>
<h2>Description</h2>
<p>systemd-sysctl.service is an early boot service that configures <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8) kernel parameters by invoking <code>/lib/systemd/systemd-sysctl</code>. </p>
<p> When invoked with no arguments, <code>/lib/systemd/systemd-sysctl</code> applies all directives from configuration files listed in <code><a href="/docs/linux/man/5-sysctl-d/">sysctl.d</a></code>(5). If one or more filenames are passed on the command line, only the directives in these files are applied. </p>
<p> In addition, <code>&#8211;prefix=</code> option may be used to limit which sysctl settings are applied. </p>
<p> See <code><a href="/docs/linux/man/5-sysctl-d/">sysctl.d</a></code>(5) for information about the configuration of sysctl settings. After sysctl configuration is changed on disk, it must be written to the files in /proc/sys/ before it takes effect. It is possible to update specific settings, or simply to reload all configuration, see Examples below.</p>
<h2>Options</h2>
<p><code>&#8211;prefix=</code></p>
<dl>
<dd>Only apply rules with the specified prefix.</dl>
<p> <code>&#8211;cat-config</code></p>
<dl>
<dd>Copy the contents of config files to standard output. Before each file, the filename is printed as a comment.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dd>Do not pipe output into a pager.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>Examples</h2>
<p><code>Example 1. Reset all sysctl settings</code> </p>
<dl>
<dd>
<pre>systemctl restart systemd-sysctl</pre>
</dl>
<p> <code>Example 2. View coredump handler configuration</code> </p>
<dl>
<dd>
<pre># sysctl kernel.core_pattern
kernel.core_pattern = |/libexec/abrt-hook-ccpp %s %c %p %u %g %t %P %I</pre>
</dl>
<p> <code>Example 3. Update coredump handler configuration</code> </p>
<dl>
<dd>
<pre># /lib/systemd/systemd-sysctl --prefix kernel.core_pattern</pre>
</dl>
<p> This searches all the directories listed in <code><a href="/docs/linux/man/5-sysctl-d/">sysctl.d</a></code>(5) for configuration files and writes /proc/sys/kernel/core_pattern. </p>
<p> <code>Example 4. Update coredump handler configuration according to a specific file</code> </p>
<dl>
<dd>
<pre># /lib/systemd/systemd-sysctl 50-coredump.conf</pre>
</dl>
<p> This applies all the settings found in 50-coredump.conf. Either /etc/sysctl.d/50-coredump.conf, or /run/sysctl.d/50-coredump.conf, or /usr/lib/sysctl.d/50-coredump.conf will be used, in the order of preference. </p>
<p> See <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8) for various ways to directly apply sysctl settings.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-sysctl-d/">sysctl.d</a></code>(5), <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8), </p>
