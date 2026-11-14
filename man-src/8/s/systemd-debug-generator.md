---
title: "systemd-debug-generator(8)"
name: "systemd-debug-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-debug-generator/"
description: "systemd-debug-generator – Generator for enabling a runtime debug shell and masking specific units at boot"
---

<p>systemd-debug-generator &#8211; Generator for enabling a runtime debug shell and masking specific units at boot</p>
<h2>Synopsis</h2>
<p>/lib/systemd/system-generators/systemd-debug-generator</p>
<h2>Description</h2>
<p>systemd-debug-generator is a generator that reads the kernel command line and understands three options: </p>
<p> If the <code>systemd.mask=</code> or <code>rd.systemd.mask=</code> option is specified and followed by a unit name, this unit is masked for the runtime, similar to the effect of <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1)&#8217;s <code>mask</code> command. This is useful to boot with certain units removed from the initial boot transaction for debugging system startup. May be specified more than once. <code>rd.systemd.mask=</code> is honored only by initial RAM disk (initrd) while <code>systemd.mask=</code> is honored only in the main system. </p>
<p> If the <code>systemd.wants=</code> or <code>rd.systemd.wants=</code> option is specified and followed by a unit name, a start job for this unit is added to the initial transaction. This is useful to start one or more additional units at boot. May be specified more than once. <code>rd.systemd.wants=</code> is honored only by initial RAM disk (initrd) while <code>systemd.wants=</code> is honored only in the main system. </p>
<p> If the <code>systemd.debug_shell</code> or <code>rd.systemd.debug_shell</code> option is specified, the debug shell service &quot;debug-shell.service&quot; is pulled into the boot transaction and a debug shell will be spawned during early boot. By default, /dev/tty9 is used, but a specific tty can also be set, either with or without the /dev/ prefix. Note that the shell may also be turned on persistently by enabling it with <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1)&#8217;s <code>enable</code> command. <code>rd.systemd.debug_shell=</code> is honored only by initial RAM disk (initrd) while <code>systemd.debug_shell</code> is honored only in the main system. </p>
<p> systemd-debug-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/7-kernel-command-line/">kernel-command-line</a></code>(7) </p>
