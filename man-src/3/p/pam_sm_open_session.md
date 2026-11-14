---
title: "pam_sm_open_session(3)"
name: "pam_sm_open_session"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_sm_open_session/"
description: "pam_sm_open_session – PAM service function to start session management"
---

<p>pam_sm_open_session &#8211; PAM service function to start session management</p>
<h2>Synopsis</h2>
<pre><code>#define PAM_SM_SESSION
#include &lt;security/pam_modules.h&gt;

PAM_EXTERN int pam_sm_open_session(pam_handle_t *pamh, int flags, int argc, const char **argv);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_sm_open_session</code> function is the service module&#8217;s implementation of the <code><a href="/docs/linux/man/3-pam_open_session/">pam_open_session</a></code>(3) interface. </p>
<p> This function is called to commence a session. The only valid value for <i>flags</i> is zero or: </p>
<p> PAM_SILENT</p>
<dl>
<dd>Do not emit any messages.</dl>
<h2>Return Values</h2>
<p>PAM_SESSION_ERR</p>
<dl>
<dd>Cannot make/remove an entry for the specified session.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>The session was successfully started.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam/">pam</a></code>(3), <code><a href="/docs/linux/man/3-pam_open_session/">pam_open_session</a></code>(3), <code><a href="/docs/linux/man/3-pam_sm_close_session/">pam_sm_close_session</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3), <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8) </p>
