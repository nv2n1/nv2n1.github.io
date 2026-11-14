---
title: "containerd-config(1)"
name: "containerd-config"
section: "1"
letter: "c"
url: "/docs/linux/man/1-containerd-config/"
description: "containerd-config – information on the containerd config"
---

<h2 class="name">NAME</h2>
<p> containerd-config &#8211; information on the containerd config</p>
<h2>SYNOPSIS</h2>
<p> containerd config [command] </p>
<h2>DESCRIPTION</h2>
<p> The <i>containerd config</i> command has one subcommand, named <i>default</i>, which will display on standard output the default containerd config for this version of the containerd daemon. </p>
<p> This output can be piped to a <code><a href="/docs/linux/man/5-containerd-config-toml/">containerd-config.toml</a>(5)</code> file and placed in <code>/etc/containerd</code> to be used as the configuration for containerd on daemon startup. The configuration can be placed in any filesystem location and used with the <code>&#8211;config</code> option to the containerd daemon as well. </p>
<p> See <code><a href="/docs/linux/man/5-containerd-config-toml/">containerd-config.toml</a>(5)</code> for more information on the containerd configuration options. </p>
<h2>OPTIONS</h2>
<p> <code>default</code> : This subcommand will output the TOML formatted containerd configuration to standard output </p>
<h2>BUGS</h2>
<p> Please file any specific issues that you encounter at </p>
<p> &lt;<a rel="nofollow" href="https://github.com/containerd/containerd">https://github.com/containerd/containerd</a>&gt;. </p>
<h2>AUTHOR</h2>
<p> Phil Estes &lt;estesp [at] gmail.com&gt; </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ctr/">ctr</a>(1), <a href="/docs/linux/man/1-containerd/">containerd</a>(1), <a href="/docs/linux/man/5-containerd-config-toml/">containerd-config.toml</a>(5) </p>
<h2>Index</h2>
