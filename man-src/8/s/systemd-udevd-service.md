---
title: "systemd-udevd-service(8)"
name: "systemd-udevd-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-udevd-service/"
description: "systemd-udevd.service, systemd-udevd-control.socket, systemd-udevd-kernel.socket, systemd-udevd – Device event managing daemon"
---

<p>systemd-udevd.service, systemd-udevd-control.socket, systemd-udevd-kernel.socket, systemd-udevd &#8211; Device event managing daemon</p>
<h2>Synopsis</h2>
<p>systemd-udevd.service </p>
<p> systemd-udevd-control.socket </p>
<p> systemd-udevd-kernel.socket</p>
<dl>
<dt> <code>/lib/systemd/systemd-udevd</code> [<code>&#8211;daemon</code>] [<code>&#8211;debug</code>] [<code>&#8211;children-max=</code>] [<code>&#8211;exec-delay=</code>] [<code>&#8211;event-timeout=</code>] [<code>&#8211;resolve-names=early|late|never</code>] [<code>&#8211;version</code>] [<code>&#8211;help</code>]</dl>
<h2>Description</h2>
<p><code>systemd-udevd</code></p>
<dd>listens to kernel uevents. For every event, systemd-udevd executes matching instructions specified in udev rules. See <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7). </p>
<p> The behavior of the daemon can be configured using <code><a href="/docs/linux/man/5-udev-conf/">udev.conf</a></code>(5), its command line options, environment variables, and on the kernel command line, or changed dynamically with <code>udevadm control</code>.</p>
<h2>Options</h2>
<p><code>-d</code>, <code>&#8211;daemon</code></p>
<dl>
<dd>Detach and run in the background.</dl>
<p> <code>-D</code>, <code>&#8211;debug</code></p>
<dl>
<dd>Print debug messages to standard error.</dl>
<p> <code>-c</code>, <code>&#8211;children-max=</code></p>
<dl>
<dd>Limit the number of events executed in parallel.</dl>
<p> <code>-e</code>, <code>&#8211;exec-delay=</code></p>
<dl>
<dd>Delay the execution of each <i>RUN{</i><i>program</i><i>}</i> parameter by the given number of seconds. This option might be useful when debugging system crashes during coldplug caused by loading non-working kernel modules.</dl>
<p> <code>-t</code>, <code>&#8211;event-timeout=</code></p>
<dl>
<dd>Set the number of seconds to wait for events to finish. After this time, the event will be terminated. The default is 180 seconds.</dl>
<p> <code>-s</code>, <code>&#8211;timeout-signal=</code></p>
<dl>
<dd>Set the signal which systemd-udevd will send to forked off processes after reaching event timeout. The setting can be overridden at boot time with the kernel command line option <i>udev.timeout_signal=</i>. Setting to <code>SIGABRT</code> may be helpful in order to debug worker timeouts. Defaults to <code>SIGKILL</code>. Note that setting the option on the command line overrides the setting from the configuration file.</dl>
<p> <code>-N</code>, <code>&#8211;resolve-names=</code></p>
<dl>
<dd>Specify when systemd-udevd should resolve names of users and groups. When set to <code>early</code> (the default), names will be resolved when the rules are parsed. When set to <code>late</code>, names will be resolved for every event. When set to <code>never</code>, names will never be resolved and all devices will be owned by root.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>Kernel Command Line</h2>
<p>Parameters prefixed with &quot;rd.&quot; will be read when <code>systemd-udevd</code> is used in an initrd, those without will be processed both in the initrd and on the host. </p>
<p> <i>udev.log_level=</i>, <i>rd.udev.log_level=</i></p>
<dl>
<dd>Set the log level.</dl>
<p> <i>udev.children_max=</i>, <i>rd.udev.children_max=</i></p>
<dl>
<dd>Limit the number of events executed in parallel.</dl>
<p> <i>udev.exec_delay=</i>, <i>rd.udev.exec_delay=</i></p>
<dl>
<dd>Delay the execution of each <i>RUN{</i><i>program</i><i>}</i> parameter by the given number of seconds. This option might be useful when debugging system crashes during coldplug caused by loading non-working kernel modules.</dl>
<p> <i>udev.event_timeout=</i>, <i>rd.udev.event_timeout=</i></p>
<dl>
<dd>Wait for events to finish up to the given number of seconds. This option might be useful if events are terminated due to kernel drivers taking too long to initialize.</dl>
<p> <i>udev.timeout_signal=</i>, <i>rd.udev.timeout_signal=</i></p>
<dl>
<dd>Specifies a signal that systemd-udevd will send to workers on timeout. Note that kernel command line option overrides both the setting in the configuration file and the one on the program command line.</dl>
<p> <i>udev.blockdev_read_only</i>, <i>rd.udev.blockdev_read_only</i></p>
<dl>
<dd>If specified, mark all physical block devices read-only as they appear. Synthetic block devices (such as loopback block devices or device mapper devices) are left as they are. This is useful to guarantee that the contents of physical block devices remains unmodified during runtime, for example to implement fully stateless systems, for testing or for recovery situations where corrupted file systems shall not be corrupted further through accidental modification. </p>
<p> A block device may be marked writable again by issuing the <code>blockdev &#8211;setrw</code> command, see <code><a href="/docs/linux/man/8-blockdev/">blockdev</a></code>(8) for details.</dl>
<p> <i>net.ifnames=</i></p>
<dl>
<dd>Network interfaces are renamed to give them predictable names when possible. It is enabled by default; specifying 0 disables it.</dl>
<p> <i>net.naming-scheme=</i></p>
<dl>
<dd>Network interfaces are renamed to give them predictable names when possible (unless <i>net.ifnames=0</i> is specified, see above). With this kernel command line option it is possible to pick a specific version of this algorithm and override the default chosen at compilation time. Expects one of the naming scheme identifiers listed in <code><a href="/docs/linux/man/7-systemd-net-naming-scheme/">systemd.net-naming-scheme</a></code>(7), or &quot;latest&quot; to select the latest scheme known (to this particular version of systemd-udevd.service). </p>
<p> Note that selecting a specific scheme is not sufficient to fully stabilize interface naming: the naming is generally derived from driver attributes exposed by the kernel. As the kernel is updated, previously missing attributes systemd-udevd.service is checking might appear, which affects older name derivation algorithms, too.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-udev-conf/">udev.conf</a></code>(5), <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7), <code><a href="/docs/linux/man/8-udevadm/">udevadm</a></code>(8) </p>
