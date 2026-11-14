---
title: "pam_vprompt(3)"
name: "pam_vprompt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_vprompt/"
description: "pam_prompt, pam_vprompt – interface to conversation function"
---

<p>pam_prompt, pam_vprompt &#8211; interface to conversation function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_ext.h&gt;

void pam_prompt(pam_handle_t *pamh, int style, char **response, const char *fmt, ...);

void pam_vprompt(pam_handle_t *pamh, int style, char **response, const char *fmt, va_list args);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_prompt</code> function constructs a message from the specified format string and arguments and passes it to the conversation function as set by the service. Upon successful return, <i>response</i> is set to point to a string returned from the conversation function. This string is allocated on heap and should be freed.</p>
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
<p><code><a href="/docs/linux/man/8-pam/">pam</a></code>(8), <code><a href="/docs/linux/man/3-pam_conv/">pam_conv</a></code>(3)</p>
<h2>Standards</h2>
<p>The <code>pam_prompt</code> and <code>pam_vprompt</code> functions are Linux-PAM extensions.</p>
