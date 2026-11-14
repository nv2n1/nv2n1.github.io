---
title: "ddupdate-config(8)"
name: "ddupdate-config"
section: "8"
letter: "d"
url: "/docs/linux/man/8-ddupdate-config/"
description: "dddupdate-config – ddupdate configuration file setup tool."
---

<p><code>dddupdate-config</code> &#8211; ddupdate configuration file setup tool.</p>
<h2>Synopsis</h2>
<p><code>dddupdate-config</code> </p>
<h2>Description</h2>
<p>A simple configuration script for <code>ddupdate</code>. Script provides a way to define address-plugin, service-plugin and hostname in an interactive way. The set of available plugins loaded depends on environment variables. See PLUGIN LOADING in <code><a href="/docs/linux/man/8-ddupdate/">ddupdate</a>(8)</code>. </p>
<h2>Bugs</h2>
<p>Does not support configuration of more advanced features like ipv6 and non-standard address-plugins beyond <i>web-default-ip</i> and <i>default-if</i>. </p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/8-ddupdate/">ddupdate</a>(8)</code></p>
<dd>
