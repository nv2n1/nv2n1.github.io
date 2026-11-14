---
title: "audit_log_format(9)"
name: "audit_log_format"
section: "9"
letter: "a"
url: "/docs/linux/man/9-audit_log_format/"
---

audit_log_format - format a message into the audit buffer.

<h2>Synopsis</h2>

<pre><code>void audit_log_format(struct audit_buffer *ab, const char *fmt, ...);</code></pre>

<h2>Arguments</h2>

<i>ab</i>
<dl><dd><dd>audit_buffer</dl>
 

 <i>fmt</i>
<dl><dd>format string</dl>
 

 <i>...</i>
<dl><dd>optional parameters matching <i>fmt</i> string</dl>

<h2>Description</h2>

All the work is done in audit_log_vformat.

<h2>Copyright</h2>


