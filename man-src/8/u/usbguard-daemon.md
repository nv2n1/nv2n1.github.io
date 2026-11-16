---
title: "usbguard-daemon(8)"
name: "usbguard-daemon"
section: "8"
letter: "u"
url: "/docs/linux/man/8-usbguard-daemon/"
---

usbguard-daemon -- USBGuard daemon

<h2>Synopsis</h2>

usbguard-daemon&nbsp;<wbr>[OPTIONS]

<h2>Description</h2>

The usbguard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in <a HREF="/docs/linux/man/5-usbguard-rules-conf/">usbguard-rules.conf</a>(5). The policy and the authorization state of USB devices can be modified during runtime using the <a HREF="/docs/linux/man/1-usbguard/">usbguard</a>(1) tool.

<h2>Options</h2>

<dl><dt>-d
</dt><dd>Enable debugging messages in the log.
</dd><dl><dd></dd></dl><dt>-s
</dt><dd>Log to syslog.
</dd><dl><dd></dd></dl><dt>-k
</dt><dd>Log to console.
</dd><dl><dd></dd></dl><dt>-l &lt;path&gt;
</dt><dd>Log to a file at path.
</dd><dl><dd></dd></dl><dt>-p &lt;path&gt;
</dt><dd>Write PID to a file at path.
</dd><dl><dd></dd></dl><dt>-c &lt;path&gt;
</dt><dd>Load configuration from a file at path (default: /etc/usbguard/usbguard-daemon.conf).
</dd><dl><dd></dd></dl><dt>-h
</dt><dd>Show the help/usage screen.
</dd><dl><dd></dd></dl></dl>

<h2>Security Considerations</h2>

The daemon provides the USBGuard public IPC interface. Depending on your distribution defaults, the access to this interface is limited to a certain group or a specific user only. Please refer to the <a HREF="/docs/linux/man/5-usbguard-daemon-conf/">usbguard-daemon.conf</a>(5) man page for more information on how to configure the ACL correctly. Do not leave the ACL unconfigured as that will expose the IPC interface to all local users and will allow them to manipulate the authorization state of USB devices and modify the USBGuard policy.

<h2>Bugs</h2>

If you find a bug in this software or if you'd like to request a feature to be implemented, please file a ticket at &lt;<a rel="nofollow" HREF="https://github.com/dkopecek/usbguard/issues/new">https://github.com/dkopecek/usbguard/issues/new</a>&gt;.

<h2>Copyright</h2>

Copyright © 2015 Red Hat, Inc. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" HREF="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;. This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-usbguard-daemon-conf/">usbguard-daemon.conf</a>(5), <a HREF="/docs/linux/man/5-usbguard-rules-conf/">usbguard-rules.conf</a>(5), <a HREF="/docs/linux/man/1-usbguard/">usbguard</a>(1), <a HREF="/docs/linux/man/1-usbguard-applet-qt/">usbguard-applet-qt</a>(1)

<h2>Authors</h2>

Daniel Kopeček &lt;dkopecek [at] redhat.com&gt;.
