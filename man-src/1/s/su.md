---
title: "su(1)"
name: "su"
section: "1"
letter: "s"
url: "/docs/linux/man/1-su/"
description: "su – run a command with substitute user and group ID"
---

<h2 class="name">NAME</h2>
<p> su &#8211; run a command with substitute user and group ID </p>
<h2>SYNOPSIS</h2>
<p> <code>su</code> [options] [<code>&#8211;</code>] [<i>user</i> [<i>argument</i>&#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> <code>su</code> allows commands to be run with a substitute user and group ID. </p>
<p> When called with no <i>user</i> specified, <code>su</code> defaults to running an interactive shell as <i>root</i>. When <i>user</i> is specified, additional <i>argument</i>s can be supplied, in which case they are passed to the shell. </p>
<p> For backward compatibility, <code>su</code> defaults to not change the current directory and to only set the environment variables <code>HOME</code> and <code>SHELL</code> (plus <code>USER</code> and <code>LOGNAME</code> if the target <i>user</i> is not root). It is recommended to always use the <code>&#8211;login</code> option (instead of its shortcut <code>&#8211;</code>) to avoid side effects caused by mixing environments. </p>
<p> This version of <code>su</code> uses PAM for authentication, account and session management. Some configuration options found in other <code>su</code> implementations, such as support for a wheel group, have to be configured via PAM. </p>
<p> <code>su</code> is mostly designed for unprivileged users, the recommended solution for privileged users (e.g., scripts executed by root) is to use non-set-user-ID command <code><a href="/docs/linux/man/1-runuser/">runuser</a></code>(1) that does not require authentication and provides separate PAM configuration. If the PAM session is not required at all then the recommended solution is to use command <code><a href="/docs/linux/man/1-setpriv/">setpriv</a></code>(1). </p>
<p> Note that <code>su</code> in all cases uses PAM (<code><a href="/docs/linux/man/3-pam_getenvlist/">pam_getenvlist</a></code>(3)) to do the final environment modification. Command-line options such as <code>&#8211;login</code> and <code>&#8211;preserve-environment</code> affect the environment before it is modified by PAM.</p>
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
<dd> Specify the primary group. This option is available to the root user only.</dl>
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
<dd> &bull; clears all the environment variables except <code>TERM</code> and variables specified by <code>&#8211;whitelist-environment</code></dl>
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
<p> <code>-m</code>, <code>-p</code>, <code>&#8211;preserve-environment</code></p>
<dl>
<dt>
<dd> Preserve the entire environment, i.e., do not set <code>HOME</code>, <code>SHELL</code>, <code>USER</code> or <code>LOGNAME</code>. This option is ignored if the option <code>&#8211;login</code> is specified.</dl>
<p> <code>-P</code>, <code>&#8211;pty</code></p>
<dl>
<dt>
<dd> Create a pseudo-terminal for the session. The independent terminal provides better security as the user does not share a terminal with the original session. This can be used to avoid TIOCSTI ioctl terminal injection and other security attacks against terminal file descriptors. The entire session can also be moved to the background (e.g., &quot;su &#8211;pty &#8211; username -c application &amp;&quot;). If the pseudo-terminal is enabled, then <code>su</code> works as a proxy between the sessions (copy stdin and stdout). </p>
<p> This feature is mostly designed for interactive sessions. If the standard input is not a terminal, but for example a pipe (e.g., echo &quot;date&quot; | su &#8211;pty), then the ECHO flag for the pseudo-terminal is disabled to avoid messy output.</dl>
<p> <code>-s</code>, <code>&#8211;shell</code>=<i>shell</i></p>
<dl>
<dt>
<dd> Run the specified <i>shell</i> instead of the default. The shell to run is selected according to the following rules, in order: </p>
<dl>
<dt>
<dd> &bull; the shell specified with <code>&#8211;shell</code></dl>
<dl>
<dt>
<dd> &bull; the shell specified in the environment variable <code>SHELL</code>, if the <code>&#8211;preserve-environment</code> option is used</dl>
<dl>
<dt>
<dd> &bull; the shell listed in the passwd entry of the target user</dl>
<dl>
<dt>
<dd> &bull; /bin/sh</dl>
</dl>
<p> If the target user has a restricted shell (i.e., not listed in /etc/shells), the <code>&#8211;shell</code> option and the <code>SHELL</code> environment variables are ignored unless the calling user is root. </p>
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
<h2>SIGNALS</h2>
<p> Upon receiving either <code>SIGINT</code>, <code>SIGQUIT</code> or <code>SIGTERM</code>, <code>su</code> terminates its child and afterwards terminates itself with the received signal. The child is terminated by <code>SIGTERM</code>, after unsuccessful attempt and 2 seconds of delay the child is killed by <code>SIGKILL</code>.</p>
<h2>CONFIG FILES</h2>
<p> <code>su</code> reads the <i>/etc/default/su</i> and <i>/etc/login.defs</i> configuration files. The following configuration items are relevant for <code>su:</code> </p>
<p> <code>FAIL_DELAY</code> (number)</p>
<dl>
<dt>
<dd> Delay in seconds in case of an authentication failure. The number must be a non-negative integer.</dl>
<p> <code>ENV_PATH</code> (string)</p>
<dl>
<dt>
<dd> Defines the <code>PATH</code> environment variable for a regular user. The default value is <i>/usr/local/bin:/bin:/usr/bin</i>.</dl>
<p> <code>ENV_ROOTPATH</code> (string), <code>ENV_SUPATH</code> (string)</p>
<dl>
<dt>
<dd> Defines the <code>PATH</code> environment variable for root. <code>ENV_SUPATH</code> takes precedence. The default value is <i>/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin</i>.</dl>
<p> <code>ALWAYS_SET_PATH</code> (boolean)</p>
<dl>
<dt>
<dd> If set to <i>yes</i> and <code>&#8211;login</code> and <code>&#8211;preserve-environment</code> were not specified <code>su</code> initializes <code>PATH</code>. </p>
<p> The environment variable <code>PATH</code> may be different on systems where <i>/bin</i> and <i>/sbin</i> are merged into <i>/usr</i>; this variable is also affected by the <code>&#8211;login</code> command-line option and the PAM system setting (e.g., <code><a href="/docs/linux/man/8-pam_env/">pam_env</a></code>(8)).</dl>
<h2>EXIT STATUS</h2>
<p> <code>su</code> normally returns the exit status of the command it executed. If the command was killed by a signal, <code>su</code> returns the number of the signal plus 128. </p>
<p> Exit status generated by <code>su</code> itself: </p>
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
<p> <i>/etc/pam.d/su</i></p>
<dl>
<dt>
<dd> default PAM configuration file</dl>
<p> <i>/etc/pam.d/su-l</i></p>
<dl>
<dt>
<dd> PAM configuration file if <code>&#8211;login</code> is specified</dl>
<p> <i>/etc/default/su</i></p>
<dl>
<dt>
<dd> command specific logindef config file</dl>
<p> <i>/etc/login.defs</i></p>
<dl>
<dt>
<dd> global logindef config file</dl>
<h2>NOTES</h2>
<p> For security reasons, <code>su</code> always logs failed log-in attempts to the btmp file, but it does not write to the <i>lastlog</i> file at all. This solution can be used to control <code>su</code> behavior by PAM configuration. If you want to use the <code><a href="/docs/linux/man/8-pam_lastlog/">pam_lastlog</a></code>(8) module to print warning message about failed log-in attempts then <code><a href="/docs/linux/man/8-pam_lastlog/">pam_lastlog</a></code>(8) has to be configured to update the <i>lastlog</i> file as well. For example by:</p>
<dl>
<dt>
<dd>
<p> session required pam_lastlog.so nowtmp
</dl>
<h2>HISTORY</h2>
<p> This <code>su</code> command was derived from coreutils&#8217; <code>su</code>, which was based on an implementation by David MacKenzie. The util-linux version has been refactored by Karel Zak.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-setpriv/">setpriv</a></code>(1), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/5-shells/">shells</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8), <code><a href="/docs/linux/man/1-runuser/">runuser</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>su</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
