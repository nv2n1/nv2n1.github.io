---
title: "remctld(8)"
name: "remctld"
section: "8"
letter: "r"
url: "/docs/linux/man/8-remctld/"
description: "remctld – Server for remctl, a remote command execution utility"
---

<p>remctld &#8211; Server for remctl, a remote command execution utility</p>
<h2>Synopsis</h2>
<p>remctld [<code>-dFhmSvZ</code>] [<code>-b</code> <i>bind-address</i> [<code>-b</code> <i>bind-address</i> &#8230;]]<br />
&nbsp;<wbr>[<code>-f</code>&nbsp;<wbr><i>config</i>]&nbsp;<wbr>[<code>-k</code>&nbsp;<wbr><i>keytab</i>]&nbsp;<wbr>[<code>-P</code>&nbsp;<wbr><i>file</i>]&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr><i>port</i>]<br />
&nbsp;<wbr>[<code>-s</code>&nbsp;<wbr><i>service</i>]</p>
<h2>Description</h2>
<p><code>remctld</code> is the server for remctl. It accepts a connection from remctl, receives the command to execute and the arguments, verifies authorization of the user and executes the command, returning the result back to the client. All connections are authenticated using Kerberos GSS-API Kerberos, and all transmissions are also encrypted using the GSS-API privacy layer. </p>
<p> <code>remctld</code> is normally started using <code>tcpserver</code> or from <code>inetd</code>, but it may be run in stand-alone mode as a daemon using <code>-m</code>. Either <code>-s</code> must be given to use an alternate identity (which will require the same flag be used for <code>remctl</code> client invocations), or it must be run as root to read the host keytab file. <code>remctld</code> logs its activity using syslog (the daemon facility). </p>
<p> The location of the configuration file may be specified with the <code>-f</code> option. The default location is <i>/etc/remctl.conf</i>. For information on the format of the configuration file, see &#8220;<font SIZE="-1">CONFIGURATION FILE&#8221;</font> below. </p>
<p> When the command is run, several environment variables will be set providing information about the remote connection. See <font SIZE="-1">ENVIRONMENT</font> below for more information. </p>
<p> Command-line and configuration options and <font SIZE="-1">ACL</font> methods are annotated below with the version at which they were added. For version information for more general features, see <font SIZE="-1">COMPATIBILITY</font> below.</p>
<h2>Options</h2>
<p>The start of each option description is annotated with the version of <code>remctld</code> in which that option was added with its current meaning.</p>
<dl>
<dt><code>-b</code> <i>bind-address</i></p>
<dd>[2.17] When running as a standalone server, bind to the specified local address rather than listening on all interfaces. This option may be given multiple times to bind to multiple addresses. <i>bind-address</i> must be an <font SIZE="-1">IP</font> address (either IPv4 or IPv6), not a hostname. Only makes sense in combination with <code>-m</code>. </p>
<p> This option is ignored if <code>remctld</code> is passed already open sockets via the systemd socket activation protocol. In that case, the bind addresses of the sockets should be controlled via the systemd configuration.</p>
<dt><code>-d</code></p>
<dd>[1.10] Enable verbose debug logging to syslog (or to standard output if <code>-S</code> is also given).</p>
<dt><code>-F</code></p>
<dd>[2.8] Normally when running in stand-alone mode (<code>-m</code>), <code>remctld</code> backgrounds itself to run as a daemon, changes directory to <i>/</i>, and drops any controlling terminal. This flag suppresses this behavior, usually for debugging or so that <code>remctld</code> can be monitored by other processes.</p>
<dt><code>-f</code> <i>config</i></p>
<dd>[1.0] The configuration file for <code>remctld</code>, overriding the default path.</p>
<dt><code>-h</code></p>
<dd>[1.10] Show a brief usage message and then exit. This usage method will include a list of supported <font SIZE="-1">ACL</font> types and can be used to determine if optional <font SIZE="-1">ACL</font> methods were compiled into a given <code>remctld</code> build.</p>
<dt><code>-k</code> <i>keytab</i></p>
<dd>[2.8] Use <i>keytab</i> as the keytab for server credentials rather than the system default or the value of the <font SIZE="-1">KRB5_KTNAME</font> environment variable. Using <code>-k</code> just sets the <font SIZE="-1">KRB5_KTNAME</font> environment variable internally in the process.</p>
<dt><code>-m</code></p>
<dd>[2.8] Enable stand-alone mode. <code>remctld</code> will listen to its configured port and fork a new child for each incoming connection. By default, when this option is used, <code>remctld</code> also changes directory to <i>/</i>, backgrounds itself, and closes standard input, output, and error. To not background, pass <code>-F</code> as well. To not close standard output and error and continue using them for logging, pass <code>-S</code> as well. </p>
<p> To determine the port, <code>remctld</code> attempts to look up the <tt>&quot;remctl&quot;</tt> service in the local <i>/etc/services</i> file and uses the port defined there. If the <tt>&quot;remctl&quot;</tt> service could not be found, it uses 4373, the registered remctl port.</p>
<dt><code>-P</code> <i>file</i></p>
<dd>[2.0] When running in stand-alone mode (<code>-m</code>), write the <font SIZE="-1">PID</font> of <code>remctld</code> to <i>file</i>. This option is ignored unless <code>-m</code> is also given.</p>
<dt><code>-p</code> <i>port</i></p>
<dd>[1.0] When running in stand-alone mode, listen on port <i>port</i> rather than the default. This option does nothing unless used with <code>-m</code>. </p>
<p> This option is ignored if <code>remctld</code> is passed already open sockets via the systemd socket activation protocol. In that case, the listening port should be controlled via the systemd configuration.</p>
<dt><code>-S</code></p>
<dd>[2.3] Rather than logging to syslog, log debug and routine connection messages to standard output and error messages to standard error. This option is mostly useful for testing and debugging.</p>
<dt><code>-s</code> <i>service</i></p>
<dd>[1.0] Specifies which principal is used as the server identity for client authentication. The client must also use the same identity as the server identity for authentication to succeed. By default, <code>remctld</code> accepts any principal with a key in the default keytab file (which can be changed with the <code>-k</code> option). This is normally the most desirable behavior.</p>
<dt><code>-v</code></p>
<dd>[1.10] Print the version of <code>remctld</code> and exit.</p>
<dt><code>-Z</code></p>
<dd>[3.7] When <code>remctld</code> is running in stand-alone mode, after it has set up its network socket and is ready to answer requests, raise <font SIZE="-1">SIGSTOP. </font> This signals to upstart, when using <tt>&quot;expect stop&quot;</tt>, that the daemon is ready to accept connections, and upstart will raise <font SIZE="-1">SIGCONT</font> to allow <code>remctld</code> to continue. This option is probably only useful when using upstart as the init system. Only makes sense in combination with <code>-m</code>.</dl>
<h2>Configuration File</h2>
<p>The configuration file defines the allowed commands and specifies access control information. The configuration file format is lines of space- or tab-separated strings, where each line is: </p>
<pre> command subcommand executable [option=value ...] acl [acl ...]</pre>
<p>Each command consists of a command, a subcommand, and zero or more arguments. Each configuration line defines an acceptable command and subcommand (or, if <tt>&quot;ALL&quot;</tt> is used as mentioned below under <i>command</i> and <i>subcommand</i>, a set of commands). The first configuration line matching the received command is used, so list more specific entries before more general entries. </p>
<p> Blank lines and lines beginning with <tt>&quot;#&quot;</tt> are ignored. Lines can be continued on the next line by ending them with a backslash (<tt>&quot;\&quot;</tt>). Be aware that comments can be continued with a backslash as well. </p>
<p> As a special case, a line like: </p>
<pre> include file</pre>
<p>will include <i>file</i> as if its contents were pasted verbatim into the configuration file at that point. <i>file</i> may be a directory, in which case all files whose names do not contain a period found in that directory will be included (in no particular order). <i>file</i> should be a fully qualified path. </p>
<p> The meaning of the fields on each configuration line are:</p>
<dl>
<dt><i>command</i></p>
<dd>The command being issued or the special keyword <tt>&quot;ALL&quot;</tt>. Normally, related commands (such as all commands for managing a particular service) are grouped together as subcommands under one command. </p>
<p> If the keyword <tt>&quot;ALL&quot;</tt> is used instead of a specific subcommand, this line matches all commands with the given subcommand (so <tt>&quot;ALL ALL&quot;</tt> matches any command) and can be used to dispatch all commands to the same executable with the same ACLs. Since the first matching entry is used, list entries for specific commands first (if any) and then the <tt>&quot;ALL&quot;</tt> catch-all. </p>
<p> Note that while the subcommand is passed to the executable as a command-line option, the command is not. The command is available to the executable in the environment variable <font SIZE="-1">REMCTL_COMMAND </font>(see <font SIZE="-1">ENVIRONMENT</font> below). </p>
<p> The command <tt>&quot;help&quot;</tt> is handled specially if no such command is defined in the configuration file. See below under the <tt>&quot;help&quot;</tt> and <tt>&quot;summary&quot;</tt> options.</p>
<dt><i>subcommand</i></p>
<dd>The subcommand within the command being requested, such as <tt>&quot;release&quot;</tt> for the release function of the <font SIZE="-1">AFS</font> volume backend, or one of the special keywords <tt>&quot;ALL&quot;</tt> or <tt>&quot;EMPTY&quot;</tt>. </p>
<p> If the keyword <tt>&quot;ALL&quot;</tt> is used instead of a specific subcommand, this line matches all subcommands with the given command and can be used to dispatch all subcommands under that command to the same executable with the same ACLs. Since the first matching entry is used, list entries for specific services first (if any) and then the <tt>&quot;ALL&quot;</tt> catch-all. </p>
<p> If the keyword <tt>&quot;EMPTY&quot;</tt> is used instead of a specific subcommand, this line matches only commands where no subcommand was given. </p>
<p> The subcommand is always passed as the first argument to the executable program that is listed for that service unless no subcommand was given.</p>
<dt><i>executable</i></p>
<dd>The full path to the command executable to run for this command and subcommand combination. (See examples below.)</p>
<dt><i>option</i>=<i>value</i></p>
<dd>An option setting that applies to this command. Supported option settings, annotated with the version at which that option was added in its current form, are:</p>
<dl>
<dd>
<dl>
<dt>help=<i>arg</i></p>
<dd>[3.2] Specifies the argument for this command that will print help for a particular subcommand to standard output. </p>
<p> If remctld receives the command <tt>&quot;help&quot;</tt> with one or two arguments, and no <tt>&quot;help&quot;</tt> command is defined in the configuration file, the server will take the command arguments as a command and subcommand. It will then look through the configuration for a configuration line matching that command and subcommand with a <tt>&quot;help&quot;</tt> option set. If one is found and the user is authorized to run that command, the server will run the specified <i>executable</i> with the argument <i>arg</i> and second and optional third arguments taken from the arguments to the <tt>&quot;help&quot;</tt> command, sending the output back to the user. </p>
<p> This permits a standard interface to get additional help for a particular remctl command. Also see the <tt>&quot;summary&quot;</tt> option.</p>
<dt>logmask=<i>n</i>[,&#8230;]</p>
<dd>[1.4] Limit logging of command arguments. Any argument listed in the logmask list will have its value logged as &#8220;**MASKED**&#8221;. This is to avoid logging the arguments of commands that take private information such as passwords. The logmask list should contain argument numbers separated by commas, with the <i>subcommand</i> considered argument 1. The <i>command</i> argument cannot be masked. </p>
<p> For example, if the command is <tt>&quot;admin passwd </tt>username<tt> </tt>password<tt>&quot;</tt>, then you&#8217;d want to set logmask to <tt>3</tt>, so the password argument gets logged as <tt>&quot;**MASKED**&quot;</tt>. If the command is <tt>&quot;user passwd </tt>username<tt> </tt>old-password<tt> </tt>new-password<tt>&quot;</tt>, you&#8217;d want to set logmask to <tt>&quot;3,4&quot;</tt>.</p>
<dt>stdin=(<i>n</i> | &quot;last&quot;)</p>
<dd>[2.14] Specifies that the <i>n</i>th or last argument to the command be passed on standard input instead of on the command line. The value of this option must either be the number of argument to pass on standard input (with the <i>subcommand</i> considered argument 1) or the special value <tt>&quot;last&quot;</tt>, which indicates that the final argument (no matter how many there are) be passed on standard input. </p>
<p> The <i>command</i> cannot be passed on standard input, so <i>n</i> must be at least <tt>1</tt>. If this option is set to <tt>&quot;last&quot;</tt> and no arguments are given except the <i>command</i> and possibly the <i>subcommand</i>, nothing will be passed on standard input. </p>
<p> This option is used primarily for passing large amounts of data that may not fit on the command line or data that contains <font SIZE="-1">NUL</font> characters. It can also be used for arguments like passwords that shouldn&#8217;t be exposed on the command line. Only at most one argument may be passed on standard input to the command. Be aware that even if the <i>subcommand</i> is the designated argument to pass on standard input (<tt>&quot;stdin=1&quot;</tt>), the <i>subcommand</i> may not contain <font SIZE="-1">NUL</font> characters.</p>
<dt>summary=<i>arg</i></p>
<dd>[3.2] Specifies the argument for this command that will print a usage summary to standard output. </p>
<p> If remctld receives the command <tt>&quot;help&quot;</tt> with no arguments, and no <tt>&quot;help&quot;</tt> command is defined in the configuration file, the server will look through the configuration for any command with a <tt>&quot;summary&quot;</tt> option set. If this option is set, the <i>subcommand</i> is <tt>&quot;ALL&quot;</tt>, and the user is authorized to run the command, the server will run the specified <i>executable</i> with the argument <i>arg</i>, sending the output back to the user. It will do this for every command in the configuration that meets the above criteria. </p>
<p> This allows display of a summary of available commands to the user based on which commands that user is authorized to run. It&#8217;s a lightweight form of service discovery. Also see the <tt>&quot;help&quot;</tt> option. </p>
<p> As mentioned above, this option is only meaningful on configuration lines with a <i>subcommand</i> of <tt>&quot;ALL&quot;</tt>.</p>
<dt>user=(<i>username</i> | <i>uid</i>)</p>
<dd>[3.1] Run this command as the specified user, which can be given as either a username or as a <font SIZE="-1">UID. </font> Even if given as a <font SIZE="-1">UID,</font> the user must be found in the user database (searched via <i><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></i>(3)). <code>remctld</code> will run the command as the specified user, including that user&#8217;s primary and supplemental groups.</dl>
</dl>
<dl>
<dd></dl>
<dt><i>acl</i></p>
<dd>One or more entries of the form [<i>method</i>:]<i>data</i>, where <i>method</i> specifies an access control method to be used, and <i>data</i> contains parameters whose meaning depends on the method. If the method is omitted, the data is processed as described for the <tt>&quot;file&quot;</tt> method. </p>
<p> If <i>method</i> is omitted, <i>acl</i> must either begin with <tt>&quot;/&quot;</tt> or must not contain <tt>&quot;=&quot;</tt>. Otherwise, it will be parsed as an option instead. If there is any ambiguity, prepend the <i>method</i>. </p>
<p> Each entry is checked in order, and access is granted as soon as an entry matches. If no entry matches, access is denied. The following methods may supported; however, be aware that the availability of several <font SIZE="-1">ACL</font> types depends on whether <code>remctld</code> was built with that support. Each <font SIZE="-1">ACL</font> type is annotated with the version in which it was added.</p>
<dl>
<dd>
<dl>
<dt>file</p>
<dd>[2.13] The data is the full path of an <font SIZE="-1">ACL</font> file or to a directory containing <font SIZE="-1">ACL</font> files. Directories are handled as described for the include directive in configuration files. An <font SIZE="-1">ACL</font> file contains one entry per line, in the [<i>method</i>:]<i>data</i> form described above. Entries are handled exactly as if they had appeared in the configuration file except that the default method is <tt>&quot;princ&quot;</tt> instead of <tt>&quot;file&quot;</tt>. Blank lines and lines beginning with <tt>&quot;#&quot;</tt> are ignored in the <font SIZE="-1">ACL</font> files. </p>
<p> For backward compatibility, a line like: </p>
<pre> include [&lt;method&gt;:]&lt;data&gt;</pre>
<p>in an <font SIZE="-1">ACL</font> file behaves exactly as if the <tt>&quot;include&quot;</tt> directive had been omitted, except that the default method is <tt>&quot;file&quot;</tt>. Thus, writing: </p>
<pre> include &lt;path&gt;</pre>
<p>in an <font SIZE="-1">ACL</font> file is the same as writing: </p>
<pre> file:&lt;path&gt;</pre>
<p>and is handled identically to the include directive in configuration files.</p>
<dt>princ</p>
<dd>[2.13] The data is the name of a Kerberos v5 principal which is to be granted access, such as <tt>&quot;username [at] EXAMPLE.ORG&quot;</tt>.</p>
<dt>deny</p>
<dd>[2.13] This method is used to selectively deny access. The data is parsed as a [<i>method</i>:]<i>data</i> and evaluated as described above, with the default scheme being <tt>&quot;princ&quot;</tt>. If it matches, access is denied immediately without examining any further entries. Otherwise, processing continues. </p>
<p> Remember that access is granted as soon as an entry matches. For <tt>&quot;deny&quot;</tt> rules to be effective, they therefore must come before any ACLs they are intended to override. Be careful when using <tt>&quot;deny&quot;</tt> when including a directory of <font SIZE="-1">ACL</font> files, since the files in that directory are read in an undefined order (not in alphabetical order by filename). It&#8217;s best to explicitly include the file containing <tt>&quot;deny&quot;</tt> <font SIZE="-1">ACL</font> rules first. </p>
<p> Note that <tt>&quot;deny&quot;</tt> only denies access; it never grants it. Thus, deny alone does not grant access to anyone, and using deny on itself as in <tt>&quot;deny:deny:foo&quot;</tt> neither denies nor grants access to anyone.</p>
<dt>gput</p>
<dd>[2.13] This method is used to grant access based on the <font SIZE="-1">CMU GPUT </font>(Global Privileged User Table &#8212; see <i><a href="/docs/linux/man/5-gput/">gput</a></i>(5)). The data is either a <font SIZE="-1">GPUT</font> role name or a string of the form <i>group</i>[<i>xform</i>], where <i>group</i> is a <font SIZE="-1">GPUT</font> role name and <i>xform</i> is a <font SIZE="-1">GPUT</font> transform string. Access is granted if the user is a member of the specified <font SIZE="-1">GPUT</font> group, after applying either the optional <i>xform</i> or the default transform. </p>
<p> This method is supported only if <code>remctld</code> was compiled with <font SIZE="-1">GPUT</font> support by using the <tt>&quot;--with-gput&quot;</tt> configure option.</p>
<dt>localgroup</p>
<dd>[3.9] This method is used to grant or deny access based on membership in local <font SIZE="-1">UNIX</font> groups. The data is taken to be a name of a local system group. The user principal is converted to a local user name with <i><a href="/docs/linux/man/3-krb5_aname_to_localname/">krb5_aname_to_localname</a></i>(3) and then compared to the members of the given group. </p>
<p> For example, to allow access to the members of group <tt>&quot;goodguys&quot;</tt>, use an <font SIZE="-1">ACL</font> of <tt>&quot;localgroup:goodguys&quot;</tt> syntax. To deny access to the members of group <tt>&quot;badguys&quot;</tt>, use <tt>&quot;deny:localgroup:badguys&quot;</tt>. </p>
<p> <i>krb5_aname_to_localname()</i> follows local configuration rules to determine how to convert Kerberos principal to local users. If the realm of the principal is not in a local realm and is not otherwise covered by one of those rules, the principal will be unchanged, which will almost certainly mean that it will not be a member of any local group and access will be denied. </p>
<p> This method is supported only if <code>remctld</code> was built with Kerberos support and the <i><a href="/docs/linux/man/3-getgrnam_r/">getgrnam_r</a></i>(3) library function was supported by the C library when it was built.</p>
<dt>pcre</p>
<dd>[2.16] This method is used to grant or deny access based on Perl-compatible regular expressions. The data is taken to be a Perl-compatible regular expression and matched against the user identity. To deny access, use the <tt>&quot;deny:pcre:</tt>regex<tt>&quot;</tt> syntax. </p>
<p> This method is supported only if <code>remctld</code> was compiled with <font SIZE="-1">PCRE</font> support by using the <tt>&quot;--with-pcre&quot;</tt> configure option.</p>
<dt>regex</p>
<dd>[2.16] This method is used to grant or deny access based on <font SIZE="-1">POSIX</font> extended regular expressions. The data is taken to be a <font SIZE="-1">POSIX</font> extended regular expression (like those used by <code>egrep</code>) and matched against the user identity. To deny access, use the <tt>&quot;deny:regex:</tt>regex<tt>&quot;</tt> syntax. </p>
<p> This method is supported only if a library for POSIX-compatible regular expressions was found when <code>remctld</code> was built.</dl>
</dl>
<dl>
<dd>To see the list of <font SIZE="-1">ACL</font> types supported by a particular build of <code>remctld</code>, run <tt>&quot;remctld -h&quot;</tt>. </p>
<p> The keyword <font SIZE="-1">ANYUSER</font> may be used instead of the ACLs to allow access to all users. The user still needs to authenticate to <code>remctld</code>; this only affects authorization. This can be used for backend programs that want to check ACLs themselves and will retrieve the authenticated principal from the <font SIZE="-1">REMOTE_USER</font> environment variable. Note that <font SIZE="-1">ANYUSER</font> accepts <code>any</code> authenticated user, including cross-realm users from foreign Kerberos realms.</dl>
</dl>
<h2>Environment</h2>
<p><code>remctld</code> itself uses the following environment variables when run in stand-alone mode (<code>-m</code>):</p>
<dl>
<dt><font SIZE="-1">LISTEN_FDS</font></p>
<dd>
<dt><font SIZE="-1">LISTEN_PID</font></p>
<dd>If these environment variables are set, <code>remctld</code> will expect to be provided its listening sockets via the systemd socket activation protocol and will not attempt to bind its own sockets. For more details on the protocol, see <i><a href="/docs/linux/man/7-daemon/">daemon</a></i>(7) and <i><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></i>(3).</p>
<dt><font SIZE="-1">NOTIFY_SOCKET</font></p>
<dd>If this environment variable is set, <code>remctld</code> will notify the socket named in this variable when it is ready to accept incoming packets using the systemd status notification protocol. For more details, see <i><a href="/docs/linux/man/7-daemon/">daemon</a></i>(7) and <i><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></i>(3). </p>
<p> Note that using socket activation is recommended when running under systemd in stand-alone mode, and status notification is not necessary or useful when using socket activation.</dl>
<p> When running in stand-alone mode, these environment variables will be cleared by <code>remctld</code> before running any commands. </p>
<p> The following environment variables will be set for any commands run via <code>remctld</code> (annotated with the version at which they were added):</p>
<dl>
<dt><font SIZE="-1">REMOTE_USER</font></p>
<dd>
<dt><font SIZE="-1">REMUSER</font></p>
<dd>[1.0 for <font SIZE="-1">REMUSER, 2.1</font> for <font SIZE="-1">REMOTE_USER</font>] Set to the Kerberos principal of the authenticated client.</p>
<dt><font SIZE="-1">REMOTE_ADDR</font></p>
<dd>[2.1] The <font SIZE="-1">IP</font> address of the remote host. This may be IPv4 or IPv6.</p>
<dt><font SIZE="-1">REMOTE_HOST</font></p>
<dd>[2.1] The hostname of the remote host, if it was available. If reverse name resolution failed, this environment variable will not be set.</p>
<dt><font SIZE="-1">REMCTL_COMMAND</font></p>
<dd>[2.16] The command string that caused this command to be run. This variable will contain only the command, not the subcommand or any additional arguments (which are passed as command arguments).</dl>
<p> If the <code>-k</code> flag is used, <code>remctld</code> will also set <font SIZE="-1">KRB5_KTNAME</font> to the provided keytab path. This is primarily for communication with the GSS-API library, but this setting will also be inherited by any commands run by <code>remctld</code>.</p>
<h2>Examples</h2>
<p>Typically <code>remctld</code> is to be started as follows, where &#8220;hostname&#8221; is the machine where remctld will run, and 4373 is the port: </p>
<pre> tcpserver hostname 4373 remctld</pre>
<p>The equivalent line for <i>/etc/inetd.conf</i> is: </p>
<pre> 4373 stream tcp nowait root /usr/sbin/tcpd /usr/sbin/remctld</pre>
<p>or: </p>
<pre> remctl stream tcp nowait root /usr/sbin/tcpd /usr/sbin/remctld</pre>
<p>if the <tt>&quot;remctl&quot;</tt> service is listed in your <i>/etc/services</i> file. </p>
<p> To start <code>remctld</code> in stand-alone mode instead, run: </p>
<pre> remctld -m</pre>
<p>To start <code>remctld</code> in stand-alone mode in the foreground, use: </p>
<pre> remctld -F -m</pre>
<p>This is a typical invocation with systemd using socket activation. For upstart (with <tt>&quot;expect stop&quot;</tt>), use: </p>
<pre> remctld -F -m -Z</pre>
<p>Example configuration file: </p>
<pre> # Comments can be used like this.
 accounts create /usr/local/bin/doaccount /etc/acl/group1 \
 /etc/acl/group2
 accounts delete /usr/local/bin/doaccount /etc/acl/group3
 accounts view /usr/local/bin/doaccount ANYUSER
 accounts passwd /usr/local/bin/dopasswd logmask=3 /etc/acl/group1
 printing ALL /usr/local/bin/printthing /etc/acl/group2</pre>
<p>The commands <tt>&quot;accounts create&quot;</tt>, <tt>&quot;accounts delete&quot;</tt>, and so forth will all be passed to /usr/local/bin/doaccount with the first argument being the specific subcommand, with the exception of <tt>&quot;accounts passwd&quot;</tt>. That command will be passed to /usr/local/bin/dopasswd instead, but it will still get <tt>&quot;passwd&quot;</tt> as its first argument. The third argument to <tt>&quot;accounts passwd&quot;</tt> (presumably the password) will not be logged to syslog. All commands starting with <tt>&quot;printing&quot;</tt> will be passed to /usr/local/bin/printthing. </p>
<p> Example <font SIZE="-1">ACL</font> file: </p>
<pre> # This is a comment.
 deny:baduser [at] EXAMPLE.ORG
 file:/etc/remctl/acl/admins
 principal:service/admin [at] EXAMPLE.ORG
 service/other [at] EXAMPLE.ORG</pre>
<p>This <font SIZE="-1">ACL</font> file will reject <tt>&quot;baduser [at] EXAMPLE.ORG&quot;</tt> even if that user would have been allowed by one of the other <font SIZE="-1">ACL</font> rules. It will then grant access according to the <font SIZE="-1">ACL</font> entries in <i>/etc/remctl/acl/admins</i> and the specific principals <tt>&quot;service/admin [at] EXAMPLE.ORG&quot;</tt> and <tt>&quot;service/other [at] EXAMPLE.ORG&quot;</tt>. The last line takes advantage of the default <font SIZE="-1">ACL</font> method of <tt>&quot;principal&quot;</tt> when processing an <font SIZE="-1">ACL</font> file.</p>
<h2>Compatibility</h2>
<p>The version at which various command-line and configuration options and <font SIZE="-1">ACL</font> methods were added to <code>remctld</code> are noted in their descriptions. Below is the version information for more general features, in reverse order of when the feature was added. </p>
<p> Support for the systemd readiness protocol and socket activation, including honoring the environment variables <font SIZE="-1">LISTEN_FDS, LISTEN_PID,</font> and <font SIZE="-1">NOTIFY_SOCKET,</font> was added in version 3.7. </p>
<p> Special handling of the <tt>&quot;help&quot;</tt> and <tt>&quot;summary&quot;</tt> commands was added in version 3.2. </p>
<p> Support for the <tt>&quot;ALL&quot;</tt> keyword in the command field of the configuration file was added in version 2.15. (It has always been supported in the subcommand field.) </p>
<p> Support for the <tt>&quot;EMPTY&quot;</tt> keyword in the subcommand field of the configuration file was added in version 2.15. </p>
<p> Support for <font SIZE="-1">ACL</font> schemes and the <i>method</i>:<i>data</i> syntax was added in remctl 2.13. Prior versions of <code>remctld</code> expected only files in the main <code>remctld</code> configuration file, and only principals or lines starting with <tt>&quot;include&quot;</tt> in those files, without any <i>method</i>: prefixes. </p>
<p> The default listening port with the <code>-m</code> option was changed to the IANA-registered port of 4373 in version 2.11. </p>
<p> Support for IPv6 addresses in the <font SIZE="-1">REMOTE_ADDR</font> environment variable was added in version 2.4. </p>
<p> <code>remctld</code> used to set the environment variable <font SIZE="-1">SCPRINCIPAL</font> when running commands, for (partial) backward compatibility with <code>sysctld</code>, but stopped doing so in version 2.1. </p>
<p> <tt>&quot;include&quot;</tt> directives in <font SIZE="-1">ACL</font> files were added in version 1.11. <tt>&quot;include&quot;</tt> directives in configuration files were added in version 1.8.</p>
<h2>Caveats</h2>
<p>When using Heimdal with triple-DES keys and talking to old clients that only speak version one of the remctl protocol, <code>remctld</code> may have problems with <font SIZE="-1">MIC</font> verification. This doesn&#8217;t affect new clients and servers since the version two protocol doesn&#8217;t use MICs. If you are using Heimdal and run into <font SIZE="-1">MIC</font> verification problems, see the <font SIZE="-1">COMPATIBILITY</font> section of <i><a href="/docs/linux/man/3-gssapi/">gssapi</a></i>(3). </p>
<p> <code>remctld</code> does not itself impose any limits on the number of child processes or other system resources. You may want to set resource limits in your inetd server or with <code>ulimit</code> when running it as a standalone daemon or under <code>tcpserver</code>. </p>
<p> Command arguments may not contain <font SIZE="-1">NUL</font> characters and must be shorter than the operating system limit on the length of a command line since they&#8217;re passed to the command as command-line arguments. The exception is an argument passed via standard input using the <tt>&quot;stdin=&quot;</tt> option in the configuration file. At most one argument may be passed that way.</p>
<h2>Notes</h2>
<p>The remctl port number, 4373, was derived by tracing the diagonals of a <font SIZE="-1">QWERTY</font> keyboard up from the letters <tt>&quot;remc&quot;</tt> to the number row.</p>
<h2>Author</h2>
<p><code>remctld</code> was originally written by Anton Ushakov. Updates and current maintenance are done by Russ Allbery &lt;eagle [at] eyrie.org&gt;.</p>
<h2>Copyright And License</h2>
<p>Copyright 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2014 The Board of Trustees of the Leland Stanford Junior University </p>
<p> Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-remctl/">remctl</a></i>(1), <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3), <i><a href="/docs/linux/man/1-tcpserver/">tcpserver</a></i>(1) The current version of this program is available from its web page at &lt;<a rel="nofollow" href="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;. </p>
