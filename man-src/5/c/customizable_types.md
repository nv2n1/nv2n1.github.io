---
title: "customizable_types(5)"
name: "customizable_types"
section: "5"
letter: "c"
url: "/docs/linux/man/5-customizable_types/"
description: "customizable_types – The SELinux customizable types configuration file"
---

<p>customizable_types &#8211; The SELinux customizable types configuration file</p>
<h2>Description</h2>
<p>The <i>customizable_types</i> file contains a list of types that can be customised in some way by SELinux-aware applications. </p>
<p> Generally this is a file context type that is usually set on files that need to be shared among certain domains and where the administrator wants to manually manage the type. </p>
<p> The use of customizable types is deprecated as the preferred approach is to use <code><a href="/docs/linux/man/8-semanage/">semanage</a></code>(8) <code><a href="/docs/linux/man/8-fcontext/">fcontext</a></code>(8) <code>&#8230;</code>(8). However, SELinux-aware applications such as <code><a href="/docs/linux/man/8-setfiles/">setfiles</a></code>(8) will use this information to obtain a list of types relating to files that should not be relabeled. </p>
<p> <code><a href="/docs/linux/man/3-selinux_customizable_types_path/">selinux_customizable_types_path</a></code>(3) will return the active policy path to this file. The default customizable types file is:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/contexts/customizable_types</i></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)). </p>
<p> <code><a href="/docs/linux/man/3-is_context_customizable/">is_context_customizable</a></code>(3) reads this file to determine if a context is customisable or not for the active policy.</p>
<h2>File Format</h2>
<p>Each line in the file consists of the following:</p>
<dl>
<dd><i>type</i></dl>
<p> Where:</p>
<dl>
<dd><i>type</i></p>
<dl>
<dd>The type defined in the policy that can be customised.</dl>
</dl>
<h2>Example</h2>
<p># ./contexts/customizable_types<br />
 mount_loopback_t<br />
 public_content_rw_t<br />
 public_content_t<br />
 swapfile_t<br />
 sysadm_untrusted_content_t</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-selinux_customizable_types_path/">selinux_customizable_types_path</a></code>(3), <code><a href="/docs/linux/man/3-is_context_customizable/">is_context_customizable</a></code>(3), <code><a href="/docs/linux/man/8-semanage/">semanage</a></code>(8), <code><a href="/docs/linux/man/8-setfiles/">setfiles</a></code>(8), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5) </p>
