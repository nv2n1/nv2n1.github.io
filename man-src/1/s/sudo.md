---
title: "sudo(1)"
name: "sudo"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sudo/"
description: "sudo, sudoedit – execute a command as another user"
---

<h2 class="name">NAME</h2>
<p> sudo, sudoedit &#8211; execute a command as another user </p>
<h2>SYNOPSIS</h2>
<p> <code>sudo</code> <code>-h</code> | <code>-K</code> | <code>-k</code> | <code>-L</code> | <code>-V</code> </p>
<p> <code>sudo</code> <code>-v</code> [<code>-AknS</code>] [<code>-g</code>&nbsp;<wbr><i>group name</i>|<i>#gid</i>] [<code>-p</code>&nbsp;<wbr><i>prompt</i>] [<code>-u</code>&nbsp;<wbr><i>username</i>|<i>#uid</i>] </p>
<p> <code>sudo</code> <code>-l[l]</code> [<code>-AknS</code>] [<code>-g</code>&nbsp;<wbr><i>group name</i>|<i>#gid</i>] [<code>-p</code>&nbsp;<wbr><i>prompt</i>] [<code>-U</code>&nbsp;<wbr><i>user name</i>] [<code>-u</code>&nbsp;<wbr><i>user name</i>|<i>#uid</i>] [<i>command</i>] </p>
<p> <code>sudo</code> [<code>-AbEHnPS</code>] [<code>-C</code>&nbsp;<wbr><i>fd</i>] [<code>-g</code>&nbsp;<wbr><i>group name</i>|<i>#gid</i>] [<code>-p</code>&nbsp;<wbr><i>prompt</i>] [<code>-r</code>&nbsp;<wbr><i>role</i>] [<code>-t</code>&nbsp;<wbr><i>type</i>] [<code>-u</code>&nbsp;<wbr><i>user name</i>|<i>#uid</i>] [<font SIZE="-1"><code>VAR</code></font>=<i>value</i>] [<code>-i</code>&nbsp;<wbr>|&nbsp;<wbr><code>-s</code>] [<i>command</i>] </p>
<p> <code>sudoedit</code> [<code>-AnS</code>] [<code>-C</code>&nbsp;<wbr><i>fd</i>] [<code>-g</code>&nbsp;<wbr><i>group name</i>|<i>#gid</i>] [<code>-p</code>&nbsp;<wbr><i>prompt</i>] [<code>-u</code>&nbsp;<wbr><i>user name</i>|<i>#uid</i>] file &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>sudo</code> allows a permitted user to execute a <i>command</i> as the superuser or another user, as specified in the <i>sudoers</i> file. The real and effective uid and gid are set to match those of the target user as specified in the passwd file and the group vector is initialized based on the group file (unless the <code>-P</code> option was specified). If the invoking user is root or if the target user is the same as the invoking user, no password is required. Otherwise, <code>sudo</code> requires that users authenticate themselves with a password by default (<font SIZE="-1">NOTE:</font> in the default configuration this is the user&#8217;s password, not the root password). Once a user has been authenticated, a time stamp is updated and the user may then use sudo without a password for a short period of time (<tt> 5<br />
 </tt> minutes unless overridden in <i>sudoers</i>). </p>
<p> When invoked as <code>sudoedit</code>, the <code>-e</code> option (described below), is implied. </p>
<p> <code>sudo</code> determines who is an authorized user by consulting the file <i>/etc/sudoers</i>. By running <code>sudo</code> with the <code>-v</code> option, a user can update the time stamp without running a <i>command</i>. If a password is required, <code>sudo</code> will exit if the user&#8217;s password is not entered within a configurable time limit. The default password prompt timeout is <tt> 5<br />
 </tt> minutes. </p>
<p> If a user who is not listed in the <i>sudoers</i> file tries to run a command via <code>sudo</code>, mail is sent to the proper authorities, as defined at configure time or in the <i>sudoers</i> file (defaults to <tt> root<br />
 </tt>). Note that the mail will not be sent if an unauthorized user tries to run sudo with the <code>-l</code> or <code>-v</code> option. This allows users to determine for themselves whether or not they are allowed to use <code>sudo</code>. </p>
<p> If <code>sudo</code> is run by root and the <tt> SUDO_USER<br />
 </tt> environment variable is set, <code>sudo</code> will use this value to determine who the actual user is. This can be used by a user to log commands through sudo even when a root shell has been invoked. It also allows the <code>-e</code> option to remain useful even when being run via a sudo-run script or program. Note however, that the sudoers lookup is still done for root, not the user specified by <tt> SUDO_USER<br />
 </tt>. </p>
<p> <code>sudo</code> can log both successful and unsuccessful attempts (as well as errors) to <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3), a log file, or both. By default <code>sudo</code> will log via <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3) but this is changeable at configure time or via the <i>sudoers</i> file.</p>
<h2>OPTIONS</h2>
<p> <code>sudo</code> accepts the following command line options:</p>
<dl>
<dt>-A</p>
<dd> Normally, if <code>sudo</code> requires a password, it will read it from the current terminal. If the <code>-A</code> (<i>askpass</i>) option is specified, a (possibly graphical) helper program is executed to read the user&#8217;s password and output the password to the standard output. If the <tt> SUDO_ASKPASS<br />
 </tt> environment variable is set, it specifies the path to the helper program. Otherwise, the value specified by the <i>askpass</i> option in <i><a href="/docs/linux/man/5-sudoers/">sudoers</a></i>(5) is used.</p>
<dt>-b</p>
<dd> The <code>-b</code> (<i>background</i>) option tells <code>sudo</code> to run the given command in the background. Note that if you use the <code>-b</code> option you cannot use shell job control to manipulate the process.</p>
<dt>-C <i>fd</i></p>
<dd> Normally, <code>sudo</code> will close all open file descriptors other than standard input, standard output and standard error. The <code>-C</code> (<i>close from</i>) option allows the user to specify a starting point above the standard error (file descriptor three). Values less than three are not permitted. This option is only available if the administrator has enabled the <i>closefrom_override</i> option in <i><a href="/docs/linux/man/5-sudoers/">sudoers</a></i>(5).</p>
<dt>-E</p>
<dd> The <code>-E</code> (<i>preserve</i> <i>environment</i>) option will override the <i>env_reset</i> option in <i><a href="/docs/linux/man/5-sudoers/">sudoers</a></i>(5)). It is only available when either the matching command has the <tt> SETENV<br />
 </tt> tag or the <i>setenv</i> option is set in <i><a href="/docs/linux/man/5-sudoers/">sudoers</a></i>(5).</p>
<dt>-e</p>
<dd> The <code>-e</code> (<i>edit</i>) option indicates that, instead of running a command, the user wishes to edit one or more files. In lieu of a command, the string &#8220;sudoedit&#8221; is used when consulting the <i>sudoers</i> file. If the user is authorized by <i>sudoers</i> the following steps are taken:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Temporary copies are made of the files to be edited with the owner set to the invoking user.</p>
<dt>2.</p>
<dd> The editor specified by the <tt> SUDO_EDITOR<br />
 </tt>, <tt> VISUAL<br />
 </tt> or <tt> EDITOR<br />
 </tt> environment variables is run to edit the temporary files. If none of <tt> SUDO_EDITOR<br />
 </tt>, <tt> VISUAL<br />
 </tt> or <tt> EDITOR<br />
 </tt> are set, the first program listed in the <i>editor</i> <i>sudoers</i> variable is used.</p>
<dt>3.</p>
<dd> If they have been modified, the temporary files are copied back to their original location and the temporary versions are removed.</dl>
</dl>
<dl>
<dt>
<dd>
<p> If the specified file does not exist, it will be created. Note that unlike most commands run by <code>sudo</code>, the editor is run with the invoking user&#8217;s environment unmodified. If, for some reason, <code>sudo</code> is unable to update a file with its edited version, the user will receive a warning and the edited copy will remain in a temporary file.</dl>
<dt>-g <i>group</i></p>
<dd> Normally, <code>sudo</code> sets the primary group to the one specified by the passwd database for the user the command is being run as (by default, root). The <code>-g</code> (<i>group</i>) option causes <code>sudo</code> to run the specified command with the primary group set to <i>group</i>. To specify a <i>gid</i> instead of a <i>group name</i>, use <i>#gid</i>. When running commands as a <i>gid</i>, many shells require that the &#8216;#&#8217; be escaped with a backslash (&#8216;\&#8217;). If no <code>-u</code> option is specified, the command will be run as the invoking user (not root). In either case, the primary group will be set to <i>group</i>.</p>
<dt>-H</p>
<dd> The <code>-H</code> (<i></i><font SIZE="-1"><i>HOME</i></font><i></i>) option sets the <tt> HOME<br />
 </tt> environment variable to the homedir of the target user (root by default) as specified in <i><a href="/docs/linux/man/5-passwd/">passwd</a></i>(5). The default handling of the <tt> HOME<br />
 </tt> environment variable depends on <i><a href="/docs/linux/man/5-sudoers/">sudoers</a></i>(5) settings. By default, <code>sudo</code> will set <tt> HOME<br />
 </tt> if <i>env_reset</i> or <i>always_set_home</i> are set, or if <i>set_home</i> is set and the <code>-s</code> option is specified on the command line.</p>
<dt>-h</p>
<dd> The <code>-h</code> (<i>help</i>) option causes <code>sudo</code> to print a usage message and exit.</p>
<dt>-i [command]</p>
<dd> The <code>-i</code> (<i>simulate initial login</i>) option runs the shell specified in the <i><a href="/docs/linux/man/5-passwd/">passwd</a></i>(5) entry of the target user as a login shell. This means that login-specific resource files such as <tt> .profile<br />
 </tt> or <tt> .login<br />
 </tt> will be read by the shell. If a command is specified, it is passed to the shell for execution. Otherwise, an interactive shell is executed. <code>sudo</code> attempts to change to that user&#8217;s home directory before running the shell. It also initializes the environment, leaving <i></i><font SIZE="-1"><i>DISPLAY</i></font><i></i> and <i></i><font SIZE="-1"><i>TERM</i></font><i></i> unchanged, setting <i></i><font SIZE="-1"><i>HOME</i></font><i></i>, <i></i><font SIZE="-1"><i>MAIL</i></font><i></i>, <i></i><font SIZE="-1"><i>SHELL</i></font><i></i>, <i></i><font SIZE="-1"><i>USER</i></font><i></i>, <i></i><font SIZE="-1"><i>LOGNAME</i></font><i></i>, and <i></i><font SIZE="-1"><i>PATH</i></font><i></i>, as well as the contents of <i>/etc/environment</i> on Linux and <font SIZE="-1">AIX</font> systems. All other environment variables are removed.</p>
<dt>-K</p>
<dd> The <code>-K</code> (sure <i>kill</i>) option is like <code>-k</code> except that it removes the user&#8217;s time stamp entirely and may not be used in conjunction with a command or other option. This option does not require a password.</p>
<dt>-k</p>
<dd> When used by itself, the <code>-k</code> (<i>kill</i>) option to <code>sudo</code> invalidates the user&#8217;s time stamp by setting the time on it to the Epoch. The next time <code>sudo</code> is run a password will be required. This option does not require a password and was added to allow a user to revoke <code>sudo</code> permissions from a .logout file. </p>
<p> When used in conjunction with a command or an option that may require a password, the <code>-k</code> option will cause <code>sudo</code> to ignore the user&#8217;s time stamp file. As a result, <code>sudo</code> will prompt for a password (if one is required by <i>sudoers</i>) and will not update the user&#8217;s time stamp file.</p>
<dt>-L</p>
<dd> The <code>-L</code> (<i>list</i> defaults) option will list the parameters that may be set in a <i>Defaults</i> line along with a short description for each. This option will be removed from a future version of <code>sudo</code>.</p>
<dt>-l[l] [<i>command</i>]</p>
<dd> If no <i>command</i> is specified, the <code>-l</code> (<i>list</i>) option will list the allowed (and forbidden) commands for the invoking user (or the user specified by the <code>-U</code> option) on the current host. If a <i>command</i> is specified and is permitted by <i>sudoers</i>, the fully-qualified path to the command is displayed along with any command line arguments. If <i>command</i> is specified but not allowed, <code>sudo</code> will exit with a status value of 1. If the <code>-l</code> option is specified with an <code>l</code> argument (i.e. <code>-ll</code>), or if <code>-l</code> is specified multiple times, a longer list format is used.</p>
<dt>-n</p>
<dd> The <code>-n</code> (<i>non-interactive</i>) option prevents <code>sudo</code> from prompting the user for a password. If a password is required for the command to run, <code>sudo</code> will display an error messages and exit.</p>
<dt>-P</p>
<dd> The <code>-P</code> (<i>preserve</i> <i>group vector</i>) option causes <code>sudo</code> to preserve the invoking user&#8217;s group vector unaltered. By default, <code>sudo</code> will initialize the group vector to the list of groups the target user is in. The real and effective group IDs, however, are still set to match the target user.</p>
<dt>-p <i>prompt</i></p>
<dd> The <code>-p</code> (<i>prompt</i>) option allows you to override the default password prompt and use a custom one. The following percent (`<tt> %<br />
 </tt>&#8216;) escapes are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt>%H</p>
<dd> expanded to the local host name including the domain name (on if the machine&#8217;s host name is fully qualified or the <i>fqdn</i> <i>sudoers</i> option is set)</p>
<dt>%h</p>
<dd> expanded to the local host name without the domain name</p>
<dt>%p</p>
<dd> expanded to the user whose password is being asked for (respects the <i>rootpw</i>, <i>targetpw</i> and <i>runaspw</i> flags in <i>sudoers</i>)</p>
<dt>%U</p>
<dd> expanded to the login name of the user the command will be run as (defaults to root)</p>
<dt>%u</p>
<dd> expanded to the invoking user&#8217;s login name</p>
<dt> %%</p>
<dd> two consecutive <tt> %<br />
 </tt> characters are collapsed into a single <tt> %<br />
 </tt> character</dl>
</dl>
<dl>
<dt>
<dd>
<p> The prompt specified by the <code>-p</code> option will override the system password prompt on systems that support <font SIZE="-1">PAM</font> unless the <i>passprompt_override</i> flag is disabled in <i>sudoers</i>.</dl>
<dt>-r <i>role</i></p>
<dd> The <code>-r</code> (<i>role</i>) option causes the new (SELinux) security context to have the role specified by <i>role</i>.</p>
<dt>-S</p>
<dd> The <code>-S</code> (<i>stdin</i>) option causes <code>sudo</code> to read the password from the standard input instead of the terminal device. The password must be followed by a newline character.</p>
<dt>-s [command]</p>
<dd> The <code>-s</code> (<i>shell</i>) option runs the shell specified by the <i></i><font SIZE="-1"><i>SHELL</i></font><i></i> environment variable if it is set or the shell as specified in <i><a href="/docs/linux/man/5-passwd/">passwd</a></i>(5). If a command is specified, it is passed to the shell for execution. Otherwise, an interactive shell is executed.</p>
<dt>-t <i>type</i></p>
<dd> The <code>-t</code> (<i>type</i>) option causes the new (SELinux) security context to have the type specified by <i>type</i>. If no type is specified, the default type is derived from the specified role.</p>
<dt>-U <i>user</i></p>
<dd> The <code>-U</code> (<i>other user</i>) option is used in conjunction with the <code>-l</code> option to specify the user whose privileges should be listed. Only root or a user with <code>sudo</code> <tt> ALL<br />
 </tt> on the current host may use this option.</p>
<dt>-u <i>user</i></p>
<dd> The <code>-u</code> (<i>user</i>) option causes <code>sudo</code> to run the specified command as a user other than <i>root</i>. To specify a <i>uid</i> instead of a <i>user name</i>, use <i>#uid</i>. When running commands as a <i>uid</i>, many shells require that the &#8216;#&#8217; be escaped with a backslash (&#8216;\&#8217;). Note that if the <i>targetpw</i> Defaults option is set (see <i><a href="/docs/linux/man/5-sudoers/">sudoers</a></i>(5)) it is not possible to run commands with a uid not listed in the password database.</p>
<dt>-V</p>
<dd> The <code>-V</code> (<i>version</i>) option causes <code>sudo</code> to print the version number and exit. If the invoking user is already root the <code>-V</code> option will print out a list of the defaults <code>sudo</code> was compiled with as well as the machine&#8217;s local network addresses.</p>
<dt>-v</p>
<dd> If given the <code>-v</code> (<i>validate</i>) option, <code>sudo</code> will update the user&#8217;s time stamp, prompting for the user&#8217;s password if necessary. This extends the <code>sudo</code> timeout for another <tt> 5<br />
 </tt> minutes (or whatever the timeout is set to in <i>sudoers</i>) but does not run a command.</p>
<dt>&#8212;</p>
<dd> The <code>&#8212;</code> option indicates that <code>sudo</code> should stop processing command line arguments.</dl>
<p> Environment variables to be set for the command may also be passed on the command line in the form of <font SIZE="-1"><code>VAR</code></font>=<i>value</i>, e.g. <font SIZE="-1"><code>LD_LIBRARY_PATH</code></font>=<i>/usr/local/pkg/lib</i>. Variables passed on the command line are subject to the same restrictions as normal environment variables with one important exception. If the <i>setenv</i> option is set in <i>sudoers</i>, the command to be run has the <tt> SETENV<br />
 </tt> tag set or the command matched is <tt> ALL<br />
 </tt>, the user may set variables that would overwise be forbidden. See <i><a href="/docs/linux/man/5-sudoers/">sudoers</a></i>(5) for more information.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful execution of a program, the exit status from <code>sudo</code> will simply be the exit status of the program that was executed. </p>
<p> Otherwise, <code>sudo</code> quits with an exit value of 1 if there is a configuration/permission problem or if <code>sudo</code> cannot execute the given command. In the latter case the error string is printed to stderr. If <code>sudo</code> cannot <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2) one or more entries in the user&#8217;s <tt> PATH<br />
 </tt> an error is printed on stderr. (If the directory does not exist or if it is not really a directory, the entry is ignored and no error is printed.) This should not happen under normal circumstances. The most common reason for <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2) to return &#8220;permission denied&#8221; is if you are running an automounter and one of the directories in your <tt> PATH<br />
 </tt> is on a machine that is currently unreachable.</p>
<h2>SECURITY NOTES</h2>
<p> <code>sudo</code> tries to be safe when executing external commands. </p>
<p> There are two distinct ways to deal with environment variables. By default, the <i>env_reset</i> <i>sudoers</i> option is enabled. This causes commands to be executed with a minimal environment containing <tt> TERM<br />
 </tt>, <tt> PATH<br />
 </tt>, <tt> HOME<br />
 </tt>, <tt> SHELL<br />
 </tt>, <tt> LOGNAME<br />
 </tt>, <tt> USER<br />
 </tt> and <tt> USERNAME<br />
 </tt> in addition to variables from the invoking process permitted by the <i>env_check</i> and <i>env_keep</i> <i>sudoers</i> options. There is effectively a whitelist for environment variables. </p>
<p> If, however, the <i>env_reset</i> option is disabled in <i>sudoers</i>, any variables not explicitly denied by the <i>env_check</i> and <i>env_delete</i> options are inherited from the invoking process. In this case, <i>env_check</i> and <i>env_delete</i> behave like a blacklist. Since it is not possible to blacklist all potentially dangerous environment variables, use of the default <i>env_reset</i> behavior is encouraged. </p>
<p> In all cases, environment variables with a value beginning with <tt> ()<br />
 </tt> are removed as they could be interpreted as <code>bash</code> functions. The list of environment variables that <code>sudo</code> allows or denies is contained in the output of <tt> sudo -V<br />
 </tt> when run as root. </p>
<p> Note that the dynamic linker on most operating systems will remove variables that can control dynamic linking from the environment of setuid executables, including <code>sudo</code>. Depending on the operating system this may include <tt> _RLD*<br />
 </tt>, <tt> DYLD_*<br />
 </tt>, <tt> LD_*<br />
 </tt>, <tt> LDR_*<br />
 </tt>, <tt> LIBPATH<br />
 </tt>, <tt> SHLIB_PATH<br />
 </tt>, and others. These type of variables are removed from the environment before <code>sudo</code> even begins execution and, as such, it is not possible for <code>sudo</code> to preserve them. </p>
<p> To prevent command spoofing, <code>sudo</code> checks &#8220;.&#8221; and &quot;&quot; (both denoting current directory) last when searching for a command in the user&#8217;s <font SIZE="-1">PATH</font> (if one or both are in the <font SIZE="-1">PATH</font>). Note, however, that the actual <tt> PATH<br />
 </tt> environment variable is <i>not</i> modified and is passed unchanged to the program that <code>sudo</code> executes. </p>
<p> <code>sudo</code> will check the ownership of its time stamp directory (<i>/var/db/sudo</i> by default) and ignore the directory&#8217;s contents if it is not owned by root or if it is writable by a user other than root. On systems that allow non-root users to give away files via <i><a href="/docs/linux/man/2-chown/">chown</a></i>(2), if the time stamp directory is located in a directory writable by anyone (e.g., <i>/tmp</i>), it is possible for a user to create the time stamp directory before <code>sudo</code> is run. However, because <code>sudo</code> checks the ownership and mode of the directory and its contents, the only damage that can be done is to &#8220;hide&#8221; files by putting them in the time stamp dir. This is unlikely to happen since once the time stamp dir is owned by root and inaccessible by any other user, the user placing files there would be unable to get them back out. To get around this issue you can use a directory that is not world-writable for the time stamps (<i>/var/adm/sudo</i> for instance) or create <i>/var/db/sudo</i> with the appropriate owner (root) and permissions (0700) in the system startup files. </p>
<p> <code>sudo</code> will not honor time stamps set far in the future. Timestamps with a date greater than current_time + 2 * <tt> TIMEOUT<br />
 </tt> will be ignored and sudo will log and complain. This is done to keep a user from creating his/her own time stamp with a bogus date on systems that allow users to give away files. </p>
<p> On systems where the boot time is available, <code>sudo</code> will also not honor time stamps from before the machine booted. </p>
<p> Since time stamp files live in the file system, they can outlive a user&#8217;s login session. As a result, a user may be able to login, run a command with <code>sudo</code> after authenticating, logout, login again, and run <code>sudo</code> without authenticating so long as the time stamp file&#8217;s modification time is within <tt> 5<br />
 </tt> minutes (or whatever the timeout is set to in <i>sudoers</i>). When the <i>tty_tickets</i> option is enabled in <i>sudoers</i>, the time stamp has per-tty granularity but still may outlive the user&#8217;s session. On Linux systems where the devpts filesystem is used, Solaris systems with the devices filesystem, as well as other systems that utilize a devfs filesystem that monotonically increase the inode number of devices as they are created (such as Mac <font SIZE="-1">OS</font> X), <code>sudo</code> is able to determine when a tty-based time stamp file is stale and will ignore it. Administrators should not rely on this feature as it is not universally available. </p>
<p> Please note that <code>sudo</code> will normally only log the command it explicitly runs. If a user runs a command such as <tt> sudo su<br />
 </tt> or <tt> sudo sh<br />
 </tt>, subsequent commands run from that shell will <i>not</i> be logged, nor will <code>sudo</code>&#8216;s access control affect them. The same is true for commands that offer shell escapes (including most editors). Because of this, care must be taken when giving users access to commands via <code>sudo</code> to verify that the command does not inadvertently give the user an effective root shell. For more information, please see the <tt> PREVENTING SHELL ESCAPES<br />
 </tt> section in <i><a href="/docs/linux/man/5-sudoers/">sudoers</a></i>(5).</p>
<h2>ENVIRONMENT</h2>
<p> <code>sudo</code> utilizes the following environment variables:</p>
<dl>
<dt> EDITOR</p>
<dd> Default editor to use in <code>-e</code> (sudoedit) mode if neither <tt> SUDO_EDITOR<br />
 </tt> nor <tt> VISUAL<br />
 </tt> is set</p>
<dt> MAIL</p>
<dd> In <code>-i</code> mode or when <i>env_reset</i> is enabled in <i>sudoers</i>, set to the mail spool of the target user</p>
<dt> HOME</p>
<dd> Set to the home directory of the target user if <code>-i</code> or <code>-H</code> are specified, <i>env_reset</i> or <i>always_set_home</i> are set in <i>sudoers</i>, or when the <code>-s</code> option is specified and <i>set_home</i> is set in <i>sudoers</i></p>
<dt> PATH</p>
<dd> Set to a sane value if the <i>secure_path</i> sudoers option is set.</p>
<dt> SHELL</p>
<dd> Used to determine shell to run with <tt> -s<br />
 </tt> option</p>
<dt> SUDO_ASKPASS</p>
<dd> Specifies the path to a helper program used to read the password if no terminal is available or if the <tt> -A<br />
 </tt> option is specified.</p>
<dt> SUDO_COMMAND</p>
<dd> Set to the command run by sudo</p>
<dt> SUDO_EDITOR</p>
<dd> Default editor to use in <code>-e</code> (sudoedit) mode</p>
<dt> SUDO_GID</p>
<dd> Set to the group <font SIZE="-1">ID</font> of the user who invoked sudo</p>
<dt> SUDO_PROMPT</p>
<dd> Used as the default password prompt</p>
<dt> SUDO_PS1</p>
<dd> If set, <tt> PS1<br />
 </tt> will be set to its value for the program being run</p>
<dt> SUDO_UID</p>
<dd> Set to the user <font SIZE="-1">ID</font> of the user who invoked sudo</p>
<dt> SUDO_USER</p>
<dd> Set to the login of the user who invoked sudo</p>
<dt> USER</p>
<dd> Set to the target user (root unless the <code>-u</code> option is specified)</p>
<dt> VISUAL</p>
<dd> Default editor to use in <code>-e</code> (sudoedit) mode if <tt> SUDO_EDITOR<br />
 </tt> is not set</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/sudoers</i></p>
<dd> List of who can run what</p>
<dt><i>/var/db/sudo</i></p>
<dd> Directory containing time stamps</p>
<dt><i>/etc/environment</i></p>
<dd> Initial environment for <code>-i</code> mode on Linux and <font SIZE="-1">AIX</font></dl>
<h2>EXAMPLES</h2>
<p> Note: the following examples assume suitable <i><a href="/docs/linux/man/5-sudoers/">sudoers</a></i>(5) entries. </p>
<p> To get a file listing of an unreadable directory: </p>
<pre>
 $ sudo ls /usr/local/protected
</pre>
<p> To list the home directory of user yaz on a machine where the file system holding ~yaz is not exported as root: </p>
<pre>
 $ sudo -u yaz ls ~yaz
</pre>
<p> To edit the <i>index.html</i> file as user www: </p>
<pre>
 $ sudo -u www vi ~www/htdocs/index.html
</pre>
<p> To view system logs only accessible to root and users in the adm group: </p>
<pre>
 $ sudo -g adm view /var/log/syslog
</pre>
<p> To run an editor as jim with a different primary group: </p>
<pre>
 $ sudo -u jim -g audio vi ~jim/sound.txt
</pre>
<p> To shutdown a machine: </p>
<pre>
 $ sudo shutdown -r +15 &quot;quick reboot&quot;
</pre>
<p> To make a usage listing of the directories in the /home partition. Note that this runs the commands in a sub-shell to make the <tt> cd<br />
 </tt> and file redirection work. </p>
<pre>
 $ sudo sh -c &quot;cd /home ; du -s * | sort -rn &gt; USAGE&quot;
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-grep/">grep</a></i>(1), <i><a href="/docs/linux/man/1-su/">su</a></i>(1), <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2), <i><a href="/docs/linux/man/5-passwd/">passwd</a></i>(5), <i><a href="/docs/linux/man/5-sudoers/">sudoers</a></i>(5), <i><a href="/docs/linux/man/8-visudo/">visudo</a></i>(8)</p>
<h2>AUTHORS</h2>
<p> Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<pre>
        Todd C. Miller
</pre>
<p> See the <font SIZE="-1">HISTORY</font> file in the <code>sudo</code> distribution or visit <a rel="nofollow" href="http://www.sudo.ws/sudo/history.html">http://www.sudo.ws/sudo/history.html</a> for a short history of <code>sudo</code>.</p>
<h2>CAVEATS</h2>
<p> There is no easy way to prevent a user from gaining a root shell if that user is allowed to run arbitrary commands via <code>sudo</code>. Also, many programs (such as editors) allow the user to run commands via shell escapes, thus avoiding <code>sudo</code>&#8216;s checks. However, on most systems it is possible to prevent shell escapes with <code>sudo</code>&#8216;s <i>noexec</i> functionality. See the <i><a href="/docs/linux/man/5-sudoers/">sudoers</a></i>(5) manual for details. </p>
<p> It is not meaningful to run the <tt> cd<br />
 </tt> command directly via sudo, e.g., </p>
<pre>
 $ sudo cd /usr/local/protected
</pre>
<p> since when the command exits the parent process (your shell) will still be the same. Please see the <font SIZE="-1">EXAMPLES</font> section for more information. </p>
<p> If users have sudo <tt> ALL<br />
 </tt> there is nothing to prevent them from creating their own program that gives them a root shell regardless of any &#8216;!&#8217; elements in the user specification. </p>
<p> Running shell scripts via <code>sudo</code> can expose the same kernel bugs that make setuid shell scripts unsafe on some operating systems (if your <font SIZE="-1">OS</font> has a /dev/fd/ directory, setuid shell scripts are generally safe).</p>
<h2>BUGS</h2>
<p> If you feel you have found a bug in <code>sudo</code>, please submit a bug report at <a rel="nofollow" href="http://www.sudo.ws/sudo/bugs/">http://www.sudo.ws/sudo/bugs/</a></p>
<h2>SUPPORT</h2>
<p> Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="http://www.sudo.ws/mailman/listinfo/sudo-users">http://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.</p>
<h2>DISCLAIMER</h2>
<p> <code>sudo</code> is provided &#8220;<font SIZE="-1">AS</font> <font SIZE="-1">IS</font>&#8221; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the <font SIZE="-1">LICENSE</font> file distributed with <code>sudo</code> or <a rel="nofollow" href="http://www.sudo.ws/sudo/license.html">http://www.sudo.ws/sudo/license.html</a> for complete details. </p>
<h2>Index</h2>
