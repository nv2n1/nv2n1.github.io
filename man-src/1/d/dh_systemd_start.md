---
title: "dh_systemd_start(1)"
name: "dh_systemd_start"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_systemd_start/"
description: "dh_systemd_start – start/stop/restart systemd unit files"
---

<h2 class="name">NAME</h2>
<p> dh_systemd_start &#8211; start/stop/restart systemd unit files </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_systemd_start</code> [<i>debhelper options</i>] [<code>&#8211;restart-after-upgrade</code>] [<code>&#8211;no-stop-on-upgrade</code>] [<i>unit file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_systemd_start</code> is a debhelper program that is responsible for starting/stopping or restarting systemd unit files in case no corresponding sysv init script is available. </p>
<p> As with <code>dh_installinit</code>, the unit file is stopped before upgrades and started afterwards (unless <code>&#8211;restart-after-upgrade</code> is specified, in which case it will only be restarted after the upgrade). This logic is not used when there is a corresponding SysV init script because invoke-rc.d performs the stop/start/restart in that case.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;restart-after-upgrade</code></p>
<dd> Do not stop the unit file until after the package upgrade has been completed. This is the default behaviour in compat 10. </p>
<p> In earlier compat levels the default was to stop the unit file in the <i>prerm</i>, and start it again in the <i>postinst</i>. </p>
<p> This can be useful for daemons that should not have a possibly long downtime during upgrade. But you should make sure that the daemon will not get confused by the package being upgraded while it&#8217;s running before using this option.</p>
<dt><code>&#8211;no-restart-after-upgrade</code></p>
<dd> Undo a previous <code>&#8211;restart-after-upgrade</code> (or the default of compat 10). If no other options are given, this will cause the service to be stopped in the <i>prerm</i> script and started again in the <i>postinst</i> script.</p>
<dt><code>-r</code>, <code>&#8211;no-stop-on-upgrade</code>, <code>&#8211;no-restart-on-upgrade</code></p>
<dd> Do not stop service on upgrade.</p>
<dt><code>&#8211;no-start</code></p>
<dd> Do not start the unit file after upgrades and after initial installation (the latter is only relevant for services without a corresponding init script).</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) should be called between invocations of this command (with the same arguments). Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts. </p>
<p> Note that <code>dh_systemd_start</code> should be run after <code>dh_installinit</code> so that it can detect corresponding SysV init scripts. The default sequence in <code>dh</code> does the right thing, this note is only relevant when you are calling <code>dh_systemd_start</code> manually.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7)</p>
<h2>AUTHORS</h2>
<p> pkg-systemd-maintainers [at] lists.alioth.debian.org </p>
<h2>Index</h2>
