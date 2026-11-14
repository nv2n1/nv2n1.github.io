---
title: "udev(5)"
name: "udev"
section: "5"
letter: "u"
url: "/docs/linux/man/5-udev/"
description: "udev.conf – Configuration for device event managing daemon"
---

<p>udev.conf &#8211; Configuration for device event managing daemon</p>
<h2>Synopsis</h2>
<p>/etc/udev/udev.conf</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/8-systemd-udevd/">systemd-udevd</a></code>(8) expects its main configuration file at /etc/udev/udev.conf. It consists of a set of variables allowing the user to override default udev values. All empty lines or lines beginning with &#8216;#&#8217; are ignored. The following variables can be set: </p>
<p> <i>udev_log</i></p>
<dl>
<dd>The logging priority. Valid values are the numerical syslog priorities or their textual representations: <code>err</code>, <code>info</code> and <code>debug</code>.</dl>
<p> In addition, systemd-udevd can be configured by command-line options and the kernel commandline (see <code><a href="/docs/linux/man/8-systemd-udevd/">systemd-udevd</a></code>(8)).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-systemd-udevd/">systemd-udevd</a></code>(8), <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7), <code><a href="/docs/linux/man/8-udevadm/">udevadm</a></code>(8) </p>
