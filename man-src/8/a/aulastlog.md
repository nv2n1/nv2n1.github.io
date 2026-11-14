---
title: "aulastlog(8)"
name: "aulastlog"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aulastlog/"
description: "aulastlog – a program similar to lastlog"
---

<p>aulastlog &#8211; a program similar to lastlog</p>
<h2>Synopsis</h2>
<p><code>aulastlog [ options ]</code></p>
<h2>Description</h2>
<p><code>aulastlog</code> is a program that prints out the last login for all users of the <code>local</code> machine similar to the way lastlog does. The login-name, port, and last login time will be printed. If the user has never logged in, the message <code>** Never logged in**</code> will be displayed instead of the port and time. </p>
<h2>Options</h2>
<dl>
<dt><code>-u, &#8211;user</code></p>
<dd>Print the lastlog record for user with specified LOGIN only.</p>
<dt><code>&#8211;stdin</code></p>
<dd>Use stdin as the source of audit records. The audit events must be in the raw format.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lastlog/">lastlog</a></code>(8), <code><a href="/docs/linux/man/8-ausearch/">ausearch</a></code>(8), <code><a href="/docs/linux/man/8-aureport/">aureport</a></code>(8). </p>
<h2>Author</h2>
<p>Steve Grubb</p>
