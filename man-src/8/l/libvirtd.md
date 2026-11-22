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
<p><code>libvirtd</code> [<i></i><i>OPTION</i><i></i>]&#8230;</p>
<h2>Description</h2>
<p>The <code>libvirtd</code> program is the server side daemon component of the libvirt virtualization management system. </p>
<p> This daemon runs on host servers and performs required management tasks for virtualized guests. This includes activities such as starting, stopping and migrating guests between host servers, configuring and manipulating networking, and managing storage for use by guests. </p>
<p> The libvirt client libraries and utilities connect to this daemon to issue tasks and collect information about the configuration and resources of the host system and guests. </p>
<p> By default, the libvirtd daemon listens for requests on a local Unix domain socket. Using the <code>-l</code>|<code>&#8211;listen</code> command line option, the libvirtd daemon can be instructed to additionally listen on a TCP/IP socket. The TCP/IP socket to use is defined in the libvirtd configuration file. </p>
<p> Restarting libvirtd does not impact running guests. Guests continue to operate and will be picked up automatically if their XML configuration has been defined. Any guests whose XML configuration has not been defined will be lost from the configuration.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Display command line help usage then exit.</dd>
<dt><code>-d, &#8211;daemon</code></dt>
<dd>Run as a daemon &amp; write PID file.</dd>
<dt><code>-f, &#8211;config</code> <i></i><i>FILE</i><i></i></dt>
<dd>Use this configuration file, overriding the default value.</dd>
<dt><code>-l, &#8211;listen</code></dt>
<dd>Listen for TCP/IP connections.</dd>
<dt><code>-p, &#8211;pid-file</code> <i></i><i>FILE</i><i></i></dt>
<dd>Use this name for the PID file, overriding the default value.</dd>
<dt><code>-t, &#8211;timeout</code> <i></i><i>SECONDS</i><i></i></dt>
<dd>Exit after timeout period (in seconds) elapse with no client connections or registered resources. Be aware that resources such as autostart networks will result in never reaching the timeout, even when there are no client connections.</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd>Enable output of verbose messages.</dd>
<dt><code> &#8211;version</code></dt>
<dd>Display version information then exit.</dd></dl>
<h2>Signals</h2>
<p>On receipt of <code>SIGHUP</code> libvirtd will reload its configuration.</p>
<h2>Files</h2>
<h3>When run as <code>root</code>.</h3>
<dl>
<dt><i>/etc/libvirtd.conf</i></dt>
<dd>The default configuration file used by libvirtd, unless overridden on the command line using the <code>-f</code>|<code>&#8211;config</code> option.</dd>
<dt><i>/var/run/libvirt/libvirt-sock</i></dt>
<dd>
</dd><dt><i>/var/run/libvirt/libvirt-sock-ro</i></dt>
<dd>The sockets libvirtd will use.</dd>
<dt><i>/etc/pki/CA/cacert.pem</i></dt>
<dd>The TLS <code>Certificate Authority</code> certificate libvirtd will use.</dd>
<dt><i>/etc/pki/libvirt/servercert.pem</i></dt>
<dd>The TLS <code>Server</code> certificate libvirtd will use.</dd>
<dt><i>/etc/pki/libvirt/private/serverkey.pem</i></dt>
<dd>The TLS <code>Server</code> private key libvirtd will use.</dd>
<dt><i>/var/run/libvirtd.pid</i></dt>
<dd>The PID file to use, unless overridden by the <code>-p</code>|<code>&#8211;pid-file</code> option.</dd></dl>
<h3>When run as <code>non-root</code>.</h3>
<dl>
<dt><i>$XDG_CONFIG_HOME/libvirtd.conf</i></dt>
<dd>The default configuration file used by libvirtd, unless overridden on the command line using the <code>-f</code>|<code>&#8211;config</code> option.</dd>
<dt><i>$XDG_RUNTIME_DIR/libvirt/libvirt-sock</i></dt>
<dd>The socket libvirtd will use.</dd>
<dt><i>$HOME/.pki/libvirt/cacert.pem</i></dt>
<dd>The TLS <code>Certificate Authority</code> certificate libvirtd will use.</dd>
<dt><i>$HOME/.pki/libvirt/servercert.pem</i></dt>
<dd>The TLS <code>Server</code> certificate libvirtd will use.</dd>
<dt><i>$HOME/.pki/libvirt/serverkey.pem</i></dt>
<dd>The TLS <code>Server</code> private key libvirtd will use.</dd>
<dt><i>$XDG_RUNTIME_DIR/libvirt/libvirtd.pid</i></dt>
<dd>The PID file to use, unless overridden by the <code>-p</code>|<code>&#8211;pid-file</code> option.</dd>
<dt>If $XDG_CONFIG_HOME is not set in your environment, libvirtd will use <i>$HOME/.config</i></dt>
<dd>
</dd><dt>If $XDG_RUNTIME_DIR is not set in your environment, libvirtd will use <i>$HOME/.cache</i></dt>
<dd></dd></dl>
<h2>Examples</h2>
<p>To retrieve the version of libvirtd: </p>
<pre> # libvirtd --version
 libvirtd (libvirt) 0.8.2
 #</pre>
<p>To start libvirtd, instructing it to daemonize and create a PID file: </p>
<pre> # libvirtd -d
 # ls -la /var/run/libvirtd.pid
 -rw-r--r-- 1 root root 6 Jul 9 02:40 /var/run/libvirtd.pid
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
<p>Copyright (C) 2006-2012 Red Hat, Inc., and the authors listed in the libvirt AUTHORS file.</p>
<h2>License</h2>
<p>libvirtd is distributed under the terms of the GNU LGPL v2.1+. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1), <i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1), <i><a href="/docs/linux/man/1-virt-xml-validate/">virt-xml-validate</a></i>(1), <i><a href="/docs/linux/man/1-virt-top/">virt-top</a></i>(1), <i><a href="/docs/linux/man/1-virt-df/">virt-df</a></i>(1), &lt;<a rel="nofollow" href="http://www.libvirt.org/">http://www.libvirt.org/</a>&gt; </p>
