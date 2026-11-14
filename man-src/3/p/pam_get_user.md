---
title: "pam_get_user(3)"
name: "pam_get_user"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_get_user/"
description: "pam_get_user – get user name"
---

<p>pam_get_user &#8211; get user name</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_modules.h&gt;

int pam_get_user(const pam_handle_t *pamh, const char **user, const char *prompt);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_get_user</code> function returns the name of the user specified by <code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3). If no user was specified it what <code>pam_get_item (pamh, PAM_USER, &#8230; );</code> would have returned. If this is NULL it obtains the username via the <code><a href="/docs/linux/man/3-pam_conv/">pam_conv</a></code>(3) mechanism, it prompts the user with the first non-NULL string in the following list: </p>
<dl>
<dd>&bull; The <i>prompt</i> argument passed to the function.</dl>
<dl>
<dd>&bull; What is returned by pam_get_item (pamh, PAM_USER_PROMPT, &#8230; );</dl>
<dl>
<dd>&bull; The default prompt: &quot;login: &quot;</dl>
<p> By whatever means the username is obtained, a pointer to it is returned as the contents of <i>*user</i>. Note, this memory should <code>not</code> be <i>free()</i>&#8216;d or <i>modified</i> by the module. </p>
<p> This function sets the <i>PAM_USER</i> item associated with the <code><a href="/docs/linux/man/3-pam_set_item/">pam_set_item</a></code>(3) and <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3) functions.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>User name was successful retrieved.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>A NULL pointer was submitted.</dl>
<p> PAM_CONV_ERR</p>
<dl>
<dd>The conversation method supplied by the application failed to obtain the username.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_end/">pam_end</a></code>(3), <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3), <code><a href="/docs/linux/man/3-pam_set_item/">pam_set_item</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3) </p>
