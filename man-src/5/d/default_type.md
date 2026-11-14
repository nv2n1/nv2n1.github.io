---
title: "default_type(5)"
name: "default_type"
section: "5"
letter: "d"
url: "/docs/linux/man/5-default_type/"
description: "default_type – The SELinux default type configuration file"
---

<p>default_type &#8211; The SELinux default type configuration file</p>
<h2>Description</h2>
<p>The <i>default_type</i> file contains entries that allow SELinux-aware applications such as <code><a href="/docs/linux/man/1-newrole/">newrole</a></code>(1) to select a default type for a role if one is not supplied. </p>
<p> <code><a href="/docs/linux/man/3-selinux_default_type_path/">selinux_default_type_path</a></code>(3) will return the active policy path to this file. The default, default type file is:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/contexts/default_type</i></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)). </p>
<p> <code><a href="/docs/linux/man/3-get_default_type/">get_default_type</a></code>(3) reads this file to determine a type for the active policy.</p>
<h2>File Format</h2>
<p>Each line within the <i>default_type</i> file is formatted with <i>role</i><code>:</code><i>type</i> entries where:</p>
<dl>
<dd><i>role</i></p>
<dl>
<dd>The SELinux role.</dl>
<p> <i>type</i></p>
<dl>
<dd>The domain type that is returned for this role.</dl>
</dl>
<h2>Example</h2>
<p># ./contexts/default_type<br />
 auditadm_r:auditadm_t<br />
 user_r:user_t</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-get_default_type/">get_default_type</a></code>(3), <code><a href="/docs/linux/man/1-newrole/">newrole</a></code>(1), <code><a href="/docs/linux/man/3-selinux_default_type_path/">selinux_default_type_path</a></code>(3), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5) </p>
