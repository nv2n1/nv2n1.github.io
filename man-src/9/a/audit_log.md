---
title: "audit_log(9)"
name: "audit_log"
section: "9"
letter: "a"
url: "/docs/linux/man/9-audit_log/"
---

audit_log - Log an audit record

<h2>Synopsis</h2>

<pre><code>void audit_log(struct audit_context *ctx, gfp_t gfp_mask, int type, const char *fmt, ...);</code></pre>

<h2>Arguments</h2>

<i>ctx</i>
<dl><dd><dd>audit context</dl>
 

 <i>gfp_mask</i>
<dl><dd>type of allocation</dl>
 

 <i>type</i>
<dl><dd>audit message type</dl>
 

 <i>fmt</i>
<dl><dd>format string to use</dl>
 

 <i>...</i>
<dl><dd>variable parameters matching the format string</dl>

<h2>Description</h2>

This is a convenience function that calls audit_log_start, audit_log_vformat, and audit_log_end. It may be called in any context.

<h2>Copyright</h2>


