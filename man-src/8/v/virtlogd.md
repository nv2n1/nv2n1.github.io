---
title: "virtlogd(8)"
name: "virtlogd"
section: "8"
letter: "v"
url: "/docs/linux/man/8-virtlogd/"
description: "virtlogd – libvirt log management daemon"
---

<p>virtlogd &#8211; libvirt log management daemon</p>
<h2>Synopsis</h2>
<p><code>virtlogd</code> [<i></i><i>OPTION</i><i></i>]&#8230;</p>
<h2>Description</h2>
<p>The <code>virtlogd</code> program is a server side daemon component of the libvirt virtualization management system that is used to manage logs from virtual machine consoles. </p>
<p> This daemon is not used directly by libvirt client applications, rather it is called on their behalf by <code>libvirtd</code>. By maintaining the logs in a standalone daemon, the main libvirtd daemon can be restarted without risk of losing logs. The <code>virtlogd</code> daemon has the ability to re-<i>exec()</i> itself upon receiving SIGUSR1, to allow live upgrades without downtime. </p>
<p> The virtlogd daemon listens for requests on a local Unix domain socket.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Display command line help usage then exit.</dd>
<dt><code>-d, &#8211;daemon</code></dt>
<dd>Run as a daemon and write PID file.</dd>
<dt><code>-f, &#8211;config</code> <i></i><i>FILE</i><i></i></dt>
<dd>Use this configuration file, overriding the default value.</dd>
<dt><code>-t, &#8211;timeout</code> <i></i><i>SECONDS</i><i></i></dt>
<dd>Automatically shutdown after <i></i><i>SECONDS</i><i></i> have elapsed with no active console log.</dd>
<dt><code>-p, &#8211;pid-file</code> <i></i><i>FILE</i><i></i></dt>
<dd>Use this name for the PID file, overriding the default value.</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd>Enable output of verbose messages.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd>Display version information then exit.</dd></dl>
<h2>Signals</h2>
<p>On receipt of <code>SIGUSR1</code> virtlogd will re-<i>exec()</i> its binary, while maintaining all current logs and clients. This allows for live upgrades of the virtlogd service.</p>
<h2>Files</h2>
<h3>When run as <code>root</code>.</h3>
<dl>
<dt><i>/etc/virtlogd.conf</i></dt>
<dd>The default configuration file used by virtlogd, unless overridden on the command line using the <code>-f</code>|<code>&#8211;config</code> option.</dd>
<dt><i>/var/run/libvirt/virtlogd-sock</i></dt>
<dd>The sockets libvirtd will use.</dd>
<dt><i>/var/run/virtlogd.pid</i></dt>
<dd>The PID file to use, unless overridden by the <code>-p</code>|<code>&#8211;pid-file</code> option.</dd></dl>
<h3>When run as <code>non-root</code>.</h3>
<dl>
<dt><i>$XDG_CONFIG_HOME/virtlogd.conf</i></dt>
<dd>The default configuration file used by libvirtd, unless overridden on the command line using the <code>-f</code>|<code>&#8211;config</code> option.</dd>
<dt><i>$XDG_RUNTIME_DIR/libvirt/virtlogd-sock</i></dt>
<dd>The socket libvirtd will use.</dd>
<dt><i>$XDG_RUNTIME_DIR/libvirt/virtlogd.pid</i></dt>
<dd>The PID file to use, unless overridden by the <code>-p</code>|<code>&#8211;pid-file</code> option.</dd>
<dt>If $XDG_CONFIG_HOME is not set in your environment, libvirtd will use <i>$HOME/.config</i></dt>
<dd>
</dd><dt>If $XDG_RUNTIME_DIR is not set in your environment, libvirtd will use <i>$HOME/.cache</i></dt>
<dd></dd></dl>
<h2>Examples</h2>
<p>To retrieve the version of virtlogd: </p>
<pre> # virtlogd --version
 virtlogd (libvirt) 1.1.1
 #</pre>
<p>To start virtlogd, instructing it to daemonize and create a PID file: </p>
<pre> # virtlogd -d
 # ls -la /var/run/virtlogd.pid
 -rw-r--r-- 1 root root 6 Jul 9 02:40 /var/run/virtlogd.pid
 #</pre>
<h2>Bugs</h2>
<p>Please report all bugs you discover. This should be done via either:</p>
<dl>
<dt>a) the mailing list</dt>
<dd>&lt;<a rel="nofollow" href="http://libvirt.org/contact.html">http://libvirt.org/contact.html</a>&gt;</dd>
<dt>or,</dt>
<dd>
</dd><dt>b) the bug tracker</dt>
<dd>&lt;<a rel="nofollow" href="http://libvirt.org/bugs.html">http://libvirt.org/bugs.html</a>&gt;</dd>
<dt>Alternatively, you may report bugs to your software distributor / vendor.</dt>
<dd></dd></dl>
<h2>Authors</h2>
<p>Please refer to the AUTHORS file distributed with libvirt.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2006-2015 Red Hat, Inc., and the authors listed in the libvirt AUTHORS file.</p>
<h2>License</h2>
<p>virtlogd is distributed under the terms of the GNU LGPL v2.1+. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-libvirtd/">libvirtd</a></i>(8), &lt;<a rel="nofollow" href="http://www.libvirt.org/">http://www.libvirt.org/</a>&gt; </p>
