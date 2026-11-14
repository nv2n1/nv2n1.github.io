---
title: "byobu-reconnect-sockets(1)"
name: "byobu-reconnect-sockets"
section: "1"
letter: "b"
url: "/docs/linux/man/1-byobu-reconnect-sockets/"
description: "byobu-reconnect-sockets – Sourcable script that updates GPG_AGENT_INFO and DBUS_SESSION_BUS_ADDRESS in the environment"
---

<h2>NAME</h2>
<p> byobu-reconnect-sockets &#8211; Sourcable script that updates GPG_AGENT_INFO and DBUS_SESSION_BUS_ADDRESS in the environment </p>
<h2>DESCRIPTION</h2>
<p> <code>byobu-reconnect-sockets</code> is a sourcable bit of shell code that will update the GPG_AGENT_INFO and DBUS_SESSION_BUS_ADDRESS environment variables in the current shell, such that you may restablish connection to <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1) and <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a>(1)</code>. </p>
<p> This is often useful when reattaching to a detached Byobu session. </p>
<dl>
<dt><i><a rel="nofollow" href="http://byobu.co">http://byobu.co</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage and the utility were written by Dustin Kirkland &lt;kirkland [at] byobu.co&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document and the utility under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> The complete text of the GNU General Public License can be found in <i>/usr/share/common-licenses/GPL</i> on Debian/Ubuntu systems, or in <i>/usr/share/doc/fedora-release-*/GPL</i> on Fedora systems, or on the web at <i><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.txt">http://www.gnu.org/licenses/gpl.txt</a></i>. </p>
<h2>Index</h2>
