---
title: "pam_acct_mgmt(3)"
name: "pam_acct_mgmt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_acct_mgmt/"
description: "pam_acct_mgmt – PAM account validation management"
---

<p>pam_acct_mgmt &#8211; PAM account validation management</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;

int pam_acct_mgmt(pam_handle_t *pamh, int flags);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_acct_mgmt</code> function is used to determine if the users account is valid. It checks for authentication token and account expiration and verifies access restrictions. It is typically called after the user has been authenticated. </p>
<p> The <i>pamh</i> argument is an authentication handle obtained by a prior call to pam_start(). The flags argument is the binary or of zero or more of the following values: </p>
<p> PAM_SILENT</p>
<dl>
<dd>Do not emit any messages.</dl>
<p> PAM_DISALLOW_NULL_AUTHTOK</p>
<dl>
<dd>The PAM module service should return PAM_NEW_AUTHTOK_REQD if the user has a null authentication token.</dl>
<h2>Return Values</h2>
<p>PAM_ACCT_EXPIRED</p>
<dl>
<dd>User account has expired.</dl>
<p> PAM_AUTH_ERR</p>
<dl>
<dd>Authentication failure.</dl>
<p> PAM_NEW_AUTHTOK_REQD</p>
<dl>
<dd>The user account is valid but their authentication token is <i>expired</i>. The correct response to this return-value is to require that the user satisfies the <code>pam_chauthtok()</code> function before obtaining service. It may not be possible for some applications to do this. In such cases, the user should be denied access until such time as they can update their password.</dl>
<p> PAM_PERM_DENIED</p>
<dl>
<dd>Permission denied.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>The authentication token was successfully updated.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User unknown to password service.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3), <code><a href="/docs/linux/man/3-pam_authenticate/">pam_authenticate</a></code>(3), <code><a href="/docs/linux/man/3-pam_chauthtok/">pam_chauthtok</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) </p>
