---
title: "systemd-xdg-autostart-generator(8)"
name: "systemd-xdg-autostart-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-xdg-autostart-generator/"
description: "systemd-xdg-autostart-generator – User unit generator for XDG autostart files"
---

<p>systemd-xdg-autostart-generator &#8211; User unit generator for XDG autostart files</p>
<h2>Synopsis</h2>
<p>/usr/lib/systemd/user-generators/systemd-xdg-autostart-generator</p>
<h2>Description</h2>
<p>systemd-xdg-autostart-generator is a generator that creates .service units for m[blue]<code>XDG autostart</code>m[]<font SIZE="-2">[1]</font> files. This permits desktop environments to delegate startup of these applications to <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) . </p>
<p> Units created by systemd-xdg-autostart-generator can be started by the desktop environment using &quot;xdg-desktop-autostart.target&quot;. See <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) for more details. </p>
<p> systemd-xdg-autostart-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-target/">systemd.target</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>XDG autostart</p>
<dl>
<dd><a rel="nofollow" href="https://specifications.freedesktop.org/autostart-spec/autostart-spec-latest.html">https://specifications.freedesktop.org/autostart-spec/autostart-spec-latest.html</a></dl>
