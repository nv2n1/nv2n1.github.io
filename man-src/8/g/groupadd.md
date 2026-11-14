---
title: "groupadd(8)"
name: "groupadd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-groupadd/"
description: "groupadd – create a new group"
---

<p>groupadd &#8211; create a new group</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>groupadd</code> [<i>options</i>] <i>group</i></dl>
<h2>Description</h2>
<dd>The <code>groupadd</code> command creates a new group account using the values specified on the command line plus the default values from the system. The new group will be entered into the system files as needed.</p>
<h2>Options</h2>
<p>The options which apply to the <code>groupadd</code> command are: </p>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dd>This option causes the command to simply exit with success status if the specified group already exists. When used with <code>-g</code>, and the specified GID already exists, another (unique) GID is chosen (i.e. <code>-g</code> is turned off).</dl>
<p> <code>-g</code>, <code>&#8211;gid</code>&nbsp;<i>GID</i></p>
<dl>
<dd>The numerical value of the group&#8217;s ID. This value must be unique, unless the <code>-o</code> option is used. The value must be non-negative. The default is to use the smallest ID value greater than or equal to <code>GID_MIN</code> and greater than every other group. </p>
<p> See also the <code>-r</code> option and the <code>GID_MAX</code> description.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-K</code>, <code>&#8211;key</code>&nbsp;<i>KEY</i>=<i>VALUE</i></p>
<dl>
<dd>Overrides /etc/login.defs defaults (GID_MIN, GID_MAX and others). Multiple <code>-K</code> options can be specified. </p>
<p> Example: <code>-K</code>&nbsp;<i>GID_MIN</i>=<i>100</i>&nbsp; <code>-K</code>&nbsp;<i>GID_MAX</i>=<i>499</i> </p>
<p> Note: <code>-K</code>&nbsp;<i>GID_MIN</i>=<i>10</i>,<i>GID_MAX</i>=<i>499</i> doesn&#8217;t work yet.</dl>
<p> <code>-o</code>, <code>&#8211;non-unique</code></p>
<dl>
<dd>This option permits to add a group with a non-unique GID.</dl>
<p> <code>-p</code>, <code>&#8211;password</code>&nbsp;<i>PASSWORD</i></p>
<dl>
<dd>The encrypted password, as returned by <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3). The default is to disable the password. </p>
<p> <code>Note:</code> This option is not recommended because the password (or encrypted password) will be visible by users listing the processes. </p>
<p> You should make sure the password respects the system&#8217;s password policy.</dl>
<p> <code>-r</code>, <code>&#8211;system</code></p>
<dl>
<dd>Create a system group. </p>
<p> The numeric identifiers of new system groups are chosen in the <code>SYS_GID_MIN</code>&#8211;<code>SYS_GID_MAX</code> range, defined in login.defs, instead of <code>GID_MIN</code>&#8211;<code>GID_MAX</code>.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-P</code>, <code>&#8211;prefix</code>&nbsp;<i>PREFIX_DIR</i></p>
<dl>
<dd>Apply changes in the <i>PREFIX_DIR</i> directory and use the configuration files from the <i>PREFIX_DIR</i> directory. This option does not chroot and is intended for preparing a cross-compilation target. Some limitations: NIS and LDAP users/groups are not verified. PAM authentication is using the host files. No SELINUX support.</dl>
<h2>Configuration</h2>
<p>The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>GID_MAX</code> (number), <code>GID_MIN</code> (number)</p>
<dl>
<dd>Range of group IDs used for the creation of regular groups by <code>useradd</code>, <code>groupadd</code>, or <code>newusers</code>. </p>
<p> The default value for <code>GID_MIN</code> (resp. <code>GID_MAX</code>) is 1000 (resp. 60000).</dl>
<p> <code>MAX_MEMBERS_PER_GROUP</code> (number)</p>
<dl>
<dd>Maximum members per group entry. When the maximum is reached, a new group entry (line) is started in /etc/group (with the same name, same password, and same GID). </p>
<p> The default value is 0, meaning that there are no limits in the number of members in a group. </p>
<p> This feature (split group) permits to limit the length of lines in the group file. This is useful to make sure that lines for NIS groups are not larger than 1024 characters. </p>
<p> If you need to enforce such limit, you can use 25. </p>
<p> Note: split groups may not be supported by all tools (even in the Shadow toolsuite). You should not use this variable unless you really need it.</dl>
<p> <code>SYS_GID_MAX</code> (number), <code>SYS_GID_MIN</code> (number)</p>
<dl>
<dd>Range of group IDs used for the creation of system groups by <code>useradd</code>, <code>groupadd</code>, or <code>newusers</code>. </p>
<p> The default value for <code>SYS_GID_MIN</code> (resp. <code>SYS_GID_MAX</code>) is 101 (resp. <code>GID_MIN</code>-1).</dl>
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
<h2>Caveats</h2>
<p>It is usually recommended to only use groupnames that begin with a lower case letter or an underscore, followed by lower case letters, digits, underscores, or dashes. They can end with a dollar sign. In regular expression terms: [a-z_][a-z0-9_-]*[$]? </p>
<p> On Debian, the only constraints are that groupnames must neither start with a dash (&#8216;-&#8216;) nor plus (&#8216;+&#8217;) nor tilde (&#8216;~&#8217;) nor contain a colon (&#8216;:&#8217;), a comma (&#8216;,&#8217;), or a whitespace (space:&#8217; &#8216;, end of line: &#8216;
&#8217;, tabulation: &#8216;	&#8217;, etc.). </p>
<p> On Ubuntu, the same constraints as Debian are in place, with the additional constraint that the groupname cannot be fully numeric. This includes octal and hexadecimal syntax. </p>
<p> Groupnames may only be up to 32 characters long. </p>
<p> You may not add a NIS or LDAP group. This must be performed on the corresponding server. </p>
<p> If the groupname already exists in an external group database such as NIS or LDAP, <code>groupadd</code> will deny the group creation request.</p>
<h2>Exit Values</h2>
<p>The <code>groupadd</code> command exits with the following values: </p>
<p> <i>0</i></p>
<dl>
<dd>success</dl>
<p> <i>2</i></p>
<dl>
<dd>invalid command syntax</dl>
<p> <i>3</i></p>
<dl>
<dd>invalid argument to option</dl>
<p> <i>4</i></p>
<dl>
<dd>GID not unique (when <code>-o</code> not used)</dl>
<p> <i>9</i></p>
<dl>
<dd>group name not unique</dl>
<p> <i>10</i></p>
<dl>
<dd>can&#8217;t update group file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chfn/">chfn</a></code>(1), <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/8-gpasswd/">gpasswd</a></code>(8), <code><a href="/docs/linux/man/8-groupdel/">groupdel</a></code>(8), <code><a href="/docs/linux/man/8-groupmod/">groupmod</a></code>(8), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/8-useradd/">useradd</a></code>(8), <code><a href="/docs/linux/man/8-userdel/">userdel</a></code>(8), <code><a href="/docs/linux/man/8-usermod/">usermod</a></code>(8). </p>
