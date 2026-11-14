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
<p><code>virtlogd</code> [<i></i><font SIZE="-1"><i>OPTION</i></font><i></i>]&#8230;</p>
<h2>Description</h2>
<p>The <code>virtlogd</code> program is a server side daemon component of the libvirt virtualization management system that is used to manage logs from virtual machine consoles. </p>
<p> This daemon is not used directly by libvirt client applications, rather it is called on their behalf by <code>libvirtd</code>. By maintaining the logs in a standalone daemon, the main libvirtd daemon can be restarted without risk of losing logs. The <code>virtlogd</code> daemon has the ability to re-<i>exec()</i> itself upon receiving <font SIZE="-1">SIGUSR1,</font> to allow live upgrades without downtime. </p>
<p> The virtlogd daemon listens for requests on a local Unix domain socket.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Display command line help usage then exit.</p>
<dt><code>-d, &#8211;daemon</code></p>
<dd>Run as a daemon and write <font SIZE="-1">PID</font> file.</p>
<dt><code>-f, &#8211;config</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd>Use this configuration file, overriding the default value.</p>
<dt><code>-t, &#8211;timeout</code> <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd>Automatically shutdown after <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i> have elapsed with no active console log.</p>
<dt><code>-p, &#8211;pid-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd>Use this name for the <font SIZE="-1">PID</font> file, overriding the default value.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Enable output of verbose messages.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Display version information then exit.</dl>
<h2>Signals</h2>
<p>On receipt of <font SIZE="-1"><code>SIGUSR1</code></font> virtlogd will re-<i>exec()</i> its binary, while maintaining all current logs and clients. This allows for live upgrades of the virtlogd service.</p>
<h2>Files</h2>
<h3>When run as <code>root</code>.</h3>
<dl>
<dt><i>/etc/virtlogd.conf</i></p>
<dd>The default configuration file used by virtlogd, unless overridden on the command line using the <code>-f</code>|<code>&#8211;config</code> option.</p>
<dt><i>/var/run/libvirt/virtlogd-sock</i></p>
<dd>The sockets libvirtd will use.</p>
<dt><i>/var/run/virtlogd.pid</i></p>
<dd>The <font SIZE="-1">PID</font> file to use, unless overridden by the <code>-p</code>|<code>&#8211;pid-file</code> option.</dl>
<h3>When run as <code>non-root</code>.</h3>
<dl>
<dt><i>$XDG_CONFIG_HOME/virtlogd.conf</i></p>
<dd>The default configuration file used by libvirtd, unless overridden on the command line using the <code>-f</code>|<code>&#8211;config</code> option.</p>
<dt><i>$XDG_RUNTIME_DIR/libvirt/virtlogd-sock</i></p>
<dd>The socket libvirtd will use.</p>
<dt><i>$XDG_RUNTIME_DIR/libvirt/virtlogd.pid</i></p>
<dd>The <font SIZE="-1">PID</font> file to use, unless overridden by the <code>-p</code>|<code>&#8211;pid-file</code> option.</p>
<dt>If $XDG_CONFIG_HOME is not set in your environment, libvirtd will use <i>$HOME/.config</i></p>
<dd>
<dt>If $XDG_RUNTIME_DIR is not set in your environment, libvirtd will use <i>$HOME/.cache</i></p>
<dd></dl>
<h2>Examples</h2>
<p>To retrieve the version of virtlogd: </p>
<pre> # virtlogd --version
 virtlogd (libvirt) 1.1.1
 #</pre>
<p>To start virtlogd, instructing it to daemonize and create a <font SIZE="-1">PID</font> file: </p>
<pre> # virtlogd -d
 # ls -la /var/run/virtlogd.pid
 -rw-r--r-- 1 root root 6 Jul 9 02:40 /var/run/virtlogd.pid
 #</pre>
<h2>Bugs</h2>
<p>Please report all bugs you discover. This should be done via either:</p>
<dl>
<dt>a) the mailing list</p>
<dd>&lt;<a rel="nofollow" href="http://libvirt.org/contact.html">http://libvirt.org/contact.html</a>&gt;</p>
<dt>or,</p>
<dd>
<dt>b) the bug tracker</p>
<dd>&lt;<a rel="nofollow" href="http://libvirt.org/bugs.html">http://libvirt.org/bugs.html</a>&gt;</p>
<dt>Alternatively, you may report bugs to your software distributor / vendor.</p>
<dd></dl>
<h2>Authors</h2>
<p>Please refer to the <font SIZE="-1">AUTHORS</font> file distributed with libvirt.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2006-2015 Red Hat, Inc., and the authors listed in the libvirt <font SIZE="-1">AUTHORS</font> file.</p>
<h2>License</h2>
<p>virtlogd is distributed under the terms of the <font SIZE="-1">GNU LGPL</font> v2.1+. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE</font></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-libvirtd/">libvirtd</a></i>(8), &lt;<a rel="nofollow" href="http://www.libvirt.org/">http://www.libvirt.org/</a>&gt; </p>
