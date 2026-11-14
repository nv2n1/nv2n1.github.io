---
title: "systemd-backlight(8)"
name: "systemd-backlight"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-backlight/"
description: "systemd-backlight [at] .service, systemd-backlight – Load and save the display backlight brightness at boot and shutdown"
---

<p>systemd-backlight [at] .service, systemd-backlight &#8211; Load and save the display backlight brightness at boot and shutdown</p>
<h2>Synopsis</h2>
<p>systemd-backlight [at] .service </p>
<p> /usr/lib/systemd/systemd-backlight</p>
<h2>Description</h2>
<p>systemd-backlight [at] .service is a service that restores the display backlight brightness at early boot and saves it at shutdown. On disk, the backlight brightness is stored in /var/lib/systemd/backlight/.</p>
<h2>Kernel Command Line</h2>
<p>systemd-backlight understands the following kernel command line parameter: </p>
<p> <i>systemd.restore_state=</i></p>
<dl>
<dd>Takes a boolean argument. Defaults to &quot;1&quot;. If &quot;0&quot;, does not restore the backlight settings on boot. However, settings will still be stored on shutdown.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) </p>
