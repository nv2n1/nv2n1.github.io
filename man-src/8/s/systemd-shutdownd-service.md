---
title: "systemd-shutdownd-service(8)"
name: "systemd-shutdownd-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-shutdownd-service/"
description: "systemd-shutdownd.service, systemd-shutdownd.socket, systemd-shutdownd – Scheduled shutdown service"
---

<p>systemd-shutdownd.service, systemd-shutdownd.socket, systemd-shutdownd &#8211; Scheduled shutdown service</p>
<h2>Synopsis</h2>
<p>systemd-shutdownd.service </p>
<p> systemd-shutdownd.socket </p>
<p> /usr/lib/systemd/systemd-shutdownd</p>
<h2>Description</h2>
<p>systemd-shutdownd.service is a system service that implements scheduled shutdowns, as exposed by <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8). systemd-shutdownd.service is automatically activated on request and terminates itself when it is unused.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8) </p>
