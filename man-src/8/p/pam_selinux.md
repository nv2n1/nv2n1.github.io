---
title: "pam_selinux(8)"
name: "pam_selinux"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_selinux/"
description: "pam_selinux – PAM module to set the default security context"
---

<p>pam_selinux &#8211; PAM module to set the default security context</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_selinux.so</code> [open] [close] [restore] [nottys] [debug] [verbose] [select_context] [env_params] [use_current_range]</dl>
<h2>Description</h2>
<dd>pam_selinux is a PAM module that sets up the default SELinux security context for the next executed process. </p>
<p> When a new session is started, the open_session part of the module computes and sets up the execution security context used for the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) call, the file security context for the controlling terminal, and the security context used for creating a new kernel keyring. </p>
<p> When the session is ended, the close_session part of the module restores old security contexts that were in effect before the change made by the open_session part of the module. </p>
<p> Adding pam_selinux into the PAM stack might disrupt behavior of other PAM modules which execute applications. To avoid that, <i>pam_selinux.so open</i> should be placed after such modules in the PAM stack, and <i>pam_selinux.so close</i> should be placed before them. When such a placement is not feasible, <i>pam_selinux.so restore</i> could be used to temporary restore original security contexts.</p>
<h2>Options</h2>
<p><code>open</code></p>
<dl>
<dd>Only execute the open_session part of the module.</dl>
<p> <code>close</code></p>
<dl>
<dd>Only execute the close_session part of the module.</dl>
<p> <code>restore</code></p>
<dl>
<dd>In open_session part of the module, temporarily restore the security contexts as they were before the previous call of the module. Another call of this module without the restore option will set up the new security contexts again.</dl>
<p> <code>nottys</code></p>
<dl>
<dd>Do not setup security context of the controlling terminal.</dl>
<p> <code>debug</code></p>
<dl>
<dd>Turn on debug messages via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> <code>verbose</code></p>
<dl>
<dd>Attempt to inform the user when security context is set.</dl>
<p> <code>select_context</code></p>
<dl>
<dd>Attempt to ask the user for a custom security context role. If MLS is on, ask also for sensitivity level.</dl>
<p> <code>env_params</code></p>
<dl>
<dd>Attempt to obtain a custom security context role from PAM environment. If MLS is on, obtain also sensitivity level. This option and the select_context option are mutually exclusive. The respective PAM environment variables are <i>SELINUX_ROLE_REQUESTED</i>, <i>SELINUX_LEVEL_REQUESTED</i>, and <i>SELINUX_USE_CURRENT_RANGE</i>. The first two variables are self describing and the last one if set to 1 makes the PAM module behave as if the use_current_range was specified on the command line of the module.</dl>
<p> <code>use_current_range</code></p>
<dl>
<dd>Use the sensitivity level of the current process for the user context instead of the default level. Also suppresses asking of the sensitivity level from the user or obtaining it from PAM environment.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>session</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The security context was set successfully.</dl>
<p> PAM_SESSION_ERR</p>
<dl>
<dd>Unable to get or set a valid context.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>The user is not known to the system.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory allocation error.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>auth required pam_unix.so
session required pam_permit.so
session optional pam_selinux.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8)</p>
<h2>Author</h2>
<p>pam_selinux was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.</p>
