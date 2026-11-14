---
title: "system-config-authentication(8)"
name: "system-config-authentication"
section: "8"
letter: "s"
url: "/docs/linux/man/8-system-config-authentication/"
description: "authconfig-gtk, system-config-authentication – GUI utility for configuring user identity and system authentication services"
---

<p>authconfig-gtk, system-config-authentication &#8211; GUI utility for configuring user identity and system authentication services</p>
<h2>Synopsis</h2>
<p><code>authconfig-gtk</code> [&#8211;nox] [&#8211;updateall] [&#8211;firstboot]</p>
<h2>Description</h2>
<p><code>authconfig-gtk</code> provides a simple graphical user interface for configuring user identity and system authentication services. It provides basic configuration options to handle NIS, LDAP, Kerberos 5, and Winbind client configuration. </p>
<h2>Options</h2>
<p>If the <code>&#8211;nox</code> option is specified, <code>authconfig</code> command line utility is run instead of the GUI. </p>
<p> The <code>&#8211;updateall</code> option forces overwriting of all configuration files not only the files affected by the changes made in the user interaction with the GUI. This option can be useful in case the configuration files are broken by manual editing. </p>
<p> The <code>&#8211;firstboot</code> option is to be used only when <i>firstboot</i> utility runs the GUI during the first setup of the system after installation.</p>
<h2>Return Codes</h2>
<p><code>authconfig-gtk</code> returns 0 on success, non zero on error.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-authconfig/">authconfig</a>(8), <a href="/docs/linux/man/5-system-auth-ac/">system-auth-ac</a>(5) </p>
<h2>Authors</h2>
<pre>Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;, Preston Brown &lt;pbrown [at] redhat.com&gt;,
Matt Wilson &lt;msw [at] redhat.com&gt;, Tomas Mraz &lt;tmraz [at] redhat.com&gt;</pre>
