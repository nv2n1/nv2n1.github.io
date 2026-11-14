---
title: "netplugd(5)"
name: "netplugd"
section: "5"
letter: "n"
url: "/docs/linux/man/5-netplugd/"
description: "netplugd – network cable hotplug management daemon"
---

<p><code>netplugd</code> &#8211; network cable hotplug management daemon</p>
<h2>Synopsis</h2>
<p><code>netplugd</code> [-<code>FP</code> ] [-<code>c </code><i>config_file</i> ] [-<code>i </code><i>interface_pattern</i> ] [-<code>p </code><i>pid_file</i> ]</p>
<h2>Description</h2>
<p><code>netplugd</code> is a daemon that responds to network link events from the Linux kernel, such as a network interface losing or acquiring a carrier signal. </p>
<p> When an Ethernet-style network interface on a host is plugged into a powered-up switch, hub, or other host, the two use a carrier signal to establish that the link is alive. The Linux kernel makes this information available through its <a href="/docs/linux/man/7-netlink/">netlink</a>(7) interface. </p>
<p> The <code>netplugd</code> daemon listens for carrier detection and loss messages from the kernel&#8217;s <a href="/docs/linux/man/7-netlink/">netlink</a>(7) subsystem. When a carrier signal is detected on an interface, it runs a script to bring the interface up. When carrier is lost, <code>netplugd</code> runs a script to bring the interface down. <code>netplugd</code> does not define any policies for how to manage interfaces; it leaves that to a script, /etc/netplug.d/netplug which is described in Sx FILES below. </p>
<p> You tell <code>netplugd</code> which interfaces it should manage by giving it a list of shell-style glob patterns, which it matches against using the <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) function. For example, a pattern of eth[13] will tell <code>netplugd</code> to only manage eth1 and eth3 if those interfaces exist. If the interfaces are not known to the kernel at the time you start <code>,</code> perhaps because they are unplugged PCMCIA network interfaces or devices whose drivers have not yet been installed, <code>netplugd</code> will start to manage them as soon as they are plugged in or their drivers are available.</p>
<h2>Options</h2>
<dl>
<dt><code>-F</code></p>
<dd>Run in the foreground; do not detach and run as a daemon. Messages are logged to stdout or stderr instead of using the <a href="/docs/linux/man/3-syslog/">syslog</a>(3) mechanism. This option is useful mainly for debugging your configuration.</p>
<dt><code>-P</code></p>
<dd>Prevent autoprobing for interfaces. The <code>netplugd</code> daemon normally probes for all possible interface names that might match the patterns you tell it to manage. This is necessary in order to get network driver modules (the default with almost all Linux distributions) loaded and set up, so that they can provide link status notifications to the <code>netplugd</code> daemon. Autoprobing should always be safe, and doesn&#8217;t take long. Disable it with caution.</p>
<dt><code>-c </code><i>config_file</i></p>
<dd>Specify the name of a file from which to read patterns that describe the interfaces to manage. You can provide this option multiple times to read from more than one file. If you do not provide this option at all, <code>netplugd</code> will attempt to read from a default config file. If you do not want <code>netplugd</code> to try to read from any real config files, you can specify /dev/null as a config file.</p>
<dt><code>-i </code><i>interface_pattern</i></p>
<dd>Specify a pattern that will be used to match interface names that <code>netplugd</code> should manage. You can provide this option multiple times to specify multiple patterns.</p>
<dt><code>-p </code><i>pid_file</i></p>
<dd>Write the daemon&#8217;s process ID to the file <i>pid_file</i> If you tell <code>netplugd</code> to run in the foreground, this option is ignored.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/netplug/netplugd.conf </code></p>
<dd>Default config file to read, if none is specified on the command line. The config file format is one pattern per line, with white space, empty lines, and comments starting with a <code>#</code> character ignored. Patterns are standard shell-style glob patterns, e.g. &quot;eth[0-9]&quot;.</p>
<dt><code>/etc/netplug.d/netplug </code></p>
<dd>The &quot;policy&quot; program (typically a shell script) that <code>netplugd</code> uses to probe for interfaces, and to bring them up or down in response to network link events. This program is called with the name of the interface as its first argument, and one of the following options:</p>
<dl>
<dt><code>in</code></p>
<dd>A cable was plugged in, or carrier came up. The command should bring the interface up. The command is run asynchronously, and it should exit with status 0 on success.</p>
<dt><code>out</code></p>
<dd>A cable was plugged out, or carrier went down. The command should bring the interface down. The command is run asynchronously, and it should exit with status 0 on success.</p>
<dt><code>probe</code></p>
<dd>The command should load and initialise the driver for this interface, if possible, and bring the interface into the &quot;up&quot; state, so that it can generate <a href="/docs/linux/man/7-netlink/">netlink</a>(7) events. The command is run synchronously; it must exit with status code 0 if it succeeds, otherwise with a non-zero exit code or signal.</dl>
<dt><code>/etc/rc.d/init.d/netplugd </code></p>
<dd>The <a href="/docs/linux/man/8-init/">init</a>(8) script that starts, stops, and displays status of the <code>netplugd</code> daemon.</dl>
<h2>Author</h2>
<p><code>netplugd</code> was written by An Bryan O&#8217;Sullivan <i>&lt;bos [at] serpentine.com&gt;</i></p>
<h2>Copyright And License</h2>
<p>Copyright 2003 PathScale, Inc. Copyright 2003, 2004, 2005 Bryan O&#8217;Sullivan </p>
<p> <code>netplugd</code> is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the Free Software Foundation. You are forbidden from redistributing or modifying it under the terms of any other license, including other versions of the GNU General Public License. </p>
<p> <code>netplugd</code> is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-cardmgr/">cardmgr</a>(5), <a href="/docs/linux/man/8-hotplug/">hotplug</a>(8), <a href="/docs/linux/man/8-ip/">ip</a>(8), <a href="/docs/linux/man/7-netlink/">netlink</a>(7) </p>
