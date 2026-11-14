---
title: "newusers(8)"
name: "newusers"
section: "8"
letter: "n"
url: "/docs/linux/man/8-newusers/"
description: "newusers – update and create new users in batch"
---

<p>newusers &#8211; update and create new users in batch</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>newusers</code> [<i>options</i>] [<i>file</i>]</dl>
<h2>Description</h2>
<dd>The <code>newusers</code> command reads a <i>file</i> (or the standard input by default) and uses this information to update a set of existing users or to create new users. Each line is in the same format as the standard password file (see <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5)) with the exceptions explained below: </p>
<p> pw_name:pw_passwd:pw_uid:pw_gid:pw_gecos:pw_dir:pw_shell </p>
<p> <i>pw_name</i></p>
<dl>
<dd>This is the name of the user. </p>
<p> It can be the name of a new user or the name of an existing user (or a user created before by <code>newusers</code>). In case of an existing user, the user&#8217;s information will be changed, otherwise a new user will be created.</dl>
<p> <i>pw_passwd</i></p>
<dl>
<dd>This field will be encrypted and used as the new value of the encrypted password.</dl>
<p> <i>pw_uid</i></p>
<dl>
<dd>This field is used to define the UID of the user. </p>
<p> If the field is empty, a new (unused) UID will be defined automatically by <code>newusers</code>. </p>
<p> If this field contains a number, this number will be used as the UID. </p>
<p> If this field contains the name of an existing user (or the name of a user created before by <code>newusers</code>), the UID of the specified user will be used. </p>
<p> If the UID of an existing user is changed, the files ownership of the user&#8217;s file should be fixed manually.</dl>
<p> <i>pw_gid</i></p>
<dl>
<dd>This field is used to define the primary group ID for the user. </p>
<p> If this field contains the name of an existing group (or a group created before by <code>newusers</code>), the GID of this group will be used as the primary group ID for the user. </p>
<p> If this field is a number, this number will be used as the primary group ID of the user. If no groups exist with this GID, a new group will be created with this GID, and the name of the user. </p>
<p> If this field is empty, a new group will be created with the name of the user and a GID will be automatically defined by <code>newusers</code> to be used as the primary group ID for the user and as the GID for the new group. </p>
<p> If this field contains the name of a group which does not exist (and was not created before by <code>newusers</code>), a new group will be created with the specified name and a GID will be automatically defined by <code>newusers</code> to be used as the primary group ID for the user and GID for the new group.</dl>
<p> <i>pw_gecos</i></p>
<dl>
<dd>This field is copied in the GECOS field of the user.</dl>
<p> <i>pw_dir</i></p>
<dl>
<dd>This field is used to define the home directory of the user. </p>
<p> If this field does not specify an existing directory, the specified directory is created, with ownership set to the user being created or updated and its primary group. </p>
<p> If the home directory of an existing user is changed, <code>newusers</code> does not move or copy the content of the old directory to the new location. This should be done manually.</dl>
<p> <i>pw_shell</i></p>
<dl>
<dd>This field defines the shell of the user. No checks are performed on this field.</dl>
<p> <code>newusers</code> first tries to create or change all the specified users, and then write these changes to the user or group databases. If an error occurs (except in the final writes to the databases), no changes are committed to the databases. </p>
<p> During this first pass, users are created with a locked password (and passwords are not changed for the users which are not created). A second pass is used to update the passwords using PAM. Failures to update a password are reported, but will not stop the other password updates. </p>
<p> This command is intended to be used in a large system environment where many accounts are updated at a single time.</p>
<h2>Options</h2>
<p>The options which apply to the <code>newusers</code> command are: </p>
<p> <code>&#8211;badname</code>&nbsp;</p>
<dl>
<dd>Allow names that do not conform to standards.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-r</code>, <code>&#8211;system</code></p>
<dl>
<dd>Create a system account. </p>
<p> System users will be created with no aging information in /etc/shadow, and their numeric identifiers are chosen in the <code>SYS_UID_MIN</code>&#8211;<code>SYS_UID_MAX</code> range, defined in login.defs, instead of <code>UID_MIN</code>&#8211;<code>UID_MAX</code> (and their <code>GID</code> counterparts for the creation of groups).</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<h2>Caveats</h2>
<p>The input file must be protected since it contains unencrypted passwords.</p>
<h2>Configuration</h2>
<p>The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>GID_MAX</code> (number), <code>GID_MIN</code> (number)</p>
<dl>
<dd>Range of group IDs used for the creation of regular groups by <code>useradd</code>, <code>groupadd</code>, or <code>newusers</code>. </p>
<p> The default value for <code>GID_MIN</code> (resp. <code>GID_MAX</code>) is 1000 (resp. 60000).</dl>
<p> <code>HOME_MODE</code> (number)</p>
<dl>
<dd>The mode for new home directories. If not specified, the <code>UMASK</code> is used to create the mode. </p>
<p> <code>useradd</code> and <code>newusers</code> use this to set the mode of the home directory they create.</dl>
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
<p> /etc/login.defs</p>
<dl>
<dd>Shadow password suite configuration.</dl>
<p> /etc/pam.d/newusers</p>
<dl>
<dd>PAM configuration for <code>newusers</code>.</dl>
<p> /etc/subgid</p>
<dl>
<dd>Per user subordinate group IDs.</dl>
<p> /etc/subuid</p>
<dl>
<dd>Per user subordinate user IDs.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/5-subgid/">subgid</a></code>(5), <code><a href="/docs/linux/man/5-subuid/">subuid</a></code>(5), <code><a href="/docs/linux/man/8-useradd/">useradd</a></code>(8). </p>
