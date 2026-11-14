---
title: "pam_verror(3)"
name: "pam_verror"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_verror/"
description: "pam_error, pam_verror – display error messages to the user"
---

<p>pam_error, pam_verror &#8211; display error messages to the user</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_ext.h&gt;

int pam_error(pam_handle_t *pamh, const char *fmt, ...);

int pam_verror(pam_handle_t *pamh, const char *fmt, va_list args);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_error</code> function prints error messages through the conversation function to the user. </p>
<p> The <code>pam_verror</code> function performs the same task as <code>pam_error()</code> with the difference that it takes a set of arguments which have been obtained using the <code><a href="/docs/linux/man/3-stdarg/">stdarg</a></code>(3) variable argument list macros.</p>
<h2>Return Values</h2>
<p>PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_CONV_ERR</p>
<dl>
<dd>Conversation failure.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Error message was displayed.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>System error.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_info/">pam_info</a></code>(3), <code><a href="/docs/linux/man/3-pam_vinfo/">pam_vinfo</a></code>(3), <code><a href="/docs/linux/man/3-pam_prompt/">pam_prompt</a></code>(3), <code><a href="/docs/linux/man/3-pam_vprompt/">pam_vprompt</a></code>(3), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Standards</h2>
<p>The <code>pam_error</code> and <code>pam_verror</code> functions are Linux-PAM extensions.</p>
