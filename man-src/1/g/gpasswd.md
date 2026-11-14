---
title: "gpasswd(1)"
name: "gpasswd"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpasswd/"
description: "gpasswd – administer /etc/group and /etc/gshadow"
---

<h2 class="name">NAME</h2>
<p> gpasswd &#8211; administer /etc/group and /etc/gshadow </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gpasswd</code> [<i>option</i>] <i>group</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>gpasswd</code> command is used to administer /etc/group, and /etc/gshadow. Every group can have administrators, members and a password. </p>
<p> System administrators can use the <code>-A</code> option to define group administrator(s) and the <code>-M</code> option to define members. They have all rights of group administrators and members. </p>
<p> <code>gpasswd</code> called by a group administrator with a group name only prompts for the new password of the <i>group</i>. </p>
<p> If a password is set the members can still use <code><a href="/docs/linux/man/1-newgrp/">newgrp</a></code>(1) without a password, and non-members must supply the password.</p>
<h3>Notes about group passwords</h3>
<p> Group passwords are an inherent security problem since more than one person is permitted to know the password. However, groups are a useful tool for permitting co-operation between different users.</p>
<h2>OPTIONS</h2>
<p> Except for the <code>-A</code> and <code>-M</code> options, the options cannot be combined. </p>
<p> The options which apply to the <code>gpasswd</code> command are: </p>
<p> <code>-a</code>, <code>&#8211;add</code>&nbsp;<i>user</i></p>
<dl>
<dt>
<dd> Add the <i>user</i> to the named <i>group</i>.</dl>
<p> <code>-d</code>, <code>&#8211;delete</code>&nbsp;<i>user</i></p>
<dl>
<dt>
<dd> Remove the <i>user</i> from the named <i>group</i>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help message and exit.</dl>
<p> <code>-Q</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dt>
<dd> Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-r</code>, <code>&#8211;remove-password</code></p>
<dl>
<dt>
<dd> Remove the password from the named <i>group</i>. The group password will be empty. Only group members will be allowed to use <code>newgrp</code> to join the named <i>group</i>.</dl>
<p> <code>-R</code>, <code>&#8211;restrict</code></p>
<dl>
<dt>
<dd> Restrict the access to the named <i>group</i>. The group password is set to &quot;!&quot;. Only group members with a password will be allowed to use <code>newgrp</code> to join the named <i>group</i>.</dl>
<p> <code>-A</code>, <code>&#8211;administrators</code>&nbsp;<i>user</i>,&#8230;</p>
<dl>
<dt>
<dd> Set the list of administrative users.</dl>
<p> <code>-M</code>, <code>&#8211;members</code>&nbsp;<i>user</i>,&#8230;</p>
<dl>
<dt>
<dd> Set the list of group members.</dl>
<h2>CAVEATS</h2>
<p> This tool only operates on the /etc/group and /etc/gshadow files. Thus you cannot change any NIS or LDAP group. This must be performed on the corresponding server.</p>
<h2>CONFIGURATION</h2>
<p> The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>ENCRYPT_METHOD</code> (string)</p>
<dl>
<dt>
<dd> This defines the system default encryption algorithm for encrypting passwords (if no algorithm are specified on the command line). </p>
<p> It can take one of these values: <i>DES</i> (default), <i>MD5</i>, <i>SHA256</i>, <i>SHA512</i>. </p>
<p> Note: this parameter overrides the <code>MD5_CRYPT_ENAB</code> variable. </p>
<p> Note: This only affect the generation of group passwords. The generation of user passwords is done by PAM and subject to the PAM configuration. It is recommended to set this variable consistently with the PAM configuration.</dl>
<p> <code>MAX_MEMBERS_PER_GROUP</code> (number)</p>
<dl>
<dt>
<dd> Maximum members per group entry. When the maximum is reached, a new group entry (line) is started in /etc/group (with the same name, same password, and same GID). </p>
<p> The default value is 0, meaning that there are no limits in the number of members in a group. </p>
<p> This feature (split group) permits to limit the length of lines in the group file. This is useful to make sure that lines for NIS groups are not larger than 1024 characters. </p>
<p> If you need to enforce such limit, you can use 25. </p>
<p> Note: split groups may not be supported by all tools (even in the Shadow toolsuite). You should not use this variable unless you really need it.</dl>
<p> <code>MD5_CRYPT_ENAB</code> (boolean)</p>
<dl>
<dt>
<dd> Indicate if passwords must be encrypted using the MD5-based algorithm. If set to <i>yes</i>, new passwords will be encrypted using the MD5-based algorithm compatible with the one used by recent releases of FreeBSD. It supports passwords of unlimited length and longer salt strings. Set to <i>no</i> if you need to copy encrypted passwords to other systems which don&#8217;t understand the new algorithm. Default is <i>no</i>. </p>
<p> This variable is superseded by the <code>ENCRYPT_METHOD</code> variable or by any command line option used to configure the encryption algorithm. </p>
<p> This variable is deprecated. You should use <code>ENCRYPT_METHOD</code>. </p>
<p> Note: This only affect the generation of group passwords. The generation of user passwords is done by PAM and subject to the PAM configuration. It is recommended to set this variable consistently with the PAM configuration.</dl>
<p> <code>SHA_CRYPT_MIN_ROUNDS</code> (number), <code>SHA_CRYPT_MAX_ROUNDS</code> (number)</p>
<dl>
<dt>
<dd> When <code>ENCRYPT_METHOD</code> is set to <i>SHA256</i> or <i>SHA512</i>, this defines the number of SHA rounds used by the encryption algorithm by default (when the number of rounds is not specified on the command line). </p>
<p> With a lot of rounds, it is more difficult to brute forcing the password. But note also that more CPU resources will be needed to authenticate users. </p>
<p> If not specified, the libc will choose the default number of rounds (5000). </p>
<p> The values must be inside the 1000-999,999,999 range. </p>
<p> If only one of the <code>SHA_CRYPT_MIN_ROUNDS</code> or <code>SHA_CRYPT_MAX_ROUNDS</code> values is set, then this value will be used. </p>
<p> If <code>SHA_CRYPT_MIN_ROUNDS</code> &gt; <code>SHA_CRYPT_MAX_ROUNDS</code>, the highest value will be used. </p>
<p> Note: This only affect the generation of group passwords. The generation of user passwords is done by PAM and subject to the PAM configuration. It is recommended to set this variable consistently with the PAM configuration.</dl>
<h2>FILES</h2>
<p> /etc/group</p>
<dl>
<dt>
<dd> Group account information.</dl>
<p> /etc/gshadow</p>
<dl>
<dt>
<dd> Secure group account information.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-newgrp/">newgrp</a></code>(1), <code><a href="/docs/linux/man/8-groupadd/">groupadd</a></code>(8), <code><a href="/docs/linux/man/8-groupdel/">groupdel</a></code>(8), <code><a href="/docs/linux/man/8-groupmod/">groupmod</a></code>(8), <code><a href="/docs/linux/man/8-grpck/">grpck</a></code>(8), <code><a href="/docs/linux/man/5-group/">group</a></code>(5), <code><a href="/docs/linux/man/5-gshadow/">gshadow</a></code>(5). </p>
<h2>Index</h2>
