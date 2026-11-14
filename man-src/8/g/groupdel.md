---
title: "groupdel(8)"
name: "groupdel"
section: "8"
letter: "g"
url: "/docs/linux/man/8-groupdel/"
description: "groupdel – delete a group"
---

<p>groupdel &#8211; delete a group</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>groupdel</code> [<i>options</i>] <i>GROUP</i></dl>
<h2>Description</h2>
<dd>The <code>groupdel</code> command modifies the system account files, deleting all entries that refer to <i>GROUP</i>. The named group must exist.</p>
<h2>Options</h2>
<p>The options which apply to the <code>groupdel</code> command are: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-P</code>, <code>&#8211;prefix</code>&nbsp;<i>PREFIX_DIR</i></p>
<dl>
<dd>Apply changes in the <i>PREFIX_DIR</i> directory and use the configuration files from the <i>PREFIX_DIR</i> directory. This option does not chroot and is intended for preparing a cross-compilation target. Some limitations: NIS and LDAP users/groups are not verified. PAM authentication is using the host files. No SELINUX support.</dl>
<h2>Caveats</h2>
<p>You may not remove the primary group of any existing user. You must remove the user before you remove the group. </p>
<p> You should manually check all file systems to ensure that no files remain owned by this group.</p>
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
<dd>Secure group account information.</dl>
<h2>Exit Values</h2>
<p>The <code>groupdel</code> command exits with the following values: </p>
<p> <i>0</i></p>
<dl>
<dd>success</dl>
<p> <i>2</i></p>
<dl>
<dd>invalid command syntax</dl>
<p> <i>6</i></p>
<dl>
<dd>specified group doesn&#8217;t exist</dl>
<p> <i>8</i></p>
<dl>
<dd>can&#8217;t remove user&#8217;s primary group</dl>
<p> <i>10</i></p>
<dl>
<dd>can&#8217;t update group file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chfn/">chfn</a></code>(1), <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/8-gpasswd/">gpasswd</a></code>(8), <code><a href="/docs/linux/man/8-groupadd/">groupadd</a></code>(8), <code><a href="/docs/linux/man/8-groupmod/">groupmod</a></code>(8), <code><a href="/docs/linux/man/8-useradd/">useradd</a></code>(8), <code><a href="/docs/linux/man/8-userdel/">userdel</a></code>(8), <code><a href="/docs/linux/man/8-usermod/">usermod</a></code>(8). </p>
