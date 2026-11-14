---
title: "udisks2-conf(5)"
name: "udisks2-conf"
section: "5"
letter: "u"
url: "/docs/linux/man/5-udisks2-conf/"
description: "udisks2.conf – The udisks2 configuration file"
---

<p>udisks2.conf &#8211; The udisks2 configuration file</p>
<h2>Description</h2>
<p>The udisks project provides additional functionality via pluggable modules. These plugins can be inserted into the daemon either by D-Bus call <code>org.freedesktop.UDisks2.Manager.EnableModules()</code> or by running the udisks daemon with <code>&#8211;force-load-modules</code> command line option. </p>
<p> It is also possible to configure the modules loading behavior via the configuration file placed at <i>/etc/udisks2/udisks2.conf</i>.</p>
<h2>Configuration File</h2>
<p>The default configuration file <code>udisks2.conf</code> looks like this: </p>
<dl>
<dd>
<pre> [udisks2]
 modules=*
 modules_load_preference=ondemand
 [defaults]
 encryption=luks1</pre>
</dl>
<p> <code>modules = &lt;string list&gt;</code></p>
<dl>
<dd>This variable controls what modules should be loaded. It may contain either a comma-separated list of modules to load or a single asterisk which stands for all the modules.</dl>
<p> <code>modules_load_preference = ondemand|onstartup</code></p>
<dl>
<dd>This key tells udisksd when to load the plugins: either at startup or on demand by D-Bus <code>org.freedesktop.UDisks2.Manager.EnableModules()</code>.</dl>
<p> <code>encryption = luks1|luks2</code></p>
<dl>
<dd>This variable controls which encryption technology will be used by default when creating an encrypted filesystem.</dl>
<h2>Author</h2>
<p>&lt;phatina [at] redhat.com&gt;</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://github.com/storaged-project/udisks/issues">https://github.com/storaged-project/udisks/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-udisks/">udisks</a></code>(8), <code><a href="/docs/linux/man/1-udisksctl/">udisksctl</a></code>(1), <code><a href="/docs/linux/man/8-umount-udisks2/">umount.udisks2</a></code>(8) </p>
