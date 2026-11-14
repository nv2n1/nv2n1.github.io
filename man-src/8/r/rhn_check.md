---
title: "rhn_check(8)"
name: "rhn_check"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rhn_check/"
description: "rhn_check – Check for and execute queued actions on RHN."
---

<p>rhn_check &#8211; Check for and execute queued actions on RHN. </p>
<h2>Synopsis</h2>
<p>rhn_check [<i>options</i>] </p>
<h2>Description</h2>
<p><code>rhn_check</code> is a client program that connects to &quot;<code>Red Hat Satellite</code>&quot; and receives queued actions for this particular system. After receiving the actions, <code>rhn_check</code> will then process them, and return the results to Red Hat Satellite. </p>
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
<dd>The common configuration file used by RHN client programs. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rhn_register/">rhn_register</a></code>(8), <code><a href="/docs/linux/man/8-rhnreg_ks/">rhnreg_ks</a></code>(8), <code><a href="/docs/linux/man/8-rhnsd/">rhnsd</a></code>(8), <code><a href="/docs/linux/man/8-rhn-profile-sync/">rhn-profile-sync</a></code>(8), <code><a href="/docs/linux/man/8-rhnplugin/">rhnplugin</a></code>(8), <code><a href="/docs/linux/man/5-up2date/">up2date</a></code>(5). </p>
<h2>Authors</h2>
<p>See the AUTHORS file included with this software. </p>
<p> This manual page was written by James Bowes &lt;jbowes [at] redhat.com&gt;</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;. </p>
<h2>Copyright</h2>
<p>Copyright &#169; 1999-2010 Red Hat, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
