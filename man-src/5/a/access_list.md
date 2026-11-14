---
title: "access_list(5)"
name: "access_list"
section: "5"
letter: "a"
url: "/docs/linux/man/5-access_list/"
description: "access_list – xxQS_NAMExx access list file format"
---

<p>access_list &#8211; xxQS_NAMExx access list file format</p>
<h2>Description</h2>
<p>Access lists are used in xxQS_NAMExx to define access permissions of users to queues (see parallel environments (see execution hosts (see or the whole cluster ( see A list of currently configured access lists can be displayed via the <code>-sul</code> option. The contents of each access list can shown via the <code>-su</code> switch. The output follows the <i>access_list</i> format description. New access lists can be created and existing ones can be modified via the <code>-au</code> and <code>-du</code> options to </p>
<p> Departments are a special form of access list that additionally allow assignment of functional shares and override tickets. </p>
<p> Note, xxQS_NAMExx allows backslashes (\) be used to escape newline characters. The backslash and the newline are replaced with a space character before any interpretation.</p>
<h2>Format</h2>
<p>The following list of <i>access_list</i> parameters specifies the <i>access_list</i> content:</p>
<h3><code>name</code></h3>
<p>The name of the access list in the format for <i>userset_name</i> in</p>
<h3><code>type</code></h3>
<p>The type of the access list, currently one of <i>ACL,</i> or <i>DEPT</i> or a combination of both in a comma-separated list. Depending on this parameter, the access list can be used as an access list only, or as a department.</p>
<h3><code>oticket</code></h3>
<p>The number of override tickets currently assigned to the department.</p>
<h3><code>fshare</code></h3>
<p>The current functional share of the department.</p>
<h3><code>entries</code></h3>
<p>A comma-separated list of those UNIX users (see <i>user_name</i> in or those primary UNIX groups that are assigned to the access list or the department. Only a user&#8217;s primary UNIX group is used; secondary groups are ignored. Only symbolic names are allowed. A group is differentiated from a user name by prefixing the group name with a &#8216;@&#8217; sign. Pure access lists allow listing any user or group in any access list. </p>
<p> When using departments, each user or group may only be listed in one department, in order to ensure a unique assignment of jobs to departments. If the <i>defaultdepartment</i> is defined, it is assigned to jobs whose users do not match with any of the users or groups listed under <i>entries</i>.</p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
