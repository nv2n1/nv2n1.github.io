---
title: "sk_ns_capable(9)"
name: "sk_ns_capable"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_ns_capable/"
description: "sk_ns_capable – General socket capability test"
---

<p>sk_ns_capable &#8211; General socket capability test</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool sk_ns_capable(const struct sock&nbsp;<wbr>*&nbsp;<wbr></code><i>sk</i><code>, struct user_namespace&nbsp;<wbr>*&nbsp;<wbr></code><i>user_ns</i><code>, int&nbsp;<wbr></code><i>cap</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>sk</i></p>
<dl>
<dd>
<dd>Socket to use a capability on or through</dl>
<p> <i>user_ns</i></p>
<dl>
<dd>The user namespace of the capability to use</dl>
<p> <i>cap</i></p>
<dl>
<dd>The capability to use</dl>
<h2>Description</h2>
<p>Test to see if the opener of the socket had when the socket was created and the current process has the capability <i>cap</i> in the user namespace <i>user_ns</i>.</p>
<h2>Copyright</h2>
