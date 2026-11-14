---
title: "groupmod(8)"
name: "groupmod"
section: "8"
letter: "g"
url: "/docs/linux/man/8-groupmod/"
description: "groupmod – modify a group definition on the system"
---

<p>groupmod &#8211; modify a group definition on the system</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>groupmod</code> [<i>options</i>] <i>GROUP</i></dl>
<h2>Description</h2>
<dd>The <code>groupmod</code> command modifies the definition of the specified <i>GROUP</i> by modifying the appropriate entry in the group database.</p>
<h2>Options</h2>
<p>The options which apply to the <code>groupmod</code> command are: </p>
<p> <code>-g</code>, <code>&#8211;gid</code>&nbsp;<i>GID</i></p>
<dl>
<dd>The group ID of the given <i>GROUP</i> will be changed to <i>GID</i>. </p>
<p> The value of <i>GID</i> must be a non-negative decimal integer. This value must be unique, unless the <code>-o</code> option is used. </p>
<p> Users who use the group as primary group will be updated to keep the group as their primary group. </p>
<p> Any files that have the old group ID and must continue to belong to <i>GROUP</i>, must have their group ID changed manually. </p>
<p> No checks will be performed with regard to the <code>GID_MIN</code>, <code>GID_MAX</code>, <code>SYS_GID_MIN</code>, or <code>SYS_GID_MAX</code> from /etc/login.defs.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-n</code>, <code>&#8211;new-name</code>&nbsp;<i>NEW_GROUP</i></p>
<dl>
<dd>The name of the group will be changed from <i>GROUP</i> to <i>NEW_GROUP</i> name.</dl>
<p> <code>-o</code>, <code>&#8211;non-unique</code></p>
<dl>
<dd>When used with the <code>-g</code> option, allow to change the group <i>GID</i> to a non-unique value.</dl>
<p> <code>-p</code>, <code>&#8211;password</code>&nbsp;<i>PASSWORD</i></p>
<dl>
<dd>The encrypted password, as returned by <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3). </p>
<p> <code>Note:</code> This option is not recommended because the password (or encrypted password) will be visible by users listing the processes. </p>
<p> You should make sure the password respects the system&#8217;s password policy.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-P</code>, <code>&#8211;prefix</code>&nbsp;<i>PREFIX_DIR</i></p>
<dl>
<dd>Apply changes in the <i>PREFIX_DIR</i> directory and use the configuration files from the <i>PREFIX_DIR</i> directory. This option does not chroot and is intended for preparing a cross-compilation target. Some limitations: NIS and LDAP users/groups are not verified. PAM authentication is using the host files. No SELINUX support.</dl>
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
<p> /etc/login.defs</p>
<dl>
<dd>Shadow password suite configuration.</dl>
<p> /etc/passwd</p>
<dl>
<dd>User account information.</dl>
<h2>Exit Values</h2>
<p>The <code>groupmod</code> command exits with the following values: </p>
<p> <i>0</i></p>
<dl>
<dd>E_SUCCESS: success</dl>
<p> <i>2</i></p>
<dl>
<dd>E_USAGE: invalid command syntax</dl>
<p> <i>3</i></p>
<dl>
<dd>E_BAD_ARG: invalid argument to option</dl>
<p> <i>4</i></p>
<dl>
<dd>E_GID_IN_USE: specified group doesn&#8217;t exist</dl>
<p> <i>6</i></p>
<dl>
<dd>E_NOTFOUND: specified group doesn&#8217;t exist</dl>
<p> <i>9</i></p>
<dl>
<dd>E_NAME_IN_USE: group name already in use</dl>
<p> <i>10</i></p>
<dl>
<dd>E_GRP_UPDATE: can&#8217;t update group file</dl>
<p> <i>11</i></p>
<dl>
<dd>E_CLEANUP_SERVICE: can&#8217;t setup cleanup service</dl>
<p> <i>12</i></p>
<dl>
<dd>E_PAM_USERNAME: can&#8217;t determine your username for use with pam</dl>
<p> <i>13</i></p>
<dl>
<dd>E_PAM_ERROR: pam returned an error, see syslog facility id groupmod for the PAM error message</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chfn/">chfn</a></code>(1), <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/8-gpasswd/">gpasswd</a></code>(8), <code><a href="/docs/linux/man/8-groupadd/">groupadd</a></code>(8), <code><a href="/docs/linux/man/8-groupdel/">groupdel</a></code>(8), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/8-useradd/">useradd</a></code>(8), <code><a href="/docs/linux/man/8-userdel/">userdel</a></code>(8), <code><a href="/docs/linux/man/8-usermod/">usermod</a></code>(8). </p>
