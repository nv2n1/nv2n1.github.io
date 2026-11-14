---
title: "systemd-update-utmp-runlevel-service(8)"
name: "systemd-update-utmp-runlevel-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-update-utmp-runlevel-service/"
description: "systemd-update-utmp.service, systemd-update-utmp-runlevel.service, systemd-update-utmp – Write audit and utmp updates at bootup, runlevel changes and shutdown"
---

<p>systemd-update-utmp.service, systemd-update-utmp-runlevel.service, systemd-update-utmp &#8211; Write audit and utmp updates at bootup, runlevel changes and shutdown</p>
<h2>Synopsis</h2>
<p>systemd-update-utmp.service </p>
<p> systemd-update-utmp-runlevel.service </p>
<p> /lib/systemd/systemd-update-utmp</p>
<h2>Description</h2>
<p>systemd-update-utmp-runlevel.service is a service that writes SysV runlevel changes to utmp and wtmp, as well as the audit logs, as they occur. systemd-update-utmp.service does the same for system reboots and shutdown requests.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8) </p>
