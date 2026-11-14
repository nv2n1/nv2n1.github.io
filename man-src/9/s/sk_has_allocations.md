---
title: "sk_has_allocations(9)"
name: "sk_has_allocations"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_has_allocations/"
description: "sk_has_allocations – check if allocations are outstanding"
---

<p>sk_has_allocations &#8211; check if allocations are outstanding</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool sk_has_allocations(const struct sock&nbsp;<wbr>*&nbsp;<wbr></code><i>sk</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>sk</i></p>
<dl>
<dd>
<dd>socket</dl>
<h2>Description</h2>
<p>Returns true if socket has write or read allocations</p>
<h2>Copyright</h2>
