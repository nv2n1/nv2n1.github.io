---
title: "pam_sm_authenticate(3)"
name: "pam_sm_authenticate"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_sm_authenticate/"
description: "pam_sm_authenticate – PAM service function for user authentication"
---

<p>pam_sm_authenticate &#8211; PAM service function for user authentication</p>
<h2>Synopsis</h2>
<pre><code>#define PAM_SM_AUTH
#include &lt;security/pam_modules.h&gt;

PAM_EXTERN int pam_sm_authenticate(pam_handle_t *pamh, int flags, int argc, const char **argv);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_sm_authenticate</code> function is the service module&#8217;s implementation of the <code><a href="/docs/linux/man/3-pam_authenticate/">pam_authenticate</a></code>(3) interface. </p>
<p> This function performs the task of authenticating the user. </p>
<p> Valid flags, which may be logically OR&#8217;d with <i>PAM_SILENT</i>, are: </p>
<p> PAM_SILENT</p>
<dl>
<dd>Do not emit any messages.</dl>
<p> PAM_DISALLOW_NULL_AUTHTOK</p>
<dl>
<dd>Return <code>PAM_AUTH_ERR</code> if the database of authentication tokens for this authentication mechanism has a <i>NULL</i> entry for the user. Without this flag, such a <i>NULL</i> token will lead to a success without the user being prompted.</dl>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>Authentication failure.</dl>
<p> PAM_CRED_INSUFFICIENT</p>
<dl>
<dd>For some reason the application does not have sufficient credentials to authenticate the user.</dl>
<p> PAM_AUTHINFO_UNAVAIL</p>
<dl>
<dd>The modules were not able to access the authentication information. This might be due to a network or hardware failure etc.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>The authentication token was successfully updated.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>The supplied username is not known to the authentication service.</dl>
<p> PAM_MAXTRIES</p>
<dl>
<dd>One or more of the authentication modules has reached its limit of tries authenticating the user. Do not try again.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam/">pam</a></code>(3), <code><a href="/docs/linux/man/3-pam_authenticate/">pam_authenticate</a></code>(3), <code><a href="/docs/linux/man/3-pam_sm_setcred/">pam_sm_setcred</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3), <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8) </p>
