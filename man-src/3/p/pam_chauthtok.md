---
title: "pam_chauthtok(3)"
name: "pam_chauthtok"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_chauthtok/"
description: "pam_chauthtok – updating authentication tokens"
---

<p>pam_chauthtok &#8211; updating authentication tokens</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;

int pam_chauthtok(pam_handle_t *pamh, int flags);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_chauthtok</code> function is used to change the authentication token for a given user (as indicated by the state associated with the handle <i>pamh</i>). </p>
<p> The <i>pamh</i> argument is an authentication handle obtained by a prior call to pam_start(). The flags argument is the binary or of zero or more of the following values: </p>
<p> PAM_SILENT</p>
<dl>
<dd>Do not emit any messages.</dl>
<p> PAM_CHANGE_EXPIRED_AUTHTOK</p>
<dl>
<dd>This argument indicates to the modules that the users authentication token (password) should only be changed if it has expired. If this argument is not passed, the application requires that all authentication tokens are to be changed.</dl>
<h2>Return Values</h2>
<p>PAM_AUTHTOK_ERR</p>
<dl>
<dd>A module was unable to obtain the new authentication token.</dl>
<p> PAM_AUTHTOK_RECOVERY_ERR</p>
<dl>
<dd>A module was unable to obtain the old authentication token.</dl>
<p> PAM_AUTHTOK_LOCK_BUSY</p>
<dl>
<dd>One or more of the modules was unable to change the authentication token since it is currently locked.</dl>
<p> PAM_AUTHTOK_DISABLE_AGING</p>
<dl>
<dd>Authentication token aging has been disabled for at least one of the modules.</dl>
<p> PAM_PERM_DENIED</p>
<dl>
<dd>Permission denied.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>The authentication token was successfully updated.</dl>
<p> PAM_TRY_AGAIN</p>
<dl>
<dd>Not all of the modules were in a position to update the authentication token(s). In such a case none of the user&#8217;s authentication tokens are updated.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User unknown to password service.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3), <code><a href="/docs/linux/man/3-pam_authenticate/">pam_authenticate</a></code>(3), <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3), <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) </p>
