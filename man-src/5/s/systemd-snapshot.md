---
title: "systemd-snapshot(5)"
name: "systemd-snapshot"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-snapshot/"
description: "systemd.snapshot – Snapshot unit configuration"
---

<p>systemd.snapshot &#8211; Snapshot unit configuration</p>
<h2>Synopsis</h2>
<p><i>snapshot</i>.snapshot</p>
<h2>Description</h2>
<p>Snapshot units are not configured via unit configuration files. Nonetheless they are named similar to filenames. A unit whose name ends in &quot;.snapshot&quot; refers to a dynamic snapshot of the systemd runtime state. </p>
<p> Snapshots are not configured on disk but created dynamically via <code>systemctl snapshot</code> (see <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) for details) or an equivalent command. When created, they will automatically get dependencies on the currently activated units. They act as saved runtime state of the systemd manager. Later on, the user may choose to return to the saved state via <code>systemctl isolate</code>. They are useful to roll back to a defined state after temporarily starting/stopping services or similar.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7) </p>
