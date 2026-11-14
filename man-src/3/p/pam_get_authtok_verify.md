---
title: "pam_get_authtok_verify(3)"
name: "pam_get_authtok_verify"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_get_authtok_verify/"
description: "pam_get_authtok, pam_get_authtok_verify, pam_get_authtok_noverify – get authentication token"
---

<p>pam_get_authtok, pam_get_authtok_verify, pam_get_authtok_noverify &#8211; get authentication token</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_ext.h&gt;

int pam_get_authtok(pam_handle_t *pamh, int item, const char **authtok, const char *prompt);

int pam_get_authtok_noverify(pam_handle_t *pamh, const char **authtok, const char *prompt);

int pam_get_authtok_verify(pam_handle_t *pamh, const char **authtok, const char *prompt);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_get_authtok</code> function returns the cached authentication token, or prompts the user if no token is currently cached. It is intended for internal use by Linux-PAM and PAM service modules. Upon successful return, <i>authtok</i> contains a pointer to the value of the authentication token. Note, this is a pointer to the <i>actual</i> data and should <code>not</code> be <i>free()</i>&#8216;ed or over-written! </p>
<p> The <i>prompt</i> argument specifies a prompt to use if no token is cached. If a NULL pointer is given, <code>pam_get_authtok</code> uses pre-defined prompts. </p>
<p> The following values are supported for <i>item</i>: </p>
<p> PAM_AUTHTOK</p>
<dl>
<dd>Returns the current authentication token. Called from <code><a href="/docs/linux/man/3-pam_sm_chauthtok/">pam_sm_chauthtok</a></code>(3)<code>pam_get_authtok</code> will ask the user to confirm the new token by retyping it. If a prompt was specified, &quot;Retype&quot; will be used as prefix.</dl>
<p> PAM_OLDAUTHTOK</p>
<dl>
<dd>Returns the previous authentication token when changing authentication tokens.</dl>
<p> The <code>pam_get_authtok_noverify</code> function can only be used for changing the password (from <code><a href="/docs/linux/man/3-pam_sm_chauthtok/">pam_sm_chauthtok</a></code>(3)). It returns the cached authentication token, or prompts the user if no token is currently cached. The difference to <code>pam_get_authtok</code> is, that this function does not ask a second time for the password to verify it. Upon successful return, <i>authtok</i> contains a pointer to the value of the authentication token. Note, this is a pointer to the <i>actual</i> data and should <code>not</code> be <i>free()</i>&#8216;ed or over-written! </p>
<p> The <code>pam_get_authtok_verify</code> function can only be used to verify a password for mistypes gotten by <code><a href="/docs/linux/man/3-pam_get_authtok_noverify/">pam_get_authtok_noverify</a></code>(3). This function asks a second time for the password and verify it with the password provided by <i>authtok</i> argument. In case of an error, the value of <i>authtok</i> is undefined. Else this argument will point to the <i>actual</i> data and should <code>not</code> be <i>free()</i>&#8216;ed or over-written!</p>
<h2>Options</h2>
<p><code>pam_get_authtok</code> honours the following module options: </p>
<p> <code>try_first_pass</code></p>
<dl>
<dd>Before prompting the user for their password, the module first tries the previous stacked module&#8217;s password in case that satisfies this module as well.</dl>
<p> <code>use_first_pass</code></p>
<dl>
<dd>The argument <code>use_first_pass</code> forces the module to use a previous stacked modules password and will never prompt the user &#8211; if no password is available or the password is not appropriate, the user will be denied access.</dl>
<p> <code>use_authtok</code></p>
<dl>
<dd>When password changing enforce the module to set the new token to the one provided by a previously stacked <code>password</code> module. If no token is available token changing will fail.</dl>
<p> <code>authtok_type=</code><i>XXX</i></p>
<dl>
<dd>The default action is for the module to use the following prompts when requesting passwords: &quot;New UNIX password: &quot; and &quot;Retype UNIX password: &quot;. The example word <i>UNIX</i> can be replaced with this option, by default it is empty.</dl>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>Authentication token could not be retrieved.</dl>
<p> PAM_AUTHTOK_ERR</p>
<dl>
<dd>New authentication could not be retrieved.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Authentication token was successfully retrieved.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>No space for an authentication token was provided.</dl>
<p> PAM_TRY_AGAIN</p>
<dl>
<dd>New authentication tokens mismatch.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Standards</h2>
<p>The <code>pam_get_authtok</code> function is a Linux-PAM extensions.</p>
