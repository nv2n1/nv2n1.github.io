---
title: "usbguard-dbus(8)"
name: "usbguard-dbus"
section: "8"
letter: "u"
url: "/docs/linux/man/8-usbguard-dbus/"
---

usbguard-dbus -- USBGuard D-Bus interface service

<h2>Synopsis</h2>

usbguard-dbus&nbsp;<wbr>[OPTIONS]

<h2>Description</h2>

The usbguard-dbus component exposes a D-Bus interface to a running instance of the <a HREF="/docs/linux/man/8-usbguard-daemon/">usbguard-daemon</a>(8).

<h2>Options</h2>

<dl><dt>-s, --system
<dd>Listen on the system bus.
<dl><dd></dl><dt>-S, --session
<dd>Listen on the session bus.
<dl><dd></dl><dt>-h, --help
<dd>Show the help/usage screen.
<dl><dd></dl></dl>

<h2>Bugs</h2>

If you find a bug in this software or if you'd like to request a feature to be implemented, please file a ticket at &lt;<a rel="nofollow" HREF="https://github.com/dkopecek/usbguard/issues/new">https://github.com/dkopecek/usbguard/issues/new</a>&gt;.

<h2>Copyright</h2>

Copyright © 2015 Red Hat, Inc. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" HREF="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;. This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-usbguard/">usbguard</a>(1), <a HREF="/docs/linux/man/1-usbguard-applet-qt/">usbguard-applet-qt</a>(1)

<h2>Authors</h2>

Daniel Kopeček &lt;dkopecek [at] redhat.com&gt;; Muri Nicanor &lt;muri [at] immerda.ch&gt;.
