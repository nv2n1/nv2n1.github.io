---
title: "sudoedit(8)"
name: "sudoedit"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sudoedit/"
description: "sudo sudoedit – execute a command as another user"
---

<p>Sudo 1.9.9</p>
<h2>Name</h2>
<p><code>sudo</code> <code>sudoedit</code> &#8211; execute a command as another user</p>
<h2>Synopsis</h2>
<p><code>sudo</code> &#8211;<code>h | K | k | V</code><br />
<code>sudo</code> &#8211;<code>v</code> [-<code>ABknS</code> ] [-<code>g </code><i>group</i> ] [-<code>h </code><i>host</i> ] [-<code>p </code><i>prompt</i> ] [-<code>u </code><i>user</i> ]<br />
<code>sudo</code> &#8211;<code>l</code> [-<code>ABknS</code> ] [-<code>g </code><i>group</i> ] [-<code>h </code><i>host</i> ] [-<code>p </code><i>prompt</i> ] [-<code>U </code><i>user</i> ] [-<code>u </code><i>user</i> ] [<i>command</i> ]<br />
<code>sudo</code> [-<code>ABbEHnPS</code> ] [-<code>C </code><i>num</i> ] [-<code>D </code><i>directory</i> ] [-<code>g </code><i>group</i> ] [-<code>h </code><i>host</i> ] [-<code>p </code><i>prompt</i> ] [-<code>R </code><i>directory</i> ] [-<code>r </code><i>role</i> ] [-<code>t </code><i>type</i> ] [-<code>T </code><i>timeout</i> ] [-<code>u </code><i>user</i> ] [<i>VAR </i><code>= </code><i>value</i> ] [-<code>i | s</code> ] [<i>command</i> ]<br />
<code>sudoedit</code> [-<code>ABknS</code> ] [-<code>C </code><i>num</i> ] [-<code>D </code><i>directory</i> ] [-<code>g </code><i>group</i> ] [-<code>h </code><i>host</i> ] [-<code>p </code><i>prompt</i> ] [-<code>R </code><i>directory</i> ] [-<code>r </code><i>role</i> ] [-<code>t </code><i>type</i> ] [-<code>T </code><i>timeout</i> ] [-<code>u </code><i>user</i> ] <i>file &#8230;</i></p>
<h2>Description</h2>
<p><code>sudo</code> allows a permitted user to execute a <i>command</i> as the superuser or another user, as specified by the security policy. The invoking user&#8217;s real (<i>not </i><code>effective</code> ) user-ID is used to determine the user name with which to query the security policy. </p>
<p> <code>sudo</code> supports a plugin architecture for security policies, auditing, and input/output logging. Third parties can develop and distribute their own plugins to work seamlessly with the <code>sudo</code> front-end. The default security policy is <i>sudoers</i> which is configured via the file /etc/sudoers or via LDAP. See the Sx Plugins section for more information. </p>
<p> The security policy determines what privileges, if any, a user has to run <code>sudo.</code> The policy may require that users authenticate themselves with a password or another authentication mechanism. If authentication is required, <code>sudo</code> will exit if the user&#8217;s password is not entered within a configurable time limit. This limit is policy-specific; the default password prompt timeout for the <i>sudoers</i> security policy is <code>0</code> minutes. </p>
<p> Security policies may support credential caching to allow the user to run <code>sudo</code> again for a period of time without requiring authentication. By default, the <i>sudoers</i> policy caches credentials on a per-terminal basis for <code>15</code> minutes. See the <i>timestamp_type</i> and <i>timestamp_timeout</i> options in <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5) for more information. By running <code>sudo</code> with the &#8211;<code>v</code> option, a user can update the cached credentials without running a <i>command</i> </p>
<p> On systems where <code>sudo</code> is the primary method of gaining superuser privileges, it is imperative to avoid syntax errors in the security policy configuration files. For the default security policy, <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5), changes to the configuration files should be made using the <a href="/docs/linux/man/8-visudo/">visudo</a>(8) utility which will ensure that no syntax errors are introduced. </p>
<p> When invoked as <code>sudoedit</code> the &#8211;<code>e</code> option (described below), is implied. </p>
<p> Security policies and audit plugins may log successful and failed attempts to run <code>sudo.</code> If an I/O plugin is configured, the running command&#8217;s input and output may be logged as well. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-A , -askpass</code></p>
<dd>Normally, if <code>sudo</code> requires a password, it will read it from the user&#8217;s terminal. If the &#8211;<code>A (</code><i>askpass</i> ) option is specified, a (possibly graphical) helper program is executed to read the user&#8217;s password and output the password to the standard output. If the <code>SUDO_ASKPASS</code> environment variable is set, it specifies the path to the helper program. Otherwise, if sudo.conf5 contains a line specifying the askpass program, that value will be used. For example: </p>
<pre># Path to askpass helper program
Path askpass /usr/X11R6/bin/ssh-askpass</pre>
<p>If no askpass program is available, <code>sudo</code> will exit with an error.</p>
<dt><code>-B , -bell</code></p>
<dd>Ring the bell as part of the password prompt when a terminal is present. This option has no effect if an askpass program is used.</p>
<dt><code>-b , -background</code></p>
<dd>Run the given command in the background. Note that it is not possible to use shell job control to manipulate background processes started by <code>sudo.</code> Most interactive commands will fail to work properly in background mode.</p>
<dt><code>-C </code><i>num , &#8211;</i><code>-close-from = </code><i>num</i></p>
<dd>Close all file descriptors greater than or equal to <i>num</i> before executing a command. Values less than three are not permitted. By default, <code>sudo</code> will close all open file descriptors other than standard input, standard output, and standard error when executing a command. The security policy may restrict the user&#8217;s ability to use this option. The <i>sudoers</i> policy only permits use of the &#8211;<code>C</code> option when the administrator has enabled the <i>closefrom_override</i> option.</p>
<dt><code>-D </code><i>directory , &#8211;</i><code>-chdir = </code><i>directory</i></p>
<dd>Run the command in the specified <i>directory</i> instead of the current working directory. The security policy may return an error if the user does not have permission to specify the working directory.</p>
<dt><code>-E , -preserve-env</code></p>
<dd>Indicates to the security policy that the user wishes to preserve their existing environment variables. The security policy may return an error if the user does not have permission to preserve the environment.</p>
<dt><code>&#8211;preserve-env=list</code></p>
<dd>Indicates to the security policy that the user wishes to add the comma-separated list of environment variables to those preserved from the user&#8217;s environment. The security policy may return an error if the user does not have permission to preserve the environment. This option may be specified multiple times.</p>
<dt><code>-e , -edit</code></p>
<dd>Edit one or more files instead of running a command. In lieu of a path name, the string &quot;sudoedit&quot; is used when consulting the security policy. If the user is authorized by the policy, the following steps are taken: </p>
<ol>
<li> Temporary copies are made of the files to be edited with the owner set to the invoking user.
<li> The editor specified by the policy is run to edit the temporary files. The <i>sudoers</i> policy uses the <code>SUDO_EDITOR</code> <code>VISUAL</code> and <code>EDITOR</code> environment variables (in that order). If none of <code>SUDO_EDITOR</code> <code>VISUAL</code> or <code>EDITOR</code> are set, the first program listed in the <i>editor</i> <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5) option is used.
<li> If they have been modified, the temporary files are copied back to their original location and the temporary versions are removed. </ol>
<p> To help prevent the editing of unauthorized files, the following restrictions are enforced unless explicitly allowed by the security policy: </p>
<ul>
<li> Symbolic links may not be edited (version 1.8.15 and higher).
<li> Symbolic links along the path to be edited are not followed when the parent directory is writable by the invoking user unless that user is root (version 1.8.16 and higher).
<li> Files located in a directory that is writable by the invoking user may not be edited unless that user is root (version 1.8.16 and higher). </ul>
<p> Users are never allowed to edit device special files. </p>
<p> If the specified file does not exist, it will be created. Note that unlike most commands run by <i>sudo</i> the editor is run with the invoking user&#8217;s environment unmodified. If the temporary file becomes empty after editing, the user will be prompted before it is installed. If, for some reason, <code>sudo</code> is unable to update a file with its edited version, the user will receive a warning and the edited copy will remain in a temporary file.</p>
<dt><code>-g </code><i>group , &#8211;</i><code>-group = </code><i>group</i></p>
<dd>Run the command with the primary group set to <i>group</i> instead of the primary group specified by the target user&#8217;s password database entry. The <i>group</i> may be either a group name or a numeric group-ID (GID) prefixed with the `#&#8217; character (e.g., <code>#0</code> for GID 0). When running a command as a GID, many shells require that the `#&#8217; be escaped with a backslash (`\&#8217; ) If no &#8211;<code>u</code> option is specified, the command will be run as the invoking user. In either case, the primary group will be set to <i>group</i> The <i>sudoers</i> policy permits any of the target user&#8217;s groups to be specified via the &#8211;<code>g</code> option as long as the &#8211;<code>P</code> option is not in use.</p>
<dt><code>-H , -set-home</code></p>
<dd>Request that the security policy set the <code>HOME</code> environment variable to the home directory specified by the target user&#8217;s password database entry. Depending on the policy, this may be the default behavior.</p>
<dt><code>-h , -help</code></p>
<dd>Display a short help message to the standard output and exit.</p>
<dt><code>-h </code><i>host , &#8211;</i><code>-host = </code><i>host</i></p>
<dd>Run the command on the specified <i>host</i> if the security policy plugin supports remote commands. Note that the <i>sudoers</i> plugin does not currently support running remote commands. This may also be used in conjunction with the &#8211;<code>l</code> option to list a user&#8217;s privileges for the remote host.</p>
<dt><code>-i , -login</code></p>
<dd>Run the shell specified by the target user&#8217;s password database entry as a login shell. This means that login-specific resource files such as .profile .bash_profile or .login will be read by the shell. If a command is specified, it is passed to the shell as a simple command using the &#8211;<code>c</code> option. The command and any arguments are concatenated, separated by spaces, after escaping each character (including white space) with a backslash (`\&#8217; ) except for alphanumerics, underscores, hyphens, and dollar signs. If no command is specified, an interactive shell is executed. <code>sudo</code> attempts to change to that user&#8217;s home directory before running the shell. The command is run with an environment similar to the one a user would receive at log in. Note that most shells behave differently when a command is specified as compared to an interactive session; consult the shell&#8217;s manual for details. The <i>Command environment</i> section in the <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5) manual documents how the &#8211;<code>i</code> option affects the environment in which a command is run when the <i>sudoers</i> policy is in use.</p>
<dt><code>-K , -remove-timestamp</code></p>
<dd>Similar to the &#8211;<code>k</code> option, except that it removes the user&#8217;s cached credentials entirely and may not be used in conjunction with a command or other option. This option does not require a password. Not all security policies support credential caching.</p>
<dt><code>-k , -reset-timestamp</code></p>
<dd>When used without a command, invalidates the user&#8217;s cached credentials. In other words, the next time <code>sudo</code> is run a password will be required. This option does not require a password, and was added to allow a user to revoke <code>sudo</code> permissions from a .logout file. </p>
<p> When used in conjunction with a command or an option that may require a password, this option will cause <code>sudo</code> to ignore the user&#8217;s cached credentials. As a result, <code>sudo</code> will prompt for a password (if one is required by the security policy) and will not update the user&#8217;s cached credentials. </p>
<p> Not all security policies support credential caching.</p>
<dt><code>-l , &#8211;list</code></p>
<dd>If no <i>command</i> is specified, list the allowed (and forbidden) commands for the invoking user (or the user specified by the &#8211;<code>U</code> option) on the current host. A longer list format is used if this option is specified multiple times and the security policy supports a verbose output format. </p>
<p> If a <i>command</i> is specified and is permitted by the security policy, the fully-qualified path to the command is displayed along with any command line arguments. If a <i>command</i> is specified but not allowed by the policy, <code>sudo</code> will exit with a status value of 1.</p>
<dt><code>-n , -non-interactive</code></p>
<dd>Avoid prompting the user for input of any kind. If a password is required for the command to run, <code>sudo</code> will display an error message and exit.</p>
<dt><code>-P , -preserve-groups</code></p>
<dd>Preserve the invoking user&#8217;s group vector unaltered. By default, the <i>sudoers</i> policy will initialize the group vector to the list of groups the target user is a member of. The real and effective group-IDs, however, are still set to match the target user.</p>
<dt><code>-p </code><i>prompt , &#8211;</i><code>-prompt = </code><i>prompt</i></p>
<dd>Use a custom password prompt with optional escape sequences. The following percent (`%&#8217; ) escape sequences are supported by the <i>sudoers</i> policy:</p>
<dl>
<dt><code>%H</code></p>
<dd>expanded to the host name including the domain name (only if the machine&#8217;s host name is fully qualified or the <i>fqdn</i> option is set in <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5))</p>
<dt><code>%h</code></p>
<dd>expanded to the local host name without the domain name</p>
<dt><code>%p</code></p>
<dd>expanded to the name of the user whose password is being requested (respects the <i>rootpw</i> <i>targetpw</i> and <i>runaspw</i> flags in <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5))</p>
<dt><code>%U</code></p>
<dd>expanded to the login name of the user the command will be run as (defaults to root unless the &#8211;<code>u</code> option is also specified)</p>
<dt><code>%u</code></p>
<dd>expanded to the invoking user&#8217;s login name</p>
<dt><code>%%</code></p>
<dd>two consecutive `%&#8217; characters are collapsed into a single `%&#8217; character</dl>
<p> The custom prompt will override the default prompt specified by either the security policy or the <code>SUDO_PROMPT</code> environment variable. On systems that use PAM, the custom prompt will also override the prompt specified by a PAM module unless the <i>passprompt_override</i> flag is disabled in <i>sudoers</i></p>
<dt><code>-R </code><i>directory , &#8211;</i><code>-chroot = </code><i>directory</i></p>
<dd>Change to the specified root <i>directory</i> (see <a href="/docs/linux/man/8-chroot/">chroot</a>(8)) before running the command. The security policy may return an error if the user does not have permission to specify the root directory.</p>
<dt><code>-r </code><i>role , &#8211;</i><code>-role = </code><i>role</i></p>
<dd>Run the command with an SELinux security context that includes the specified <i>role</i></p>
<dt><code>-S , -stdin</code></p>
<dd>Write the prompt to the standard error and read the password from the standard input instead of using the terminal device.</p>
<dt><code>-s , -shell</code></p>
<dd>Run the shell specified by the <code>SHELL</code> environment variable if it is set or the shell specified by the invoking user&#8217;s password database entry. If a command is specified, it is passed to the shell as a simple command using the &#8211;<code>c</code> option. The command and any arguments are concatenated, separated by spaces, after escaping each character (including white space) with a backslash (`\&#8217; ) except for alphanumerics, underscores, hyphens, and dollar signs. If no command is specified, an interactive shell is executed. Note that most shells behave differently when a command is specified as compared to an interactive session; consult the shell&#8217;s manual for details.</p>
<dt><code>-t </code><i>type , &#8211;</i><code>-type = </code><i>type</i></p>
<dd>Run the command with an SELinux security context that includes the specified <i>type</i> If no <i>type</i> is specified, the default type is derived from the role.</p>
<dt><code>-U </code><i>user , &#8211;</i><code>-other-user = </code><i>user</i></p>
<dd>Used in conjunction with the &#8211;<code>l</code> option to list the privileges for <i>user</i> instead of for the invoking user. The security policy may restrict listing other users&#8217; privileges. The <i>sudoers</i> policy only allows root or a user with the <code>ALL</code> privilege on the current host to use this option.</p>
<dt><code>-T </code><i>timeout , &#8211;</i><code>-command-timeout = </code><i>timeout</i></p>
<dd>Used to set a timeout for the command. If the timeout expires before the command has exited, the command will be terminated. The security policy may restrict the ability to set command timeouts. The <i>sudoers</i> policy requires that user-specified timeouts be explicitly enabled.</p>
<dt><code>-u </code><i>user , &#8211;</i><code>-user = </code><i>user</i></p>
<dd>Run the command as a user other than the default target user (usually <i>root )</i> The <i>user</i> may be either a user name or a numeric user-ID (UID) prefixed with the `#&#8217; character (e.g., <code>#0</code> for UID 0). When running commands as a UID, many shells require that the `#&#8217; be escaped with a backslash (`\&#8217; ) Some security policies may restrict UIDs to those listed in the password database. The <i>sudoers</i> policy allows UIDs that are not in the password database as long as the <i>targetpw</i> option is not set. Other security policies may not support this.</p>
<dt><code>-V , -version</code></p>
<dd>Print the <code>sudo</code> version string as well as the version string of any configured plugins. If the invoking user is already root, the &#8211;<code>V</code> option will display the arguments passed to configure when <code>sudo</code> was built; plugins may display additional information such as default options.</p>
<dt><code>-v , -validate</code></p>
<dd>Update the user&#8217;s cached credentials, authenticating the user if necessary. For the <i>sudoers</i> plugin, this extends the <code>sudo</code> timeout for another <code>15</code> minutes by default, but does not run a command. Not all security policies support cached credentials.</p>
<dt><code>&#8211; </code></p>
<dd>The &#8211;<code>&#8211;</code> option indicates that <code>sudo</code> should stop processing command line arguments.</dl>
<p> Options that take a value may only be specified once unless otherwise indicated in the description. This is to help guard against problems caused by poorly written scripts that invoke <code>sudo</code> with user-controlled input. </p>
<p> Environment variables to be set for the command may also be passed on the command line in the form of <i>VAR </i><code>= </code><i>value</i> e.g., <code>LD_LIBRARY_PATH = /usr/local/pkg/lib </code> Variables passed on the command line are subject to restrictions imposed by the security policy plugin. The <i>sudoers</i> policy subjects variables passed on the command line to the same restrictions as normal environment variables with one important exception. If the <i>setenv</i> option is set in <i>sudoers</i> the command to be run has the <code>SETENV</code> tag set or the command matched is <code>ALL</code> the user may set variables that would otherwise be forbidden. See <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5) for more information.</p>
<h2>Command Execution</h2>
<p>When <code>sudo</code> executes a command, the security policy specifies the execution environment for the command. Typically, the real and effective user and group and IDs are set to match those of the target user, as specified in the password database, and the group vector is initialized based on the group database (unless the &#8211;<code>P</code> option was specified). </p>
<p> The following parameters may be specified by security policy: </p>
<ul>
<li> real and effective user-ID
<li> real and effective group-ID
<li> supplementary group-IDs
<li> the environment list
<li> current working directory
<li> file creation mode mask (umask)
<li> SELinux role and type
<li> scheduling priority (aka nice value) </ul>
<h3>Process model</h3>
<p>There are two distinct ways <code>sudo</code> can run a command. </p>
<p> If an I/O logging plugin is configured or if the security policy explicitly requests it, a new pseudo-terminal (&#8220;pty&#8221; ) is allocated and <a href="/docs/linux/man/2-fork/">fork</a>(2) is used to create a second <code>sudo</code> process, referred to as the <i>monitor</i> The <i>monitor</i> creates a new terminal session with itself as the leader and the pty as its controlling terminal, calls <a href="/docs/linux/man/2-fork/">fork</a>(2), sets up the execution environment as described above, and then uses the <a href="/docs/linux/man/2-execve/">execve</a>(2) system call to run the command in the child process. The <i>monitor</i> exists to relay job control signals between the user&#8217;s existing terminal and the pty the command is being run in. This makes it possible to suspend and resume the command. Without the monitor, the command would be in what POSIX terms an &#8220;orphaned process group&#8221; and it would not receive any job control signals from the kernel. When the command exits or is terminated by a signal, the <i>monitor</i> passes the command&#8217;s exit status to the main <code>sudo</code> process and exits. After receiving the command&#8217;s exit status, the main <code>sudo</code> passes the command&#8217;s exit status to the security policy&#8217;s close function and exits. </p>
<p> If no pty is used, <code>sudo</code> calls <a href="/docs/linux/man/2-fork/">fork</a>(2), sets up the execution environment as described above, and uses the <a href="/docs/linux/man/2-execve/">execve</a>(2) system call to run the command in the child process. The main <code>sudo</code> process waits until the command has completed, then passes the command&#8217;s exit status to the security policy&#8217;s close function and exits. As a special case, if the policy plugin does not define a close function, <code>sudo</code> will execute the command directly instead of calling <a href="/docs/linux/man/2-fork/">fork</a>(2) first. The <i>sudoers</i> policy plugin will only define a close function when I/O logging is enabled, a pty is required, an SELinux role is specified, the command has an associated timeout, or the <i>pam_session</i> or <i>pam_setcred</i> options are enabled. Note that <i>pam_session</i> and <i>pam_setcred</i> are enabled by default on systems using PAM. </p>
<p> On systems that use PAM, the security policy&#8217;s close function is responsible for closing the PAM session. It may also log the command&#8217;s exit status.</p>
<h3>Signal handling</h3>
<p>When the command is run as a child of the <code>sudo</code> process, <code>sudo</code> will relay signals it receives to the command. The <code>SIGINT</code> and <code>SIGQUIT</code> signals are only relayed when the command is being run in a new pty or when the signal was sent by a user process, not the kernel. This prevents the command from receiving <code>SIGINT</code> twice each time the user enters control-C. Some signals, such as <code>SIGSTOP</code> and <code>SIGKILL</code> cannot be caught and thus will not be relayed to the command. As a general rule, <code>SIGTSTP</code> should be used instead of <code>SIGSTOP</code> when you wish to suspend a command being run by <code>sudo.</code> </p>
<p> As a special case, <code>sudo</code> will not relay signals that were sent by the command it is running. This prevents the command from accidentally killing itself. On some systems, the <a href="/docs/linux/man/8-reboot/">reboot</a>(8) command sends <code>SIGTERM</code> to all non-system processes other than itself before rebooting the system. This prevents <code>sudo</code> from relaying the <code>SIGTERM</code> signal it received back to <a href="/docs/linux/man/8-reboot/">reboot</a>(8), which might then exit before the system was actually rebooted, leaving it in a half-dead state similar to single user mode. Note, however, that this check only applies to the command run by <code>sudo</code> and not any other processes that the command may create. As a result, running a script that calls <a href="/docs/linux/man/8-reboot/">reboot</a>(8) or <a href="/docs/linux/man/8-shutdown/">shutdown</a>(8) via <code>sudo</code> may cause the system to end up in this undefined state unless the <a href="/docs/linux/man/8-reboot/">reboot</a>(8) or <a href="/docs/linux/man/8-shutdown/">shutdown</a>(8) are run using the Fn exec family of functions instead of Fn system (which interposes a shell between the command and the calling process). </p>
<p> If no I/O logging plugins are loaded and the policy plugin has not defined a Fn close function, set a command timeout, or required that the command be run in a new pty, <code>sudo</code> may execute the command directly instead of running it as a child process.</p>
<h3>Plugins</h3>
<p>Plugins may be specified via <code>Plugin</code> directives in the sudo.conf5 file. They may be loaded as dynamic shared objects (on systems that support them), or compiled directly into the <code>sudo</code> binary. If no sudo.conf5 file is present, or if it doesn&#8217;t contain any <code>Plugin</code> lines, <code>sudo</code> will use <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5) for the policy, auditing, and I/O logging plugins. See the sudo.conf5 manual for details of the /etc/sudo.conf file and the sudo_plugin5 manual for more information about the <code>sudo</code> plugin architecture.</p>
<h2>Exit Value</h2>
<p>Upon successful execution of a command, the exit status from <code>sudo</code> will be the exit status of the program that was executed. If the command terminated due to receipt of a signal, <code>sudo</code> will send itself the same signal that terminated the command. </p>
<p> If the &#8211;<code>l</code> option was specified without a command, <code>sudo</code> will exit with a value of 0 if the user is allowed to run <code>sudo</code> and they authenticated successfully (as required by the security policy). If a command is specified with the &#8211;<code>l</code> option, the exit value will only be 0 if the command is permitted by the security policy, otherwise it will be 1. </p>
<p> If there is an authentication failure, a configuration/permission problem, or if the given command cannot be executed, <code>sudo</code> exits with a value of 1. In the latter case, the error string is printed to the standard error. If <code>sudo</code> cannot <a href="/docs/linux/man/2-stat/">stat</a>(2) one or more entries in the user&#8217;s <code>PATH</code> an error is printed to the standard error. (If the directory does not exist or if it is not really a directory, the entry is ignored and no error is printed.) This should not happen under normal circumstances. The most common reason for <a href="/docs/linux/man/2-stat/">stat</a>(2) to return &#8220;permission denied&#8221; is if you are running an automounter and one of the directories in your <code>PATH</code> is on a machine that is currently unreachable.</p>
<h2>Security Notes</h2>
<p><code>sudo</code> tries to be safe when executing external commands. </p>
<p> To prevent command spoofing, <code>sudo</code> checks &quot;.&quot; and &quot;&quot; (both denoting current directory) last when searching for a command in the user&#8217;s <code>PATH</code> (if one or both are in the <code>PATH )</code> Depending on the security policy, the user&#8217;s <code>PATH</code> environment variable may be modified, replaced, or passed unchanged to the program that <code>sudo</code> executes. </p>
<p> Users should <i>never</i> be granted <code>sudo</code> privileges to execute files that are writable by the user or that reside in a directory that is writable by the user. If the user can modify or replace the command there is no way to limit what additional commands they can run. </p>
<p> Please note that <code>sudo</code> will normally only log the command it explicitly runs. If a user runs a command such as <code>sudo su</code> or <code>sudo sh</code> subsequent commands run from that shell are not subject to <code>sudo &#8216;s</code> security policy. The same is true for commands that offer shell escapes (including most editors). If I/O logging is enabled, subsequent commands will have their input and/or output logged, but there will not be traditional logs for those commands. Because of this, care must be taken when giving users access to commands via <code>sudo</code> to verify that the command does not inadvertently give the user an effective root shell. For information on ways to address this, please see the <i>Preventing shell escapes</i> section in <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5). </p>
<p> To prevent the disclosure of potentially sensitive information, <code>sudo</code> disables core dumps by default while it is executing (they are re-enabled for the command that is run). This historical practice dates from a time when most operating systems allowed set-user-ID processes to dump core by default. To aid in debugging <code>sudo</code> crashes, you may wish to re-enable core dumps by setting &#8220;disable_coredump&#8221; to false in the sudo.conf5 file as follows: </p>
<blockquote>
<pre>Set disable_coredump false</pre>
</blockquote>
<p> See the sudo.conf5 manual for more information.</p>
<h2>Environment</h2>
<p><code>sudo</code> utilizes the following environment variables. The security policy has control over the actual content of the command&#8217;s environment.</p>
<dl>
<dt><code>EDITOR</code></p>
<dd>Default editor to use in &#8211;<code>e</code> (sudoedit) mode if neither <code>SUDO_EDITOR</code> nor <code>VISUAL</code> is set.</p>
<dt><code>MAIL</code></p>
<dd>Set to the mail spool of the target user when the &#8211;<code>i</code> option is specified, or when <i>env_reset</i> is enabled in <i>sudoers</i> (unless <code>MAIL</code> is present in the <i>env_keep</i> list).</p>
<dt><code>HOME</code></p>
<dd>Set to the home directory of the target user when the &#8211;<code>i</code> or &#8211;<code>H</code> options are specified, when the &#8211;<code>s</code> option is specified and <i>set_home</i> is set in <i>sudoers</i> when <i>always_set_home</i> is enabled in <i>sudoers</i> or when <i>env_reset</i> is enabled in <i>sudoers</i> and <i>HOME</i> is not present in the <i>env_keep</i> list.</p>
<dt><code>LOGNAME</code></p>
<dd>Set to the login name of the target user when the &#8211;<code>i</code> option is specified, when the <i>set_logname</i> option is enabled in <i>sudoers</i> or when the <i>env_reset</i> option is enabled in <i>sudoers</i> (unless <code>LOGNAME</code> is present in the <i>env_keep</i> list).</p>
<dt><code>PATH</code></p>
<dd>May be overridden by the security policy.</p>
<dt><code>SHELL</code></p>
<dd>Used to determine shell to run with &#8211;<code>s</code> option.</p>
<dt><code>SUDO_ASKPASS</code></p>
<dd>Specifies the path to a helper program used to read the password if no terminal is available or if the &#8211;<code>A</code> option is specified.</p>
<dt><code>SUDO_COMMAND</code></p>
<dd>Set to the command run by sudo, including command line arguments. The command line arguments are truncated at 4096 characters to prevent a potential execution error.</p>
<dt><code>SUDO_EDITOR</code></p>
<dd>Default editor to use in &#8211;<code>e</code> (sudoedit) mode.</p>
<dt><code>SUDO_GID</code></p>
<dd>Set to the group-ID of the user who invoked sudo.</p>
<dt><code>SUDO_PROMPT</code></p>
<dd>Used as the default password prompt unless the &#8211;<code>p</code> option was specified.</p>
<dt><code>SUDO_PS1</code></p>
<dd>If set, <code>PS1</code> will be set to its value for the program being run.</p>
<dt><code>SUDO_UID</code></p>
<dd>Set to the user-ID of the user who invoked sudo.</p>
<dt><code>SUDO_USER</code></p>
<dd>Set to the login name of the user who invoked sudo.</p>
<dt><code>USER</code></p>
<dd>Set to the same value as <code>LOGNAME</code> described above.</p>
<dt><code>VISUAL</code></p>
<dd>Default editor to use in &#8211;<code>e</code> (sudoedit) mode if <code>SUDO_EDITOR</code> is not set.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/sudo.conf </code></p>
<dd><code>sudo</code> front-end configuration</dl>
<h2>Examples</h2>
<p>Note: the following examples assume a properly configured security policy. </p>
<p> To get a file listing of an unreadable directory: </p>
<blockquote>
<pre>$ sudo ls /usr/local/protected</pre>
</blockquote>
<p> To list the home directory of user yaz on a machine where the file system holding ~yaz is not exported as root: </p>
<blockquote>
<pre>$ sudo -u yaz ls ~yaz</pre>
</blockquote>
<p> To edit the index.html file as user www: </p>
<blockquote>
<pre>$ sudoedit -u www ~www/htdocs/index.html</pre>
</blockquote>
<p> To view system logs only accessible to root and users in the adm group: </p>
<blockquote>
<pre>$ sudo -g adm more /var/log/syslog</pre>
</blockquote>
<p> To run an editor as jim with a different primary group: </p>
<blockquote>
<pre>$ sudoedit -u jim -g audio ~jim/sound.txt</pre>
</blockquote>
<p> To shut down a machine: </p>
<blockquote>
<pre>$ sudo shutdown -r +15 &quot;quick reboot&quot;</pre>
</blockquote>
<p> To make a usage listing of the directories in the /home partition. Note that this runs the commands in a sub-shell to make the <code>cd</code> and file redirection work. </p>
<blockquote>
<pre>$ sudo sh -c &quot;cd /home ; du -s * | sort -rn &gt; USAGE&quot;</pre>
</blockquote>
<h2>Diagnostics</h2>
<p>Error messages produced by <code>sudo</code> include:</p>
<dl>
<dt><code>editing files in a writable directory is not permitted</code></p>
<dd>By default, <code>sudoedit</code> does not permit editing a file when any of the parent directories are writable by the invoking user. This avoids a race condition that could allow the user to overwrite an arbitrary file. See the <i>sudoedit_checkdir</i> option in <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5) for more information.</p>
<dt><code>editing symbolic links is not permitted</code></p>
<dd>By default, <code>sudoedit</code> does not follow symbolic links when opening files. See the <i>sudoedit_follow</i> option in <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5) for more information.</p>
<dt><code>effective uid is not 0, is sudo installed setuid root?</code></p>
<dd><code>sudo</code> was not run with root privileges. The <code>sudo</code> binary must be owned by the root user and have the set-user-ID bit set. Also, it must not be located on a file system mounted with the `nosuid&#8217; option or on an NFS file system that maps uid 0 to an unprivileged uid.</p>
<dt><code>effective uid is not 0, is sudo on a file system with the &#8216;nosuid&#8217; option set or an NFS file system without root privileges?</code></p>
<dd><code>sudo</code> was not run with root privileges. The <code>sudo</code> binary has the proper owner and permissions but it still did not run with root privileges. The most common reason for this is that the file system the <code>sudo</code> binary is located on is mounted with the `nosuid&#8217; option or it is an NFS file system that maps uid 0 to an unprivileged uid.</p>
<dt><code>fatal error, unable to load plugins</code></p>
<dd>An error occurred while loading or initializing the plugins specified in sudo.conf5.</p>
<dt><code>invalid environment variable name</code></p>
<dd>One or more environment variable names specified via the &#8211;<code>E</code> option contained an equal sign (`=&#8217; ) The arguments to the &#8211;<code>E</code> option should be environment variable names without an associated value.</p>
<dt><code>no password was provided</code></p>
<dd>When <code>sudo</code> tried to read the password, it did not receive any characters. This may happen if no terminal is available (or the &#8211;<code>S</code> option is specified) and the standard input has been redirected from /dev/null</p>
<dt><code>a terminal is required to read the password</code></p>
<dd><code>sudo</code> needs to read the password but there is no mechanism available for it to do so. A terminal is not present to read the password from, <code>sudo</code> has not been configured to read from the standard input, the &#8211;<code>S</code> option was not used, and no askpass helper has been specified either via the sudo.conf5 file or the <code>SUDO_ASKPASS</code> environment variable.</p>
<dt><code>no writable temporary directory found</code></p>
<dd><code>sudoedit</code> was unable to find a usable temporary directory in which to store its intermediate files.</p>
<dt><code>The Do </code>no new privileges Dc flag is set, which prevents sudo from running as root.</p>
<dd><code>sudo</code> was run by a process that has the Linux &#8220;no new privileges&#8221; flag is set. This causes the set-user-ID bit to be ignored when running an executable, which will prevent <code>sudo</code> from functioning. The most likely cause for this is running <code>sudo</code> within a container that sets this flag. Check the documentation to see if it is possible to configure the container such that the flag is not set.</p>
<dt><code>sudo must be owned by uid 0 and have the setuid bit set</code></p>
<dd><code>sudo</code> was not run with root privileges. The <code>sudo</code> binary does not have the correct owner or permissions. It must be owned by the root user and have the set-user-ID bit set.</p>
<dt><code>sudoedit is not supported on this platform</code></p>
<dd>It is only possible to run <code>sudoedit</code> on systems that support setting the effective user-ID.</p>
<dt><code>timed out reading password</code></p>
<dd>The user did not enter a password before the password timeout (5 minutes by default) expired.</p>
<dt><code>you do not exist in the passwd database</code></p>
<dd>Your user-ID does not appear in the system passwd database.</p>
<dt><code>you may not specify environment variables in edit mode</code></p>
<dd>It is only possible to specify environment variables when running a command. When editing a file, the editor is run with the user&#8217;s environment unmodified.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-su/">su</a>(1), <a href="/docs/linux/man/2-stat/">stat</a>(2), login_cap3, <a href="/docs/linux/man/5-passwd/">passwd</a>(5), sudo.conf5, sudo_plugin5, <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5), sudoers_timestamp5, <a href="/docs/linux/man/8-sudoreplay/">sudoreplay</a>(8), <a href="/docs/linux/man/8-visudo/">visudo</a>(8)</p>
<h2>History</h2>
<p>See the HISTORY file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/history.html)">https://www.sudo.ws/history.html)</a> for a brief history of sudo.</p>
<h2>Authors</h2>
<p>Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<blockquote><p> An Todd C. Miller </p></blockquote>
<p> See the CONTRIBUTORS file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/contributors.html)">https://www.sudo.ws/contributors.html)</a> for an exhaustive list of people who have contributed to <code>sudo.</code></p>
<h2>Caveats</h2>
<p>There is no easy way to prevent a user from gaining a root shell if that user is allowed to run arbitrary commands via <code>sudo.</code> Also, many programs (such as editors) allow the user to run commands via shell escapes, thus avoiding <code>sudo &#8216;s</code> checks. However, on most systems it is possible to prevent shell escapes with the <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5) plugin&#8217;s <i>noexec</i> functionality. </p>
<p> It is not meaningful to run the <code>cd</code> command directly via sudo, e.g., </p>
<blockquote>
<pre>$ sudo cd /usr/local/protected</pre>
</blockquote>
<p> since when the command exits the parent process (your shell) will still be the same. Please see the Sx EXAMPLES section for more information. </p>
<p> Running shell scripts via <code>sudo</code> can expose the same kernel bugs that make set-user-ID shell scripts unsafe on some operating systems (if your OS has a /dev/fd/ directory, set-user-ID shell scripts are generally safe).</p>
<h2>Bugs</h2>
<p>If you feel you have found a bug in <code>sudo,</code> please submit a bug report at <a rel="nofollow" href="https://bugzilla.sudo.ws/">https://bugzilla.sudo.ws/</a></p>
<h2>Support</h2>
<p>Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="https://www.sudo.ws/mailman/listinfo/sudo-users">https://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.</p>
<h2>Disclaimer</h2>
<p><code>sudo</code> is provided &#8220;AS IS&#8221; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the LICENSE file distributed with <code>sudo</code> or <a rel="nofollow" href="https://www.sudo.ws/license.html">https://www.sudo.ws/license.html</a> for complete details.</p>
