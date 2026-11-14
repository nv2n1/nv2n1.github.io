---
title: "failsafe_context(5)"
name: "failsafe_context"
section: "5"
letter: "f"
url: "/docs/linux/man/5-failsafe_context/"
description: "failsafe_context – The SELinux fail safe context configuration file"
---

<p>failsafe_context &#8211; The SELinux fail safe context configuration file</p>
<h2>Description</h2>
<p>The <i>failsafe_context</i> file allows SELinux-aware applications such as <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8) to obtain a known valid login context for an administrator if no valid default entries can be found elsewhere. </p>
<p> <code><a href="/docs/linux/man/3-selinux_failsafe_context_path/">selinux_failsafe_context_path</a></code>(3) will return the active policy path to this file. The default failsafe context file is:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/contexts/failsafe_context</i></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)). </p>
<p> The following functions read this file from the active policy path if they cannot obtain a default context: </p>
<dl>
<dd><code><a href="/docs/linux/man/3-get_default_context/">get_default_context</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-get_ordered_context_list/">get_ordered_context_list</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-get_ordered_context_list_with_level/">get_ordered_context_list_with_level</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-get_default_context_with_level/">get_default_context_with_level</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-get_default_context_with_role/">get_default_context_with_role</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-get_default_context_with_rolelevel/">get_default_context_with_rolelevel</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-query_user_context/">query_user_context</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-manual_user_enter_context/">manual_user_enter_context</a></code>(3)</dl>
<h2>File Format</h2>
<p>The file consists of a single line entry as follows:</p>
<dl>
<dd><i>role</i><code>:</code><i>type</i>[<code>:</code><i>range</i>]</dl>
<p> Where:</p>
<dl>
<dd><i>role</i> <i>type</i> <i>range</i></p>
<dl>
<dd>A role, type and optional range (for MCS/MLS), separated by colons (:) to form a valid login process context for an administrator to access the system.</dl>
</dl>
<h2>Example</h2>
<p># ./contexts/failsafe_context<br />
 unconfined_r:unconfined_t:s0</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-selinux_failsafe_context_path/">selinux_failsafe_context_path</a></code>(3), <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8), <code><a href="/docs/linux/man/3-selinux_default_type_path/">selinux_default_type_path</a></code>(3), <code><a href="/docs/linux/man/3-get_default_context/">get_default_context</a></code>(3), <code><a href="/docs/linux/man/3-get_ordered_context_list/">get_ordered_context_list</a></code>(3), <code><a href="/docs/linux/man/3-get_ordered_context_list_with_level/">get_ordered_context_list_with_level</a></code>(3), <code><a href="/docs/linux/man/3-get_default_context_with_level/">get_default_context_with_level</a></code>(3), <code><a href="/docs/linux/man/3-get_default_context_with_role/">get_default_context_with_role</a></code>(3), <code><a href="/docs/linux/man/3-get_default_context_with_rolelevel/">get_default_context_with_rolelevel</a></code>(3), <code><a href="/docs/linux/man/3-query_user_context/">query_user_context</a></code>(3), <code><a href="/docs/linux/man/3-manual_user_enter_context/">manual_user_enter_context</a></code>(3), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5) </p>
