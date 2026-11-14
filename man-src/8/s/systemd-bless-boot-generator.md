---
title: "systemd-bless-boot-generator(8)"
name: "systemd-bless-boot-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-bless-boot-generator/"
description: "systemd-bless-boot-generator – Pull systemd-bless-boot.service into the initial boot transaction when boot counting is in effect"
---

<p>systemd-bless-boot-generator &#8211; Pull systemd-bless-boot.service into the initial boot transaction when boot counting is in effect</p>
<h2>Synopsis</h2>
<p>/lib/systemd/system-generators/systemd-bless-boot-generator</p>
<h2>Description</h2>
<p>systemd-bless-boot-generator is a generator that pulls systemd-bless-boot.service into the initial boot transaction when boot counting, as implemented by <code><a href="/docs/linux/man/7-systemd-boot/">systemd-boot</a></code>(7), is enabled. </p>
<p> systemd-bless-boot-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-bless-boot-service/">systemd-bless-boot.service</a></code>(8), <code><a href="/docs/linux/man/7-systemd-boot/">systemd-boot</a></code>(7) </p>
