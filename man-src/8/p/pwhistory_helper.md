---
title: "pwhistory_helper(8)"
name: "pwhistory_helper"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pwhistory_helper/"
description: "pwhistory_helper – Helper binary that transfers password hashes from passwd or shadow to opasswd"
---

<p>pwhistory_helper &#8211; Helper binary that transfers password hashes from passwd or shadow to opasswd</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pwhistory_helper</code> [&#8230;]</dl>
<h2>Description</h2>
<p><i>pwhistory_helper</i></p>
<dd>is a helper program for the <i>pam_pwhistory</i> module that transfers password hashes from passwd or shadow file to the opasswd file and checks a password supplied by user against the existing hashes in the opasswd file. </p>
<p> The purpose of the helper is to enable tighter confinement of login and password changing services. The helper is thus called only when SELinux is enabled on the system. </p>
<p> The interface of the helper &#8211; command line options, and input/output data format are internal to the <i>pam_pwhistory</i> module and it should not be called directly from applications.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_pwhistory/">pam_pwhistory</a></code>(8)</p>
<h2>Author</h2>
<p>Written by Tomas Mraz based on the code originally in <i>pam_pwhistory and pam_unix</i> modules.</p>
