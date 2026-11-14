---
title: "user_contexts(5)"
name: "user_contexts"
section: "5"
letter: "u"
url: "/docs/linux/man/5-user_contexts/"
description: "user_contexts – The SELinux user contexts configuration files"
---

<p>user_contexts &#8211; The SELinux user contexts configuration files</p>
<h2>Description</h2>
<p>These optional user context configuration files contain entries that allow SELinux-aware login applications such as <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8) (running in their own process context), to determine the context that a users login session should run under. </p>
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
<p> There can be one file for each SELinux user configured on the system. The file path is formed using the path returned by <code><a href="/docs/linux/man/3-selinux_user_contexts_path/">selinux_user_contexts_path</a></code>(3) for the active policy, with the SELinux user name appended, for example:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/contexts/users/unconfined_u</i><br />
 <i>/etc/selinux/{SELINUXTYPE}/contexts/users/xguest_u</i></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)). </p>
<p> These files contain context information as described in the <code>FILE FORMAT</code> section.</p>
<h2>File Format</h2>
<p>Each line in the user context configuration file consists of the following:</p>
<dl>
<dd><i>login_process user_login_process</i></dl>
<p> Where:</p>
<dl>
<dd><i>login_process</i></p>
<dl>
<dd>This consists of a <i>role</i><code>:</code><i>type</i>[<code>:</code><i>range</i>] entry that represents the login process context.</dl>
<p> <i>user_login_process</i></p>
<dl>
<dd>This consists of a <i>role</i><code>:</code><i>type</i>[<code>:</code><i>range</i>] entry that represents the user login process context.</dl>
</dl>
<h2>Example</h2>
<p># Example for xguest_u at /etc/selinux/targeted/contexts/users/xguest_u<br />
 system_r:crond_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>xguest_r:xguest_t:s0</p>
<p> system_r:initrc_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>xguest_r:xguest_t:s0</p>
<p> system_r:local_login_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>xguest_r:xguest_t:s0</p>
<p> system_r:remote_login_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>xguest_r:xguest_t:s0</p>
<p> system_r:sshd_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>xguest_r:xguest_t:s0</p>
<p> system_r:xdm_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>xguest_r:xguest_t:s0</p>
<p> xguest_r:xguest_t:s0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>xguest_r:xguest_t:s0</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-selinux_user_contexts_path/">selinux_user_contexts_path</a></code>(3), <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8), <code><a href="/docs/linux/man/3-get_ordered_context_list/">get_ordered_context_list</a></code>(3), <code><a href="/docs/linux/man/3-get_ordered_context_list_with_level/">get_ordered_context_list_with_level</a></code>(3), <code><a href="/docs/linux/man/3-get_default_context_with_level/">get_default_context_with_level</a></code>(3), <code><a href="/docs/linux/man/3-get_default_context_with_role/">get_default_context_with_role</a></code>(3), <code><a href="/docs/linux/man/3-get_default_context_with_rolelevel/">get_default_context_with_rolelevel</a></code>(3), <code><a href="/docs/linux/man/3-query_user_context/">query_user_context</a></code>(3), <code><a href="/docs/linux/man/3-manual_user_enter_context/">manual_user_enter_context</a></code>(3), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5) </p>
