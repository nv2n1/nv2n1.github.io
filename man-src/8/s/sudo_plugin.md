---
title: "sudo_plugin(8)"
name: "sudo_plugin"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sudo_plugin/"
description: "sudo_plugin – Sudo Plugin API"
---

<p>Sudo 1.9.9</p>
<h2>Name</h2>
<p><code>sudo_plugin</code> &#8211; Sudo Plugin API</p>
<h2>Description</h2>
<p>Starting with version 1.8, <code>sudo</code> supports a plugin API for policy and session logging. Plugins may be compiled as dynamic shared objects (the default on systems that support them) or compiled statically into the <code>sudo</code> binary itself. By default, the <code>sudoers</code> plugin provides audit, security policy and I/O logging capabilities. Via the plugin API, <code>sudo</code> can be configured to use alternate plugins provided by third parties. The plugins to be used are specified in the sudo.conf5 file. The API is versioned with a major and minor number. The minor version number is incremented when additions are made. The major number is incremented when incompatible changes are made. A plugin should be check the version passed to it and make sure that the major version matches. The plugin API is defined by the <code>sudo_plugin.h</code> header file.</p>
<h3>Policy plugin API</h3>
<p>A policy plugin must declare and populate a <code>policy_plugin</code> struct in the global scope. This structure contains pointers to the functions that implement the <code>sudo</code> policy checks. The name of the symbol should be specified in sudo.conf5 along with a path to the plugin so that <code>sudo</code> can load it. </p>
<pre>struct policy_plugin {
#define SUDO_POLICY_PLUGIN 1
 unsigned int type; /* always SUDO_POLICY_PLUGIN */
 unsigned int version; /* always SUDO_API_VERSION */
 int (*open)(unsigned int version, sudo_conv_t conversation,
 sudo_printf_t plugin_printf, char * const settings[],
 char * const user_info[], char * const user_env[],
 char * const plugin_options[], const char **errstr);
 void (*close)(int exit_status, int error);
 int (*show_version)(int verbose);
 int (*check_policy)(int argc, char * const argv[],
 char *env_add[], char **command_info[],
 char **argv_out[], char **user_env_out[], const char **errstr);
 int (*list)(int argc, char * const argv[], int verbose,
 const char *list_user, const char **errstr);
 int (*validate)(const char **errstr);
 void (*invalidate)(int remove);
 int (*init_session)(struct passwd *pwd, char **user_env[],
 const char **errstr);
 void (*register_hooks)(int version,
 int (*register_hook)(struct sudo_hook *hook));
 void (*deregister_hooks)(int version,
 int (*deregister_hook)(struct sudo_hook *hook));
 struct sudo_plugin_event * (*event_alloc)(void);
};</pre>
<p>The policy_plugin struct has the following fields:</p>
<dl>
<dt><code>type</code></p>
<dd>The <code>type</code> field should always be set to SUDO_POLICY_PLUGIN.</p>
<dt><code>version</code></p>
<dd>The <code>version</code> field should be set to <code>SUDO_API_VERSION</code> This allows <code>sudo</code> to determine the API version the plugin was built against.</p>
<dt><code>open</code></p>
<dd>
<pre>int (*open)(unsigned int version, sudo_conv_t conversation,
 sudo_printf_t plugin_printf, char * const settings[],
 char * const user_info[], char * const user_env[],
 char * const plugin_options[], const char **errstr);</pre>
<p>Returns 1 on success, 0 on failure, -1 if a general error occurred, or -2 if there was a usage error. In the latter case, <code>sudo</code> will print a usage message before it exits. If an error occurs, the plugin may optionally call the Fn conversation or Fn plugin_printf function with <code>SUDO_CONF_ERROR_MSG</code> to present additional error information to the user. The function arguments are as follows:</p>
<dl>
<dt><code>version</code></p>
<dd>The version passed in by <code>sudo</code> allows the plugin to determine the major and minor version number of the plugin API supported by <code>sudo</code></p>
<dt><code>conversation</code></p>
<dd>A pointer to the Fn conversation function that can be used by the plugin to interact with the user (see Sx Conversation API for details). Returns 0 on success and -1 on failure.</p>
<dt><code>plugin_printf</code></p>
<dd>A pointer to a Fn printf Ns -style function that may be used to display informational or error messages (see Sx Conversation API for details). Returns the number of characters printed on success and -1 on failure.</p>
<dt><code>settings</code></p>
<dd>A vector of user-supplied <code>sudo</code> settings in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. These settings correspond to options the user specified when running <code>sudo</code> As such, they will only be present when the corresponding option has been specified on the command line. When parsing <i>settings</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. The following values may be set by <code>sudo</code></p>
<dl>
<dt><code>bsdauth_type=string</code></p>
<dd>Authentication type, if specified by the &#8211;<code>a</code> option, to use on systems where BSD authentication is supported.</p>
<dt><code>closefrom=number</code></p>
<dd>If specified, the user has requested via the &#8211;<code>C</code> option that <code>sudo</code> close all files descriptors with a value of <i>number</i> or higher. The plugin may optionally pass this, or another value, back in the <i>command_info</i> list.</p>
<dt><code>cmnd_chroot=string</code></p>
<dd>The root directory (see <a href="/docs/linux/man/2-chroot/">chroot</a>(2)) to run the command in, as specified by the user via the &#8211;<code>R</code> option. The plugin may ignore or restrict the user&#8217;s ability to specify a new root directory. Only available starting with API version 1.16.</p>
<dt><code>cmnd_cwd=string</code></p>
<dd>The working directory to run the command in, as specified by the user via the &#8211;<code>D</code> option. The plugin may ignore or restrict the user&#8217;s ability to specify a new working directory. Only available starting with API version 1.16.</p>
<dt><code>debug_flags=string</code></p>
<dd>A debug file path name followed by a space and a comma-separated list of debug flags that correspond to the plugin&#8217;s <code>Debug</code> entry in sudo.conf5, if there is one. The flags are passed to the plugin exactly as they appear in sudo.conf5. The syntax used by <code>sudo</code> and the <code>sudoers</code> plugin is <i>subsystem </i><code>@ </code><i>priority</i> but a plugin is free to use a different format so long as it does not include a comma (`,&#8217; ) Prior to <code>sudo</code> 1.8.12, there was no way to specify plugin-specific <i>debug_flags</i> so the value was always the same as that used by the <code>sudo</code> front-end and did not include a path name, only the flags themselves. As of version 1.7 of the plugin interface, <code>sudo</code> will only pass <i>debug_flags</i> if sudo.conf5 contains a plugin-specific <code>Debug</code> entry.</p>
<dt><code>ignore_ticket=bool</code></p>
<dd>Set to true if the user specified the &#8211;<code>k</code> option along with a command, indicating that the user wishes to ignore any cached authentication credentials. <i>implied_shell</i> to true. This allows <code>sudo</code> with no arguments to be used similarly to <a href="/docs/linux/man/1-su/">su</a>(1). If the plugin does not to support this usage, it may return a value of -2 from the Fn check_policy function, which will cause <code>sudo</code> to print a usage message and exit.</p>
<dt><code>implied_shell=bool</code></p>
<dd>If the user does not specify a program on the command line, <code>sudo</code> will pass the plugin the path to the user&#8217;s shell and set</p>
<dt><code>login_class=string</code></p>
<dd>BSD login class to use when setting resource limits and nice value, if specified by the &#8211;<code>c</code> option.</p>
<dt><code>login_shell=bool</code></p>
<dd>Set to true if the user specified the &#8211;<code>i</code> option, indicating that the user wishes to run a login shell.</p>
<dt><code>max_groups=int</code></p>
<dd>The maximum number of groups a user may belong to. This will only be present if there is a corresponding setting in sudo.conf5.</p>
<dt><code>network_addrs=list</code></p>
<dd>A space-separated list of IP network addresses and netmasks in the form &#8220;addr/netmask&#8221; e.g., &#8220;192.168.1.2/255.255.255.0&#8221; The address and netmask pairs may be either IPv4 or IPv6, depending on what the operating system supports. If the address contains a colon (`:&#8217; ) it is an IPv6 address, else it is IPv4.</p>
<dt><code>noninteractive=bool</code></p>
<dd>Set to true if the user specified the &#8211;<code>n</code> option, indicating that <code>sudo</code> should operate in non-interactive mode. The plugin may reject a command run in non-interactive mode if user interaction is required.</p>
<dt><code>plugin_dir=string</code></p>
<dd>The default plugin directory used by the <code>sudo</code> front-end. This is the default directory set at compile time and may not correspond to the directory the running plugin was loaded from. It may be used by a plugin to locate support files.</p>
<dt><code>plugin_path=string</code></p>
<dd>The path name of plugin loaded by the <code>sudo</code> front-end. The path name will be a fully-qualified unless the plugin was statically compiled into <code>sudo</code></p>
<dt><code>preserve_environment=bool</code></p>
<dd>Set to true if the user specified the &#8211;<code>E</code> option, indicating that the user wishes to preserve the environment.</p>
<dt><code>preserve_groups=bool</code></p>
<dd>Set to true if the user specified the &#8211;<code>P</code> option, indicating that the user wishes to preserve the group vector instead of setting it based on the runas user.</p>
<dt><code>progname=string</code></p>
<dd>The command name that sudo was run as, typically &#8220;sudo&#8221; or &#8220;sudoedit&#8221;</p>
<dt><code>prompt=string</code></p>
<dd>The prompt to use when requesting a password, if specified via the &#8211;<code>p</code> option.</p>
<dt><code>remote_host=string</code></p>
<dd>The name of the remote host to run the command on, if specified via the &#8211;<code>h</code> option. Support for running the command on a remote host is meant to be implemented via a helper program that is executed in place of the user-specified command. The <code>sudo</code> front-end is only capable of executing commands on the local host. Only available starting with API version 1.4.</p>
<dt><code>run_shell=bool</code></p>
<dd>Set to true if the user specified the &#8211;<code>s</code> option, indicating that the user wishes to run a shell.</p>
<dt><code>runas_group=string</code></p>
<dd>The group name or group-ID to run the command as, if specified via the &#8211;<code>g</code> option.</p>
<dt><code>runas_user=string</code></p>
<dd>The user name or user-ID to run the command as, if specified via the &#8211;<code>u</code> option.</p>
<dt><code>selinux_role=string</code></p>
<dd>SELinux role to use when executing the command, if specified by the &#8211;<code>r</code> option.</p>
<dt><code>selinux_type=string</code></p>
<dd>SELinux type to use when executing the command, if specified by the &#8211;<code>t</code> option.</p>
<dt><code>set_home=bool</code></p>
<dd>Set to true if the user specified the &#8211;<code>H</code> option. If true, set the <code>HOME</code> environment variable to the target user&#8217;s home directory.</p>
<dt><code>sudoedit=bool</code></p>
<dd>Set to true when the &#8211;<code>e</code> option is specified or if invoked as <code>sudoedit</code> The plugin shall substitute an editor into <i>argv</i> in the Fn check_policy function or return -2 with a usage error if the plugin does not support <i>sudoedit</i> For more information, see the <i>check_policy</i> section.</p>
<dt><code>timeout=string</code></p>
<dd>Command timeout specified by the user via the &#8211;<code>T</code> option. Not all plugins support command timeouts and the ability of the user to set a timeout may be restricted by policy. The format of the timeout string is plugin-specific.</dl>
<p> Additional settings may be added in the future so the plugin should silently ignore settings that it does not recognize.</p>
<dt><code>user_info</code></p>
<dd>A vector of information about the user running the command in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. When parsing <i>user_info</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. The following values may be set by <code>sudo</code></p>
<dl>
<dt><code>cols=int</code></p>
<dd>The number of columns the user&#8217;s terminal supports. If there is no terminal device available, a default value of 80 is used.</p>
<dt><code>cwd=string</code></p>
<dd>The user&#8217;s current working directory.</p>
<dt><code>egid=gid_t</code></p>
<dd>The effective group-ID of the user invoking <code>sudo</code></p>
<dt><code>euid=uid_t</code></p>
<dd>The effective user-ID of the user invoking <code>sudo</code></p>
<dt><code>gid=gid_t</code></p>
<dd>The real group-ID of the user invoking <code>sudo</code></p>
<dt><code>groups=list</code></p>
<dd>The user&#8217;s supplementary group list formatted as a string of comma-separated group-IDs.</p>
<dt><code>host=string</code></p>
<dd>The local machine&#8217;s hostname as returned by the <a href="/docs/linux/man/2-gethostname/">gethostname</a>(2) system call.</p>
<dt><code>lines=int</code></p>
<dd>The number of lines the user&#8217;s terminal supports. If there is no terminal device available, a default value of 24 is used.</p>
<dt><code>pgid=int</code></p>
<dd>The ID of the process group that the running <code>sudo</code> process is a member of. Only available starting with API version 1.2.</p>
<dt><code>pid=int</code></p>
<dd>The process ID of the running <code>sudo</code> process. Only available starting with API version 1.2.</p>
<dt><code>ppid=int</code></p>
<dd>The parent process ID of the running <code>sudo</code> process. Only available starting with API version 1.2.</p>
<dt><code>rlimit_as=soft,hard</code></p>
<dd>The maximum size to which the process&#8217;s address space may grow (in bytes), if supported by the operating system. The soft and hard limits are separated by a comma. A value of &#8220;infinity&#8221; indicates that there is no limit. Only available starting with API version 1.16.</p>
<dt><code>rlimit_core=soft,hard</code></p>
<dd>The largest size core dump file that may be created (in bytes). The soft and hard limits are separated by a comma. A value of &#8220;infinity&#8221; indicates that there is no limit. Only available starting with API version 1.16.</p>
<dt><code>rlimit_cpu=soft,hard</code></p>
<dd>The maximum amount of CPU time that the process may use (in seconds). The soft and hard limits are separated by a comma. A value of &#8220;infinity&#8221; indicates that there is no limit. Only available starting with API version 1.16.</p>
<dt><code>rlimit_data=soft,hard</code></p>
<dd>The maximum size of the data segment for the process (in bytes). The soft and hard limits are separated by a comma. A value of &#8220;infinity&#8221; indicates that there is no limit. Only available starting with API version 1.16.</p>
<dt><code>rlimit_fsize=soft,hard</code></p>
<dd>The largest size file that the process may create (in bytes). The soft and hard limits are separated by a comma. A value of &#8220;infinity&#8221; indicates that there is no limit. Only available starting with API version 1.16.</p>
<dt><code>rlimit_locks=soft,hard</code></p>
<dd>The maximum number of locks that the process may establish, if supported by the operating system. The soft and hard limits are separated by a comma. A value of &#8220;infinity&#8221; indicates that there is no limit. Only available starting with API version 1.16.</p>
<dt><code>rlimit_memlock=soft,hard</code></p>
<dd>The maximum size that the process may lock in memory (in bytes), if supported by the operating system. The soft and hard limits are separated by a comma. A value of &#8220;infinity&#8221; indicates that there is no limit. Only available starting with API version 1.16.</p>
<dt><code>rlimit_nofile=soft,hard</code></p>
<dd>The maximum number of files that the process may have open. The soft and hard limits are separated by a comma. A value of &#8220;infinity&#8221; indicates that there is no limit. Only available starting with API version 1.16.</p>
<dt><code>rlimit_nproc=soft,hard</code></p>
<dd>The maximum number of processes that the user may run simultaneously. The soft and hard limits are separated by a comma. A value of &#8220;infinity&#8221; indicates that there is no limit. Only available starting with API version 1.16.</p>
<dt><code>rlimit_rss=soft,hard</code></p>
<dd>The maximum size to which the process&#8217;s resident set size may grow (in bytes). The soft and hard limits are separated by a comma. A value of &#8220;infinity&#8221; indicates that there is no limit. Only available starting with API version 1.16.</p>
<dt><code>rlimit_stack=soft,hard</code></p>
<dd>The maximum size to which the process&#8217;s stack may grow (in bytes). The soft and hard limits are separated by a comma. A value of &#8220;infinity&#8221; indicates that there is no limit. Only available starting with API version 1.16.</p>
<dt><code>sid=int</code></p>
<dd>The session ID of the running <code>sudo</code> process or 0 if <code>sudo</code> is not part of a POSIX job control session. Only available starting with API version 1.2.</p>
<dt><code>tcpgid=int</code></p>
<dd>The ID of the foreground process group associated with the terminal device associated with the <code>sudo</code> process or 0 if there is no terminal present. Only available starting with API version 1.2.</p>
<dt><code>tty=string</code></p>
<dd>The path to the user&#8217;s terminal device. If the user has no terminal device associated with the session, the value will be empty, as in &#8220;<code>tty=</code> &#8221;</p>
<dt><code>uid=uid_t</code></p>
<dd>The real user-ID of the user invoking <code>sudo</code></p>
<dt><code>umask=octal</code></p>
<dd>The invoking user&#8217;s file creation mask. Only available starting with API version 1.10.</p>
<dt><code>user=string</code></p>
<dd>The name of the user invoking <code>sudo</code></dl>
<dt><code>user_env</code></p>
<dd>The user&#8217;s environment in the form of a <code>NULL -terminated vector of</code> &#8220;name=value&#8221; strings. When parsing <i>user_env</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might.</p>
<dt><code>plugin_options</code></p>
<dd>Any (non-comment) strings immediately after the plugin path are passed as arguments to the plugin. These arguments are split on a white space boundary and are passed to the plugin in the form of a <code>NULL -terminated</code> array of strings. If no arguments were specified, <i>plugin_options</i> will be the <code>NULL</code> pointer. NOTE: the <i>plugin_options</i> parameter is only available starting with API version 1.2. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using <i>plugin_options</i> Failure to do so may result in a crash.</p>
<dt><code>errstr</code></p>
<dd>If the Fn open function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</dl>
<dt><code>close</code></p>
<dd>
<pre>void (*close)(int exit_status, int error);</pre>
<p>The Fn close function is called when <code>sudo</code> is finished, shortly before it exits. Starting with API version 1.15, Fn close is called regardless of whether or not a command was actually executed. This makes it possible for plugins to perform cleanup even when a command was not run. It is not possible to tell whether a command was run based solely on the arguments passed to the Fn close function. To determine if a command was actually run, the plugin must keep track of whether or not the Fn check_policy function returned successfully. The function arguments are as follows:</p>
<dl>
<dt><code>exit_status</code></p>
<dd>The command&#8217;s exit status, as returned by the <a href="/docs/linux/man/2-wait/">wait</a>(2) system call, or zero if no command was run. The value of <code>exit_status</code> is undefined if <code>error</code> is non-zero.</p>
<dt><code>error</code></p>
<dd>If the command could not be executed, this is set to the value of <code>errno</code> set by the <a href="/docs/linux/man/2-execve/">execve</a>(2) system call. The plugin is responsible for displaying error information via the Fn conversation or Fn plugin_printf function. If the command was successfully executed, the value of <code>error</code> is zero.</dl>
<p> If no Fn close function is defined, no I/O logging plugins are loaded, and neither the <i>timeout</i> not <i>use_pty</i> options are set in the <code>command_info</code> list, the <code>sudo</code> front-end may execute the command directly instead of running it as a child process.</p>
<dt><code>show_version</code></p>
<dd>
<pre>int (*show_version)(int verbose);</pre>
<p>The Fn show_version function is called by <code>sudo</code> when the user specifies the &#8211;<code>V</code> option. The plugin may display its version information to the user via the Fn conversation or Fn plugin_printf function using <code>SUDO_CONV_INFO_MSG</code> If the user requests detailed version information, the verbose flag will be set. </p>
<pre><code>Returns 1 on success, 0 on failure, -1 if a general error occurred,
    or -2 if there was a usage error, although the return value is currently ignored.check_policy

                                      int(*check_policy)(int argc, char *const argv[], char *env_add[], char **command_info[], char **argv_out[], char **user_env_out[], const char **errstr);</code></pre>
<p> The Fn check_policy function is called by <code>sudo</code> to determine whether the user is allowed to run the specified commands. If the <i>sudoedit</i> option was enabled in the <i>settings</i> array passed to the Fn open function, the user has requested <i>sudoedit</i> mode. <i>sudoedit</i> is a mechanism for editing one or more files where an editor is run with the user&#8217;s credentials instead of with elevated privileges. <code>sudo</code> achieves this by creating user-writable temporary copies of the files to be edited and then overwriting the originals with the temporary copies after editing is complete. If the plugin supports <i>sudoedit</i> it should choose the editor to be used, potentially from a variable in the user&#8217;s environment, such as <code>EDITOR</code> and include it in <i>argv_out</i> (note that environment variables may include command line options). The files to be edited should be copied from <i>argv</i> into <i>argv_out</i> separated from the editor and its arguments by a &#8220;<code>&#8212;</code> &#8221; element. The &#8220;<code>&#8212;</code> &#8221; will be removed by <code>sudo</code> before the editor is executed. The plugin should also set <i>sudoedit=true</i> in the <i>command_info</i> list. The Fn check_policy function returns 1 if the command is allowed, 0 if not allowed, -1 for a general error, or -2 for a usage error or if <i>sudoedit</i> was specified but is unsupported by the plugin. In the latter case, <code>sudo</code> will print a usage message before it exits. If an error occurs, the plugin may optionally call the Fn conversation or Fn plugin_printf function with <code>SUDO_CONF_ERROR_MSG</code> to present additional error information to the user. The function arguments are as follows:</p>
<dl>
<dt><code>argc</code></p>
<dd>The number of elements in <i>argv</i> not counting the final <code>NULL</code> pointer.</p>
<dt><code>argv</code></p>
<dd>The argument vector describing the command the user wishes to run, in the same form as what would be passed to the <a href="/docs/linux/man/2-execve/">execve</a>(2) system call. The vector is terminated by a <code>NULL</code> pointer.</p>
<dt><code>env_add</code></p>
<dd>Additional environment variables specified by the user on the command line in the form of a <code>NULL -terminated</code> vector of &#8220;name=value&#8221; strings. The plugin may reject the command if one or more variables are not allowed to be set, or it may silently ignore such variables. When parsing <i>env_add</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might.</p>
<dt><code>command_info</code></p>
<dd>Information about the command being run in the form of &#8220;name=value&#8221; strings. These values are used by <code>sudo</code> to set the execution environment when running a command. The plugin is responsible for creating and populating the vector, which must be terminated with a <code>NULL</code> pointer. The following values are recognized by <code>sudo</code></p>
<dl>
<dt><code>chroot=string</code></p>
<dd>The root directory to use when running the command.</p>
<dt><code>closefrom=number</code></p>
<dd>If specified, <code>sudo</code> will close all files descriptors with a value of <i>number</i> or higher.</p>
<dt><code>command=string</code></p>
<dd>Fully qualified path to the command to be executed.</p>
<dt><code>cwd=string</code></p>
<dd>The current working directory to change to when executing the command. If <code>sudo</code> is unable to change to the new working directory, the command will not be run unless <i>cwd_optional</i> is also set (see below).</p>
<dt><code>cwd_optional=bool</code></p>
<dd>If enabled, <code>sudo</code> will treat an inability to change to the new working directory as a non-fatal error. This setting has no effect unless <i>cwd</i> is also set.</p>
<dt><code>exec_background=bool</code></p>
<dd>By default, <code>sudo</code> runs a command as the foreground process as long as <code>sudo</code> itself is running in the foreground. When <i>exec_background</i> is enabled and the command is being run in a pseudo-terminal (due to I/O logging or the <i>use_pty</i> setting), the command will be run as a background process. Attempts to read from the controlling terminal (or to change terminal settings) will result in the command being suspended with the <code>SIGTTIN</code> signal (or <code>SIGTTOU</code> in the case of terminal settings). If this happens when <code>sudo</code> is a foreground process, the command will be granted the controlling terminal and resumed in the foreground with no user intervention required. The advantage of initially running the command in the background is that <code>sudo</code> need not read from the terminal unless the command explicitly requests it. Otherwise, any terminal input must be passed to the command, whether it has required it or not (the kernel buffers terminals so it is not possible to tell whether the command really wants the input). This is different from historic <i>sudo</i> behavior or when the command is not being run in a pseudo-terminal. For this to work seamlessly, the operating system must support the automatic restarting of system calls. Unfortunately, not all operating systems do this by default, and even those that do may have bugs. For example, macOS fails to restart the Fn tcgetattr and Fn tcsetattr system calls (this is a bug in macOS). Furthermore, because this behavior depends on the command stopping with the <code>SIGTTIN</code> or <code>SIGTTOU</code> signals, programs that catch these signals and suspend themselves with a different signal (usually <code>SIGTOP</code> will not be automatically foregrounded. Some versions of the linux <a href="/docs/linux/man/1-su/">su</a>(1) command behave this way. Because of this, a plugin should not set <i>exec_background</i> unless it is explicitly enabled by the administrator and there should be a way to enabled or disable it on a per-command basis. This setting has no effect unless I/O logging is enabled or <i>use_pty</i> is enabled.</p>
<dt><code>execfd=number</code></p>
<dd>If specified, <code>sudo</code> will use the <a href="/docs/linux/man/2-fexecve/">fexecve</a>(2) system call to execute the command instead of <a href="/docs/linux/man/2-execve/">execve</a>(2). The specified <i>number</i> must refer to an open file descriptor.</p>
<dt><code>iolog_compress=bool</code></p>
<dd>Set to true if the I/O logging plugins, if any, should compress the log data. This is a hint to the I/O logging plugin which may choose to ignore it.</p>
<dt><code>iolog_group=string</code></p>
<dd>The group that will own newly created I/O log files and directories. This is a hint to the I/O logging plugin which may choose to ignore it.</p>
<dt><code>iolog_mode=octal</code></p>
<dd>The file permission mode to use when creating I/O log files and directories. This is a hint to the I/O logging plugin which may choose to ignore it.</p>
<dt><code>iolog_user=string</code></p>
<dd>The user that will own newly created I/O log files and directories. This is a hint to the I/O logging plugin which may choose to ignore it.</p>
<dt><code>iolog_path=string</code></p>
<dd>Fully qualified path to the file or directory in which I/O log is to be stored. This is a hint to the I/O logging plugin which may choose to ignore it. If no I/O logging plugin is loaded, this setting has no effect.</p>
<dt><code>iolog_stdin=bool</code></p>
<dd>Set to true if the I/O logging plugins, if any, should log the standard input if it is not connected to a terminal device. This is a hint to the I/O logging plugin which may choose to ignore it.</p>
<dt><code>iolog_stdout=bool</code></p>
<dd>Set to true if the I/O logging plugins, if any, should log the standard output if it is not connected to a terminal device. This is a hint to the I/O logging plugin which may choose to ignore it.</p>
<dt><code>iolog_stderr=bool</code></p>
<dd>Set to true if the I/O logging plugins, if any, should log the standard error if it is not connected to a terminal device. This is a hint to the I/O logging plugin which may choose to ignore it.</p>
<dt><code>iolog_ttyin=bool</code></p>
<dd>Set to true if the I/O logging plugins, if any, should log all terminal input. This only includes input typed by the user and not from a pipe or redirected from a file. This is a hint to the I/O logging plugin which may choose to ignore it.</p>
<dt><code>iolog_ttyout=bool</code></p>
<dd>Set to true if the I/O logging plugins, if any, should log all terminal output. This only includes output to the screen, not output to a pipe or file. This is a hint to the I/O logging plugin which may choose to ignore it.</p>
<dt><code>login_class=string</code></p>
<dd>BSD login class to use when setting resource limits and nice value (optional). This option is only set on systems that support login classes.</p>
<dt><code>nice=int</code></p>
<dd>Nice value (priority) to use when executing the command. The nice value, if specified, overrides the priority associated with the <i>login_class</i> on BSD systems.</p>
<dt><code>noexec=bool</code></p>
<dd>If set, prevent the command from executing other programs.</p>
<dt><code>preserve_fds=list</code></p>
<dd>A comma-separated list of file descriptors that should be preserved, regardless of the value of the <i>closefrom</i> setting. Only available starting with API version 1.5.</p>
<dt><code>preserve_groups=bool</code></p>
<dd>If set, <code>sudo</code> will preserve the user&#8217;s group vector instead of initializing the group vector based on <code>runas_user</code></p>
<dt><code>rlimit_as=soft,hard</code></p>
<dd>The maximum size to which the process&#8217;s address space may grow (in bytes), if supported by the operating system. The soft and hard limits are separated by a comma. If only a single value is specified, both the hard and soft limits are set. A value of &#8220;infinity&#8221; indicates that there is no limit. A value of &#8220;user&#8221; will cause the invoking user&#8217;s resource limit to be preserved. A value of &#8220;default&#8221; will cause the target user&#8217;s default resource limit to be used on systems that allow per-user resource limits to be configured. Only available starting with API version 1.17.</p>
<dt><code>rlimit_core=soft,hard</code></p>
<dd>The largest size core dump file that may be created (in bytes). The soft and hard limits are separated by a comma. If only a single value is specified, both the hard and soft limits are set. A value of &#8220;infinity&#8221; indicates that there is no limit. A value of &#8220;user&#8221; will cause the invoking user&#8217;s resource limit to be preserved. A value of &#8220;default&#8221; will cause the target user&#8217;s default resource limit to be used on systems that allow per-user resource limits to be configured. Only available starting with API version 1.17.</p>
<dt><code>rlimit_cpu=soft,hard</code></p>
<dd>The maximum amount of CPU time that the process may use (in seconds). The soft and hard limits are separated by a comma. If only a single value is specified, both the hard and soft limits are set. A value of &#8220;infinity&#8221; indicates that there is no limit. A value of &#8220;user&#8221; will cause the invoking user&#8217;s resource limit to be preserved. A value of &#8220;default&#8221; will cause the target user&#8217;s default resource limit to be used on systems that allow per-user resource limits to be configured. Only available starting with API version 1.17.</p>
<dt><code>rlimit_data=soft,hard</code></p>
<dd>The maximum size of the data segment for the process (in bytes). The soft and hard limits are separated by a comma. If only a single value is specified, both the hard and soft limits are set. A value of &#8220;infinity&#8221; indicates that there is no limit. A value of &#8220;user&#8221; will cause the invoking user&#8217;s resource limit to be preserved. A value of &#8220;default&#8221; will cause the target user&#8217;s default resource limit to be used on systems that allow per-user resource limits to be configured. Only available starting with API version 1.17.</p>
<dt><code>rlimit_fsize=soft,hard</code></p>
<dd>The largest size file that the process may create (in bytes). The soft and hard limits are separated by a comma. If only a single value is specified, both the hard and soft limits are set. A value of &#8220;infinity&#8221; indicates that there is no limit. A value of &#8220;user&#8221; will cause the invoking user&#8217;s resource limit to be preserved. A value of &#8220;default&#8221; will cause the target user&#8217;s default resource limit to be used on systems that allow per-user resource limits to be configured. Only available starting with API version 1.17.</p>
<dt><code>rlimit_locks=soft,hard</code></p>
<dd>The maximum number of locks that the process may establish, if supported by the operating system. The soft and hard limits are separated by a comma. If only a single value is specified, both the hard and soft limits are set. A value of &#8220;infinity&#8221; indicates that there is no limit. A value of &#8220;user&#8221; will cause the invoking user&#8217;s resource limit to be preserved. A value of &#8220;default&#8221; will cause the target user&#8217;s default resource limit to be used on systems that allow per-user resource limits to be configured. Only available starting with API version 1.17.</p>
<dt><code>rlimit_memlock=soft,hard</code></p>
<dd>The maximum size that the process may lock in memory (in bytes), if supported by the operating system. The soft and hard limits are separated by a comma. If only a single value is specified, both the hard and soft limits are set. A value of &#8220;infinity&#8221; indicates that there is no limit. A value of &#8220;user&#8221; will cause the invoking user&#8217;s resource limit to be preserved. A value of &#8220;default&#8221; will cause the target user&#8217;s default resource limit to be used on systems that allow per-user resource limits to be configured. Only available starting with API version 1.17.</p>
<dt><code>rlimit_nofile=soft,hard</code></p>
<dd>The maximum number of files that the process may have open. The soft and hard limits are separated by a comma. If only a single value is specified, both the hard and soft limits are set. A value of &#8220;infinity&#8221; indicates that there is no limit. A value of &#8220;user&#8221; will cause the invoking user&#8217;s resource limit to be preserved. A value of &#8220;default&#8221; will cause the target user&#8217;s default resource limit to be used on systems that allow per-user resource limits to be configured. Only available starting with API version 1.17.</p>
<dt><code>rlimit_nproc=soft,hard</code></p>
<dd>The maximum number of processes that the user may run simultaneously. The soft and hard limits are separated by a comma. If only a single value is specified, both the hard and soft limits are set. A value of &#8220;infinity&#8221; indicates that there is no limit. A value of &#8220;user&#8221; will cause the invoking user&#8217;s resource limit to be preserved. A value of &#8220;default&#8221; will cause the target user&#8217;s default resource limit to be used on systems that allow per-user resource limits to be configured. Only available starting with API version 1.17.</p>
<dt><code>rlimit_rss=soft,hard</code></p>
<dd>The maximum size to which the process&#8217;s resident set size may grow (in bytes). The soft and hard limits are separated by a comma. If only a single value is specified, both the hard and soft limits are set. A value of &#8220;infinity&#8221; indicates that there is no limit. A value of &#8220;user&#8221; will cause the invoking user&#8217;s resource limit to be preserved. A value of &#8220;default&#8221; will cause the target user&#8217;s default resource limit to be used on systems that allow per-user resource limits to be configured. Only available starting with API version 1.17.</p>
<dt><code>rlimit_stack=soft,hard</code></p>
<dd>The maximum size to which the process&#8217;s stack may grow (in bytes). The soft and hard limits are separated by a comma. If only a single value is specified, both the hard and soft limits are set. A value of &#8220;infinity&#8221; indicates that there is no limit. A value of &#8220;user&#8221; will cause the invoking user&#8217;s resource limit to be preserved. A value of &#8220;default&#8221; will cause the target user&#8217;s default resource limit to be used on systems that allow per-user resource limits to be configured. Only available starting with API version 1.17.</p>
<dt><code>runas_egid=gid</code></p>
<dd>Effective group-ID to run the command as. If not specified, the value of <i>runas_gid</i> is used.</p>
<dt><code>runas_euid=uid</code></p>
<dd>Effective user-ID to run the command as. If not specified, the value of <i>runas_uid</i> is used.</p>
<dt><code>runas_gid=gid</code></p>
<dd>Group-ID to run the command as.</p>
<dt><code>runas_group=string</code></p>
<dd>The name of the group the command will run as, if it is different from the <i>runas_user </i><code>&#8216;s</code> default group. This value is provided for auditing purposes only, the <code>sudo</code> front-end uses <i>runas_egid</i> and <i>runas_gid</i> when executing the command.</p>
<dt><code>runas_groups=list</code></p>
<dd>The supplementary group vector to use for the command in the form of a comma-separated list of group-IDs. If <i>preserve_groups</i> is set, this option is ignored.</p>
<dt><code>runas_uid=uid</code></p>
<dd>User-ID to run the command as.</p>
<dt><code>runas_user=string</code></p>
<dd>The name of the user the command will run as, which should correspond to <i>runas_euid</i> (or <i>runas_uid</i> if <i>runas_euid</i> is not set). This value is provided for auditing purposes only, the <code>sudo</code> front-end uses <i>runas_euid</i> and <i>runas_uid</i> when executing the command.</p>
<dt><code>selinux_role=string</code></p>
<dd>SELinux role to use when executing the command.</p>
<dt><code>selinux_type=string</code></p>
<dd>SELinux type to use when executing the command.</p>
<dt><code>set_utmp=bool</code></p>
<dd>Create a utmp (or utmpx) entry when a pseudo-terminal is allocated. By default, the new entry will be a copy of the user&#8217;s existing utmp entry (if any), with the tty, time, type, and pid fields updated.</p>
<dt><code>sudoedit=bool</code></p>
<dd>Set to true when in <i>sudoedit</i> mode. The plugin may enable <i>sudoedit</i> mode even if <code>sudo</code> was not invoked as <code>sudoedit</code> This allows the plugin to perform command substitution and transparently enable <i>sudoedit</i> when the user attempts to run an editor.</p>
<dt><code>sudoedit_checkdir=bool</code></p>
<dd>Set to false to disable directory writability checks in <code>sudoedit</code> By default, <code>sudoedit</code> 1.8.16 and higher will check all directory components of the path to be edited for writability by the invoking user. Symbolic links will not be followed in writable directories and <code>sudoedit</code> will refuse to edit a file located in a writable directory. These restrictions are not enforced when <code>sudoedit</code> is run by root. The <i>sudoedit_follow</i> option can be set to false to disable this check. Only available starting with API version 1.8.</p>
<dt><code>sudoedit_follow=bool</code></p>
<dd>Set to true to allow <code>sudoedit</code> to edit files that are symbolic links. By default, <code>sudoedit</code> 1.8.15 and higher will refuse to open a symbolic link. The <i>sudoedit_follow</i> option can be used to restore the older behavior and allow <code>sudoedit</code> to open symbolic links. Only available starting with API version 1.8.</p>
<dt><code>timeout=int</code></p>
<dd>Command timeout. If non-zero then when the timeout expires the command will be killed.</p>
<dt><code>umask=octal</code></p>
<dd>The file creation mask to use when executing the command. This value may be overridden by PAM or login.conf on some systems unless the <i>umask_override</i> option is also set.</p>
<dt><code>umask_override=bool</code></p>
<dd>Force the value specified by the <i>umask</i> option to override any umask set by PAM or login.conf.</p>
<dt><code>use_pty=bool</code></p>
<dd>Allocate a pseudo-terminal to run the command in, regardless of whether or not I/O logging is in use. By default, <code>sudo</code> will only run the command in a pseudo-terminal when an I/O log plugin is loaded.</p>
<dt><code>utmp_user=string</code></p>
<dd>User name to use when constructing a new utmp (or utmpx) entry when <i>set_utmp</i> is enabled. This option can be used to set the user field in the utmp entry to the user the command runs as rather than the invoking user. If not set, <code>sudo</code> will base the new entry on the invoking user&#8217;s existing entry.</dl>
<p> Unsupported values will be ignored.</p>
<dt><code>argv_out</code></p>
<dd>The <code>NULL -terminated</code> argument vector to pass to the <a href="/docs/linux/man/2-execve/">execve</a>(2) system call when executing the command. The plugin is responsible for allocating and populating the vector.</p>
<dt><code>user_env_out</code></p>
<dd>The <code>NULL -terminated</code> environment vector to use when executing the command. The plugin is responsible for allocating and populating the vector.</p>
<dt><code>errstr</code></p>
<dd>If the Fn check_policy function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</dl>
<dt><code>list</code></p>
<dd>
<pre>int (*list)(int argc, char * const argv[], int verbose,
 const char *list_user, const char **errstr);</pre>
<p>List available privileges for the invoking user. Returns 1 on success, 0 on failure, and -1 on error. On error, the plugin may optionally call the Fn conversation or Fn plugin_printf function with <code>SUDO_CONF_ERROR_MSG</code> to present additional error information to the user. Privileges should be output via the Fn conversation or Fn plugin_printf function using <code>SUDO_CONV_INFO_MSG</code> The function arguments are as follows:</p>
<dl>
<dt><code>argc</code></p>
<dd>The number of elements in <i>argv</i> not counting the final <code>NULL</code> pointer.</p>
<dt><code>argv</code></p>
<dd>If <code>non- NULL</code> an argument vector describing a command the user wishes to check against the policy in the same form as what would be passed to the <a href="/docs/linux/man/2-execve/">execve</a>(2) system call. If the command is permitted by the policy, the fully-qualified path to the command should be displayed along with any command line arguments.</p>
<dt><code>verbose</code></p>
<dd>Flag indicating whether to list in verbose mode or not.</p>
<dt><code>list_user</code></p>
<dd>The name of a different user to list privileges for if the policy allows it. If <code>NULL</code> the plugin should list the privileges of the invoking user.</p>
<dt><code>errstr</code></p>
<dd>If the Fn list function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</dl>
<dt><code>validate</code></p>
<dd>
<pre>int (*validate)(const char **errstr);</pre>
<p>The Fn validate function is called when <code>sudo</code> is run with the &#8211;<code>v</code> option. For policy plugins such as <code>sudoers</code> that cache authentication credentials, this function will validate and cache the credentials. The Fn validate function should be <code>NULL</code> if the plugin does not support credential caching. Returns 1 on success, 0 on failure, and -1 on error. On error, the plugin may optionally call the Fn conversation or Fn plugin_printf function with <code>SUDO_CONF_ERROR_MSG</code> to present additional error information to the user. The function arguments are as follows:</p>
<dl>
<dt><code>errstr</code></p>
<dd>If the Fn validate function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</dl>
<dt><code>invalidate</code></p>
<dd>
<pre>void (*invalidate)(int remove);</pre>
<p>The Fn invalidate function is called when <code>sudo</code> is run with the &#8211;<code>k</code> or &#8211;<code>K</code> option. For policy plugins such as <code>sudoers</code> that cache authentication credentials, this function will invalidate the credentials. If the <i>remove</i> flag is set, the plugin may remove the credentials instead of simply invalidating them. The Fn invalidate function should be <code>NULL</code> if the plugin does not support credential caching.</p>
<dt><code>init_session</code></p>
<dd>
<pre>int (*init_session)(struct passwd *pwd, char **user_env_out[]);</pre>
<p>The Fn init_session function is called before <code>sudo</code> sets up the execution environment for the command. It is run in the parent <code>sudo</code> process and before any user-ID or group-ID changes. This can be used to perform session setup that is not supported by <i>command_info</i> such as opening the PAM session. The Fn close function can be used to tear down the session that was opened by <code>init_session</code> The <i>pwd</i> argument points to a passwd struct for the user the command will be run as if the user-ID the command will run as was found in the password database, otherwise it will be <code>NULL</code> The <i>user_env_out</i> argument points to the environment the command will run in, in the form of a <code>NULL -terminated</code> vector of &#8220;name=value&#8221; strings. This is the same string passed back to the front-end via the Policy Plugin&#8217;s <i>user_env_out</i> parameter. If the Fn init_session function needs to modify the user environment, it should update the pointer stored in <i>user_env_out</i> The expected use case is to merge the contents of the PAM environment (if any) with the contents of <i>user_env_out</i> NOTE: the <i>user_env_out</i> parameter is only available starting with API version 1.2. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using <i>user_env_out</i> Failure to do so may result in a crash. Returns 1 on success, 0 on failure, and -1 on error. On error, the plugin may optionally call the Fn conversation or Fn plugin_printf function with <code>SUDO_CONF_ERROR_MSG</code> to present additional error information to the user.</p>
<dt><code>register_hooks</code></p>
<dd>
<pre>void (*register_hooks)(int version,
 int (*register_hook)(struct sudo_hook *hook));</pre>
<p>The Fn register_hooks function is called by the sudo front-end to register any hooks the plugin needs. If the plugin does not support hooks, <code>register_hooks</code> should be set to the <code>NULL</code> pointer. The <i>version</i> argument describes the version of the hooks API supported by the <code>sudo</code> front-end. The Fn register_hook function should be used to register any supported hooks the plugin needs. It returns 0 on success, 1 if the hook type is not supported, and -1 if the major version in <code>struct hook</code> does not match the front-end&#8217;s major hook API version. See the Sx Hook function API section below for more information about hooks. NOTE: the Fn register_hooks function is only available starting with API version 1.2. If the <code>sudo</code> front-end doesn&#8217;t support API version 1.2 or higher, <code>register_hooks</code> will not be called.</p>
<dt><code>deregister_hooks</code></p>
<dd>
<pre>void (*deregister_hooks)(int version,
 int (*deregister_hook)(struct sudo_hook *hook));</pre>
<p>The Fn deregister_hooks function is called by the sudo front-end to deregister any hooks the plugin has registered. If the plugin does not support hooks, <code>deregister_hooks</code> should be set to the <code>NULL</code> pointer. The <i>version</i> argument describes the version of the hooks API supported by the <code>sudo</code> front-end. The Fn deregister_hook function should be used to deregister any hooks that were put in place by the Fn register_hook function. If the plugin tries to deregister a hook that the front-end does not support, <code>deregister_hook</code> will return an error. See the Sx Hook function API section below for more information about hooks. NOTE: the Fn deregister_hooks function is only available starting with API version 1.2. If the <code>sudo</code> front-end doesn&#8217;t support API version 1.2 or higher, <code>deregister_hooks</code> will not be called.</p>
<dt><code>event_alloc</code></p>
<dd>
<pre>struct sudo_plugin_event * (*event_alloc)(void);</pre>
<p>The Fn event_alloc function is used to allocate a <code>struct sudo_plugin_event</code> which provides access to the main <code>sudo</code> event loop. Unlike the other fields, the Fn event_alloc pointer is filled in by the <code>sudo</code> front-end, not by the plugin. See the Sx Event API section below for more information about events. NOTE: the Fn event_alloc function is only available starting with API version 1.15. If the <code>sudo</code> front-end doesn&#8217;t support API version 1.15 or higher, Fn event_alloc will not be set.</p>
<dt><code>errstr</code></p>
<dd>If the Fn init_session function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</dl>
<p> Policy Plugin Version Macros</p>
<p>/* Plugin API version major/minor. */<br />
#define SUDO_API_VERSION_MAJOR 1<br />
#define SUDO_API_VERSION_MINOR 13<br />
#define SUDO_API_MKVERSION(x, y) ((x &lt;&lt; 16) | y)<br />
#define SUDO_API_VERSION SUDO_API_MKVERSION(SUDO_API_VERSION_MAJOR, \<br />
                                            SUDO_API_VERSION_MINOR)</p>
<p>/* Getters and setters for API version */<br />
#define SUDO_API_VERSION_GET_MAJOR(v) ((v) &gt;&gt; 16)<br />
#define SUDO_API_VERSION_GET_MINOR(v) ((v)&amp;0xffff)<br />
#define SUDO_API_VERSION_SET_MAJOR(vp, n)         \<br />
    do {                                          \<br />
        *(vp) = (*(vp)&amp;0x0000ffff) | ((n) &lt;&lt; 16); \<br />
    } while (0)<br />
#define SUDO_API_VERSION_SET_MINOR(vp, n) \<br />
    do {                                  \<br />
        *(vp) = (*(vp)&amp;0xffff0000) | (n); \<br />
    } while (0)</p>
<p>        I /<br />
    O plugin API</p>
<p>    struct io_plugin {<br />
#define SUDO_IO_PLUGIN 2<br />
    unsigned int type;    /* always SUDO_IO_PLUGIN */<br />
    unsigned int version; /* always SUDO_API_VERSION */<br />
    int (*open)(unsigned int version, sudo_conv_t conversation,<br />
                sudo_printf_t plugin_printf, char *const settings[],<br />
                char *const user_info[], char *const command_info[],<br />
                int argc, char *const argv[], char *const user_env[],<br />
                char *const plugin_options[], const char **errstr);<br />
    void (*close)(int exit_status, int error); /* wait status or error */<br />
    int (*show_version)(int verbose);<br />
    int (*log_ttyin)(const char *buf, unsigned int len,<br />
                     const char **errstr);<br />
    int (*log_ttyout)(const char *buf, unsigned int len,<br />
                      const char **errstr);<br />
    int (*log_stdin)(const char *buf, unsigned int len,<br />
                     const char **errstr);<br />
    int (*log_stdout)(const char *buf, unsigned int len,<br />
                      const char **errstr);<br />
    int (*log_stderr)(const char *buf, unsigned int len,<br />
                      const char **errstr);<br />
    void (*register_hooks)(int version,<br />
                           int (*register_hook)(struct sudo_hook *hook));<br />
    void (*deregister_hooks)(int version,<br />
                             int (*deregister_hook)(struct sudo_hook *hook));<br />
    int (*change_winsize)(unsigned int lines, unsigned int cols,<br />
                          const char **errstr);<br />
    int (*log_suspend)(int signo, const char **errstr);<br />
    struct sudo_plugin_event *(*event_alloc)(void);<br />
}; When an I/O plugin is loaded, <code>sudo</code> runs the command in a pseudo-terminal. This makes it possible to log the input and output from the user&#8217;s session. If any of the standard input, standard output, or standard error do not correspond to a tty, <code>sudo</code> will open a pipe to capture the I/O for logging before passing it on. The log_ttyin function receives the raw user input from the terminal device (note that this will include input even when echo is disabled, such as when a password is read). The log_ttyout function receives output from the pseudo-terminal that is suitable for replaying the user&#8217;s session at a later time. The Fn log_stdin , Fn log_stdout , and Fn log_stderr functions are only called if the standard input, standard output, or standard error respectively correspond to something other than a tty. Any of the logging functions may be set to the <code>NULL</code> pointer if no logging is to be performed. If the open function returns 0, no I/O will be sent to the plugin. If a logging function returns an error (-1) the running command will be terminated and all of the plugin&#8217;s logging functions will be disabled. Other I/O logging plugins will still receive any remaining input or output that has not yet been processed. If an input logging function rejects the data by returning 0, the command will be terminated and the data will not be passed to the command, though it will still be sent to any other I/O logging plugins. If an output logging function rejects the data by returning 0, the command will be terminated and the data will not be written to the terminal, though it will still be sent to any other I/O logging plugins. The audit_plugin struct has the following fields:</p>
<dl>
<dt><code>type</code></p>
<dd>The <code>type</code> field should always be set to <code>SUDO_IO_PLUGIN</code></p>
<dt><code>version</code></p>
<dd>The <code>version</code> field should be set to <code>SUDO_API_VERSION</code> This allows <code>sudo</code> to determine the API version the plugin was built against.</p>
<dt><code>open</code></p>
<dd>
<pre>int (*open)(unsigned int version, sudo_conv_t conversation,
 sudo_printf_t plugin_printf, char * const settings[],
 char * const user_info[], char * const command_info[],
 int argc, char * const argv[], char * const user_env[],
 char * const plugin_options[]);</pre>
<p>The Fn open function is run before the Fn log_ttyin , Fn log_ttyout , Fn log_stdin , Fn log_stdout , Fn log_stderr , Fn log_suspend , Fn change_winsize , or Fn show_version functions are called. It is only called if the version is being requested or if the policy plugin&#8217;s Fn check_policy function has returned successfully. It returns 1 on success, 0 on failure, -1 if a general error occurred, or -2 if there was a usage error. In the latter case, <code>sudo</code> will print a usage message before it exits. If an error occurs, the plugin may optionally call the Fn conversation or Fn plugin_printf function with <code>SUDO_CONF_ERROR_MSG</code> to present additional error information to the user. The function arguments are as follows:</p>
<dl>
<dt><code>version</code></p>
<dd>The version passed in by <code>sudo</code> allows the plugin to determine the major and minor version number of the plugin API supported by <code>sudo</code></p>
<dt><code>conversation</code></p>
<dd>A pointer to the Fn conversation function that may be used by the Fn show_version function to display version information (see Fn show_version below). The Fn conversation function may also be used to display additional error message to the user. The Fn conversation function returns 0 on success and -1 on failure.</p>
<dt><code>plugin_printf</code></p>
<dd>A pointer to a Fn printf Ns -style function that may be used by the Fn show_version function to display version information (see show_version below). The Fn plugin_printf function may also be used to display additional error message to the user. The Fn plugin_printf function returns number of characters printed on success and -1 on failure.</p>
<dt><code>settings</code></p>
<dd>A vector of user-supplied <code>sudo</code> settings in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. These settings correspond to options the user specified when running <code>sudo</code> As such, they will only be present when the corresponding option has been specified on the command line. When parsing <i>settings</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. See the Sx Policy plugin API section for a list of all possible settings.</p>
<dt><code>user_info</code></p>
<dd>A vector of information about the user running the command in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. When parsing <i>user_info</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. See the Sx Policy plugin API section for a list of all possible strings.</p>
<dt><code>command_info</code></p>
<dd>A vector of information describing the command being run in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. When parsing <i>command_info</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. See the Sx Policy plugin API section for a list of all possible strings.</p>
<dt><code>argc</code></p>
<dd>The number of elements in <i>argv</i> not counting the final <code>NULL</code> pointer. It can be zero, when <code>sudo</code> is called with &#8211;<code>V</code></p>
<dt><code>argv</code></p>
<dd>If <code>non- NULL</code> an argument vector describing a command the user wishes to run in the same form as what would be passed to the <a href="/docs/linux/man/2-execve/">execve</a>(2) system call.</p>
<dt><code>user_env</code></p>
<dd>The user&#8217;s environment in the form of a <code>NULL -terminated</code> vector of &#8220;name=value&#8221; strings. When parsing <i>user_env</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might.</p>
<dt><code>plugin_options</code></p>
<dd>Any (non-comment) strings immediately after the plugin path are treated as arguments to the plugin. These arguments are split on a white space boundary and are passed to the plugin in the form of a <code>NULL -terminated</code> array of strings. If no arguments were specified, <i>plugin_options</i> will be the <code>NULL</code> pointer. NOTE: the <i>plugin_options</i> parameter is only available starting with API version 1.2. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using <i>plugin_options</i> Failure to do so may result in a crash.</p>
<dt><code>errstr</code></p>
<dd>If the Fn open function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</dl>
<dt><code>close</code></p>
<dd>
<pre>void (*close)(int exit_status, int error);</pre>
<p>The Fn close function is called when <code>sudo</code> is finished, shortly before it exits. The function arguments are as follows:</p>
<dl>
<dt><code>exit_status</code></p>
<dd>The command&#8217;s exit status, as returned by the <a href="/docs/linux/man/2-wait/">wait</a>(2) system call, or zero if no command was run. The value of <code>exit_status</code> is undefined if <code>error</code> is non-zero.</p>
<dt><code>error</code></p>
<dd>If the command could not be executed, this is set to the value of <code>errno</code> set by the <a href="/docs/linux/man/2-execve/">execve</a>(2) system call. If the command was successfully executed, the value of <code>error</code> is zero.</dl>
<dt><code>show_version</code></p>
<dd>
<pre>int (*show_version)(int verbose);</pre>
<p>The Fn show_version function is called by <code>sudo</code> when the user specifies the &#8211;<code>V</code> option. The plugin may display its version information to the user via the Fn conversation or Fn plugin_printf function using <code>SUDO_CONV_INFO_MSG</code> Returns 1 on success, 0 on failure, -1 if a general error occurred,<br />
    or -2 if there was a usage error, although the return value is currently ignored.log_ttyin</p>
<p>                                      int(*log_ttyin)(const char *buf, unsigned int len, const char **errstr); The Fn log_ttyin function is called whenever data can be read from the user but before it is passed to the running command. This allows the plugin to reject data if it chooses to (for instance if the input contains banned content). Returns 1 if the data should be passed to the command, 0 if the data is rejected (which will terminate the running command), or -1 if an error occurred. The function arguments are as follows:</p>
<dl>
<dt><code>buf</code></p>
<dd>The buffer containing user input.</p>
<dt><code>len</code></p>
<dd>The length of <i>buf</i> in bytes.</p>
<dt><code>errstr</code></p>
<dd>If the Fn log_ttyin function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</dl>
<dt><code>log_ttyout</code></p>
<dd>
<pre>int (*log_ttyout)(const char *buf, unsigned int len,
 const char **errstr);</pre>
<p>The Fn log_ttyout function is called whenever data can be read from the command but before it is written to the user&#8217;s terminal. This allows the plugin to reject data if it chooses to (for instance if the output contains banned content). Returns 1 if the data should be passed to the user, 0 if the data is rejected (which will terminate the running command), or -1 if an error occurred. The function arguments are as follows:</p>
<dl>
<dt><code>buf</code></p>
<dd>The buffer containing command output.</p>
<dt><code>len</code></p>
<dd>The length of <i>buf</i> in bytes.</p>
<dt><code>errstr</code></p>
<dd>If the Fn log_ttyout function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</dl>
<dt><code>log_stdin</code></p>
<dd>
<pre>int (*log_stdin)(const char *buf, unsigned int len,
 const char **errstr);</pre>
<p>The Fn log_stdin function is only used if the standard input does not correspond to a tty device. It is called whenever data can be read from the standard input but before it is passed to the running command. This allows the plugin to reject data if it chooses to (for instance if the input contains banned content). Returns 1 if the data should be passed to the command, 0 if the data is rejected (which will terminate the running command), or -1 if an error occurred. The function arguments are as follows:</p>
<dl>
<dt><code>buf</code></p>
<dd>The buffer containing user input.</p>
<dt><code>len</code></p>
<dd>The length of <i>buf</i> in bytes.</p>
<dt><code>errstr</code></p>
<dd>If the Fn log_stdin function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</dl>
<dt><code>log_stdout</code></p>
<dd>
<pre>int (*log_stdout)(const char *buf, unsigned int len,
 const char **errstr);</pre>
<p>The Fn log_stdout function is only used if the standard output does not correspond to a tty device. It is called whenever data can be read from the command but before it is written to the standard output. This allows the plugin to reject data if it chooses to (for instance if the output contains banned content). Returns 1 if the data should be passed to the user, 0 if the data is rejected (which will terminate the running command), or -1 if an error occurred. The function arguments are as follows:</p>
<dl>
<dt><code>buf</code></p>
<dd>The buffer containing command output.</p>
<dt><code>len</code></p>
<dd>The length of <i>buf</i> in bytes.</p>
<dt><code>errstr</code></p>
<dd>If the Fn log_stdout function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</dl>
<dt><code>log_stderr</code></p>
<dd>
<pre>int (*log_stderr)(const char *buf, unsigned int len,
 const char **errstr);</pre>
<p>The Fn log_stderr function is only used if the standard error does not correspond to a tty device. It is called whenever data can be read from the command but before it is written to the standard error. This allows the plugin to reject data if it chooses to (for instance if the output contains banned content). Returns 1 if the data should be passed to the user, 0 if the data is rejected (which will terminate the running command), or -1 if an error occurred. The function arguments are as follows:</p>
<dl>
<dt><code>buf</code></p>
<dd>The buffer containing command output.</p>
<dt><code>len</code></p>
<dd>The length of <i>buf</i> in bytes.</p>
<dt><code>errstr</code></p>
<dd>If the Fn log_stderr function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</dl>
<dt><code>register_hooks</code></p>
<dd>See the Sx Policy plugin API section for a description of <code>register_hooks</code></p>
<dt><code>deregister_hooks</code></p>
<dd>See the Sx Policy plugin API section for a description of <code>deregister_hooks</code></p>
<dt><code>change_winsize</code></p>
<dd>
<pre>int (*change_winsize)(unsigned int lines, unsigned int cols,
 const char **errstr);</pre>
<p>The Fn change_winsize function is called whenever the window size of the terminal changes from the initial values specified in the <code>user_info</code> list. Returns -1 if an error occurred, in which case no further calls to Fn change_winsize will be made, The function arguments are as follows:</p>
<dl>
<dt><code>lines</code></p>
<dd>The number of lines (rows) in the re-sized terminal.</p>
<dt><code>cols</code></p>
<dd>The number of columns in the re-sized terminal.</p>
<dt><code>errstr</code></p>
<dd>If the Fn change_winsize function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</dl>
<dt><code>log_suspend</code></p>
<dd>
<pre>int (*log_suspend)(int signo, const char **errstr);</pre>
<p>The Fn log_suspend function is called whenever a command is suspended or resumed. Logging this information makes it possible to skip the period of time when the command was suspended during playback of a session. Returns -1 if an error occurred, in which case no further calls to Fn log_suspend will be made, The function arguments are as follows:</p>
<dl>
<dt><code>signo</code></p>
<dd>The signal that caused the command to be suspended, or <code>SIGCONT</code> if the command was resumed.</p>
<dt><code>errstr</code></p>
<dd>If the Fn log_suspend function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called. NOTE: the Fa errstr parameter is only available starting with API version 1.15. A plugin <code>must</code> check the API version specified by the <code>sudo</code> front-end before using Fa errstr . Failure to do so may result in a crash.</p>
<dt><code>event_alloc</code></p>
<dd>
<pre>struct sudo_plugin_event * (*event_alloc)(void);</pre>
<p>The Fn event_alloc function is used to allocate a <code>struct sudo_plugin_event</code> which provides access to the main <code>sudo</code> event loop. Unlike the other fields, the Fn event_alloc pointer is filled in by the <code>sudo</code> front-end, not by the plugin. See the Sx Event API section below for more information about events. NOTE: the Fn event_alloc function is only available starting with API version 1.15. If the <code>sudo</code> front-end doesn&#8217;t support API version 1.15 or higher, Fn event_alloc will not be set.</dl>
<p> <i>I/O Plugin Version Macros</i> Same as for the Sx Policy plugin API .</dl>
<p> Audit plugin API</p>
<p>/* Audit plugin close function status types. */<br />
#define SUDO_PLUGIN_NO_STATUS 0<br />
#define SUDO_PLUGIN_WAIT_STATUS 1<br />
#define SUDO_PLUGIN_EXEC_ERROR 2<br />
#define SUDO_PLUGIN_SUDO_ERROR 3</p>
<p>#define SUDO_AUDIT_PLUGIN 3<br />
    struct audit_plugin {<br />
    unsigned int type;    /* always SUDO_AUDIT_PLUGIN */<br />
    unsigned int version; /* always SUDO_API_VERSION */<br />
    int (*open)(unsigned int version, sudo_conv_t conversation,<br />
                sudo_printf_t sudo_printf, char *const settings[],<br />
                char *const user_info[], int submit_optind,<br />
                char *const submit_argv[], char *const submit_envp[],<br />
                char *const plugin_options[], const char **errstr);<br />
    void (*close)(int status_type, int status);<br />
    int (*accept)(const char *plugin_name,<br />
                  unsigned int plugin_type, char *const command_info[],<br />
                  char *const run_argv[], char *const run_envp[],<br />
                  const char **errstr);<br />
    int (*reject)(const char *plugin_name, unsigned int plugin_type,<br />
                  const char *audit_msg, char *const command_info[],<br />
                  const char **errstr);<br />
    int (*error)(const char *plugin_name, unsigned int plugin_type,<br />
                 const char *audit_msg, char *const command_info[],<br />
                 const char **errstr);<br />
    int (*show_version)(int verbose);<br />
    void (*register_hooks)(int version,<br />
                           int (*register_hook)(struct sudo_hook *hook));<br />
    void (*deregister_hooks)(int version,<br />
                             int (*deregister_hook)(struct sudo_hook *hook));<br />
    struct sudo_plugin_event *(*event_alloc)(void);<br />
} An audit plugin can be used to log successful and unsuccessful attempts to run <code>sudo</code> independent of the policy or any I/O plugins. Multiple audit plugins may be specified in sudo.conf5. The audit_plugin struct has the following fields:</p>
<dl>
<dt><code>type</code></p>
<dd>The <code>type</code> field should always be set to <code>SUDO_AUDIT_PLUGIN</code></p>
<dt><code>version</code></p>
<dd>The <code>version</code> field should be set to <code>SUDO_API_VERSION</code> This allows <code>sudo</code> to determine the API version the plugin was built against.</p>
<dt><code>open</code></p>
<dd>
<pre>int (*open)(unsigned int version, sudo_conv_t conversation,
 sudo_printf_t sudo_printf, char * const settings[],
 char * const user_info[], int submit_optind,
 char * const submit_argv[], char * const submit_envp[],
 char * const plugin_options[], const char **errstr);</pre>
<p>The audit Fn open function is run before any other <code>sudo</code> plugin API functions. This makes it possible to audit failures in the other plugins. It returns 1 on success, 0 on failure, -1 if a general error occurred, or -2 if there was a usage error. In the latter case, <code>sudo</code> will print a usage message before it exits. If an error occurs, the plugin may optionally call the Fn conversation or Fn plugin_printf function with <code>SUDO_CONF_ERROR_MSG</code> to present additional error information to the user. The function arguments are as follows:</p>
<dl>
<dt><code>version</code></p>
<dd>The version passed in by <code>sudo</code> allows the plugin to determine the major and minor version number of the plugin API supported by <code>sudo</code></p>
<dt><code>conversation</code></p>
<dd>A pointer to the Fn conversation function that may be used by the Fn show_version function to display version information (see Fn show_version below). The Fn conversation function may also be used to display additional error message to the user. The Fn conversation function returns 0 on success, and -1 on failure.</p>
<dt><code>plugin_printf</code></p>
<dd>A pointer to a Fn printf Ns -style function that may be used by the Fn show_version function to display version information (see show_version below). The Fn plugin_printf function may also be used to display additional error message to the user. The Fn plugin_printf function returns number of characters printed on success and -1 on failure.</p>
<dt><code>settings</code></p>
<dd>A vector of user-supplied <code>sudo</code> settings in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. These settings correspond to options the user specified when running <code>sudo</code> As such, they will only be present when the corresponding option has been specified on the command line. When parsing <i>settings</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. See the Sx Policy plugin API section for a list of all possible settings.</p>
<dt><code>user_info</code></p>
<dd>A vector of information about the user running the command in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. When parsing <i>user_info</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. See the Sx Policy plugin API section for a list of all possible strings.</p>
<dt><code>submit_optind</code></p>
<dd>The index into Fa submit_argv that corresponds to the first entry that is not a command line option. If Fa submit_argv only consists of options, which may be the case with the &#8211;<code>l</code> or &#8211;<code>v</code> options, <code>submit_argv[submit_optind]</code> will evaluate to the NULL pointer.</p>
<dt><code>submit_argv</code></p>
<dd>The argument vector <code>sudo</code> was invoked with, including all command line options. The Fa submit_optind argument can be used to determine the end of the command line options.</p>
<dt><code>submit_envp</code></p>
<dd>The invoking user&#8217;s environment in the form of a <code>NULL -terminated</code> vector of &#8220;name=value&#8221; strings. When parsing <i>submit_envp</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might.</p>
<dt><code>plugin_options</code></p>
<dd>Any (non-comment) strings immediately after the plugin path are treated as arguments to the plugin. These arguments are split on a white space boundary and are passed to the plugin in the form of a <code>NULL -terminated</code> array of strings. If no arguments were specified, <i>plugin_options</i> will be the <code>NULL</code> pointer.</p>
<dt><code>errstr</code></p>
<dd>If the Fn open function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called.</dl>
<dt><code>close</code></p>
<dd>
<pre>void (*close)(int status_type, int status);</pre>
<p>The Fn close function is called when <code>sudo</code> is finished, shortly before it exits. The function arguments are as follows:</p>
<dl>
<dt><code>status_type</code></p>
<dd>The type of status being passed. One of <code>SUDO_PLUGIN_NO_STATUS</code> <code>SUDO_PLUGIN_WAIT_STATUS</code> <code>SUDO_PLUGIN_EXEC_ERROR</code> or <code>SUDO_PLUGIN_SUDO_ERROR</code></p>
<dt><code>status</code></p>
<dd>Depending on the value of Fa status_type , this value is either ignored, the command&#8217;s exit status as returned by the <a href="/docs/linux/man/2-wait/">wait</a>(2) system call, the value of <code>errno</code> set by the <a href="/docs/linux/man/2-execve/">execve</a>(2) system call, or the value of <code>errno</code> resulting from an error in the <code>sudo</code> front-end.</dl>
<dt><code>accept</code></p>
<dd>
<pre>int (*accept)(const char *plugin_name, unsigned int plugin_type,
 char * const command_info[], char * const run_argv[],
 char * const run_envp[], const char **errstr);</pre>
<p>The Fn accept function is called when a command or action is accepted by a policy or approval plugin. The function arguments are as follows:</p>
<dl>
<dt><code>plugin_name</code></p>
<dd>The name of the plugin that accepted the command or &#8220;sudo&#8221; for the <code>sudo</code> front-end.</p>
<dt><code>plugin_type</code></p>
<dd>The type of plugin that accepted the command, currently either <code>SUDO_POLICY_PLUGIN</code> <code>SUDO_POLICY_APPROVAL</code> or <code>SUDO_FRONT_END</code> The Fn accept function is called multiple times&#8211;once for each policy or approval plugin that succeeds and once for the sudo front-end. When called on behalf of the sudo front-end, Fa command_info may include information from an I/O logging plugin as well. Typically, an audit plugin is interested in either the accept status from the <code>sudo</code> front-end or from the various policy and approval plugins, but not both. It is possible for the policy plugin to accept a command that is later rejected by an approval plugin, in which case the audit plugin&#8217;s Fn accept and Fn reject functions will <i>both</i> be called.</p>
<dt><code>command_info</code></p>
<dd>An optional vector of information describing the command being run in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. When parsing <i>command_info</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. See the Sx Policy plugin API section for a list of all possible strings.</p>
<dt><code>run_argv</code></p>
<dd>A <code>NULL -terminated</code> argument vector describing a command that will be run in the same form as what would be passed to the <a href="/docs/linux/man/2-execve/">execve</a>(2) system call.</p>
<dt><code>run_envp</code></p>
<dd>The environment the command will be run with in the form of a <code>NULL -terminated</code> vector of &#8220;name=value&#8221; strings. When parsing <i>run_envp</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might.</p>
<dt><code>errstr</code></p>
<dd>If the Fn accept function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called.</dl>
<dt><code>reject</code></p>
<dd>
<pre>int (*reject)(const char *plugin_name, unsigned int plugin_type,
 const char *audit_msg, char * const command_info[],
 const char **errstr);</pre>
<p>The Fn reject function is called when a command or action is rejected by a plugin. The function arguments are as follows:</p>
<dl>
<dt><code>plugin_name</code></p>
<dd>The name of the plugin that rejected the command.</p>
<dt><code>plugin_type</code></p>
<dd>The type of plugin that rejected the command, currently either <code>SUDO_POLICY_PLUGIN</code> <code>SUDO_APPROVAL_PLUGIN</code> or <code>SUDO_IO_PLUGIN</code> Unlike the Fn accept function, the Fn reject function is not called on behalf of the <code>sudo</code> front-end.</p>
<dt><code>audit_msg</code></p>
<dd>An optional string describing the reason the command was rejected by the plugin. If the plugin did not provide a reason, Fa audit_msg will be the <code>NULL</code> pointer.</p>
<dt><code>command_info</code></p>
<dd>An optional vector of information describing the command being run in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. When parsing <i>command_info</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. See the Sx Policy plugin API section for a list of all possible strings.</p>
<dt><code>errstr</code></p>
<dd>If the Fn reject function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called.</dl>
<dt><code>error</code></p>
<dd>
<pre>int (*error)(const char *plugin_name, unsigned int plugin_type,
 const char *audit_msg, char * const command_info[],
 const char **errstr);</pre>
<p>The Fn error function is called when a plugin or the <code>sudo</code> front-end returns an error. The function arguments are as follows:</p>
<dl>
<dt><code>plugin_name</code></p>
<dd>The name of the plugin that generated the error or &#8220;sudo&#8221; for the <code>sudo</code> front-end.</p>
<dt><code>plugin_type</code></p>
<dd>The type of plugin that generated the error, or <code>SUDO_FRONT_END</code> for the <code>sudo</code> front-end.</p>
<dt><code>audit_msg</code></p>
<dd>An optional string describing the plugin error. If the plugin did not provide a description, Fa audit_msg will be the <code>NULL</code> pointer.</p>
<dt><code>command_info</code></p>
<dd>An optional vector of information describing the command being run in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. When parsing <i>command_info</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. See the Sx Policy plugin API section for a list of all possible strings.</p>
<dt><code>errstr</code></p>
<dd>If the Fn error function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called.</dl>
<dt><code>show_version</code></p>
<dd>
<pre>int (*show_version)(int verbose);</pre>
<p>The Fn show_version function is called by <code>sudo</code> when the user specifies the &#8211;<code>V</code> option. The plugin may display its version information to the user via the Fn conversation or Fn plugin_printf function using <code>SUDO_CONV_INFO_MSG</code> If the user requests detailed version information, the verbose flag will be set. Returns 1 on success, 0 on failure, -1 if a general error occurred,<br />
or -2 if there was a usage error, although the return value is currently<br />
ignored.<br />
register_hooks</p>
<p>See the<br />
Sx Policy plugin API</p>
<p>section for a description of<br />
register_hooks</p>
<p>deregister_hooks</p>
<p>See the<br />
Sx Policy plugin API</p>
<p>section for a description of<br />
deregister_hooks</p>
<p>event_alloc</p>
<p>struct sudo_plugin_event * (*event_alloc)(void); The Fn event_alloc function is used to allocate a <code>struct sudo_plugin_event</code> which provides access to the main <code>sudo</code> event loop. Unlike the other fields, the Fn event_alloc pointer is filled in by the <code>sudo</code> front-end, not by the plugin. See the Sx Event API section below for more information about events. NOTE: the Fn event_alloc function is only available starting with API version 1.17. If the <code>sudo</code> front-end doesn&#8217;t support API version 1.17 or higher, Fn event_alloc will not be set.</dl>
<p> Approval plugin API</p>
<p>    struct approval_plugin {<br />
#define SUDO_APPROVAL_PLUGIN 4<br />
    unsigned int type;    /* always SUDO_APPROVAL_PLUGIN */<br />
    unsigned int version; /* always SUDO_API_VERSION */<br />
    int (*open)(unsigned int version, sudo_conv_t conversation,<br />
                sudo_printf_t sudo_printf, char *const settings[],<br />
                char *const user_info[], int submit_optind,<br />
                char *const submit_argv[], char *const submit_envp[],<br />
                char *const plugin_options[], const char **errstr);<br />
    void (*close)(void);<br />
    int (*check)(char *const command_info[], char *const run_argv[],<br />
                 char *const run_envp[], const char **errstr);<br />
    int (*show_version)(int verbose);<br />
}; An approval plugin can be used to apply extra constraints after a command has been accepted by the policy plugin. Unlike the other plugin types, it does not remain open until the command completes. The plugin is opened before a call to Fn check or Fn show_version and closed shortly thereafter (audit plugin functions must be called before the plugin is closed). Multiple approval plugins may be specified in sudo.conf5. The approval_plugin struct has the following fields:</p>
<dl>
<dt><code>type</code></p>
<dd>The <code>type</code> field should always be set to <code>SUDO_APPROVAL_PLUGIN</code></p>
<dt><code>version</code></p>
<dd>The <code>version</code> field should be set to <code>SUDO_API_VERSION</code> This allows <code>sudo</code> to determine the API version the plugin was built against.</p>
<dt><code>open</code></p>
<dd>
<pre>int (*open)(unsigned int version, sudo_conv_t conversation,
 sudo_printf_t sudo_printf, char * const settings[],
 char * const user_info[], int submit_optind,
 char * const submit_argv[], char * const submit_envp[],
 char * const plugin_options[], const char **errstr);</pre>
<p>The approval Fn open function is run immediately before a call to the plugin&#8217;s Fn check or Fn show_version functions. It is only called if the version is being requested or if the policy plugin&#8217;s Fn check_policy function has returned successfully. It returns 1 on success, 0 on failure, -1 if a general error occurred, or -2 if there was a usage error. In the latter case, <code>sudo</code> will print a usage message before it exits. If an error occurs, the plugin may optionally call the Fn conversation or Fn plugin_printf function with <code>SUDO_CONF_ERROR_MSG</code> to present additional error information to the user. The function arguments are as follows:</p>
<dl>
<dt><code>version</code></p>
<dd>The version passed in by <code>sudo</code> allows the plugin to determine the major and minor version number of the plugin API supported by <code>sudo</code></p>
<dt><code>conversation</code></p>
<dd>A pointer to the Fn conversation function that can be used by the plugin to interact with the user (see Sx Conversation API for details). Returns 0 on success and -1 on failure.</p>
<dt><code>plugin_printf</code></p>
<dd>A pointer to a Fn printf Ns -style function that may be used to display informational or error messages (see Sx Conversation API for details). Returns the number of characters printed on success and -1 on failure.</p>
<dt><code>settings</code></p>
<dd>A vector of user-supplied <code>sudo</code> settings in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. These settings correspond to options the user specified when running <code>sudo</code> As such, they will only be present when the corresponding option has been specified on the command line. When parsing <i>settings</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. See the Sx Policy plugin API section for a list of all possible settings.</p>
<dt><code>user_info</code></p>
<dd>A vector of information about the user running the command in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. When parsing <i>user_info</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. See the Sx Policy plugin API section for a list of all possible strings.</p>
<dt><code>submit_optind</code></p>
<dd>The index into Fa submit_argv that corresponds to the first entry that is not a command line option. If Fa submit_argv only consists of options, which may be the case with the &#8211;<code>l</code> or &#8211;<code>v</code> options, <code>submit_argv[submit_optind]</code> will evaluate to the NULL pointer.</p>
<dt><code>submit_argv</code></p>
<dd>The argument vector <code>sudo</code> was invoked with, including all command line options. The Fa submit_optind argument can be used to determine the end of the command line options.</p>
<dt><code>submit_envp</code></p>
<dd>The invoking user&#8217;s environment in the form of a <code>NULL -terminated</code> vector of &#8220;name=value&#8221; strings. When parsing <i>submit_envp</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might.</p>
<dt><code>plugin_options</code></p>
<dd>Any (non-comment) strings immediately after the plugin path are treated as arguments to the plugin. These arguments are split on a white space boundary and are passed to the plugin in the form of a <code>NULL -terminated</code> array of strings. If no arguments were specified, <i>plugin_options</i> will be the <code>NULL</code> pointer.</p>
<dt><code>errstr</code></p>
<dd>If the Fn open function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called.</dl>
<dt><code>close</code></p>
<dd>
<pre>void (*close)(void);</pre>
<p>The Fn close function is called after the approval plugin&#8217;s Fn check or Fn show_version functions have been called. It takes no arguments. The Fn close function is typically used to perform plugin-specific cleanup, such as the freeing of memory objects allocated by the plugin. If the plugin does not need to perform any cleanup, Fn close may be set to the <code>NULL</code> pointer.</p>
<dt><code>check</code></p>
<dd>
<pre>int (*check)(char * const command_info[], char * const run_argv[],
 char * const run_envp[], const char **errstr);</pre>
<p>The approval Fn check function is run after the policy plugin Fn check_policy function and before any I/O logging plugins. If multiple approval plugins are loaded, they must all succeed for the command to be allowed. It returns 1 on success, 0 on failure, -1 if a general error occurred, or -2 if there was a usage error. In the latter case, <code>sudo</code> will print a usage message before it exits. If an error occurs, the plugin may optionally call the Fn conversation or Fn plugin_printf function with <code>SUDO_CONF_ERROR_MSG</code> to present additional error information to the user. The function arguments are as follows:</p>
<dl>
<dt><code>command_info</code></p>
<dd>A vector of information describing the command being run in the form of &#8220;name=value&#8221; strings. The vector is terminated by a <code>NULL</code> pointer. When parsing <i>command_info</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might. See the Sx Policy plugin API section for a list of all possible strings.</p>
<dt><code>run_argv</code></p>
<dd>A <code>NULL -terminated</code> argument vector describing a command that will be run in the same form as what would be passed to the <a href="/docs/linux/man/2-execve/">execve</a>(2) system call.</p>
<dt><code>run_envp</code></p>
<dd>The environment the command will be run with in the form of a <code>NULL -terminated</code> vector of &#8220;name=value&#8221; strings. When parsing <i>run_envp</i> the plugin should split on the <code>first</code> equal sign (`=&#8217; ) since the <i>name</i> field will never include one itself but the <i>value</i> might.</p>
<dt><code>errstr</code></p>
<dd>If the Fn open function returns a value other than 1, the plugin may store a message describing the failure or error in Fa errstr . The <code>sudo</code> front-end will then pass this value to any registered audit plugins. The string stored in Fa errstr must remain valid until the plugin&#8217;s Fn close function is called.</dl>
<dt><code>show_version</code></p>
<dd>
<pre>int (*show_version)(int verbose);</pre>
<p>The Fn show_version function is called by <code>sudo</code> when the user specifies the &#8211;<code>V</code> option. The plugin may display its version information to the user via the Fn conversation or Fn plugin_printf function using <code>SUDO_CONV_INFO_MSG</code> If the user requests detailed version information, the verbose flag will be set. Returns 1 on success, 0 on failure, -1 if a general error occurred, or -2 if there was a usage error, although the return value is currently ignored.</dl>
<h3>Signal handlers</h3>
<p>The <code>sudo</code> front-end installs default signal handlers to trap common signals while the plugin functions are run. The following signals are trapped by default before the command is executed:  </p>
<li> <code>SIGALRM</code>
<li> <code>SIGHUP</code>
<li> <code>SIGINT</code>
<li> <code>SIGPIPE</code>
<li> <code>SIGQUIT</code>
<li> <code>SIGTERM</code>
<li> <code>SIGTSTP</code>
<li> <code>SIGUSR1</code>
<li> <code>SIGUSR2</code> </ul>
<p> If a fatal signal is received before the command is executed, <code>sudo</code> will call the plugin&#8217;s Fn close function with an exit status of 128 plus the value of the signal that was received. This allows for consistent logging of commands killed by a signal for plugins that log such information in their Fn close function. An exception to this is <code>SIGPIPE</code> which is ignored until the command is executed. A plugin may temporarily install its own signal handlers but must restore the original handler before the plugin function returns.</p>
<h3>Hook function API</h3>
<p>Beginning with plugin API version 1.2, it is possible to install hooks for certain functions called by the <code>sudo</code> front-end. Currently, the only supported hooks relate to the handling of environment variables. Hooks can be used to intercept attempts to get, set, or remove environment variables so that these changes can be reflected in the version of the environment that is used to execute a command. A future version of the API will support hooking internal <code>sudo</code> front-end functions as well. <i>Hook structure</i> Hooks in <code>sudo</code> are described by the following structure: </p>
<pre>typedef int (*sudo_hook_fn_t)();
struct sudo_hook {
 unsigned int hook_version;
 unsigned int hook_type;
 sudo_hook_fn_t hook_fn;
 void *closure;
};</pre>
<p>The <code>sudo_hook</code> structure has the following fields:</p>
<dl>
<dt><code>hook_version</code></p>
<dd>The <code>hook_version</code> field should be set to <code>SUDO_HOOK_VERSION</code></p>
<dt><code>hook_type</code></p>
<dd>The <code>hook_type</code> field may be one of the following supported hook types:</p>
<dl>
<dt><code>SUDO_HOOK_SETENV</code></p>
<dd>The C library <a href="/docs/linux/man/3-setenv/">setenv</a>(3) function. Any registered hooks will run before the C library implementation. The <code>hook_fn</code> field should be a function that matches the following typedef: </p>
<pre>typedef int (*sudo_hook_fn_setenv_t)(const char *name,
 const char *value, int overwrite, void *closure);</pre>
<p>If the registered hook does not match the typedef the results are unspecified.</p>
<dt><code>SUDO_HOOK_UNSETENV</code></p>
<dd>The C library <a href="/docs/linux/man/3-unsetenv/">unsetenv</a>(3) function. Any registered hooks will run before the C library implementation. The <code>hook_fn</code> field should be a function that matches the following typedef: </p>
<pre>typedef int (*sudo_hook_fn_unsetenv_t)(const char *name,
 void *closure);</pre>
<dt><code>SUDO_HOOK_GETENV</code></p>
<dd>The C library <a href="/docs/linux/man/3-getenv/">getenv</a>(3) function. Any registered hooks will run before the C library implementation. The <code>hook_fn</code> field should be a function that matches the following typedef: </p>
<pre>typedef int (*sudo_hook_fn_getenv_t)(const char *name,
 char **value, void *closure);</pre>
<p>If the registered hook does not match the typedef the results are unspecified.</p>
<dt><code>SUDO_HOOK_PUTENV</code></p>
<dd>The C library <a href="/docs/linux/man/3-putenv/">putenv</a>(3) function. Any registered hooks will run before the C library implementation. The <code>hook_fn</code> field should be a function that matches the following typedef: </p>
<pre>typedef int (*sudo_hook_fn_putenv_t)(char *string,
 void *closure);</pre>
<p>If the registered hook does not match the typedef the results are unspecified.</dl>
<dt><code>hook_fn</code></p>
<dd>sudo_hook_fn_t hook_fn; The <code>hook_fn</code> field should be set to the plugin&#8217;s hook implementation. The actual function arguments will vary depending on the <code>hook_type</code> (see <code>hook_type</code> above). In all cases, the <code>closure</code> field of <code>struct sudo_hook</code> is passed as the last function parameter. This can be used to pass arbitrary data to the plugin&#8217;s hook implementation. The function return value may be one of the following:</p>
<dl>
<dt><code>SUDO_HOOK_RET_ERROR</code></p>
<dd>The hook function encountered an error.</p>
<dt><code>SUDO_HOOK_RET_NEXT</code></p>
<dd>The hook completed without error, go on to the next hook (including the system implementation if applicable). For example, a <a href="/docs/linux/man/3-getenv/">getenv</a>(3) hook might return <code>SUDO_HOOK_RET_NEXT</code> if the specified variable was not found in the private copy of the environment.</p>
<dt><code>SUDO_HOOK_RET_STOP</code></p>
<dd>The hook completed without error, stop processing hooks for this invocation. This can be used to replace the system implementation. For example, a <code>setenv</code> hook that operates on a private copy of the environment but leaves <code>environ</code> unchanged.</dl>
<p>  Note that it is very easy to create an infinite loop when hooking C library functions. For example, a <a href="/docs/linux/man/3-getenv/">getenv</a>(3) hook that calls the <a href="/docs/linux/man/3-snprintf/">snprintf</a>(3) function may create a loop if the <a href="/docs/linux/man/3-snprintf/">snprintf</a>(3) implementation calls <a href="/docs/linux/man/3-getenv/">getenv</a>(3) to check the locale. To prevent this, you may wish to use a static variable in the hook function to guard against nested calls. For example: </p>
<pre>static int in_progress = 0; /* avoid recursion */
if (in_progress)
 return SUDO_HOOK_RET_NEXT;
in_progress = 1;
...
in_progress = 0;
return SUDO_HOOK_RET_STOP;</pre>
<p>Hook API Version Macros</p>
<p>/* Hook API version major/minor */<br />
#define SUDO_HOOK_VERSION_MAJOR 1<br />
#define SUDO_HOOK_VERSION_MINOR 0<br />
#define SUDO_HOOK_VERSION SUDO_API_MKVERSION(SUDO_HOOK_VERSION_MAJOR,\<br />
SUDO_HOOK_VERSION_MINOR) For getters and setters see the Sx Policy plugin API .</p>
<h3>Event API</h3>
<p>When <code>sudo</code> runs a command, it uses an event loop to service signals and I/O. Events may be triggered based on time, a file or socket descriptor becoming ready, or due to receipt of a signal. Starting with API version 1.15, it is possible for a plugin to participate in this event loop by calling the Fn event_alloc function. <i>Event structure</i> Events are described by the following structure: </p>
<pre>typedef void (*sudo_plugin_ev_callback_t)(int fd, int what, void *closure);
struct sudo_plugin_event {
 int (*set)(struct sudo_plugin_event *pev, int fd, int events,
 sudo_plugin_ev_callback_t callback, void *closure);
 int (*add)(struct sudo_plugin_event *pev, struct timespec *timeout);
 int (*del)(struct sudo_plugin_event *pev);
 int (*pending)(struct sudo_plugin_event *pev, int events,
 struct timespec *ts);
 int (*fd)(struct sudo_plugin_event *pev);
 void (*setbase)(struct sudo_plugin_event *pev, void *base);
 void (*loopbreak)(struct sudo_plugin_event *pev);
 void (*free)(struct sudo_plugin_event *pev);
};</pre>
<p>The sudo_plugin_event struct contains the following function pointers:</p>
<dl>
<dt><code>Fn </code>set</p>
<dd>
<pre>int (*set)(struct sudo_plugin_event *pev, int fd, int events,
 sudo_plugin_ev_callback_t callback, void *closure);</pre>
<p>The Fn set function takes the following arguments:</p>
<dl>
<dt><code>struct sudo_plugin_event * Fa </code>pev</p>
<dd>A pointer to the struct sudo_plugin_event itself.</p>
<dt><code>Fa </code>fd</p>
<dd>The file or socket descriptor for I/O-based events or the signal number for signal events. For time-based events, Fa fd must be -1.</p>
<dt><code>Fa </code>events</p>
<dd>The following values determine what will trigger the event callback:</p>
<dl>
<dt><code>SUDO_PLUGIN_EV_TIMEOUT</code></p>
<dd>callback is run after the specified timeout expires</p>
<dt><code>SUDO_PLUGIN_EV_READ</code></p>
<dd>callback is run when the file descriptor is readable</p>
<dt><code>SUDO_PLUGIN_EV_WRITE</code></p>
<dd>callback is run when the file descriptor is writable</p>
<dt><code>SUDO_PLUGIN_EV_PERSIST</code></p>
<dd>event is persistent and remains enabled until explicitly deleted</p>
<dt><code>SUDO_PLUGIN_EV_SIGNAL</code></p>
<dd>callback is run when the specified signal is received</dl>
<p> The <code>SUDO_PLUGIN_EV_PERSIST</code> flag may be ORed with any of the event types. It is also possible to OR <code>SUDO_PLUGIN_EV_READ</code> and <code>SUDO_PLUGIN_EV_WRITE</code> together to run the callback when a descriptor is ready to be either read from or written to. All other event values are mutually exclusive.</p>
<dt><code>sudo_plugin_ev_callback_t Fa </code>callback</p>
<dd>
<pre>typedef void (*sudo_plugin_ev_callback_t)(int fd, int what,
 void *closure);</pre>
<p>The function to call when an event is triggered. The Fn callback function is run with the following arguments:</p>
<dl>
<dt><code>Fa </code>fd</p>
<dd>The file or socket descriptor for I/O-based events or the signal number for signal events.</p>
<dt><code>Fa </code>what</p>
<dd>The event type that triggered that callback. For events that have multiple event types (for example <code>SUDO_PLUGIN_EV_READ</code> and <code>SUDO_PLUGIN_EV_WRITE</code> or have an associated timeout, Fa what can be used to determine why the callback was run.</p>
<dt><code>Fa </code>closure</p>
<dd>The generic pointer that was specified in the Fn set function.</dl>
<dt><code>closure</code></p>
<dd>A generic pointer that will be passed to the callback function.</dl>
<p> The Fn set function returns 1 on success, and -1 if a error occurred.</p>
<dt><code>Fn </code>add</p>
<dd>
<pre>int (*add)(struct sudo_plugin_event *pev, struct timespec *timeout);</pre>
<p>The Fn add function adds the event Fa pev to <code>sudo &#8216;s</code> event loop. The event must have previously been initialized via the Fn set function. If the Fa timeout argument is not NULL, it should specify a (relative) timeout after which the event will be triggered if the main event criteria has not been met. This is often used to implement an I/O timeout where the event will fire if a descriptor is not ready within a certain time period. If the event is already present in the event loop, its Fa timeout will be adjusted to match the new value, if any. The Fn add function returns 1 on success, and -1 if a error occurred.</p>
<dt><code>Fn </code>del</p>
<dd>
<pre>int (*del)(struct sudo_plugin_event *pev);</pre>
<p>The Fn del function deletes the event Fa pev from <code>sudo &#8216;s</code> event loop. Deleted events can be added back via the Fn add function. The Fn del function returns 1 on success, and -1 if a error occurred.</p>
<dt><code>Fn </code>pending</p>
<dd>
<pre>int (*pending)(struct sudo_plugin_event *pev, int events,
 struct timespec *ts);</pre>
<p>The Fn pending function can be used to determine whether one or more events is pending. The Fa events argument specifies which events to check for. See the Fn set function for a list of valid event types. If <code>SUDO_PLUGIN_EV_TIMEOUT</code> is specified in <code>events</code> the event has an associated timeout and the Fa ts pointer is non-NULL, it will be filled in with the remaining time.</p>
<dt><code>Fn </code>fd</p>
<dd>
<pre>int (*fd)(struct sudo_plugin_event *pev);</pre>
<p>The Fn fd function returns the descriptor or signal number associated with the event Fa pev .</p>
<dt><code>Fn </code>setbase</p>
<dd>
<pre>void (*setbase)(struct sudo_plugin_event *pev, void *base);</pre>
<p>The Fn setbase function sets the underlying event Fa base for Fa pev to the specified value. This can be used to move an event created via Fn event_alloc to a new event loop allocated by sudo&#8217;s event subsystem. If Fa base is <code>NULL</code> Fa pev Ns &#8216;s event base is reset to the default value, which corresponds to <code>sudo &#8216;s</code> main event loop. Using this function requires linking the plugin with the sudo_util library. It is unlikely to be used outside of the <code>sudoers</code> plugin.</p>
<dt><code>Fn </code>loopbreak</p>
<dd>
<pre>void (*loopbreak)(struct sudo_plugin_event *pev);</pre>
<p>The Fn loopbreak function causes <code>sudo &#8216;s</code> event loop to exit immediately and the running command to be terminated.</p>
<dt><code>Fn </code>free</p>
<dd>
<pre>void (*free)(struct sudo_plugin_event *pev);</pre>
<p>The Fn free function deletes the event Fa pev from the event loop and frees the memory associated with it.</dl>
<h3>Remote command execution</h3>
<p>The <code>sudo</code> front-end does not support running remote commands. However, starting with <code>sudo</code> 1.8.8, the &#8211;<code>h</code> option may be used to specify a remote host that is passed to the policy plugin. A plugin may also accept a <i>runas_user</i> in the form of &#8220;user [at] hostname&#8221; which will work with older versions of <code>sudo</code> It is anticipated that remote commands will be supported by executing a &#8220;helper&#8221; program. The policy plugin should setup the execution environment such that the <code>sudo</code> front-end will run the helper which, in turn, will connect to the remote host and run the command. For example, the policy plugin could utilize <code>ssh</code> to perform remote command execution. The helper program would be responsible for running <code>ssh</code> with the proper options to use a private key or certificate that the remote host will accept and run a program on the remote host that would setup the execution environment accordingly. Note that remote <code>sudoedit</code> functionality must be handled by the policy plugin, not <code>sudo</code> itself as the front-end has no knowledge that a remote command is being executed. This may be addressed in a future revision of the plugin API.</p>
<h3>Conversation API</h3>
<p>If the plugin needs to interact with the user, it may do so via the Fn conversation function. A plugin should not attempt to read directly from the standard input or the user&#8217;s tty (neither of which are guaranteed to exist). The caller must include a trailing newline in <code>msg</code> if one is to be printed. A Fn printf Ns -style function is also available that can be used to display informational or error messages to the user, which is usually more convenient for simple messages where no use input is required. <i>Conversation function structures</i> The conversation function takes as arguments pointers to the following structures: </p>
<pre>struct sudo_conv_message {
#define SUDO_CONV_PROMPT_ECHO_OFF 0x0001 /* do not echo user input */
#define SUDO_CONV_PROMPT_ECHO_ON 0x0002 /* echo user input */
#define SUDO_CONV_ERROR_MSG 0x0003 /* error message */
#define SUDO_CONV_INFO_MSG 0x0004 /* informational message */
#define SUDO_CONV_PROMPT_MASK 0x0005 /* mask user input */
#define SUDO_CONV_PROMPT_ECHO_OK 0x1000 /* flag: allow echo if no tty */
#define SUDO_CONV_PREFER_TTY 0x2000 /* flag: use tty if possible */
 int msg_type;
 int timeout;
 const char *msg;
};
#define SUDO_CONV_REPL_MAX 1023
struct sudo_conv_reply {
 char *reply;
};
typedef int (*sudo_conv_callback_fn_t)(int signo, void *closure);
struct sudo_conv_callback {
 unsigned int version;
 void *closure;
 sudo_conv_callback_fn_t on_suspend;
 sudo_conv_callback_fn_t on_resume;
};</pre>
<p>Pointers to the Fn conversation and Fn printf Ns -style functions are passed in to the plugin&#8217;s Fn open function when the plugin is initialized. The following type definitions can be used in the declaration of the Fn open function: </p>
<pre>typedef int (*sudo_conv_t)(int num_msgs,
 const struct sudo_conv_message msgs[],
 struct sudo_conv_reply replies[], struct sudo_conv_callback *callback);
typedef int (*sudo_printf_t)(int msg_type, const char *fmt, ...);</pre>
<p>To use the Fn conversation function, the plugin must pass an array of <code>sudo_conv_message</code> and <code>sudo_conv_reply</code> structures. There must be a <code>struct sudo_conv_message</code> and <code>struct sudo_conv_reply</code> for each message in the conversation, that is, both arrays must have the same number of elements. Each <code>struct sudo_conv_reply</code> must have its <i>reply</i> member initialized to <code>NULL</code> The <code>struct sudo_conv_callback</code> pointer, if not <code>NULL</code> should contain function pointers to be called when the <code>sudo</code> process is suspended and/or resumed during conversation input. The Fa on_suspend and Fa on_resume functions are called with the signal that caused <code>sudo</code> to be suspended and the Fa closure pointer from the <code>struct sudo_conv_callback</code> These functions should return 0 on success and -1 on error. On error, the conversation will end and the conversation function will return a value of -1. The intended use is to allow the plugin to release resources, such as locks, that should not be held indefinitely while suspended and then reacquire them when the process is resumed. Note that the functions are not actually invoked from within a signal handler. The <i>msg_type</i> must be set to one of the following values:</p>
<dl>
<dt><code>SUDO_CONV_PROMPT_ECHO_OFF</code></p>
<dd>Prompt the user for input with echo disabled; this is generally used for passwords. The reply will be stored in the <i>replies</i> array, and it will never be <code>NULL</code></p>
<dt><code>SUDO_CONV_PROMPT_ECHO_ON</code></p>
<dd>Prompt the user for input with echo enabled. The reply will be stored in the <i>replies</i> array, and it will never be <code>NULL</code></p>
<dt><code>SUDO_CONV_ERROR_MSG</code></p>
<dd>Display an error message. The message is written to the standard error unless the <code>SUDO_CONV_PREFER_TTY</code> flag is set, in which case it is written to the user&#8217;s terminal if possible.</p>
<dt><code>SUDO_CONV_INFO_MSG</code></p>
<dd>Display a message. The message is written to the standard output unless the <code>SUDO_CONV_PREFER_TTY</code> flag is set, in which case it is written to the user&#8217;s terminal if possible.</p>
<dt><code>SUDO_CONV_PROMPT_MASK</code></p>
<dd>Prompt the user for input but echo an asterisk character for each character read. The reply will be stored in the <i>replies</i> array, and it will never be <code>NULL</code> This can be used to provide visual feedback to the user while reading sensitive information that should not be displayed.</dl>
<p> In addition to the above values, the following flag bits may also be set:</p>
<dl>
<dt><code>SUDO_CONV_PROMPT_ECHO_OK</code></p>
<dd>Allow input to be read when echo cannot be disabled when the message type is <code>SUDO_CONV_PROMPT_ECHO_OFF</code> or <code>SUDO_CONV_PROMPT_MASK</code> By default, <code>sudo</code> will refuse to read input if the echo cannot be disabled for those message types.</p>
<dt><code>SUDO_CONV_PREFER_TTY</code></p>
<dd>When displaying a message via <code>SUDO_CONV_ERROR_MSG</code> or <code>SUDO_CONV_INFO_MSG</code> try to write the message to the user&#8217;s terminal. If the terminal is unavailable, the standard error or standard output will be used, depending upon whether <code>SUDO_CONV_ERROR_MSG</code> or <code>SUDO_CONV_INFO_MSG</code> was used. The user&#8217;s terminal is always used when possible for input, this flag is only used for output.</dl>
<p> The <i>timeout</i> in seconds until the prompt will wait for no more input. A zero value implies an infinite timeout. The plugin is responsible for freeing the reply buffer located in each <code>struct sudo_conv_reply</code> if it is not <code>NULL</code> <code>SUDO_CONV_REPL_MAX</code> represents the maximum length of the reply buffer (not including the trailing NUL character). In practical terms, this is the longest password <code>sudo</code> will support. The Fn printf Ns -style function uses the same underlying mechanism as the Fn conversation function but only supports <code>SUDO_CONV_INFO_MSG</code> and <code>SUDO_CONV_ERROR_MSG</code> for the <i>msg_type</i> parameter. It can be more convenient than using the Fn conversation function if no user reply is needed and supports standard Fn printf escape sequences. See the sample plugin for an example of the Fn conversation function usage.</p>
<h3>Plugin invocation order</h3>
<p>As of <code>sudo</code> 1.9.0, the plugin Fn open and Fn close functions are called in the following order: </p>
<ol>
<li> audit open
<li> policy open
<li> approval open
<li> approval close
<li> I/O log open
<li> command runs
<li> command exits
<li> I/O log close
<li> policy close
<li> audit close
<li> sudo exits </ol>
<p> Prior to <code>sudo</code> 1.9.0, the I/O log Fn close function was called <i>after</i> the policy Fn close function.</p>
<h3>Sudoers group plugin API</h3>
<p>The <code>sudoers</code> plugin supports its own plugin interface to allow non-Unix group lookups. This can be used to query a group source other than the standard Unix group database. Two sample group plugins are bundled with <code>sudo</code> <i>group_file</i> and <i>system_group</i> are detailed in <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5). Third party group plugins include a QAS AD plugin available from Quest Software. A group plugin must declare and populate a <code>sudoers_group_plugin</code> struct in the global scope. This structure contains pointers to the functions that implement plugin initialization, cleanup, and group lookup. </p>
<pre>struct sudoers_group_plugin {
 unsigned int version;
 int (*init)(int version, sudo_printf_t sudo_printf,
 char *const argv[]);
 void (*cleanup)(void);
 int (*query)(const char *user, const char *group,
 const struct passwd *pwd);
};</pre>
<p>The <code>sudoers_group_plugin</code> struct has the following fields:</p>
<dl>
<dt><code>version</code></p>
<dd>The <code>version</code> field should be set to GROUP_API_VERSION. This allows <code>sudoers</code> to determine the API version the group plugin was built against.</p>
<dt><code>init</code></p>
<dd>
<pre>int (*init)(int version, sudo_printf_t plugin_printf,
 char *const argv[]);</pre>
<p>The Fn init function is called after <i>sudoers</i> has been parsed but before any policy checks. It returns 1 on success, 0 on failure (or if the plugin is not configured), and -1 if a error occurred. If an error occurs, the plugin may call the Fn plugin_printf function with <code>SUDO_CONF_ERROR_MSG</code> to present additional error information to the user. The function arguments are as follows:</p>
<dl>
<dt><code>version</code></p>
<dd>The version passed in by <code>sudoers</code> allows the plugin to determine the major and minor version number of the group plugin API supported by <code>sudoers</code></p>
<dt><code>plugin_printf</code></p>
<dd>A pointer to a Fn printf Ns -style function that may be used to display informational or error message to the user. Returns the number of characters printed on success and -1 on failure.</p>
<dt><code>argv</code></p>
<dd>A <code>NULL -terminated</code> array of arguments generated from the <i>group_plugin</i> option in <i>sudoers</i> If no arguments were given, <i>argv</i> will be <code>NULL</code></dl>
<dt><code>cleanup</code></p>
<dd>
<pre>void (*cleanup)();</pre>
<p>The Fn cleanup function is called when <code>sudoers</code> has finished its group checks. The plugin should free any memory it has allocated and close open file handles.</p>
<dt><code>query</code></p>
<dd>
<pre>int (*query)(const char *user, const char *group,
 const struct passwd *pwd);</pre>
<p>The Fn query function is used to ask the group plugin whether <i>user</i> is a member of <i>group</i> The function arguments are as follows:</p>
<dl>
<dt><code>user</code></p>
<dd>The name of the user being looked up in the external group database.</p>
<dt><code>group</code></p>
<dd>The name of the group being queried.</p>
<dt><code>pwd</code></p>
<dd>The password database entry for <i>user</i> if any. If <i>user</i> is not present in the password database, <i>pwd</i> will be <code>NULL</code></dl>
<pre><code>

Group API Version Macros



/* Sudoers group plugin version major/minor */
#define GROUP_API_VERSION_MAJOR 1
#define GROUP_API_VERSION_MINOR 0
#define GROUP_API_VERSION ((GROUP_API_VERSION_MAJOR &lt;&lt; 16) | \
GROUP_API_VERSION_MINOR)


For getters and setters see the
Sx Policy plugin API .</code></pre>
<h2>Plugin Api Changelog</h2>
<p>The following revisions have been made to the Sudo Plugin API.</p>
<dl>
<dt><code>Version 1.0</code></p>
<dd>Initial API version.</p>
<dt><code>Version 1.1 (sudo 1.8.0)</code></p>
<dd>The I/O logging plugin&#8217;s Fn open function was modified to take the <code>command_info</code> list as an argument.</p>
<dt><code>Version 1.2 (sudo 1.8.5)</code></p>
<dd>The Policy and I/O logging plugins&#8217; Fn open functions are now passed a list of plugin parameters if any are specified in sudo.conf5. </p>
<p> A simple hooks API has been introduced to allow plugins to hook in to the system&#8217;s environment handling functions. </p>
<p> The <code>init_session</code> Policy plugin function is now passed a pointer to the user environment which can be updated as needed. This can be used to merge in environment variables stored in the PAM handle before a command is run.</p>
<dt><code>Version 1.3 (sudo 1.8.7)</code></p>
<dd>Support for the <i>exec_background</i> entry has been added to the <code>command_info</code> list. </p>
<p> The <i>max_groups</i> and <i>plugin_dir</i> entries were added to the <code>settings</code> list. </p>
<p> The Fn version and Fn close functions are now optional. Previously, a missing Fn version or Fn close function would result in a crash. If no policy plugin Fn close function is defined, a default Fn close function will be provided by the <code>sudo</code> front-end that displays a warning if the command could not be executed. </p>
<p> The <code>sudo</code> front-end now installs default signal handlers to trap common signals while the plugin functions are run.</p>
<dt><code>Version 1.4 (sudo 1.8.8)</code></p>
<dd>The <i>remote_host</i> entry was added to the <code>settings</code> list.</p>
<dt><code>Version 1.5 (sudo 1.8.9)</code></p>
<dd>The <i>preserve_fds</i> entry was added to the <code>command_info</code> list.</p>
<dt><code>Version 1.6 (sudo 1.8.11)</code></p>
<dd>The behavior when an I/O logging plugin returns an error (-1) has changed. Previously, the <code>sudo</code> front-end took no action when the Fn log_ttyin , Fn log_ttyout , Fn log_stdin , Fn log_stdout , or Fn log_stderr function returned an error. </p>
<p> The behavior when an I/O logging plugin returns 0 has changed. Previously, output from the command would be displayed to the terminal even if an output logging function returned 0.</p>
<dt><code>Version 1.7 (sudo 1.8.12)</code></p>
<dd>The <i>plugin_path</i> entry was added to the <code>settings</code> list. </p>
<p> The <i>debug_flags</i> entry now starts with a debug file path name and may occur multiple times if there are multiple plugin-specific Debug lines in the sudo.conf5file.</p>
<dt><code>Version 1.8 (sudo 1.8.15)</code></p>
<dd>The <i>sudoedit_checkdir</i> and <i>sudoedit_follow</i> entries were added to the <code>command_info</code> list. The default value of <i>sudoedit_checkdir</i> was changed to true in sudo 1.8.16. </p>
<p> The sudo <i>conversation</i> function now takes a pointer to a <code>struct sudo_conv_callback</code> as its fourth argument. The <code>sudo_conv_t</code> definition has been updated to match. The plugin must specify that it supports plugin API version 1.8 or higher to receive a conversation function pointer that supports this argument.</p>
<dt><code>Version 1.9 (sudo 1.8.16)</code></p>
<dd>The <i>execfd</i> entry was added to the <code>command_info</code> list.</p>
<dt><code>Version 1.10 (sudo 1.8.19)</code></p>
<dd>The <i>umask</i> entry was added to the <code>user_info</code> list. The <i>iolog_group</i> <i>iolog_mode</i> and <i>iolog_user</i> entries were added to the <code>command_info</code> list.</p>
<dt><code>Version 1.11 (sudo 1.8.20)</code></p>
<dd>The <i>timeout</i> entry was added to the <code>settings</code> list.</p>
<dt><code>Version 1.12 (sudo 1.8.21)</code></p>
<dd>The <code>change_winsize</code> field was added to the io_plugin struct.</p>
<dt><code>Version 1.13 (sudo 1.8.26)</code></p>
<dd>The <code>log_suspend</code> field was added to the io_plugin struct.</p>
<dt><code>Version 1.14 (sudo 1.8.29)</code></p>
<dd>The <i>umask_override</i> entry was added to the <code>command_info</code> list.</p>
<dt><code>Version 1.15 (sudo 1.9.0)</code></p>
<dd>The <i>cwd_optional</i> entry was added to the <code>command_info</code> list. </p>
<p> The <i>event_alloc</i> field was added to the policy_plugin and io_plugin structs. </p>
<p> The Fa errstr argument was added to the policy and I/O plugin functions which the plugin function can use to return an error string. This string may be used by the audit plugin to report failure or error conditions set by the other plugins. </p>
<p> The Fn close function is now is called regardless of whether or not a command was actually executed. This makes it possible for plugins to perform cleanup even when a command was not run. </p>
<p> <code>SUDO_CONV_REPL_MAX</code> has increased from 255 to 1023 bytes. </p>
<p> Support for audit and approval plugins was added.</p>
<dt><code>Version 1.16 (sudo 1.9.3)</code></p>
<dd>Initial resource limit values were added to the <code>user_info</code> list. </p>
<p> The <i>cmnd_chroot</i> and <i>cmnd_cwd</i> enties were added to the <code>settings</code> list.</p>
<dt><code>Version 1.17 (sudo 1.9.4)</code></p>
<dd>The <i>event_alloc</i> field was added to the audit_plugin and approval_plugin structs.</p>
<dt><code>Version 1.18 (sudo 1.9.9)</code></p>
<dd>The policy may now set resource limit values in the <code>command_info</code> list.</dl>
<h2>See Also</h2>
<p>sudo.conf5, <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5), <a href="/docs/linux/man/8-sudo/">sudo</a>(8)</p>
<h2>Authors</h2>
<p>Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<blockquote><p> An Todd C. Miller </p></blockquote>
<p> See the CONTRIBUTORS file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/contributors.html)">https://www.sudo.ws/contributors.html)</a> for an exhaustive list of people who have contributed to <code>sudo</code></p>
<h2>Bugs</h2>
<p>If you feel you have found a bug in <code>sudo</code> please submit a bug report at <a rel="nofollow" href="https://bugzilla.sudo.ws/">https://bugzilla.sudo.ws/</a></p>
<h2>Support</h2>
<p>Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="https://www.sudo.ws/mailman/listinfo/sudo-users">https://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.</p>
<h2>Disclaimer</h2>
<p><code>sudo</code> is provided &#8220;AS IS&#8221; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the LICENSE file distributed with <code>sudo</code> or <a rel="nofollow" href="https://www.sudo.ws/license.html">https://www.sudo.ws/license.html</a> for complete details.</p>
