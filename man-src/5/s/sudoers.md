---
title: "sudoers(5)"
name: "sudoers"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sudoers/"
description: "sudoers – default sudo security policy plugin"
---

<p>Sudo 1.9.9</p>
<h2>Name</h2>
<p><code>sudoers</code> &#8211; default sudo security policy plugin</p>
<h2>Description</h2>
<p>The <code>sudoers</code> policy plugin determines a user&#8217;s <code>sudo</code> privileges. It is the default <code>sudo</code> policy plugin. The policy is driven by the /etc/sudoers file or, optionally, in LDAP. The policy format is described in detail in the Sx SUDOERS FILE FORMAT section. For information on storing <code>sudoers</code> policy information in LDAP, please see sudoers.ldap5.</p>
<h3>Configuring sudo.conf for sudoers</h3>
<p><code>sudo</code> consults the sudo.conf5 file to determine which plugins to load. If no sudo.conf5 file is present, or if it contains no <code>Plugin</code> lines, <code>sudoers</code> will be used for auditing, policy decisions and I/O logging. To explicitly configure sudo.conf5 to use the <code>sudoers</code> plugin, the following configuration can be used. </p>
<blockquote>
<pre>Plugin sudoers_audit sudoers.so
Plugin sudoers_policy sudoers.so
Plugin sudoers_io sudoers.so</pre>
</blockquote>
<p> Starting with <code>sudo</code> 1.8.5, it is possible to specify optional arguments to the <code>sudoers</code> plugin in the sudo.conf5 file. Plugin arguments, if any, should be listed after the path to the plugin (i.e., after sudoers.so ) The arguments are only effective for the plugin that opens (and parses) the <i>sudoers</i> file. For <code>sudo</code> version 1.9.1 and higher, this is the <i>sudoers_audit</i> plugin. For older versions, it is the <i>sudoers_policy</i> plugin. Multiple arguments may be specified, separated by white space. For example: </p>
<blockquote>
<pre>Plugin sudoers_audit sudoers.so sudoers_mode=0400 error_recovery=false</pre>
</blockquote>
<p> The following plugin arguments are supported:</p>
<dl>
<dt><code>error_recovery=bool</code></p>
<dd>The <i>error_recovery</i> argument can be used to control whether <code>sudoers</code> should attempt to recover from syntax errors in the <i>sudoers</i> file. If set to <i>true</i> (the default), <code>sudoers</code> will try to recover from a syntax error by discarding the portion of the line that contains the error until the end of the line. A value of <i>false</i> will disable error recovery. Prior to version 1.9.3, no error recovery was performed.</p>
<dt><code>ldap_conf=pathname</code></p>
<dd>The <i>ldap_conf</i> argument can be used to override the default path to the ldap.conf file.</p>
<dt><code>ldap_secret=pathname</code></p>
<dd>The <i>ldap_secret</i> argument can be used to override the default path to the ldap.secret file.</p>
<dt><code>sudoers_file=pathname</code></p>
<dd>The <i>sudoers_file</i> argument can be used to override the default path to the <i>sudoers</i> file.</p>
<dt><code>sudoers_uid=user-ID</code></p>
<dd>The <i>sudoers_uid</i> argument can be used to override the default owner of the sudoers file. It should be specified as a numeric user-ID.</p>
<dt><code>sudoers_gid=group-ID</code></p>
<dd>The <i>sudoers_gid</i> argument can be used to override the default group of the sudoers file. It must be specified as a numeric group-ID (not a group name).</p>
<dt><code>sudoers_mode=mode</code></p>
<dd>The <i>sudoers_mode</i> argument can be used to override the default file mode for the sudoers file. It should be specified as an octal value.</dl>
<p> For more information on configuring sudo.conf5, please refer to its manual.</p>
<h3>User Authentication</h3>
<p>The <code>sudoers</code> security policy requires that most users authenticate themselves before they can use <code>sudo</code> A password is not required if the invoking user is root, if the target user is the same as the invoking user, or if the policy has disabled authentication for the user or command. Unlike <a href="/docs/linux/man/1-su/">su</a>(1), when <code>sudoers</code> requires authentication, it validates the invoking user&#8217;s credentials, not the target user&#8217;s (or root&#8217;s) credentials. This can be changed via the <i>rootpw</i> <i>targetpw</i> and <i>runaspw</i> flags, described later. If a user who is not listed in the policy tries to run a command via <code>sudo</code> mail is sent to the proper authorities. The address used for such mail is configurable via the <i>mailto</i> Defaults entry (described later) and defaults to <code>root</code> Note that no mail will be sent if an unauthorized user tries to run <code>sudo</code> with the &#8211;<code>l</code> or &#8211;<code>v</code> option unless there is an authentication error and either the <i>mail_always</i> or <i>mail_badpass</i> flags are enabled. This allows users to determine for themselves whether or not they are allowed to use <code>sudo</code> By default, all attempts to run <code>sudo</code> (successful or not) are logged, regardless of whether or not mail is sent. If <code>sudo</code> is run by root and the <code>SUDO_USER</code> environment variable is set, the <code>sudoers</code> policy will use this value to determine who the actual user is. This can be used by a user to log commands through sudo even when a root shell has been invoked. It also allows the &#8211;<code>e</code> option to remain useful even when invoked via a sudo-run script or program. Note, however, that the <i>sudoers</i> file lookup is still done for root, not the user specified by <code>SUDO_USER</code> <code>sudoers</code> uses per-user time stamp files for credential caching. Once a user has been authenticated, a record is written containing the user-ID that was used to authenticate, the terminal session ID, the start time of the session leader (or parent process) and a time stamp (using a monotonic clock if one is available). The user may then use <code>sudo</code> without a password for a short period of time Po <code>15</code> minutes unless overridden by the <i>timestamp_timeout</i> option Pc . By default, <code>sudoers</code> uses a separate record for each terminal, which means that a user&#8217;s login sessions are authenticated separately. The <i>timestamp_type</i> option can be used to select the type of time stamp record <code>sudoers</code> will use.</p>
<h3>Logging</h3>
<p>By default, <code>sudoers</code> logs both successful and unsuccessful attempts (as well as errors). The <i>log_allowed</i> and <i>log_denied</i> flags can be used to control this behavior. Messages can be logged to <a href="/docs/linux/man/3-syslog/">syslog</a>(3), a log file, or both. The default is to log to <a href="/docs/linux/man/3-syslog/">syslog</a>(3) but this is configurable via the <i>syslog</i> and <i>logfile</i> settings. See Sx LOG FORMAT for a description of the log file format. <code>sudoers</code> is also capable of running a command in a pseudo-terminal and logging all input and/or output. The standard input, standard output, and standard error can be logged even when not associated with a terminal. I/O logging is not on by default but can be enabled using the <i>log_input</i> and <i>log_output</i> options as well as the <code>LOG_INPUT</code> and <code>LOG_OUTPUT</code> command tags. See Sx I/O LOG FILES for details on how I/O log files are stored. Starting with version 1.9, the <i>log_servers</i> setting may be used to send event and I/O log data to a remote server running <code>sudo_logsrvd</code> or another service that implements the protocol described by sudo_logsrv.proto5.</p>
<h3>Command environment</h3>
<p>Since environment variables can influence program behavior, <code>sudoers</code> provides a means to restrict which variables from the user&#8217;s environment are inherited by the command to be run. There are two distinct ways <code>sudoers</code> can deal with environment variables. By default, the <i>env_reset</i> flag is enabled. This causes commands to be executed with a new, minimal environment. On AIX (and Linux systems without PAM), the environment is initialized with the contents of the /etc/environment file. The <code>HOME</code> <code>MAIL</code> <code>SHELL</code> <code>LOGNAME</code> and <code>USER</code> environment variables are initialized based on the target user and the <code>SUDO_*</code> variables are set based on the invoking user. Additional variables, such as <code>DISPLAY</code> <code>PATH</code> and <code>TERM</code> are preserved from the invoking user&#8217;s environment if permitted by the <i>env_check</i> or <i>env_keep</i> options. A few environment variables are treated specially. If the <code>PATH</code> and <code>TERM</code> variables are not preserved from the user&#8217;s environment, they will be set to default values. The <code>LOGNAME</code> and <code>USER</code> are handled as a single entity. If one of them is preserved (or removed) from the user&#8217;s environment, the other will be as well. If <code>LOGNAME</code> and <code>USER</code> are to be preserved but only one of them is present in the user&#8217;s environment, the other will be set to the same value. This avoids an inconsistent environment where one of the variables describing the user name is set to the invoking user and one is set to the target user. Environment variables with a value beginning with <code>()</code> are removed unless both the name and value parts are matched by <i>env_keep</i> or <i>env_check</i> as they may be interpreted as functions by the <code>bash</code> shell. Prior to version 1.8.11, such variables were always removed. If, however, the <i>env_reset</i> flag is disabled, any variables not explicitly denied by the <i>env_check</i> and <i>env_delete</i> options are allowed and their values are inherited from the invoking process. Prior to version 1.8.21, environment variables with a value beginning with <code>()</code> were always removed. Beginning with version 1.8.21, a pattern in <i>env_delete</i> is used to match <code>bash</code> shell functions instead. Since it is not possible to block all potentially dangerous environment variables, use of the default <i>env_reset</i> behavior is encouraged. Environment variables specified by <i>env_check</i> <i>env_delete</i> or <i>env_keep</i> may include one or more `*&#8217; characters which will match zero or more characters. No other wildcard characters are supported. </p>
<pre><code>By default, environment variables are matched by name.
However, if the pattern includes an equal sign
(`='

)


both the variables name and value must match.
For example, a
bash

shell function could be matched as follows:


env_keep += &quot;BASH_FUNC_my_func%%=()*&quot;</code></pre>
<p> Without the &#8220;<code>=()*</code> &#8221; suffix, this would not match, as <code>bash</code> shell functions are not preserved by default. The complete list of environment variables that are preserved or removed, as modified by global Defaults parameters in <i>sudoers</i> is displayed when <code>sudo</code> is run by root with the &#8211;<code>V</code> option. Please note that the list of environment variables to remove varies based on the operating system <code>sudo</code> is running on. Other <code>sudoers</code> options may influence the command environment, such as <i>always_set_home</i> <i>secure_path</i> <i>set_logname</i> and <i>set_home</i> On systems that support PAM where the <code>pam_env</code> module is enabled for <code>sudo</code> variables in the PAM environment may be merged in to the environment. If a variable in the PAM environment is already present in the user&#8217;s environment, the value will only be overridden if the variable was not preserved by <code>sudoers.</code> When <i>env_reset</i> is enabled, variables preserved from the invoking user&#8217;s environment by the <i>env_keep</i> list take precedence over those in the PAM environment. When <i>env_reset</i> is disabled, variables present the invoking user&#8217;s environment take precedence over those in the PAM environment unless they match a pattern in the <i>env_delete</i> list. Note that the dynamic linker on most operating systems will remove variables that can control dynamic linking from the environment of set-user-ID executables, including <code>sudo</code> Depending on the operating system this may include <code>_RLD*</code> <code>DYLD_*</code> <code>LD_*</code> <code>LDR_*</code> <code>LIBPATH</code> <code>SHLIB_PATH</code> and others. These type of variables are removed from the environment before <code>sudo</code> even begins execution and, as such, it is not possible for <code>sudo</code> to preserve them. As a special case, if the &#8211;<code>i</code> option (initial login) is specified, <code>sudoers</code> will initialize the environment regardless of the value of <i>env_reset</i> The <code>DISPLAY</code> <code>PATH</code> and <code>TERM</code> variables remain unchanged; <code>HOME</code> <code>MAIL</code> <code>SHELL</code> <code>USER</code> and <code>LOGNAME</code> are set based on the target user. On AIX (and Linux systems without PAM), the contents of /etc/environment are also included. All other environment variables are removed unless permitted by <i>env_keep</i> or <i>env_check</i> described above. Finally, the <i>restricted_env_file</i> and <i>env_file</i> files are applied, if present. The variables in <i>restricted_env_file</i> are applied first and are subject to the same restrictions as the invoking user&#8217;s environment, as detailed above. The variables in <i>env_file</i> are applied last and are not subject to these restrictions. In both cases, variables present in the files will only be set to their specified values if they would not conflict with an existing environment variable.</p>
<h2>Sudoers File Format</h2>
<p>The <i>sudoers</i> file is composed of two types of entries: aliases (basically variables) and user specifications (which specify who may run what). </p>
<p> When multiple entries match for a user, they are applied in order. Where there are multiple matches, the last match is used (which is not necessarily the most specific match). </p>
<p> The <i>sudoers</i> file grammar will be described below in Extended Backus-Naur Form (EBNF). Don&#8217;t despair if you are unfamiliar with EBNF; it is fairly simple, and the definitions below are annotated.</p>
<h3>Resource limits</h3>
<p>By default, <code>sudoers</code> uses the operating system&#8217;s native method of setting resource limits for the target user. On Linux systems, resource limits are usually set by the <code>pam_limits.so</code> PAM module. On some BSD systems, the /etc/login.conf file specifies resource limits for the user. On AIX systems, resource limits are configured in the /etc/security/limits file. If there is no system mechanism to set per-user resource limits, the command will run with the same limits as the invoking user. The one exception to this is the core dump file size, which is set by <code>sudoers</code> to 0 by default. Disabling core dumps by default makes it possible to avoid potential security problems where the core file is treated as trusted input. </p>
<p> Resource limits may also be set in the <i>sudoers</i> file itself, in which case they override those set by the system. See the <i>rlimit_as,</i> <i>rlimit_core,</i> <i>rlimit_cpu,</i> <i>rlimit_data,</i> <i>rlimit_fsize,</i> <i>rlimit_locks,</i> <i>rlimit_memlock,</i> <i>rlimit_nofile,</i> <i>rlimit_nproc,</i> <i>rlimit_rss,</i> <i>rlimit_stack</i> options described below. Resource limits in <code>sudoers</code> may be specified in one of the following formats:</p>
<dl>
<dt><code>&#8220;value&#8221; </code></p>
<dd>Both the soft and hard resource limits are set to the same value. The special value &#8220;infinity&#8221; can be used to indicate that the value is unlimited.</p>
<dt><code>&#8220;soft,hard&#8221; </code></p>
<dd>Two comma-separated values. The soft limit is set to the first value and the hard limit is set to the second. Both values must either be enclosed in a set of double quotes, or the comma must be escaped with a backslash (`\&#8217; ) The special value &#8220;infinity&#8221; may be used in place of either value.</p>
<dt><code>&#8220;default&#8221; </code></p>
<dd>The default resource limit for the user will be used. This may be a user-specific value (see above) or the value of the resource limit when <code>sudo</code> was invoked for systems that don&#8217;t support per-user limits.</p>
<dt><code>&#8220;user&#8221; </code></p>
<dd>The invoking user&#8217;s resource limits will be preserved when running the command.</dl>
<p> For example, to restore the historic core dump file size behavior, a line like the following may be used. </p>
<blockquote><p><tt>Defaults rlimit_core=default</tt></p></blockquote>
<p> Resource limits in <code>sudoers</code> are only supported by version 1.8.7 or higher.</p>
<h3>Quick guide to EBNF</h3>
<p>EBNF is a concise and exact way of describing the grammar of a language. Each EBNF definition is made up of <i>production rules</i> E.g., </p>
<p> <code>symbol ::= definition | alternate1 | alternate2 &#8230;</code> </p>
<p> Each <i>production rule</i> references others and thus makes up a grammar for the language. EBNF also contains the following operators, which many readers will recognize from regular expressions. Do not, however, confuse them with &#8220;wildcard&#8221; characters, which have different meanings.</p>
<dl>
<dt><code>?</code></p>
<dd>Means that the preceding symbol (or group of symbols) is optional. That is, it may appear once or not at all.</p>
<dt><code>*</code></p>
<dd>Means that the preceding symbol (or group of symbols) may appear zero or more times.</p>
<dt><code>+</code></p>
<dd>Means that the preceding symbol (or group of symbols) may appear one or more times.</dl>
<p> Parentheses may be used to group symbols together. For clarity, we will use single quotes (&#8221;) to designate what is a verbatim character string (as opposed to a symbol name).</p>
<h3>Aliases</h3>
<p>There are four kinds of aliases: <code>User_Alias</code> <code>Runas_Alias</code> <code>Host_Alias</code> and <code>Cmnd_Alias</code> Beginning with <code>sudo</code> 1.9.0, <code>Cmd_Alias</code> may be used in place of <code>Cmnd_Alias</code> if desired. </p>
<pre>Alias ::= 'User_Alias' User_Alias_Spec (':' User_Alias_Spec)* |
 'Runas_Alias' Runas_Alias_Spec (':' Runas_Alias_Spec)* |
 'Host_Alias' Host_Alias_Spec (':' Host_Alias_Spec)* |
 'Cmnd_Alias' Cmnd_Alias_Spec (':' Cmnd_Alias_Spec)* |
 'Cmd_Alias' Cmnd_Alias_Spec (':' Cmnd_Alias_Spec)*
User_Alias ::= NAME
User_Alias_Spec ::= User_Alias '=' User_List
Runas_Alias ::= NAME
Runas_Alias_Spec ::= Runas_Alias '=' Runas_List
Host_Alias ::= NAME
Host_Alias_Spec ::= Host_Alias '=' Host_List
Cmnd_Alias ::= NAME
Cmnd_Alias_Spec ::= Cmnd_Alias '=' Cmnd_List
NAME ::= [A-Z]([A-Z][0-9]_)*</pre>
<p>Each <i>alias</i> definition is of the form </p>
<pre>Alias_Type NAME = item1, item2, ...</pre>
<p>where <i>Alias_Type</i> is one of <code>User_Alias</code> <code>Runas_Alias</code> <code>Host_Alias</code> or <code>Cmnd_Alias</code> A <code>NAME</code> is a string of uppercase letters, numbers, and underscore characters (`_&#8217; ) A <code>NAME</code> <code>must</code> start with an uppercase letter. It is possible to put several alias definitions of the same type on a single line, joined by a colon (`:&#8217; ) E.g., </p>
<pre>Alias_Type NAME = item1, item2, item3 : NAME = item4, item5</pre>
<p>It is a syntax error to redefine an existing <i>alias</i> It is possible to use the same name for <i>aliases</i> of different types, but this is not recommended. </p>
<p> The definitions of what constitutes a valid <i>alias</i> member follow. </p>
<pre>User_List ::= User |
 User ',' User_List
User ::= '!'* user name |
 '!'* #user-ID |
 '!'* %group |
 '!'* %#group-ID |
 '!'* +netgroup |
 '!'* %:nonunix_group |
 '!'* %:#nonunix_gid |
 '!'* User_Alias</pre>
<p>A <code>User_List</code> is made up of one or more user names, user-IDs (prefixed with `#&#8217; ) , system group names and IDs (prefixed with `%&#8217; and `%#&#8217; respectively), netgroups (prefixed with `+&#8217; ) , non-Unix group names and IDs (prefixed with `%:&#8217; and `%:#&#8217; respectively), and <code>User_Alias es.</code> Each list item may be prefixed with zero or more `!&#8217; operators. An odd number of `!&#8217; operators negate the value of the item; an even number just cancel each other out. User netgroups are matched using the user and domain members only; the host member is not used when matching. </p>
<p> A <code>user name</code> <code>user-ID</code> <code>group</code> <code>group-ID</code> <code>netgroup</code> <code>nonunix_group</code> or <code>nonunix_gid</code> may be enclosed in double quotes to avoid the need for escaping special characters. Alternately, special characters may be specified in escaped hex mode, e.g.,   for space. When using double quotes, any prefix characters must be included inside the quotes. </p>
<p> The actual <code>nonunix_group</code> and <code>nonunix_gid</code> syntax depends on the underlying group provider plugin. For instance, the QAS AD plugin supports the following formats: </p>
<ul>
<li> Group in the same domain: &quot;%:Group Name&quot;
<li> Group in any domain: &quot;%:Group Name [at] FULLY.QUALIFIED.DOMAIN&quot;
<li> Group SID: &quot;%:S-1-2-34-5678901234-5678901234-5678901234-567&quot; </ul>
<p> See Sx GROUP PROVIDER PLUGINS for more information. </p>
<p> Note that quotes around group names are optional. Unquoted strings must use a backslash (`\&#8217; ) to escape spaces and special characters. See Sx Other special characters and reserved words for a list of characters that need to be escaped. </p>
<pre>Runas_List ::= Runas_Member |
 Runas_Member ',' Runas_List
Runas_Member ::= '!'* user name |
 '!'* #user-ID |
 '!'* %group |
 '!'* %#group-ID |
 '!'* %:nonunix_group |
 '!'* %:#nonunix_gid |
 '!'* +netgroup |
 '!'* Runas_Alias</pre>
<p>A <code>Runas_List</code> is similar to a <code>User_List</code> except that instead of <code>User_Alias es</code> it can contain <code>Runas_Alias es</code> Note that user names and groups are matched as strings. In other words, two users (groups) with the same user (group) ID are considered to be distinct. If you wish to match all user names with the same user-ID (e.g., root and toor), you can use a user-ID instead of a name (#0 in the example given). Note that the user-ID or group-ID specified in a <code>Runas_Member</code> need not be listed in the password or group database. </p>
<pre>Host_List ::= Host |
 Host ',' Host_List
Host ::= '!'* host name |
 '!'* ip_addr |
 '!'* network(/netmask)? |
 '!'* +netgroup |
 '!'* Host_Alias</pre>
<p>A <code>Host_List</code> is made up of one or more host names, IP addresses, network numbers, netgroups (prefixed with `+&#8217; ) , and other aliases. Again, the value of an item may be negated with the `!&#8217; operator. Host netgroups are matched using the host (both qualified and unqualified) and domain members only; the user member is not used when matching. If you specify a network number without a netmask, <code>sudo</code> will query each of the local host&#8217;s network interfaces and, if the network number corresponds to one of the hosts&#8217;s network interfaces, will use the netmask of that interface. The netmask may be specified either in standard IP address notation (e.g., 255.255.255.0 or ffff:ffff:ffff:ffff::), or CIDR notation (number of bits, e.g., 24 or 64). A host name may include shell-style wildcards (see the Sx Wildcards section below), but unless the <code>host name</code> command on your machine returns the fully qualified host name, you&#8217;ll need to use the <i>fqdn</i> flag for wildcards to be useful. Note that <code>sudo</code> only inspects actual network interfaces; this means that IP address 127.0.0.1 (localhost) will never match. Also, the host name &#8220;localhost&#8221; will only match if that is the actual host name, which is usually only the case for non-networked systems. </p>
<pre>digest ::= [A-Fa-f0-9]+ |
 [A-Za-z0-9\+/=]+
Digest_Spec ::= &quot;sha224&quot; ':' digest |
 &quot;sha256&quot; ':' digest |
 &quot;sha384&quot; ':' digest |
 &quot;sha512&quot; ':' digest
Digest_List ::= Digest_Spec |
 Digest_Spec ',' Digest_List
Cmnd_List ::= Cmnd |
 Cmnd ',' Cmnd_List
command name ::= file name |
 file name args |
 file name '&quot;&quot;'
Edit_Spec ::= &quot;sudoedit&quot; file name+
Cmnd ::= Digest_List? '!'* command name |
 '!'* directory |
 '!'* Edit_Spec |
 '!'* Cmnd_Alias</pre>
<p>A <code>Cmnd_List</code> is a list of one or more command names, directories, and other aliases. A command name is a fully qualified file name which may include shell-style wildcards (see the Sx Wildcards section below). A simple file name allows the user to run the command with any arguments they wish. However, you may also specify command line arguments (including wildcards). Alternately, you can specify to indicate that the command may only be run <code>without</code> command line arguments. A directory is a fully qualified path name ending in a `/&#8217; When you specify a directory in a <code>Cmnd_List</code> the user will be able to run any file within that directory (but not in any sub-directories therein). </p>
<p> If a <code>Cmnd</code> has associated command line arguments, then the arguments in the <code>Cmnd</code> must match exactly those given by the user on the command line (or match the wildcards if there are any). Note that the following characters must be escaped with a `\&#8217; if they are used in command arguments: `,&#8217; , `:&#8217; , `=&#8217; , `\&#8217; The built-in command &#8220;<code>sudoedit</code> &#8221; is used to permit a user to run <code>sudo</code> with the &#8211;<code>e</code> option (or as <code>sudoedit )</code> It may take command line arguments just as a normal command does. Note that &#8220;<code>sudoedit</code> &#8221; is a command built into <code>sudo</code> itself and must be specified in the <i>sudoers</i> file <code>without</code> a leading path. If a leading path is present, for example /usr/bin/sudoedit the path name will be silently converted to &#8220;<code>sudoedit</code> &#8221; A fully-qualified path for <code>sudoedit</code> is treated as an error by <code>visudo</code> </p>
<p> A <code>command name</code> may be preceded by a <code>Digest_List</code> a comma-separated list of one or more <code>Digest_Spec</code> entries. If a <code>Digest_List</code> is present, the command will only match successfully if it can be verified using one of the SHA-2 digests in the list. Starting with version 1.9.0, the <code>ALL</code> reserved word can be used in conjunction with a <code>Digest_List</code> The following digest formats are supported: sha224, sha256, sha384, and sha512. The string may be specified in either hex or base64 format (base64 is more compact). There are several utilities capable of generating SHA-2 digests in hex format such as openssl, shasum, sha224sum, sha256sum, sha384sum, sha512sum. </p>
<p> For example, using openssl: </p>
<pre>$ openssl dgst -sha224 /bin/ls
SHA224(/bin/ls)= 118187da8364d490b4a7debbf483004e8f3e053ec954309de2c41a25</pre>
<p>It is also possible to use openssl to generate base64 output: </p>
<pre>$ openssl dgst -binary -sha224 /bin/ls | openssl base64
EYGH2oNk1JC0p9679IMATo8+BT7JVDCd4sQaJQ==</pre>
<p>Warning, if the user has write access to the command itself (directly or via a <code>sudo</code> command), it may be possible for the user to replace the command after the digest check has been performed but before the command is executed. A similar race condition exists on systems that lack the Fn fexecve system call when the directory in which the command is located is writable by the user. See the description of the <i>fdexec</i> setting for more information on how <code>sudo</code> executes commands that have an associated digest. </p>
<p> Command digests are only supported by version 1.8.7 or higher.</p>
<h3>Defaults</h3>
<p>Certain configuration options may be changed from their default values at run-time via one or more <code>Default_Entry</code> lines. These may affect all users on any host, all users on a specific host, a specific user, a specific command, or commands being run as a specific user. Note that per-command entries may not include command line arguments. If you need to specify arguments, define a <code>Cmnd_Alias</code> and reference that instead. </p>
<pre>Default_Type ::= 'Defaults' |
 'Defaults' '@' Host_List |
 'Defaults' ':' User_List |
 'Defaults' '!' Cmnd_List |
 'Defaults' '&gt;' Runas_List
Default_Entry ::= Default_Type Parameter_List
Parameter_List ::= Parameter |
 Parameter ',' Parameter_List
Parameter ::= Parameter '=' Value |
 Parameter '+=' Value |
 Parameter '-=' Value |
 '!'* Parameter</pre>
<p>Parameters may be <code>flags</code> <code>integer</code> values, <code>strings</code> or <code>lists</code> Flags are implicitly boolean and can be turned off via the `!&#8217; operator. Some integer, string and list parameters may also be used in a boolean context to disable them. Values may be enclosed in double quotes () when they contain multiple words. Special characters may be escaped with a backslash (`\&#8217; ) </p>
<p> To include a literal backslash character in a command line argument you must escape the backslash twice. For example, to match `
&#8217; as part of a command line argument, you must use `\\n&#8217; in the <i>sudoers</i> file. This is due to there being two levels of escaping, one in the <i>sudoers</i> parser itself and another when command line arguments are matched by the <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) function. </p>
<p> Lists have two additional assignment operators, <code>+=</code> and <code>-=</code> These operators are used to add to and delete from a list respectively. It is not an error to use the <code>-=</code> operator to remove an element that does not exist in a list. </p>
<p> Defaults entries are parsed in the following order: generic, host, user, and runas Defaults first, then command defaults. If there are multiple Defaults settings of the same type, the last matching setting is used. The following Defaults settings are parsed before all others since they may affect subsequent entries: <i>fqdn</i> <i>group_plugin</i> <i>runas_default</i> <i>sudoers_locale</i> </p>
<p> See Sx SUDOERS OPTIONS for a list of supported Defaults parameters.</p>
<h3>User specification</h3>
<pre>User_Spec ::= User_List Host_List '=' Cmnd_Spec_List \
 (':' Host_List '=' Cmnd_Spec_List)*
Cmnd_Spec_List ::= Cmnd_Spec |
 Cmnd_Spec ',' Cmnd_Spec_List
Cmnd_Spec ::= Runas_Spec? Option_Spec* Tag_Spec* Cmnd
Runas_Spec ::= '(' Runas_List? (':' Runas_List)? ')'
Option_Spec ::= (SELinux_Spec | Date_Spec | Timeout_Spec | Chdir_Spec | Chroot_Spec)
Option_Spec ::= (Date_Spec | Timeout_Spec | Chdir_Spec | Chroot_Spec)
SELinux_Spec ::= ('ROLE=role' | 'TYPE=type')
Date_Spec ::= ('NOTBEFORE=timestamp' | 'NOTAFTER=timestamp')
Timeout_Spec ::= 'TIMEOUT=timeout'
Chdir_Spec ::= 'CWD=directory'
Chroot_Spec ::= 'CHROOT=directory'
Tag_Spec ::= ('EXEC:' | 'NOEXEC:' | 'FOLLOW:' | 'NOFOLLOW' |
 'LOG_INPUT:' | 'NOLOG_INPUT:' | 'LOG_OUTPUT:' |
 'NOLOG_OUTPUT:' | 'MAIL:' | 'NOMAIL:' | 'INTERCEPT:' |
 'NOINTERCEPT:' | 'PASSWD:' | 'NOPASSWD:' | 'SETENV:' |
 'NOSETENV:')</pre>
<p>A <code>user specification</code> determines which commands a user may run (and as what user) on specified hosts. By default, commands are run as <code>root</code> but this can be changed on a per-command basis. </p>
<p> The basic structure of a user specification is &#8220;who where = (as_whom) what&#8221; Let&#8217;s break that down into its constituent parts:</p>
<h3>Runas_Spec</h3>
<p>A <code>Runas_Spec</code> determines the user and/or the group that a command may be run as. A fully-specified <code>Runas_Spec</code> consists of two <code>Runas_List s</code> (as defined above) separated by a colon (`:&#8217; ) and enclosed in a set of parentheses. The first <code>Runas_List</code> indicates which users the command may be run as via the &#8211;<code>u</code> option. The second defines a list of groups that may be specified via the &#8211;<code>g</code> option (in addition to any of the target user&#8217;s groups). If both <code>Runas_List s</code> are specified, the command may be run with any combination of users and groups listed in their respective <code>Runas_List s.</code> If only the first is specified, the command may be run as any user in the list and, optionally, with any group the target user belongs to. If the first <code>Runas_List</code> is empty but the second is specified, the command may be run as the invoking user with the group set to any listed in the <code>Runas_List</code> If both <code>Runas_List s</code> are empty, the command may only be run as the invoking user and the group, if specified, must be one that the invoking user is a member of. If no <code>Runas_Spec</code> is specified, the command may only be run as <code>root</code> and the group, if specified, must be one that <code>root</code> is a member of. </p>
<p> A <code>Runas_Spec</code> sets the default for the commands that follow it. What this means is that for the entry: </p>
<pre>dgb boulder = (operator) /bin/ls, /bin/kill, /usr/bin/lprm</pre>
<p>The user <code>dgb</code> may run /bin/ls /bin/kill and /usr/bin/lprm on the host <code>boulder &#8212; but</code> only as <code>operator</code> E.g., </p>
<pre>$ sudo -u operator /bin/ls</pre>
<p>It is also possible to override a <code>Runas_Spec</code> later on in an entry. If we modify the entry like so: </p>
<pre>dgb boulder = (operator) /bin/ls, (root) /bin/kill, /usr/bin/lprm</pre>
<p>Then user <code>dgb</code> is now allowed to run /bin/ls as <code>operator</code> but /bin/kill and /usr/bin/lprm as <code>root</code> </p>
<p> We can extend this to allow <code>dgb</code> to run <code>/bin/ls</code> with either the user or group set to <code>operator</code> </p>
<pre>dgb boulder = (operator : operator) /bin/ls, (root) /bin/kill,\
 /usr/bin/lprm</pre>
<p>Note that while the group portion of the <code>Runas_Spec</code> permits the user to run as command with that group, it does not force the user to do so. If no group is specified on the command line, the command will run with the group listed in the target user&#8217;s password database entry. The following would all be permitted by the sudoers entry above: </p>
<pre>$ sudo -u operator /bin/ls
$ sudo -u operator -g operator /bin/ls
$ sudo -g operator /bin/ls</pre>
<p>In the following example, user <code>tcm</code> may run commands that access a modem device file with the dialer group. </p>
<pre>tcm boulder = (:dialer) /usr/bin/tip, /usr/bin/cu,\
 /usr/local/bin/minicom</pre>
<p>Note that in this example only the group will be set, the command still runs as user <code>tcm</code> E.g. </p>
<pre>$ sudo -g dialer /usr/bin/cu</pre>
<p>Multiple users and groups may be present in a <code>Runas_Spec</code> in which case the user may select any combination of users and groups via the &#8211;<code>u</code> and &#8211;<code>g</code> options. In this example: </p>
<pre>alan ALL = (root, bin : operator, system) ALL</pre>
<p>user <code>alan</code> may run any command as either user root or bin, optionally setting the group to operator or system.</p>
<h3>Option_Spec</h3>
<p>A <code>Cmnd</code> may have zero or more options associated with it. Options may consist of SELinux roles and/or types, start and/or end dates and command timeouts. Once an option is set for a <code>Cmnd</code> subsequent <code>Cmnd s</code> in the <code>Cmnd_Spec_List</code> inherit that option unless it is overridden by another option. Note that the option names are reserved words in <i>sudoers</i> This means that none of the valid option names (see below) can be used when declaring an alias.</p>
<h3>SELinux_Spec</h3>
<p>On systems with SELinux support, <i>sudoers</i> file entries may optionally have an SELinux role and/or type associated with a command. This can be used to implement a form of role-based access control (RBAC). If a role or type is specified with the command it will override any default values specified in <i>sudoers</i> A role or type specified on the command line, however, will supersede the values in <i>sudoers</i></p>
<h3>Date_Spec</h3>
<p><code>sudoers</code> rules can be specified with a start and end date via the <code>NOTBEFORE</code> and <code>NOTAFTER</code> settings. The time stamp must be specified in <i>Generalized Time</i> as defined by RFC 4517. The format is effectively <code>yyyymmddHHMMSSZ</code> where the minutes and seconds are optional. The `Z&#8217; suffix indicates that the time stamp is in Coordinated Universal Time (UTC). It is also possible to specify a timezone offset from UTC in hours and minutes instead of a `Z&#8217; For example, `-0500&#8242; would correspond to Eastern Standard time in the US. As an extension, if no `Z&#8217; or timezone offset is specified, local time will be used. </p>
<p> The following are all valid time stamps: </p>
<pre>20170214083000Z
2017021408Z
20160315220000-0500
20151201235900</pre>
<h3>Timeout_Spec</h3>
<p>A command may have a timeout associated with it. If the timeout expires before the command has exited, the command will be terminated. The timeout may be specified in combinations of days, hours, minutes, and seconds with a single-letter case-insensitive suffix that indicates the unit of time. For example, a timeout of 7 days, 8 hours, 30 minutes, and 10 seconds would be written as <code>7d8h30m10s</code> If a number is specified without a unit, seconds are assumed. Any of the days, minutes, hours, or seconds may be omitted. The order must be from largest to smallest unit and a unit may not be specified more than once. </p>
<p> The following are all <i>valid</i> timeout values: <code>7d8h30m10s</code> <code>14d</code> <code>8h30m</code> <code>600s</code> <code>3600</code> The following are <i>invalid</i> timeout values: <code>12m2w1d</code> <code>30s10m4h</code> <code>1d2d3h</code> </p>
<p> This setting is only supported by version 1.8.20 or higher.</p>
<h3>Chdir_Spec</h3>
<p>The working directory that the command will be run in can be specified using the <code>CWD</code> setting. The Fa directory must be a fully-qualified path name beginning with a `/&#8217; or `~&#8217; character, or the special value &#8220;*&#8221; A value of &#8220;*&#8221; indicates that the user may specify the working directory by running <code>sudo</code> with the &#8211;<code>D</code> option. By default, commands are run from the invoking user&#8217;s current working directory, unless the &#8211;<code>i</code> option is given. Path names of the form <code>~user/path/name</code> are interpreted as being relative to the named user&#8217;s home directory. If the user name is omitted, the path will be relative to the runas user&#8217;s home directory. </p>
<p> This setting is only supported by version 1.9.3 or higher.</p>
<h3>Chroot_Spec</h3>
<p>The root directory that the command will be run in can be specified using the <code>CHROOT</code> setting. The Fa directory must be a fully-qualified path name beginning with a `/&#8217; or `~&#8217; character, or the special value &#8220;*&#8221; A value of &#8220;*&#8221; indicates that the user may specify the root directory by running <code>sudo</code> with the &#8211;<code>R</code> option. This setting can be used to run the command in a <a href="/docs/linux/man/2-chroot/">chroot</a>(2) &#8220;sandbox&#8221; similar to the <a href="/docs/linux/man/8-chroot/">chroot</a>(8) utility. Path names of the form <code>~user/path/name</code> are interpreted as being relative to the named user&#8217;s home directory. If the user name is omitted, the path will be relative to the runas user&#8217;s home directory. </p>
<p> This setting is only supported by version 1.9.3 or higher.</p>
<h3>Tag_Spec</h3>
<p>A command may have zero or more tags associated with it. The following tag values are supported: <code>EXEC</code> <code>NOEXEC</code> <code>FOLLOW</code> <code>NOFOLLOW</code> <code>LOG_INPUT</code> <code>NOLOG_INPUT</code> <code>LOG_OUTPUT</code> <code>NOLOG_OUTPUT</code> <code>MAIL</code> <code>NOMAIL</code> <code>INTERCEPT</code> <code>NOINTERCEPT</code> <code>PASSWD</code> <code>NOPASSWD</code> <code>SETENV</code> and <code>NOSETENV</code> Once a tag is set on a <code>Cmnd</code> subsequent <code>Cmnd s</code> in the <code>Cmnd_Spec_List</code> inherit the tag unless it is overridden by the opposite tag (in other words, <code>PASSWD</code> overrides <code>NOPASSWD</code> and <code>NOEXEC</code> overrides <code>EXEC )</code></p>
<dl>
<dt><i>EXEC </i><code>and </code><i>NOEXEC</i></p>
<dd>If <code>sudo</code> has been compiled with <i>noexec</i> support and the underlying operating system supports it, the <code>NOEXEC</code> tag can be used to prevent a dynamically-linked executable from running further commands itself. </p>
<p> In the following example, user <code>aaron</code> may run /usr/bin/more and /usr/bin/vi but shell escapes will be disabled. </p>
<pre>aaron shanty = NOEXEC: /usr/bin/more, /usr/bin/vi</pre>
<p>See the Sx Preventing shell escapes section below for more details on how <code>NOEXEC</code> works and whether or not it will work on your system.</p>
<dt><i>FOLLOW </i><code>and </code><i>NOFOLLOW</i></p>
<dd>Starting with version 1.8.15, <code>sudoedit</code> will not open a file that is a symbolic link unless the <i>sudoedit_follow</i> flag is enabled. The <i>FOLLOW</i> and <i>NOFOLLOW</i> tags override the value of <i>sudoedit_follow</i> and can be used to permit (or deny) the editing of symbolic links on a per-command basis. These tags are only effective for the <i>sudoedit</i> command and are ignored for all other commands.</p>
<dt><i>LOG_INPUT </i><code>and </code><i>NOLOG_INPUT</i></p>
<dd>These tags override the value of the <i>log_input</i> flag on a per-command basis. For more information, see the description of <i>log_input</i> in the Sx SUDOERS OPTIONS section below.</p>
<dt><i>LOG_OUTPUT </i><code>and </code><i>NOLOG_OUTPUT</i></p>
<dd>These tags override the value of the <i>log_output</i> flag on a per-command basis. For more information, see the description of <i>log_output</i> in the Sx SUDOERS OPTIONS section below.</p>
<dt><i>MAIL </i><code>and </code><i>NOMAIL</i></p>
<dd>These tags provide fine-grained control over whether mail will be sent when a user runs a command by overriding the value of the <i>mail_all_cmnds</i> flag on a per-command basis. They have no effect when <code>sudo</code> is run with the &#8211;<code>l</code> or &#8211;<code>v</code> options. A <i>NOMAIL</i> tag will also override the <i>mail_always</i> and <i>mail_no_perms</i> options. For more information, see the descriptions of <i>mail_all_cmnds</i> <i>mail_always</i> and <i>mail_no_perms</i> in the Sx SUDOERS OPTIONS section below.</p>
<dt><i>PASSWD </i><code>and </code><i>NOPASSWD</i></p>
<dd>By default, <code>sudo</code> requires that a user authenticate before running a command. This behavior can be modified via the <code>NOPASSWD</code> tag. Like a <code>Runas_Spec</code> the <code>NOPASSWD</code> tag sets a default for the commands that follow it in the <code>Cmnd_Spec_List</code> Conversely, the <code>PASSWD</code> tag can be used to reverse things. For example: </p>
<pre>ray rushmore = NOPASSWD: /bin/kill, /bin/ls, /usr/bin/lprm</pre>
<p>would allow the user <code>ray</code> to run /bin/kill /bin/ls and /usr/bin/lprm as <code>root</code> on the machine &#8220;rushmore&#8221; without authenticating himself. If we only want <code>ray</code> to be able to run /bin/kill without a password the entry would be: </p>
<pre>ray rushmore = NOPASSWD: /bin/kill, PASSWD: /bin/ls, /usr/bin/lprm</pre>
<p>Note, however, that the <code>PASSWD</code> tag has no effect on users who are in the group specified by the <i>exempt_group</i> setting. </p>
<p> By default, if the <code>NOPASSWD</code> tag is applied to any of a user&#8217;s entries for the current host, the user will be able to run &#8220;<code>sudo -l</code> &#8221; without a password. Additionally, a user may only run &#8220;<code>sudo -v</code> &#8221; without a password if all of the user&#8217;s entries for the current host have the <code>NOPASSWD</code> tag. This behavior may be overridden via the <i>verifypw</i> and <i>listpw</i> options.</p>
<dt><i>SETENV </i><code>and </code><i>NOSETENV</i></p>
<dd>These tags override the value of the <i>setenv</i> flag on a per-command basis. Note that if <code>SETENV</code> has been set for a command, the user may disable the <i>env_reset</i> flag from the command line via the &#8211;<code>E</code> option. Additionally, environment variables set on the command line are not subject to the restrictions imposed by <i>env_check</i> <i>env_delete</i> or <i>env_keep</i> As such, only trusted users should be allowed to set variables in this manner. If the command matched is <code>ALL</code> the <code>SETENV</code> tag is implied for that command; this default may be overridden by use of the <code>NOSETENV</code> tag.</p>
<dt><i>INTERCEPT </i><code>and </code><i>NOINTERCEPT</i></p>
<dd>If <code>sudo</code> has been compiled with <i>intercept</i> support and the underlying operating system supports it, the <code>INTERCEPT</code> tag can be used to cause programs spawned by a command to be validated against <i>sudoers</i> and logged just like they would be if run through <code>sudo</code> directly. This is useful in conjunction with commands that allow shell escapes such as editors, shells, and paginators. </p>
<p> In the following example, user <code>chuck</code> may run any command on the machine &#8220;research&#8221; in intercept mode. </p>
<pre>chuck research = INTERCEPT: ALL</pre>
<p>See the Sx Preventing shell escapes section below for more details on how <code>INTERCEPT</code> works and whether or not it will work on your system.</dl>
<h3>Wildcards</h3>
<p><code>sudo</code> allows shell-style <i>wildcards</i> (aka meta or glob characters) to be used in host names, path names, and command line arguments in the <i>sudoers</i> file. Wildcard matching is done via the <a href="/docs/linux/man/3-glob/">glob</a>(3) and <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) functions as specified by St -p1003.1 .</p>
<dl>
<dt><code>*</code></p>
<dd>Matches any set of zero or more characters (including white space).</p>
<dt><code>?</code></p>
<dd>Matches any single character (including white space).</p>
<dt><code>[&#8230;]</code></p>
<dd>Matches any character in the specified range.</p>
<dt><code>[!&#8230;]</code></p>
<dd>Matches any character <i>not</i> in the specified range.</p>
<dt><code>
