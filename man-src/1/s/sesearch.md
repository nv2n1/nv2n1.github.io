---
title: "sesearch(1)"
name: "sesearch"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sesearch/"
description: "sesearch – SELinux policy query tool"
---

<h2>NAME</h2>
<p> sesearch &#8211; SELinux policy query tool</p>
<h2>SYNOPSIS</h2>
<p> <code>sesearch</code> [OPTIONS] RULE_TYPE [RULE_TYPE &#8230;] [EXPRESSION] [POLICY &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>sesearch</code> allows the user to search the rules in a SELinux policy.</p>
<h2>POLICY</h2>
<p> <code>sesearch</code> supports loading a SELinux policy in one of four formats.</p>
<dl>
<dt>source</p>
<dd> A single text file containing policy source for versions 12 through 21. This file is usually named policy.conf.</p>
<dt>binary</p>
<dd> A single file containing a monolithic kernel binary policy for versions 15 through 21. This file is usually named by version &#8211; for example, policy.20.</p>
<dt>modular</p>
<dd> A list of policy packages each containing a loadable policy module. The first module listed must be a base module.</p>
<dt>policy list</p>
<dd> A single text file containing all the information needed to load a policy, usually exported by SETools graphical utilities.</dl>
<p> If no policy file is provided, <code>sesearch</code> will search for the system default policy: checking first for a source policy, next for a binary policy matching the running kernel&#8217;s preferred version, and finally for the highest version that can be found. In the latter case, the policy will be downgraded to match the running system. If no policy can be found, <code>sesearch</code> will print an error message and exit.</p>
<h2>RULE TYPE OPTIONS</h2>
<p> <code>sesearch</code> is capable of searching multiple types of rules. At least one of the following must be provided to specify the desired type(s) of rules to search.</p>
<dl>
<dt>-A, &#8211;allow</p>
<dd> Search for allow rules.</p>
<dt>&#8211;neverallow</p>
<dd> Search for neverallow rules.</p>
<dt>&#8211;auditallow</p>
<dd> Search for auditallow rules.</p>
<dt>-D, &#8211;dontaudit</p>
<dd> Search for dontaudit rules.</p>
<dt>-T, &#8211;type</p>
<dd> Search for type_transition, type_member, and type_change rules.</p>
<dt>&#8211;role_allow</p>
<dd> Search for role allow rules.</p>
<dt>&#8211;role_trans</p>
<dd> Search for role_transition rules.</p>
<dt>&#8211;range_trans</p>
<dd> Search for range_transition rules.</p>
<dt>&#8211;all</p>
<dd> Search all rule types.</dl>
<h2>EXPRESSIONS</h2>
<p> The user may specify an expression containing values for a given field(s) in a rule. Only those fields applicable to a given rule type will be used; all other fields will be ignored. (For example, type_transition rules will ignore the permissions field.) If no expression is specified or if none of the specified fields apply to a given rule type, all rules of that type are considered to match the expression.</p>
<dl>
<dt>-s NAME, &#8211;source=NAME</p>
<dd> Find rules with type/attribute NAME as their source.</p>
<dt>-t NAME, &#8211;target=NAME</p>
<dd> Find rules with type/attribute NAME as their target.</p>
<dt>-D NAME, &#8211;default=NAME</p>
<dd> Find rules with type NAME as their default.</p>
<dt>&#8211;role_source=NAME</p>
<dd> Find rules with role NAME as their source.</p>
<dt>&#8211;role_target=NAME</p>
<dd> Find rules with role NAME as their target.</p>
<dt>-c NAME, &#8211;class=NAME</p>
<dd> Find rules with class NAME as their object class.</p>
<dt>-p P1[,P2,&#8230;] &#8211;perm=P1[,P2&#8230;]</p>
<dd> Find rules with at least one of the specified permissions. Multiple permissions may be specified as a comma separated list; it is recommended that this list be quoted for shells that interpret comma as a special character.</p>
<dt>-b NAME, &#8211;bool=NAME</p>
<dd> Find conditional rules with NAME in their conditional expression. This option will include rules in both the true and false lists of the conditional.</dl>
<h2>OPTIONS</h2>
<p> The following additional options exist to modify how the search is performed and the amount of information printed for each result.</p>
<dl>
<dt>-d, &#8211;direct</p>
<dd> Normally rules are matched using the type given or any of that type&#8217;s attributes (or an attribute&#8217;s types). This &quot;indirect&quot; matching also considers types used in complemented sets, the special set &quot;*&quot;, and the special target &quot;self&quot;. When the direct flag is given, matching is done literally. The rule must explicitly contain the given type (or attribute) for it to be returned.</p>
<dt>-R, &#8211;regex</p>
<dd> Use regular expressions to match symbol names. By default only exact string matches will be considered.</p>
<dt>-n, &#8211;linenum</p>
<dd> Print the line number for each rule. This option is ignored if using the &#8211;semantic option or if line numbers are not available for the given policy.</p>
<dt>-S, &#8211;semantic</p>
<dd> Search rules semantically instead of syntactically. This option is implied for policies for which syntactic rules are not available.</p>
<dt>-C, &#8211;show_cond</p>
<dd> Print the conditional expression and state for all conditional rules found. This option has no effect on unconditional rules.</p>
<dt>-h, &#8211;help</p>
<dd> Print help information and exit.</p>
<dt>-V, &#8211;version</p>
<dd> Print version information and exit.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Jeremy A. Mowery &lt;jmowery [at] tresys.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright(C) 2003-2008 Tresys Technology, LLC</p>
<h2>BUGS</h2>
<p> Please report bugs via an email to setools-bugs [at] tresys.com.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-seinfo/">seinfo</a>(1), <a href="/docs/linux/man/1-apol/">apol</a>(1) </p>
<h2>Index</h2>
