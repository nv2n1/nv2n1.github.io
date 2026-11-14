---
title: "systemd-modules-load-service(8)"
name: "systemd-modules-load-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-modules-load-service/"
description: "systemd-modules-load.service, systemd-modules-load – Load kernel modules at boot"
---

<p>systemd-modules-load.service, systemd-modules-load &#8211; Load kernel modules at boot</p>
<h2>Synopsis</h2>
<p>systemd-modules-load.service </p>
<p> /lib/systemd/systemd-modules-load</p>
<h2>Description</h2>
<p>systemd-modules-load.service is an early boot service that loads kernel modules. It reads static configuration from files in /usr/ and /etc/, but also runtime configuration from /run/ and the kernel command line (see below). </p>
<p> See <code><a href="/docs/linux/man/5-modules-load-d/">modules-load.d</a></code>(5) for information about the configuration format of this service and paths where configuration files can be created.</p>
<h2>Kernel Command Line</h2>
<p>systemd-modules-load.service understands the following kernel command line parameters: </p>
<p> <i>modules_load=</i>, <i>rd.modules_load=</i></p>
<dl>
<dd>Takes a comma-separated list of kernel modules to statically load during early boot. The option prefixed with &quot;rd.&quot; is read by the initial RAM disk only.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-modules-load-d/">modules-load.d</a></code>(5), </p>
