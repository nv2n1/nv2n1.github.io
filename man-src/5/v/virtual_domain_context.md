---
title: "virtual_domain_context(5)"
name: "virtual_domain_context"
section: "5"
letter: "v"
url: "/docs/linux/man/5-virtual_domain_context/"
description: "virtual_domain_context – The SELinux virtual machine domain context configuration file"
---

<p>virtual_domain_context &#8211; The SELinux virtual machine domain context configuration file</p>
<h2>Description</h2>
<p>The <i>virtual_domain_context</i> file contains a list of domain contexts that are available for use by the SELinux-aware virtulization API libvirt (see <code><a href="/docs/linux/man/8-libvirtd/">libvirtd</a></code>(8)). </p>
<p> <code>selinux_virtual_domain_context_path</code>(3) will return the active policy path to this file. The default virtual domain context file is:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/contexts/virtual_domain_context</i></dd></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)).</p>
<h2>File Format</h2>
<p>Each line in the file consists of an entry as follows:</p>
<dl>
<dd><i>user</i><code>:</code><i>role</i><code>:</code><i>type</i>[<code>:</code><i>range</i>]</dd></dl>
<p> Where:</p>
<dl>
<dd><i>user role type range</i></dd>
<dl>
<dd>A user, role, type and optional range (for MCS/MLS) separated by colons (:) that can be used as a virtual domain context.</dd></dl>
</dl>
<h2>Example</h2>
<p># ./contexts/virtual_domain_context<br />
 system_u:object_r:svirt_t:s0</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-libvirtd/">libvirtd</a></code>(8), <code>selinux_virtual_domain_context_path</code>(3), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5) </p>
