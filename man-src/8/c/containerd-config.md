---
title: "containerd-config(8)"
name: "containerd-config"
section: "8"
letter: "c"
url: "/docs/linux/man/8-containerd-config/"
description: "containerd-config – information on the containerd config"
---

<p>containerd-config &#8211; information on the containerd config</p>
<h2>Synopsis</h2>
<p>containerd config [command] </p>
<h2>Description</h2>
<p>The <i>containerd config</i> command has one subcommand, named <i>default</i>, which will display on standard output the default containerd config for this version of the containerd daemon. This output can be piped to a <code><a href="/docs/linux/man/5-containerd-config-toml/">containerd-config.toml</a>(5)</code> file and placed in <code>/etc/containerd</code> to be used as the configuration for containerd on daemon startup. The configuration can be placed in any filesystem location and used with the <code>&#8211;config</code> option to the containerd daemon as well. See <code><a href="/docs/linux/man/5-containerd-config-toml/">containerd-config.toml</a>(5)</code> for more information on the containerd configuration options. </p>
<h2>Options</h2>
<dl>
<dt><code>default</code></p>
<dd>This subcommand will output the TOML formatted containerd configuration to standard output </p>
</dl>
<h2>Bugs</h2>
<p>Please file any specific issues that you encounter at <a rel="nofollow" href="https://github.com/containerd/containerd.">https://github.com/containerd/containerd.</a> </p>
<h2>Author</h2>
<p>Phil Estes estesp [at] gmail.com &lt;mailto:estesp [at] gmail.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ctr/">ctr</a>(8), <a href="/docs/linux/man/8-containerd/">containerd</a>(8), <a href="/docs/linux/man/5-containerd-config-toml/">containerd-config.toml</a>(5) </p>
