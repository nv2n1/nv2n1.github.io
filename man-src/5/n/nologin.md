---
title: "nologin(5)"
name: "nologin"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nologin/"
description: "nologin – prevent unprivileged users from logging into the system"
---

<p>nologin &#8211; prevent unprivileged users from logging into the system</p>
<h2>Description</h2>
<p>If the file <i>/etc/nologin</i> exists and is readable, <code><a href="/docs/linux/man/1-login/">login</a></code>(1) will allow access only to root. Other users will be shown the contents of this file and their logins will be refused. This provides a simple way of temporarily disabling all unprivileged logins.</p>
<h2>Files</h2>
<p><i>/etc/nologin</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
