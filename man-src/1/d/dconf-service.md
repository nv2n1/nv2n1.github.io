---
title: "dconf-service(1)"
name: "dconf-service"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dconf-service/"
description: "dconf-service – D-Bus service for writes to the dconf database"
---

<h2 class="name">NAME</h2>
<p> dconf-service &#8211; D-Bus service for writes to the dconf database </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dconf-service</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dconf-service</code> program provides the <i>ca.desrt.dconf</i> name on the session or system bus. Users or administrators should never need to start the service, as it will be automatically started by <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1) whenever an application tries to write settings. </p>
<p> Reading values from the dconf database does not involve the service; it is only needed for writes. The service is stateless and can exit freely at any time (and is therefore robust against crashes).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-dconf/">dconf</a></code>(7), <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) </p>
<h2>Index</h2>
