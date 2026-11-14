---
title: "systemd-update-done(8)"
name: "systemd-update-done"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-update-done/"
description: "systemd-update-done.service, systemd-update-done – Mark /etc and /var fully updated"
---

<p>systemd-update-done.service, systemd-update-done &#8211; Mark /etc and /var fully updated</p>
<h2>Synopsis</h2>
<p>systemd-update-done.service </p>
<p> /usr/lib/systemd/systemd-update-done</p>
<h2>Description</h2>
<p>systemd-update-done.service is a service that is invoked as part of the first boot after the vendor operating system resources in /usr have been updated. This is useful to implement offline updates of /usr which might requires updates to /etc or /var on the following boot. </p>
<p> systemd-update-done.service updates the file modification time (mtime) of the stamp files /etc/.updated and /var/.updated to the modification time of the /usr directory, unless the stamp files are already newer. </p>
<p> Services that shall run after offline upgrades of /usr should order themselves before systemd-update-done.service, and use the <i>ConditionNeedsUpdate=</i> (see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5)) condition to make sure to run when /etc or /var are older than /usr according to the modification times of the files described above. This requires that updates to /usr are always followed by an update of the modification time of /usr, for example by invoking <code><a href="/docs/linux/man/1-touch/">touch</a></code>(1) on it.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/1-touch/">touch</a></code>(1) </p>
