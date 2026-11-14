---
title: "systemd-boot-check-no-failures(8)"
name: "systemd-boot-check-no-failures"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-boot-check-no-failures/"
description: "systemd-boot-check-no-failures.service, systemd-boot-check-no-failures – verify that the system booted up cleanly"
---

<p>systemd-boot-check-no-failures.service, systemd-boot-check-no-failures &#8211; verify that the system booted up cleanly</p>
<h2>Synopsis</h2>
<p>systemd-boot-check-no-failures.service </p>
<p> /lib/systemd/system-boot-check-no-failures</p>
<h2>Description</h2>
<p>systemd-boot-check-no-failures.service is a system service that checks whether the system booted up successfully. This service implements a very minimal test only: whether there are any failed units on the system. This service is disabled by default. When enabled, it is ordered before boot-complete.target, thus ensuring the target cannot be reached when the system booted up with failed services. </p>
<p> Note that due the simple nature of this check this service is probably not suitable for deployment in most scenarios. It is primarily useful only as example for developing more fine-grained checks to order before boot-complete.target.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) </p>
