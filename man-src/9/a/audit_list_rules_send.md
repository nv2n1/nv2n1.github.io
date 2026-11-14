---
title: "audit_list_rules_send(9)"
name: "audit_list_rules_send"
section: "9"
letter: "a"
url: "/docs/linux/man/9-audit_list_rules_send/"
---

audit_list_rules_send - list the audit rules

<h2>Synopsis</h2>

<pre><code>int audit_list_rules_send(struct sk_buff *request_skb, int seq);</code></pre>

<h2>Arguments</h2>

<i>request_skb</i>
<dl><dd><dd>skb of request we are replying to (used to target the reply)</dl>
 

 <i>seq</i>
<dl><dd>netlink audit message sequence (serial) number</dl>

<h2>Copyright</h2>


