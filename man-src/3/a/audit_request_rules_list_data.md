---
title: "audit_request_rules_list_data(3)"
name: "audit_request_rules_list_data"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_request_rules_list_data/"
description: "audit_request_rules_list_data – Request list of current audit rules"
---

<h2>NAME</h2>
<p> audit_request_rules_list_data &#8211; Request list of current audit rules</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_request_rules_list_data (int fd); </p>
<h2>DESCRIPTION</h2>
<p> audit_request_rules_list_data sends a request to the kernel to list the current audit rules. The rules are sent back one after another after this request is issued. </p>
<h2>RETURN VALUE</h2>
<p> The return value is &lt;= 0 on error, otherwise it is the netlink sequence id number. This function can have any error that sendto would encounter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_add_rule_data/">audit_add_rule_data</a></code>(3), <code><a href="/docs/linux/man/3-audit_delete_rule_data/">audit_delete_rule_data</a></code>(3), <code><a href="/docs/linux/man/3-audit_open/">audit_open</a></code>(3), <code><a href="/docs/linux/man/8-auditctl/">auditctl</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
