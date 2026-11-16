---
title: "audit_rule_change(9)"
name: "audit_rule_change"
section: "9"
letter: "a"
url: "/docs/linux/man/9-audit_rule_change/"
---

audit_rule_change - apply all rules to the specified message type

<h2>Synopsis</h2>

<pre><code>int audit_rule_change(int type, __u32 portid, int seq, void *data, size_t datasz);</code></pre>

<h2>Arguments</h2>

<i>type</i>
<dl><dd></dd><dd>audit message type</dd></dl>
 

 <i>portid</i>
<dl><dd>target port id for netlink audit messages</dd></dl>
 

 <i>seq</i>
<dl><dd>netlink audit message sequence (serial) number</dd></dl>
 

 <i>data</i>
<dl><dd>payload data</dd></dl>
 

 <i>datasz</i>
<dl><dd>size of payload data</dd></dl>

<h2>Copyright</h2>


