---
title: "grpck(8)"
name: "grpck"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grpck/"
description: "grpck – verify integrity of group files"
---

<p>grpck &#8211; verify integrity of group files</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>grpck</code> [options] [<i>group</i>&nbsp;[&nbsp;<i>shadow</i>&nbsp;]]</dl>
<h2>Description</h2>
<dd>The <code>grpck</code> command verifies the integrity of the groups information. It checks that all entries in /etc/group and /etc/gshadow have the proper format and contain valid data. The user is prompted to delete entries that are improperly formatted or which have other uncorrectable errors. </p>
<p> Checks are made to verify that each entry has: </p>
<dl>
<dd>&bull; the correct number of fields</dl>
<dl>
<dd>&bull; a unique and valid group name</dl>
<dl>
<dd>&bull; a valid group identifier (/etc/group only)</dl>
<dl>
<dd>&bull; a valid list of members and administrators</dl>
<dl>
<dd>&bull; a corresponding entry in the /etc/gshadow file (respectively /etc/group for the gshadow checks)</dl>
<p> The checks for correct number of fields and unique group name are fatal. If an entry has the wrong number of fields, the user will be prompted to delete the entire line. If the user does not answer affirmatively, all further checks are bypassed. An entry with a duplicated group name is prompted for deletion, but the remaining checks will still be made. All other errors are warnings and the user is encouraged to run the <code>groupmod</code> command to correct the error. </p>
<p> The commands which operate on the /etc/group and /etc/gshadow files are not able to alter corrupted or duplicated entries. <code>grpck</code> should be used in those circumstances to remove the offending entries.</p>
<h2>Options</h2>
<p>The <code>-r</code> and <code>-s</code> options cannot be combined. </p>
<p> The options which apply to the <code>grpck</code> command are: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-r</code>, <code>&#8211;read-only</code></p>
<dl>
<dd>Execute the <code>grpck</code> command in read-only mode. This causes all questions regarding changes to be answered <i>no</i> without user intervention.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-s</code>, <code>&#8211;sort</code></p>
<dl>
<dd>Sort entries in /etc/group and /etc/gshadow by GID.</dl>
<p> By default, <code>grpck</code> operates on /etc/group and /etc/gshadow. The user may select alternate files with the <i>group</i> and <i>shadow</i> parameters.</p>
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
<p> /etc/passwd</p>
<dl>
<dd>User account information.</dl>
<h2>Exit Values</h2>
<p>The <code>grpck</code> command exits with the following values: </p>
<p> <i>0</i></p>
<dl>
<dd>success</dl>
<p> <i>1</i></p>
<dl>
<dd>invalid command syntax</dl>
<p> <i>2</i></p>
<dl>
<dd>one or more bad group entries</dl>
<p> <i>3</i></p>
<dl>
<dd>can&#8217;t open group files</dl>
<p> <i>4</i></p>
<dl>
<dd>can&#8217;t lock group files</dl>
<p> <i>5</i></p>
<dl>
<dd>can&#8217;t update group files</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-group/">group</a></code>(5), <code><a href="/docs/linux/man/8-groupmod/">groupmod</a></code>(8), <code><a href="/docs/linux/man/5-gshadow/">gshadow</a></code>(5), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/8-pwck/">pwck</a></code>(8), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5). </p>
