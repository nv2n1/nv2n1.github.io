---
title: "usbguard-applet-qt(1)"
name: "usbguard-applet-qt"
section: "1"
letter: "u"
url: "/docs/linux/man/1-usbguard-applet-qt/"
---

<h2>NAME</h2>

 

 usbguard-applet-qt -- USBGuard Qt applet

<h2>SYNOPSIS</h2>

 

 usbguard-applet-qt

<h2>DESCRIPTION</h2>

 

 USBGuard Qt applet for interaction with the USBGuard daemon.

<h2>OPTIONS</h2>

 

 There are currently no options available.

<h2>SECURITY CONSIDERATIONS</h2>

 

 The applet uses the USBGuard public IPC interface to talk to the daemon component. Depending on your distribution defaults, the access to this interface is limited to a certain group or a specific user only. Please refer to the <a HREF="/docs/linux/man/5-usbguard-daemon-conf/">usbguard-daemon.conf</a>(5) man page for more information on how to configure the ACL correctly. Do not leave the ACL unconfigured as that will expose the IPC interface to all local users and will allow them to manipulate the authorization state of USB devices and modify the USBGuard policy.

<h2>BUGS</h2>

 

 If you find a bug in this software or if you'd like to request a feature to be implemented, please file a ticket at &lt;<a rel="nofollow" HREF="https://github.com/dkopecek/usbguard/issues/new">https://github.com/dkopecek/usbguard/issues/new</a>&gt;.

<h2>COPYRIGHT</h2>

 

 Copyright © 2015 Red Hat, Inc. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" HREF="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;. This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/8-usbguard-daemon/">usbguard-daemon</a>(8), <a HREF="/docs/linux/man/5-usbguard-daemon-conf/">usbguard-daemon.conf</a>(5)

<h2>AUTHORS</h2>

 Daniel Kopeček &lt;dkopecek [at] redhat.com&gt;. 

<h2>Index</h2>


