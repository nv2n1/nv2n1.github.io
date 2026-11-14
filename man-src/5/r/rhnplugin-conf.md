---
title: "rhnplugin-conf(5)"
name: "rhnplugin-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rhnplugin-conf/"
description: "rhnplugin.conf – Configuration file for the rhnplugin(8) yum(8) plugin."
---

<p>rhnplugin.conf &#8211; Configuration file for the <code><a href="/docs/linux/man/8-rhnplugin/">rhnplugin</a></code>(8) <code><a href="/docs/linux/man/8-yum/">yum</a></code>(8) plugin. </p>
<h2>Description</h2>
<p><code>rhnplugin.conf</code> contains configuration options which are specific to <code><a href="/docs/linux/man/8-rhnplugin/">rhnplugin</a></code>(8). The configuration file is located at <i>/etc/yum/pluginconf.d/rhnplugin.conf</i>. </p>
<h2>Options</h2>
<dl>
<dt><code>enabled</code></p>
<dd>Either `0&#8242; or `1&#8242;. Determines whether the plugin will be used by yum or not. Default value is `1&#8242;. </p>
<dt><code>gpgcheck</code></p>
<dd>Either `0&#8242; or `1&#8242;. Determines whether gpg signature checking will be performed on packages coming from Spacewalk/Red Hat Satellite. Default value is `1&#8242;. If this option is not set, the value from <code><a href="/docs/linux/man/5-yum-conf/">yum.conf</a></code>(5) will be used. </p>
<dt><code>timeout</code></p>
<dd>The amount of time (in seconds) that you want to wait for a response before timing out. If this option is not set, the value from <code><a href="/docs/linux/man/5-yum-conf/">yum.conf</a></code>(5) will be used. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/yum/pluginconf.d/rhnplugin.conf</i></p>
<dd>The location of this configuration file. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rhnplugin/">rhnplugin</a></code>(8), <code><a href="/docs/linux/man/8-yum/">yum</a></code>(8), <code><a href="/docs/linux/man/5-up2date/">up2date</a></code>(5), <code><a href="/docs/linux/man/5-yum-conf/">yum.conf</a></code>(5). </p>
<h2>Authors</h2>
<p>James Bowes &lt;jbowes [at] redhat.com&gt; and Peter Vetere &lt;pvetere [at] redhat.com&gt;.</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;. </p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006 Red Hat, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
