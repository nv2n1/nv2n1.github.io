---
title: "postlogin(5)"
name: "postlogin"
section: "5"
letter: "p"
url: "/docs/linux/man/5-postlogin/"
description: "postlogin – Common configuration file for PAMified services"
---

<p>postlogin &#8211; Common configuration file for PAMified services </p>
<h2>Synopsis</h2>
<p><code>/etc/pam.d/postlogin</code> </p>
<h2>Description</h2>
<p>The purpose of this PAM configuration file is to provide a common place for all PAM modules which should be called after the stack configured in <code>system-auth</code> or the other common PAM configuration files. The <code>postlogin</code> configuration file is included from all individual service configuration files that provide login service with shell or file access. </p>
<h2>Notes</h2>
<p>The modules in the postlogin configuration file are executed regardless of the success or failure of the modules in the <code>system-auth</code> configuration file. </p>
<h2>Bugs</h2>
<p>Sometimes it would be useful to be able to skip the postlogin modules in case the substack of the <code>system-auth</code> modules failed. Unfortunately the current Linux-PAM library does not provide any way how to achieve this. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pam/">pam</a>(8), <a href="/docs/linux/man/5-config-util/">config-util</a>(5), <a href="/docs/linux/man/5-system-auth/">system-auth</a>(5) The three <code>Linux-PAM</code> Guides, for <code>system administrators</code>, <code>module developers</code>, and <code>application developers</code>. </p>
