---
title: "pam_info(3)"
name: "pam_info"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_info/"
description: "pam_info, pam_vinfo – display messages to the user"
---

<p>pam_info, pam_vinfo &#8211; display messages to the user</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_ext.h&gt;

int pam_info(pam_handle_t *pamh, const char *fmt, ...);

int pam_vinfo(pam_handle_t *pamh, const char *fmt, va_list args);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_info</code> function prints messages through the conversation function to the user. </p>
<p> The <code>pam_vinfo</code> function performs the same task as <code>pam_info()</code> with the difference that it takes a set of arguments which have been obtained using the <code><a href="/docs/linux/man/3-stdarg/">stdarg</a></code>(3) variable argument list macros.</p>
<h2>Return Values</h2>
<p>PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_CONV_ERR</p>
<dl>
<dd>Conversation failure.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Transaction was successful created.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>System error.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Standards</h2>
<p>The <code>pam_info</code> and <code>pam_vinfo</code> functions are Linux-PAM extensions.</p>
