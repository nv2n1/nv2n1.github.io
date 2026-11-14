---
title: "securetty(5)"
name: "securetty"
section: "5"
letter: "s"
url: "/docs/linux/man/5-securetty/"
description: "securetty – list of terminals on which root is allowed to login"
---

<p>securetty &#8211; list of terminals on which root is allowed to login</p>
<h2>Description</h2>
<p>The file <i>/etc/securetty</i> contains the names of terminals (one per line, without leading <i>/dev/</i>) which are considered secure for the transmission of certain authentication tokens. </p>
<p> It is used by (some versions of) <code><a href="/docs/linux/man/1-login/">login</a></code>(1) to restrict the terminals on which root is allowed to login. See <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5) if you use the shadow suite. </p>
<p> On PAM enabled systems, it is used for the same purpose by <code><a href="/docs/linux/man/8-pam_securetty/">pam_securetty</a></code>(8) to restrict the terminals on which empty passwords are accepted.</p>
<h2>Files</h2>
<p><i>/etc/securetty</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/8-pam_securetty/">pam_securetty</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
