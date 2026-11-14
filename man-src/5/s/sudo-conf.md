---
title: "sudo-conf(5)"
name: "sudo-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sudo-conf/"
description: "sudo.conf – configuration for sudo front-end"
---

<p>Sudo 1.9.9</p>
<h2>Name</h2>
<p><code>sudo.conf</code> &#8211; configuration for sudo front-end</p>
<h2>Description</h2>
<p>The <code>sudo.conf</code> file is used to configure the <code>sudo</code> front-end. It is used to configure sudo plugins, plugin-agnostic path names, debug flags, and other settings. </p>
<p> The <code>sudo.conf</code> file supports the following directives, described in detail below.</p>
<dl>
<dt><code>Plugin</code></p>
<dd>an approval, audit, I/O logging, or security policy plugin</p>
<dt><code>Path</code></p>
<dd>a plugin-agnostic path</p>
<dt><code>Set</code></p>
<dd>a front-end setting, such as <i>disable_coredump</i> or <i>group_source</i></p>
<dt><code>Debug</code></p>
<dd>debug flags to aid in debugging <code>sudo</code> <code>sudoreplay</code> <code>visudo</code> and the <code>sudoers</code> plugin.</dl>
<p> The pound sign (`#&#8217; ) is used to indicate a comment. Both the comment character and any text after it, up to the end of the line, are ignored. </p>
<p> Long lines can be continued with a backslash (`\&#8217; ) as the last character on the line. Note that leading white space is removed from the beginning of lines even when the continuation character is used. </p>
<p> Non-comment lines that don&#8217;t begin with <code>Plugin</code> <code>Path</code> <code>Debug</code> or <code>Set</code> are silently ignored. </p>
<p> The <code>sudo.conf</code> file is always parsed in the &#8220;<code>C</code> &#8221; locale.</p>
<h3>Plugin configuration</h3>
<p><code>sudo</code> supports a plugin architecture for security policies and input/output logging. Third parties can develop and distribute their own policy and I/O logging plugins to work seamlessly with the <code>sudo</code> front-end. Plugins are dynamically loaded based on the contents of <code>sudo.conf.</code> </p>
<p> A <code>Plugin</code> line consists of the <code>Plugin</code> keyword, followed by the <i>symbol_name</i> and the <i>path</i> to the dynamic shared object that contains the plugin. The <i>symbol_name</i> is the name of the <code>approval_plugin</code> <code>audit_plugin</code> <code>io_plugin</code> or <code>policy_plugin</code> struct contained in the plugin. If a plugin implements multiple plugin types, there must be a <code>Plugin</code> line for each unique symbol name. The <i>path</i> may be fully qualified or relative. If not fully qualified, it is relative to the directory specified by the <i>plugin_dir</i> <code>Path</code> setting, which defaults to /usr/libexec/sudo In other words: </p>
<blockquote>
<pre>Plugin sudoers_policy sudoers.so</pre>
</blockquote>
<p> is equivalent to: </p>
<blockquote>
<pre>Plugin sudoers_policy /usr/libexec/sudo/sudoers.so</pre>
</blockquote>
<p> If the plugin was compiled statically into the <code>sudo</code> binary instead of being installed as a dynamic shared object, the <i>path</i> should be specified without a leading directory, as it does not actually exist in the file system. For example: </p>
<blockquote>
<pre>Plugin sudoers_policy sudoers.so</pre>
</blockquote>
<p> Starting with <code>sudo</code> 1.8.5, any additional parameters after the <i>path</i> are passed as arguments to the plugin&#8217;s <i>open</i> function. For example, to override the compile-time default sudoers file mode: </p>
<blockquote>
<pre>Plugin sudoers_policy sudoers.so sudoers_mode=0440</pre>
</blockquote>
<p> See the <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5) manual for a list of supported arguments. </p>
<p> The same dynamic shared object may contain multiple plugins, each with a different symbol name. The file must be owned by user-ID 0 and only writable by its owner. Because of ambiguities that arise from composite policies, only a single policy plugin may be specified. This limitation does not apply to I/O plugins. </p>
<p> If no <code>sudo.conf</code> file is present, or if it contains no <code>Plugin</code> lines, the <code>sudoers</code> plugin will be used as the default security policy, for I/O logging (if enabled by the policy), and for auditing. This is equivalent to the following: </p>
<blockquote>
<pre>Plugin sudoers_policy sudoers.so
Plugin sudoers_io sudoers.so
Plugin sudoers_audit sudoers.so</pre>
</blockquote>
<p> Starting with <code>sudo</code> version 1.9.1, some of the logging functionality of the <code>sudoers</code> plugin has been moved from the policy plugin to an audit plugin. To maintain compatibility with <code>sudo.conf</code> files from older <code>sudo</code> versions, if <code>sudoers</code> is configured as the security policy, it will be used as an audit plugin as well. This guarantees that the logging behavior will be consistnet with that of <code>sudo</code> versions 1.9.0 and below. </p>
<p> For more information on the <code>sudo</code> plugin architecture, see the sudo_plugin5 manual.</p>
<h3>Path settings</h3>
<p>A <code>Path</code> line consists of the <code>Path</code> keyword, followed by the name of the path to set and its value. For example: </p>
<blockquote>
<pre>Path intercept /usr/libexec/sudo/sudo_intercept.so
Path noexec /usr/libexec/sudo/sudo_noexec.so
Path askpass /usr/X11R6/bin/ssh-askpass</pre>
</blockquote>
<p> If no path name is specified, features relying on the specified setting will be disabled. Disabling <code>Path</code> settings is only supported in <code>sudo</code> version 1.8.16 and higher. </p>
<p> The following plugin-agnostic paths may be set in the /etc/sudo.conf file:</p>
<dl>
<dt><code>askpass</code></p>
<dd>The fully qualified path to a helper program used to read the user&#8217;s password when no terminal is available. This may be the case when <code>sudo</code> is executed from a graphical (as opposed to text-based) application. The program specified by <i>askpass</i> should display the argument passed to it as the prompt and write the user&#8217;s password to the standard output. The value of <i>askpass</i> may be overridden by the <code>SUDO_ASKPASS</code> environment variable.</p>
<dt><code>devsearch</code></p>
<dd>An ordered, colon-separated search path of directories to look in for device nodes. This is used when mapping the process&#8217;s tty device number to a device name on systems that do not provide such a mechanism. Sudo will <i>not</i> recurse into sub-directories. If terminal devices may be located in a sub-directory of /dev that path must be explicitly listed in <i>devsearch</i> The default value is <code>/dev/pts:/dev/vt:/dev/term:/dev/zcons:/dev/pty:/dev</code> </p>
<p> This option is ignored on systems that support either the Fn devname or Fn _ttyname_dev functions, for example BSD , macOS and Solaris.</p>
<dt><code>intercept</code></p>
<dd>The fully-qualified path to a shared library containing a wrappers for the Fn execl , Fn execle , Fn execlp , Fn execv , Fn execve , Fn execvp , and Fn execvpe library functions that intercepts attempts to run further commands and performs a policy check before allowing them to be executed. This is used to implement the <i>intercept</i> functionality on systems that support <code>LD_PRELOAD</code> or its equivalent. The default value is /usr/libexec/sudo/sudo_intercept.so</p>
<dt><code>noexec</code></p>
<dd>The fully-qualified path to a shared library containing wrappers for the Fn execl , Fn execle , Fn execlp , Fn exect , Fn execv , Fn execve , Fn execveat , Fn execvP , Fn execvp , Fn execvpe , Fn fexecve , Fn popen , Fn posix_spawn , Fn posix_spawnp , Fn system , and Fn wordexp library functions that prevent the execution of further commands. This is used to implement the <i>noexec</i> functionality on systems that support <code>LD_PRELOAD</code> or its equivalent. The default value is /usr/libexec/sudo/sudo_noexec.so</p>
<dt><code>plugin_dir</code></p>
<dd>The default directory to use when searching for plugins that are specified without a fully qualified path name. The default value is /usr/libexec/sudo</p>
<dt><code>sesh</code></p>
<dd>The fully-qualified path to the <code>sesh</code> binary. This setting is only used when <code>sudo</code> is built with SELinux support. The default value is /usr/libexec/sudo/sesh</dl>
<h3>Other settings</h3>
<p>The <code>sudo.conf</code> file also supports the following front-end settings:</p>
<dl>
<dt><code>disable_coredump</code></p>
<dd>Core dumps of <code>sudo</code> itself are disabled by default to prevent the disclosure of potentially sensitive information. To aid in debugging <code>sudo</code> crashes, you may wish to re-enable core dumps by setting &#8220;disable_coredump&#8221; to false in <code>sudo.conf</code> as follows: </p>
<blockquote>
<pre>Set disable_coredump false</pre>
</blockquote>
<p> All modern operating systems place restrictions on core dumps from set-user-ID processes like <code>sudo</code> so this option can be enabled without compromising security. To actually get a <code>sudo</code> core file you will likely need to enable core dumps for set-user-ID processes. On BSD and Linux systems this is accomplished in the <a href="/docs/linux/man/8-sysctl/">sysctl</a>(8) command. On Solaris, the <a href="//www.systutorials.com/docs/linux/man/1m-coreadm/">coreadm</a>(1m) command is used to configure core dump behavior. </p>
<p> This setting is only available in <code>sudo</code> version 1.8.4 and higher.</p>
<dt><code>developer_mode</code></p>
<dd>By default <code>sudo</code> refuses to load plugins which can be modified by other than the root user. The plugin should be owned by root and write access permissions should be disabled for &#8220;group&#8221; and &#8220;other&#8221; . To make development of a plugin easier, you can disable that by setting &#8220;developer_mode&#8221; option to true in <code>sudo.conf</code> as follows: </p>
<blockquote>
<pre>Set developer_mode true</pre>
</blockquote>
<p> Please note that this creates a security risk, so it is not recommended on critical systems such as a desktop machine for daily use, but is intended to be used in development environments (VM, container, etc). Before enabling developer mode, ensure you understand the implications. </p>
<p> This setting is only available in <code>sudo</code> version 1.9.0 and higher.</p>
<dt><code>group_source</code></p>
<dd><code>sudo</code> passes the invoking user&#8217;s group list to the policy and I/O plugins. On most systems, there is an upper limit to the number of groups that a user may belong to simultaneously (typically 16 for compatibility with NFS). On systems with the <a href="/docs/linux/man/1-getconf/">getconf</a>(1) utility, running: </p>
<blockquote><p><tt>getconf NGROUPS_MAX</tt></p></blockquote>
<p> will return the maximum number of groups. </p>
<p> However, it is still possible to be a member of a larger number of groups&#8211;they simply won&#8217;t be included in the group list returned by the kernel for the user. Starting with <code>sudo</code> version 1.8.7, if the user&#8217;s kernel group list has the maximum number of entries, <code>sudo</code> will consult the group database directly to determine the group list. This makes it possible for the security policy to perform matching by group name even when the user is a member of more than the maximum number of groups. </p>
<p> The <i>group_source</i> setting allows the administrator to change this default behavior. Supported values for <i>group_source</i> are:</p>
<dl>
<dt><code>static</code></p>
<dd>Use the static group list that the kernel returns. Retrieving the group list this way is very fast but it is subject to an upper limit as described above. It is &#8220;static&#8221; in that it does not reflect changes to the group database made after the user logs in. This was the default behavior prior to <code>sudo</code> 1.8.7.</p>
<dt><code>dynamic</code></p>
<dd>Always query the group database directly. It is &#8220;dynamic&#8221; in that changes made to the group database after the user logs in will be reflected in the group list. On some systems, querying the group database for all of a user&#8217;s groups can be time consuming when querying a network-based group database. Most operating systems provide an efficient method of performing such queries. Currently, <code>sudo</code> supports efficient group queries on AIX, BSD , HP-UX, Linux, macOS, and Solaris. This is the default behavior on macOS in <code>sudo</code> 1.9.6 and higher.</p>
<dt><code>adaptive</code></p>
<dd>Only query the group database if the static group list returned by the kernel has the maximum number of entries. This is the default behavior on systems other than macOS in <code>sudo</code> 1.8.7 and higher.</dl>
<p> For example, to cause <code>sudo</code> to only use the kernel&#8217;s static list of groups for the user: </p>
<blockquote>
<pre>Set group_source static</pre>
</blockquote>
<p> This setting is only available in <code>sudo</code> version 1.8.7 and higher.</p>
<dt><code>max_groups</code></p>
<dd>The maximum number of user groups to retrieve from the group database. Values less than one or larger than 1024 will be ignored. This setting is only used when querying the group database directly. It is intended to be used on systems where it is not possible to detect when the array to be populated with group entries is not sufficiently large. By default, <code>sudo</code> will allocate four times the system&#8217;s maximum number of groups (see above) and retry with double that number if the group database query fails. </p>
<p> This setting is only available in <code>sudo</code> version 1.8.7 and higher. It should not be required in <code>sudo</code> versions 1.8.24 and higher and may be removed in a later release.</p>
<dt><code>probe_interfaces</code></p>
<dd>By default, <code>sudo</code> will probe the system&#8217;s network interfaces and pass the IP address of each enabled interface to the policy plugin. This makes it possible for the plugin to match rules based on the IP address without having to query DNS. On Linux systems with a large number of virtual interfaces, this may take a non-negligible amount of time. If IP-based matching is not required, network interface probing can be disabled as follows: </p>
<blockquote>
<pre>Set probe_interfaces false</pre>
</blockquote>
<p> This setting is only available in <code>sudo</code> version 1.8.10 and higher.</dl>
<h3>Debug settings</h3>
<p><code>sudo</code> versions 1.8.4 and higher support a flexible debugging framework that can log what <code>sudo</code> is doing internally if there is a problem. </p>
<p> A <code>Debug</code> line consists of the <code>Debug</code> keyword, followed by the name of the program, plugin, or shared object to debug, the debug file name, and a comma-separated list of debug flags. The debug flag syntax used by <code>sudo</code> the <code>sudoers</code> plugin along with its associated programs and shared objects is <i>subsystem </i><code>@ </code><i>priority</i> but a third-party plugin is free to use a different format so long as it does not include a comma (`,&#8217; ) </p>
<p> Examples: </p>
<blockquote>
<pre>Debug sudo /var/log/sudo_debug all [at] warn,plugin [at] info</pre>
</blockquote>
<p> would log all debugging statements at the <i>warn</i> level and higher in addition to those at the <i>info</i> level for the plugin subsystem. </p>
<blockquote>
<pre>Debug sudo_intercept.so /var/log/intercept_debug all [at] debug</pre>
</blockquote>
<p> would log all debugging statements, regardless of level, for the sudo_intercept.so shared object that implements <code>sudo &#8216;s</code> intercept functionality. </p>
<p> As of <code>sudo</code> 1.8.12, multiple <code>Debug</code> entries may be specified per program. Older versions of <code>sudo</code> only support a single <code>Debug</code> entry per program. Plugin-specific <code>Debug</code> entries are also supported starting with <code>sudo</code> 1.8.12 and are matched by either the base name of the plugin that was loaded (for example <code>sudoers.so</code> or by the plugin&#8217;s fully-qualified path name. Previously, the <code>sudoers</code> plugin shared the same <code>Debug</code> entry as the <code>sudo</code> front-end and could not be configured separately. </p>
<p> The following priorities are supported, in order of decreasing severity: <i>crit , err , warn , notice , diag , info , trace</i> and <i>debug</i> Each priority, when specified, also includes all priorities higher than it. For example, a priority of <i>notice</i> would include debug messages logged at <i>notice</i> and higher. </p>
<p> The priorities <i>trace</i> and <i>debug</i> also include function call tracing which logs when a function is entered and when it returns. For example, the following trace is for the Fn get_user_groups function located in src/sudo.c: </p>
<blockquote>
<pre>sudo[123] -&gt; get_user_groups @ src/sudo.c:385
sudo[123] &lt;- get_user_groups @ src/sudo.c:429 := groups=10,0,5</pre>
</blockquote>
<p> When the function is entered, indicated by a right arrow `-&gt;&#8217; , the program, process ID, function, source file, and line number are logged. When the function returns, indicated by a left arrow `&lt;-&#8216; , the same information is logged along with the return value. In this case, the return value is a string. </p>
<p> The following subsystems are used by the <code>sudo</code> front-end:</p>
<dl>
<dt><i>all</i></p>
<dd>matches every subsystem</p>
<dt><i>args</i></p>
<dd>command line argument processing</p>
<dt><i>conv</i></p>
<dd>user conversation</p>
<dt><i>edit</i></p>
<dd>sudoedit</p>
<dt><i>event</i></p>
<dd>event subsystem</p>
<dt><i>exec</i></p>
<dd>command execution</p>
<dt><i>main</i></p>
<dd><code>sudo</code> main function</p>
<dt><i>netif</i></p>
<dd>network interface handling</p>
<dt><i>pcomm</i></p>
<dd>communication with the plugin</p>
<dt><i>plugin</i></p>
<dd>plugin configuration</p>
<dt><i>pty</i></p>
<dd>pseudo-terminal related code</p>
<dt><i>selinux</i></p>
<dd>SELinux-specific handling</p>
<dt><i>util</i></p>
<dd>utility functions</p>
<dt><i>utmp</i></p>
<dd>utmp handling</dl>
<p> The <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5) plugin includes support for additional subsystems.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/sudo.conf </code></p>
<dd><code>sudo</code> front-end configuration</dl>
<h2>Examples</h2>
<pre>#
# Default /etc/sudo.conf file
#
# Sudo plugins:
# Plugin plugin_name plugin_path plugin_options ...
#
# The plugin_path is relative to /usr/libexec/sudo unless
# fully qualified.
# The plugin_name corresponds to a global symbol in the plugin
# that contains the plugin interface structure.
# The plugin_options are optional.
#
# The sudoers plugin is used by default if no Plugin lines are present.
#Plugin sudoers_policy sudoers.so
#Plugin sudoers_io sudoers.so
#Plugin sudoers_audit sudoers.so
#
# Sudo askpass:
# Path askpass /path/to/askpass
#
# An askpass helper program may be specified to provide a graphical
# password prompt for &quot;sudo -A&quot; support. Sudo does not ship with its
# own askpass program but can use the OpenSSH askpass.
#
# Use the OpenSSH askpass
#Path askpass /usr/X11R6/bin/ssh-askpass
#
# Use the Gnome OpenSSH askpass
#Path askpass /usr/libexec/openssh/gnome-ssh-askpass
#
# Sudo device search path:
# Path devsearch /dev/path1:/dev/path2:/dev
#
# A colon-separated list of paths to check when searching for a user's
# terminal device.
#
#Path devsearch /dev/pts:/dev/vt:/dev/term:/dev/zcons:/dev/pty:/dev
#
# Sudo command interception:
# Path intercept /path/to/sudo_intercept.so
#
# Path to a shared library containing replacements for the execv()
# and execve() library functions that perform a policy check to verify
# the command is allowed and simply return an error if not. This is
# used to implement the &quot;intercept&quot; functionality on systems that
# support LD_PRELOAD or its equivalent.
#
# The compiled-in value is usually sufficient and should only be changed
# if you rename or move the sudo_intercept.so file.
#
#Path intercept /usr/libexec/sudo/sudo_intercept.so
#
# Sudo noexec:
# Path noexec /path/to/sudo_noexec.so
#
# Path to a shared library containing replacements for the execv()
# family of library functions that just return an error. This is
# used to implement the &quot;noexec&quot; functionality on systems that support
# LD_PRELOAD or its equivalent.
#
# The compiled-in value is usually sufficient and should only be changed
# if you rename or move the sudo_noexec.so file.
#
#Path noexec /usr/libexec/sudo/sudo_noexec.so
#
# Sudo plugin directory:
# Path plugin_dir /path/to/plugins
#
# The default directory to use when searching for plugins that are
# specified without a fully qualified path name.
#
#Path plugin_dir /usr/libexec/sudo
#
# Sudo developer mode:
# Set developer_mode true|false
#
# Allow loading of plugins that are owned by non-root or are writable
# by &quot;group&quot; or &quot;other&quot;. Should only be used during plugin development.
#Set developer_mode true
#
# Core dumps:
# Set disable_coredump true|false
#
# By default, sudo disables core dumps while it is executing (they
# are re-enabled for the command that is run).
# To aid in debugging sudo problems, you may wish to enable core
# dumps by setting &quot;disable_coredump&quot; to false.
#
#Set disable_coredump false
#
# User groups:
# Set group_source static|dynamic|adaptive
#
# Sudo passes the user's group list to the policy plugin.
# If the user is a member of the maximum number of groups (usually 16),
# sudo will query the group database directly to be sure to include
# the full list of groups.
#
# On some systems, this can be expensive so the behavior is configurable.
# The &quot;group_source&quot; setting has three possible values:
# static - use the user's list of groups returned by the kernel.
# dynamic - query the group database to find the list of groups.
# adaptive - if user is in less than the maximum number of groups.
# use the kernel list, else query the group database.
#
#Set group_source static
#
# Sudo interface probing:
# Set probe_interfaces true|false
#
# By default, sudo will probe the system's network interfaces and
# pass the IP address of each enabled interface to the policy plugin.
# On systems with a large number of virtual interfaces this may take
# a noticeable amount of time.
#
#Set probe_interfaces false
#
# Sudo debug files:
# Debug program /path/to/debug_log subsystem [at] priority[,subsyste [at] priority]
#
# Sudo and related programs support logging debug information to a file.
# The program is typically sudo, sudoers.so, sudoreplay, or visudo.
#
# Subsystems vary based on the program; &quot;all&quot; matches all subsystems.
# Priority may be crit, err, warn, notice, diag, info, trace, or debug.
# Multiple subsystem [at] priority may be specified, separated by a comma.
#
#Debug sudo /var/log/sudo_debug all [at] debug
#Debug sudoers.so /var/log/sudoers_debug all [at] debug</pre>
<h2>See Also</h2>
<p>sudo_plugin5, <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5), <a href="/docs/linux/man/8-sudo/">sudo</a>(8)</p>
<h2>History</h2>
<p>See the HISTORY file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/history.html)">https://www.sudo.ws/history.html)</a> for a brief history of sudo.</p>
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
