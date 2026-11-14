---
title: "pam_warn(8)"
name: "pam_warn"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_warn/"
description: "pam_warn – PAM module which logs all PAM items if called"
---

<p>pam_warn &#8211; PAM module which logs all PAM items if called</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_warn.so</code></dl>
<h2>Description</h2>
<dd>pam_warn is a PAM module that logs the service, terminal, user, remote user and remote host to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). The items are not probed for, but instead obtained from the standard PAM items. The module always returns <code>PAM_IGNORE</code>, indicating that it does not want to affect the authentication process.</p>
<h2>Options</h2>
<p>This module does not recognise any options.</p>
<h2>Module Types Provided</h2>
<p>The <code>auth</code>, <code>account</code>, <code>password</code> and <code>session</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_IGNORE</p>
<dl>
<dd>This module always returns PAM_IGNORE.</dl>
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
<p>pam_warn was written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;.</p>
