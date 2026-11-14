---
title: "systemd-udevd-kernel(8)"
name: "systemd-udevd-kernel"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-udevd-kernel/"
description: "systemd-udevd.service, systemd-udevd-control.socket, systemd-udevd-kernel.socket, systemd-udevd – Device event managing daemon"
---

<p>systemd-udevd.service, systemd-udevd-control.socket, systemd-udevd-kernel.socket, systemd-udevd &#8211; Device event managing daemon</p>
<h2>Synopsis</h2>
<p>systemd-udevd.service </p>
<p> systemd-udevd-control.socket </p>
<p> systemd-udevd-kernel.socket</p>
<dl>
<dt> <code>/usr/lib/systemd/systemd-udevd</code> [<code>&#8211;daemon</code>] [<code>&#8211;debug</code>] [<code>&#8211;children-max=</code>] [<code>&#8211;exec-delay=</code>] [<code>&#8211;event-timeout=</code>] [<code>&#8211;resolve-names=early|late|never</code>] [<code>&#8211;version</code>] [<code>&#8211;help</code>]</dl>
<h2>Description</h2>
<p><code>systemd-udevd</code></p>
<dd>listens to kernel uevents. For every event, systemd-udevd executes matching instructions specified in udev rules. See <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7). </p>
<p> The behavior of the daemon can be configured using <code><a href="/docs/linux/man/5-udev-conf/">udev.conf</a></code>(5), its command-line options, environment variables, and on the kernel command-line, or changed dynamically with <code>udevadm control</code>.</p>
<h2>Options</h2>
<p><code>&#8211;daemon</code></p>
<dl>
<dd>Detach and run in the background.</dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dd>Print debug messages to standard error.</dl>
<p> <code>&#8211;children-max=</code></p>
<dl>
<dd>Limit the number of events executed in parallel.</dl>
<p> <code>&#8211;exec-delay=</code></p>
<dl>
<dd>Delay the execution of <i>RUN</i> instructions by the given number of seconds. This option might be useful when debugging system crashes during coldplug caused by loading non-working kernel modules.</dl>
<p> <code>&#8211;event-timeout=</code></p>
<dl>
<dd>Set the number of seconds to wait for events to finish. After this time the event will be terminated. The default is 30 seconds.</dl>
<p> <code>&#8211;resolve-names=</code></p>
<dl>
<dd>Specify when systemd-udevd should resolve names of users and groups. When set to <code>early</code> (the default), names will be resolved when the rules are parsed. When set to <code>late</code>, names will be resolved for every event. When set to <code>never</code>, names will never be resolved and all devices will be owned by root.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>Environment</h2>
<p><i>$UDEV_LOG=</i></p>
<dl>
<dd>Set the logging priority.</dl>
<h2>Kernel Command Line</h2>
<p>Parameters starting with &quot;rd.&quot; will be read when <code>systemd-udevd</code> is used in an initrd. </p>
<p> <i>udev.log-priority=</i>, <i>rd.udev.log-priority=</i></p>
<dl>
<dd>Set the logging priority.</dl>
<p> <i>udev.children-max=</i>, <i>rd.udev.children-max=</i></p>
<dl>
<dd>Limit the number of events executed in parallel.</dl>
<p> <i>udev.exec-delay=</i>, <i>rd.udev.exec-delay=</i></p>
<dl>
<dd>Delay the execution of <i>RUN</i> instructions by the given number of seconds. This option might be useful when debugging system crashes during coldplug caused by loading non-working kernel modules.</dl>
<p> <i>udev.event-timeout=</i>, <i>rd.udev.event-timeout=</i></p>
<dl>
<dd>Wait for events to finish up to the given number of seconds. This option might be useful if events are terminated due to kernel drivers taking too long to initialize.</dl>
<p> <i>net.ifnames=</i></p>
<dl>
<dd>Network interfaces are renamed to give them predictable names when possible. It is enabled by default; specifying 0 disables it.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-udev-conf/">udev.conf</a></code>(5), <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7), <code><a href="/docs/linux/man/8-udevadm/">udevadm</a></code>(8) </p>
