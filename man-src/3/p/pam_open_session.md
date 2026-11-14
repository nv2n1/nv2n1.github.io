---
title: "pam_open_session(3)"
name: "pam_open_session"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_open_session/"
description: "pam_open_session – start PAM session management"
---

<p>pam_open_session &#8211; start PAM session management</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;

int pam_open_session(pam_handle_t *pamh, int flags);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_open_session</code> function sets up a user session for a previously successful authenticated user. The session should later be terminated with a call to <code><a href="/docs/linux/man/3-pam_close_session/">pam_close_session</a></code>(3). </p>
<p> It should be noted that the effective uid, <code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2). of the application should be of sufficient privilege to perform such tasks as creating or mounting the user&#8217;s home directory for example. </p>
<p> The flags argument is the binary or of zero or more of the following values: </p>
<p> PAM_SILENT</p>
<dl>
<dd>Do not emit any messages.</dl>
<h2>Return Values</h2>
<p>PAM_ABORT</p>
<dl>
<dd>General failure.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_SESSION_ERR</p>
<dl>
<dd>Session failure.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Session was successful created.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_close_session/">pam_close_session</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3) </p>
