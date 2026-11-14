---
title: "audit_getloginuid(3)"
name: "audit_getloginuid"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_getloginuid/"
description: "audit_getloginuid – Get a program’s loginuid value"
---

<h2>NAME</h2>
<p> audit_getloginuid &#8211; Get a program&#8217;s loginuid value</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> uid_t audit_getloginuid(void); </p>
<h2>DESCRIPTION</h2>
<p> This function returns the task attribute loginuid. </p>
<h2>RETURN VALUE</h2>
<p> This function returns the loginuid value if it was set. It will return a -1 if loginuid was unset. However, since uid_t is an unsigned type, you will see the converted value instead of -1. </p>
<h2>ERRORS</h2>
<p> This function returns -1 on failure. However, in the event of a real error, errno would be set. The function can set errno based on failures of open, read, or strtoul. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_setloginuid/">audit_setloginuid</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
