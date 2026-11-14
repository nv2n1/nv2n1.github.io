---
title: "audit_update_watch_perms(3)"
name: "audit_update_watch_perms"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_update_watch_perms/"
description: "audit_update_watch_perms – update permissions field of watch command"
---

<h2>NAME</h2>
<p> audit_update_watch_perms &#8211; update permissions field of watch command</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_update_watch_perms(struct audit_rule_data *rule, int perms); </p>
<h2>DESCRIPTION</h2>
<p> audit_update_watch_perms adds the permission checks to a watch command that is being built. The perms are a bitwise or&#8217;ing of: AUDIT_PERM_EXEC, AUDIT_PERM_WRITE, AUDIT_PERM_READ, AUDIT_PERM_ATTR. </p>
<h2>RETURN VALUE</h2>
<p> Returns a number &lt; 0 if an error occurs; otherwise, 0 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_add_rule_data/">audit_add_rule_data</a></code>(3), <code><a href="/docs/linux/man/3-audit_add_watch/">audit_add_watch</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
