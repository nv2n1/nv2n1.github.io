---
title: "dh_systemd_enable(1)"
name: "dh_systemd_enable"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_systemd_enable/"
description: "dh_systemd_enable – enable/disable systemd unit files"
---

<h2 class="name">NAME</h2>
<p> dh_systemd_enable &#8211; enable/disable systemd unit files </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_systemd_enable</code> [<i>debhelper options</i>] [<code>&#8211;no-enable</code>] [<code>&#8211;name=</code><i>name</i>] [<i>unit file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_systemd_enable</code> is a debhelper program that is responsible for enabling and disabling systemd unit files. </p>
<p> In the simple case, it finds all unit files installed by a package (e.g. bacula-fd.service) and enables them. It is not necessary that the machine actually runs systemd during package installation time, enabling happens on all machines in order to be able to switch from sysvinit to systemd and back. </p>
<p> In the complex case, you can call <code>dh_systemd_enable</code> and <code>dh_systemd_start</code> manually (by overwriting the debian/rules targets) and specify flags per unit file. An example is colord, which ships colord.service, a dbus-activated service without an [Install] section. This service file cannot be enabled or disabled (a state called &#8220;static&#8221; by systemd) because it has no [Install] section. Therefore, running dh_systemd_enable does not make sense. </p>
<p> For only generating blocks for specific service files, you need to pass them as arguments, e.g. <code>dh_systemd_enable quota.service</code> and <code>dh_systemd_enable &#8211;name=quotarpc quotarpc.service</code>.</p>
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
<p> <code>Note</code> that this option does not affect whether the services are started. That is controlled by <i><a href="/docs/linux/man/1-dh_systemd_start/">dh_systemd_start</a></i>(1) (using e.g. its <code>&#8211;no-start</code> option).</p>
<dt><code>&#8211;name=</code><i>name</i></p>
<dd> Install the service file as <i>name.service</i> instead of the default filename, which is the <i>package.service</i>. When this parameter is used, <code>dh_systemd_enable</code> looks for and installs files named <i>debian/package.name.service</i> instead of the usual <i>debian/package.service</i>.</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) should be called between invocations of this command (with the same arguments). Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts. </p>
<p> Note that <code>dh_systemd_enable</code> should be run before <code>dh_installinit</code>. The default sequence in <code>dh</code> does the right thing, this note is only relevant when you are calling <code>dh_systemd_enable</code> manually.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dh_systemd_start/">dh_systemd_start</a></i>(1), <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7)</p>
<h2>AUTHORS</h2>
<p> pkg-systemd-maintainers [at] lists.alioth.debian.org </p>
<h2>Index</h2>
