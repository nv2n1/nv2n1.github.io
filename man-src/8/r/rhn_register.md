---
title: "rhn_register(8)"
name: "rhn_register"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rhn_register/"
description: "rhn_register – Connect to Red Hat Satellite."
---

<p>rhn_register &#8211; Connect to Red Hat Satellite. </p>
<h2>Synopsis</h2>
<p>rhn_register [<i>options</i>] </p>
<h2>Description</h2>
<p><code>rhn_register</code> is a client program that registers your system with &quot;<code>Red Hat Satellite</code>&quot;. After registering, your system can receive software updates, install new software, and remotely manage your system. It can run both in graphical and text modes. </p>
<h2>Options</h2>
<dl>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Increase the debugging output. </p>
<dt><code>&#8211;proxy=PROXY</code></p>
<dd>Specify an http proxy to use. </p>
<dt><code>&#8211;proxyUser=PROXYUSER</code></p>
<dd>Specify a username to use for an authenticated proxy. This option must be used in conjunction with <code>proxyPassword</code>. </p>
<dt><code>&#8211;proxyPassword=PROXYPASSWORD</code></p>
<dd>Specify a password to use for an authenticated proxy. This option must be used in conjunction with <code>proxyUser</code>. </p>
<dt><code>&#8211;nox</code></p>
<dd>Run in text mode. </p>
<dt><code>&#8211;version</code></p>
<dd>Show the program&#8217;s version number and exit. </p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show a help message and exit. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sysconfig/rhn/systemid</i></p>
<dd>The digital server ID for this machine if the system has been registered onto &quot;<code>Red Hat Satellite</code>&quot;. This file does not exist otherwise. </p>
<dt><i>/etc/sysconfig/rhn/up2date</i></p>
<dd>The common configuration file used by Red Hat client programs. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rhn_check/">rhn_check</a></code>(8), <code><a href="/docs/linux/man/8-rhnreg_ks/">rhnreg_ks</a></code>(8), <code><a href="/docs/linux/man/8-rhnsd/">rhnsd</a></code>(8), <code><a href="/docs/linux/man/8-rhn-profile-sync/">rhn-profile-sync</a></code>(8), <code><a href="/docs/linux/man/8-rhnplugin/">rhnplugin</a></code>(8), <code><a href="/docs/linux/man/5-up2date/">up2date</a></code>(5). </p>
<h2>Authors</h2>
<p>See the AUTHORS file included with this software. </p>
<p> This manual page was written by James Bowes &lt;jbowes [at] redhat.com&gt;</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;. </p>
<h2>Copyright</h2>
<p>Copyright &#169; 1999-2011 Red Hat, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
