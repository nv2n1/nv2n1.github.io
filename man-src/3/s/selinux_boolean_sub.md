---
title: "selinux_boolean_sub(3)"
name: "selinux_boolean_sub"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_boolean_sub/"
description: "selinux_boolean_sub – Search the translated name for a boolean_name record"
---

<p>selinux_boolean_sub &#8211; Search the translated name for a boolean_name record</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
char *selinux_boolean_sub(const char *boolean_name);
</code></pre>
<h2>Description</h2>
<p><code>selinux_boolean_sub</code>() searches the <i>/etc/selinux/{POLICYTYPE}/booleans.subs_dist</i> file for a matching boolean_name record. If the record exists the boolean substitution name is returned. If not <code>selinux_boolean_sub</code>() returns the original <i>boolean_name</i>. </p>
<h2>Return Value</h2>
<p><code>selinux_boolean_sub</code>() returns the <i>boolean_name</i> or the substituted name on success. The returned value must be freed with <code><a href="/docs/linux/man/3-free/">free</a></code>(3). <code>selinux_boolean_sub</code>() returns NULL on error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-security_get_boolean_names/">security_get_boolean_names</a></code>(3) </p>
