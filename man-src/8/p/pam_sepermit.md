---
title: "pam_sepermit(8)"
name: "pam_sepermit"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_sepermit/"
description: "pam_sepermit – PAM module to allow/deny login depending on SELinux enforcement state"
---

<p>pam_sepermit &#8211; PAM module to allow/deny login depending on SELinux enforcement state</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_sepermit.so</code> [debug] [conf=<i>/path/to/config/file</i>]</dl>
<h2>Description</h2>
<dd>The pam_sepermit module allows or denies login depending on SELinux enforcement state. </p>
<p> When the user which is logging in matches an entry in the config file he is allowed access only when the SELinux is in enforcing mode. Otherwise he is denied access. For users not matching any entry in the config file the pam_sepermit module returns PAM_IGNORE return value. </p>
<p> The config file contains a list of user names one per line with optional arguments. If the <i>name</i> is prefixed with <i>@</i> character it means that all users in the group <i>name</i> match. If it is prefixed with a <i>%</i> character the SELinux user is used to match against the <i>name</i> instead of the account name. Note that when SELinux is disabled the SELinux user assigned to the account cannot be determined. This means that such entries are never matched when SELinux is disabled and pam_sepermit will return PAM_IGNORE. </p>
<p> See <code><a href="/docs/linux/man/5-sepermit-conf/">sepermit.conf</a></code>(5) for details.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Turns on debugging via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> <code>conf=</code><i>/path/to/config/file</i></p>
<dl>
<dd>Path to alternative config file overriding the default.</dl>
<h2>Module Types Provided</h2>
<p>The <code>auth</code> and <code>account</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>SELinux is disabled or in the permissive mode and the user matches.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>SELinux is in the enforcing mode and the user matches.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>The user does not match any entry in the config file.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>The module was unable to determine the user&#8217;s name.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>Error during reading or parsing the config file.</dl>
<h2>Files</h2>
<p>/etc/security/sepermit.conf</p>
<dl>
<dd>Default configuration file</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>auth [success=done ignore=ignore default=bad] pam_sepermit.so
auth required pam_unix.so
account required pam_unix.so
session required pam_permit.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sepermit-conf/">sepermit.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7) <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8)</p>
<h2>Author</h2>
<p>pam_sepermit and this manual page were written by Tomas Mraz &lt;tmraz [at] redhat.com&gt;.</p>
