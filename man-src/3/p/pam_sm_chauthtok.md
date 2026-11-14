---
title: "pam_sm_chauthtok(3)"
name: "pam_sm_chauthtok"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_sm_chauthtok/"
description: "pam_sm_chauthtok – PAM service function for authentication token management"
---

<p>pam_sm_chauthtok &#8211; PAM service function for authentication token management</p>
<h2>Synopsis</h2>
<pre><code>#define PAM_SM_PASSWORD
#include &lt;security/pam_modules.h&gt;

PAM_EXTERN int pam_sm_chauthtok(pam_handle_t *pamh, int flags, int argc, const char **argv);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_sm_chauthtok</code> function is the service module&#8217;s implementation of the <code><a href="/docs/linux/man/3-pam_chauthtok/">pam_chauthtok</a></code>(3) interface. </p>
<p> This function is used to (re-)set the authentication token of the user. </p>
<p> Valid flags, which may be logically OR&#8217;d with <i>PAM_SILENT</i>, are: </p>
<p> PAM_SILENT</p>
<dl>
<dd>Do not emit any messages.</dl>
<p> PAM_CHANGE_EXPIRED_AUTHTOK</p>
<dl>
<dd>This argument indicates to the module that the users authentication token (password) should only be changed if it has expired. This flag is optional and <i>must</i> be combined with one of the following two flags. Note, however, the following two options are <i>mutually exclusive</i>.</dl>
<p> PAM_PRELIM_CHECK</p>
<dl>
<dd>This indicates that the modules are being probed as to their ready status for altering the user&#8217;s authentication token. If the module requires access to another system over some network it should attempt to verify it can connect to this system on receiving this flag. If a module cannot establish it is ready to update the user&#8217;s authentication token it should return <code>PAM_TRY_AGAIN</code>, this information will be passed back to the application. </p>
<p> If the control value <i>sufficient</i> is used in the password stack, the <i>PAM_PRELIM_CHECK</i> section of the modules following that control value is not always executed.</dl>
<p> PAM_UPDATE_AUTHTOK</p>
<dl>
<dd>This informs the module that this is the call it should change the authorization tokens. If the flag is logically OR&#8217;d with <code>PAM_CHANGE_EXPIRED_AUTHTOK</code>, the token is only changed if it has actually expired.</dl>
<p> The PAM library calls this function twice in succession. The first time with <code>PAM_PRELIM_CHECK</code> and then, if the module does not return <code>PAM_TRY_AGAIN</code>, subsequently with <code>PAM_UPDATE_AUTHTOK</code>. It is only on the second call that the authorization token is (possibly) changed.</p>
<h2>Return Values</h2>
<p>PAM_AUTHTOK_ERR</p>
<dl>
<dd>The module was unable to obtain the new authentication token.</dl>
<p> PAM_AUTHTOK_RECOVERY_ERR</p>
<dl>
<dd>The module was unable to obtain the old authentication token.</dl>
<p> PAM_AUTHTOK_LOCK_BUSY</p>
<dl>
<dd>Cannot change the authentication token since it is currently locked.</dl>
<p> PAM_AUTHTOK_DISABLE_AGING</p>
<dl>
<dd>Authentication token aging has been disabled.</dl>
<p> PAM_PERM_DENIED</p>
<dl>
<dd>Permission denied.</dl>
<p> PAM_TRY_AGAIN</p>
<dl>
<dd>Preliminary check was unsuccessful. Signals an immediate return to the application is desired.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>The authentication token was successfully updated.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User unknown to password service.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam/">pam</a></code>(3), <code><a href="/docs/linux/man/3-pam_chauthtok/">pam_chauthtok</a></code>(3), <code><a href="/docs/linux/man/3-pam_sm_chauthtok/">pam_sm_chauthtok</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3), <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8) </p>
