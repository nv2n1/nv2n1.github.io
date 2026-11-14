---
title: "login-defs(5)"
name: "login-defs"
section: "5"
letter: "l"
url: "/docs/linux/man/5-login-defs/"
description: "login.defs – shadow password suite configuration"
---

<p>login.defs &#8211; shadow password suite configuration</p>
<h2>Description</h2>
<p>The /etc/login.defs file defines the site-specific configuration for the shadow password suite. This file is required. Absence of this file will not prevent system operation, but will probably result in undesirable operation. This file is a readable text file, each line of the file describing one configuration parameter. The lines consist of a configuration name and value, separated by whitespace. Blank lines and comment lines are ignored. Comments are introduced with a &quot;#&quot; pound sign and the pound sign must be the first non-white character of the line. Parameter values may be of four types: strings, booleans, numbers, and long numbers. A string is comprised of any printable characters. A boolean should be either the value <i>yes</i> or <i>no</i>. An undefined boolean parameter or one with a value other than these will be given a <i>no</i> value. Numbers (both regular and long) may be either decimal values, octal values (precede the value with <i>0</i>) or hexadecimal values (precede the value with <i>0x</i>). The maximum value of the regular and long numeric parameters is machine-dependent. The following configuration items are provided: <code>CHFN_RESTRICT</code> (string)</p>
<dl>
<dd>This parameter specifies which values in the <i>gecos</i> field of the /etc/passwd file may be changed by regular users using the <code>chfn</code> program. It can be any combination of letters <i>f</i>, <i>r</i>, <i>w</i>, <i>h</i>, for Full name, Room number, Work phone, and Home phone, respectively. For backward compatibility, <i>yes</i> is equivalent to <i>rwh</i> and <i>no</i> is equivalent to <i>frwh</i>. If not specified, only the superuser can make any changes. The most restrictive setting is better achieved by not installing <code>chfn</code> SUID.</dl>
<p> <code>CONSOLE_GROUPS</code> (string)</p>
<dl>
<dd>List of groups to add to the user&#8217;s supplementary groups set when logging in on the console (as determined by the CONSOLE setting). Default is none. Use with caution &#8211; it is possible for users to gain permanent access to these groups, even when not logged in on the console.</dl>
<p> <code>CREATE_HOME</code> (boolean)</p>
<dl>
<dd>Indicate if a home directory should be created by default for new users. This setting does not apply to system users, and can be overridden on the command line.</dl>
<p> <code>DEFAULT_HOME</code> (boolean)</p>
<dl>
<dd>Indicate if login is allowed if we can&#8217;t cd to the home directory. Default is no. If set to <i>yes</i>, the user will login in the root (/) directory if it is not possible to cd to her home directory.</dl>
<p> <code>ENCRYPT_METHOD</code> (string)</p>
<dl>
<dd>This defines the system default encryption algorithm for encrypting passwords (if no algorithm are specified on the command line). It can take one of these values: <i>DES</i> (default), <i>MD5</i>, <i>SHA256</i>, <i>SHA512</i>. Note: this parameter overrides the <code>MD5_CRYPT_ENAB</code> variable. Note: This only affect the generation of group passwords. The generation of user passwords is done by PAM and subject to the PAM configuration. It is recommended to set this variable consistently with the PAM configuration.</dl>
<p> <code>ENV_HZ</code> (string)</p>
<dl>
<dd>If set, it will be used to define the HZ environment variable when a user login. The value must be preceded by <i>HZ=</i>. A common value on Linux is <i>HZ=100</i>. The <code>HZ</code> environment variable is only set when the user (the superuser) logs in with <code>sulogin</code>.</dl>
<p> <code>ENV_PATH</code> (string)</p>
<dl>
<dd>If set, it will be used to define the PATH environment variable when a regular user login. The value is a colon separated list of paths (for example <i>/bin:/usr/bin</i>) and can be preceded by <i>PATH=</i>. The default value is <i>PATH=/bin:/usr/bin</i>.</dl>
<p> <code>ENV_SUPATH</code> (string)</p>
<dl>
<dd>If set, it will be used to define the PATH environment variable when the superuser login. The value is a colon separated list of paths (for example <i>/sbin:/bin:/usr/sbin:/usr/bin</i>) and can be preceded by <i>PATH=</i>. The default value is <i>PATH=/sbin:/bin:/usr/sbin:/usr/bin</i>.</dl>
<p> <code>ERASECHAR</code> (number)</p>
<dl>
<dd>Terminal ERASE character (<i>010</i> = backspace, <i>0177</i> = DEL). The value can be prefixed &quot;0&quot; for an octal value, or &quot;0x&quot; for an hexadecimal value.</dl>
<p> <code>FAIL_DELAY</code> (number)</p>
<dl>
<dd>Delay in seconds before being allowed another attempt after a login failure.</dl>
<p> <code>FAKE_SHELL</code> (string)</p>
<dl>
<dd>If set, <code>login</code> will execute this shell instead of the users&#8217; shell specified in /etc/passwd.</dl>
<p> <code>GID_MAX</code> (number), <code>GID_MIN</code> (number)</p>
<dl>
<dd>Range of group IDs used for the creation of regular groups by <code>useradd</code>, <code>groupadd</code>, or <code>newusers</code>. The default value for <code>GID_MIN</code> (resp. <code>GID_MAX</code>) is 1000 (resp. 60000).</dl>
<p> <code>HOME_MODE</code> (number)</p>
<dl>
<dd>The mode for new home directories. If not specified, the <code>UMASK</code> is used to create the mode. <code>useradd</code> and <code>newusers</code> use this to set the mode of the home directory they create.</dl>
<p> <code>HUSHLOGIN_FILE</code> (string)</p>
<dl>
<dd>If defined, this file can inhibit all the usual chatter during the login sequence. If a full pathname is specified, then hushed mode will be enabled if the user&#8217;s name or shell are found in the file. If not a full pathname, then hushed mode will be enabled if the file exists in the user&#8217;s home directory.</dl>
<p> <code>KILLCHAR</code> (number)</p>
<dl>
<dd>Terminal KILL character (<i>025</i> = CTRL/U). The value can be prefixed &quot;0&quot; for an octal value, or &quot;0x&quot; for an hexadecimal value.</dl>
<p> <code>LASTLOG_UID_MAX</code> (number)</p>
<dl>
<dd>Highest user ID number for which the lastlog entries should be updated. As higher user IDs are usually tracked by remote user identity and authentication services there is no need to create a huge sparse lastlog file for them. No <code>LASTLOG_UID_MAX</code> option present in the configuration means that there is no user ID limit for writing lastlog entries.</dl>
<p> <code>LOG_OK_LOGINS</code> (boolean)</p>
<dl>
<dd>Enable logging of successful logins.</dl>
<p> <code>LOG_UNKFAIL_ENAB</code> (boolean)</p>
<dl>
<dd>Enable display of unknown usernames when login failures are recorded. Note: logging unknown usernames may be a security issue if an user enter her password instead of her login name.</dl>
<p> <code>LOGIN_RETRIES</code> (number)</p>
<dl>
<dd>Maximum number of login retries in case of bad password. This will most likely be overridden by PAM, since the default pam_unix module has its own built in of 3 retries. However, this is a safe fallback in case you are using an authentication module that does not enforce PAM_MAXTRIES.</dl>
<p> <code>LOGIN_TIMEOUT</code> (number)</p>
<dl>
<dd>Max time in seconds for login.</dl>
<p> <code>MAIL_DIR</code> (string)</p>
<dl>
<dd>The mail spool directory. This is needed to manipulate the mailbox when its corresponding user account is modified or deleted. If not specified, a compile-time default is used.</dl>
<p> <code>MAIL_FILE</code> (string)</p>
<dl>
<dd>Defines the location of the users mail spool files relatively to their home directory.</dl>
<p> The <code>MAIL_DIR</code> and <code>MAIL_FILE</code> variables are used by <code>useradd</code>, <code>usermod</code>, and <code>userdel</code> to create, move, or delete the user&#8217;s mail spool. <code>MAX_MEMBERS_PER_GROUP</code> (number)</p>
<dl>
<dd>Maximum members per group entry. When the maximum is reached, a new group entry (line) is started in /etc/group (with the same name, same password, and same GID). The default value is 0, meaning that there are no limits in the number of members in a group. This feature (split group) permits to limit the length of lines in the group file. This is useful to make sure that lines for NIS groups are not larger than 1024 characters. If you need to enforce such limit, you can use 25. Note: split groups may not be supported by all tools (even in the Shadow toolsuite). You should not use this variable unless you really need it.</dl>
<p> <code>MD5_CRYPT_ENAB</code> (boolean)</p>
<dl>
<dd>Indicate if passwords must be encrypted using the MD5-based algorithm. If set to <i>yes</i>, new passwords will be encrypted using the MD5-based algorithm compatible with the one used by recent releases of FreeBSD. It supports passwords of unlimited length and longer salt strings. Set to <i>no</i> if you need to copy encrypted passwords to other systems which don&#8217;t understand the new algorithm. Default is <i>no</i>. This variable is superseded by the <code>ENCRYPT_METHOD</code> variable or by any command line option used to configure the encryption algorithm. This variable is deprecated. You should use <code>ENCRYPT_METHOD</code>. Note: This only affect the generation of group passwords. The generation of user passwords is done by PAM and subject to the PAM configuration. It is recommended to set this variable consistently with the PAM configuration.</dl>
<p> <code>PASS_MAX_DAYS</code> (number)</p>
<dl>
<dd>The maximum number of days a password may be used. If the password is older than this, a password change will be forced. If not specified, -1 will be assumed (which disables the restriction).</dl>
<p> <code>PASS_MIN_DAYS</code> (number)</p>
<dl>
<dd>The minimum number of days allowed between password changes. Any password changes attempted sooner than this will be rejected. If not specified, -1 will be assumed (which disables the restriction).</dl>
<p> <code>PASS_WARN_AGE</code> (number)</p>
<dl>
<dd>The number of days warning given before a password expires. A zero means warning is given only upon the day of expiration, a negative value means no warning is given. If not specified, no warning will be provided.</dl>
<p> <code>PASS_MAX_DAYS</code>, <code>PASS_MIN_DAYS</code> and <code>PASS_WARN_AGE</code> are only used at the time of account creation. Any changes to these settings won&#8217;t affect existing accounts. <code>SHA_CRYPT_MIN_ROUNDS</code> (number), <code>SHA_CRYPT_MAX_ROUNDS</code> (number)</p>
<dl>
<dd>When <code>ENCRYPT_METHOD</code> is set to <i>SHA256</i> or <i>SHA512</i>, this defines the number of SHA rounds used by the encryption algorithm by default (when the number of rounds is not specified on the command line). With a lot of rounds, it is more difficult to brute forcing the password. But note also that more CPU resources will be needed to authenticate users. If not specified, the libc will choose the default number of rounds (5000). The values must be inside the 1000-999,999,999 range. If only one of the <code>SHA_CRYPT_MIN_ROUNDS</code> or <code>SHA_CRYPT_MAX_ROUNDS</code> values is set, then this value will be used. If <code>SHA_CRYPT_MIN_ROUNDS</code> &gt; <code>SHA_CRYPT_MAX_ROUNDS</code>, the highest value will be used. Note: This only affect the generation of group passwords. The generation of user passwords is done by PAM and subject to the PAM configuration. It is recommended to set this variable consistently with the PAM configuration.</dl>
<p> <code>SULOG_FILE</code> (string)</p>
<dl>
<dd>If defined, all su activity is logged to this file.</dl>
<p> <code>SU_NAME</code> (string)</p>
<dl>
<dd>If defined, the command name to display when running &quot;su -&quot;. For example, if this is defined as &quot;su&quot; then a &quot;ps&quot; will display the command is &quot;-su&quot;. If not defined, then &quot;ps&quot; would display the name of the shell actually being run, e.g. something like &quot;-sh&quot;.</dl>
<p> <code>SUB_GID_MIN</code> (number), <code>SUB_GID_MAX</code> (number), <code>SUB_GID_COUNT</code> (number)</p>
<dl>
<dd>If /etc/subuid exists, the commands <code>useradd</code> and <code>newusers</code> (unless the user already have subordinate group IDs) allocate <code>SUB_GID_COUNT</code> unused group IDs from the range <code>SUB_GID_MIN</code> to <code>SUB_GID_MAX</code> for each new user. The default values for <code>SUB_GID_MIN</code>, <code>SUB_GID_MAX</code>, <code>SUB_GID_COUNT</code> are respectively 100000, 600100000 and 65536.</dl>
<p> <code>SUB_UID_MIN</code> (number), <code>SUB_UID_MAX</code> (number), <code>SUB_UID_COUNT</code> (number)</p>
<dl>
<dd>If /etc/subuid exists, the commands <code>useradd</code> and <code>newusers</code> (unless the user already have subordinate user IDs) allocate <code>SUB_UID_COUNT</code> unused user IDs from the range <code>SUB_UID_MIN</code> to <code>SUB_UID_MAX</code> for each new user. The default values for <code>SUB_UID_MIN</code>, <code>SUB_UID_MAX</code>, <code>SUB_UID_COUNT</code> are respectively 100000, 600100000 and 65536.</dl>
<p> <code>SYS_GID_MAX</code> (number), <code>SYS_GID_MIN</code> (number)</p>
<dl>
<dd>Range of group IDs used for the creation of system groups by <code>useradd</code>, <code>groupadd</code>, or <code>newusers</code>. The default value for <code>SYS_GID_MIN</code> (resp. <code>SYS_GID_MAX</code>) is 101 (resp. <code>GID_MIN</code>-1).</dl>
<p> <code>SYS_UID_MAX</code> (number), <code>SYS_UID_MIN</code> (number)</p>
<dl>
<dd>Range of user IDs used for the creation of system users by <code>useradd</code> or <code>newusers</code>. The default value for <code>SYS_UID_MIN</code> (resp. <code>SYS_UID_MAX</code>) is 101 (resp. <code>UID_MIN</code>-1).</dl>
<p> <code>SYSLOG_SG_ENAB</code> (boolean)</p>
<dl>
<dd>Enable &quot;syslog&quot; logging of <code>sg</code> activity.</dl>
<p> <code>SYSLOG_SU_ENAB</code> (boolean)</p>
<dl>
<dd>Enable &quot;syslog&quot; logging of <code>su</code> activity &#8211; in addition to sulog file logging.</dl>
<p> <code>TTYGROUP</code> (string), <code>TTYPERM</code> (string)</p>
<dl>
<dd>The terminal permissions: the login tty will be owned by the <code>TTYGROUP</code> group, and the permissions will be set to <code>TTYPERM</code>. By default, the ownership of the terminal is set to the user&#8217;s primary group and the permissions are set to <i>0600</i>. <code>TTYGROUP</code> can be either the name of a group or a numeric group identifier. If you have a <code>write</code> program which is &quot;setgid&quot; to a special group which owns the terminals, define TTYGROUP to the group number and TTYPERM to 0620. Otherwise leave TTYGROUP commented out and assign TTYPERM to either 622 or 600.</dl>
<p> <code>TTYTYPE_FILE</code> (string)</p>
<dl>
<dd>If defined, file which maps tty line to TERM environment parameter. Each line of the file is in a format something like &quot;vt100 tty01&quot;.</dl>
<p> <code>UID_MAX</code> (number), <code>UID_MIN</code> (number)</p>
<dl>
<dd>Range of user IDs used for the creation of regular users by <code>useradd</code> or <code>newusers</code>. The default value for <code>UID_MIN</code> (resp. <code>UID_MAX</code>) is 1000 (resp. 60000).</dl>
<p> <code>UMASK</code> (number)</p>
<dl>
<dd>The file mode creation mask is initialized to this value. If not specified, the mask will be initialized to 022. <code>useradd</code> and <code>newusers</code> use this mask to set the mode of the home directory they create if <code>HOME_MODE</code> is not set. It is also used by <code>pam_umask</code> as the default umask value.</dl>
<p> <code>USERDEL_CMD</code> (string)</p>
<dl>
<dd>If defined, this command is run when removing a user. It should remove any at/cron/print jobs etc. owned by the user to be removed (passed as the first argument). The return code of the script is not taken into account. Here is an example script, which removes the user&#8217;s cron, at and print jobs:</p>
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
<p>  <code>USERGROUPS_ENAB</code> (boolean)</p>
<dl>
<dd>If set to <i>yes</i>, <code>userdel</code> will remove the user&#8217;s group if it contains no more members, and <code>useradd</code> will create by default a group with the name of the user.</dl>
<h2>Cross References</h2>
<p>The following cross references show which programs in the shadow password suite use which parameters. </p>
<p> chfn</p>
<dl>
<dd>CHFN_RESTRICT</dl>
<p> chgpasswd</p>
<dl>
<dd>ENCRYPT_METHOD MAX_MEMBERS_PER_GROUP MD5_CRYPT_ENAB SHA_CRYPT_MAX_ROUNDS SHA_CRYPT_MIN_ROUNDS</dl>
<p> chpasswd</p>
<dl>
<dd>SHA_CRYPT_MAX_ROUNDS SHA_CRYPT_MIN_ROUNDS</dl>
<p> gpasswd</p>
<dl>
<dd>ENCRYPT_METHOD MAX_MEMBERS_PER_GROUP MD5_CRYPT_ENAB SHA_CRYPT_MAX_ROUNDS SHA_CRYPT_MIN_ROUNDS</dl>
<p> groupadd</p>
<dl>
<dd>GID_MAX GID_MIN MAX_MEMBERS_PER_GROUP SYS_GID_MAX SYS_GID_MIN</dl>
<p> groupdel</p>
<dl>
<dd>MAX_MEMBERS_PER_GROUP</dl>
<p> groupmems</p>
<dl>
<dd>MAX_MEMBERS_PER_GROUP</dl>
<p> groupmod</p>
<dl>
<dd>MAX_MEMBERS_PER_GROUP</dl>
<p> grpck</p>
<dl>
<dd>MAX_MEMBERS_PER_GROUP</dl>
<p> grpconv</p>
<dl>
<dd>MAX_MEMBERS_PER_GROUP</dl>
<p> grpunconv</p>
<dl>
<dd>MAX_MEMBERS_PER_GROUP</dl>
<p> lastlog</p>
<dl>
<dd>LASTLOG_UID_MAX</dl>
<p> login</p>
<dl>
<dd>CONSOLE_GROUPS DEFAULT_HOME ERASECHAR FAIL_DELAY FAKE_SHELL HUSHLOGIN_FILE KILLCHAR LOGIN_RETRIES LOGIN_TIMEOUT LOG_OK_LOGINS LOG_UNKFAIL_ENAB TTYGROUP TTYPERM TTYTYPE_FILE USERGROUPS_ENAB</dl>
<p> newgrp / sg</p>
<dl>
<dd>SYSLOG_SG_ENAB</dl>
<p> newusers</p>
<dl>
<dd>ENCRYPT_METHOD GID_MAX GID_MIN MAX_MEMBERS_PER_GROUP MD5_CRYPT_ENAB HOME_MODE PASS_MAX_DAYS PASS_MIN_DAYS PASS_WARN_AGE SHA_CRYPT_MAX_ROUNDS SHA_CRYPT_MIN_ROUNDS SUB_GID_COUNT SUB_GID_MAX SUB_GID_MIN SUB_UID_COUNT SUB_UID_MAX SUB_UID_MIN SYS_GID_MAX SYS_GID_MIN SYS_UID_MAX SYS_UID_MIN UID_MAX UID_MIN UMASK</dl>
<p> pwck</p>
<dl>
<dd>PASS_MAX_DAYS PASS_MIN_DAYS PASS_WARN_AGE</dl>
<p> pwconv</p>
<dl>
<dd>PASS_MAX_DAYS PASS_MIN_DAYS PASS_WARN_AGE</dl>
<p> su</p>
<dl>
<dd>CONSOLE_GROUPS DEFAULT_HOME ENV_PATH ENV_SUPATH SULOG_FILE SU_NAME SYSLOG_SU_ENAB</dl>
<p> sulogin</p>
<dl>
<dd>ENV_HZ</dl>
<p> useradd</p>
<dl>
<dd>CREATE_HOME GID_MAX GID_MIN HOME_MODE LASTLOG_UID_MAX MAIL_DIR MAX_MEMBERS_PER_GROUP PASS_MAX_DAYS PASS_MIN_DAYS PASS_WARN_AGE SUB_GID_COUNT SUB_GID_MAX SUB_GID_MIN SUB_UID_COUNT SUB_UID_MAX SUB_UID_MIN SYS_GID_MAX SYS_GID_MIN SYS_UID_MAX SYS_UID_MIN UID_MAX UID_MIN UMASK</dl>
<p> userdel</p>
<dl>
<dd>MAIL_DIR MAIL_FILE MAX_MEMBERS_PER_GROUP USERDEL_CMD USERGROUPS_ENAB</dl>
<p> usermod</p>
<dl>
<dd>LASTLOG_UID_MAX MAIL_DIR MAIL_FILE MAX_MEMBERS_PER_GROUP</dl>
<h2>Bugs</h2>
<p>Much of the functionality that used to be provided by the shadow password suite is now handled by PAM. Thus, /etc/login.defs is no longer used by <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), or less used by <code><a href="/docs/linux/man/1-login/">login</a></code>(1), and <code><a href="/docs/linux/man/1-su/">su</a></code>(1). Please refer to the corresponding PAM configuration files instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/1-su/">su</a></code>(1), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8). </p>
