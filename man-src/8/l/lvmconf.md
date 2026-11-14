---
title: "lvmconf(8)"
name: "lvmconf"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvmconf/"
description: "lvmconf — LVM configuration modifier"
---

<p>lvmconf &#8212; LVM configuration modifier</p>
<h2>Synopsis</h2>
<p><code>lvmconf</code> [<code>&#8211;disable-cluster</code>] [<code>&#8211;enable-cluster</code>] [<code>&#8211;enable-halvm</code>] [<code>&#8211;disable-halvm</code>] [<code>&#8211;file</code> &lt;<i>configfile</i>&gt;] [<code>&#8211;lockinglib</code> &lt;<i>lib</i>&gt;] [<code>&#8211;lockinglibdir</code> &lt;<i>dir</i>&gt;] [<code>&#8211;services</code>] [<code>&#8211;mirrorservice</code>] [<code>&#8211;startstopservices</code>] </p>
<h2>Description</h2>
<p>lvmconf is a script that modifies the locking configuration in an lvm configuration file. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5). In addition to that, it can also set Systemd or SysV services according to changes in the lvm configuration if needed. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;disable-cluster</code></p>
<dd>Set <code>locking_type</code> to the default non-clustered type. Also reset lvmetad use to its default.</p>
<dt><code>&#8211;enable-cluster</code></p>
<dd>Set <code>locking_type</code> to the default clustered type on this system. Also disable lvmetad use as it is not yet supported in clustered environment.</p>
<dt><code>&#8211;disable-halvm</code></p>
<dd>Set <code>locking_type</code> to the default non-clustered type. Also reset lvmetad use to its default.</p>
<dt><code>&#8211;enable-halvm</code></p>
<dd>Set <code>locking_type</code> suitable for HA LVM use. Also disable lvmetad use as it is not yet supported in HA LVM environment.</p>
<dt><code>&#8211;file</code> &lt;<i>configfile</i>&gt;</p>
<dd>Apply the changes to <i>configfile</i> instead of the default <i>/etc/lvm/lvm.conf</i>.</p>
<dt><code>&#8211;lockinglib</code> &lt;<i>lib</i>&gt;</p>
<dd>Set external <code>locking_library</code> locking library to load if an external locking type is used.</p>
<dt><code>&#8211;lockinglibdir</code> &lt;<i>dir</i>&gt;</p>
<dd>
<dt><code>&#8211;services</code></p>
<dd>In addition to setting the lvm configuration, also enable or disable related Systemd or SysV clvmd and lvmetad services. This script does not configure services provided by cluster resource agents.</p>
<dt><code>&#8211;mirrorservice</code></p>
<dd>Also enable or disable optional cmirrord service when handling services (applicable only with &#8211;services).</p>
<dt><code>&#8211;startstopservices</code></p>
<dd>In addition to enabling or disabling related services, start or stop them immediately (applicable only with &#8211;services).</dl>
<h2>Files</h2>
<p><i>/etc/lvm/lvm.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8), <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) </p>
