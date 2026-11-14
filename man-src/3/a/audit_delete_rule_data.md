---
title: "audit_delete_rule_data(3)"
name: "audit_delete_rule_data"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_delete_rule_data/"
description: "audit_delete_rule_data – Delete audit rule"
---

<h2>NAME</h2>
<p> audit_delete_rule_data &#8211; Delete audit rule</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_delete_rule_data (int fd, struct audit_rule_data *rule, int flags, int action); </p>
<h2>DESCRIPTION</h2>
<p> audit_delete_rule_data is used to delete rules that are currently loaded in the kernel. To delete a rule, you must set up the rules identical to the one being deleted. See audit_add_rule_data for flag and action definitions. </p>
<h2>RETURN VALUE</h2>
<p> The return value is &lt;= 0 on error, otherwise it is the netlink sequence id number. This function can have any error that sendto would encounter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_add_rule_data/">audit_add_rule_data</a></code>(3), <code><a href="/docs/linux/man/8-auditctl/">auditctl</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
