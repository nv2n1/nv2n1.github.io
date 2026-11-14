---
title: "sge_resource_quota(5)"
name: "sge_resource_quota"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_resource_quota/"
description: "xxqs_name_sxx_resource_quota – xxQS_NAMExx resource quota file format"
---

<p>xxqs_name_sxx_resource_quota &#8211; xxQS_NAMExx resource quota file format</p>
<h2>Description</h2>
<p>Resource quota sets (RQS) are a flexible way to set a maximum resource consumption for any job requests. They are used by the scheduler to select the next possible jobs for running. The job request quota application is done according to a set of user, project, cluster queue, host and PE filter criteria. RQS are applied to resource requests before considering the amount of resources defined (in order) at the global, host, and queue levels. If an RQS denies the request the other levels are not considered. </p>
<p> By using resource quota sets, administrators can define a fine-grained quota configuration, restricting some job requests to lesser resource usage and granting others higher usage. </p>
<p> Note: Jobs requesting an Advance Reservation (AR) are not honored by RQS, and are neither subject to the resulting limit, nor debited in the usage consumption. </p>
<p> A list of currently configured RQS can be displayed via the <code>-srqsl</code> option. The contents of each listed rqs definition can be shown via the <code>-srqs</code> switch. The output follows the format described below. New RQS can be created, and existing ones modified, via the <code>-arqs</code>, <code>-mrqs</code> and <code>-drqs</code> options to </p>
<p> A resource quota set defines a maximum resource quota for a particular job request. All of the configured and enabled rule sets apply all of the time. This means that if multiple resource quota sets are defined, the most restrictive set is used. </p>
<p> Every resource quota set consists of one or more resource quota rules. These rules are evaluated in order, and the first rule that matches a specific request will be used. A resource quota set always results in at most one effective resource quota rule for a specific request. </p>
<p> Note, xxQS_NAMExx allows backslashes (\) be used to escape newline characters. The backslash and the newline are replaced with a space character before any interpretation.</p>
<h2>Format</h2>
<p>A resource quota set definition contains the following parameters one per-line in braces which enclose the whole set. See below for the formal syntax.</p>
<h3><code>name</code></h3>
<p>The resource quota set name.</p>
<h3><code>enabled</code></h3>
<p>If set to <i>true</i> the resource quota set is active and will be considered for scheduling decisions. The default value is <i>false</i>.</p>
<h3><code>description</code></h3>
<p>This description field is optional and can be set to an arbitrary string. The default value is <i>NONE</i>.</p>
<h3><code>limit</code></h3>
<p>Every resource quota set needs at least one resource quota rule definition, started by the limit field. It is possible to define multiple resource quota rules, separated by a new line, processed in order top to bottom. </p>
<p> A resource quota rule consists of an optional name, the filters for a specific job request, and the resource quota limit. </p>
<p> The tags for expressing a resource quota rule are:</p>
<dl>
<dt>name</p>
<dd>The name of the rule (optional). The rule name must be unique within a resource quota set.</p>
<dt>users</p>
<dd>Contains a comma-separated list of user names or ACLs (see This parameter filters jobs by user or ACL in the list. Any user not in the list will not be considered for the resource quota rule. The default value is &#8216;*&#8217;, which means all users. An ACL is differentiated from a user name by prefixing the ACL name with &#8216;@&#8217;. To exclude a user or ACL from the rule, the name can be prefixed with &#8216;!&#8217;. The defined user or ACL names need not exist in the xxQS_NAMExx configuration.</p>
<dt>projects</p>
<dd>Contains a comma-separated list of projects (see This parameter filters jobs requesting a project in the list. Any project not in the list will not be considered for the resource quota rule. If no project filter is specified, all projects, and jobs with no requested project, match the rule. The value &#8216;*&#8217; means all jobs with requested projects. To exclude a project from the rule, the name can be prefixed with &#8216;!&#8217;. The value &#8216;!*&#8217; means only jobs with no project requested.</p>
<dt>pes</p>
<dd>Contains a comma-separated list of PEs (see This parameter filters jobs requesting a PE in the list. Any PE not in the list will not be considered for the resource quota rule. If no PE filter is specified, all PEs, and jobs with no requested PE, match the rule. The value &#8216;*&#8217; means all jobs requesting a PE. To exclude a PE from the rule, the name can be prefixed with &#8216;!&#8217;. The value &#8216;!*&#8217; means only jobs with no PE requested.</p>
<dt>queues</p>
<dd>Contains a comma-separated list of cluster queues (see This parameter filters jobs that may be scheduled in a queue in the list. Any queue not in the list will not be considered for the resource quota rule. The default value is &#8216;*&#8217;, which means all queues. To exclude a queue from the rule, the name can be prefixed with &#8216;!&#8217;.</p>
<dt>hosts</p>
<dd>Contains a comma-separated list of hosts or hostgroups (see and This parameter filters jobs that may be scheduled to a host in the list or a host contained in a hostgroup in the list. Any host not in the list will not be considered for the resource quota rule. The default value is &#8216;*&#8217;, which means all hosts. To exclude a host or hostgroup from the rule, the name can be prefixed with &#8216;!&#8217;.</p>
<dt>to</p>
<dd>This mandatory field defines the quota for resource attributes for this rule. The quota is expressed by one or more comma-separated limit definitions referring to fixed or consumable resources (not load values). Two kinds of limit definition may be used:</p>
<dl>
<dd>
<dl>
<dt>static limits</p>
<dd>Static limits set static values as quotas. Each limit consists of a complex attribute followed by an &quot;=&quot; sign and a value specification consistent with the complex attribute&#8217;s type (see</p>
<dt>dynamic limits</p>
<dd>A dynamic limit is a simple algebraic expression used to derive the limit value. The formula can reference complex attributes, whose value is used for the calculation of the resulting limit. The formula expression syntax is that of a sum of weighted complex values, that is: </p>
<pre>{<i>w1</i>|<code>$</code><i>complex1</i>[<code>*</code><i>w1</i>]}[{<code>+</code>|<code>-</code>}{<i>w2</i>|<code>$</code><i>complex2</i>[<code>*</code><i>w2</i>]}[{<code>+</code>|<code>-</code>}...]]</pre>
<p>The weighting factors (<i>w1</i>, &#8230;) are positive integers or floating point numbers in double precision. The complex values (<i>complex1</i>, &#8230;) must be of numerical type (INT, DOUBLE, MEMORY, or TIME), as specified by the complex&#8217;s type in the complex list (see and defined either on global, queue, or host level to resolve the value.<br />
 <code>Note:</code> Dynamic limits can only be configured for a host-specific rule, and must be defined for an expanded host list (or individual host). Also, if a load value corresponding to a complex used is not available, a large value is used for it to suggest an overloaded condition. Dynamic limits may slow the scheduler significantly.</dl>
</dl>
</dl>
<p> A complex form of limit may be used: &quot;expanded&quot; filters with the consumer list enclosed in braces (&#8216;{&#8216; &#8216;}&#8217;). This may be thought of as applying for each member of the list individually, as opposed to for all elements of a non-braced list in total. Alternatively, it is equivalent to an expansion into multiple instances of the rule, per the syntax which inspired it in shells such as <i><a href="/docs/linux/man/1-bash/">bash</a></i>(1). Thus</p>
<dl>
<dd>limit users {a, b} &#8230; to &#8230;</dl>
<p> is equivalent to</p>
<dl>
<dd>
<pre>limit users a ... to ...
limit users b ... to ...</pre>
</dl>
<p> where the text represented by the ellipses in each position is carried over to the expansion, and could be expanded itself. &#8216;{*}&#8217; represents a limit for each consumer of that type, as opposed to &#8216;*&#8217;, which limits all the consumers together. E.g.</p>
<dl>
<dd>limit users * to slots=100</dl>
<p> limits the total number of slots in use to 100, whereas</p>
<dl>
<dd>limit users {*} to slots=100</dl>
<p> limits each user to 100 slots. ACLs and hostgroups in expanded lists are treated as if they are expanded into a list of their constituents before expanding the whole list. A &#8216;!&#8217; prefix is distributed through the expansion of ACLs or hostgroups, i.e.</p>
<dl>
<dd>limit users {!@acl,&#8230;} &#8230;</dl>
<p> where @acl has members user1, user2, &#8230;, expands to</p>
<dl>
<dd>limit users {!user1,!user2,&#8230;} &#8230;</dl>
<p> and thus</p>
<dl>
<dd>
<pre> limit users !user1 ...
 limit users !user2 ...
 ...</pre>
</dl>
<h3>Formal Syntax</h3>
<table>
<tr VALIGN=top>
<td>ALL: </td>
<td> &#8216;*&#8217;
</td>
</tr>
<tr VALIGN=top>
<td>SEPARATOR: </td>
<td> &#8216;,&#8217;
</td>
</tr>
<tr VALIGN=top>
<td>STRING: </td>
<td> [^
]*
</td>
</tr>
<tr VALIGN=top>
<td>QUOTE: </td>
<td> &#8216;&quot;&#8217; S_EXPANDER: @ &#8216;{&#8216;
</td>
</tr>
<tr VALIGN=top>
<td>E_EXPANDER: </td>
<td> &#8216;}&#8217;
</td>
</tr>
<tr VALIGN=top>
<td>NOT: </td>
<td> &#8216;!&#8217;
</td>
</tr>
<tr VALIGN=top>
<td>BOOL: </td>
<td> [tT][rR][uU][eE]
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td> | 1
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td> | [fF][aA][lL][sS][eE]
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td> | 0
</td>
</tr>
<tr VALIGN=top>
<td>NAME: </td>
<td> [a-zA-Z][a-zA-Z0-9_-]*
</td>
</tr>
<tr VALIGN=top>
<td>LISTVALUE: </td>
<td> ALL | [NOT]STRING
</td>
</tr>
<tr VALIGN=top>
<td>LIST: </td>
<td> LISTVALUE [SEPARATOR LISTVALUE]*
</td>
</tr>
<tr VALIGN=top>
<td>FILTER: </td>
<td> LIST | S_EXPANDER LIST E_EXPANDER
</td>
</tr>
<tr VALIGN=top>
<td>RESOURCEPAIR: </td>
<td> STRING=STRING
</td>
</tr>
<tr VALIGN=top>
<td>RESOURCE: </td>
<td> RESOURCEPAIR [SEPARATOR RESOURCEPAIR]*
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>rule: </td>
<td> &quot;limit&quot; [&quot;name&quot; NAME] [&quot;users&quot; FILTER]
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td> [&quot;projects&quot; FILTER] [&quot;pes&quot; FILTER] [&quot;queues&quot; FILTER]
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td> [&quot;hosts&quot; FILTER] &quot;to&quot; RESOURCE NL
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>ruleset_attributes:</td>
<td> &quot;name&quot; NAME NL
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td> [&quot;enabled&quot; BOOL NL]
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td> [&quot;description&quot; QUOTE STRING QUOTE NL]
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>ruleset: </td>
<td> &quot;{&quot;
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td> ruleset_attributes
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td> rule+
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td> &quot;}&quot; NL
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>rulesets: </td>
<td> ruleset*
</td>
</tr>
</table>
<h2>Notes</h2>
<p>Please note that resource quotas are not enforced as job resource limits. Limiting, for example, h_vmem in a resource quota set does not result in a memory limit being set for job execution; it is necessary to specify such a limit on the job request, or as the complex&#8217;s default value. Thus</p>
<dl>
<dd>limit users {*} to h_vmem=2G</dl>
<p> will not restrict the memory a job can actually allocate to 2G, only what it can request, with the request actually enforcing the allocation. </p>
<p> The most restrictive rule in a set should be first in the <code>limit</code> List so that the scheduler can dispatch jobs efficiently by rejecting queues to consider as early as possible since subsequent rules in the list are not considered after one matches. This can be important in large clusters, in which RQS can significantly slow down scheduling.</p>
<h2>Examples</h2>
<p>The following is the simplest form of a resource quota set. It restricts all users together to a maximal use of 100 slots in the whole cluster. Similarly, &quot;slots=0&quot; could be used to prevent new jobs starting for draining the system. </p>
<pre>=======================================================================
{
 name max_u_slots
 description &quot;All users max use of 100 slots&quot;
 enabled true
 limit to slots=100
}
=======================================================================</pre>
<p>The next example restricts user1 and user2 to requesting 6g virtual_free, and all other users to requesting 4g virtual_free, on each host in hostgroup lx_hosts. </p>
<pre>=======================================================================
{
 name max_virtual_free_on_lx_hosts
 description &quot;resource quota for virtual_free restriction&quot;
 enabled true
 limit users {user1,user2} hosts {@lx_host} to virtual_free=6g
 limit users {*} hosts {@lx_host} to virtual_free=4g
}
=======================================================================</pre>
<p>The next example shows the use of a dynamic limit. It restricts the total slot usage by all users on each host to twice the value of num_proc (the number of processor units) on the host. (It would be more usual to use &quot;slots=$num_proc&quot; to prevent over-subscription of nodes.) </p>
<pre>=======================================================================
{
 name max_slots_on_every_host
 enabled true
 limit hosts {*} to slots=$num_proc*2
}
=======================================================================</pre>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
