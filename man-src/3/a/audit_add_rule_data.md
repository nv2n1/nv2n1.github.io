---
title: "audit_add_rule_data(3)"
name: "audit_add_rule_data"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_add_rule_data/"
description: "audit_add_rule_data – Add new audit rule"
---

<h2>NAME</h2>
<p> audit_add_rule_data &#8211; Add new audit rule</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_add_rule_data (int fd, struct audit_rule_data *rule, int flags, int action); </p>
<h2>DESCRIPTION</h2>
<p> audit_add_rule adds an audit rule previously constructed with <a href="/docs/linux/man/3-audit_rule_fieldpair_data/">audit_rule_fieldpair_data</a>(3) to one of several kernel event filters. The filter is specified by the flags argument. Possible values for flags are: </p>
<dl>
<dt>&bull;</p>
<dd> AUDIT_FILTER_USER &#8211; Apply rule to userspace generated messages.</p>
<dt>&bull;</p>
<dd> AUDIT_FILTER_TASK &#8211; Apply rule at task creation (not syscall).</p>
<dt>&bull;</p>
<dd> AUDIT_FILTER_EXIT &#8211; Apply rule at syscall exit.</p>
<dt>&bull;</p>
<dd> AUDIT_FILTER_TYPE &#8211; Apply rule at audit_log_start.</dl>
<p> The rule&#8217;s action has two possible values: </p>
<dl>
<dt>&bull;</p>
<dd> AUDIT_NEVER &#8211; Do not build context if rule matches.</p>
<dt>&bull;</p>
<dd> AUDIT_ALWAYS &#8211; Generate audit record if rule matches.</dl>
<h2>RETURN VALUE</h2>
<p> The return value is &lt;= 0 on error, otherwise it is the netlink sequence id number. This function can have any error that sendto would encounter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_rule_fieldpair_data/">audit_rule_fieldpair_data</a>(3),</code> <code><a href="/docs/linux/man/3-audit_delete_rule_data/">audit_delete_rule_data</a></code>(3), <code><a href="/docs/linux/man/8-auditctl/">auditctl</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb. </p>
<h2>Index</h2>
