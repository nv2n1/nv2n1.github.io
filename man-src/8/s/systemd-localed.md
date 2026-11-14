---
title: "systemd-localed(8)"
name: "systemd-localed"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-localed/"
description: "systemd-localed.service, systemd-localed – Locale bus mechanism"
---

<p>systemd-localed.service, systemd-localed &#8211; Locale bus mechanism</p>
<h2>Synopsis</h2>
<p>systemd-localed.service </p>
<p> /lib/systemd/systemd-localed</p>
<h2>Description</h2>
<p>systemd-localed.service is a system service that may be used as mechanism to change the system locale settings, as well as the console key mapping and default X11 key mapping. systemd-localed is automatically activated on request and terminates itself when it is unused. </p>
<p> The tool <code><a href="/docs/linux/man/1-localectl/">localectl</a></code>(1) is a command line client to this service. </p>
<p> See <code><a href="/docs/linux/man/5-org-freedesktop-locale1/">org.freedesktop.locale1</a></code>(5) and <code><a href="/docs/linux/man/5-org-freedesktop-logcontrol1/">org.freedesktop.LogControl1</a></code>(5) for a description of the D-Bus API.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-locale-conf/">locale.conf</a></code>(5), <code><a href="/docs/linux/man/5-vconsole-conf/">vconsole.conf</a></code>(5), <code><a href="/docs/linux/man/1-localectl/">localectl</a></code>(1), <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) </p>
