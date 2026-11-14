---
title: "dh_installsystemd(1)"
name: "dh_installsystemd"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installsystemd/"
description: "dh_installsystemd – install systemd unit files"
---

<h2 class="name">NAME</h2>
<p> dh_installsystemd &#8211; install systemd unit files </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installsystemd</code> [<i>debhelper options</i>] [<code>&#8211;restart-after-upgrade</code>] [<code>&#8211;no-stop-on-upgrade</code>] [<code>&#8211;no-enable</code>] [<code>&#8211;name=</code><i>name</i>] [<i>unit file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installsystemd</code> is a debhelper program that is responsible for enabling, disabling, starting, stopping and restarting systemd unit files. </p>
<p> In the simple case, it finds all unit files installed by a package (e.g. bacula-fd.service) and enables them. It is not necessary that the machine actually runs systemd during package installation time, enabling happens on all machines in order to be able to switch from sysvinit to systemd and back. </p>
<p> For only generating blocks for specific service files, you need to pass them as arguments, e.g. <code>dh_installsystemd quota.service</code> and <code>dh_installsystemd &#8211;name=quotarpc quotarpc.service</code>.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.service, debian/<i>package</i>@.service</p>
<dd> If this exists, it is installed into lib/systemd/system/<i>package</i>.service (or lib/systemd/system/<i>package</i>@.service) in the package build directory.</p>
<dt>debian/<i>package</i>.tmpfile</p>
<dd> If this exists, it is installed into usr/lib/tmpfiles.d/<i>package</i>.conf in the package build directory. (The tmpfiles.d mechanism is currently only used by systemd.)</p>
<dt>debian/<i>package</i>.target, debian/<i>package</i>@.target</p>
<dd> If this exists, it is installed into lib/systemd/system/<i>package</i>.target (or lib/systemd/system/<i>package</i>@.target) in the package build directory.</p>
<dt>debian/<i>package</i>.socket, debian/<i>package</i>@.socket</p>
<dd> If this exists, it is installed into lib/systemd/system/<i>package</i>.socket (or lib/systemd/system/<i>package</i>@.socket) in the package build directory.</p>
<dt>debian/<i>package</i>.mount</p>
<dd> If this exists, it is installed into lib/systemd/system/<i>package</i>.mount in the package build directory.</p>
<dt>debian/<i>package</i>.path, debian/<i>package</i>@.path</p>
<dd> If this exists, it is installed into lib/systemd/system/<i>package</i>.path (or lib/systemd/system/<i>package</i>@.path) in the package build directory.</p>
<dt>debian/<i>package</i>.timer, debian/<i>package</i>@.timer</p>
<dd> If this exists, it is installed into lib/systemd/system/<i>package</i>.timer (or lib/systemd/system/<i>package</i>@.timer) in the package build directory.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;no-enable</code></p>
<dd> Disable the service(s) on purge, but do not enable them on install. </p>
<p> <code>Note</code> that this option does not affect whether the services are started. Please remember to also use <code>&#8211;no-start</code> if the service should not be started.</p>
<dt><code>&#8211;name=</code><i>name</i></p>
<dd> Install the service file as <i>name.service</i> instead of the default filename, which is the <i>package.service</i>. When this parameter is used, <code>dh_installsystemd</code> looks for and installs files named <i>debian/package.name.service</i> instead of the usual <i>debian/package.service</i>. Moreover, maintainer scripts are only generated for units that match the given <i>name</i>.</p>
<dt><code>&#8211;restart-after-upgrade</code></p>
<dd> Do not stop the unit file until after the package upgrade has been completed. This is the default behaviour in compat 10. </p>
<p> In earlier compat levels the default was to stop the unit file in the <i>prerm</i>, and start it again in the <i>postinst</i>. </p>
<p> This can be useful for daemons that should not have a possibly long downtime during upgrade. But you should make sure that the daemon will not get confused by the package being upgraded while it&#8217;s running before using this option.</p>
<dt><code>&#8211;no-restart-after-upgrade</code></p>
<dd> Undo a previous <code>&#8211;restart-after-upgrade</code> (or the default of compat 10). If no other options are given, this will cause the service to be stopped in the <i>prerm</i> script and started again in the <i>postinst</i> script.</p>
<dt><code>-r</code>, <code>&#8211;no-stop-on-upgrade</code>, <code>&#8211;no-restart-on-upgrade</code></p>
<dd> Do not stop service on upgrade.</p>
<dt><code>&#8211;no-start</code></p>
<dd> Do not start the unit file after upgrades and after initial installation (the latter is only relevant for services without a corresponding init script). </p>
<p> <code>Note</code> that this option does not affect whether the services are enabled. Please remember to also use <code>&#8211;no-enable</code> if the services should not be enabled.</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) should be called between invocations of this command (with the same arguments). Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7)</p>
<h2>AUTHORS</h2>
<p> pkg-systemd-maintainers [at] lists.alioth.debian.org </p>
<h2>Index</h2>
