---
title: "runuser(1)"
name: "runuser"
section: "1"
letter: "r"
url: "/docs/linux/man/1-runuser/"
description: "runuser – run a command with substitute user and group ID"
---

<h2 class="name">NAME</h2>
<p> runuser &#8211; run a command with substitute user and group ID </p>
<h2>SYNOPSIS</h2>
<p> <code>runuser</code> [options] <code>-u</code> <i>user</i> [[&#8211;] <i>command</i> [<i>argument</i>&#8230;]] </p>
<p> <code>runuser</code> [options] [<code>&#8211;</code>] [<i>user</i> [<i>argument</i>&#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> <code>runuser</code> can be used to run commands with a substitute user and group ID. If the option <code>-u</code> is not given, <code>runuser</code> falls back to <code>su</code>-compatible semantics and a shell is executed. The difference between the commands <code>runuser</code> and <code>su</code> is that <code>runuser</code> does not ask for a password (because it may be executed by the root user only) and it uses a different PAM configuration. The command <code>runuser</code> does not have to be installed with set-user-ID permissions. </p>
<p> If the PAM session is not required, then the recommended solution is to use the <code><a href="/docs/linux/man/1-setpriv/">setpriv</a></code>(1) command. </p>
<p> When called without arguments, <code>runuser</code> defaults to running an interactive shell as <i>root</i>. </p>
<p> For backward compatibility, <code>runuser</code> defaults to not changing the current directory and to setting only the environment variables <code>HOME</code> and <code>SHELL</code> (plus <code>USER</code> and <code>LOGNAME</code> if the target <i>user</i> is not root). This version of <code>runuser</code> uses PAM for session management. </p>
<p> Note that <code>runuser</code> in all cases use PAM (pam_getenvlist()) to do the final environment modification. Command-line options such as <code>&#8211;login</code> and <code>&#8211;preserve-environment</code> affect the environment before it is modified by PAM.</p>
<h2>OPTIONS</h2>
<p> <code>-c</code>, <code>&#8211;command</code>=<i>command</i></p>
<dl>
<dt>
<dd> Pass <i>command</i> to the shell with the <code>-c</code> option.</dl>
<p> <code>-f</code>, <code>&#8211;fast</code></p>
<dl>
<dt>
<dd> Pass <code>-f</code> to the shell, which may or may not be useful, depending on the shell.</dl>
<p> <code>-g</code>, <code>&#8211;group</code>=<i>group</i></p>
<dl>
<dt>
<dd> The primary group to be used. This option is allowed for the root user only.</dl>
<p> <code>-G</code>, <code>&#8211;supp-group</code>=<i>group</i></p>
<dl>
<dt>
<dd> Specify a supplementary group. This option is available to the root user only. The first specified supplementary group is also used as a primary group if the option <code>&#8211;group</code> is not specified.</dl>
<p> <code>&#8211;</code>, <code>-l</code>, <code>&#8211;login</code></p>
<dl>
<dt>
<dd> Start the shell as a login shell with an environment similar to a real login: </p>
<dl>
<dt>
<dd> &bull; clears all the environment variables except for <code>TERM</code> and variables specified by <code>&#8211;whitelist-environment</code></dl>
<dl>
<dt>
<dd> &bull; initializes the environment variables <code>HOME</code>, <code>SHELL</code>, <code>USER</code>, <code>LOGNAME</code>, and <code>PATH</code></dl>
<dl>
<dt>
<dd> &bull; changes to the target user&#8217;s home directory</dl>
<dl>
<dt>
<dd> &bull; sets argv[0] of the shell to &#8216;<code>&#8211;</code>&#8216; in order to make the shell a login shell</dl>
</dl>
<p> <code>-P</code>, <code>&#8211;pty</code></p>
<dl>
<dt>
<dd> Create a pseudo-terminal for the session. The independent terminal provides better security as the user does not share a terminal with the original session. This can be used to avoid TIOCSTI ioctl terminal injection and other security attacks against terminal file descriptors. The entire session can also be moved to the background (e.g., <code>runuser &#8211;pty -u username &#8212; command &amp;</code>). If the pseudo-terminal is enabled, then <code>runuser</code> works as a proxy between the sessions (copy stdin and stdout). </p>
<p> This feature is mostly designed for interactive sessions. If the standard input is not a terminal, but for example a pipe (e.g., <code>echo &quot;date&quot; | runuser &#8211;pty -u user</code>), then the ECHO flag for the pseudo-terminal is disabled to avoid messy output.</dl>
<p> <code>-m</code>, <code>-p</code>, <code>&#8211;preserve-environment</code></p>
<dl>
<dt>
<dd> Preserve the entire environment, i.e., do not set <code>HOME</code>, <code>SHELL</code>, <code>USER</code> or <code>LOGNAME</code>. The option is ignored if the option <code>&#8211;login</code> is specified.</dl>
<p> <code>-s</code>, <code>&#8211;shell</code>=<i>shell</i></p>
<dl>
<dt>
<dd> Run the specified <i>shell</i> instead of the default. The shell to run is selected according to the following rules, in order: </p>
<dl>
<dt>
<dd> &bull; the shell specified with <code>&#8211;shell</code></dl>
<dl>
<dt>
<dd> &bull; the shell specified in the environment variable <code>SHELL</code> if the <code>&#8211;preserve-environment</code> option is used</dl>
<dl>
<dt>
<dd> &bull; the shell listed in the passwd entry of the target user</dl>
<dl>
<dt>
<dd> &bull; /bin/sh </p>
<p> If the target user has a restricted shell (i.e., not listed in <i>/etc/shells</i>), then the <code>&#8211;shell</code> option and the <code>SHELL</code> environment variables are ignored unless the calling user is root.</dl>
</dl>
<p> <code>&#8211;session-command=</code><i>command</i></p>
<dl>
<dt>
<dd> Same as <code>-c</code>, but do not create a new session. (Discouraged.)</dl>
<p> <code>-w</code>, <code>&#8211;whitelist-environment</code>=<i>list</i></p>
<dl>
<dt>
<dd> Don&#8217;t reset the environment variables specified in the comma-separated <i>list</i> when clearing the environment for <code>&#8211;login</code>. The whitelist is ignored for the environment variables <code>HOME</code>, <code>SHELL</code>, <code>USER</code>, <code>LOGNAME</code>, and <code>PATH</code>.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>CONFIG FILES</h2>
<p> <code>runuser</code> reads the <i>/etc/default/runuser</i> and <i>/etc/login.defs</i> configuration files. The following configuration items are relevant for <code>runuser</code>: </p>
<p> <code>ENV_PATH</code> (string)</p>
<dl>
<dt>
<dd> Defines the PATH environment variable for a regular user. The default value is <i>/usr/local/bin:/bin:/usr/bin</i>.</dl>
<p> <code>ENV_ROOTPATH</code> (string), <code>ENV_SUPATH</code> (string)</p>
<dl>
<dt>
<dd> Defines the <code>PATH</code> environment variable for root. <code>ENV_SUPATH</code> takes precedence. The default value is <i>/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin</i>.</dl>
<p> <code>ALWAYS_SET_PATH</code> (boolean)</p>
<dl>
<dt>
<dd> If set to <i>yes</i> and &#8211;login and &#8211;preserve-environment were not specified <code>runuser</code> initializes <code>PATH</code>.</dl>
<p> The environment variable <code>PATH</code> may be different on systems where <i>/bin</i> and <i>/sbin</i> are merged into <i>/usr</i>; this variable is also affected by the <code>&#8211;login</code> command-line option and the PAM system setting (e.g., <code><a href="/docs/linux/man/8-pam_env/">pam_env</a></code>(8)).</p>
<h2>EXIT STATUS</h2>
<p> <code>runuser</code> normally returns the exit status of the command it executed. If the command was killed by a signal, <code>runuser</code> returns the number of the signal plus 128. </p>
<p> Exit status generated by <code>runuser</code> itself: </p>
<p> 1</p>
<dl>
<dt>
<dd> Generic error before executing the requested command</dl>
<p> 126</p>
<dl>
<dt>
<dd> The requested command could not be executed</dl>
<p> 127</p>
<dl>
<dt>
<dd> The requested command was not found</dl>
<h2>FILES</h2>
<p> <i>/etc/pam.d/runuser</i></p>
<dl>
<dt>
<dd> default PAM configuration file</dl>
<p> <i>/etc/pam.d/runuser-l</i></p>
<dl>
<dt>
<dd> PAM configuration file if <code>&#8211;login</code> is specified</dl>
<p> <i>/etc/default/runuser</i></p>
<dl>
<dt>
<dd> runuser specific logindef config file</dl>
<p> <i>/etc/login.defs</i></p>
<dl>
<dt>
<dd> global logindef config file</dl>
<h2>HISTORY</h2>
<p> This <code>runuser</code> command was derived from coreutils&#8217; <code>su</code>, which was based on an implementation by David MacKenzie, and the Fedora <code>runuser</code> command by Dan Walsh.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-setpriv/">setpriv</a></code>(1), <code><a href="/docs/linux/man/1-su/">su</a></code>(1), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/5-shells/">shells</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>runuser</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
