---
title: "storaged-conf(5)"
name: "storaged-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-storaged-conf/"
description: "storaged.conf – The storaged configuration file"
---

<p>storaged.conf &#8211; The storaged configuration file</p>
<h2>Description</h2>
<p>The storaged project provides additional functionality via pluggable modules. These plugins can be inserted into the daemon either by D-Bus call <code>org.storaged.Storaged.Manager.EnableModules()</code> or by running the storaged daemon with <code>&#8211;force-load-modules</code> command line option. </p>
<p> It is also possible to configure the modules loading behavior via the configuration file placed at <i>/etc/storaged/storaged.conf</i>.</p>
<h2>Configuration File</h2>
<p>The default configuration file <code>storaged.conf</code> looks like this: </p>
<dl>
<dd>
<pre> [storaged]
 modules=*
 modules_load_preference=ondemand</pre>
</dl>
<p> <code>modules = &lt;string list&gt;</code></p>
<dl>
<dd>This variable controlls what modules should be loaded. It may contain either a comma-separated list of modules to load or a single asterisk which stands for all the modules.</dl>
<p> <code>modules_load_preference = ondemand|onstartup</code></p>
<dl>
<dd>This key tells storaged when to load the plugins: either at startup or on demand by D-Bus <code>org.storaged.Storaged.Manager.EnableModules()</code>.</dl>
<h2>Author</h2>
<p>&lt;phatina [at] redhat.com&gt;</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://github.com/storaged-project/storaged/issues">https://github.com/storaged-project/storaged/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-storaged/">storaged</a></code>(8), <code><a href="/docs/linux/man/1-storagectl/">storagectl</a></code>(1), <code><a href="/docs/linux/man/8-umount-storaged/">umount.storaged</a></code>(8) </p>
