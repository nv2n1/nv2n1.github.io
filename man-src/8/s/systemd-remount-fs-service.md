---
title: "systemd-remount-fs-service(8)"
name: "systemd-remount-fs-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-remount-fs-service/"
description: "systemd-remount-fs.service, systemd-remount-fs – Remount root and kernel file systems"
---

<p>systemd-remount-fs.service, systemd-remount-fs &#8211; Remount root and kernel file systems</p>
<h2>Synopsis</h2>
<p>systemd-remount-fs.service </p>
<p> /lib/systemd/systemd-remount-fs</p>
<h2>Description</h2>
<p>systemd-remount-fs.service is an early boot service that applies mount options listed in <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), or gathered from the partition table (when <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8) is active) to the root file system, the /usr/ file system, and the kernel API file systems. This is required so that the mount options of these file systems &#8212; which are pre-mounted by the kernel, the initial RAM disk, container environments or system manager code &#8212; are updated to those configured in /etc/fstab and the other sources. This service ignores normal file systems and only changes the root file system (i.e. /), /usr/, and the virtual kernel API file systems such as /proc/, /sys/ or /dev/. This service executes no operation if no configuration is found (/etc/fstab does not exist or lists no entries for the mentioned file systems, or the partition table does not contain relevant entries). </p>
<p> For a longer discussion of kernel API file systems see m[blue]<code>API File Systems</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> Note: systemd-remount-fs.service is usually pulled in by <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8), hence it is also affected by the kernel command line option <i>fstab=</i>, which may be used to disable the generator. It may also pulled in by <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8), which is affected by <i>systemd.gpt_auto</i> and other options.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>API File Systems</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems">https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems</a></dl>
