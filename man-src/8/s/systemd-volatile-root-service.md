---
title: "systemd-volatile-root-service(8)"
name: "systemd-volatile-root-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-volatile-root-service/"
description: "systemd-volatile-root.service, systemd-volatile-root – Make the root file system volatile"
---

<p>systemd-volatile-root.service, systemd-volatile-root &#8211; Make the root file system volatile</p>
<h2>Synopsis</h2>
<p>systemd-volatile-root.service </p>
<p> /lib/systemd/systemd-volatile-root</p>
<h2>Description</h2>
<p>systemd-volatile-root.service is a service that replaces the root directory with a volatile memory file system (&quot;tmpfs&quot;), mounting the original (non-volatile) /usr/ inside it read-only. This way, vendor data from /usr/ is available as usual, but all configuration data in /etc/, all state data in /var/ and all other resources stored directly under the root directory are reset on boot and lost at shutdown, enabling fully stateless systems. </p>
<p> This service is only enabled if full volatile mode is selected, for example by specifying &quot;systemd.volatile=yes&quot; on the kernel command line. This service runs only in the initial RAM disk (&quot;initrd&quot;), before the system transitions to the host&#8217;s root directory. Note that this service is not used if &quot;systemd.volatile=state&quot; is used, as in that mode the root directory is non-volatile.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8), <code><a href="/docs/linux/man/7-kernel-command-line/">kernel-command-line</a></code>(7) </p>
