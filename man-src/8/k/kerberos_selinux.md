---
title: "kerberos_selinux(8)"
name: "kerberos_selinux"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kerberos_selinux/"
---

kerberos_selinux - Security Enhanced Linux Policy for Kerberos.

<h2>Description</h2>

Security-Enhanced Linux secures the system via flexible mandatory access control. SELinux policy can be configured to deny Kerberos access to confined applications, since it requires daemons to be allowed greater access to certain secure files and additional access to the network.

<h2>Booleans</h2>

You must set the allow_kerberos boolean to allow your system to work properly in a Kerberos environment. <pre>setsebool -P allow_kerberos 1</pre>system-config-selinux is a GUI tool available to customize SELinux policy settings.

<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>

This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-selinux/">selinux</a>(8), <a HREF="/docs/linux/man/1-kerberos/">kerberos</a>(1), <a HREF="/docs/linux/man/1-chcon/">chcon</a>(1), <a HREF="/docs/linux/man/8-setsebool/">setsebool</a>(8) 
