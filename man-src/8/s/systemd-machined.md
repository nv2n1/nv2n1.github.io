---
title: "systemd-machined(8)"
name: "systemd-machined"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-machined/"
description: "systemd-machined.service, systemd-machined – Virtual machine and container registration manager"
---

<p>systemd-machined.service, systemd-machined &#8211; Virtual machine and container registration manager</p>
<h2>Synopsis</h2>
<p>systemd-machined.service </p>
<p> /usr/lib/systemd/systemd-machined</p>
<h2>Description</h2>
<p><code>systemd-machined</code> is a system service that keeps track of virtual machines and containers, and processes belonging to them. </p>
<p> See <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1) for some examples on how to run containers with OS tools. </p>
<p> Use <code><a href="/docs/linux/man/8-nss-mymachines/">nss-mymachines</a></code>(8) to make the names of local containers known to <code>systemd-machined</code> locally resolvable as host names. </p>
<p> See the m[blue]<code>machined D-Bus API Documentation</code>m[]<font SIZE="-2">[1]</font> for information about the APIs systemd-machined provides.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-machinectl/">machinectl</a></code>(1), <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1), <code><a href="/docs/linux/man/8-nss-mymachines/">nss-mymachines</a></code>(8), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>machined D-Bus API Documentation</p>
<dl>
<dd><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/systemd/machined">http://www.freedesktop.org/wiki/Software/systemd/machined</a></dl>
