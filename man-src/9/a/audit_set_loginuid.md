---
title: "audit_set_loginuid(9)"
name: "audit_set_loginuid"
section: "9"
letter: "a"
url: "/docs/linux/man/9-audit_set_loginuid/"
description: "audit_set_loginuid – set current task’s audit_context loginuid"
---

<p>audit_set_loginuid &#8211; set current task&#8217;s audit_context loginuid</p>
<h2>Synopsis</h2>
<pre><code>int audit_set_loginuid(kuid_t loginuid);</code></pre>
<h2>Arguments</h2>
<p><i>loginuid</i></p>
<dl>
<dd>
<dd>loginuid value</dl>
<h2>Description</h2>
<p>Returns 0. </p>
<p> Called (set) from fs/proc/base.c::<code>proc_loginuid_write</code>.</p>
<h2>Copyright</h2>
