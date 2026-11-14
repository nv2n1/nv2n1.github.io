---
title: "booleans(8)"
name: "booleans"
section: "8"
letter: "b"
url: "/docs/linux/man/8-booleans/"
description: "booleans – Policy booleans enable runtime customization of SELinux policy"
---

<p>booleans &#8211; Policy booleans enable runtime customization of SELinux policy</p>
<h2>Description</h2>
<p>This manual page describes SELinux policy booleans. The SELinux policy can include conditional rules that are enabled or disabled based on the current values of a set of policy booleans. These policy booleans allow runtime modification of the security policy without having to load a new policy. </p>
<p> For example, the boolean httpd_enable_cgi allows the httpd daemon to run cgi scripts if it is enabled. If the administrator does not want to allow execution of cgi scripts, he can simply disable this boolean value. </p>
<p> The policy defines a default value for each boolean, typically false. These default values can be overridden via local settings created via the <code><a href="/docs/linux/man/8-setsebool/">setsebool</a></code>(8) utility, using <code>-P</code> to make the setting persistent across reboots. The <code>system-config-securitylevel</code> tool provides a graphical interface for altering the settings. The <code><a href="/docs/linux/man/8-load_policy/">load_policy</a></code>(8) program will preserve current boolean settings upon a policy reload by default, or can optionally reset booleans to the boot-time defaults via the <code>-b</code> option. </p>
<p> Boolean values can be listed by using the <code><a href="/docs/linux/man/8-getsebool/">getsebool</a></code>(8) utility and passing it the <code>-a</code> option. </p>
<p> Boolean values can also be changed at runtime via the <code><a href="/docs/linux/man/8-setsebool/">setsebool</a></code>(8) utility or the <code><a href="/docs/linux/man/8-togglesebool/">togglesebool</a></code>(8) utility. By default, these utilities only change the current boolean value and do not affect the persistent settings, unless the <code>-P</code> option is used to setsebool.</p>
<h2>Author</h2>
<p>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;. The SELinux conditional policy support was developed by Tresys Technology.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-getsebool/">getsebool</a></code>(8), <code><a href="/docs/linux/man/8-setsebool/">setsebool</a></code>(8), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-togglesebool/">togglesebool</a></code>(8) </p>
