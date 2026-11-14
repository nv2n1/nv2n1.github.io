---
title: "pam_nologin(8)"
name: "pam_nologin"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_nologin/"
description: "pam_nologin – Prevent non-root users from login"
---

<p>pam_nologin &#8211; Prevent non-root users from login</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_nologin.so</code> [file=<i>/path/nologin</i>] [successok]</dl>
<h2>Description</h2>
<dd>pam_nologin is a PAM module that prevents users from logging into the system when /var/run/nologin or /etc/nologin exists. The contents of the file are displayed to the user. The pam_nologin module has no effect on the root user&#8217;s ability to log in.</p>
<h2>Options</h2>
<p><code>file=</code><i>/path/nologin</i></p>
<dl>
<dd>Use this file instead the default /var/run/nologin or /etc/nologin.</dl>
<p> <code>successok</code></p>
<dl>
<dd>Return PAM_SUCCESS if no file exists, the default is PAM_IGNORE.</dl>
<h2>Module Types Provided</h2>
<p>The <code>auth</code> and <code>account</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>The user is not root and /etc/nologin exists, so the user is not permitted to log in.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>This is the default return value.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Success: either the user is root or the nologin file does not exist.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User not known to the underlying authentication module.</dl>
<h2>Examples</h2>
<p>The suggested usage for /etc/pam.d/login is:</p>
<dl>
<dd>
<pre>auth required pam_nologin.so</pre>
</dl>
<h2>Notes</h2>
<p>In order to make this module effective, all login methods should be secured by it. It should be used as a <i>required</i> method listed before any <i>sufficient</i> methods in order to get standard Unix nologin semantics. Note, the use of <code>successok</code> module argument causes the module to return <i>PAM_SUCCESS</i> and as such would break such a configuration &#8211; failing <i>sufficient</i> modules would lead to a successful login because the nologin module <i>succeeded</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-nologin/">nologin</a></code>(5), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_nologin was written by Michael K. Johnson &lt;johnsonm [at] redhat.com&gt;.</p>
