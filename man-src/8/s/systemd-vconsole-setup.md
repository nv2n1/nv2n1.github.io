---
title: "systemd-vconsole-setup(8)"
name: "systemd-vconsole-setup"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-vconsole-setup/"
description: "systemd-vconsole-setup.service, systemd-vconsole-setup – Configure the virtual console at boot"
---

<p>systemd-vconsole-setup.service, systemd-vconsole-setup &#8211; Configure the virtual console at boot</p>
<h2>Synopsis</h2>
<p>systemd-vconsole-setup.service </p>
<p> /usr/lib/systemd/systemd-vconsole-setup</p>
<h2>Description</h2>
<p>systemd-vconsole-setup.service is an early-boot service that configures the virtual console font and console keymap. Internally it calls <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) and <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8). </p>
<p> See <code><a href="/docs/linux/man/5-vconsole-conf/">vconsole.conf</a></code>(5) for information about the configuration files understood by this service.</p>
<h2>Kernel Command Line</h2>
<p>A few configuration parameters from vconsole.conf may be overridden on the kernel command line: </p>
<p> <i>vconsole.keymap=</i>, <i>vconsole.keymap.toggle=</i></p>
<dl>
<dd>Overrides the key mapping table for the keyboard and the second toggle keymap.</dl>
<p> <i>vconsole.font=</i>, <i>vconsole.font.map=</i>, <i>vconsole.font.unimap=</i></p>
<dl>
<dd>Configures the console font, the console map, and the unicode font map.</dl>
<p> See <code><a href="/docs/linux/man/5-vconsole-conf/">vconsole.conf</a></code>(5) for information about these settings.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-vconsole-conf/">vconsole.conf</a></code>(5), <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1), <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8), <code><a href="/docs/linux/man/8-systemd-localed-service/">systemd-localed.service</a></code>(8) </p>
