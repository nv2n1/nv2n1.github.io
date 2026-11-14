---
title: "genhomedircon(8)"
name: "genhomedircon"
section: "8"
letter: "g"
url: "/docs/linux/man/8-genhomedircon/"
description: "genhomedircon – generate SELinux file context configuration entries for user home directories"
---

<p>genhomedircon &#8211; generate SELinux file context configuration entries for user home directories</p>
<h2>Description</h2>
<p><code>genhomedircon</code> is a script that executes <code>semodule</code> to rebuild the currently active SELinux policy (without reloading it) and to create the labels for each user home directory based on directory paths returned by calls to getpwent(). The latter functionality depends on the &quot;usepasswd&quot; parameter being set to &quot;true&quot; (default) in /etc/selinux/semanage.conf. This script is usually executed by <code>semanage</code> although this default behavior can be optionally modified by setting to &quot;true&quot; the &quot;disable-genhomedircon&quot; in /etc/selinux/semanage.conf. </p>
<h2>Author</h2>
<p>This manual page was written by <i>Dan Walsh &lt;dwalsh [at] redhat.com&gt;</i></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-semanage-conf/">semanage.conf</a>(5), <a href="/docs/linux/man/8-semodule/">semodule</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8), <a href="/docs/linux/man/3-getpwent/">getpwent</a>(3), <a href="/docs/linux/man/3-getpwent_r/">getpwent_r</a>(3) </p>
