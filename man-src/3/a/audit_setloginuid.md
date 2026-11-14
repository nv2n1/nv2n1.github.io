---
title: "audit_setloginuid(3)"
name: "audit_setloginuid"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_setloginuid/"
description: "audit_setloginuid – Set a program’s loginuid value"
---

<h2>NAME</h2>
<p> audit_setloginuid &#8211; Set a program&#8217;s loginuid value</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_setloginuid(uid_t uid); </p>
<h2>DESCRIPTION</h2>
<p> This function sets the task attribute loginuid with the value of uid. The loginuid value may only be set by programs with the CAP_AUDIT_CONTROL capability. This normally means the root account. </p>
<p> The loginuid value is part of the task structure and is inheritted by child processes. It is used to track what account a user gained system access with. All system entry point programs should set this value right before changing to the uid of the user granted access so that audit events are properly attributed to the that user. </p>
<h2>RETURN VALUE</h2>
<p> This function returns 0 on success and non-zero otherwise. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_getloginuid/">audit_getloginuid</a></code>(3), <code><a href="/docs/linux/man/8-pam_loginuid/">pam_loginuid</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
