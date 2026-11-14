---
title: "userdel(8)"
name: "userdel"
section: "8"
letter: "u"
url: "/docs/linux/man/8-userdel/"
description: "userdel – delete a user account and related files"
---

<p>userdel &#8211; delete a user account and related files</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>userdel</code> [options] <i>LOGIN</i></dl>
<h2>Description</h2>
<p><code>userdel</code></p>
<dd>is a low level utility for removing users. On Debian, administrators should usually use <code><a href="/docs/linux/man/8-deluser/">deluser</a></code>(8) instead. </p>
<p> The <code>userdel</code> command modifies the system account files, deleting all entries that refer to the user name <i>LOGIN</i>. The named user must exist.</p>
<h2>Options</h2>
<p>The options which apply to the <code>userdel</code> command are: </p>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dd>This option forces the removal of the user account, even if the user is still logged in. It also forces <code>userdel</code> to remove the user&#8217;s home directory and mail spool, even if another user uses the same home directory or if the mail spool is not owned by the specified user. If <code>USERGROUPS_ENAB</code> is defined to <i>yes</i> in /etc/login.defs and if a group exists with the same name as the deleted user, then this group will be removed, even if it is still the primary group of another user. </p>
<p> <i>Note:</i> This option is dangerous and may leave your system in an inconsistent state.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-r</code>, <code>&#8211;remove</code></p>
<dl>
<dd>Files in the user&#8217;s home directory will be removed along with the home directory itself and the user&#8217;s mail spool. Files located in other file systems will have to be searched for and deleted manually. </p>
<p> The mail spool is defined by the <code>MAIL_DIR</code> variable in the login.defs file.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-P</code>, <code>&#8211;prefix</code>&nbsp;<i>PREFIX_DIR</i></p>
<dl>
<dd>Apply changes in the <i>PREFIX_DIR</i> directory and use the configuration files from the <i>PREFIX_DIR</i> directory. This option does not chroot and is intended for preparing a cross-compilation target. Some limitations: NIS and LDAP users/groups are not verified. PAM authentication is using the host files. No SELINUX support.</dl>
<p> <code>-Z</code>, <code>&#8211;selinux-user</code></p>
<dl>
<dd>Remove any SELinux user mapping for the user&#8217;s login.</dl>
<h2>Configuration</h2>
<p>The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
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
<p> <code>USERDEL_CMD</code> (string)</p>
<dl>
<dd>If defined, this command is run when removing a user. It should remove any at/cron/print jobs etc. owned by the user to be removed (passed as the first argument). </p>
<p> The return code of the script is not taken into account. </p>
<p> Here is an example script, which removes the user&#8217;s cron, at and print jobs: </p>
<dl>
<dd>
<pre>#! /bin/sh
# Check for the required argument.
if [ $# != 1 ]; then
 echo &quot;Usage: $0 username&quot;
 exit 1
fi
# Remove cron jobs.
crontab -r -u $1
# Remove at jobs.
# Note that it will remove any jobs owned by the same UID,
# even if it was shared by a different username.
AT_SPOOL_DIR=/var/spool/cron/atjobs
find $AT_SPOOL_DIR -name &quot;[^.]*&quot; -type f -user $1 -delete \;
# Remove print jobs.
lprm $1
# All done.
exit 0</pre>
</dl>
</dl>
<p> <code>USERGROUPS_ENAB</code> (boolean)</p>
<dl>
<dd>If set to <i>yes</i>, <code>userdel</code> will remove the user&#8217;s group if it contains no more members, and <code>useradd</code> will create by default a group with the name of the user.</dl>
<h2>Files</h2>
<p>/etc/group</p>
<dl>
<dd>Group account information.</dl>
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
<h2>Exit Values</h2>
<p>The <code>userdel</code> command exits with the following values: </p>
<p> <i>0</i></p>
<dl>
<dd>success</dl>
<p> <i>1</i></p>
<dl>
<dd>can&#8217;t update password file</dl>
<p> <i>2</i></p>
<dl>
<dd>invalid command syntax</dl>
<p> <i>6</i></p>
<dl>
<dd>specified user doesn&#8217;t exist</dl>
<p> <i>8</i></p>
<dl>
<dd>user currently logged in</dl>
<p> <i>10</i></p>
<dl>
<dd>can&#8217;t update group file</dl>
<p> <i>12</i></p>
<dl>
<dd>can&#8217;t remove home directory</dl>
<h2>Caveats</h2>
<p><code>userdel</code> will not allow you to remove an account if there are running processes which belong to this account. In that case, you may have to kill those processes or lock the user&#8217;s password or account and remove the account later. The <code>-f</code> option can force the deletion of this account. </p>
<p> You should manually check all file systems to ensure that no files remain owned by this user. </p>
<p> You may not remove any NIS attributes on a NIS client. This must be performed on the NIS server. </p>
<p> If <code>USERGROUPS_ENAB</code> is defined to <i>yes</i> in /etc/login.defs, <code>userdel</code> will delete the group with the same name as the user. To avoid inconsistencies in the passwd and group databases, <code>userdel</code> will check that this group is not used as a primary group for another user, and will just warn without deleting the group otherwise. The <code>-f</code> option can force the deletion of this group.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chfn/">chfn</a></code>(1), <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/8-gpasswd/">gpasswd</a></code>(8), <code><a href="/docs/linux/man/8-groupadd/">groupadd</a></code>(8), <code><a href="/docs/linux/man/8-groupdel/">groupdel</a></code>(8), <code><a href="/docs/linux/man/8-groupmod/">groupmod</a></code>(8), <code><a href="/docs/linux/man/5-subgid/">subgid</a></code>(5), <code><a href="/docs/linux/man/5-subuid/">subuid</a></code>(5), <code><a href="/docs/linux/man/8-useradd/">useradd</a></code>(8), <code><a href="/docs/linux/man/8-usermod/">usermod</a></code>(8). </p>
