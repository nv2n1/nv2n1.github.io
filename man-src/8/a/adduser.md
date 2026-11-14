---
title: "adduser(8)"
name: "adduser"
section: "8"
letter: "a"
url: "/docs/linux/man/8-adduser/"
description: "adduser, addgroup – add a user or group to the system"
---

<p>adduser, addgroup &#8211; add a user or group to the system</p>
<h2>Synopsis</h2>
<p><code>adduser</code> [options] [&#8211;home DIR] [&#8211;shell SHELL] [&#8211;no-create-home] [&#8211;uid ID] [&#8211;firstuid ID] [&#8211;lastuid ID] [&#8211;ingroup GROUP | &#8211;gid ID] [&#8211;disabled-password] [&#8211;disabled-login] [&#8211;gecos GECOS] [&#8211;add_extra_groups] [&#8211;encrypt-home] user </p>
<p> <code>adduser</code> &#8211;system [options] [&#8211;home DIR] [&#8211;shell SHELL] [&#8211;no-create-home] [&#8211;uid ID] [&#8211;group | &#8211;ingroup GROUP | &#8211;gid ID] [&#8211;disabled-password] [&#8211;disabled-login] [&#8211;gecos GECOS] user </p>
<p> <code>addgroup</code> [options] [&#8211;gid ID] group </p>
<p> <code>addgroup</code> &#8211;system [options] [&#8211;gid ID] group </p>
<p> <code>adduser</code> [options] user group</p>
<h3>Common Options</h3>
<p>[&#8211;quiet] [&#8211;debug] [&#8211;force-badname] [&#8211;help|-h] [&#8211;version] [&#8211;conf FILE]</p>
<h2>Description</h2>
<p><code>adduser</code> and <code>addgroup</code> add users and groups to the system according to command line options and configuration information in <i>/etc/adduser.conf</i>. They are friendlier front ends to the low level tools like <code>useradd,</code> <code>groupadd</code> and <code>usermod</code> programs, by default choosing Debian policy conformant UID and GID values, creating a home directory with skeletal configuration, running a custom script, and other features. <code>adduser</code> and <code>addgroup</code> can be run in one of five modes:</p>
<h3>Add a normal user</h3>
<p>If called with one non-option argument and without the <code>&#8211;system</code> or <code>&#8211;group</code> options, <code>adduser</code> will add a normal user. </p>
<p> <code>adduser</code> will choose the first available UID from the range specified for normal users in the configuration file. The UID can be overridden with the <code>&#8211;uid</code> option. </p>
<p> The range specified in the configuration file may be overridden with the <code>&#8211;firstuid</code> and <code>&#8211;lastuid</code> options. </p>
<p> By default, each user in Debian GNU/Linux is given a corresponding group with the same name. Usergroups allow group writable directories to be easily maintained by placing the appropriate users in the new group, setting the set-group-ID bit in the directory, and ensuring that all users use a umask of 002. If this option is turned off by setting <code>USERGROUPS</code> to <i>no</i>, all users&#8217; GIDs are set to <code>USERS_GID</code>. Users&#8217; primary groups can also be overridden from the command line with the <code>&#8211;gid</code> or <code>&#8211;ingroup</code> options to set the group by id or name, respectively. Also, users can be added to one or more groups defined in adduser.conf either by setting ADD_EXTRA_GROUPS to 1 in adduser.conf, or by passing <code>&#8211;add_extra_groups </code> on the commandline. </p>
<p> <code>adduser</code> will create a home directory subject to <code>DHOME</code>, <code>GROUPHOMES</code>, and <code>LETTERHOMES</code>. The home directory can be overridden from the command line with the <code>&#8211;home</code> option, and the shell with the <code>&#8211;shell</code> option. The home directory&#8217;s set-group-ID bit is set if <code>USERGROUPS</code> is <i>yes</i> so that any files created in the user&#8217;s home directory will have the correct group. </p>
<p> <code>adduser</code> will copy files from <code>SKEL</code> into the home directory and prompt for finger (gecos) information and a password. The gecos may also be set with the <code>&#8211;gecos</code> option. With the <code>&#8211;disabled-login</code> option, the account will be created but will be disabled until a password is set. The <code>&#8211;disabled-password</code> option will not set a password, but login is still possible (for example with SSH RSA keys). To set up an encrypted home directory for the new user, add the <code>&#8211;encrypt-home</code> option. For more information, refer to the -b option of <code><a href="/docs/linux/man/1-ecryptfs-setup-private/">ecryptfs-setup-private</a>(1).</code> </p>
<p> If the file <code>/usr/local/sbin/adduser.local</code> exists, it will be executed after the user account has been set up in order to do any local setup. The arguments passed to <code>adduser.local</code> are:<br />
 username uid gid home-directory<br />
 The environment variable VERBOSE is set according to the following rule:</p>
<dl>
<dt>0 if</p>
<dd><code>&#8211;quiet</code> is specified</p>
<dt>1 if neither</p>
<dd><code>&#8211;quiet </code> nor <code>&#8211;debug </code> is specified</p>
<dt>2 if</p>
<dd><code>&#8211;debug</code> is specified </p>
<p> (The same applies to the variable DEBUG, but DEBUG is deprecated and will be removed in a later version of <code>adduser</code>.) </p>
</dl>
<h3>Add a system user</h3>
<p>If called with one non-option argument and the <code>&#8211;system</code> option, <code>adduser</code> will add a system user. If a user with the same name already exists in the system uid range (or, if the uid is specified, if a user with that uid already exists), adduser will exit with a warning. This warning can be suppressed by adding <code>&#8211;quiet</code>. </p>
<p> <code>adduser</code> will choose the first available UID from the range specified for system users in the configuration file (FIRST_SYSTEM_UID and LAST_SYSTEM_UID). If you want to have a specific UID, you can specify it using the <code>&#8211;uid</code> option. </p>
<p> By default, system users are placed in the <code>nogroup</code> group. To place the new system user in an already existing group, use the <code>&#8211;gid</code> or <code>&#8211;ingroup</code> options. To place the new system user in a new group with the same ID, use the <code>&#8211;group</code> option. </p>
<p> A home directory is created by the same rules as for normal users. The new system user will have the shell <i>/usr/sbin/nologin</i> (unless overridden with the <code>&#8211;shell</code> option), and have logins disabled. Skeletal configuration files are not copied.</p>
<h3>Add a user group</h3>
<p>If <code>adduser</code> is called with the <code>&#8211;group</code> option and without the <code>&#8211;system</code> option, or <code>addgroup</code> is called respectively, a user group will be added. </p>
<p> A GID will be chosen from the range specified for system GIDS in the configuration file (FIRST_GID, LAST_GID). To override that mechanism you can give the GID using the <code>&#8211;gid</code> option. </p>
<p> The group is created with no users.</p>
<h3>Add a system group</h3>
<p>If <code>addgroup</code> is called with the <code>&#8211;system</code> option, a system group will be added. </p>
<p> A GID will be chosen from the range specified for system GIDS in the configuration file (FIRST_SYSTEM_GID, LAST_SYSTEM_GID). To override that mechanism you can give the GID using the <code>&#8211;gid</code> option. </p>
<p> The group is created with no users.</p>
<h3>Add an existing user to an existing group</h3>
<p>If called with two non-option arguments, <code>adduser</code> will add an existing user to an existing group.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;conf FILE</code></p>
<dd>Use FILE instead of <i>/etc/adduser.conf</i>.</p>
<dt><code>&#8211;disabled-login</code></p>
<dd>Do not run passwd to set the password. The user won&#8217;t be able to use her account until the password is set.</p>
<dt><code>&#8211;disabled-password</code></p>
<dd>Like &#8211;disabled-login, but logins are still possible (for example using SSH RSA keys) but not using password authentication.</p>
<dt><code>&#8211;force-badname</code></p>
<dd>By default, user and group names are checked against the configurable regular expression <code>NAME_REGEX</code> (or <code>NAME_REGEX_SYSTEM</code> if <code>&#8211;system</code> is specified) specified in the configuration file. This option forces <code>adduser</code> and <code>addgroup</code> to apply only a weak check for validity of the name. <code>NAME_REGEX</code> is described in <code><a href="/docs/linux/man/5-adduser-conf/">adduser.conf</a></code>(5).</p>
<dt><code>&#8211;gecos GECOS</code></p>
<dd>Set the gecos field for the new entry generated. <code>adduser </code> will not ask for finger information if this option is given.</p>
<dt><code>&#8211;gid ID</code></p>
<dd>When creating a group, this option forces the new groupid to be the given number. When creating a user, this option will put the user in that group.</p>
<dt><code>&#8211;group</code></p>
<dd>When combined with <code>&#8211;system</code>, a group with the same name and ID as the system user is created. If not combined with <code>&#8211;system</code>, a group with the given name is created. This is the default action if the program is invoked as <code>addgroup</code>.</p>
<dt><code>&#8211;help</code></p>
<dd>Display brief instructions.</p>
<dt><code>&#8211;home DIR</code></p>
<dd>Use DIR as the user&#8217;s home directory, rather than the default specified by the configuration file. If the directory does not exist, it is created and skeleton files are copied.</p>
<dt><code>&#8211;shell SHELL</code></p>
<dd>Use SHELL as the user&#8217;s login shell, rather than the default specified by the configuration file.</p>
<dt><code>&#8211;ingroup GROUP</code></p>
<dd>Add the new user to GROUP instead of a usergroup or the default group defined by <code>USERS_GID </code> in the configuration file. This affects the users primary group. To add additional groups, see the <code>add_extra_groups</code> option.</p>
<dt><code>&#8211;no-create-home</code></p>
<dd>Do not create the home directory, even if it doesn&#8217;t exist.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Suppress informational messages, only show warnings and errors.</p>
<dt><code>&#8211;debug</code></p>
<dd>Be verbose, most useful if you want to nail down a problem with adduser.</p>
<dt><code>&#8211;system</code></p>
<dd>Create a system user or group.</p>
<dt><code>&#8211;uid ID</code></p>
<dd>Force the new userid to be the given number. <code>adduser </code> will fail if the userid is already taken.</p>
<dt><code>&#8211;firstuid ID</code></p>
<dd>Override the first uid in the range that the uid is chosen from (overrides <code>FIRST_UID</code> specified in the configuration file).</p>
<dt><code>&#8211;lastuid ID</code></p>
<dd>Override the last uid in the range that the uid is chosen from ( <code>LAST_UID</code> )</p>
<dt><code>&#8211;add_extra_groups</code></p>
<dd>Add new user to extra groups defined in the configuration file.</p>
<dt><code>&#8211;version</code></p>
<dd>Display version and copyright information. </p>
</dl>
<h2>Exit Values</h2>
<dl>
<dt><code>0 </code></p>
<dd>The user exists as specified. This can have 2 causes: The user was created by adduser or the user was already present on the system before adduser was invoked. If adduser was returning 0 , invoking adduser a second time with the same parameters as before also returns 0.</p>
<dt><code>1</code></p>
<dd>Creating the user or group failed because it was already present with other UID/GID than specified. The username or groupname was rejected because of a mismatch with the configured regular expressions, see <a href="/docs/linux/man/5-adduser-conf/">adduser.conf</a>(5). Adduser has been aborted by a signal.<br />
 Or for many other yet undocumented reasons which are printed to console then. You may then consider to remove <code>&#8211;quiet</code> to make adduser more verbose. </p>
</dl>
<h2>Files</h2>
<dl>
<dt>/etc/adduser.conf</p>
<dd>Default configuration file for adduser and addgroup</p>
<dt>/usr/local/sbin/adduser.local</p>
<dd>Optional custom add-ons. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-adduser-conf/">adduser.conf</a></code>(5), <code><a href="/docs/linux/man/8-deluser/">deluser</a></code>(8), <code><a href="/docs/linux/man/8-groupadd/">groupadd</a></code>(8), <code><a href="/docs/linux/man/8-useradd/">useradd</a></code>(8), <code><a href="/docs/linux/man/8-usermod/">usermod</a></code>(8), Debian Policy 9.2.2. </p>
<h2>Copyright</h2>
<p>Copyright (C) 1997, 1998, 1999 Guy Maor. Modifications by Roland Bauerschmidt and Marc Haber. Additional patches by Joerg Hoh and Stephen Gran.<br />
 Copyright (C) 1995 Ted Hajek, with a great deal borrowed from the original Debian <code>adduser</code><br />
 Copyright (C) 1994 Ian Murdock. <code>adduser</code> is free software; see the GNU General Public Licence version 2 or later for copying conditions. There is <i>no</i> warranty.</p>
