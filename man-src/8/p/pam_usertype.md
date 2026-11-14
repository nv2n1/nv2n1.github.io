---
title: "pam_usertype(8)"
name: "pam_usertype"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_usertype/"
description: "pam_usertype – check if the authenticated user is a system or regular account"
---

<p>pam_usertype &#8211; check if the authenticated user is a system or regular account</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_usertype.so</code> [<i>flag</i>&#8230;] {<i>condition</i>}</dl>
<h2>Description</h2>
<dd>pam_usertype.so is designed to succeed or fail authentication based on type of the account of the authenticated user. The type of the account is decided with help of <i>SYS_UID_MIN</i> and <i>SYS_UID_MAX</i> settings in <i>/etc/login.defs</i>. One use is to select whether to load other modules based on this test. </p>
<p> The module should be given only one condition as module argument. Authentication will succeed only if the condition is met.</p>
<h2>Options</h2>
<p>The following <i>flag</i>s are supported: </p>
<p> <code>use_uid</code></p>
<dl>
<dd>Evaluate conditions using the account of the user whose UID the application is running under instead of the user being authenticated.</dl>
<p> <code>audit</code></p>
<dl>
<dd>Log unknown users to the system log.</dl>
<p> Available <i>condition</i>s are: </p>
<p> <code>issystem</code></p>
<dl>
<dd>Succeed if the user is a system user.</dl>
<p> <code>isregular</code></p>
<dl>
<dd>Succeed if the user is a regular user.</dl>
<h2>Module Types Provided</h2>
<p>All module types (<code>account</code>, <code>auth</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The condition was true.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_CONV_ERR</p>
<dl>
<dd>The conversation method supplied by the application failed to obtain the username.</dl>
<p> PAM_INCOMPLETE</p>
<dl>
<dd>The conversation method supplied by the application returned PAM_CONV_AGAIN.</dl>
<p> PAM_AUTH_ERR</p>
<dl>
<dd>The condition was false.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>A service error occurred or the arguments can&#8217;t be parsed correctly.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User was not found.</dl>
<h2>Examples</h2>
<p>Skip remaining modules if the user is a system user: </p>
<dl>
<dd>
<pre>account sufficient pam_usertype.so issystem</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Author</h2>
<p>Pavel Březina &lt;pbrezina [at] redhat.com&gt;</p>
