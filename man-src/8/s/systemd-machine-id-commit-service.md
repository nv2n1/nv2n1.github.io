---
title: "systemd-machine-id-commit-service(8)"
name: "systemd-machine-id-commit-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-machine-id-commit-service/"
description: "systemd-machine-id-commit.service – Commit a transient machine ID to disk"
---

<p>systemd-machine-id-commit.service &#8211; Commit a transient machine ID to disk</p>
<h2>Synopsis</h2>
<p>systemd-machine-id-commit.service</p>
<h2>Description</h2>
<p>systemd-machine-id-commit.service is an early boot service responsible for committing transient /etc/machine-id files to a writable disk file system. See <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5) for more information about machine IDs. </p>
<p> This service is started after local-fs.target in case /etc/machine-id is a mount point of its own (usually from a memory file system such as &quot;tmpfs&quot;) and /etc is writable. The service will invoke <code>systemd-machine-id-setup &#8211;commit</code>, which writes the current transient machine ID to disk and unmount the /etc/machine-id file in a race-free manner to ensure that file is always valid and accessible for other processes. See <code><a href="/docs/linux/man/1-systemd-machine-id-setup/">systemd-machine-id-setup</a></code>(1) for details. </p>
<p> The main use case of this service are systems where /etc/machine-id is read-only and initially not initialized. In this case, the system manager will generate a transient machine ID file on a memory file system, and mount it over /etc/machine-id, during the early boot phase. This service is then invoked in a later boot phase, as soon as /etc/ has been remounted writable and the ID may thus be committed to disk to make it permanent.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemd-machine-id-setup/">systemd-machine-id-setup</a></code>(1), <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5), <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) </p>
