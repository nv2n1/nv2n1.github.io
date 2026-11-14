---
title: "pam_sm_acct_mgmt(3)"
name: "pam_sm_acct_mgmt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_sm_acct_mgmt/"
description: "pam_sm_acct_mgmt – PAM service function for account management"
---

<p>pam_sm_acct_mgmt &#8211; PAM service function for account management</p>
<h2>Synopsis</h2>
<pre><code>#define PAM_SM_ACCOUNT
#include &lt;security/pam_modules.h&gt;

PAM_EXTERN int pam_sm_acct_mgmt(pam_handle_t *pamh, int flags, int argc, const char **argv);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_sm_acct_mgmt</code> function is the service module&#8217;s implementation of the <code><a href="/docs/linux/man/3-pam_acct_mgmt/">pam_acct_mgmt</a></code>(3) interface. </p>
<p> This function performs the task of establishing whether the user is permitted to gain access at this time. It should be understood that the user has previously been validated by an authentication module. This function checks for other things. Such things might be: the time of day or the date, the terminal line, remote hostname, etc. This function may also determine things like the expiration on passwords, and respond that the user change it before continuing. </p>
<p> Valid flags, which may be logically OR&#8217;d with <i>PAM_SILENT</i>, are: </p>
<p> PAM_SILENT</p>
<dl>
<dd>Do not emit any messages.</dl>
<p> PAM_DISALLOW_NULL_AUTHTOK</p>
<dl>
<dd>Return <code>PAM_AUTH_ERR</code> if the database of authentication tokens for this authentication mechanism has a <i>NULL</i> entry for the user.</dl>
<h2>Return Values</h2>
<p>PAM_ACCT_EXPIRED</p>
<dl>
<dd>User account has expired.</dl>
<p> PAM_AUTH_ERR</p>
<dl>
<dd>Authentication failure.</dl>
<p> PAM_NEW_AUTHTOK_REQD</p>
<dl>
<dd>The user&#8217;s authentication token has expired. Before calling this function again the application will arrange for a new one to be given. This will likely result in a call to <code>pam_sm_chauthtok()</code>.</dl>
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
<p><code><a href="/docs/linux/man/3-pam/">pam</a></code>(3), <code><a href="/docs/linux/man/3-pam_acct_mgmt/">pam_acct_mgmt</a></code>(3), <code><a href="/docs/linux/man/3-pam_sm_chauthtok/">pam_sm_chauthtok</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3), <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8) </p>
