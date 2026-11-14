---
title: "30-systemd-environment-d-generator(8)"
name: "30-systemd-environment-d-generator"
section: "8"
letter: "3"
url: "/docs/linux/man/8-30-systemd-environment-d-generator/"
description: "systemd-environment-d-generator, 30-systemd-environment-d-generator – Load variables specified by environment.d"
---

<p>systemd-environment-d-generator, 30-systemd-environment-d-generator &#8211; Load variables specified by environment.d</p>
<h2>Synopsis</h2>
<p>/usr/lib/systemd/user-environment-generators/30-systemd-environment-d-generator</p>
<h2>Description</h2>
<p>systemd-environment-d-generator is a <code><a href="/docs/linux/man/7-systemd-environment-generator/">systemd.environment-generator</a></code>(7) that reads environment configuration specified by <code><a href="/docs/linux/man/5-environment-d/">environment.d</a></code>(5) configuration files and passes it to the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) user manager instance.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-environment-generator/">systemd.environment-generator</a></code>(7), <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7) </p>
