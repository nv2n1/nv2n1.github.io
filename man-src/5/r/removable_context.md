---
title: "removable_context(5)"
name: "removable_context"
section: "5"
letter: "r"
url: "/docs/linux/man/5-removable_context/"
description: "removable_context – The SELinux removable devices context configuration file"
---

<p>removable_context &#8211; The SELinux removable devices context configuration file</p>
<h2>Description</h2>
<p>This file contains the default label that should be used for removable devices that are not defined in the <i>media</i> file (that is described in <code><a href="/docs/linux/man/5-selabel_media/">selabel_media</a></code>(5)). </p>
<p> <code><a href="/docs/linux/man/3-selinux_removable_context_path/">selinux_removable_context_path</a></code>(3) will return the active policy path to this file. The default removable context file is:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/contexts/removable_context</i></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)).</p>
<h2>File Format</h2>
<p>The file consists of a single line entry as follows:</p>
<dl>
<dd><i>user</i><code>:</code><i>role</i><code>:</code><i>type</i>[<code>:</code><i>range</i>]</dl>
<p> Where:</p>
<dl>
<dd><i>user role type range</i></p>
<dl>
<dd>A user, role, type and optional range (for MCS/MLS) separated by colons (:) that will be applied to removable devices.</dl>
</dl>
<h2>Example</h2>
<p># ./contexts/removable_contexts<br />
 system_u:object_r:removable_t:s0</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-selinux_removable_context_path/">selinux_removable_context_path</a></code>(3), <code><a href="/docs/linux/man/5-selabel_media/">selabel_media</a></code>(5), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5) </p>
