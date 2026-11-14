---
title: "audit_log_end(9)"
name: "audit_log_end"
section: "9"
letter: "a"
url: "/docs/linux/man/9-audit_log_end/"
description: "audit_log_end – end one audit record"
---

<p>audit_log_end &#8211; end one audit record</p>
<h2>Synopsis</h2>
<pre><code>void audit_log_end(struct audit_buffer *ab);</code></pre>
<h2>Arguments</h2>
<p><i>ab</i></p>
<dl>
<dd>
<dd>the audit_buffer</dl>
<h2>Description</h2>
<p><code>netlink_unicast</code> cannot be called inside an irq context because it blocks (last arg, flags, is not set to MSG_DONTWAIT), so the audit buffer is placed on a queue and a tasklet is scheduled to remove them from the queue outside the irq context. May be called in any context.</p>
<h2>Copyright</h2>
