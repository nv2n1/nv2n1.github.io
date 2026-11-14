---
title: "pam_tty_audit(8)"
name: "pam_tty_audit"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_tty_audit/"
description: "pam_tty_audit – Enable or disable TTY auditing for specified users"
---

<p>pam_tty_audit &#8211; Enable or disable TTY auditing for specified users</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_tty_audit.so</code> [disable=<i>patterns</i>] [enable=<i>patterns</i>]</dl>
<h2>Description</h2>
<dd>The pam_tty_audit PAM module is used to enable or disable TTY auditing. By default, the kernel does not audit input on any TTY.</p>
<h2>Options</h2>
<p><code>disable=</code><i>patterns</i></p>
<dl>
<dd>For each user matching <i>patterns</i>, disable TTY auditing. This overrides any previous <code>enable</code> option matching the same user name on the command line. See NOTES for further description of <i>patterns</i>.</dl>
<p> <code>enable=</code><i>patterns</i></p>
<dl>
<dd>For each user matching <i>patterns</i>, enable TTY auditing. This overrides any previous <code>disable</code> option matching the same user name on the command line. See NOTES for further description of <i>patterns</i>.</dl>
<p> <code>open_only</code></p>
<dl>
<dd>Set the TTY audit flag when opening the session, but do not restore it when closing the session. Using this option is necessary for some services that don&#8217;t <code>fork()</code> to run the authenticated session, such as <code>sudo</code>.</dl>
<p> <code>log_passwd</code></p>
<dl>
<dd>Log keystrokes when ECHO mode is off but ICANON mode is active. This is the mode in which the tty is placed during password entry. By default, passwords are not logged. This option may not be available on older kernels (3.9?).</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>session</code> type is supported.</p>
<h2>Return Values</h2>
<p>PAM_SESSION_ERR</p>
<dl>
<dd>Error reading or modifying the TTY audit flag. See the system log for more details.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Success.</dl>
<h2>Notes</h2>
<p>When TTY auditing is enabled, it is inherited by all processes started by that user. In particular, daemons restarted by an user will still have TTY auditing enabled, and audit TTY input even by other users unless auditing for these users is explicitly disabled. Therefore, it is recommended to use <code>disable=*</code> as the first option for most daemons using PAM. </p>
<p> To view the data that was logged by the kernel to audit use the command <code>aureport &#8211;tty</code>. </p>
<p> The <i>patterns</i> are comma separated lists of glob patterns or ranges of uids. A range is specified as <i>min_uid</i>:<i>max_uid</i> where one of these values can be empty. If <i>min_uid</i> is empty only user with the uid <i>max_uid</i> will be matched. If <i>max_uid</i> is empty users with the uid greater than or equal to <i>min_uid</i> will be matched. </p>
<p> Please note that passwords in some circumstances may be logged by TTY auditing even if the <code>log_passwd</code> is not used. For example, all input to an ssh session will be logged &#8211; even if there is a password being typed into some software running at the remote host because only the local TTY state affects the local TTY auditing.</p>
<h2>Examples</h2>
<p>Audit all administrative actions.</p>
<dl>
<dd>
<pre>session required pam_tty_audit.so disable=* enable=root</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-aureport/">aureport</a></code>(8), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_tty_audit was written by Miloslav Trmač &lt;mitr [at] redhat.com&gt;. The log_passwd option was added by Richard Guy Briggs &lt;rgb [at] redhat.com&gt;.</p>
