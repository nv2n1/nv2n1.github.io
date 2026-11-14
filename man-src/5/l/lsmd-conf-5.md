---
title: "lsmd-conf-5(5)"
name: "lsmd-conf-5"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lsmd-conf-5/"
description: "lsmd.conf – libStorageMgmt daemon lsmd configuration file."
---

<p>lsmd.conf &#8211; libStorageMgmt daemon lsmd configuration file. </p>
<h2>Description</h2>
<p>The libStorageMgmt plugin daemon (<code>lsmd</code>) will read the <code>lsmd.conf</code> file in the folder defined via <code>&#8211;confdir</code> (default is <code>/etc/lsm/</code>). The daemon reads the plugin configuration files from the sub-folder <code>pluginconf.d</code>. The plugin configuration file should be named as &lt;uri_scheme&gt;.conf, for example:<br />
&nbsp;<wbr>*&nbsp;<wbr>MegaRAID plugin&nbsp;<wbr>(<code>megaraid</code>://):&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>megaraid.conf</code> The <code>lsmd.conf</code> file controls the global settings for <code>lsmd</code> while the plugin configuration file for each plugin controls individual plugin behavior. Each option line of the configuration file should contain a trailing semicolon(<code>;</code>). </p>
<h2>lsmd.conf OPTIONS</h2>
<dl>
<dt><code>allow-plugin-root-privilege = true;</code></p>
<dd>Indicates whether the <code>lsmd</code> daemon should keep running as root mode and invoke plugin as root user when needed. </p>
<p> Without this option or with option set as <code>false</code> means that the daemon and the plugins will never run as root. </p>
<p> Only when all the following requirements are met, will <code>lsmd</code> run specified plugins as root user: </p>
<p>&nbsp;<wbr>1.&nbsp;<wbr>&quot;allow-plugin-root-privilege&nbsp;<wbr>=&nbsp;<wbr>true;&quot;&nbsp;<wbr>in lsmd.conf<br />
&nbsp;<wbr>2.&nbsp;<wbr>&quot;require-root-privilege&nbsp;<wbr>=&nbsp;<wbr>true;&quot;&nbsp;<wbr>in plugin config<br />
&nbsp;<wbr>3. API connection&nbsp;<wbr>(or lsmcli)&nbsp;<wbr>has root privileges </p>
</dl>
<h2>Plugin OPTIONS</h2>
<dl>
<dt><code>require-root-privilege = true;</code></p>
<dd>Indicates plugin requires root privilege. Without this line or set as <code>false</code>, the plugin will never be invoked as root user by <code>lsmd</code>. </p>
<p> Please check <code>lsmd.conf</code> option <code>allow-plugin-root-privilege</code> for detail. </p>
</dl>
<h2>See Also</h2>
<p><i>lsmd (1)</i> </p>
<h2>Bugs</h2>
<p>Please report bugs to &lt;libstoragemgmt-devel [at] lists.fedorahosted.org&gt;</p>
<h2>Author</h2>
<p>Gris Ge &lt;fge [at] redhat.com&gt;</p>
