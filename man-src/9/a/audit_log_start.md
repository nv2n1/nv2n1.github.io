---
title: "audit_log_start(9)"
name: "audit_log_start"
section: "9"
letter: "a"
url: "/docs/linux/man/9-audit_log_start/"
---

audit_log_start - obtain an audit buffer

<h2>Synopsis</h2>

<pre><code>struct audit_buffer *audit_log_start(struct audit_context *ctx, gfp_t gfp_mask, int type);</code></pre>

<h2>Arguments</h2>

<i>ctx</i>
<dl><dd><dd>audit_context (may be NULL)</dl>
 

 <i>gfp_mask</i>
<dl><dd>type of allocation</dl>
 

 <i>type</i>
<dl><dd>audit message type</dl>

<h2>Description</h2>

Returns audit_buffer pointer on success or NULL on error. 

 Obtain an audit buffer. This routine does locking to obtain the audit buffer, but then no locking is required for calls to audit_log_*format. If the task (ctx) is a task that is currently in a syscall, then the syscall is marked as auditable and an audit record will be written at syscall exit. If there is no associated task, then task context (ctx) should be NULL.

<h2>Copyright</h2>


