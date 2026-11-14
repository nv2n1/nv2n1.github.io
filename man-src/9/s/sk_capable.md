---
title: "sk_capable(9)"
name: "sk_capable"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_capable/"
description: "sk_capable – Socket global capability test"
---

<p>sk_capable &#8211; Socket global capability test</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool sk_capable(const struct sock&nbsp;<wbr>*&nbsp;<wbr></code><i>sk</i><code>, int&nbsp;<wbr></code><i>cap</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>sk</i></p>
<dl>
<dd>
<dd>Socket to use a capability on or through</dl>
<p> <i>cap</i></p>
<dl>
<dd>The global capability to use</dl>
<h2>Description</h2>
<p>Test to see if the opener of the socket had when the socket was created and the current process has the capability <i>cap</i> in all user namespaces.</p>
<h2>Copyright</h2>
