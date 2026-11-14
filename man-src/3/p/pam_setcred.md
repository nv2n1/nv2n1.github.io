---
title: "pam_setcred(3)"
name: "pam_setcred"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_setcred/"
description: "pam_setcred – establish / delete user credentials"
---

<p>pam_setcred &#8211; establish / delete user credentials</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;

int pam_setcred(pam_handle_t *pamh, int flags);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_setcred</code> function is used to establish, maintain and delete the credentials of a user. It should be called to set the credentials after a user has been authenticated and before a session is opened for the user (with <code><a href="/docs/linux/man/3-pam_open_session/">pam_open_session</a></code>(3)). The credentials should be deleted after the session has been closed (with <code><a href="/docs/linux/man/3-pam_close_session/">pam_close_session</a></code>(3)). </p>
<p> A credential is something that the user possesses. It is some property, such as a <i>Kerberos</i> ticket, or a supplementary group membership that make up the uniqueness of a given user. On a Linux system the user&#8217;s <i>UID</i> and <i>GID</i>&#8216;s are credentials too. However, it has been decided that these properties (along with the default supplementary groups of which the user is a member) are credentials that should be set directly by the application and not by PAM. Such credentials should be established, by the application, prior to a call to this function. For example, <code><a href="/docs/linux/man/2-initgroups/">initgroups</a></code>(2) (or equivalent) should have been performed. </p>
<p> Valid <i>flags</i>, any one of which, may be logically OR&#8217;d with <code>PAM_SILENT</code>, are: </p>
<p> PAM_ESTABLISH_CRED</p>
<dl>
<dd>Initialize the credentials for the user.</dl>
<p> PAM_DELETE_CRED</p>
<dl>
<dd>Delete the user&#8217;s credentials.</dl>
<p> PAM_REINITIALIZE_CRED</p>
<dl>
<dd>Fully reinitialize the user&#8217;s credentials.</dl>
<p> PAM_REFRESH_CRED</p>
<dl>
<dd>Extend the lifetime of the existing credentials.</dl>
<h2>Return Values</h2>
<p>PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_CRED_ERR</p>
<dl>
<dd>Failed to set user credentials.</dl>
<p> PAM_CRED_EXPIRED</p>
<dl>
<dd>User credentials are expired.</dl>
<p> PAM_CRED_UNAVAIL</p>
<dl>
<dd>Failed to retrieve user credentials.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Data was successful stored.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>A NULL pointer was submitted as PAM handle, the function was called by a module or another system error occured.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User is not known to an authentication module.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_authenticate/">pam_authenticate</a></code>(3), <code><a href="/docs/linux/man/3-pam_open_session/">pam_open_session</a></code>(3), <code><a href="/docs/linux/man/3-pam_close_session/">pam_close_session</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3) </p>
