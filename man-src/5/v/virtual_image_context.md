---
title: "virtual_image_context(5)"
name: "virtual_image_context"
section: "5"
letter: "v"
url: "/docs/linux/man/5-virtual_image_context/"
description: "virtual_image_context – The SELinux virtual machine image context configuration file"
---

<p>virtual_image_context &#8211; The SELinux virtual machine image context configuration file</p>
<h2>Description</h2>
<p>The <i>virtual_image_context</i> file contains a list of image contexts for use by the SELinux-aware virtulization API libvirt (see <code><a href="/docs/linux/man/8-libvirtd/">libvirtd</a></code>(8)). </p>
<p> <code><a href="/docs/linux/man/3-selinux_virtual_image_context_path/">selinux_virtual_image_context_path</a></code>(3) will return the active policy path to this file. The default virtual image context file is:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/contexts/virtual_image_context</i></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)).</p>
<h2>File Format</h2>
<p>Each line in the file consists of an entry as follows:</p>
<dl>
<dd><i>user</i><code>:</code><i>role</i><code>:</code><i>type</i>[<code>:</code><i>range</i>]</dl>
<p> Where:</p>
<dl>
<dd><i>user role type range</i></p>
<dl>
<dd>A user, role, type and optional range (for MCS/MLS) separated by colons (:) that can be used as a virtual image context.</dl>
</dl>
<h2>Example</h2>
<p># ./contexts/virtual_image_context<br />
 system_u:object_r:svirt_image_t:s0<br />
 system_u:object_r:svirt_content_t:s0</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-libvirtd/">libvirtd</a></code>(8), <code><a href="/docs/linux/man/3-selinux_virtual_image_context_path/">selinux_virtual_image_context_path</a></code>(3), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5) </p>
