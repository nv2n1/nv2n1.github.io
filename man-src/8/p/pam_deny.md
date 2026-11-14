---
title: "pam_deny(8)"
name: "pam_deny"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_deny/"
description: "pam_deny – The locking-out PAM module"
---

<p>pam_deny &#8211; The locking-out PAM module</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_deny.so</code></dl>
<h2>Description</h2>
<dd>This module can be used to deny access. It always indicates a failure to the application through the PAM framework. It might be suitable for using for default (the <i>OTHER</i>) entries.</p>
<h2>Options</h2>
<p>This module does not recognise any options.</p>
<h2>Module Types Provided</h2>
<p>All module types (<code>account</code>, <code>auth</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>This is returned by the account and auth services.</dl>
<p> PAM_CRED_ERR</p>
<dl>
<dd>This is returned by the setcred function.</dl>
<p> PAM_AUTHTOK_ERR</p>
<dl>
<dd>This is returned by the password service.</dl>
<p> PAM_SESSION_ERR</p>
<dl>
<dd>This is returned by the session service.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>#%PAM-1.0
#
# If we don't have config entries for a service, the
# OTHER entries are used. To be secure, warn and deny
# access to everything.
other auth required pam_warn.so
other auth required pam_deny.so
other account required pam_warn.so
other account required pam_deny.so
other password required pam_warn.so
other password required pam_deny.so
other session required pam_warn.so
other session required pam_deny.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_deny was written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;</p>
