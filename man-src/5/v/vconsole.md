---
title: "vconsole(5)"
name: "vconsole"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vconsole/"
description: "vconsole.conf – Configuration file for the virtual console"
---

<p>vconsole.conf &#8211; Configuration file for the virtual console</p>
<h2>Synopsis</h2>
<p>/etc/vconsole.conf</p>
<h2>Description</h2>
<p>The /etc/vconsole.conf file configures the virtual console, i.e. keyboard mapping and console font. It is applied at boot by <code><a href="/docs/linux/man/8-systemd-vconsole-setup-service/">systemd-vconsole-setup.service</a></code>(8). </p>
<p> The basic file format of the vconsole.conf is a newline-separated list of environment-like shell-compatible variable assignments. It is possible to source the configuration from shell scripts, however, beyond mere variable assignments no shell features are supported, allowing applications to read the file without implementing a shell compatible execution engine. </p>
<p> Note that the kernel command line options <i>vconsole.keymap=</i>, <i>vconsole.keymap.toggle=</i>, <i>vconsole.font=</i>, <i>vconsole.font.map=</i>, <i>vconsole.font.unimap=</i> may be used to override the console settings at boot. </p>
<p> Depending on the operating system other configuration files might be checked for configuration of the virtual console as well, however only as fallback.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <i>KEYMAP=</i>, <i>KEYMAP_TOGGLE=</i></p>
<dl>
<dd>Configures the key mapping table for the keyboard. <i>KEYMAP=</i> defaults to &quot;us&quot; if not set. The <i>KEYMAP_TOGGLE=</i> can be used to configure a second toggle keymap and is by default unset.</dl>
<p> <i>FONT=</i>, <i>FONT_MAP=</i>, <i>FONT_UNIMAP=</i></p>
<dl>
<dd>Configures the console font, the console map and the unicode font map.</dl>
<h2>Example</h2>
<p><code>Example 1. German keyboard and console</code> </p>
<p> /etc/vconsole.conf: </p>
<dl>
<dd>
<pre>KEYMAP=de-latin1
FONT=latarcyrheb-sun16</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-vconsole-setup-service/">systemd-vconsole-setup.service</a></code>(8), <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1), <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8), <code><a href="/docs/linux/man/5-locale-conf/">locale.conf</a></code>(5), <code><a href="/docs/linux/man/8-systemd-localed-service/">systemd-localed.service</a></code>(8) </p>
