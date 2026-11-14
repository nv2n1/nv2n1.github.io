---
title: "login(1)"
name: "login"
section: "1"
letter: "l"
url: "/docs/linux/man/1-login/"
description: "login – begin session on the system"
---

<h2 class="name">NAME</h2>
<p> login &#8211; begin session on the system </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>login</code> [-p] [-h&nbsp;<i>host</i>] [<i>username</i>] [<i>ENV=VAR</i>&#8230;]</p>
<dt> <code>login</code> [-p] [-h&nbsp;<i>host</i>] -f <i>username</i></p>
<dt> <code>login</code> [-p] -r&nbsp;<i>host</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>login</code> program is used to establish a new session with the system. It is normally invoked automatically by responding to the <i>login:</i> prompt on the user&#8217;s terminal. <code>login</code> may be special to the shell and may not be invoked as a sub-process. When called from a shell, <code>login</code> should be executed as <code>exec login</code> which will cause the user to exit from the current shell (and thus will prevent the new logged in user to return to the session of the caller). Attempting to execute <code>login</code> from any shell but the login shell will produce an error message. </p>
<p> The user is then prompted for a password, where appropriate. Echoing is disabled to prevent revealing the password. Only a small number of password failures are permitted before <code>login</code> exits and the communications link is severed. </p>
<p> If password aging has been enabled for your account, you may be prompted for a new password before proceeding. You will be forced to provide your old password and the new password before continuing. Please refer to <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1) for more information. </p>
<p> Your user and group ID will be set according to their values in the /etc/passwd file. The value for <code>$HOME</code>, <code>$SHELL</code>, <code>$PATH</code>, <code>$LOGNAME</code>, and <code>$MAIL</code> are set according to the appropriate fields in the password entry. Ulimit, umask and nice values may also be set according to entries in the GECOS field. </p>
<p> On some installations, the environmental variable <code>$TERM</code> will be initialized to the terminal type on your tty line, as specified in /etc/ttytype. </p>
<p> An initialization script for your command interpreter may also be executed. Please see the appropriate manual section for more information on this function. </p>
<p> A subsystem login is indicated by the presence of a &quot;*&quot; as the first character of the login shell. The given home directory will be used as the root of a new file system which the user is actually logged into. </p>
<p> The <code>login</code> program is NOT responsible for removing users from the utmp file. It is the responsibility of <code><a href="/docs/linux/man/8-getty/">getty</a></code>(8) and <code><a href="/docs/linux/man/8-init/">init</a></code>(8) to clean up apparent ownership of a terminal session. If you use <code>login</code> from the shell prompt without <code>exec</code>, the user you use will continue to appear to be logged in even after you log out of the &quot;subsession&quot;.</p>
<h2>OPTIONS</h2>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> Do not perform authentication, user is preauthenticated. </p>
<p> Note: In that case, <i>username</i> is mandatory.</dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Name of the remote host for this login.</dl>
<p> <code>-p</code></p>
<dl>
<dt>
<dd> Preserve environment.</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> Perform autologin protocol for rlogin.</dl>
<p> The <code>-r</code>, <code>-h</code> and <code>-f</code> options are only used when <code>login</code> is invoked by root.</p>
<h2>CAVEATS</h2>
<p> This version of <code>login</code> has many compilation options, only some of which may be in use at any particular site. </p>
<p> The location of files is subject to differences in system configuration. </p>
<p> The <code>login</code> program is NOT responsible for removing users from the utmp file. It is the responsibility of <code><a href="/docs/linux/man/8-getty/">getty</a></code>(8) and <code><a href="/docs/linux/man/8-init/">init</a></code>(8) to clean up apparent ownership of a terminal session. If you use <code>login</code> from the shell prompt without <code>exec</code>, the user you use will continue to appear to be logged in even after you log out of the &quot;subsession&quot;. </p>
<p> As with any program, <code>login</code>&#8216;s appearance can be faked. If non-trusted users have physical access to a machine, an attacker could use this to obtain the password of the next person coming to sit in front of the machine. Under Linux, the SAK mechanism can be used by users to initiate a trusted path and prevent this kind of attack.</p>
<h2>CONFIGURATION</h2>
<p> The following configuration variables in /etc/login.defs change the behavior of this tool: </p>
<p> <code>CONSOLE_GROUPS</code> (string)</p>
<dl>
<dt>
<dd> List of groups to add to the user&#8217;s supplementary groups set when logging in on the console (as determined by the CONSOLE setting). Default is none. </p>
<p> Use with caution &#8211; it is possible for users to gain permanent access to these groups, even when not logged in on the console.</dl>
<p> <code>DEFAULT_HOME</code> (boolean)</p>
<dl>
<dt>
<dd> Indicate if login is allowed if we can&#8217;t cd to the home directory. Default is no. </p>
<p> If set to <i>yes</i>, the user will login in the root (/) directory if it is not possible to cd to her home directory.</dl>
<p> <code>ENV_PATH</code> (string)</p>
<dl>
<dt>
<dd> If set, it will be used to define the PATH environment variable when a regular user login. The value is a colon separated list of paths (for example <i>/bin:/usr/bin</i>) and can be preceded by <i>PATH=</i>. The default value is <i>PATH=/bin:/usr/bin</i>.</dl>
<p> <code>ENV_SUPATH</code> (string)</p>
<dl>
<dt>
<dd> If set, it will be used to define the PATH environment variable when the superuser login. The value is a colon separated list of paths (for example <i>/sbin:/bin:/usr/sbin:/usr/bin</i>) and can be preceded by <i>PATH=</i>. The default value is <i>PATH=/sbin:/bin:/usr/sbin:/usr/bin</i>.</dl>
<p> <code>ERASECHAR</code> (number)</p>
<dl>
<dt>
<dd> Terminal ERASE character (<i>010</i> = backspace, <i>0177</i> = DEL). </p>
<p> The value can be prefixed &quot;0&quot; for an octal value, or &quot;0x&quot; for an hexadecimal value.</dl>
<p> <code>FAIL_DELAY</code> (number)</p>
<dl>
<dt>
<dd> Delay in seconds before being allowed another attempt after a login failure.</dl>
<p> <code>FAKE_SHELL</code> (string)</p>
<dl>
<dt>
<dd> If set, <code>login</code> will execute this shell instead of the users&#8217; shell specified in /etc/passwd.</dl>
<p> <code>HUSHLOGIN_FILE</code> (string)</p>
<dl>
<dt>
<dd> If defined, this file can inhibit all the usual chatter during the login sequence. If a full pathname is specified, then hushed mode will be enabled if the user&#8217;s name or shell are found in the file. If not a full pathname, then hushed mode will be enabled if the file exists in the user&#8217;s home directory.</dl>
<p> <code>KILLCHAR</code> (number)</p>
<dl>
<dt>
<dd> Terminal KILL character (<i>025</i> = CTRL/U). </p>
<p> The value can be prefixed &quot;0&quot; for an octal value, or &quot;0x&quot; for an hexadecimal value.</dl>
<p> <code>LOGIN_RETRIES</code> (number)</p>
<dl>
<dt>
<dd> Maximum number of login retries in case of bad password. </p>
<p> This will most likely be overridden by PAM, since the default pam_unix module has its own built in of 3 retries. However, this is a safe fallback in case you are using an authentication module that does not enforce PAM_MAXTRIES.</dl>
<p> <code>LOGIN_TIMEOUT</code> (number)</p>
<dl>
<dt>
<dd> Max time in seconds for login.</dl>
<p> <code>LOG_OK_LOGINS</code> (boolean)</p>
<dl>
<dt>
<dd> Enable logging of successful logins.</dl>
<p> <code>LOG_UNKFAIL_ENAB</code> (boolean)</p>
<dl>
<dt>
<dd> Enable display of unknown usernames when login failures are recorded. </p>
<p> Note: logging unknown usernames may be a security issue if an user enter her password instead of her login name.</dl>
<p> <code>TTYGROUP</code> (string), <code>TTYPERM</code> (string)</p>
<dl>
<dt>
<dd> The terminal permissions: the login tty will be owned by the <code>TTYGROUP</code> group, and the permissions will be set to <code>TTYPERM</code>. </p>
<p> By default, the ownership of the terminal is set to the user&#8217;s primary group and the permissions are set to <i>0600</i>. </p>
<p> <code>TTYGROUP</code> can be either the name of a group or a numeric group identifier. </p>
<p> If you have a <code>write</code> program which is &quot;setgid&quot; to a special group which owns the terminals, define TTYGROUP to the group number and TTYPERM to 0620. Otherwise leave TTYGROUP commented out and assign TTYPERM to either 622 or 600.</dl>
<p> <code>TTYTYPE_FILE</code> (string)</p>
<dl>
<dt>
<dd> If defined, file which maps tty line to TERM environment parameter. Each line of the file is in a format something like &quot;vt100 tty01&quot;.</dl>
<p> <code>USERGROUPS_ENAB</code> (boolean)</p>
<dl>
<dt>
<dd> If set to <i>yes</i>, <code>userdel</code> will remove the user&#8217;s group if it contains no more members, and <code>useradd</code> will create by default a group with the name of the user.</dl>
<h2>FILES</h2>
<p> /var/run/utmp</p>
<dl>
<dt>
<dd> List of current login sessions.</dl>
<p> /var/log/wtmp</p>
<dl>
<dt>
<dd> List of previous login sessions.</dl>
<p> /etc/passwd</p>
<dl>
<dt>
<dd> User account information.</dl>
<p> /etc/shadow</p>
<dl>
<dt>
<dd> Secure user account information.</dl>
<p> /etc/motd</p>
<dl>
<dt>
<dd> System message of the day file.</dl>
<p> /etc/nologin</p>
<dl>
<dt>
<dd> Prevent non-root users from logging in.</dl>
<p> /etc/ttytype</p>
<dl>
<dt>
<dd> List of terminal types.</dl>
<p> $HOME/.hushlogin</p>
<dl>
<dt>
<dd> Suppress printing of system messages.</dl>
<p> /etc/login.defs</p>
<dl>
<dt>
<dd> Shadow password suite configuration.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-su/">su</a></code>(1), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/5-nologin/">nologin</a></code>(5), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/5-securetty/">securetty</a></code>(5), <code><a href="/docs/linux/man/8-getty/">getty</a></code>(8). </p>
<h2>Index</h2>
