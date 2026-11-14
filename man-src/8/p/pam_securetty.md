---
title: "pam_securetty(8)"
name: "pam_securetty"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_securetty/"
description: "pam_securetty – Limit root login to special devices"
---

<p>pam_securetty &#8211; Limit root login to special devices</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_securetty.so</code> [debug]</dl>
<h2>Description</h2>
<dd>pam_securetty is a PAM module that allows root logins only if the user is logging in on a &quot;secure&quot; tty, as defined by the listing in the securetty file. pam_securetty checks at first, if /etc/securetty exists. If not and it was built with vendordir support, it will use &lt;vendordir&gt;/securetty. pam_securetty also checks that the securetty files are plain files and not world writable. It will also allow root logins on the tty specified with <code>console=</code> switch on the kernel command line and on ttys from the /sys/class/tty/console/active. </p>
<p> This module has no effect on non-root users and requires that the application fills in the <code>PAM_TTY</code> item correctly. </p>
<p> For canonical usage, should be listed as a <code>required</code> authentication method before any <code>sufficient</code> authentication methods.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>noconsole</code></p>
<dl>
<dd>Do not automatically allow root logins on the kernel console device, as specified on the kernel command line or by the sys file, if it is not also specified in the securetty file.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>auth</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The user is allowed to continue authentication. Either the user is not root, or the root user is trying to log in on an acceptable device.</dl>
<p> PAM_AUTH_ERR</p>
<dl>
<dd>Authentication is rejected. Either root is attempting to log in via an unacceptable device, or the securetty file is world writable or not a normal file.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_CONV_ERR</p>
<dl>
<dd>The conversation method supplied by the application failed to obtain the username.</dl>
<p> PAM_INCOMPLETE</p>
<dl>
<dd>The conversation method supplied by the application returned PAM_CONV_AGAIN.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>An error occurred while the module was determining the user&#8217;s name or tty, or the module could not open the securetty file.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>The module could not find the user name in the /etc/passwd file to verify whether the user had a UID of 0. Therefore, the results of running this module are ignored.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>auth required pam_securetty.so
auth required pam_unix.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-securetty/">securetty</a></code>(5), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_securetty was written by Elliot Lee &lt;sopwith [at] cuc.edu&gt;.</p>
