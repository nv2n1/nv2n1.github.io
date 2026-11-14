---
title: "pam_loginuid(8)"
name: "pam_loginuid"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_loginuid/"
description: "pam_loginuid – Record user’s login uid to the process attribute"
---

<p>pam_loginuid &#8211; Record user&#8217;s login uid to the process attribute</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_loginuid.so</code> [require_auditd]</dl>
<h2>Description</h2>
<dd>The pam_loginuid module sets the loginuid process attribute for the process that was authenticated. This is necessary for applications to be correctly audited. This PAM module should only be used for entry point applications like: login, sshd, gdm, vsftpd, crond and atd. There are probably other entry point applications besides these. You should not use it for applications like sudo or su as that defeats the purpose by changing the loginuid to the account they just switched to.</p>
<h2>Options</h2>
<p><code>require_auditd</code></p>
<dl>
<dd>This option, when given, will cause this module to query the audit daemon status and deny logins if it is not running.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>session</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The loginuid value is set and auditd is running if check requested.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>The /proc/self/loginuid file is not present on the system or the login process runs inside uid namespace and kernel does not support overwriting loginuid.</dl>
<p> PAM_SESSION_ERR</p>
<dl>
<dd>Any other error prevented setting loginuid or auditd is not running.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>#%PAM-1.0
auth required pam_unix.so
auth required pam_nologin.so
account required pam_unix.so
password required pam_unix.so
session required pam_unix.so
session required pam_loginuid.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7), <code><a href="/docs/linux/man/8-auditctl/">auditctl</a></code>(8), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8)</p>
<h2>Author</h2>
<p>pam_loginuid was written by Steve Grubb &lt;sgrubb [at] redhat.com&gt;</p>
