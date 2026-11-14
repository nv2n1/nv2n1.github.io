---
title: "nologin(8)"
name: "nologin"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nologin/"
description: "nologin – politely refuse a login"
---

<p>nologin &#8211; politely refuse a login</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>nologin</code></dl>
<h2>Description</h2>
<dd>The <code>nologin</code> command displays a message that an account is not available and exits non-zero. It is intended as a replacement shell field for accounts that have been disabled. </p>
<p> To disable all logins, investigate <code><a href="/docs/linux/man/5-nologin/">nologin</a></code>(5). </p>
<p> If <code>SSH_ORIGINAL_COMMAND</code> is populated it will be logged.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/5-nologin/">nologin</a></code>(5).</p>
<h2>History</h2>
<p>The <code>nologin</code> command appeared in BSD 4.4.</p>
