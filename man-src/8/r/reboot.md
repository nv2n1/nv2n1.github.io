---
title: "reboot(8)"
name: "reboot"
section: "8"
letter: "r"
url: "/docs/linux/man/8-reboot/"
description: "halt, poweroff, reboot – Halt, power-off or reboot the machine"
---

<p>halt, poweroff, reboot &#8211; Halt, power-off or reboot the machine</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>halt</code> [OPTIONS&#8230;]</p>
<dt> <code>poweroff</code> [OPTIONS&#8230;]</p>
<dt> <code>reboot</code> [OPTIONS&#8230;]</dl>
<h2>Description</h2>
<p><code>halt</code>, <code>poweroff</code>, <code>reboot</code></p>
<dd>may be used to halt, power-off, or reboot the machine. All three commands take the same options.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;halt</code></p>
<dl>
<dd>Halt the machine, regardless of which one of the three commands is invoked.</dl>
<p> <code>-p</code>, <code>&#8211;poweroff</code></p>
<dl>
<dd>Power-off the machine, regardless of which one of the three commands is invoked.</dl>
<p> <code>&#8211;reboot</code></p>
<dl>
<dd>Reboot the machine, regardless of which one of the three commands is invoked.</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dd>Force immediate halt, power-off, or reboot. When specified once, this results in an immediate but clean shutdown by the system manager. When specified twice, this results in an immediate shutdown without contacting the system manager. See the description of <code>&#8211;force</code> in <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) for more details.</dl>
<p> <code>-w</code>, <code>&#8211;wtmp-only</code></p>
<dl>
<dd>Only write wtmp shutdown entry, do not actually halt, power-off, reboot.</dl>
<p> <code>-d</code>, <code>&#8211;no-wtmp</code></p>
<dl>
<dd>Do not write wtmp shutdown entry.</dl>
<p> <code>-n</code>, <code>&#8211;no-sync</code></p>
<dl>
<dd>Don&#8217;t sync hard disks/storage media before halt, power-off, reboot.</dl>
<p> <code>&#8211;no-wall</code></p>
<dl>
<dd>Do not send wall message before halt, power-off, reboot.</dl>
<h2>Exit Status</h2>
<p>On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>Notes</h2>
<p>These commands are implemented in a way that preserves basic compatibility with the original SysV commands. <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) verbs <code>halt</code>, <code>poweroff</code>, <code>reboot</code> provide the same functionality with some additional features. </p>
<p> Note that on many SysV systems <code>halt</code> used to be synonymous to <code>poweroff</code>, i.e. both commands would equally result in powering the machine off. systemd is more accurate here, and <code>halt</code> results in halting the machine only (leaving power on), and <code>poweroff</code> is required to actually power it off.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8), <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1) </p>
