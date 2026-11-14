---
title: "auditsc_get_stamp(9)"
name: "auditsc_get_stamp"
section: "9"
letter: "a"
url: "/docs/linux/man/9-auditsc_get_stamp/"
---

auditsc_get_stamp - get local copies of audit_context values

<h2>Synopsis</h2>

<pre><code>int auditsc_get_stamp(struct audit_context *ctx, struct timespec *t, unsigned int *serial);</code></pre>

<h2>Arguments</h2>

<i>ctx</i>
<dl><dd><dd>audit_context for the task</dl>
 

 <i>t</i>
<dl><dd>timespec to store time recorded in the audit_context</dl>
 

 <i>serial</i>
<dl><dd>serial value that is recorded in the audit_context</dl>

<h2>Description</h2>

Also sets the context as auditable.

<h2>Copyright</h2>


