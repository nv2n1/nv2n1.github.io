---
title: "audit_log_secctx(9)"
name: "audit_log_secctx"
section: "9"
letter: "a"
url: "/docs/linux/man/9-audit_log_secctx/"
---

audit_log_secctx - Converts and logs SELinux context

<h2>Synopsis</h2>

<pre><code>void audit_log_secctx(struct audit_buffer *ab, u32 secid);</code></pre>

<h2>Arguments</h2>

<i>ab</i>
<dl><dd><dd>audit_buffer</dl>
 

 <i>secid</i>
<dl><dd>security number</dl>

<h2>Description</h2>

This is a helper function that calls security_secid_to_secctx to convert secid to secctx and then adds the (converted) SELinux context to the audit log by calling audit_log_format, thus also preventing leak of internal secid to userspace. If secid cannot be converted audit_panic is called.

<h2>Copyright</h2>


