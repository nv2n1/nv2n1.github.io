---
title: "audit_get_session(3)"
name: "audit_get_session"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_get_session/"
description: "audit_getloginuid – Get a program’s login session id value"
---

<h2>NAME</h2>
<p> audit_getloginuid &#8211; Get a program&#8217;s login session id value</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> uin32_t audit_get_session(void); </p>
<h2>DESCRIPTION</h2>
<p> This function returns the task&#8217;s session id attribute. </p>
<h2>RETURN VALUE</h2>
<p> This function returns the session id value if it was set. It will return a -1 if the session id is unset. However, since uint32_t is an unsigned type, you will see the converted value instead of -1. </p>
<h2>ERRORS</h2>
<p> This function returns -2 on failure. Additionally, in the event of a real error, errno would be set. The function can set errno based on failures of open, read, or strtoul. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_getloginuid/">audit_getloginuid</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
