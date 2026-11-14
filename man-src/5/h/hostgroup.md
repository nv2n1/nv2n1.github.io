---
title: "hostgroup(5)"
name: "hostgroup"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hostgroup/"
description: "hostgroup – host group entry file format"
---

<p>hostgroup &#8211; host group entry file format</p>
<h2>Description</h2>
<p>A host group entry is used to merge host names to groups. Each host group entry file defines one group. Inside a group definition file you can also reference groups. These groups are called subgroups. A subgroup is referenced by the sign &quot;@&quot; as first character of the name. </p>
<p> A list of currently-configured host group entries can be displayed via the <code>-shgrpl</code> option. The contents of each listed host group entry can be shown via the <code>-shgrp</code> switch. The output follows the <i>hostgroup</i> format description. New host group entries can be created and existing can be modified via the <code>-ahgrp</code>, <code>-mhgrp</code>, <code>-dhgrp</code> and <code>-?attr</code> options to </p>
<p> Note, xxQS_NAMExx allows backslashes (\) be used to escape newline characters. The backslash and the newline are replaced with a space character before any interpretation.</p>
<h2>Format</h2>
<p>A host group entry contains the following parameters:</p>
<h3><code>group_name</code></h3>
<p>The group_name defines the host group name. Host group names have to begin with an &#8216;@&#8217; character as explained for <i>hostgroup_name</i> in</p>
<h3><code>hostlist</code></h3>
<p>The names of all hosts and host groups (see <i>host_identifier</i> in which are members of the group. Only whitespace is allowed as list separators. The default value for this parameter is NONE. </p>
<p> Note, if the first character of the <i>host_identifier</i> is an &quot;@&quot; sign the name is used to reference a which is taken as a subgroup of this group.</p>
<h2>Example</h2>
<p>This is a typical host group entry: group_name @bigMachines hostlist @solaris64 @solaris32 fangorn balrog The entry will define a new host group called <code>@bigMachines</code>. In this host group are the host <code>fangorn</code>, <code>balrog</code> and all members of the host groups <code>@solaris64</code> and <code>@solaris32</code>. </p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
