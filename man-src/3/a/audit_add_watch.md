---
title: "audit_add_watch(3)"
name: "audit_add_watch"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_add_watch/"
description: "audit_add_watch – create a rule layout for a watch"
---

<h2>NAME</h2>
<p> audit_add_watch &#8211; create a rule layout for a watch</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_add_watch(struct audit_rule_data **rulep, const char *path); </p>
<h2>DESCRIPTION</h2>
<p> audit_add_watch will create a watch rule in the pointer to a pointer rulep. All that you need to pass it is the full path to a file and it will initialize the audit_rule_data structure for a watch. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs; otherwise, 0 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_add_rule_data/">audit_add_rule_data</a></code>(3), <code><a href="/docs/linux/man/3-audit_delete_rule_data/">audit_delete_rule_data</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
