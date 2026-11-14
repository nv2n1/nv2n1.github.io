---
title: "unix_update(8)"
name: "unix_update"
section: "8"
letter: "u"
url: "/docs/linux/man/8-unix_update/"
description: "unix_update – Helper binary that updates the password of a given user"
---

<p>unix_update &#8211; Helper binary that updates the password of a given user</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>unix_update</code> [&#8230;]</dl>
<h2>Description</h2>
<p><i>unix_update</i></p>
<dd>is a helper program for the <i>pam_unix</i> module that updates the password of a given user. It is not intended to be run directly from the command line and logs a security violation if done so. </p>
<p> The purpose of the helper is to enable tighter confinement of login and password changing services. The helper is thus called only when SELinux is enabled on the system. </p>
<p> The interface of the helper &#8211; command line options, and input/output data format are internal to the <i>pam_unix</i> module and it should not be called directly from applications.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_unix/">pam_unix</a></code>(8)</p>
<h2>Author</h2>
<p>Written by Tomas Mraz and other various people.</p>
