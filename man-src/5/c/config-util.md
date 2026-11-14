---
title: "config-util(5)"
name: "config-util"
section: "5"
letter: "c"
url: "/docs/linux/man/5-config-util/"
description: "config-util – Common PAM configuration file for configuration utilities"
---

<p>config-util &#8211; Common PAM configuration file for configuration utilities </p>
<h2>Synopsis</h2>
<p><code>/etc/pam.d/config-util</code> </p>
<h2>Description</h2>
<p>The purpose of this configuration file is to provide common configuration file for all configuration utilities which must be run from the supervisor account and use the userhelper wrapper application. The <code>config-util</code> configuration file is included from all individual configuration files of such utilities with the help of the <code>include</code> directive. There are not usually any other modules in the individual configuration files of these utilities. It is possible for example to modify duration of the validity of the authentication timestamp there. See <code><a href="/docs/linux/man/8-pam_timestamp/">pam_timestamp</a>(8)</code> for details. </p>
<h2>Bugs</h2>
<p>None known. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pam/">pam</a>(8), <a href="/docs/linux/man/5-config-util/">config-util</a>(5), <a href="/docs/linux/man/8-pam_timestamp/">pam_timestamp</a>(8) </p>
