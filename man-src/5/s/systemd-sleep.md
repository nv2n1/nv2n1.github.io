---
title: "systemd-sleep(5)"
name: "systemd-sleep"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-sleep/"
description: "systemd-sleep.conf – Suspend and hibernation configuration file"
---

<p>systemd-sleep.conf &#8211; Suspend and hibernation configuration file</p>
<h2>Synopsis</h2>
<p>/etc/systemd/sleep.conf</p>
<h2>Description</h2>
<p><code>systemd</code> supports three general power-saving modes: </p>
<p> suspend</p>
<dl>
<dd>a low-power state where execution of the OS is paused, and complete power loss might result in lost data, and which is fast to enter and exit. This corresponds to suspend, standby, or freeze states as understood by the kernel.</dl>
<p> hibernate</p>
<dl>
<dd>a low-power state where execution of the OS is paused, and complete power loss does not result in lost data, and which might be slow to enter and exit. This corresponds to the hibernation as understood by the kernel.</dl>
<p> hybrid-sleep</p>
<dl>
<dd>a low-power state where execution of the OS is paused, which might be slow to enter, and on complete power loss does not result in lost data but might be slower to exit in that case. This mode is called suspend-to-both by the kernel.</dl>
<p> Settings in this file determine what strings will be written to /sys/power/disk and /sys/power/state by <code><a href="/docs/linux/man/8-systemd-sleep/">systemd-sleep</a></code>(8) when <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) attempts to suspend or hibernate the machine.</p>
<h2>Options</h2>
<p>The following options can be configured in the &quot;[Sleep]&quot; section of /etc/systemd/sleep.conf: </p>
<p> <i>SuspendMode=</i>, <i>HibernateMode=</i>, <i>HybridSleepMode=</i></p>
<dl>
<dd>The string to be written to /sys/power/disk by, respectively, <code><a href="/docs/linux/man/8-systemd-suspend-service/">systemd-suspend.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-hibernate-service/">systemd-hibernate.service</a></code>(8), or <code><a href="/docs/linux/man/8-systemd-hybrid-sleep-service/">systemd-hybrid-sleep.service</a></code>(8). More than one value can be specified by separating multiple values with whitespace. They will be tried in turn, until one is written without error. If neither succeeds, the operation will be aborted.</dl>
<p> <i>SuspendState=</i>, <i>HibernateState=</i>, <i>HybridSleepState=</i></p>
<dl>
<dd>The string to be written to /sys/power/state by, respectively, <code><a href="/docs/linux/man/8-systemd-suspend-service/">systemd-suspend.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-hibernate-service/">systemd-hibernate.service</a></code>(8), or <code><a href="/docs/linux/man/8-systemd-hybrid-sleep-service/">systemd-hybrid-sleep.service</a></code>(8). More than one value can be specified by separating multiple values with whitespace. They will be tried in turn, until one is written without error. If neither succeeds, the operation will be aborted.</dl>
<h2>Example: Freeze</h2>
<p>Example: to exploit the &#8220;freeze&#8221; mode added in Linux 3.9, one can use <code>systemctl suspend</code> with </p>
<dl>
<dd>
<pre>[Sleep]
SuspendState=freeze</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-systemd-sleep/">systemd-sleep</a></code>(8), <code><a href="/docs/linux/man/8-systemd-suspend-service/">systemd-suspend.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-hibernate-service/">systemd-hibernate.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-hybrid-sleep-service/">systemd-hybrid-sleep.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7) </p>
