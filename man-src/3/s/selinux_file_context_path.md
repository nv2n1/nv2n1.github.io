---
title: "selinux_file_context_path(3)"
name: "selinux_file_context_path"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_file_context_path/"
description: "selinux_path, selinux_policy_root, selinux_binary_policy_path, selinux_current_policy_path, selinux_failsafe_context_path, selinux_removable_context_path, selinux_default_context_path, selinux_user..."
---

<p>selinux_path, selinux_policy_root, selinux_binary_policy_path, selinux_current_policy_path, selinux_failsafe_context_path, selinux_removable_context_path, selinux_default_context_path, selinux_user_contexts_path, selinux_file_context_path, selinux_media_context_path, selinux_contexts_path &#8211; These functions return the paths to the active SELinux policy configuration directories and files</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;

const char *selinux_path(void);
const char *selinux_policy_root(void);
const char *selinux_binary_policy_path(void);
const char *selinux_current_policy_path(void);
const char *selinux_failsafe_context_path(void);
const char *selinux_removable_context_path(void);
const char *selinux_default_context_path(void);
const char *selinux_user_contexts_path(void);
const char *selinux_usersconf_path(void);
const char *selinux_x_context_path(void);
const char *selinux_sepgsql_context_path(void);
const char *selinux_file_context_path(void);
const char *selinux_media_context_path(void);
const char *selinux_securetty_types_path(void);
const char *selinux_contexts_path(void);</code></pre>
<h2>Description</h2>
<p>These functions return the paths to the active policy configuration directories and files based on the settings in <i>/etc/selinux/config</i>. </p>
<p> <code>selinux_path</code>() returns the top-level SELinux configuration directory. </p>
<p> <code>selinux_policy_root</code>() returns the top-level policy directory. </p>
<p> <code>selinux_binary_policy_path</code>() returns the binary policy file loaded into kernel. </p>
<p> <code>selinux_current_policy_path</code>() returns the currently loaded policy file from the kernel. </p>
<p> <code>selinux_default_type_path</code>() returns the context file mapping roles to default types. </p>
<p> <code>selinux_failsafe_context_path</code>() returns the failsafe context for emergency logins. </p>
<p> <code>selinux_removable_context_path</code>() returns the filesystem context for removable media. </p>
<p> <code>selinux_default_context_path</code>() returns the system-wide default contexts for user sessions. </p>
<p> <code>selinux_user_contexts_path</code>() returns the directory containing per-user default contexts. </p>
<p> <code>selinux_usersconf_path</code>() returns the file containing mapping between Linux Users and SELinux users. </p>
<p> <code>selinux_x_context_path</code>() returns the file containing configuration for XSELinux extension. </p>
<p> <code>selinux_sepgsql_context_path</code>() returns the file containing configuration for SE-PostgreSQL. </p>
<p> <code>selinux_netfilter_context_path</code>() returns the default netfilter context. </p>
<p> <code>selinux_file_context_path</code>() returns the default system file contexts configuration. </p>
<p> <code>selinux_file_context_local_path</code>() returns the local customization file contexts configuration. </p>
<p> <code>selinux_file_context_homedir_path</code>() returns the home directory file contexts configuration. </p>
<p> <code>selinux_media_context_path</code>() returns the file contexts for media device nodes. </p>
<p> <code>selinux_contexts_path</code>() returns the directory containing all of the context configuration files. </p>
<p> <code>selinux_securetty_types_path</code>() returns the defines tty types for newrole securettys.</p>
<h2>Author</h2>
<p>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
