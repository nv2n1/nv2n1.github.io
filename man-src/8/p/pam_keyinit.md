---
title: "pam_keyinit(8)"
name: "pam_keyinit"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_keyinit/"
description: "pam_keyinit – Kernel session keyring initialiser module"
---

<p>pam_keyinit &#8211; Kernel session keyring initialiser module</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_keyinit.so</code> [debug] [force] [revoke]</dl>
<h2>Description</h2>
<dd>The pam_keyinit PAM module ensures that the invoking process has a session keyring other than the user default session keyring. </p>
<p> The module checks to see if the process&#8217;s session keyring is the <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7), and, if it is, creates a new <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7) with which to replace it. If a new session keyring is created, it will install a link to the <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7) in the session keyring so that keys common to the user will be automatically accessible through it. The session keyring of the invoking process will thenceforth be inherited by all its children unless they override it. </p>
<p> In order to allow other PAM modules to attach tokens to the keyring, this module provides both an <i>auth</i> (limited to <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3) and a <i>session</i> component. The session keyring is created in the module called. Moreover this module should be included as early as possible in a PAM configuration. </p>
<p> This module is intended primarily for use by login processes. Be aware that after the session keyring has been replaced, the old session keyring and the keys it contains will no longer be accessible. </p>
<p> This module should not, generally, be invoked by programs like <code>su</code>, since it is usually desirable for the key set to percolate through to the alternate context. The keys have their own permissions system to manage this. </p>
<p> The keyutils package is used to manipulate keys more directly. This can be obtained from: </p>
<p> m[blue]<code>Keyutils</code>m[]<font SIZE="-2">[1]</font></p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Log debug information with <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> <code>force</code></p>
<dl>
<dd>Causes the session keyring of the invoking process to be replaced unconditionally.</dl>
<p> <code>revoke</code></p>
<dl>
<dd>Causes the session keyring of the invoking process to be revoked when the invoking process exits if the session keyring was created for this process in the first place.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>session</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>This module will usually return this value</dl>
<p> PAM_AUTH_ERR</p>
<dl>
<dd>Authentication failure.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>The return value should be ignored by PAM dispatch.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>Cannot determine the user name.</dl>
<p> PAM_SESSION_ERR</p>
<dl>
<dd>This module will return this value if its arguments are invalid or if a system error such as ENOMEM occurs.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User not known.</dl>
<h2>Examples</h2>
<p>Add this line to your login entries to start each login session with its own session keyring: </p>
<dl>
<dd>
<pre>session required pam_keyinit.so</pre>
</dl>
<p> This will prevent keys from one session leaking into another session for the same user.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7), <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1)</p>
<h2>Author</h2>
<p>pam_keyinit was written by David Howells, &lt;dhowells [at] redhat.com&gt;.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Keyutils</p>
<dl>
<dd><a rel="nofollow" href="http://people.redhat.com/~dhowells/keyutils/">http://people.redhat.com/~dhowells/keyutils/</a></dl>
