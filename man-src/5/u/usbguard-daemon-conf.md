---
title: "usbguard-daemon-conf(5)"
name: "usbguard-daemon-conf"
section: "5"
letter: "u"
url: "/docs/linux/man/5-usbguard-daemon-conf/"
---

usbguard-daemon.conf -- USBGuard daemon configuration file

<h2>Description</h2>

The usbguard-daemon.conf file is loaded by the USBGuard daemon after it parses its command-line options and is used to configure runtime parameters of the daemon. The default search path is /etc/usbguard/usbguard-daemon.conf. It may be overridden using the -c command-line option, see <a HREF="/docs/linux/man/8-usbguard-daemon/">usbguard-daemon</a>(8) for further details.

<h2>Options</h2>

<dl><dt>RuleFile=&lt;path&gt;
<dd>The USBGuard daemon will use this file to load the policy rule set from it and to write new rules received via the IPC interface.
<dl><dd></dl><dt>IPCAllowedUsers=&lt;username&gt;&nbsp;<wbr>[&lt;username&gt;&nbsp;<wbr>...]
<dd>A space delimited list of usernames that the daemon will accept IPC connections from.
<dl><dd></dl><dt>IPCAllowedGroups=&lt;groupname&gt;&nbsp;<wbr>[&lt;groupname&gt;&nbsp;<wbr>...]
<dd>A space delimited list of groupnames that the daemon will accept IPC connections from.
<dl><dd></dl></dl>

<h2>Security Considerations</h2>

The daemon provides the USBGuard public IPC interface. Depending on your distribution defaults, the access to this interface is limited to a certain group or a specific user only. Please set either the IPCAllowedUsers or IPCAllowedGroups options to limit access to the IPC interface. Do not leave the ACL unconfigured as that will expose the IPC interface to all local users and will allow them to manipulate the authorization state of USB devices and modify the USBGuard policy.

<h2>Bugs</h2>

If you find a bug in this software or if you'd like to request a feature to be implemented, please file a ticket at &lt;<a rel="nofollow" HREF="https://github.com/dkopecek/usbguard/issues/new">https://github.com/dkopecek/usbguard/issues/new</a>&gt;.

<h2>Copyright</h2>

Copyright © 2015 Red Hat, Inc. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" HREF="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;. This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-usbguard-daemon/">usbguard-daemon</a>(8), <a HREF="/docs/linux/man/5-usbguard-rules-conf/">usbguard-rules.conf</a>(5)

<h2>Authors</h2>

Daniel Kopeček &lt;dkopecek [at] redhat.com&gt;.
