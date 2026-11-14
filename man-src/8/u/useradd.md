---
title: "useradd(8)"
name: "useradd"
section: "8"
letter: "u"
url: "/docs/linux/man/8-useradd/"
description: "useradd – create a new user or update default new user information"
---

<p>useradd &#8211; create a new user or update default new user information</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>useradd</code> [<i>options</i>] <i>LOGIN</i></p>
<dt> <code>useradd</code> -D</p>
<dt> <code>useradd</code> -D [<i>options</i>]</dl>
<h2>Description</h2>
<p><code>useradd</code></p>
<dd>is a low level utility for adding users. On Debian, administrators should usually use <code><a href="/docs/linux/man/8-adduser/">adduser</a></code>(8) instead. </p>
<p> When invoked without the <code>-D</code> option, the <code>useradd</code> command creates a new user account using the values specified on the command line plus the default values from the system. Depending on command line options, the <code>useradd</code> command will update system files and may also create the new user&#8217;s home directory and copy initial files. </p>
<p> By default, a group will also be created for the new user (see <code>-g</code>, <code>-N</code>, <code>-U</code>, and <code>USERGROUPS_ENAB</code>).</p>
<h2>Options</h2>
<p>The options which apply to the <code>useradd</code> command are: </p>
<p> <code>&#8211;badname</code>&nbsp;</p>
<dl>
<dd>Allow names that do not conform to standards.</dl>
<p> <code>-b</code>, <code>&#8211;base-dir</code>&nbsp;<i>BASE_DIR</i></p>
<dl>
<dd>The default base directory for the system if <code>-d</code>&nbsp;<i>HOME_DIR</i> is not specified. <i>BASE_DIR</i> is concatenated with the account name to define the home directory. If the <code>-m</code> option is not used, <i>BASE_DIR</i> must exist. </p>
<p> If this option is not specified, <code>useradd</code> will use the base directory specified by the <code>HOME</code> variable in /etc/default/useradd, or /home by default.</dl>
<p> <code>-c</code>, <code>&#8211;comment</code>&nbsp;<i>COMMENT</i></p>
<dl>
<dd>Any text string. It is generally a short description of the login, and is currently used as the field for the user&#8217;s full name.</dl>
<p> <code>-d</code>, <code>&#8211;home-dir</code>&nbsp;<i>HOME_DIR</i></p>
<dl>
<dd>The new user will be created using <i>HOME_DIR</i> as the value for the user&#8217;s login directory. The default is to append the <i>LOGIN</i> name to <i>BASE_DIR</i> and use that as the login directory name. The directory <i>HOME_DIR</i> does not have to exist but will not be created if it is missing.</dl>
<p> <code>-D</code>, <code>&#8211;defaults</code></p>
<dl>
<dd>See below, the subsection &quot;Changing the default values&quot;.</dl>
<p> <code>-e</code>, <code>&#8211;expiredate</code>&nbsp;<i>EXPIRE_DATE</i></p>
<dl>
<dd>The date on which the user account will be disabled. The date is specified in the format <i>YYYY-MM-DD</i>. </p>
<p> If not specified, <code>useradd</code> will use the default expiry date specified by the <code>EXPIRE</code> variable in /etc/default/useradd, or an empty string (no expiry) by default.</dl>
<p> <code>-f</code>, <code>&#8211;inactive</code>&nbsp;<i>INACTIVE</i></p>
<dl>
<dd>The number of days after a password expires until the account is permanently disabled. A value of 0 disables the account as soon as the password has expired, and a value of -1 disables the feature. </p>
<p> If not specified, <code>useradd</code> will use the default inactivity period specified by the <code>INACTIVE</code> variable in /etc/default/useradd, or -1 by default.</dl>
<p> <code>-g</code>, <code>&#8211;gid</code>&nbsp;<i>GROUP</i></p>
<dl>
<dd>The group name or number of the user&#8217;s initial login group. The group name must exist. A group number must refer to an already existing group. </p>
<p> If not specified, the behavior of <code>useradd</code> will depend on the <code>USERGROUPS_ENAB</code> variable in /etc/login.defs. If this variable is set to <i>yes</i> (or <code>-U/&#8211;user-group</code> is specified on the command line), a group will be created for the user, with the same name as her loginname. If the variable is set to <i>no</i> (or <code>-N/&#8211;no-user-group</code> is specified on the command line), useradd will set the primary group of the new user to the value specified by the <code>GROUP</code> variable in /etc/default/useradd, or 100 by default.</dl>
<p> <code>-G</code>, <code>&#8211;groups</code>&nbsp;<i>GROUP1</i>[<i>,GROUP2,&#8230;</i>[<i>,GROUPN</i>]]]</p>
<dl>
<dd>A list of supplementary groups which the user is also a member of. Each group is separated from the next by a comma, with no intervening whitespace. The groups are subject to the same restrictions as the group given with the <code>-g</code> option. The default is for the user to belong only to the initial group.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-k</code>, <code>&#8211;skel</code>&nbsp;<i>SKEL_DIR</i></p>
<dl>
<dd>The skeleton directory, which contains files and directories to be copied in the user&#8217;s home directory, when the home directory is created by <code>useradd</code>. </p>
<p> This option is only valid if the <code>-m</code> (or <code>&#8211;create-home</code>) option is specified. </p>
<p> If this option is not set, the skeleton directory is defined by the <code>SKEL</code> variable in /etc/default/useradd or, by default, /etc/skel. </p>
<p> If possible, the ACLs and extended attributes are copied.</dl>
<p> <code>-K</code>, <code>&#8211;key</code>&nbsp;<i>KEY</i>=<i>VALUE</i></p>
<dl>
<dd>Overrides /etc/login.defs defaults (<code>UID_MIN</code>, <code>UID_MAX</code>, <code>UMASK</code>, <code>PASS_MAX_DAYS</code> and others). </p>
<p> Example: <code>-K</code>&nbsp;<i>PASS_MAX_DAYS</i>=<i>-1</i> can be used when creating system account to turn off password aging, even though system account has no password at all. Multiple <code>-K</code> options can be specified, e.g.: <code>-K</code>&nbsp;<i>UID_MIN</i>=<i>100</i>&nbsp; <code>-K</code>&nbsp;<i>UID_MAX</i>=<i>499</i></dl>
<p> <code>-l</code>, <code>&#8211;no-log-init</code></p>
<dl>
<dd>Do not add the user to the lastlog and faillog databases. </p>
<p> By default, the user&#8217;s entries in the lastlog and faillog databases are reset to avoid reusing the entry from a previously deleted user. </p>
<p> For the compatibility with previous Debian&#8217;s <code>useradd</code>, the <code>-O</code> option is also supported.</dl>
<p> <code>-m</code>, <code>&#8211;create-home</code></p>
<dl>
<dd>Create the user&#8217;s home directory if it does not exist. The files and directories contained in the skeleton directory (which can be defined with the <code>-k</code> option) will be copied to the home directory. </p>
<p> By default, if this option is not specified and <code>CREATE_HOME</code> is not enabled, no home directories are created.</dl>
<p> <code>-M</code>, <code>&#8211;no-create-home</code></p>
<dl>
<dd>Do no create the user&#8217;s home directory, even if the system wide setting from /etc/login.defs (<code>CREATE_HOME</code>) is set to <i>yes</i>.</dl>
<p> <code>-N</code>, <code>&#8211;no-user-group</code></p>
<dl>
<dd>Do not create a group with the same name as the user, but add the user to the group specified by the <code>-g</code> option or by the <code>GROUP</code> variable in /etc/default/useradd. </p>
<p> The default behavior (if the <code>-g</code>, <code>-N</code>, and <code>-U</code> options are not specified) is defined by the <code>USERGROUPS_ENAB</code> variable in /etc/login.defs.</dl>
<p> <code>-o</code>, <code>&#8211;non-unique</code></p>
<dl>
<dd>Allow the creation of a user account with a duplicate (non-unique) UID. </p>
<p> This option is only valid in combination with the <code>-u</code> option.</dl>
<p> <code>-p</code>, <code>&#8211;password</code>&nbsp;<i>PASSWORD</i></p>
<dl>
<dd>The encrypted password, as returned by <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3). The default is to disable the password. </p>
<p> <code>Note:</code> This option is not recommended because the password (or encrypted password) will be visible by users listing the processes. </p>
<p> You should make sure the password respects the system&#8217;s password policy.</dl>
<p> <code>-r</code>, <code>&#8211;system</code></p>
<dl>
<dd>Create a system account. </p>
<p> System users will be created with no aging information in /etc/shadow, and their numeric identifiers are chosen in the <code>SYS_UID_MIN</code>&#8211;<code>SYS_UID_MAX</code> range, defined in /etc/login.defs, instead of <code>UID_MIN</code>&#8211;<code>UID_MAX</code> (and their <code>GID</code> counterparts for the creation of groups). </p>
<p> Note that <code>useradd</code> will not create a home directory for such a user, regardless of the default setting in /etc/login.defs (<code>CREATE_HOME</code>). You have to specify the <code>-m</code> options if you want a home directory for a system account to be created.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-P</code>, <code>&#8211;prefix</code>&nbsp;<i>PREFIX_DIR</i></p>
<dl>
<dd>Apply changes in the <i>PREFIX_DIR</i> directory and use the configuration files from the <i>PREFIX_DIR</i> directory. This option does not chroot and is intended for preparing a cross-compilation target. Some limitations: NIS and LDAP users/groups are not verified. PAM authentication is using the host files. No SELINUX support.</dl>
<p> <code>-s</code>, <code>&#8211;shell</code>&nbsp;<i>SHELL</i></p>
<dl>
<dd>The name of the user&#8217;s login shell. The default is to leave this field blank, which causes the system to select the default login shell specified by the <code>SHELL</code> variable in /etc/default/useradd, or an empty string by default.</dl>
<p> <code>-u</code>, <code>&#8211;uid</code>&nbsp;<i>UID</i></p>
<dl>
<dd>The numerical value of the user&#8217;s ID. This value must be unique, unless the <code>-o</code> option is used. The value must be non-negative. The default is to use the smallest ID value greater than or equal to <code>UID_MIN</code> and greater than every other user. </p>
<p> See also the <code>-r</code> option and the <code>UID_MAX</code> description.</dl>
<p> <code>-U</code>, <code>&#8211;user-group</code></p>
<dl>
<dd>Create a group with the same name as the user, and add the user to this group. </p>
<p> The default behavior (if the <code>-g</code>, <code>-N</code>, and <code>-U</code> options are not specified) is defined by the <code>USERGROUPS_ENAB</code> variable in /etc/login.defs.</dl>
<p> <code>-Z</code>, <code>&#8211;selinux-user</code>&nbsp;<i>SEUSER</i></p>
<dl>
<dd>The SELinux user for the user&#8217;s login. The default is to leave this field blank, which causes the system to select the default SELinux user.</dl>
<h3>Changing the default values</h3>
<p>When invoked with only the <code>-D</code> option, <code>useradd</code> will display the current default values. When invoked with <code>-D</code> plus other options, <code>useradd</code> will update the default values for the specified options. Valid default-changing options are: </p>
<p> <code>-b</code>, <code>&#8211;base-dir</code>&nbsp;<i>BASE_DIR</i></p>
<dl>
<dd>The path prefix for a new user&#8217;s home directory. The user&#8217;s name will be affixed to the end of <i>BASE_DIR</i> to form the new user&#8217;s home directory name, if the <code>-d</code> option is not used when creating a new account. </p>
<p> This option sets the <code>HOME</code> variable in /etc/default/useradd.</dl>
<p> <code>-e</code>, <code>&#8211;expiredate</code>&nbsp;<i>EXPIRE_DATE</i></p>
<dl>
<dd>The date on which the user account is disabled. </p>
<p> This option sets the <code>EXPIRE</code> variable in /etc/default/useradd.</dl>
<p> <code>-f</code>, <code>&#8211;inactive</code>&nbsp;<i>INACTIVE</i></p>
<dl>
<dd>The number of days after a password has expired before the account will be disabled. </p>
<p> This option sets the <code>INACTIVE</code> variable in /etc/default/useradd.</dl>
<p> <code>-g</code>, <code>&#8211;gid</code>&nbsp;<i>GROUP</i></p>
<dl>
<dd>The group name or ID for a new user&#8217;s initial group (when the <code>-N/&#8211;no-user-group</code> is used or when the <code>USERGROUPS_ENAB</code> variable is set to <i>no</i> in /etc/login.defs). The named group must exist, and a numerical group ID must have an existing entry. </p>
<p> This option sets the <code>GROUP</code> variable in /etc/default/useradd.</dl>
<p> <code>-s</code>, <code>&#8211;shell</code>&nbsp;<i>SHELL</i></p>
<dl>
<dd>The name of a new user&#8217;s login shell. </p>
<p> This option sets the <code>SHELL</code> variable in /etc/default/useradd.</dl>
<h2>Notes</h2>
<p>The system administrator is responsible for placing the default user files in the /etc/skel/ directory (or any other skeleton directory specified in /etc/default/useradd or on the command line).</p>
<h2>Caveats</h2>
<p>You may not add a user to a NIS or LDAP group. This must be performed on the corresponding server. </p>
<p> Similarly, if the username already exists in an external user database such as NIS or LDAP, <code>useradd</code> will deny the user account creation request. </p>
<p> It is usually recommended to only use usernames that begin with a lower case letter or an underscore, followed by lower case letters, digits, underscores, or dashes. They can end with a dollar sign. In regular expression terms: [a-z_][a-z0-9_-]*[$]? </p>
<p> On Debian, the only constraints are that usernames must neither start with a dash (&#8216;-&#8216;) nor plus (&#8216;+&#8217;) nor tilde (&#8216;~&#8217;) nor contain a colon (&#8216;:&#8217;), a comma (&#8216;,&#8217;), or a whitespace (space: &#8216; &#8216;, end of line: &#8216;
&#8217;, tabulation: &#8216;	&#8217;, etc.). Note that using a slash (&#8216;/&#8217;) may break the default algorithm for the definition of the user&#8217;s home directory. </p>
<p> On Ubuntu, the same constraints as Debian are in place, with the additional constraint that the username cannot be fully numeric. This includes octal and hexadecimal syntax. </p>
<p> Usernames may only be up to 32 characters long.</p>
<h2>Configuration</h2>
<p>The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>CREATE_HOME</code> (boolean)</p>
<dl>
<dd>Indicate if a home directory should be created by default for new users. </p>
<p> This setting does not apply to system users, and can be overridden on the command line.</dl>
<p> <code>GID_MAX</code> (number), <code>GID_MIN</code> (number)</p>
<dl>
<dd>Range of group IDs used for the creation of regular groups by <code>useradd</code>, <code>groupadd</code>, or <code>newusers</code>. </p>
<p> The default value for <code>GID_MIN</code> (resp. <code>GID_MAX</code>) is 1000 (resp. 60000).</dl>
<p> <code>HOME_MODE</code> (number)</p>
<dl>
<dd>The mode for new home directories. If not specified, the <code>UMASK</code> is used to create the mode. </p>
<p> <code>useradd</code> and <code>newusers</code> use this to set the mode of the home directory they create.</dl>
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
<p> <code>PASS_MAX_DAYS</code> (number)</p>
<dl>
<dd>The maximum number of days a password may be used. If the password is older than this, a password change will be forced. If not specified, -1 will be assumed (which disables the restriction).</dl>
<p> <code>PASS_MIN_DAYS</code> (number)</p>
<dl>
<dd>The minimum number of days allowed between password changes. Any password changes attempted sooner than this will be rejected. If not specified, -1 will be assumed (which disables the restriction).</dl>
<p> <code>PASS_WARN_AGE</code> (number)</p>
<dl>
<dd>The number of days warning given before a password expires. A zero means warning is given only upon the day of expiration, a negative value means no warning is given. If not specified, no warning will be provided.</dl>
<p> <code>SUB_GID_MIN</code> (number), <code>SUB_GID_MAX</code> (number), <code>SUB_GID_COUNT</code> (number)</p>
<dl>
<dd>If /etc/subuid exists, the commands <code>useradd</code> and <code>newusers</code> (unless the user already have subordinate group IDs) allocate <code>SUB_GID_COUNT</code> unused group IDs from the range <code>SUB_GID_MIN</code> to <code>SUB_GID_MAX</code> for each new user. </p>
<p> The default values for <code>SUB_GID_MIN</code>, <code>SUB_GID_MAX</code>, <code>SUB_GID_COUNT</code> are respectively 100000, 600100000 and 65536.</dl>
<p> <code>SUB_UID_MIN</code> (number), <code>SUB_UID_MAX</code> (number), <code>SUB_UID_COUNT</code> (number)</p>
<dl>
<dd>If /etc/subuid exists, the commands <code>useradd</code> and <code>newusers</code> (unless the user already have subordinate user IDs) allocate <code>SUB_UID_COUNT</code> unused user IDs from the range <code>SUB_UID_MIN</code> to <code>SUB_UID_MAX</code> for each new user. </p>
<p> The default values for <code>SUB_UID_MIN</code>, <code>SUB_UID_MAX</code>, <code>SUB_UID_COUNT</code> are respectively 100000, 600100000 and 65536.</dl>
<p> <code>SYS_GID_MAX</code> (number), <code>SYS_GID_MIN</code> (number)</p>
<dl>
<dd>Range of group IDs used for the creation of system groups by <code>useradd</code>, <code>groupadd</code>, or <code>newusers</code>. </p>
<p> The default value for <code>SYS_GID_MIN</code> (resp. <code>SYS_GID_MAX</code>) is 101 (resp. <code>GID_MIN</code>-1).</dl>
<p> <code>SYS_UID_MAX</code> (number), <code>SYS_UID_MIN</code> (number)</p>
<dl>
<dd>Range of user IDs used for the creation of system users by <code>useradd</code> or <code>newusers</code>. </p>
<p> The default value for <code>SYS_UID_MIN</code> (resp. <code>SYS_UID_MAX</code>) is 101 (resp. <code>UID_MIN</code>-1).</dl>
<p> <code>UID_MAX</code> (number), <code>UID_MIN</code> (number)</p>
<dl>
<dd>Range of user IDs used for the creation of regular users by <code>useradd</code> or <code>newusers</code>. </p>
<p> The default value for <code>UID_MIN</code> (resp. <code>UID_MAX</code>) is 1000 (resp. 60000).</dl>
<p> <code>UMASK</code> (number)</p>
<dl>
<dd>The file mode creation mask is initialized to this value. If not specified, the mask will be initialized to 022. </p>
<p> <code>useradd</code> and <code>newusers</code> use this mask to set the mode of the home directory they create if <code>HOME_MODE</code> is not set. </p>
<p> It is also used by <code>pam_umask</code> as the default umask value.</dl>
<p> <code>USERGROUPS_ENAB</code> (boolean)</p>
<dl>
<dd>If set to <i>yes</i>, <code>userdel</code> will remove the user&#8217;s group if it contains no more members, and <code>useradd</code> will create by default a group with the name of the user.</dl>
<h2>Files</h2>
<p>/etc/passwd</p>
<dl>
<dd>User account information.</dl>
<p> /etc/shadow</p>
<dl>
<dd>Secure user account information.</dl>
<p> /etc/group</p>
<dl>
<dd>Group account information.</dl>
<p> /etc/gshadow</p>
<dl>
<dd>Secure group account information.</dl>
<p> /etc/default/useradd</p>
<dl>
<dd>Default values for account creation.</dl>
<p> /etc/skel/</p>
<dl>
<dd>Directory containing default files.</dl>
<p> /etc/subgid</p>
<dl>
<dd>Per user subordinate group IDs.</dl>
<p> /etc/subuid</p>
<dl>
<dd>Per user subordinate user IDs.</dl>
<p> /etc/login.defs</p>
<dl>
<dd>Shadow password suite configuration.</dl>
<h2>Exit Values</h2>
<p>The <code>useradd</code> command exits with the following values: </p>
<p> <i>0</i></p>
<dl>
<dd>success</dl>
<p> <i>1</i></p>
<dl>
<dd>can&#8217;t update password file</dl>
<p> <i>2</i></p>
<dl>
<dd>invalid command syntax</dl>
<p> <i>3</i></p>
<dl>
<dd>invalid argument to option</dl>
<p> <i>4</i></p>
<dl>
<dd>UID already in use (and no <code>-o</code>)</dl>
<p> <i>6</i></p>
<dl>
<dd>specified group doesn&#8217;t exist</dl>
<p> <i>9</i></p>
<dl>
<dd>username already in use</dl>
<p> <i>10</i></p>
<dl>
<dd>can&#8217;t update group file</dl>
<p> <i>12</i></p>
<dl>
<dd>can&#8217;t create home directory</dl>
<p> <i>14</i></p>
<dl>
<dd>can&#8217;t update SELinux user mapping</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chfn/">chfn</a></code>(1), <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3), <code><a href="/docs/linux/man/8-groupadd/">groupadd</a></code>(8), <code><a href="/docs/linux/man/8-groupdel/">groupdel</a></code>(8), <code><a href="/docs/linux/man/8-groupmod/">groupmod</a></code>(8), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/8-newusers/">newusers</a></code>(8), <code><a href="/docs/linux/man/5-subgid/">subgid</a></code>(5), <code><a href="/docs/linux/man/5-subuid/">subuid</a></code>(5), <code><a href="/docs/linux/man/8-userdel/">userdel</a></code>(8), <code><a href="/docs/linux/man/8-usermod/">usermod</a></code>(8). </p>
