---
title: "qquota(1)"
name: "qquota"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qquota/"
description: "qquota – shows current usage of xxQS_NAMExx resource quotas"
---

<h2 class="name">NAME</h2>
<p> qquota &#8211; shows current usage of xxQS_NAMExx resource quotas </p>
<h2>SYNTAX</h2>
<p> <code>qquota</code> [ <code>-h wc_host|wc_hostgroup,&#8230;</code> ] [ <code>-help</code> ] [ <code>-l resource_name,&#8230;</code> ] [ <code>-u wc_user,&#8230;</code> ] [ <code>-P wc_project,&#8230;</code> ] [ <code>-pe wc_pe_name,&#8230;</code> ] [ <code>-q wc_cqueue,&#8230;</code> ] [ <code>-xml</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>qquota</i> shows the current xxQS_NAMExx resource quota sets. Only resource quota sets with a positive usage count or a static limit are printed, as described in OUTPUT FORMATS below. </p>
<p> Selection options allow you to filter for specific hosts, cluster queues, projects, parallel environments (pe), resources or users. Without any option <i>qquota</i> will display a list of all resource quota sets for the calling user. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h wc_host|wc_hostgroup,&#8230;</code></p>
<dd> <i>Display only resource quota sets that match the hosts</i> in the given wildcard host or hostgroup list. The definition of <code>wc_host</code> and <code>wc_hostgroup</code> is in</p>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-l resource_name,&#8230;</code></p>
<dd> Display only resource quota sets matching the resources in the given resource list.</p>
<dt><code>-u wc_user,&#8230;</code></p>
<dd> Display only resource quota sets matching the users in the given wildcard user list. The definition of <code>wc_user</code> is in</p>
<dt><code>-P wc_project,&#8230;</code></p>
<dd> Display only resource quota sets matching the projects in the given wildcard project list. The definition of <code>wc_project</code> is in</p>
<dt><code>-pe wc_pe_name,&#8230;</code></p>
<dd> Display only resource quota sets matching the parallel environments (pe) in the given wildcard pe list. The definition of <code>wc_pe_name</code> is in</p>
<dt><code>-q wc_cqueue,&#8230;</code></p>
<dd> Display only resource quota sets matching the queues in the given wildcard cluster queue list. The definition of <code>wc_cqueue</code> is in</p>
<dt><code>-xml </code></p>
<dd> This option can be used with all other options, and changes the output to XML. The schema used is referenced in the XML output. The output is printed to stdout.</dl>
<h2>OUTPUT FORMAT</h2>
<p> A line is printed for every resource quota with a positive usage count or static resource. The line consists of</p>
<dl>
<dt>&bull;</p>
<dd> the resource quota &#8211; rule set name/rule name or number of rule in ruleset</p>
<dt>&bull;</p>
<dd> the limit &#8211; resource name, the number of used and available entities of that resource</p>
<dt>&bull;</p>
<dd> the effective resource quota set filter</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qquota</i> uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition, the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</dl>
<h2>FILES</h2>
<pre>
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/act_qmaster</i>
                          xxQS_NAMExx master host file
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/xxqs_name_sxx_qquota</i>
                          cluster qquota default options
<i>$HOME/.xxqs_name_sxx_qquota</i>
                          user qquota default options
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
