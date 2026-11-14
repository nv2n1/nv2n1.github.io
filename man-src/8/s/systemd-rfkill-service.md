---
title: "systemd-rfkill-service(8)"
name: "systemd-rfkill-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-rfkill-service/"
description: "systemd-rfkill [at] .service, systemd-rfkill – Load and save the RF kill switch state at boot and shutdown"
---

<p>systemd-rfkill [at] .service, systemd-rfkill &#8211; Load and save the RF kill switch state at boot and shutdown</p>
<h2>Synopsis</h2>
<p>systemd-rfkill [at] .service </p>
<p> /usr/lib/systemd/systemd-rfkill</p>
<h2>Description</h2>
<p>systemd-rfkill [at] .service is a service that restores the RF kill switch state at early boot and saves it at shutdown. On disk, the RF kill switch state is stored in /var/lib/systemd/rfkill/.</p>
<h2>Kernel Command Line</h2>
<p>systemd-rfkill understands the following kernel command line parameter: </p>
<p> <i>systemd.restore_state=</i></p>
<dl>
<dd>Takes a boolean argument. Defaults to &quot;1&quot;. If &quot;0&quot;, does not restore the rfkill settings on boot. However, settings will still be stored on shutdown.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) </p>
