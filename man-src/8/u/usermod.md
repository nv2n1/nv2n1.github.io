---
title: "usermod(8)"
name: "usermod"
section: "8"
letter: "u"
url: "/docs/linux/man/8-usermod/"
description: "usermod – modify a user account"
---

<p>usermod &#8211; modify a user account</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>usermod</code> [<i>options</i>] <i>LOGIN</i></dl>
<h2>Description</h2>
<dd>The <code>usermod</code> command modifies the system account files to reflect the changes that are specified on the command line.</p>
<h2>Options</h2>
<p>The options which apply to the <code>usermod</code> command are: </p>
<p> <code>-a</code>, <code>&#8211;append</code></p>
<dl>
<dd>Add the user to the supplementary group(s). Use only with the <code>-G</code> option.</dl>
<p> <code>-b</code>, <code>&#8211;badnames</code></p>
<dl>
<dd>Allow names that do not conform to standards.</dl>
<p> <code>-c</code>, <code>&#8211;comment</code>&nbsp;<i>COMMENT</i></p>
<dl>
<dd>The new value of the user&#8217;s password file comment field. It is normally modified using the <code><a href="/docs/linux/man/1-chfn/">chfn</a></code>(1) utility.</dl>
<p> <code>-d</code>, <code>&#8211;home</code>&nbsp;<i>HOME_DIR</i></p>
<dl>
<dd>The user&#8217;s new login directory. </p>
<p> If the <code>-m</code> option is given, the contents of the current home directory will be moved to the new home directory, which is created if it does not already exist.</dl>
<p> <code>-e</code>, <code>&#8211;expiredate</code>&nbsp;<i>EXPIRE_DATE</i></p>
<dl>
<dd>The date on which the user account will be disabled. The date is specified in the format <i>YYYY-MM-DD</i>. </p>
<p> An empty <i>EXPIRE_DATE</i> argument will disable the expiration of the account. </p>
<p> This option requires a /etc/shadow file. A /etc/shadow entry will be created if there were none.</dl>
<p> <code>-f</code>, <code>&#8211;inactive</code>&nbsp;<i>INACTIVE</i></p>
<dl>
<dd>The number of days after a password expires until the account is permanently disabled. </p>
<p> A value of 0 disables the account as soon as the password has expired, and a value of -1 disables the feature. </p>
<p> This option requires a /etc/shadow file. A /etc/shadow entry will be created if there were none.</dl>
<p> <code>-g</code>, <code>&#8211;gid</code>&nbsp;<i>GROUP</i></p>
<dl>
<dd>The group name or number of the user&#8217;s new initial login group. The group must exist. </p>
<p> Any file from the user&#8217;s home directory owned by the previous primary group of the user will be owned by this new group. </p>
<p> The group ownership of files outside of the user&#8217;s home directory must be fixed manually.</dl>
<p> <code>-G</code>, <code>&#8211;groups</code>&nbsp;<i>GROUP1</i>[<i>,GROUP2,&#8230;</i>[<i>,GROUPN</i>]]]</p>
<dl>
<dd>A list of supplementary groups which the user is also a member of. Each group is separated from the next by a comma, with no intervening whitespace. The groups are subject to the same restrictions as the group given with the <code>-g</code> option. </p>
<p> If the user is currently a member of a group which is not listed, the user will be removed from the group. This behaviour can be changed via the <code>-a</code> option, which appends the user to the current supplementary group list.</dl>
<p> <code>-l</code>, <code>&#8211;login</code>&nbsp;<i>NEW_LOGIN</i></p>
<dl>
<dd>The name of the user will be changed from <i>LOGIN</i> to <i>NEW_LOGIN</i>. Nothing else is changed. In particular, the user&#8217;s home directory or mail spool should probably be renamed manually to reflect the new login name.</dl>
<p> <code>-L</code>, <code>&#8211;lock</code></p>
<dl>
<dd>Lock a user&#8217;s password. This puts a &#8216;!&#8217; in front of the encrypted password, effectively disabling the password. You can&#8217;t use this option with <code>-p</code> or <code>-U</code>. </p>
<p> Note: if you wish to lock the account (not only access with a password), you should also set the <i>EXPIRE_DATE</i> to <i>1</i>.</dl>
<p> <code>-m</code>, <code>&#8211;move-home</code></p>
<dl>
<dd>Move the content of the user&#8217;s home directory to the new location. </p>
<p> This option is only valid in combination with the <code>-d</code> (or <code>&#8211;home</code>) option. </p>
<p> <code>usermod</code> will try to adapt the ownership of the files and to copy the modes, ACL and extended attributes, but manual changes might be needed afterwards.</dl>
<p> <code>-o</code>, <code>&#8211;non-unique</code></p>
<dl>
<dd>When used with the <code>-u</code> option, this option allows to change the user ID to a non-unique value.</dl>
<p> <code>-p</code>, <code>&#8211;password</code>&nbsp;<i>PASSWORD</i></p>
<dl>
<dd>The encrypted password, as returned by <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3). </p>
<p> <code>Note:</code> This option is not recommended because the password (or encrypted password) will be visible by users listing the processes. </p>
<p> The password will be written in the local /etc/passwd or /etc/shadow file. This might differ from the password database configured in your PAM configuration. </p>
<p> You should make sure the password respects the system&#8217;s password policy.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-P</code>, <code>&#8211;prefix</code>&nbsp;<i>PREFIX_DIR</i></p>
<dl>
<dd>Apply changes in the <i>PREFIX_DIR</i> directory and use the configuration files from the <i>PREFIX_DIR</i> directory. This option does not chroot and is intended for preparing a cross-compilation target. Some limitations: NIS and LDAP users/groups are not verified. PAM authentication is using the host files. No SELINUX support.</dl>
<p> <code>-s</code>, <code>&#8211;shell</code>&nbsp;<i>SHELL</i></p>
<dl>
<dd>The name of the user&#8217;s new login shell. Setting this field to blank causes the system to select the default login shell.</dl>
<p> <code>-u</code>, <code>&#8211;uid</code>&nbsp;<i>UID</i></p>
<dl>
<dd>The new numerical value of the user&#8217;s ID. </p>
<p> This value must be unique, unless the <code>-o</code> option is used. The value must be non-negative. </p>
<p> The user&#8217;s mailbox, and any files which the user owns and which are located in the user&#8217;s home directory will have the file user ID changed automatically. </p>
<p> The ownership of files outside of the user&#8217;s home directory must be fixed manually. </p>
<p> No checks will be performed with regard to the <code>UID_MIN</code>, <code>UID_MAX</code>, <code>SYS_UID_MIN</code>, or <code>SYS_UID_MAX</code> from /etc/login.defs.</dl>
<p> <code>-U</code>, <code>&#8211;unlock</code></p>
<dl>
<dd>Unlock a user&#8217;s password. This removes the &#8216;!&#8217; in front of the encrypted password. You can&#8217;t use this option with <code>-p</code> or <code>-L</code>. </p>
<p> Note: if you wish to unlock the account (not only access with a password), you should also set the <i>EXPIRE_DATE</i> (for example to <i>99999</i>, or to the <code>EXPIRE</code> value from /etc/default/useradd).</dl>
<p> <code>-v</code>, <code>&#8211;add-subuids</code>&nbsp;<i>FIRST</i>&#8211;<i>LAST</i></p>
<dl>
<dd>Add a range of subordinate uids to the user&#8217;s account. </p>
<p> This option may be specified multiple times to add multiple ranges to a users account. </p>
<p> No checks will be performed with regard to <code>SUB_UID_MIN</code>, <code>SUB_UID_MAX</code>, or <code>SUB_UID_COUNT</code> from /etc/login.defs.</dl>
<p> <code>-V</code>, <code>&#8211;del-subuids</code>&nbsp;<i>FIRST</i>&#8211;<i>LAST</i></p>
<dl>
<dd>Remove a range of subordinate uids from the user&#8217;s account. </p>
<p> This option may be specified multiple times to remove multiple ranges to a users account. When both <code>&#8211;del-subuids</code> and <code>&#8211;add-subuids</code> are specified, the removal of all subordinate uid ranges happens before any subordinate uid range is added. </p>
<p> No checks will be performed with regard to <code>SUB_UID_MIN</code>, <code>SUB_UID_MAX</code>, or <code>SUB_UID_COUNT</code> from /etc/login.defs.</dl>
<p> <code>-w</code>, <code>&#8211;add-subgids</code>&nbsp;<i>FIRST</i>&#8211;<i>LAST</i></p>
<dl>
<dd>Add a range of subordinate gids to the user&#8217;s account. </p>
<p> This option may be specified multiple times to add multiple ranges to a users account. </p>
<p> No checks will be performed with regard to <code>SUB_GID_MIN</code>, <code>SUB_GID_MAX</code>, or <code>SUB_GID_COUNT</code> from /etc/login.defs.</dl>
<p> <code>-W</code>, <code>&#8211;del-subgids</code>&nbsp;<i>FIRST</i>&#8211;<i>LAST</i></p>
<dl>
<dd>Remove a range of subordinate gids from the user&#8217;s account. </p>
<p> This option may be specified multiple times to remove multiple ranges to a users account. When both <code>&#8211;del-subgids</code> and <code>&#8211;add-subgids</code> are specified, the removal of all subordinate gid ranges happens before any subordinate gid range is added. </p>
<p> No checks will be performed with regard to <code>SUB_GID_MIN</code>, <code>SUB_GID_MAX</code>, or <code>SUB_GID_COUNT</code> from /etc/login.defs.</dl>
<p> <code>-Z</code>, <code>&#8211;selinux-user</code>&nbsp;<i>SEUSER</i></p>
<dl>
<dd>The new SELinux user for the user&#8217;s login. </p>
<p> A blank <i>SEUSER</i> will remove the SELinux user mapping for user <i>LOGIN</i> (if any).</dl>
<h2>Caveats</h2>
<p>You must make certain that the named user is not executing any processes when this command is being executed if the user&#8217;s numerical user ID, the user&#8217;s name, or the user&#8217;s home directory is being changed. <code>usermod</code> checks this on Linux. On other platforms it only uses utmp to check if the user is logged in. </p>
<p> You must change the owner of any <code>crontab</code> files or <code>at</code> jobs manually. </p>
<p> You must make any changes involving NIS on the NIS server.</p>
<h2>Configuration</h2>
<p>The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>LASTLOG_UID_MAX</code> (number)</p>
<dl>
<dd>Highest user ID number for which the lastlog entries should be updated. As higher user IDs are usually tracked by remote user identity and authentication services there is no need to create a huge sparse lastlog file for them. </p>
<p> No <code>LASTLOG_UID_MAX</code> option present in the configuration means that there is no user ID limit for writing lastlog entries.</dl>
<p> <code>MAIL_DIR</code> (string)</p>
<dl>
<dd>The mail spool directory. This is needed to manipulate the mailbox when its corresponding user account is modified or deleted. If not specified, a compile-time default is used.</dl>
<p> <code>MAIL_FILE</code> (string)</p>
<dl>
<dd>Defines the location of the users mail spool files relatively to their home directory.</dl>
<p> The <code>MAIL_DIR</code> and <code>MAIL_FILE</code> variables are used by <code>useradd</code>, <code>usermod</code>, and <code>userdel</code> to create, move, or delete the user&#8217;s mail spool. </p>
<p> <code>MAX_MEMBERS_PER_GROUP</code> (number)</p>
<dl>
<dd>Maximum members per group entry. When the maximum is reached, a new group entry (line) is started in /etc/group (with the same name, same password, and same GID). </p>
<p> The default value is 0, meaning that there are no limits in the number of members in a group. </p>
<p> This feature (split group) permits to limit the length of lines in the group file. This is useful to make sure that lines for NIS groups are not larger than 1024 characters. </p>
<p> If you need to enforce such limit, you can use 25. </p>
<p> Note: split groups may not be supported by all tools (even in the Shadow toolsuite). You should not use this variable unless you really need it.</dl>
<p> <code>SUB_GID_MIN</code> (number), <code>SUB_GID_MAX</code> (number), <code>SUB_GID_COUNT</code> (number)</p>
<dl>
<dd>If /etc/subuid exists, the commands <code>useradd</code> and <code>newusers</code> (unless the user already have subordinate group IDs) allocate <code>SUB_GID_COUNT</code> unused group IDs from the range <code>SUB_GID_MIN</code> to <code>SUB_GID_MAX</code> for each new user. </p>
<p> The default values for <code>SUB_GID_MIN</code>, <code>SUB_GID_MAX</code>, <code>SUB_GID_COUNT</code> are respectively 100000, 600100000 and 65536.</dl>
<p> <code>SUB_UID_MIN</code> (number), <code>SUB_UID_MAX</code> (number), <code>SUB_UID_COUNT</code> (number)</p>
<dl>
<dd>If /etc/subuid exists, the commands <code>useradd</code> and <code>newusers</code> (unless the user already have subordinate user IDs) allocate <code>SUB_UID_COUNT</code> unused user IDs from the range <code>SUB_UID_MIN</code> to <code>SUB_UID_MAX</code> for each new user. </p>
<p> The default values for <code>SUB_UID_MIN</code>, <code>SUB_UID_MAX</code>, <code>SUB_UID_COUNT</code> are respectively 100000, 600100000 and 65536.</dl>
<h2>Files</h2>
<p>/etc/group</p>
<dl>
<dd>Group account information.</dl>
<p> /etc/gshadow</p>
<dl>
<dd>Secure group account information.</dl>
<p> /etc/login.defs</p>
<dl>
<dd>Shadow password suite configuration.</dl>
<p> /etc/passwd</p>
<dl>
<dd>User account information.</dl>
<p> /etc/shadow</p>
<dl>
<dd>Secure user account information.</dl>
<p> /etc/subgid</p>
<dl>
<dd>Per user subordinate group IDs.</dl>
<p> /etc/subuid</p>
<dl>
<dd>Per user subordinate user IDs.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chfn/">chfn</a></code>(1), <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3), <code><a href="/docs/linux/man/8-gpasswd/">gpasswd</a></code>(8), <code><a href="/docs/linux/man/8-groupadd/">groupadd</a></code>(8), <code><a href="/docs/linux/man/8-groupdel/">groupdel</a></code>(8), <code><a href="/docs/linux/man/8-groupmod/">groupmod</a></code>(8), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/5-subgid/">subgid</a></code>(5), <code><a href="/docs/linux/man/5-subuid/">subuid</a></code>(5), <code><a href="/docs/linux/man/8-useradd/">useradd</a></code>(8), <code><a href="/docs/linux/man/8-userdel/">userdel</a></code>(8). </p>
