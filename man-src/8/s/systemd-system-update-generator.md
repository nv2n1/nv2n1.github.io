---
title: "systemd-system-update-generator(8)"
name: "systemd-system-update-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-system-update-generator/"
description: "systemd-system-update-generator – Generator for redirecting boot to offline update mode"
---

<p>systemd-system-update-generator &#8211; Generator for redirecting boot to offline update mode</p>
<h2>Synopsis</h2>
<p>/lib/systemd/system-generators/systemd-system-update-generator</p>
<h2>Description</h2>
<p>systemd-system-update-generator is a generator that automatically redirects the boot process to system-update.target, if /system-update exists. This is required to implement the logic explained in the <code><a href="/docs/linux/man/7-systemd-offline-updates/">systemd.offline-updates</a></code>(7). </p>
<p> systemd-system-update-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) </p>
