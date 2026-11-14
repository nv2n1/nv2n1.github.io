---
title: "groupmems(8)"
name: "groupmems"
section: "8"
letter: "g"
url: "/docs/linux/man/8-groupmems/"
description: "groupmems – administer members of a user’s primary group"
---

<p>groupmems &#8211; administer members of a user&#8217;s primary group</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>groupmems</code> -a&nbsp;<i>user_name</i> | -d&nbsp;<i>user_name</i> | [-g&nbsp;<i>group_name</i>] | -l | -p</dl>
<h2>Description</h2>
<dd>The <code>groupmems</code> command allows a user to administer their own group membership list without the requirement of superuser privileges. The <code>groupmems</code> utility is for systems that configure its users to be in their own name sake primary group (i.e., guest / guest). </p>
<p> Only the superuser, as administrator, can use <code>groupmems</code> to alter the memberships of other groups.</p>
<h2>Options</h2>
<p>The options which apply to the <code>groupmems</code> command are: </p>
<p> <code>-a</code>, <code>&#8211;add</code>&nbsp;<i>user_name</i></p>
<dl>
<dd>Add a user to the group membership list. </p>
<p> If the /etc/gshadow file exist, and the group has no entry in the /etc/gshadow file, a new entry will be created.</dl>
<p> <code>-d</code>, <code>&#8211;delete</code>&nbsp;<i>user_name</i></p>
<dl>
<dd>Delete a user from the group membership list. </p>
<p> If the /etc/gshadow file exist, the user will be removed from the list of members and administrators of the group. </p>
<p> If the /etc/gshadow file exist, and the group has no entry in the /etc/gshadow file, a new entry will be created.</dl>
<p> <code>-g</code>, <code>&#8211;group</code>&nbsp;<i>group_name</i></p>
<dl>
<dd>The superuser can specify which group membership list to modify.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dd>List the group membership list.</dl>
<p> <code>-p</code>, <code>&#8211;purge</code></p>
<dl>
<dd>Purge all users from the group membership list. </p>
<p> If the /etc/gshadow file exist, and the group has no entry in the /etc/gshadow file, a new entry will be created.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<h2>Setup</h2>
<p>The <code>groupmems</code> executable should be in mode 2710 as user <i>root</i> and in group <i>groups</i>. The system administrator can add users to group <i>groups</i> to allow or disallow them using the <code>groupmems</code> utility to manage their own group membership list. </p>
<dl>
<dd>
<pre> $ groupadd -r groups
 $ chmod 2710 groupmems
 $ chown root.groups groupmems
 $ groupmems -g groups -a gk4</pre>
</dl>
<h2>Configuration</h2>
<p>The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>MAX_MEMBERS_PER_GROUP</code> (number)</p>
<dl>
<dd>Maximum members per group entry. When the maximum is reached, a new group entry (line) is started in /etc/group (with the same name, same password, and same GID). </p>
<p> The default value is 0, meaning that there are no limits in the number of members in a group. </p>
<p> This feature (split group) permits to limit the length of lines in the group file. This is useful to make sure that lines for NIS groups are not larger than 1024 characters. </p>
<p> If you need to enforce such limit, you can use 25. </p>
<p> Note: split groups may not be supported by all tools (even in the Shadow toolsuite). You should not use this variable unless you really need it.</dl>
<h2>Files</h2>
<p>/etc/group</p>
<dl>
<dd>Group account information.</dl>
<p> /etc/gshadow</p>
<dl>
<dd>secure group account information</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chfn/">chfn</a></code>(1), <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/8-groupadd/">groupadd</a></code>(8), <code><a href="/docs/linux/man/8-groupdel/">groupdel</a></code>(8), <code><a href="/docs/linux/man/8-useradd/">useradd</a></code>(8), <code><a href="/docs/linux/man/8-userdel/">userdel</a></code>(8), <code><a href="/docs/linux/man/8-usermod/">usermod</a></code>(8). </p>
