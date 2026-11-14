---
title: "pam_sm_setcred(3)"
name: "pam_sm_setcred"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_sm_setcred/"
description: "pam_sm_setcred – PAM service function to alter credentials"
---

<p>pam_sm_setcred &#8211; PAM service function to alter credentials</p>
<h2>Synopsis</h2>
<pre><code>#define PAM_SM_AUTH
#include &lt;security/pam_modules.h&gt;

PAM_EXTERN int pam_sm_setcred(pam_handle_t *pamh, int flags, int argc, const char **argv);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_sm_setcred</code> function is the service module&#8217;s implementation of the <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3) interface. </p>
<p> This function performs the task of altering the credentials of the user with respect to the corresponding authorization scheme. Generally, an authentication module may have access to more information about a user than their authentication token. This function is used to make such information available to the application. It should only be called <i>after</i> the user has been authenticated but before a session has been established. </p>
<p> Valid flags, which may be logically OR&#8217;d with <i>PAM_SILENT</i>, are: </p>
<p> PAM_SILENT</p>
<dl>
<dd>Do not emit any messages.</dl>
<p> PAM_ESTABLISH_CRED</p>
<dl>
<dd>Initialize the credentials for the user.</dl>
<p> PAM_DELETE_CRED</p>
<dl>
<dd>Delete the credentials associated with the authentication service.</dl>
<p> PAM_REINITIALIZE_CRED</p>
<dl>
<dd>Reinitialize the user credentials.</dl>
<p> PAM_REFRESH_CRED</p>
<dl>
<dd>Extend the lifetime of the user credentials.</dl>
<p> The way the <code>auth</code> stack is navigated in order to evaluate the <code>pam_setcred</code>() function call, independent of the <code>pam_sm_setcred</code>() return codes, is exactly the same way that it was navigated when evaluating the <code>pam_authenticate</code>() library call. Typically, if a stack entry was ignored in evaluating <code>pam_authenticate</code>(), it will be ignored when libpam evaluates the <code>pam_setcred</code>() function call. Otherwise, the return codes from each module specific <code>pam_sm_setcred</code>() call are treated as <code>required</code>.</p>
<h2>Return Values</h2>
<p>PAM_CRED_UNAVAIL</p>
<dl>
<dd>This module cannot retrieve the user&#8217;s credentials.</dl>
<p> PAM_CRED_EXPIRED</p>
<dl>
<dd>The user&#8217;s credentials have expired.</dl>
<p> PAM_CRED_ERR</p>
<dl>
<dd>This module was unable to set the credentials of the user.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>The user credential was successfully set.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>The user is not known to this authentication module.</dl>
<p> These, non-<i>PAM_SUCCESS</i>, return values will typically lead to the credential stack <i>failing</i>. The first such error will dominate in the return value of <code>pam_setcred</code>().</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam/">pam</a></code>(3), <code><a href="/docs/linux/man/3-pam_authenticate/">pam_authenticate</a></code>(3), <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3), <code><a href="/docs/linux/man/3-pam_sm_authenticate/">pam_sm_authenticate</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3), <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8) </p>
