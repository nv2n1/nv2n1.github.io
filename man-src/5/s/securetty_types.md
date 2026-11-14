---
title: "securetty_types(5)"
name: "securetty_types"
section: "5"
letter: "s"
url: "/docs/linux/man/5-securetty_types/"
description: "securetty_types – The SELinux secure tty type configuration file"
---

<p>securetty_types &#8211; The SELinux secure tty type configuration file</p>
<h2>Description</h2>
<p>The <i>securetty_types</i> file contains a list of types associated to secure tty type that are defined in the policy for use by SELinux-aware applications. </p>
<p> <code><a href="/docs/linux/man/3-selinux_securetty_types_path/">selinux_securetty_types_path</a></code>(3) will return the active policy path to this file. The default securetty types file is:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/contexts/securetty_types</i></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)). </p>
<p> <code><a href="/docs/linux/man/3-selinux_check_securetty_context/">selinux_check_securetty_context</a></code>(3) reads this file to determine if a context is for a secure tty defined in the active policy. </p>
<p> SELinux-aware applications such as <code><a href="/docs/linux/man/1-newrole/">newrole</a></code>(1) use this information to check the status of a tty.</p>
<h2>File Format</h2>
<p>Each line in the file consists of the following entry: </p>
<dl>
<dd><i>type</i></p>
<dl>
<dd>One or more type entries that are defined in the policy for secure tty devices.</dl>
</dl>
<h2>Example</h2>
<p># ./contexts/securetty_types<br />
 sysadm_tty_device_t<br />
 user_tty_device_t<br />
 staff_tty_device_t</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-selinux_securetty_types_path/">selinux_securetty_types_path</a></code>(3), <code><a href="/docs/linux/man/1-newrole/">newrole</a></code>(1), <code><a href="/docs/linux/man/3-selinux_check_securetty_context/">selinux_check_securetty_context</a></code>(3), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5) </p>
