---
title: "sleep-conf-d(5)"
name: "sleep-conf-d"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sleep-conf-d/"
description: "systemd-sleep.conf, sleep.conf.d – Suspend and hibernation configuration file"
---

<p>systemd-sleep.conf, sleep.conf.d &#8211; Suspend and hibernation configuration file</p>
<h2>Synopsis</h2>
<p>/etc/systemd/sleep.conf </p>
<p> /etc/systemd/sleep.conf.d/*.conf </p>
<p> /run/systemd/sleep.conf.d/*.conf </p>
<p> /usr/lib/systemd/sleep.conf.d/*.conf</p>
<h2>Description</h2>
<p><code>systemd</code> supports four general power-saving modes: </p>
<p> suspend</p>
<dl>
<dd>a low-power state where execution of the OS is paused, and complete power loss might result in lost data, and which is fast to enter and exit. This corresponds to suspend, standby, or freeze states as understood by the kernel.</dl>
<p> hibernate</p>
<dl>
<dd>a low-power state where execution of the OS is paused, and complete power loss does not result in lost data, and which might be slow to enter and exit. This corresponds to the hibernation as understood by the kernel.</dl>
<p> hybrid-sleep</p>
<dl>
<dd>a low-power state where execution of the OS is paused, which might be slow to enter, and on complete power loss does not result in lost data but might be slower to exit in that case. This mode is called suspend-to-both by the kernel.</dl>
<p> suspend-then-hibernate</p>
<dl>
<dd>A low power state where the system is initially suspended (the state is stored in RAM). If not interrupted within the delay specified by <code>HibernateDelaySec=</code>, the system will be woken using an RTC alarm and hibernated (the state is then stored on disk).</dl>
<p> Settings in these files determine what strings will be written to /sys/power/disk and /sys/power/state by <code><a href="/docs/linux/man/8-systemd-sleep/">systemd-sleep</a></code>(8) when <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) attempts to suspend or hibernate the machine. See <code><a href="/docs/linux/man/7-systemd-syntax/">systemd.syntax</a></code>(7) for a general description of the syntax.</p>
<h2>Configuration Directories And Precedence</h2>
<p>The default configuration is set during compilation, so configuration is only needed when it is necessary to deviate from those defaults. Initially, the main configuration file in /etc/systemd/ contains commented out entries showing the defaults as a guide to the administrator. Local overrides can be created by editing this file or by creating drop-ins, as described below. Using drop-ins for local configuration is recommended over modifications to the main configuration file. </p>
<p> In addition to the &quot;main&quot; configuration file, drop-in configuration snippets are read from /usr/lib/systemd/*.conf.d/, /usr/local/lib/systemd/*.conf.d/, and /etc/systemd/*.conf.d/. Those drop-ins have higher precedence and override the main configuration file. Files in the *.conf.d/ configuration subdirectories are sorted by their filename in lexicographic order, regardless of in which of the subdirectories they reside. When multiple files specify the same option, for options which accept just a single value, the entry in the file sorted last takes precedence, and for options which accept a list of values, entries are collected as they occur in the sorted files. </p>
<p> When packages need to customize the configuration, they can install drop-ins under /usr/. Files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. Drop-ins have to be used to override package drop-ins, since the main configuration file has lower precedence. It is recommended to prefix all filenames in those subdirectories with a two-digit number and a dash, to simplify the ordering of the files. </p>
<p> To disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in the configuration directory in /etc/, with the same filename as the vendor configuration file.</p>
<h2>Options</h2>
<p>The following options can be configured in the [Sleep] section of /etc/systemd/sleep.conf or a sleep.conf.d file: </p>
<p> <i>AllowSuspend=</i>, <i>AllowHibernation=</i>, <i>AllowSuspendThenHibernate=</i>, <i>AllowHybridSleep=</i></p>
<dl>
<dd>By default any power-saving mode is advertised if possible (i.e. the kernel supports that mode, the necessary resources are available). Those switches can be used to disable specific modes. </p>
<p> If <i>AllowHibernation=no</i> or <i>AllowSuspend=no</i> is used, this implies <i>AllowSuspendThenHibernate=no</i> and <i>AllowHybridSleep=no</i>, since those methods use both suspend and hibernation internally. <i>AllowSuspendThenHibernate=yes</i> and <i>AllowHybridSleep=yes</i> can be used to override and enable those specific modes.</dl>
<p> <i>SuspendMode=</i>, <i>HibernateMode=</i>, <i>HybridSleepMode=</i></p>
<dl>
<dd>The string to be written to /sys/power/disk by, respectively, <code><a href="/docs/linux/man/8-systemd-suspend-service/">systemd-suspend.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-hibernate-service/">systemd-hibernate.service</a></code>(8), or <code><a href="/docs/linux/man/8-systemd-hybrid-sleep-service/">systemd-hybrid-sleep.service</a></code>(8). More than one value can be specified by separating multiple values with whitespace. They will be tried in turn, until one is written without error. If neither succeeds, the operation will be aborted. </p>
<p> <code><a href="/docs/linux/man/8-systemd-suspend-then-hibernate-service/">systemd-suspend-then-hibernate.service</a></code>(8) uses the value of <i>SuspendMode=</i> when suspending and the value of <i>HibernateMode=</i> when hibernating.</dl>
<p> <i>SuspendState=</i>, <i>HibernateState=</i>, <i>HybridSleepState=</i></p>
<dl>
<dd>The string to be written to /sys/power/state by, respectively, <code><a href="/docs/linux/man/8-systemd-suspend-service/">systemd-suspend.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-hibernate-service/">systemd-hibernate.service</a></code>(8), or <code><a href="/docs/linux/man/8-systemd-hybrid-sleep-service/">systemd-hybrid-sleep.service</a></code>(8). More than one value can be specified by separating multiple values with whitespace. They will be tried in turn, until one is written without error. If neither succeeds, the operation will be aborted. </p>
<p> <code><a href="/docs/linux/man/8-systemd-suspend-then-hibernate-service/">systemd-suspend-then-hibernate.service</a></code>(8) uses the value of <i>SuspendState=</i> when suspending and the value of <i>HibernateState=</i> when hibernating.</dl>
<p> <i>HibernateDelaySec=</i></p>
<dl>
<dd>The amount of time the system spends in suspend mode before the system is automatically put into hibernate mode, when using <code><a href="/docs/linux/man/8-systemd-suspend-then-hibernate-service/">systemd-suspend-then-hibernate.service</a></code>(8). Defaults to 2h.</dl>
<h2>Example: Freeze</h2>
<p>Example: to exploit the &#8220;freeze&#8221; mode added in Linux 3.9, one can use <code>systemctl suspend</code> with </p>
<dl>
<dd>
<pre>[Sleep]
SuspendState=freeze</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-systemd-sleep/">systemd-sleep</a></code>(8), <code><a href="/docs/linux/man/8-systemd-suspend-service/">systemd-suspend.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-hibernate-service/">systemd-hibernate.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-hybrid-sleep-service/">systemd-hybrid-sleep.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-suspend-then-hibernate-service/">systemd-suspend-then-hibernate.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7) </p>
