---
title: "sepermit(5)"
name: "sepermit"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sepermit/"
description: "sepermit.conf – configuration file for the pam_sepermit module"
---

<p>sepermit.conf &#8211; configuration file for the pam_sepermit module</p>
<h2>Description</h2>
<p>The lines of the configuration file have the following syntax: </p>
<p> <i>&lt;user&gt;</i>[:<i>&lt;option&gt;</i>:<i>&lt;option&gt;</i>&#8230;] </p>
<p> The <code>user</code> can be specified in the following manner: </p>
<dl>
<dd>&bull; a username</dl>
<dl>
<dd>&bull; a groupname, with <code>@group</code> syntax. This should not be confused with netgroups.</dl>
<dl>
<dd>&bull; a SELinux user name with <code>%seuser</code> syntax.</dl>
<p> The recognized options are: </p>
<p> <code>exclusive</code></p>
<dl>
<dd>Only single login session will be allowed for the user and the user&#8217;s processes will be killed on logout.</dl>
<p> <code>ignore</code></p>
<dl>
<dd>The module will never return PAM_SUCCESS status for the user. It will return PAM_IGNORE if SELinux is in the enforcing mode, and PAM_AUTH_ERR otherwise. It is useful if you want to support passwordless guest users and other confined users with passwords simultaneously.</dl>
<p> The lines which start with # character are comments and are ignored.</p>
<h2>Examples</h2>
<p>These are some example lines which might be specified in /etc/security/sepermit.conf. </p>
<dl>
<dd>
<pre>%guest_u:exclusive
%staff_u:ignore
%user_u:ignore</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_sepermit/">pam_sepermit</a></code>(8), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8),</p>
<h2>Author</h2>
<p>pam_sepermit and this manual page were written by Tomas Mraz &lt;tmraz [at] redhat.com&gt;</p>
