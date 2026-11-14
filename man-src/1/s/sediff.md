---
title: "sediff(1)"
name: "sediff"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sediff/"
description: "sediff – SELinux policy difference tool"
---

<h2>NAME</h2>
<p> sediff &#8211; SELinux policy difference tool</p>
<h2>SYNOPSIS</h2>
<p> <code>sediff</code> [OPTIONS] [EXPRESSION] ORIGINAL_POLICY ; MODIFIED_POLICY</p>
<h2>DESCRIPTION</h2>
<p> <code>sediff</code> allows the user to inspect the semantic differences between two SELinux policies.</p>
<h2>POLICY</h2>
<p> <code>sediff</code> supports loading SELinux policies in one of four formats.</p>
<dl>
<dt>source</p>
<dd> A single text file containing policy source for versions 12 through 21. This file is usually named policy.conf.</p>
<dt>binary</p>
<dd> A single file containing a monolithic kernel binary policy for versions 15 through 21. This file is usually named by version &#8211; for example, policy.20.</p>
<dt>modular</p>
<dd> A list of policy packages each containing a loadable policy module. The first module listed must be a base module.</p>
<dt>policy list</p>
<dd> A single text file containing all the information needed to load a policy, usually exported by SETools graphical utilities.</dl>
<p> Policies do not need to be the same format. If not provided <code>sediff</code> will print an error message and exit.</p>
<h2>EXPRESSIONS</h2>
<p> The user may specify an expression listing the policy elements to differentiate. If not provided, all supported policy elements sans neverallows are examined.</p>
<dl>
<dt>-c, &#8211;class</p>
<dd> Find differences in permissions assigned to object classes and common permission sets.</p>
<dt>&#8211;level</p>
<dd> Find differences in categories authorized for MLS levels.</p>
<dt>&#8211;category</p>
<dd> Find differences in category definitions.</p>
<dt>-t, &#8211;type</p>
<dd> Find differences in attributes associated with types.</p>
<dt>-a, &#8211;attribute</p>
<dd> Find differences in types assigned to attributes.</p>
<dt>-r, &#8211;role</p>
<dd> Find differences in types authorized for roles.</p>
<dt>-u, &#8211;user</p>
<dd> Find differences in roles authorized for users.</p>
<dt>-b, &#8211;bool</p>
<dd> Find differences in the default values of booleans.</p>
<dt>-A, &#8211;allow</p>
<dd> Find differences in allow rules.</p>
<dt>&#8211;auditallow</p>
<dd> Find differences in auditallow rules.</p>
<dt>&#8211;dontaudit</p>
<dd> Find differences in dontaudit rules.</p>
<dt>&#8211;neverallow</p>
<dd> Find differences in neverallow rules.</p>
<dt>&#8211;type_trans</p>
<dd> Find differences in type_transition rules.</p>
<dt>&#8211;type_member</p>
<dd> Find differences in type_member rules.</p>
<dt>&#8211;type_change</p>
<dd> Find differences in type_change rules.</p>
<dt>&#8211;role_trans</p>
<dd> Find differences in role_transition rules. This includes differences in the default role.</p>
<dt>&#8211;role_allow</p>
<dd> Find differences in role allow rules.</p>
<dt>&#8211;range_trans</p>
<dd> Find differences in range_transition rules. This includes differences in the target MLS range.</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-q, &#8211;quiet</p>
<dd> If there are no differences for elements of a given kind, suppress status output for that kind of element.</p>
<dt>&#8211;stats</p>
<dd> Print difference statistics only.</p>
<dt>-h, &#8211;help</p>
<dd> Print help information and exit.</p>
<dt>-V, &#8211;version</p>
<dd> Print version information and exit.</dl>
<h2>DIFFERENCES</h2>
<p> <code>sediff</code> categorizes differences in policy elements into one of three forms.</p>
<dl>
<dt>
<dd>
<dl>
<dt>added</p>
<dd> The element exists only in the modified policy.</p>
<dt>removed</p>
<dd> The element exists only in the original policy.</p>
<dt>modified</p>
<dd> The element exists in both policies but its semantic meaning has changed. For example, a class is modified if one or more permissions are added or removed.</dl>
</dl>
<p> For all rules with types as their source or target, two additional forms of difference are recognized. This helps distinguish differences due to new types from differences in rules for existing types.</p>
<dl>
<dt>
<dd>
<dl>
<dt>added, new type</p>
<dd> The rule exists only in the modified policy; furthermore, one or more of the types in the rule do not exist in the original policy.</p>
<dt>removed, missing type</p>
<dd> The rule exists only in the original policy; furthermore, one or more of the types in the rule do not exist in the modified policy.</dl>
</dl>
<h2>NOTE</h2>
<p> Most shells interpret the semicolon as a metacharacter, thus requiring a backslash like so: <code>sediff original.policy \; modified.policy</code></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Jeremy A. Mowery &lt;jmowery [at] tresys.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright(C) 2004-2007 Tresys Technology, LLC</p>
<h2>BUGS</h2>
<p> Please report bugs via an email to setools-bugs [at] tresys.com.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sediffx/">sediffx</a>(1) </p>
<h2>Index</h2>
