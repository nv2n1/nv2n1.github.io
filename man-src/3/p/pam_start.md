---
title: "pam_start(3)"
name: "pam_start"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_start/"
description: "pam_start – initialization of PAM transaction"
---

<p>pam_start &#8211; initialization of PAM transaction</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;

int pam_start(const char *service_name, const char *user, const struct pam_conv *pam_conversation, pam_handle_t **pamh);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_start</code> function creates the PAM context and initiates the PAM transaction. It is the first of the PAM functions that needs to be called by an application. The transaction state is contained entirely within the structure identified by this handle, so it is possible to have multiple transactions in parallel. But it is not possible to use the same handle for different transactions, a new one is needed for every new context. </p>
<p> The <i>service_name</i> argument specifies the name of the service to apply and will be stored as PAM_SERVICE item in the new context. The policy for the service will be read from the file /etc/pam.d/service_name or, if that file does not exist, from /etc/pam.conf. </p>
<p> The <i>user</i> argument can specify the name of the target user and will be stored as PAM_USER item. If the argument is NULL, the module has to ask for this item if necessary. </p>
<p> The <i>pam_conversation</i> argument points to a <i>struct pam_conv</i> describing the conversation function to use. An application must provide this for direct communication between a loaded module and the application. </p>
<p> Following a successful return (PAM_SUCCESS) the contents of <i>pamh</i> is a handle that contains the PAM context for successive calls to the PAM functions. In an error case is the content of <i>pamh</i> undefined. </p>
<p> The <i>pam_handle_t</i> is a blind structure and the application should not attempt to probe it directly for information. Instead the PAM library provides the functions <code><a href="/docs/linux/man/3-pam_set_item/">pam_set_item</a></code>(3) and <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3). The PAM handle cannot be used for mulitiple authentications at the same time as long as <code>pam_end</code> was not called on it before.</p>
<h2>Return Values</h2>
<p>PAM_ABORT</p>
<dl>
<dd>General failure.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Transaction was successful created.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>System error, for example a NULL pointer was submitted instead of a pointer to data.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_get_data/">pam_get_data</a></code>(3), <code><a href="/docs/linux/man/3-pam_set_data/">pam_set_data</a></code>(3), <code><a href="/docs/linux/man/3-pam_end/">pam_end</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3) </p>
