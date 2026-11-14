---
title: "udev-conf(5)"
name: "udev-conf"
section: "5"
letter: "u"
url: "/docs/linux/man/5-udev-conf/"
description: "udev.conf – Configuration for device event managing daemon"
---

<p>udev.conf &#8211; Configuration for device event managing daemon</p>
<h2>Synopsis</h2>
<p>/etc/udev/udev.conf</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/8-systemd-udevd/">systemd-udevd</a></code>(8) expects its main configuration file at /etc/udev/udev.conf. It consists of a set of variables allowing the user to override default udev values. All empty lines or lines beginning with &#8216;#&#8217; are ignored. The following variables can be set: </p>
<p> <i>udev_log=</i></p>
<dl>
<dd>The log level. Valid values are the numerical syslog priorities or their textual representations: <code>err</code>, <code>info</code> and <code>debug</code>.</dl>
<p> <i>children_max=</i></p>
<dl>
<dd>An integer. The maximum number of events executed in parallel. </p>
<p> This is the same as the <code>&#8211;children-max=</code> option.</dl>
<p> <i>exec_delay=</i></p>
<dl>
<dd>An integer. Delay the execution of each <i>RUN{</i><i>program</i><i>}</i> parameter by the given number of seconds. This option might be useful when debugging system crashes during coldplug caused by loading non-working kernel modules. </p>
<p> This is the same as the <code>&#8211;exec-delay=</code> option.</dl>
<p> <i>event_timeout=</i></p>
<dl>
<dd>An integer. The number of seconds to wait for events to finish. After this time, the event will be terminated. The default is 180 seconds. </p>
<p> This is the same as the <code>&#8211;event-timeout=</code> option.</dl>
<p> <i>resolve_names=</i></p>
<dl>
<dd>Specifies when systemd-udevd should resolve names of users and groups. When set to <code>early</code> (the default), names will be resolved when the rules are parsed. When set to <code>late</code>, names will be resolved for every event. When set to <code>never</code>, names will never be resolved and all devices will be owned by root. </p>
<p> This is the same as the <code>&#8211;resolve-names=</code> option.</dl>
<p> <i>timeout_signal=</i></p>
<dl>
<dd>Specifies a signal that systemd-udevd will send on worker timeouts. Note that both workers and spawned processes will be killed using this signal. Defaults to <code>SIGKILL</code>.</dl>
<p> In addition, systemd-udevd can be configured by command line options and the kernel command line (see <code><a href="/docs/linux/man/8-systemd-udevd/">systemd-udevd</a></code>(8)).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-systemd-udevd/">systemd-udevd</a></code>(8), <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7), <code><a href="/docs/linux/man/8-udevadm/">udevadm</a></code>(8) </p>
