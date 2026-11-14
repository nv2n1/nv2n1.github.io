---
title: "seusers(5)"
name: "seusers"
section: "5"
letter: "s"
url: "/docs/linux/man/5-seusers/"
description: "seusers – The SELinux GNU/Linux user to SELinux user mapping configuration file"
---

<p>seusers &#8211; The SELinux GNU/Linux user to SELinux user mapping configuration file</p>
<h2>Description</h2>
<p>The <i>seusers</i> file contains a list GNU/Linux user to SELinux user mapping for use by SELinux-aware login applications such as <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8). </p>
<p> <code><a href="/docs/linux/man/3-selinux_usersconf_path/">selinux_usersconf_path</a></code>(3) will return the active policy path to this file. The default SELinux users mapping file is located at:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/seusers</i></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)). </p>
<p> <code><a href="/docs/linux/man/3-getseuserbyname/">getseuserbyname</a></code>(3) reads this file to map a GNU/Linux user or group to an SELinux user.</p>
<h2>File Format</h2>
<p>Each line of the <i>seusers</i> configuration file consists of the following: </p>
<dl>
<dd>[<code>%</code><i>group_id</i>]|[<i>user_id</i>]<code>:</code><i>seuser_id</i>[<code>:</code><i>range</i>]</dl>
<p> Where:</p>
<dl>
<dd><i>group_id</i>|<i>user_id</p>
<dl>
<dd></i>The GNU/Linux user id, or if preceded by the percentage (<code>%</code>) symbol, then a GNU/Linux group id.<br />
 An optional entry set to <code>__default__</code> can be provided as a fall back if required.</dl>
<p> <i>seuser_id</i></p>
<dl>
<dd>The SELinux user identity.</dl>
<p> <i>range</i></p>
<dl>
<dd>The optional level or range for an MLS/MCS policy.</dl>
</dl>
<h2>Example</h2>
<p># ./seusers<br />
 system_u:system_u:s0-s15:c0.c255<br />
 root:root:s0-s15:c0.c255<br />
 fred:user_u:s0<br />
 __default__:user_u:s0<br />
 %user_group:user_u:s0</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8), <code><a href="/docs/linux/man/3-selinux_usersconf_path/">selinux_usersconf_path</a></code>(3), <code><a href="/docs/linux/man/3-getseuserbyname/">getseuserbyname</a></code>(3), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5) </p>
