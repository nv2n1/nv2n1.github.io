---
title: "default_contexts(5)"
name: "default_contexts"
section: "5"
letter: "d"
url: "/docs/linux/man/5-default_contexts/"
description: "default_contexts – The SELinux default contexts configuration file"
---

<p>default_contexts &#8211; The SELinux default contexts configuration file</p>
<h2>Description</h2>
<p>The default contexts configuration file <i>default_contexts</i> contains entries that allow SELinux-aware login applications such as <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8) </p>
<p> SELinux-aware login applications generally use one or more of the following libselinux functions that read these files from the active policy path:</p>
<dl>
<dd><code><a href="/docs/linux/man/3-get_default_context/">get_default_context</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-get_ordered_context_list/">get_ordered_context_list</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-get_ordered_context_list_with_level/">get_ordered_context_list_with_level</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-get_default_context_with_level/">get_default_context_with_level</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-get_default_context_with_role/">get_default_context_with_role</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-get_default_context_with_rolelevel/">get_default_context_with_rolelevel</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-query_user_context/">query_user_context</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-manual_user_enter_context/">manual_user_enter_context</a></code>(3)</dl>
<p> The default context configuration file path for the active policy is returned by <code><a href="/docs/linux/man/3-selinux_default_contexts_path/">selinux_default_contexts_path</a></code>(3). The default, default contexts file is:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/contexts/default_contexts</i></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)).</p>
<h2>File Format</h2>
<p>Each line in the default configuration file consists of the following:</p>
<dl>
<dd><i>login_process user_login_process [user_login_process] &#8230;</i></dl>
<p> Where:</p>
<dl>
<dd><i>login_process</i></p>
<dl>
<dd>This consists of a <i>role</i><code>:</code><i>type</i>[<code>:</code><i>range</i>] entry that represents the login process context that are defined in the policy.</dl>
<p> <i>user_login_process</i></p>
<dl>
<dd>This consists of one or more <i>role</i><code>:</code><i>type</i>[<code>:</code><i>range</i>] entries that represent the user login process context defined in the policy.</dl>
</dl>
<h2>Example</h2>
<p># ./contexts/default_contexts<br />
 system_r:crond_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> system_r:system_crond_t:s0</p>
<p> system_r:local_login_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> user_r:user_t:s0 staff_r:staff_t:s0</p>
<p> system_r:remote_login_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> user_r:user_t:s0</p>
<p> system_r:sshd_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> user_r:user_t:s0</p>
<p> system_r:sulogin_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> sysadm_r:sysadm_t:s0</p>
<p> system_r:xdm_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> user_r:user_t:s0</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-selinux_default_contexts_path/">selinux_default_contexts_path</a></code>(3), <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8), <code><a href="/docs/linux/man/3-selinux_default_type_path/">selinux_default_type_path</a></code>(3), <code><a href="/docs/linux/man/3-get_default_context/">get_default_context</a></code>(3), <code><a href="/docs/linux/man/3-get_ordered_context_list/">get_ordered_context_list</a></code>(3), <code><a href="/docs/linux/man/3-get_ordered_context_list_with_level/">get_ordered_context_list_with_level</a></code>(3), <code><a href="/docs/linux/man/3-get_default_context_with_level/">get_default_context_with_level</a></code>(3), <code><a href="/docs/linux/man/3-get_default_context_with_role/">get_default_context_with_role</a></code>(3), <code><a href="/docs/linux/man/3-get_default_context_with_rolelevel/">get_default_context_with_rolelevel</a></code>(3), <code><a href="/docs/linux/man/3-query_user_context/">query_user_context</a></code>(3), <code><a href="/docs/linux/man/3-manual_user_enter_context/">manual_user_enter_context</a></code>(3), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5) </p>
