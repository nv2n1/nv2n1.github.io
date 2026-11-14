---
title: "libvirtd(8)"
name: "libvirtd"
section: "8"
letter: "l"
url: "/docs/linux/man/8-libvirtd/"
description: "libvirtd – libvirtd management daemon"
---

<p>libvirtd &#8211; libvirtd management daemon</p>
<h2>Synopsis</h2>
<p><code>libvirtd</code> [<i></i><font SIZE="-1"><i>OPTION</i></font><i></i>]&#8230;</p>
<h2>Description</h2>
<p>The <code>libvirtd</code> program is the server side daemon component of the libvirt virtualization management system. </p>
<p> This daemon runs on host servers and performs required management tasks for virtualized guests. This includes activities such as starting, stopping and migrating guests between host servers, configuring and manipulating networking, and managing storage for use by guests. </p>
<p> The libvirt client libraries and utilities connect to this daemon to issue tasks and collect information about the configuration and resources of the host system and guests. </p>
<p> By default, the libvirtd daemon listens for requests on a local Unix domain socket. Using the <code>-l</code>|<code>&#8211;listen</code> command line option, the libvirtd daemon can be instructed to additionally listen on a <font SIZE="-1">TCP/IP</font> socket. The <font SIZE="-1">TCP/IP</font> socket to use is defined in the libvirtd configuration file. </p>
<p> Restarting libvirtd does not impact running guests. Guests continue to operate and will be picked up automatically if their <font SIZE="-1">XML</font> configuration has been defined. Any guests whose <font SIZE="-1">XML</font> configuration has not been defined will be lost from the configuration.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Display command line help usage then exit.</p>
<dt><code>-d, &#8211;daemon</code></p>
<dd>Run as a daemon &amp; write <font SIZE="-1">PID</font> file.</p>
<dt><code>-f, &#8211;config</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd>Use this configuration file, overriding the default value.</p>
<dt><code>-l, &#8211;listen</code></p>
<dd>Listen for <font SIZE="-1">TCP/IP</font> connections.</p>
<dt><code>-p, &#8211;pid-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd>Use this name for the <font SIZE="-1">PID</font> file, overriding the default value.</p>
<dt><code>-t, &#8211;timeout</code> <i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd>Exit after timeout period (in seconds) elapse with no client connections or registered resources. Be aware that resources such as autostart networks will result in never reaching the timeout, even when there are no client connections.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Enable output of verbose messages.</p>
<dt><code> &#8211;version</code></p>
<dd>Display version information then exit.</dl>
<h2>Signals</h2>
<p>On receipt of <font SIZE="-1"><code>SIGHUP</code></font> libvirtd will reload its configuration.</p>
<h2>Files</h2>
<h3>When run as <code>root</code>.</h3>
<dl>
<dt><i>/etc/libvirtd.conf</i></p>
<dd>The default configuration file used by libvirtd, unless overridden on the command line using the <code>-f</code>|<code>&#8211;config</code> option.</p>
<dt><i>/var/run/libvirt/libvirt-sock</i></p>
<dd>
<dt><i>/var/run/libvirt/libvirt-sock-ro</i></p>
<dd>The sockets libvirtd will use.</p>
<dt><i>/etc/pki/CA/cacert.pem</i></p>
<dd>The <font SIZE="-1">TLS </font><code>Certificate Authority</code> certificate libvirtd will use.</p>
<dt><i>/etc/pki/libvirt/servercert.pem</i></p>
<dd>The <font SIZE="-1">TLS </font><code>Server</code> certificate libvirtd will use.</p>
<dt><i>/etc/pki/libvirt/private/serverkey.pem</i></p>
<dd>The <font SIZE="-1">TLS </font><code>Server</code> private key libvirtd will use.</p>
<dt><i>/var/run/libvirtd.pid</i></p>
<dd>The <font SIZE="-1">PID</font> file to use, unless overridden by the <code>-p</code>|<code>&#8211;pid-file</code> option.</dl>
<h3>When run as <code>non-root</code>.</h3>
<dl>
<dt><i>$XDG_CONFIG_HOME/libvirtd.conf</i></p>
<dd>The default configuration file used by libvirtd, unless overridden on the command line using the <code>-f</code>|<code>&#8211;config</code> option.</p>
<dt><i>$XDG_RUNTIME_DIR/libvirt/libvirt-sock</i></p>
<dd>The socket libvirtd will use.</p>
<dt><i>$HOME/.pki/libvirt/cacert.pem</i></p>
<dd>The <font SIZE="-1">TLS </font><code>Certificate Authority</code> certificate libvirtd will use.</p>
<dt><i>$HOME/.pki/libvirt/servercert.pem</i></p>
<dd>The <font SIZE="-1">TLS </font><code>Server</code> certificate libvirtd will use.</p>
<dt><i>$HOME/.pki/libvirt/serverkey.pem</i></p>
<dd>The <font SIZE="-1">TLS </font><code>Server</code> private key libvirtd will use.</p>
<dt><i>$XDG_RUNTIME_DIR/libvirt/libvirtd.pid</i></p>
<dd>The <font SIZE="-1">PID</font> file to use, unless overridden by the <code>-p</code>|<code>&#8211;pid-file</code> option.</p>
<dt>If $XDG_CONFIG_HOME is not set in your environment, libvirtd will use <i>$HOME/.config</i></p>
<dd>
<dt>If $XDG_RUNTIME_DIR is not set in your environment, libvirtd will use <i>$HOME/.cache</i></p>
<dd></dl>
<h2>Examples</h2>
<p>To retrieve the version of libvirtd: </p>
<pre> # libvirtd --version
 libvirtd (libvirt) 0.8.2
 #</pre>
<p>To start libvirtd, instructing it to daemonize and create a <font SIZE="-1">PID</font> file: </p>
<pre> # libvirtd -d
 # ls -la /var/run/libvirtd.pid
 -rw-r--r-- 1 root root 6 Jul 9 02:40 /var/run/libvirtd.pid
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
<p>Copyright (C) 2006-2012 Red Hat, Inc., and the authors listed in the libvirt <font SIZE="-1">AUTHORS</font> file.</p>
<h2>License</h2>
<p>libvirtd is distributed under the terms of the <font SIZE="-1">GNU LGPL</font> v2.1+. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE</font></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1), <i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1), <i><a href="/docs/linux/man/1-virt-xml-validate/">virt-xml-validate</a></i>(1), <i><a href="/docs/linux/man/1-virt-top/">virt-top</a></i>(1), <i><a href="/docs/linux/man/1-virt-df/">virt-df</a></i>(1), &lt;<a rel="nofollow" href="http://www.libvirt.org/">http://www.libvirt.org/</a>&gt; </p>
