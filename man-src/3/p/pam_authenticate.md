---
title: "pam_authenticate(3)"
name: "pam_authenticate"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_authenticate/"
description: "pam_authenticate – account authentication"
---

<p>pam_authenticate &#8211; account authentication</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;

int pam_authenticate(pam_handle_t *pamh, int flags);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_authenticate</code> function is used to authenticate the user. The user is required to provide an authentication token depending upon the authentication service, usually this is a password, but could also be a finger print. </p>
<p> The PAM service module may request that the user enter their username vio the the conversation mechanism (see <code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3) and <code><a href="/docs/linux/man/3-pam_conv/">pam_conv</a></code>(3)). The name of the authenticated user will be present in the PAM item PAM_USER. This item may be recovered with a call to <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3). </p>
<p> The <i>pamh</i> argument is an authentication handle obtained by a prior call to pam_start(). The flags argument is the binary or of zero or more of the following values: </p>
<p> PAM_SILENT</p>
<dl>
<dd>Do not emit any messages.</dl>
<p> PAM_DISALLOW_NULL_AUTHTOK</p>
<dl>
<dd>The PAM module service should return PAM_AUTH_ERR if the user does not have a registered authentication token.</dl>
<h2>Return Values</h2>
<p>PAM_ABORT</p>
<dl>
<dd>The application should exit immediately after calling <code><a href="/docs/linux/man/3-pam_end/">pam_end</a></code>(3) first.</dl>
<p> PAM_AUTH_ERR</p>
<dl>
<dd>The user was not authenticated.</dl>
<p> PAM_CRED_INSUFFICIENT</p>
<dl>
<dd>For some reason the application does not have sufficient credentials to authenticate the user.</dl>
<p> PAM_AUTHINFO_UNVAIL</p>
<dl>
<dd>The modules were not able to access the authentication information. This might be due to a network or hardware failure etc.</dl>
<p> PAM_MAXTRIES</p>
<dl>
<dd>One or more of the authentication modules has reached its limit of tries authenticating the user. Do not try again.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>The user was successfully authenticated.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User unknown to authentication service.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3), <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3), <code><a href="/docs/linux/man/3-pam_chauthtok/">pam_chauthtok</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) </p>
