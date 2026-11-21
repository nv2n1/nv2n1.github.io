---
title: "qdbus(1)"
name: "qdbus"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qdbus/"
description: "qdbus – a communication-interface for qt-based applications"
---

<h2 class="name">NAME</h2>
<p> qdbus &#8211; a communication-interface for qt-based applications</p>
<h2>SYNOPSIS</h2>
<p> <code>qdbus</code> [&#8211;system] [&#8211;literal] [servicename] [path] [method] [args] </p>
<h2>DESCRIPTION</h2>
<p> <code>qdbus</code> provides an interface to Qt-based applications communicating over D-Bus. See <a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a> for more information about the big picture. </p>
<p> By default <code>qdbus</code> will list all service names of services that are running and you can manipulate at the moment. You can also manipulate and run several types of methods for each dbus-enabled application. </p>
<dl>
<dt><code>servicename</code></dt>
<dd> the service to connect to (e.g., org.freedesktop.DBus)</dd>
<dt><code>path</code></dt>
<dd> the path to the object (e.g., /)</dd>
<dt><code>method</code></dt>
<dd> the method to call, with or without the interface</dd>
<dt><code>args</code></dt>
<dd> arguments to pass to the call </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;system</code></dt>
<dd> connect to the system bus</dd>
<dt><code>&#8211;literal</code></dt>
<dd> print replies literally </dd>
</dl>
<h2>EXAMPLE</h2>
<p> Here is an example of using <code>qdbus</code> to list all status information about a service:<br />
 % qdbus org.ktorrent.ktorrent </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dbus-cleanup-sockets/">dbus-cleanup-sockets</a>(1), <a href="/docs/linux/man/1-dbus-launch/">dbus-launch</a>(1), <a href="/docs/linux/man/1-dbus-send/">dbus-send</a>(1), <a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a>(1), <a href="/docs/linux/man/1-dbus-monitor/">dbus-monitor</a>(1), <a href="/docs/linux/man/1-dbus-uuidgen/">dbus-uuidgen</a>(1) </p>
