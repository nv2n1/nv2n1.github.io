---
title: "system-auth(5)"
name: "system-auth"
section: "5"
letter: "s"
url: "/docs/linux/man/5-system-auth/"
description: "system-auth – Common configuration file for PAMified services"
---

<p>system-auth &#8211; Common configuration file for PAMified services </p>
<h2>Synopsis</h2>
<p><code>/etc/pam.d/system-auth</code> <code>/etc/pam.d/password-auth</code> <code>/etc/pam.d/fingerprint-auth</code> <code>/etc/pam.d/smartcard-auth</code> </p>
<h2>Description</h2>
<p>The purpose of these configuration files are to provide a common interface for all applications and service daemons calling into the PAM library. The <code>system-auth</code> configuration file is included from nearly all individual service configuration files with the help of the <code>substack</code> directive. The <code>password-auth</code> <code>fingerprint-auth</code> <code>smartcard-auth</code> configuration files are for applications which handle authentication from different types of devices via simultaneously running individual conversations instead of one aggregate conversation. </p>
<h2>Notes</h2>
<p>Previously these common configuration files were included with the help of the <code>include</code> directive. This limited the use of the different action types of modules. With the use of <code>substack</code> directive to include these common configuration files this limitation no longer applies. </p>
<h2>Bugs</h2>
<p>None known. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pam/">pam</a>(8), <a href="/docs/linux/man/5-config-util/">config-util</a>(5), <a href="/docs/linux/man/5-postlogin/">postlogin</a>(5) The three <code>Linux-PAM</code> Guides, for <code>system administrators</code>, <code>module developers</code>, and <code>application developers</code>. </p>
