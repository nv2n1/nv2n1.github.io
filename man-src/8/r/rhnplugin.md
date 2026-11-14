---
title: "rhnplugin(8)"
name: "rhnplugin"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rhnplugin/"
description: "rhnplugin – Spacewalk/Red Hat Satellite support for yum(8)."
---

<p>rhnplugin &#8211; Spacewalk/Red Hat Satellite support for <code><a href="/docs/linux/man/8-yum/">yum</a></code>(8). </p>
<h2>Description</h2>
<p><code>rhnplugin</code> provides Spacewalk support for <code><a href="/docs/linux/man/8-yum/">yum</a></code>(8) via its plugin architecture. A system registered with Spacewalk will be able to update and install packages from Spacewalk. </p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sysconfig/rhn/up2date</i></p>
<dd>The common configuration file used by RHN client programs. </p>
<dt><i>/etc/yum/pluginconf.d/rhnplugin.conf</i></p>
<dd>A file containing plugin specific configuration options. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-yum/">yum</a></code>(8), <code><a href="/docs/linux/man/8-rhn_check/">rhn_check</a></code>(8), <code><a href="/docs/linux/man/8-rhn_register/">rhn_register</a></code>(8), <code><a href="/docs/linux/man/5-rhnplugin-conf/">rhnplugin.conf</a></code>(5), <code><a href="/docs/linux/man/5-up2date/">up2date</a></code>(5). </p>
<h2>Authors</h2>
<p>James Bowes &lt;jbowes [at] redhat.com&gt; and Peter Vetere &lt;pvetere [at] redhat.com&gt;.</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;. </p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006 Red Hat, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
