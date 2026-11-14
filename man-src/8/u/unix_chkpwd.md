---
title: "unix_chkpwd(8)"
name: "unix_chkpwd"
section: "8"
letter: "u"
url: "/docs/linux/man/8-unix_chkpwd/"
description: "unix_chkpwd – Helper binary that verifies the password of the current user"
---

<p>unix_chkpwd &#8211; Helper binary that verifies the password of the current user</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>unix_chkpwd</code> [&#8230;]</dl>
<h2>Description</h2>
<p><i>unix_chkpwd</i></p>
<dd>is a helper program for the <i>pam_unix</i> module that verifies the password of the current user. It also checks password and account expiration dates in <i>shadow</i>. It is not intended to be run directly from the command line and logs a security violation if done so. </p>
<p> It is typically installed setuid root or setgid shadow. </p>
<p> The interface of the helper &#8211; command line options, and input/output data format are internal to the <i>pam_unix</i> module and it should not be called directly from applications.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_unix/">pam_unix</a></code>(8)</p>
<h2>Author</h2>
<p>Written by Andrew Morgan and other various people.</p>
