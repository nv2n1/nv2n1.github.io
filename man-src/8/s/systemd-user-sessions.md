---
title: "systemd-user-sessions(8)"
name: "systemd-user-sessions"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-user-sessions/"
description: "systemd-user-sessions.service, systemd-user-sessions – Permit user logins after boot, prohibit user logins at shutdown"
---

<p>systemd-user-sessions.service, systemd-user-sessions &#8211; Permit user logins after boot, prohibit user logins at shutdown</p>
<h2>Synopsis</h2>
<p>systemd-user-sessions.service </p>
<p> /lib/systemd/systemd-user-sessions</p>
<h2>Description</h2>
<p>systemd-user-sessions.service is a service that controls user logins through <code><a href="/docs/linux/man/8-pam_nologin/">pam_nologin</a></code>(8). After basic system initialization is complete, it removes /run/nologin, thus permitting logins. Before system shutdown, it creates /run/nologin, thus prohibiting further logins.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-logind-service/">systemd-logind.service</a></code>(8), <code><a href="/docs/linux/man/8-pam_nologin/">pam_nologin</a></code>(8) </p>
