---
title: "systemd-importd-service(8)"
name: "systemd-importd-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-importd-service/"
description: "systemd-importd.service, systemd-importd – VM and container image import and export service"
---

<p>systemd-importd.service, systemd-importd &#8211; VM and container image import and export service</p>
<h2>Synopsis</h2>
<p>systemd-importd.service </p>
<p> /lib/systemd/systemd-importd</p>
<h2>Description</h2>
<p><code>systemd-importd</code> is a system service that allows importing, exporting and downloading of system images suitable for running as VM or containers. It is a companion service for <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8), and provides the implementation for <code><a href="/docs/linux/man/1-machinectl/">machinectl</a></code>(1)&#8217;s <code>pull-raw</code>, <code>pull-tar</code>, <code>import-raw</code>, <code>import-tar</code>, <code>import-fs</code>, <code>export-raw</code>, and <code>export-tar</code> commands. </p>
<p> See <code><a href="/docs/linux/man/5-org-freedesktop-import1/">org.freedesktop.import1</a></code>(5) and <code><a href="/docs/linux/man/5-org-freedesktop-logcontrol1/">org.freedesktop.LogControl1</a></code>(5) for a description of the D-Bus API.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-machinectl/">machinectl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1) </p>
