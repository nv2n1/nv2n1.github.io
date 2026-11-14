---
title: "systemd-initctl-service(8)"
name: "systemd-initctl-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-initctl-service/"
description: "systemd-initctl.service, systemd-initctl.socket, systemd-initctl – /dev/initctl compatibility"
---

<p>systemd-initctl.service, systemd-initctl.socket, systemd-initctl &#8211; /dev/initctl compatibility</p>
<h2>Synopsis</h2>
<p>systemd-initctl.service </p>
<p> systemd-initctl.socket </p>
<p> /lib/systemd/systemd-initctl</p>
<h2>Description</h2>
<p>systemd-initctl is a system service that implements compatibility with the /dev/initctl FIFO file system object, as implemented by the SysV init system. systemd-initctl is automatically activated on request and terminates itself when it is unused.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) </p>
