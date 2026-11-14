---
title: "clamd_selinux(8)"
name: "clamd_selinux"
section: "8"
letter: "c"
url: "/docs/linux/man/8-clamd_selinux/"
description: "clamd_selinux – Security Enhanced Linux Policy for the clamd processes"
---

<p>clamd_selinux &#8211; Security Enhanced Linux Policy for the clamd processes</p>
<h2>Description</h2>
<p>clamd_t SELinux domain type is now associated with antivirus domain type (antivirus_t). Please see <code>antivirus_selinux </code> man page for more details. </p>
<h2>Commands</h2>
<p><code>semanage fcontext</code> can also be used to manipulate default file context mappings. </p>
<p> <code>semanage permissive</code> can also be used to manipulate whether or not a process type is permissive. </p>
<p> <code>semanage module</code> can also be used to enable/disable/install/remove policy modules. </p>
<p> <code>system-config-selinux</code> is a GUI tool available to customize SELinux policy settings.</p>
<h2>Author</h2>
<p>This manual page was auto-generated using <code>sepolicy manpage.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-antivirus/">antivirus</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/8-restorecon/">restorecon</a>(8), <a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8) </p>
