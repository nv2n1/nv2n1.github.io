---
title: "systemd-shutdown(8)"
name: "systemd-shutdown"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-shutdown/"
description: "systemd-halt.service, systemd-poweroff.service, systemd-reboot.service, systemd-kexec.service, systemd-shutdown – System shutdown logic"
---

<p>systemd-halt.service, systemd-poweroff.service, systemd-reboot.service, systemd-kexec.service, systemd-shutdown &#8211; System shutdown logic</p>
<h2>Synopsis</h2>
<p>systemd-halt.service </p>
<p> systemd-poweroff.service </p>
<p> systemd-reboot.service </p>
<p> systemd-kexec.service </p>
<p> /lib/systemd/systemd-shutdown </p>
<p> /lib/systemd/system-shutdown/</p>
<h2>Description</h2>
<p>systemd-halt.service is a system service that is pulled in by halt.target and is responsible for the actual system halt. Similarly, systemd-poweroff.service is pulled in by poweroff.target, systemd-reboot.service by reboot.target and systemd-kexec.service by kexec.target to execute the respective actions. </p>
<p> When these services are run, they ensure that PID 1 is replaced by the /lib/systemd/systemd-shutdown tool which is then responsible for the actual shutdown. Before shutting down, this binary will try to unmount all remaining file systems, disable all remaining swap devices, detach all remaining storage devices and kill all remaining processes. </p>
<p> It is necessary to have this code in a separate binary because otherwise rebooting after an upgrade might be broken &#8212; the running PID 1 could still depend on libraries which are not available any more, thus keeping the file system busy, which then cannot be re-mounted read-only. </p>
<p> Immediately before executing the actual system halt/poweroff/reboot/kexec systemd-shutdown will run all executables in /lib/systemd/system-shutdown/ and pass one arguments to them: either &quot;halt&quot;, &quot;poweroff&quot;, &quot;reboot&quot; or &quot;kexec&quot;, depending on the chosen action. All executables in this directory are executed in parallel, and execution of the action is not continued before all executables finished. </p>
<p> Note that systemd-halt.service (and the related units) should never be executed directly. Instead, trigger system shutdown with a command such as &quot;systemctl halt&quot; or suchlike.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/2-reboot/">reboot</a></code>(2), <code><a href="/docs/linux/man/8-systemd-suspend-service/">systemd-suspend.service</a></code>(8), <code><a href="/docs/linux/man/7-bootup/">bootup</a></code>(7) </p>
