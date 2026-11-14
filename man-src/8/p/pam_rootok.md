---
title: "pam_rootok(8)"
name: "pam_rootok"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_rootok/"
description: "pam_rootok – Gain only root access"
---

<p>pam_rootok &#8211; Gain only root access</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_rootok.so</code> [debug]</dl>
<h2>Description</h2>
<dd>pam_rootok is a PAM module that authenticates the user if their <i>UID</i> is <i>0</i>. Applications that are created setuid-root generally retain the <i>UID</i> of the user but run with the authority of an enhanced effective-UID. It is the real <i>UID</i> that is checked.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<h2>Module Types Provided</h2>
<p>The <code>auth</code>, <code>account</code> and <code>password</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The <i>UID</i> is <i>0</i>.</dl>
<p> PAM_AUTH_ERR</p>
<dl>
<dd>The <i>UID</i> is <code>not</code> <i>0</i>.</dl>
<h2>Examples</h2>
<p>In the case of the <code><a href="/docs/linux/man/1-su/">su</a></code>(1) application the historical usage is to permit the superuser to adopt the identity of a lesser user without the use of a password. To obtain this behavior with PAM the following pair of lines are needed for the corresponding entry in the /etc/pam.d/su configuration file:</p>
<dl>
<dd>
<pre># su authentication. Root is granted access by default.
auth sufficient pam_rootok.so
auth required pam_unix.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-su/">su</a></code>(1), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_rootok was written by Andrew G. Morgan, &lt;morgan [at] kernel.org&gt;.</p>
