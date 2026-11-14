---
title: "pam_shells(8)"
name: "pam_shells"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_shells/"
description: "pam_shells – PAM module to check for valid login shell"
---

<p>pam_shells &#8211; PAM module to check for valid login shell</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_shells.so</code></dl>
<h2>Description</h2>
<dd>pam_shells is a PAM module that only allows access to the system if the user&#8217;s shell is listed in /etc/shells. </p>
<p> It also checks if /etc/shells is a plain file and not world writable.</p>
<h2>Options</h2>
<p>This module does not recognise any options.</p>
<h2>Module Types Provided</h2>
<p>The <code>auth</code> and <code>account</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>Access to the system was denied.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>The user&#8217;s login shell was listed as valid shell in /etc/shells.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>The module was not able to get the name of the user.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>auth required pam_shells.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-shells/">shells</a></code>(5), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_shells was written by Erik Troan &lt;ewt [at] redhat.com&gt;.</p>
