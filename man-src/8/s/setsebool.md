---
title: "setsebool(8)"
name: "setsebool"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setsebool/"
description: "setsebool – set SELinux boolean value"
---

<p>setsebool &#8211; set SELinux boolean value </p>
<h2>Synopsis</h2>
<p><code>setsebool</code> <i>[ -PNV ] boolean value | bool1=val1 bool2=val2 &#8230;</i> </p>
<h2>Description</h2>
<p><code>setsebool </code> sets the current state of a particular SELinux boolean or a list of booleans to a given value. The value may be 1 or true or on to enable the boolean, or 0 or false or off to disable it. Without the -P option, only the current boolean value is affected; the boot-time default settings are not changed. If the -P option is given, all pending values are written to the policy file on disk. So they will be persistent across reboots. If the -N option is given, the policy on disk is not reloaded into the kernel. If the -V option is given, verbose error messages will be printed from semanage libraries. </p>
<h2>Author</h2>
<p>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;. The program was written by Tresys Technology.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-getsebool/">getsebool</a>(8), <a href="/docs/linux/man/8-booleans/">booleans</a>(8), <a href="/docs/linux/man/8-togglesebool/">togglesebool</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8) </p>
