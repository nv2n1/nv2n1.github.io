---
title: "pam_permit(8)"
name: "pam_permit"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_permit/"
description: "pam_permit – The promiscuous module"
---

<p>pam_permit &#8211; The promiscuous module</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_permit.so</code></dl>
<h2>Description</h2>
<dd>pam_permit is a PAM module that always permit access. It does nothing else. </p>
<p> In the case of authentication, the user&#8217;s name will be set to <i>nobody</i> if the application didn&#8217;t set one. Many applications and PAM modules become confused if this name is unknown. </p>
<p> This module is very dangerous. It should be used with extreme caution.</p>
<h2>Options</h2>
<p>This module does not recognise any options.</p>
<h2>Module Types Provided</h2>
<p>The <code>auth</code>, <code>account</code>, <code>password</code> and <code>session</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>This module always returns this value.</dl>
<h2>Examples</h2>
<p>Add this line to your other login entries to disable account management, but continue to permit users to log in.</p>
<dl>
<dd>
<pre>account required pam_permit.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_permit was written by Andrew G. Morgan, &lt;morgan [at] kernel.org&gt;.</p>
