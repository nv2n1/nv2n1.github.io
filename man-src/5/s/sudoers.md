---
title: "sudoers(5)"
name: "sudoers"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sudoers/"
description: "sudoers – default sudo security policy plugin"
---
<p> Sudo 1.9.9  </p>
<h2 class="name">NAME</h2>
<p> <code>sudoers</code> - default sudo security policy plugin </p>
<h2>DESCRIPTION</h2>
<p> The <code>sudoers</code> policy plugin determines a user&#8217;s <code>sudo</code> privileges. It is the default <code>sudo</code> policy plugin. The policy is driven by the /etc/sudoers file or, optionally, in LDAP. The policy format is described in detail in the Sx SUDOERS FILE FORMAT section. For information on storing <code>sudoers</code> policy information in LDAP, please see sudoers.ldap5.  </p>
<h3>Configuring sudo.conf for sudoers</h3>
<p> <code>sudo</code> consults the sudo.conf5 file to determine which plugins to load. If no sudo.conf5 file is present, or if it contains no <code>Plugin</code> lines, <code>sudoers</code> will be used for auditing, policy decisions and I/O logging. To explicitly configure sudo.conf5 to use the <code>sudoers</code> plugin, the following configuration can be used. </p>
<blockquote><pre><code>Plugin sudoers_audit sudoers.so
Plugin sudoers_policy sudoers.so
Plugin sudoers_io sudoers.so
</code></pre>
</blockquote>
<p>Starting with <code>sudo</code> 1.8.5, it is possible to specify optional arguments to the <code>sudoers</code> plugin in the sudo.conf5 file. Plugin arguments, if any, should be listed after the path to the plugin (i.e., after sudoers.so ) The arguments are only effective for the plugin that opens (and parses) the <i>sudoers</i> file. </p>
<p>For <code>sudo</code> version 1.9.1 and higher, this is the <i>sudoers_audit</i> plugin. For older versions, it is the <i>sudoers_policy</i> plugin. Multiple arguments may be specified, separated by white space. For example: </p>
<blockquote><pre><code>Plugin sudoers_audit sudoers.so sudoers_mode=0400 error_recovery=false
</code></pre>
</blockquote>
<p>The following plugin arguments are supported: </p>
<dl>
<dt><code>error_recovery=bool</code></dt>
<dd> <p> The <i>error_recovery</i> argument can be used to control whether <code>sudoers</code> should attempt to recover from syntax errors in the <i>sudoers</i> file. If set to <i>true</i> (the default), <code>sudoers</code> will try to recover from a syntax error by discarding the portion of the line that contains the error until the end of the line. A value of <i>false</i> will disable error recovery. Prior to version 1.9.3, no error recovery was performed. </p>
 </dd>
<dt><code>ldap_conf=pathname</code></dt>
<dd> <p> The <i>ldap_conf</i> argument can be used to override the default path to the ldap.conf file. </p>
 </dd>
<dt><code>ldap_secret=pathname</code></dt>
<dd> <p> The <i>ldap_secret</i> argument can be used to override the default path to the ldap.secret file. </p>
 </dd>
<dt><code>sudoers_file=pathname</code></dt>
<dd> <p> The <i>sudoers_file</i> argument can be used to override the default path to the <i>sudoers</i> file. </p>
 </dd>
<dt><code>sudoers_uid=user-ID</code></dt>
<dd> <p> The <i>sudoers_uid</i> argument can be used to override the default owner of the sudoers file. It should be specified as a numeric user-ID. </p>
 </dd>
<dt><code>sudoers_gid=group-ID</code></dt>
<dd> <p> The <i>sudoers_gid</i> argument can be used to override the default group of the sudoers file. It must be specified as a numeric group-ID (not a group name). </p>
 </dd>
<dt><code>sudoers_mode=mode</code></dt>
<dd> <p> The <i>sudoers_mode</i> argument can be used to override the default file mode for the sudoers file. It should be specified as an octal value. </p>
 </dd></dl>
<p>For more information on configuring sudo.conf5, please refer to its manual.  </p>
<h3>User Authentication</h3>
<p> The <code>sudoers</code> security policy requires that most users authenticate themselves before they can use <code>sudo</code> A password is not required if the invoking user is root, if the target user is the same as the invoking user, or if the policy has disabled authentication for the user or command. Unlike <a href="/docs/linux/man/1-su/">su</a>(1), when <code>sudoers</code> requires authentication, it validates the invoking user&#8217;s credentials, not the target user&#8217;s (or root&#8217;s) credentials. This can be changed via the <i>rootpw</i> <i>targetpw</i> and <i>runaspw</i> flags, described later. </p>
<p>If a user who is not listed in the policy tries to run a command via <code>sudo</code> mail is sent to the proper authorities. The address used for such mail is configurable via the <i>mailto</i> Defaults entry (described later) and defaults to <code>root</code> </p>
<p>Note that no mail will be sent if an unauthorized user tries to run <code>sudo</code> with the -<code>l</code> or -<code>v</code> option unless there is an authentication error and either the <i>mail_always</i> or <i>mail_badpass</i> flags are enabled. This allows users to determine for themselves whether or not they are allowed to use <code>sudo</code> By default, all attempts to run <code>sudo</code> (successful or not) are logged, regardless of whether or not mail is sent. </p>
<p>If <code>sudo</code> is run by root and the <code>SUDO_USER</code> environment variable is set, the <code>sudoers</code> policy will use this value to determine who the actual user is. This can be used by a user to log commands through sudo even when a root shell has been invoked. It also allows the -<code>e</code> option to remain useful even when invoked via a sudo-run script or program. Note, however, that the <i>sudoers</i> file lookup is still done for root, not the user specified by <code>SUDO_USER</code> </p>
<p> <code>sudoers</code> uses per-user time stamp files for credential caching. Once a user has been authenticated, a record is written containing the user-ID that was used to authenticate, the terminal session ID, the start time of the session leader (or parent process) and a time stamp (using a monotonic clock if one is available). The user may then use <code>sudo</code> without a password for a short period of time Po <code>15</code> minutes unless overridden by the <i>timestamp_timeout</i> option Pc . By default, <code>sudoers</code> uses a separate record for each terminal, which means that a user&#8217;s login sessions are authenticated separately. The <i>timestamp_type</i> option can be used to select the type of time stamp record <code>sudoers</code> will use.  </p>
<h3>Logging</h3>
<p> By default, <code>sudoers</code> logs both successful and unsuccessful attempts (as well as errors). The <i>log_allowed</i> and <i>log_denied</i> flags can be used to control this behavior. Messages can be logged to <a href="/docs/linux/man/3-syslog/">syslog</a>(3), a log file, or both. The default is to log to <a href="/docs/linux/man/3-syslog/">syslog</a>(3) but this is configurable via the <i>syslog</i> and <i>logfile</i> settings. See Sx LOG FORMAT for a description of the log file format. </p>
<p> <code>sudoers</code> is also capable of running a command in a pseudo-terminal and logging all input and/or output. The standard input, standard output, and standard error can be logged even when not associated with a terminal. I/O logging is not on by default but can be enabled using the <i>log_input</i> and <i>log_output</i> options as well as the <code>LOG_INPUT</code> and <code>LOG_OUTPUT</code> command tags. See Sx I/O LOG FILES for details on how I/O log files are stored. </p>
<p>Starting with version 1.9, the <i>log_servers</i> setting may be used to send event and I/O log data to a remote server running <code>sudo_logsrvd</code> or another service that implements the protocol described by sudo_logsrv.proto5.  </p>
<h3>Command environment</h3>
<p> Since environment variables can influence program behavior, <code>sudoers</code> provides a means to restrict which variables from the user&#8217;s environment are inherited by the command to be run. There are two distinct ways <code>sudoers</code> can deal with environment variables. </p>
<p>By default, the <i>env_reset</i> flag is enabled. This causes commands to be executed with a new, minimal environment. On AIX (and Linux systems without PAM), the environment is initialized with the contents of the /etc/environment file. The <code>HOME</code> <code>MAIL</code> <code>SHELL</code> <code>LOGNAME</code> and <code>USER</code> environment variables are initialized based on the target user and the <code>SUDO_*</code> variables are set based on the invoking user. Additional variables, such as <code>DISPLAY</code> <code>PATH</code> and <code>TERM</code> are preserved from the invoking user&#8217;s environment if permitted by the <i>env_check</i> or <i>env_keep</i> options. A few environment variables are treated specially. If the <code>PATH</code> and <code>TERM</code> variables are not preserved from the user&#8217;s environment, they will be set to default values. The <code>LOGNAME</code> and <code>USER</code> are handled as a single entity. If one of them is preserved (or removed) from the user&#8217;s environment, the other will be as well. If <code>LOGNAME</code> and <code>USER</code> are to be preserved but only one of them is present in the user&#8217;s environment, the other will be set to the same value. This avoids an inconsistent environment where one of the variables describing the user name is set to the invoking user and one is set to the target user. Environment variables with a value beginning with <code>()</code> are removed unless both the name and value parts are matched by <i>env_keep</i> or <i>env_check</i> as they may be interpreted as functions by the <code>bash</code> shell. Prior to version 1.8.11, such variables were always removed. </p>
<p>If, however, the <i>env_reset</i> flag is disabled, any variables not explicitly denied by the <i>env_check</i> and <i>env_delete</i> options are allowed and their values are inherited from the invoking process. Prior to version 1.8.21, environment variables with a value beginning with <code>()</code> were always removed. Beginning with version 1.8.21, a pattern in <i>env_delete</i> is used to match <code>bash</code> shell functions instead. Since it is not possible to block all potentially dangerous environment variables, use of the default <i>env_reset</i> behavior is encouraged. </p>
<p>Environment variables specified by <i>env_check</i> <i>env_delete</i> or <i>env_keep</i> may include one or more `*&#8216; characters which will match zero or more characters. No other wildcard characters are supported. </p>
<p>By default, environment variables are matched by name. However, if the pattern includes an equal sign (`=&#8216; ) both the variables name and value must match. For example, a <code>bash</code> shell function could be matched as follows: </p>
<pre><code>env_keep += &quot;BASH_FUNC_my_func%%=()*&quot;
</code></pre>
<p>Without the ``<code>=()*</code> &#8216;&#8216; suffix, this would not match, as <code>bash</code> shell functions are not preserved by default. </p>
<p>The complete list of environment variables that are preserved or removed, as modified by global Defaults parameters in <i>sudoers</i> is displayed when <code>sudo</code> is run by root with the -<code>V</code> option. Please note that the list of environment variables to remove varies based on the operating system <code>sudo</code> is running on. </p>
<p>Other <code>sudoers</code> options may influence the command environment, such as <i>always_set_home</i> <i>secure_path</i> <i>set_logname</i> and <i>set_home</i> </p>
<p>On systems that support PAM where the <code>pam_env</code> module is enabled for <code>sudo</code> variables in the PAM environment may be merged in to the environment. If a variable in the PAM environment is already present in the user&#8217;s environment, the value will only be overridden if the variable was not preserved by <code>sudoers.</code> When <i>env_reset</i> is enabled, variables preserved from the invoking user&#8217;s environment by the <i>env_keep</i> list take precedence over those in the PAM environment. When <i>env_reset</i> is disabled, variables present the invoking user&#8217;s environment take precedence over those in the PAM environment unless they match a pattern in the <i>env_delete</i> list. </p>
<p>Note that the dynamic linker on most operating systems will remove variables that can control dynamic linking from the environment of set-user-ID executables, including <code>sudo</code> Depending on the operating system this may include <code>_RLD*</code> <code>DYLD_*</code> <code>LD_*</code> <code>LDR_*</code> <code>LIBPATH</code> <code>SHLIB_PATH</code> and others. These type of variables are removed from the environment before <code>sudo</code> even begins execution and, as such, it is not possible for <code>sudo</code> to preserve them. </p>
<p>As a special case, if the -<code>i</code> option (initial login) is specified, <code>sudoers</code> will initialize the environment regardless of the value of <i>env_reset</i> The <code>DISPLAY</code> <code>PATH</code> and <code>TERM</code> variables remain unchanged; <code>HOME</code> <code>MAIL</code> <code>SHELL</code> <code>USER</code> and <code>LOGNAME</code> are set based on the target user. On AIX (and Linux systems without PAM), the contents of /etc/environment are also included. All other environment variables are removed unless permitted by <i>env_keep</i> or <i>env_check</i> described above. </p>
<p>Finally, the <i>restricted_env_file</i> and <i>env_file</i> files are applied, if present. The variables in <i>restricted_env_file</i> are applied first and are subject to the same restrictions as the invoking user&#8217;s environment, as detailed above. The variables in <i>env_file</i> are applied last and are not subject to these restrictions. In both cases, variables present in the files will only be set to their specified values if they would not conflict with an existing environment variable.  </p>
<h2>SUDOERS FILE FORMAT</h2>
<p> The <i>sudoers</i> file is composed of two types of entries: aliases (basically variables) and user specifications (which specify who may run what). </p>
<p>When multiple entries match for a user, they are applied in order. Where there are multiple matches, the last match is used (which is not necessarily the most specific match). </p>
<p>The <i>sudoers</i> file grammar will be described below in Extended Backus-Naur Form (EBNF). Don&#8217;t despair if you are unfamiliar with EBNF; it is fairly simple, and the definitions below are annotated.  </p>
<h3>Resource limits</h3>
<p> By default, <code>sudoers</code> uses the operating system&#8217;s native method of setting resource limits for the target user. On Linux systems, resource limits are usually set by the <code>pam_limits.so</code> PAM module. On some BSD systems, the /etc/login.conf file specifies resource limits for the user. On AIX systems, resource limits are configured in the /etc/security/limits file. If there is no system mechanism to set per-user resource limits, the command will run with the same limits as the invoking user. The one exception to this is the core dump file size, which is set by <code>sudoers</code> to 0 by default. Disabling core dumps by default makes it possible to avoid potential security problems where the core file is treated as trusted input. </p>
<p>Resource limits may also be set in the <i>sudoers</i> file itself, in which case they override those set by the system. See the <i>rlimit_as,</i> <i>rlimit_core,</i> <i>rlimit_cpu,</i> <i>rlimit_data,</i> <i>rlimit_fsize,</i> <i>rlimit_locks,</i> <i>rlimit_memlock,</i> <i>rlimit_nofile,</i> <i>rlimit_nproc,</i> <i>rlimit_rss,</i> <i>rlimit_stack</i> options described below. Resource limits in <code>sudoers</code> may be specified in one of the following formats: </p>
<dl>
<dt><code>``value&#8217;&#8216; </code></dt>
<dd> <p> Both the soft and hard resource limits are set to the same value. The special value ``infinity&#8217;&#8216; can be used to indicate that the value is unlimited. </p>
 </dd>
<dt><code>``soft,hard&#8217;&#8216; </code></dt>
<dd> <p> Two comma-separated values. The soft limit is set to the first value and the hard limit is set to the second. Both values must either be enclosed in a set of double quotes, or the comma must be escaped with a backslash (`\&#8216; ) The special value ``infinity&#8217;&#8216; may be used in place of either value. </p>
 </dd>
<dt><code>``default&#8217;&#8216; </code></dt>
<dd> <p> The default resource limit for the user will be used. This may be a user-specific value (see above) or the value of the resource limit when <code>sudo</code> was invoked for systems that don&#8217;t support per-user limits. </p>
 </dd>
<dt><code>``user&#8217;&#8216; </code></dt>
<dd> <p> The invoking user&#8217;s resource limits will be preserved when running the command. </p>
 </dd></dl>
<p>For example, to restore the historic core dump file size behavior, a line like the following may be used. </p>
<blockquote><p> <code>Defaults rlimit_core=default</code> </p>
</blockquote>
<p>Resource limits in <code>sudoers</code> are only supported by version 1.8.7 or higher.  </p>
<h3>Quick guide to EBNF</h3>
<p> EBNF is a concise and exact way of describing the grammar of a language. Each EBNF definition is made up of <i>production rules</i> E.g., </p>
<p> <code>symbol ::= definition | alternate1 | alternate2 ...</code> </p>
<p>Each <i>production rule</i> references others and thus makes up a grammar for the language. EBNF also contains the following operators, which many readers will recognize from regular expressions. Do not, however, confuse them with ``wildcard&#8217;&#8216; characters, which have different meanings. </p>
<dl>
<dt><code>?</code></dt>
<dd> <p> Means that the preceding symbol (or group of symbols) is optional. That is, it may appear once or not at all. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> Means that the preceding symbol (or group of symbols) may appear zero or more times. </p>
 </dd>
<dt><code>+</code></dt>
<dd> <p> Means that the preceding symbol (or group of symbols) may appear one or more times. </p>
 </dd></dl>
<p>Parentheses may be used to group symbols together. For clarity, we will use single quotes (&#8216;&#8216;) to designate what is a verbatim character string (as opposed to a symbol name).  </p>
<h3>Aliases</h3>
<p> There are four kinds of aliases: <code>User_Alias</code> <code>Runas_Alias</code> <code>Host_Alias</code> and <code>Cmnd_Alias</code> Beginning with <code>sudo</code> 1.9.0, <code>Cmd_Alias</code> may be used in place of <code>Cmnd_Alias</code> if desired. </p>
<pre><code>Alias ::= 'User_Alias' User_Alias_Spec (':' User_Alias_Spec)* |
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
NAME ::= [A-Z]([A-Z][0-9]_)*
</code></pre>
<p>Each <i>alias</i> definition is of the form </p>
<pre><code>Alias_Type NAME = item1, item2, ...
</code></pre>
<p>where <i>Alias_Type</i> is one of <code>User_Alias</code> <code>Runas_Alias</code> <code>Host_Alias</code> or <code>Cmnd_Alias</code> A <code>NAME</code> is a string of uppercase letters, numbers, and underscore characters (`_&#8216; ) A <code>NAME</code> <code>must</code> start with an uppercase letter. It is possible to put several alias definitions of the same type on a single line, joined by a colon (`:&#8216; ) E.g., </p>
<pre><code>Alias_Type NAME = item1, item2, item3 : NAME = item4, item5
</code></pre>
<p>It is a syntax error to redefine an existing <i>alias</i> It is possible to use the same name for <i>aliases</i> of different types, but this is not recommended. </p>
<p>The definitions of what constitutes a valid <i>alias</i> member follow. </p>
<pre><code>User_List ::= User |
              User ',' User_List
User ::= '!'* user name |
         '!'* #user-ID |
         '!'* %group |
         '!'* %#group-ID |
         '!'* +netgroup |
         '!'* %:nonunix_group |
         '!'* %:#nonunix_gid |
         '!'* User_Alias
</code></pre>
<p>A <code>User_List</code> is made up of one or more user names, user-IDs (prefixed with `#&#8216; ) , system group names and IDs (prefixed with `%&#8216; and `%#&#8216; respectively), netgroups (prefixed with `+&#8216; ) , non-Unix group names and IDs (prefixed with `%:&#8216; and `%:#&#8216; respectively), and <code>User_Alias es.</code> Each list item may be prefixed with zero or more `!&#8216; operators. An odd number of `!&#8216; operators negate the value of the item; an even number just cancel each other out. User netgroups are matched using the user and domain members only; the host member is not used when matching. </p>
<p>A <code>user name</code> <code>user-ID</code> <code>group</code> <code>group-ID</code> <code>netgroup</code> <code>nonunix_group</code> or <code>nonunix_gid</code> may be enclosed in double quotes to avoid the need for escaping special characters. Alternately, special characters may be specified in escaped hex mode, e.g., \x20 for space. When using double quotes, any prefix characters must be included inside the quotes. </p>
<p>The actual <code>nonunix_group</code> and <code>nonunix_gid</code> syntax depends on the underlying group provider plugin. For instance, the QAS AD plugin supports the following formats: </p>
<ul>
<li> <p>Group in the same domain: &quot;%:Group Name&quot;  </li>
<li>  Group in any domain: &quot;%:Group Name [at] FULLY.QUALIFIED.DOMAIN&quot;  </li>
<li>  Group SID: &quot;%:S-1-2-34-5678901234-5678901234-5678901234-567&quot;  </li>
</ul>
 </p>
<p>See Sx GROUP PROVIDER PLUGINS for more information. </p>
<p>Note that quotes around group names are optional. Unquoted strings must use a backslash (`\&#8216; ) to escape spaces and special characters. See Sx Other special characters and reserved words for a list of characters that need to be escaped. </p>
<pre><code>Runas_List ::= Runas_Member |
               Runas_Member ',' Runas_List
Runas_Member ::= '!'* user name |
                 '!'* #user-ID |
                 '!'* %group |
                 '!'* %#group-ID |
                 '!'* %:nonunix_group |
                 '!'* %:#nonunix_gid |
                 '!'* +netgroup |
                 '!'* Runas_Alias
</code></pre>
<p>A <code>Runas_List</code> is similar to a <code>User_List</code> except that instead of <code>User_Alias es</code> it can contain <code>Runas_Alias es</code> Note that user names and groups are matched as strings. In other words, two users (groups) with the same user (group) ID are considered to be distinct. If you wish to match all user names with the same user-ID (e.g., root and toor), you can use a user-ID instead of a name (#0 in the example given). Note that the user-ID or group-ID specified in a <code>Runas_Member</code> need not be listed in the password or group database. </p>
<pre><code>Host_List ::= Host |
              Host ',' Host_List
Host ::= '!'* host name |
         '!'* ip_addr |
         '!'* network(/netmask)? |
         '!'* +netgroup |
         '!'* Host_Alias
</code></pre>
<p>A <code>Host_List</code> is made up of one or more host names, IP addresses, network numbers, netgroups (prefixed with `+&#8216; ) , and other aliases. Again, the value of an item may be negated with the `!&#8216; operator. Host netgroups are matched using the host (both qualified and unqualified) and domain members only; the user member is not used when matching. If you specify a network number without a netmask, <code>sudo</code> will query each of the local host&#8217;s network interfaces and, if the network number corresponds to one of the hosts&#8217;s network interfaces, will use the netmask of that interface. The netmask may be specified either in standard IP address notation (e.g., 255.255.255.0 or ffff:ffff:ffff:ffff::), or CIDR notation (number of bits, e.g., 24 or 64). A host name may include shell-style wildcards (see the Sx Wildcards section below), but unless the <code>host name</code> command on your machine returns the fully qualified host name, you&#8217;ll need to use the <i>fqdn</i> flag for wildcards to be useful. Note that <code>sudo</code> only inspects actual network interfaces; this means that IP address 127.0.0.1 (localhost) will never match. Also, the host name ``localhost&#8217;&#8216; will only match if that is the actual host name, which is usually only the case for non-networked systems. </p>
<pre><code>digest ::= [A-Fa-f0-9]+ |
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
         '!'* Cmnd_Alias
</code></pre>
<p>A <code>Cmnd_List</code> is a list of one or more command names, directories, and other aliases. A command name is a fully qualified file name which may include shell-style wildcards (see the Sx Wildcards section below). A simple file name allows the user to run the command with any arguments they wish. However, you may also specify command line arguments (including wildcards). Alternately, you can specify to indicate that the command may only be run <code>without</code> command line arguments. A directory is a fully qualified path name ending in a `/&#8216; When you specify a directory in a <code>Cmnd_List</code> the user will be able to run any file within that directory (but not in any sub-directories therein). </p>
<p>If a <code>Cmnd</code> has associated command line arguments, then the arguments in the <code>Cmnd</code> must match exactly those given by the user on the command line (or match the wildcards if there are any). Note that the following characters must be escaped with a `\&#8216; if they are used in command arguments: `,&#8216; , `:&#8216; , `=&#8216; , `\&#8216; The built-in command ``<code>sudoedit</code> &#8216;&#8216; is used to permit a user to run <code>sudo</code> with the -<code>e</code> option (or as <code>sudoedit )</code> It may take command line arguments just as a normal command does. Note that ``<code>sudoedit</code> &#8216;&#8216; is a command built into <code>sudo</code> itself and must be specified in the <i>sudoers</i> file <code>without</code> a leading path. If a leading path is present, for example /usr/bin/sudoedit the path name will be silently converted to ``<code>sudoedit</code> &#8216;&#8216; A fully-qualified path for <code>sudoedit</code> is treated as an error by <code>visudo</code> </p>
<p>A <code>command name</code> may be preceded by a <code>Digest_List</code> a comma-separated list of one or more <code>Digest_Spec</code> entries. If a <code>Digest_List</code> is present, the command will only match successfully if it can be verified using one of the SHA-2 digests in the list. Starting with version 1.9.0, the <code>ALL</code> reserved word can be used in conjunction with a <code>Digest_List</code> The following digest formats are supported: sha224, sha256, sha384, and sha512. The string may be specified in either hex or base64 format (base64 is more compact). There are several utilities capable of generating SHA-2 digests in hex format such as openssl, shasum, sha224sum, sha256sum, sha384sum, sha512sum. </p>
<p>For example, using openssl: </p>
<pre><code>$ openssl dgst -sha224 /bin/ls
SHA224(/bin/ls)= 118187da8364d490b4a7debbf483004e8f3e053ec954309de2c41a25
</code></pre>
<p>It is also possible to use openssl to generate base64 output: </p>
<pre><code>$ openssl dgst -binary -sha224 /bin/ls | openssl base64
EYGH2oNk1JC0p9679IMATo8+BT7JVDCd4sQaJQ==
</code></pre>
<p>Warning, if the user has write access to the command itself (directly or via a <code>sudo</code> command), it may be possible for the user to replace the command after the digest check has been performed but before the command is executed. A similar race condition exists on systems that lack the Fn fexecve system call when the directory in which the command is located is writable by the user. See the description of the <i>fdexec</i> setting for more information on how <code>sudo</code> executes commands that have an associated digest. </p>
<p>Command digests are only supported by version 1.8.7 or higher.  </p>
<h3>Defaults</h3>
<p> Certain configuration options may be changed from their default values at run-time via one or more <code>Default_Entry</code> lines. These may affect all users on any host, all users on a specific host, a specific user, a specific command, or commands being run as a specific user. Note that per-command entries may not include command line arguments. If you need to specify arguments, define a <code>Cmnd_Alias</code> and reference that instead. </p>
<pre><code>Default_Type ::= 'Defaults' |
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
              '!'* Parameter
</code></pre>
<p>Parameters may be <code>flags</code> <code>integer</code> values, <code>strings</code> or <code>lists</code> Flags are implicitly boolean and can be turned off via the `!&#8216; operator. Some integer, string and list parameters may also be used in a boolean context to disable them. Values may be enclosed in double quotes () when they contain multiple words. Special characters may be escaped with a backslash (`\&#8216; ) </p>
<p>To include a literal backslash character in a command line argument you must escape the backslash twice. For example, to match `\n&#8217; as part of a command line argument, you must use `\\\\n&#8217; in the <i>sudoers</i> file. This is due to there being two levels of escaping, one in the <i>sudoers</i> parser itself and another when command line arguments are matched by the <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) function. </p>
<p>Lists have two additional assignment operators, <code>+=</code> and <code>-=</code> These operators are used to add to and delete from a list respectively. It is not an error to use the <code>-=</code> operator to remove an element that does not exist in a list. </p>
<p>Defaults entries are parsed in the following order: generic, host, user, and runas Defaults first, then command defaults. If there are multiple Defaults settings of the same type, the last matching setting is used. The following Defaults settings are parsed before all others since they may affect subsequent entries: <i>fqdn</i> <i>group_plugin</i> <i>runas_default</i> <i>sudoers_locale</i> </p>
<p>See Sx SUDOERS OPTIONS for a list of supported Defaults parameters.  </p>
<h3>User specification</h3>
<pre><code>User_Spec ::= User_List Host_List '=' Cmnd_Spec_List \
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
              'NOSETENV:')
</code></pre>
<p>A <code>user specification</code> determines which commands a user may run (and as what user) on specified hosts. By default, commands are run as <code>root</code> but this can be changed on a per-command basis. </p>
<p>The basic structure of a user specification is ``who where = (as_whom) what&#8217;&#8216; Let&#8217;s break that down into its constituent parts:  </p>
<h3>Runas_Spec</h3>
<p> A <code>Runas_Spec</code> determines the user and/or the group that a command may be run as. A fully-specified <code>Runas_Spec</code> consists of two <code>Runas_List s</code> (as defined above) separated by a colon (`:&#8216; ) and enclosed in a set of parentheses. The first <code>Runas_List</code> indicates which users the command may be run as via the -<code>u</code> option. The second defines a list of groups that may be specified via the -<code>g</code> option (in addition to any of the target user&#8217;s groups). If both <code>Runas_List s</code> are specified, the command may be run with any combination of users and groups listed in their respective <code>Runas_List s.</code> If only the first is specified, the command may be run as any user in the list and, optionally, with any group the target user belongs to. If the first <code>Runas_List</code> is empty but the second is specified, the command may be run as the invoking user with the group set to any listed in the <code>Runas_List</code> If both <code>Runas_List s</code> are empty, the command may only be run as the invoking user and the group, if specified, must be one that the invoking user is a member of. If no <code>Runas_Spec</code> is specified, the command may only be run as <code>root</code> and the group, if specified, must be one that <code>root</code> is a member of. </p>
<p>A <code>Runas_Spec</code> sets the default for the commands that follow it. What this means is that for the entry: </p>
<pre><code>dgb boulder = (operator) /bin/ls, /bin/kill, /usr/bin/lprm
</code></pre>
<p>The user <code>dgb</code> may run /bin/ls /bin/kill and /usr/bin/lprm on the host <code>boulder --- but</code> only as <code>operator</code> E.g., </p>
<pre><code>$ sudo -u operator /bin/ls
</code></pre>
<p>It is also possible to override a <code>Runas_Spec</code> later on in an entry. If we modify the entry like so: </p>
<pre><code>dgb boulder = (operator) /bin/ls, (root) /bin/kill, /usr/bin/lprm
</code></pre>
<p>Then user <code>dgb</code> is now allowed to run /bin/ls as <code>operator</code> but /bin/kill and /usr/bin/lprm as <code>root</code> </p>
<p>We can extend this to allow <code>dgb</code> to run <code>/bin/ls</code> with either the user or group set to <code>operator</code> </p>
<pre><code>dgb boulder = (operator : operator) /bin/ls, (root) /bin/kill,\
        /usr/bin/lprm
</code></pre>
<p>Note that while the group portion of the <code>Runas_Spec</code> permits the user to run as command with that group, it does not force the user to do so. If no group is specified on the command line, the command will run with the group listed in the target user&#8217;s password database entry. The following would all be permitted by the sudoers entry above: </p>
<pre><code>$ sudo -u operator /bin/ls
$ sudo -u operator -g operator /bin/ls
$ sudo -g operator /bin/ls
</code></pre>
<p>In the following example, user <code>tcm</code> may run commands that access a modem device file with the dialer group. </p>
<pre><code>tcm boulder = (:dialer) /usr/bin/tip, /usr/bin/cu,\
        /usr/local/bin/minicom
</code></pre>
<p>Note that in this example only the group will be set, the command still runs as user <code>tcm</code> E.g. </p>
<pre><code>$ sudo -g dialer /usr/bin/cu
</code></pre>
<p>Multiple users and groups may be present in a <code>Runas_Spec</code> in which case the user may select any combination of users and groups via the -<code>u</code> and -<code>g</code> options. In this example: </p>
<pre><code>alan ALL = (root, bin : operator, system) ALL
</code></pre>
<p>user <code>alan</code> may run any command as either user root or bin, optionally setting the group to operator or system.  </p>
<h3>Option_Spec</h3>
<p> A <code>Cmnd</code> may have zero or more options associated with it. Options may consist of SELinux roles and/or types, start and/or end dates and command timeouts. Once an option is set for a <code>Cmnd</code> subsequent <code>Cmnd s</code> in the <code>Cmnd_Spec_List</code> inherit that option unless it is overridden by another option. Note that the option names are reserved words in <i>sudoers</i> This means that none of the valid option names (see below) can be used when declaring an alias.  </p>
<h3>SELinux_Spec</h3>
<p> On systems with SELinux support, <i>sudoers</i> file entries may optionally have an SELinux role and/or type associated with a command. This can be used to implement a form of role-based access control (RBAC). If a role or type is specified with the command it will override any default values specified in <i>sudoers</i> A role or type specified on the command line, however, will supersede the values in <i>sudoers</i>  </p>
<h3>Date_Spec</h3>
<p> <code>sudoers</code> rules can be specified with a start and end date via the <code>NOTBEFORE</code> and <code>NOTAFTER</code> settings. The time stamp must be specified in <i>Generalized Time</i> as defined by RFC 4517. The format is effectively <code>yyyymmddHHMMSSZ</code> where the minutes and seconds are optional. The `Z&#8217; suffix indicates that the time stamp is in Coordinated Universal Time (UTC). It is also possible to specify a timezone offset from UTC in hours and minutes instead of a `Z&#8217; For example, `-0500&#8217; would correspond to Eastern Standard time in the US. As an extension, if no `Z&#8217; or timezone offset is specified, local time will be used. </p>
<p>The following are all valid time stamps: </p>
<pre><code>20170214083000Z
2017021408Z
20160315220000-0500
20151201235900
</code></pre>
<h3>Timeout_Spec</h3>
<p> A command may have a timeout associated with it. If the timeout expires before the command has exited, the command will be terminated. The timeout may be specified in combinations of days, hours, minutes, and seconds with a single-letter case-insensitive suffix that indicates the unit of time. For example, a timeout of 7 days, 8 hours, 30 minutes, and 10 seconds would be written as <code>7d8h30m10s</code> If a number is specified without a unit, seconds are assumed. Any of the days, minutes, hours, or seconds may be omitted. The order must be from largest to smallest unit and a unit may not be specified more than once. </p>
<p>The following are all <i>valid</i> timeout values: <code>7d8h30m10s</code> <code>14d</code> <code>8h30m</code> <code>600s</code> <code>3600</code> The following are <i>invalid</i> timeout values: <code>12m2w1d</code> <code>30s10m4h</code> <code>1d2d3h</code> </p>
<p>This setting is only supported by version 1.8.20 or higher.  </p>
<h3>Chdir_Spec</h3>
<p> The working directory that the command will be run in can be specified using the <code>CWD</code> setting. The Fa directory must be a fully-qualified path name beginning with a `/&#8216; or `~&#8216; character, or the special value ``*&#8216;&#8216; A value of ``*&#8216;&#8216; indicates that the user may specify the working directory by running <code>sudo</code> with the -<code>D</code> option. By default, commands are run from the invoking user&#8217;s current working directory, unless the -<code>i</code> option is given. Path names of the form <code>~user/path/name</code> are interpreted as being relative to the named user&#8217;s home directory. If the user name is omitted, the path will be relative to the runas user&#8217;s home directory. </p>
<p>This setting is only supported by version 1.9.3 or higher.  </p>
<h3>Chroot_Spec</h3>
<p> The root directory that the command will be run in can be specified using the <code>CHROOT</code> setting. The Fa directory must be a fully-qualified path name beginning with a `/&#8216; or `~&#8216; character, or the special value ``*&#8216;&#8216; A value of ``*&#8216;&#8216; indicates that the user may specify the root directory by running <code>sudo</code> with the -<code>R</code> option. This setting can be used to run the command in a <a href="/docs/linux/man/2-chroot/">chroot</a>(2) ``sandbox&#8217;&#8216; similar to the <a href="/docs/linux/man/8-chroot/">chroot</a>(8) utility. Path names of the form <code>~user/path/name</code> are interpreted as being relative to the named user&#8217;s home directory. If the user name is omitted, the path will be relative to the runas user&#8217;s home directory. </p>
<p>This setting is only supported by version 1.9.3 or higher.  </p>
<h3>Tag_Spec</h3>
<p> A command may have zero or more tags associated with it. The following tag values are supported: <code>EXEC</code> <code>NOEXEC</code> <code>FOLLOW</code> <code>NOFOLLOW</code> <code>LOG_INPUT</code> <code>NOLOG_INPUT</code> <code>LOG_OUTPUT</code> <code>NOLOG_OUTPUT</code> <code>MAIL</code> <code>NOMAIL</code> <code>INTERCEPT</code> <code>NOINTERCEPT</code> <code>PASSWD</code> <code>NOPASSWD</code> <code>SETENV</code> and <code>NOSETENV</code> Once a tag is set on a <code>Cmnd</code> subsequent <code>Cmnd s</code> in the <code>Cmnd_Spec_List</code> inherit the tag unless it is overridden by the opposite tag (in other words, <code>PASSWD</code> overrides <code>NOPASSWD</code> and <code>NOEXEC</code> overrides <code>EXEC )</code> </p>
<dl>
<dt><i>EXEC </i><code>and </code><i>NOEXEC</i></dt>
<dd> <p>If <code>sudo</code> has been compiled with <i>noexec</i> support and the underlying operating system supports it, the <code>NOEXEC</code> tag can be used to prevent a dynamically-linked executable from running further commands itself. </p>
<p>In the following example, user <code>aaron</code> may run /usr/bin/more and /usr/bin/vi but shell escapes will be disabled. </p>
<pre><code>aaron shanty = NOEXEC: /usr/bin/more, /usr/bin/vi
</code></pre>
<p>See the Sx Preventing shell escapes section below for more details on how <code>NOEXEC</code> works and whether or not it will work on your system. </p>
 </dd>
<dt><i>FOLLOW </i><code>and </code><i>NOFOLLOW</i></dt>
<dd> <p> Starting with version 1.8.15, <code>sudoedit</code> will not open a file that is a symbolic link unless the <i>sudoedit_follow</i> flag is enabled. The <i>FOLLOW</i> and <i>NOFOLLOW</i> tags override the value of <i>sudoedit_follow</i> and can be used to permit (or deny) the editing of symbolic links on a per-command basis. These tags are only effective for the <i>sudoedit</i> command and are ignored for all other commands. </p>
 </dd>
<dt><i>LOG_INPUT </i><code>and </code><i>NOLOG_INPUT</i></dt>
<dd> <p>These tags override the value of the <i>log_input</i> flag on a per-command basis. For more information, see the description of <i>log_input</i> in the Sx SUDOERS OPTIONS section below. </p>
 </dd>
<dt><i>LOG_OUTPUT </i><code>and </code><i>NOLOG_OUTPUT</i></dt>
<dd> <p>These tags override the value of the <i>log_output</i> flag on a per-command basis. For more information, see the description of <i>log_output</i> in the Sx SUDOERS OPTIONS section below. </p>
 </dd>
<dt><i>MAIL </i><code>and </code><i>NOMAIL</i></dt>
<dd> <p>These tags provide fine-grained control over whether mail will be sent when a user runs a command by overriding the value of the <i>mail_all_cmnds</i> flag on a per-command basis. They have no effect when <code>sudo</code> is run with the -<code>l</code> or -<code>v</code> options. A <i>NOMAIL</i> tag will also override the <i>mail_always</i> and <i>mail_no_perms</i> options. For more information, see the descriptions of <i>mail_all_cmnds</i> <i>mail_always</i> and <i>mail_no_perms</i> in the Sx SUDOERS OPTIONS section below. </p>
 </dd>
<dt><i>PASSWD </i><code>and </code><i>NOPASSWD</i></dt>
<dd> <p>By default, <code>sudo</code> requires that a user authenticate before running a command. This behavior can be modified via the <code>NOPASSWD</code> tag. Like a <code>Runas_Spec</code> the <code>NOPASSWD</code> tag sets a default for the commands that follow it in the <code>Cmnd_Spec_List</code> Conversely, the <code>PASSWD</code> tag can be used to reverse things. For example: </p>
<pre><code>ray rushmore = NOPASSWD: /bin/kill, /bin/ls, /usr/bin/lprm
</code></pre>
<p>would allow the user <code>ray</code> to run /bin/kill /bin/ls and /usr/bin/lprm as <code>root</code> on the machine ``rushmore&#8217;&#8216; without authenticating himself. If we only want <code>ray</code> to be able to run /bin/kill without a password the entry would be: </p>
<pre><code>ray rushmore = NOPASSWD: /bin/kill, PASSWD: /bin/ls, /usr/bin/lprm
</code></pre>
<p>Note, however, that the <code>PASSWD</code> tag has no effect on users who are in the group specified by the <i>exempt_group</i> setting. </p>
<p>By default, if the <code>NOPASSWD</code> tag is applied to any of a user&#8217;s entries for the current host, the user will be able to run ``<code>sudo -l</code> &#8216;&#8216; without a password. Additionally, a user may only run ``<code>sudo -v</code> &#8216;&#8216; without a password if all of the user&#8217;s entries for the current host have the <code>NOPASSWD</code> tag. This behavior may be overridden via the <i>verifypw</i> and <i>listpw</i> options. </p>
 </dd>
<dt><i>SETENV </i><code>and </code><i>NOSETENV</i></dt>
<dd> <p>These tags override the value of the <i>setenv</i> flag on a per-command basis. Note that if <code>SETENV</code> has been set for a command, the user may disable the <i>env_reset</i> flag from the command line via the -<code>E</code> option. Additionally, environment variables set on the command line are not subject to the restrictions imposed by <i>env_check</i> <i>env_delete</i> or <i>env_keep</i> As such, only trusted users should be allowed to set variables in this manner. If the command matched is <code>ALL</code> the <code>SETENV</code> tag is implied for that command; this default may be overridden by use of the <code>NOSETENV</code> tag. </p>
 </dd>
<dt><i>INTERCEPT </i><code>and </code><i>NOINTERCEPT</i></dt>
<dd> <p>If <code>sudo</code> has been compiled with <i>intercept</i> support and the underlying operating system supports it, the <code>INTERCEPT</code> tag can be used to cause programs spawned by a command to be validated against <i>sudoers</i> and logged just like they would be if run through <code>sudo</code> directly. This is useful in conjunction with commands that allow shell escapes such as editors, shells, and paginators. </p>
<p>In the following example, user <code>chuck</code> may run any command on the machine ``research&#8217;&#8216; in intercept mode. </p>
<pre><code>chuck research = INTERCEPT: ALL
</code></pre>
<p>See the Sx Preventing shell escapes section below for more details on how <code>INTERCEPT</code> works and whether or not it will work on your system. </p>
 </dd></dl>
<h3>Wildcards</h3>
<p> <code>sudo</code> allows shell-style <i>wildcards</i> (aka meta or glob characters) to be used in host names, path names, and command line arguments in the <i>sudoers</i> file. Wildcard matching is done via the <a href="/docs/linux/man/3-glob/">glob</a>(3) and <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) functions as specified by St -p1003.1 . </p>
<dl>
<dt><code>*</code></dt>
<dd> <p> Matches any set of zero or more characters (including white space). </p>
 </dd>
<dt><code>?</code></dt>
<dd> <p> Matches any single character (including white space). </p>
 </dd>
<dt><code>[...]</code></dt>
<dd> <p> Matches any character in the specified range. </p>
 </dd>
<dt><code>[!...]</code></dt>
<dd> <p> Matches any character <i>not</i> in the specified range. </p>
 </dd>
<dt><code>\x</code></dt>
<dd> <p> For any character `x&#8217; evaluates to `x&#8217; This is used to escape special characters such as: `*&#8216; , `?&#8216; , `[&#8216; , and `]&#8216; </p>
 </dd></dl>
<p>Bf -symbolic Note that these are not regular expressions. Ef Unlike a regular expression there is no way to match one or more characters within a range. </p>
<p>Character classes may be used if your system&#8217;s <a href="/docs/linux/man/3-glob/">glob</a>(3) and <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) functions support them. However, because the `:&#8216; character has special meaning in <i>sudoers</i> it must be escaped. For example: </p>
<pre><code>/bin/ls [[\:alpha\:]]*
</code></pre>
<p>Would match any file name beginning with a letter. </p>
<p>Note that a forward slash (`/&#8216; ) will <i>not</i> be matched by wildcards used in the file name portion of the command. This is to make a path like: </p>
<pre><code>/usr/bin/*
</code></pre>
<p>match /usr/bin/who but not /usr/bin/X11/xterm </p>
<p>When matching the command line arguments, however, a slash <i>does</i> get matched by wildcards since command line arguments may contain arbitrary strings and not just path names. </p>
<p>Bf -symbolic Wildcards in command line arguments should be used with care. Ef <br />
 Command line arguments are matched as a single, concatenated string. This mean a wildcard character such as `?&#8216; or `*&#8216; will match across word boundaries, which may be unexpected. For example, while a sudoers entry like: </p>
<pre><code>%operator ALL = /bin/cat /var/log/messages*
</code></pre>
<p>will allow command like: </p>
<pre><code>$ sudo cat /var/log/messages.1
</code></pre>
<p>It will also allow: </p>
<pre><code>$ sudo cat /var/log/messages /etc/shadow
</code></pre>
<p>which is probably not what was intended. In most cases it is better to do command line processing outside of the <i>sudoers</i> file in a scripting language.  </p>
<h3>Exceptions to wildcard rules</h3>
<p> The following exceptions apply to the above rules: </p>
<dl>
<dd> <p> If the empty string is the only command line argument in the <i>sudoers</i> file entry it means that command is not allowed to be run with <i>any</i> arguments. </p>
 </dd>
<dt><code>sudoedit</code></dt>
<dd> <p> Command line arguments to the <i>sudoedit</i> built-in command should always be path names, so a forward slash (`/&#8216; ) will not be matched by a wildcard. </p>
 </dd></dl>
<h3>Including other files from within sudoers</h3>
<p> It is possible to include other <i>sudoers</i> files from within the <i>sudoers</i> file currently being parsed using the <code>@include</code> and <code>@includedir</code> directives. For compatibility with sudo versions prior to 1.9.1, <code>#include</code> and <code>#includedir</code> are also accepted. </p>
<p>An include file can be used, for example, to keep a site-wide <i>sudoers</i> file in addition to a local, per-machine file. For the sake of this example the site-wide <i>sudoers</i> file will be /etc/sudoers and the per-machine one will be /etc/sudoers.local To include /etc/sudoers.local from within /etc/sudoers one would use the following line in /etc/sudoers </p>
<pre><code>@include /etc/sudoers.local
</code></pre>
<p>When <code>sudo</code> reaches this line it will suspend processing of the current file (/etc/sudoers ) and switch to /etc/sudoers.local Upon reaching the end of /etc/sudoers.local the rest of /etc/sudoers will be processed. Files that are included may themselves include other files. A hard limit of 128 nested include files is enforced to prevent include file loops. </p>
<p>Starting with version 1.9.1, the path to the include file may contain white space if it is escaped with a backslash (`\&#8216; ) Alternately, the entire path may be enclosed in double quotes () in which case no escaping is necessary. To include a literal backslash in the path, `\\&#8216; should be used. </p>
<p>If the path to the include file is not fully-qualified (does not begin with a `/&#8216; ) , it must be located in the same directory as the sudoers file it was included from. For example, if /etc/sudoers contains the line: </p>
<pre><code>
 @include sudoers.local 
</code></pre>
<p>the file that will be included is /etc/sudoers.local </p>
<p>The file name may also include the <code>%h</code> escape, signifying the short form of the host name. In other words, if the machine&#8217;s host name is ``xerxes&#8217;&#8216; then </p>
<pre><code>@include /etc/sudoers.%h
</code></pre>
<p>will cause <code>sudo</code> to include the file /etc/sudoers.xerxes </p>
<p>The <code>@includedir</code> directive can be used to create a sudoers.d directory that the system package manager can drop <i>sudoers</i> file rules into as part of package installation. For example, given: </p>
<pre><code>@includedir /etc/sudoers.d
</code></pre>
<p> <code>sudo</code> will suspend processing of the current file and read each file in /etc/sudoers.d skipping file names that end in `~&#8216; or contain a `.&#8216; character to avoid causing problems with package manager or editor temporary/backup files. Files are parsed in sorted lexical order. That is, /etc/sudoers.d/01_first will be parsed before /etc/sudoers.d/10_second Be aware that because the sorting is lexical, not numeric, /etc/sudoers.d/1_whoops would be loaded <i>after</i> /etc/sudoers.d/10_second Using a consistent number of leading zeroes in the file names can be used to avoid such problems. After parsing the files in the directory, control returns to the file that contained the <code>@includedir</code> directive. </p>
<p>Note that unlike files included via <code>@include</code> <code>visudo</code> will not edit the files in a <code>@includedir</code> directory unless one of them contains a syntax error. It is still possible to run <code>visudo</code> with the -<code>f</code> flag to edit the files directly, but this will not catch the redefinition of an <i>alias</i> that is also present in a different file.  </p>
<h3>Other special characters and reserved words</h3>
<p> The pound sign (`#&#8216; ) is used to indicate a comment (unless it is part of a #include directive or unless it occurs in the context of a user name and is followed by one or more digits, in which case it is treated as a user-ID). Both the comment character and any text after it, up to the end of the line, are ignored. </p>
<p>The reserved word <code>ALL</code> is a built-in <i>alias</i> that always causes a match to succeed. It can be used wherever one might otherwise use a <code>Cmnd_Alias</code> <code>User_Alias</code> <code>Runas_Alias</code> or <code>Host_Alias</code> Attempting to define an <i>alias</i> named <code>ALL</code> will result in a syntax error. Please note that using <code>ALL</code> can be dangerous since in a command context, it allows the user to run <i>any</i> command on the system. </p>
<p>The following option names permitted in an <code>Option_Spec</code> are also considered reserved words: <code>CHROOT</code> <code>ROLE</code> <code>TYPE</code> <code>TIMEOUT</code> <code>CWD</code> <code>NOTBEFORE</code> and <code>NOTAFTER</code> Attempting to define an <i>alias</i> with the same name as one of the options will result in a syntax error. </p>
<p>An exclamation point (`!&#8216; ) can be used as a logical <i>not</i> operator in a list or <i>alias</i> as well as in front of a <code>Cmnd</code> This allows one to exclude certain values. For the `!&#8216; operator to be effective, there must be something for it to exclude. For example, to match all users except for root one would use: </p>
<pre><code>ALL,!root
</code></pre>
<p>If the <code>ALL</code> is omitted, as in: </p>
<pre><code>!root
</code></pre>
<p>it would explicitly deny root but not match any other users. This is different from a true ``negation&#8217;&#8216; operator. </p>
<p>Note, however, that using a `!&#8216; in conjunction with the built-in <code>ALL</code> alias to allow a user to run ``all but a few&#8217;&#8216; commands rarely works as intended (see Sx SECURITY NOTES below). </p>
<p>Long lines can be continued with a backslash (`\&#8216; ) as the last character on the line. </p>
<p>White space between elements in a list as well as special syntactic characters in a <i>User Specification</i> Po `=&#8216; , `:&#8216; , `(&#8216; , `)&#8216; Pc is optional. </p>
<p>The following characters must be escaped with a backslash (`\&#8216; ) when used as part of a word (e.g., a user name or host name): `!&#8216; , `=&#8216; , `:&#8216; , `,&#8216; , `(&#8216; , `)&#8216; , `\&#8216;  </p>
<h2>SUDOERS OPTIONS</h2>
<p> <code>sudo &#8216;s</code> behavior can be modified by <code>Default_Entry</code> lines, as explained earlier. A list of all supported Defaults parameters, grouped by type, are listed below. </p>
<p> <code>Boolean Flags</code> </p>
<dl>
<dt><code>always_query_group_plugin</code></dt>
<dd> <p> If a <i>group_plugin</i> is configured, use it to resolve groups of the form %group as long as there is not also a system group of the same name. Normally, only groups of the form %:group are passed to the <i>group_plugin</i> This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>always_set_home</code></dt>
<dd> <p> If enabled, <code>sudo</code> will set the <code>HOME</code> environment variable to the home directory of the target user (which is the root user unless the -<code>u</code> option is used). This flag is largely obsolete and has no effect unless the <i>env_reset</i> flag has been disabled or <code>HOME</code> is present in the <i>env_keep</i> list, both of which are strongly discouraged. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>authenticate</code></dt>
<dd> <p> If set, users must authenticate themselves via a password (or other means of authentication) before they may run commands. This default may be overridden via the <code>PASSWD</code> and <code>NOPASSWD</code> tags. This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>case_insensitive_group</code></dt>
<dd> <p> If enabled, group names in <i>sudoers</i> will be matched in a case insensitive manner. This may be necessary when users are stored in LDAP or AD. This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>case_insensitive_user</code></dt>
<dd> <p> If enabled, user names in <i>sudoers</i> will be matched in a case insensitive manner. This may be necessary when groups are stored in LDAP or AD. This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>closefrom_override</code></dt>
<dd> <p> If set, the user may use the -<code>C</code> option which overrides the default starting point at which <code>sudo</code> begins closing open file descriptors. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>compress_io</code></dt>
<dd> <p> If set, and <code>sudo</code> is configured to log a command&#8217;s input or output, the I/O logs will be compressed using <code>zlib</code> This flag is <i>on</i> by default when <code>sudo</code> is compiled with <code>zlib</code> support. </p>
 </dd>
<dt><code>exec_background</code></dt>
<dd> <p> By default, <code>sudo</code> runs a command as the foreground process as long as <code>sudo</code> itself is running in the foreground. When the <i>exec_background</i> flag is enabled and the command is being run in a pseudo-terminal (due to I/O logging or the <i>use_pty</i> flag), the command will be run as a background process. Attempts to read from the controlling terminal (or to change terminal settings) will result in the command being suspended with the <code>SIGTTIN</code> signal (or <code>SIGTTOU</code> in the case of terminal settings). If this happens when <code>sudo</code> is a foreground process, the command will be granted the controlling terminal and resumed in the foreground with no user intervention required. The advantage of initially running the command in the background is that <code>sudo</code> need not read from the terminal unless the command explicitly requests it. Otherwise, any terminal input must be passed to the command, whether it has required it or not (the kernel buffers terminals so it is not possible to tell whether the command really wants the input). This is different from historic <i>sudo</i> behavior or when the command is not being run in a pseudo-terminal. </p>
<p>For this to work seamlessly, the operating system must support the automatic restarting of system calls. Unfortunately, not all operating systems do this by default, and even those that do may have bugs. For example, macOS fails to restart the Fn tcgetattr and Fn tcsetattr system calls (this is a bug in macOS). Furthermore, because this behavior depends on the command stopping with the <code>SIGTTIN</code> or <code>SIGTTOU</code> signals, programs that catch these signals and suspend themselves with a different signal (usually <code>SIGTOP</code> will not be automatically foregrounded. Some versions of the linux <a href="/docs/linux/man/1-su/">su</a>(1) command behave this way. This flag is <i>off</i> by default. </p>
<p>This setting is only supported by version 1.8.7 or higher. It has no effect unless I/O logging is enabled or the <i>use_pty</i> flag is enabled. </p>
 </dd>
<dt><code>env_editor</code></dt>
<dd> <p> If set, <code>visudo</code> will use the value of the <code>SUDO_EDITOR</code> <code>VISUAL</code> or <code>EDITOR</code> environment variables before falling back on the default editor list. Note that <code>visudo</code> is typically run as root so this flag may allow a user with <code>visudo</code> privileges to run arbitrary commands as root without logging. An alternative is to place a colon-separated list of ``safe&#8217;&#8216; editors int the <i>editor</i> setting. <code>visudo</code> will then only use <code>SUDO_EDITOR</code> <code>VISUAL</code> or <code>EDITOR</code> if they match a value specified in <i>editor</i> If the <i>env_reset</i> flag is enabled, the <code>SUDO_EDITOR</code> <code>VISUAL</code> and/or <code>EDITOR</code> environment variables must be present in the <i>env_keep</i> list for the <i>env_editor</i> flag to function when <code>visudo</code> is invoked via <code>sudo</code> This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>env_reset</code></dt>
<dd> <p> If set, <code>sudo</code> will run the command in a minimal environment containing the <code>TERM</code> <code>PATH</code> <code>HOME</code> <code>MAIL</code> <code>SHELL</code> <code>LOGNAME</code> <code>USER</code> and <code>SUDO_*</code> variables. Any variables in the caller&#8217;s environment or in the file specified by the <i>restricted_env_file</i> setting that match the <code>env_keep</code> and <code>env_check</code> lists are then added, followed by any variables present in the file specified by the <i>env_file</i> setting (if any). The contents of the <code>env_keep</code> and <code>env_check</code> lists, as modified by global Defaults parameters in <i>sudoers</i> are displayed when <code>sudo</code> is run by root with the -<code>V</code> option. If the <i>secure_path</i> setting is enabled, its value will be used for the <code>PATH</code> environment variable. This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>fast_glob</code></dt>
<dd> <p> Normally, <code>sudo</code> uses the <a href="/docs/linux/man/3-glob/">glob</a>(3) function to do shell-style globbing when matching path names. However, since it accesses the file system, <a href="/docs/linux/man/3-glob/">glob</a>(3) can take a long time to complete for some patterns, especially when the pattern references a network file system that is mounted on demand (auto mounted). The <i>fast_glob</i> flag causes <code>sudo</code> to use the <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) function, which does not access the file system to do its matching. The disadvantage of <i>fast_glob</i> is that it is unable to match relative path names such as ./ls or ../bin/ls This has security implications when path names that include globbing characters are used with the negation operator, `!&#8216; , as such rules can be trivially bypassed. As such, this flag should not be used when the <i>sudoers</i> file contains rules that contain negated path names which include globbing characters. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>fqdn</code></dt>
<dd> <p> Set this flag if you want to put fully qualified host names in the <i>sudoers</i> file when the local host name (as returned by the <code>hostname</code> command) does not contain the domain name. In other words, instead of myhost you would use myhost.mydomain.edu. You may still use the short form if you wish (and even mix the two). This flag is only effective when the ``canonical&#8217;&#8216; host name, as returned by the Fn getaddrinfo or Fn gethostbyname function, is a fully-qualified domain name. This is usually the case when the system is configured to use DNS for host name resolution. </p>
<p>If the system is configured to use the /etc/hosts file in preference to DNS, the ``canonical&#8217;&#8216; host name may not be fully-qualified. The order that sources are queried for host name resolution is usually specified in the /etc/nsswitch.conf /etc/netsvc.conf /etc/host.conf or, in some cases, /etc/resolv.conf file. In the /etc/hosts file, the first host name of the entry is considered to be the ``canonical&#8217;&#8216; name; subsequent names are aliases that are not used by <code>sudoers.</code> For example, the following hosts file line for the machine ``xyzzy&#8217;&#8216; has the fully-qualified domain name as the ``canonical&#8217;&#8216; host name, and the short version as an alias. </p>
<blockquote><p> <code>192.168.1.1 xyzzy.sudo.ws xyzzy</code> </p>
</blockquote>
<p>If the machine&#8217;s hosts file entry is not formatted properly, the <i>fqdn</i> flag will not be effective if it is queried before DNS. </p>
<p>Beware that when using DNS for host name resolution, turning on <i>fqdn</i> requires <code>sudoers</code> to make DNS lookups which renders <code>sudo</code> unusable if DNS stops working (for example if the machine is disconnected from the network). Also note that just like with the hosts file, you must use the ``canonical&#8217;&#8216; name as DNS knows it. That is, you may not use a host alias Po <code>CNAME</code> entry Pc due to performance issues and the fact that there is no way to get all aliases from DNS. </p>
<p>This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>ignore_audit_errors</code></dt>
<dd> <p> Allow commands to be run even if <code>sudoers</code> cannot write to the audit log. If enabled, an audit log write failure is not treated as a fatal error. If disabled, a command may only be run after the audit event is successfully written. This flag is only effective on systems for which <code>sudoers</code> supports audit logging, including Fx , Linux, macOS, and Solaris. This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>ignore_dot</code></dt>
<dd> <p> If set, <code>sudo</code> will ignore &quot;.&quot; or &quot;&quot; (both denoting current directory) in the <code>PATH</code> environment variable; the <code>PATH</code> itself is not modified. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>ignore_iolog_errors</code></dt>
<dd> <p> Allow commands to be run even if <code>sudoers</code> cannot write to the I/O log (local or remote). If enabled, an I/O log write failure is not treated as a fatal error. If disabled, the command will be terminated if the I/O log cannot be written to. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>ignore_logfile_errors</code></dt>
<dd> <p> Allow commands to be run even if <code>sudoers</code> cannot write to the log file. If enabled, a log file write failure is not treated as a fatal error. If disabled, a command may only be run after the log file entry is successfully written. This flag only has an effect when <code>sudoers</code> is configured to use file-based logging via the <i>logfile</i> setting. This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>ignore_local_sudoers</code></dt>
<dd> <p> If set via LDAP, parsing of /etc/sudoers will be skipped. This is intended for Enterprises that wish to prevent the usage of local sudoers files so that only LDAP is used. This thwarts the efforts of rogue operators who would attempt to add roles to /etc/sudoers When this flag is enabled, /etc/sudoers does not even need to exist. Since this flag tells <code>sudo</code> how to behave when no specific LDAP entries have been matched, this sudoOption is only meaningful for the <code>cn=defaults</code> section. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>ignore_unknown_defaults</code></dt>
<dd> <p> If set, <code>sudo</code> will not produce a warning if it encounters an unknown Defaults entry in the <i>sudoers</i> file or an unknown sudoOption in LDAP. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>insults</code></dt>
<dd> <p> If set, <code>sudo</code> will insult users when they enter an incorrect password. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>log_allowed</code></dt>
<dd> <p> If set, <code>sudoers</code> will log commands allowed by the policy to the system audit log (where supported) as well as to syslog and/or a log file. This flag is <i>on</i> by default. </p>
<p>This setting is only supported by version 1.8.29 or higher. </p>
 </dd>
<dt><code>log_denied</code></dt>
<dd> <p> If set, <code>sudoers</code> will log commands denied by the policy to the system audit log (where supported) as well as to syslog and/or a log file. This flag is <i>on</i> by default. </p>
<p>This setting is only supported by version 1.8.29 or higher. </p>
 </dd>
<dt><code>log_exit_status</code></dt>
<dd> <p> If set, <code>sudoers</code> will log the exit value of commands that are run to syslog and/or a log file. If a command was terminated by a signal, the signal name is logged as well. This flag is <i>off</i> by default. </p>
<p>This setting is only supported by version 1.9.8 or higher. </p>
 </dd>
<dt><code>log_host</code></dt>
<dd> <p> If set, the host name will be included in log entries written to the file configured by the <i>logfile</i> setting. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>log_input</code></dt>
<dd> <p> If set, <code>sudo</code> will run the command in a pseudo-terminal and log all user input. If the standard input is not connected to the user&#8217;s tty, due to I/O redirection or because the command is part of a pipeline, that input is also captured and stored in a separate log file. Anything sent to the standard input will be consumed, regardless of whether or not the command run via <code>sudo</code> is actually reading the standard input. This may have unexpected results when using <code>sudo</code> in a shell script that expects to process the standard input. For more information about I/O logging, see the Sx I/O LOG FILES section. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>log_output</code></dt>
<dd> <p> If set, <code>sudo</code> will run the command in a pseudo-terminal and log all output that is sent to the screen, similar to the <a href="/docs/linux/man/1-script/">script</a>(1) command. For more information about I/O logging, see the Sx I/O LOG FILES section. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>log_server_keepalive</code></dt>
<dd> <p> If set, <code>sudo</code> will enable the TCP keepalive socket option on the connection to the log server. This enables the periodic transmission of keepalive messages to the server. If the server does not respond to a message, the connection will be closed and the running command will be terminated unless the <i>ignore_iolog_errors</i> flag (I/O logging enabled) or the <i>ignore_log_errors</i> flag (I/O logging disabled) is set. This flag is <i>on</i> by default. </p>
<p>This setting is only supported by version 1.9.0 or higher. </p>
 </dd>
<dt><code>log_server_verify</code></dt>
<dd> <p> If set, the server certificate received during the TLS handshake must be valid and it must contain either the server name (from <i>log_servers</i> or its IP address. If either of these conditions is not met, the TLS handshake will fail. This flag is <i>on</i> by default. </p>
<p>This setting is only supported by version 1.9.0 or higher. </p>
 </dd>
<dt><code>log_subcmds</code></dt>
<dd> <p> If set, <code>sudoers</code> will log when a command spawns a child process and executes a program using the Fn execl , Fn execle , Fn execlp , Fn execv , Fn execve , Fn execvp , or Fn execvpe library functions. For example, if a shell is run by <code>sudo</code> the individual commands run via the shell will be logged. This flag is <i>off</i> by default. </p>
<p>The <i>log_subcmds</i> flag uses the same underlying mechanism as the <i>intercept</i> setting. See Sx Preventing shell escapes for more information on what systems support this option and its limitations. This setting is only supported by version 1.9.8 or higher and is incompatible with SELinux RBAC support. </p>
 </dd>
<dt><code>log_year</code></dt>
<dd> <p> If set, the four-digit year will be logged in the (non-syslog) <code>sudo</code> log file. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>long_otp_prompt</code></dt>
<dd> <p> When validating with a One Time Password (OTP) scheme such as <code>S/Key</code> or <code>OPIE</code> a two-line prompt is used to make it easier to cut and paste the challenge to a local window. It&#8217;s not as pretty as the default but some people find it more convenient. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>mail_all_cmnds</code></dt>
<dd> <p> Send mail to the <i>mailto</i> user every time a user attempts to run a command via <code>sudo</code> (this includes <code>sudoedit )</code> No mail will be sent if the user runs <code>sudo</code> with the -<code>l</code> or -<code>v</code> option unless there is an authentication error and the <i>mail_badpass</i> flag is also set. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>mail_always</code></dt>
<dd> <p> Send mail to the <i>mailto</i> user every time a user runs <code>sudo</code> This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>mail_badpass</code></dt>
<dd> <p> Send mail to the <i>mailto</i> user if the user running <code>sudo</code> does not enter the correct password. If the command the user is attempting to run is not permitted by <code>sudoers</code> and one of the <i>mail_all_cmnds</i> <i>mail_always</i> <i>mail_no_host</i> <i>mail_no_perms</i> or <i>mail_no_user</i> flags are set, this flag will have no effect. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>mail_no_host</code></dt>
<dd> <p> If set, mail will be sent to the <i>mailto</i> user if the invoking user exists in the <i>sudoers</i> file, but is not allowed to run commands on the current host. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>mail_no_perms</code></dt>
<dd> <p> If set, mail will be sent to the <i>mailto</i> user if the invoking user is allowed to use <code>sudo</code> but the command they are trying is not listed in their <i>sudoers</i> file entry or is explicitly denied. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>mail_no_user</code></dt>
<dd> <p> If set, mail will be sent to the <i>mailto</i> user if the invoking user is not in the <i>sudoers</i> file. This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>match_group_by_gid</code></dt>
<dd> <p> By default, <code>sudoers</code> will look up each group the user is a member of by group-ID to determine the group name (this is only done once). The resulting list of the user&#8217;s group names is used when matching groups listed in the <i>sudoers</i> file. This works well on systems where the number of groups listed in the <i>sudoers</i> file is larger than the number of groups a typical user belongs to. On systems where group lookups are slow, where users may belong to a large number of groups, and where the number of groups listed in the <i>sudoers</i> file is relatively small, it may be prohibitively expensive and running commands via <code>sudo</code> may take longer than normal. On such systems it may be faster to use the <i>match_group_by_gid</i> flag to avoid resolving the user&#8217;s group-IDs to group names. In this case, <code>sudoers</code> must look up any group name listed in the <i>sudoers</i> file and use the group-ID instead of the group name when determining whether the user is a member of the group. </p>
<p>Note that if <i>match_group_by_gid</i> is enabled, group database lookups performed by <code>sudoers</code> will be keyed by group name as opposed to group-ID. On systems where there are multiple sources for the group database, it is possible to have conflicting group names or group-IDs in the local /etc/group file and the remote group database. On such systems, enabling or disabling <i>match_group_by_gid</i> can be used to choose whether group database queries are performed by name (enabled) or ID (disabled), which may aid in working around group entry conflicts. </p>
<p>The <i>match_group_by_gid</i> flag has no effect when <i>sudoers</i> data is stored in LDAP. This flag is <i>off</i> by default. </p>
<p>This setting is only supported by version 1.8.18 or higher. </p>
 </dd>
<dt><code>intercept</code></dt>
<dd> <p> If set, all commands run via <code>sudo</code> will behave as if the <code>INTERCEPT</code> tag has been set, unless overridden by an <code>NOINTERCEPT</code> tag. See the description of <i>INTERCEPT and NOINTERCEPT</i> above as well as the Sx Preventing shell escapes section at the end of this manual. This flag is <i>off</i> by default. </p>
<p>This setting is only supported by version 1.9.8 or higher and is incompatible with SELinux RBAC support. </p>
 </dd>
<dt><code>intercept_allow_setid</code></dt>
<dd> <p> On most systems, the dynamic loader will ignore <code>LD_PRELOAD</code> (or the equivalent) when running set-user-ID and set-group-ID programs, effectively disabling intercept mode. To prevent this from happening, <code>sudoers</code> will not permit a set-user-ID or set-group-ID program to be run in intercept mode unless <i>intercept_allow_setid</i> is set. This flag has no effect unless the <i>intercept</i> flag is enabled or the <i>INTERCEPT</i> tag has been set for the command. This flag is <i>on</i> by default. </p>
<p>This setting is only supported by version 1.9.8 or higher. </p>
 </dd>
<dt><code>intercept_authenticate</code></dt>
<dd> <p> If set, commands run by an intercepted process must be authenticated when the user&#8217;s time stamp is not current. For example, if a shell is run with <i>intercept</i> enabled, as soon as the invoking user&#8217;s time stamp is out of date, subsequent commands will need to be authenticated. This flag has no effect unless the <i>intercept</i> flag is enabled or the <i>INTERCEPT</i> tag has been set for the command. This flag is <i>off</i> by default. </p>
<p>This setting is only supported by version 1.9.8 or higher. </p>
 </dd>
<dt><code>netgroup_tuple</code></dt>
<dd> <p> If set, netgroup lookups will be performed using the full netgroup tuple: host name, user name, and domain (if one is set). Historically, <code>sudo</code> only matched the user name and domain for netgroups used in a <code>User_List</code> and only matched the host name and domain for netgroups used in a <code>Host_List</code> This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>noexec</code></dt>
<dd> <p> If set, all commands run via <code>sudo</code> will behave as if the <code>NOEXEC</code> tag has been set, unless overridden by an <code>EXEC</code> tag. See the description of <i>EXEC and NOEXEC</i> above as well as the Sx Preventing shell escapes section at the end of this manual. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>pam_acct_mgmt</code></dt>
<dd> <p> On systems that use PAM for authentication, <code>sudo</code> will perform PAM account validation for the invoking user by default. The actual checks performed depend on which PAM modules are configured. If enabled, account validation will be performed regardless of whether or not a password is required. This flag is <i>on</i> by default. </p>
<p>This setting is only supported by version 1.8.28 or higher. </p>
 </dd>
<dt><code>pam_rhost</code></dt>
<dd> <p> On systems that use PAM for authentication, <code>sudo</code> will set the PAM remote host value to the name of the local host when the <i>pam_rhost</i> flag is enabled. On Linux systems, enabling <i>pam_rhost</i> may result in DNS lookups of the local host name when PAM is initialized. On Solaris versions prior to Solaris 8, <i>pam_rhost</i> must be enabled if <i>pam_ruser</i> is also enabled to avoid a crash in the Solaris PAM implementation. </p>
<p>This flag is <i>off</i> by default on systems other than Solaris. </p>
<p>This setting is only supported by version 1.9.0 or higher. </p>
 </dd>
<dt><code>pam_ruser</code></dt>
<dd> <p> On systems that use PAM for authentication, <code>sudo</code> will set the PAM remote user value to the name of the user that invoked sudo when the <i>pam_ruser</i> flag is enabled. This flag is <i>on</i> by default. </p>
<p>This setting is only supported by version 1.9.0 or higher. </p>
 </dd>
<dt><code>pam_session</code></dt>
<dd> <p> On systems that use PAM for authentication, <code>sudo</code> will create a new PAM session for the command to be run in. Unless <code>sudo</code> is given the -<code>i</code> or -<code>s</code> options, PAM session modules are run with the ``silent&#8217;&#8216; flag enabled. This prevents last login information from being displayed for every command on some systems. Disabling <i>pam_session</i> may be needed on older PAM implementations or on operating systems where opening a PAM session changes the utmp or wtmp files. If PAM session support is disabled, resource limits may not be updated for the command being run. If <i>pam_session</i> <i>pam_setcred</i> and <i>use_pty</i> are disabled, <i>log_servers</i> has not been set and I/O logging has not been configured, <code>sudo</code> will execute the command directly instead of running it as a child process. This flag is <i>on</i> by default. </p>
<p>This setting is only supported by version 1.8.7 or higher. </p>
 </dd>
<dt><code>pam_setcred</code></dt>
<dd> <p> On systems that use PAM for authentication, <code>sudo</code> will attempt to establish credentials for the target user by default, if supported by the underlying authentication system. One example of a credential is a Kerberos ticket. If <i>pam_session</i> <i>pam_setcred</i> and <i>use_pty</i> are disabled, <i>log_servers</i> has not been set and I/O logging has not been configured, <code>sudo</code> will execute the command directly instead of running it as a child process. This flag is <i>on</i> by default. </p>
<p>This setting is only supported by version 1.8.8 or higher. </p>
 </dd>
<dt><code>passprompt_override</code></dt>
<dd> <p> If set, the prompt specified by <i>passprompt</i> or the <code>SUDO_PROMPT</code> environment variable will always be used and will replace the prompt provided by a PAM module or other authentication method. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>path_info</code></dt>
<dd> <p> Normally, <code>sudo</code> will tell the user when a command could not be found in their <code>PATH</code> environment variable. Some sites may wish to disable this as it could be used to gather information on the location of executables that the normal user does not have access to. The disadvantage is that if the executable is simply not in the user&#8217;s <code>PATH</code> <code>sudo</code> will tell the user that they are not allowed to run it, which can be confusing. This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>preserve_groups</code></dt>
<dd> <p> By default, <code>sudo</code> will initialize the group vector to the list of groups the target user is in. When <i>preserve_groups</i> is set, the user&#8217;s existing group vector is left unaltered. The real and effective group-IDs, however, are still set to match the target user. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>pwfeedback</code></dt>
<dd> <p> By default, <code>sudo</code> reads the password like most other Unix programs, by turning off echo until the user hits the return (or enter) key. Some users become confused by this as it appears to them that <code>sudo</code> has hung at this point. When <i>pwfeedback</i> is set, <code>sudo</code> will provide visual feedback when the user presses a key. Note that this does have a security impact as an onlooker may be able to determine the length of the password being entered. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>requiretty</code></dt>
<dd> <p> If set, <code>sudo</code> will only run when the user is logged in to a real tty. When this flag is set, <code>sudo</code> can only be run from a login session and not via other means such as <a href="/docs/linux/man/8-cron/">cron</a>(8) or cgi-bin scripts. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>root_sudo</code></dt>
<dd> <p> If set, root is allowed to run <code>sudo</code> too. Disabling this prevents users from ``chaining&#8217;&#8216; <code>sudo</code> commands to get a root shell by doing something like ``<code>sudo sudo /bin/sh</code> &#8216;&#8216; Note, however, that turning off <i>root_sudo</i> will also prevent root from running <code>sudoedit</code> Disabling <i>root_sudo</i> provides no real additional security; it exists purely for historical reasons. This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>rootpw</code></dt>
<dd> <p> If set, <code>sudo</code> will prompt for the root password instead of the password of the invoking user when running a command or editing a file. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>runas_allow_unknown_id</code></dt>
<dd> <p> If enabled, allow matching of runas user and group IDs that are not present in the password or group databases. In addition to explicitly matching unknown user or group IDs in a <code>Runas_List</code> this option also allows the <code>ALL</code> alias to match unknown IDs. This flag is <i>off</i> by default. </p>
<p>This setting is only supported by version 1.8.30 or higher. Older versions of <code>sudo</code> always allowed matching of unknown user and group IDs. </p>
 </dd>
<dt><code>runas_check_shell</code></dt>
<dd> <p> If enabled, <code>sudo</code> will only run commands as a user whose shell appears in the /etc/shells file, even if the invoking user&#8217;s <code>Runas_List</code> would otherwise permit it. If no /etc/shells file is present, a system-dependent list of built-in default shells is used. On many operating systems, system users such as ``bin&#8217;&#8216; do not have a valid shell and this flag can be used to prevent commands from being run as those users. This flag is <i>off</i> by default. </p>
<p>This setting is only supported by version 1.8.30 or higher. </p>
 </dd>
<dt><code>runaspw</code></dt>
<dd> <p> If set, <code>sudo</code> will prompt for the password of the user defined by the <i>runas_default</i> option (defaults to <code>root</code> instead of the password of the invoking user when running a command or editing a file. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>selinux</code></dt>
<dd> <p> If enabled, the user may specify an SELinux role and/or type to use when running the command, as permitted by the SELinux policy. If SELinux is disabled on the system, this flag has no effect. This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>set_home</code></dt>
<dd> <p> If enabled and <code>sudo</code> is invoked with the -<code>s</code> option, the <code>HOME</code> environment variable will be set to the home directory of the target user (which is the root user unless the -<code>u</code> option is used). This flag is largely obsolete and has no effect unless the <i>env_reset</i> flag has been disabled or <code>HOME</code> is present in the <i>env_keep</i> list, both of which are strongly discouraged. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>set_logname</code></dt>
<dd> <p> Normally, <code>sudo</code> will set the <code>LOGNAME</code> and <code>USER</code> environment variables to the name of the target user (usually root unless the -<code>u</code> option is given). However, since some programs (including the RCS revision control system) use <code>LOGNAME</code> to determine the real identity of the user, it may be desirable to change this behavior. This can be done by negating the set_logname option. Note that <i>set_logname</i> will have no effect if the <i>env_reset</i> option has not been disabled and the <i>env_keep</i> list contains <code>LOGNAME</code> or <code>USER</code> This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>set_utmp</code></dt>
<dd> <p> When enabled, <code>sudo</code> will create an entry in the utmp (or utmpx) file when a pseudo-terminal is allocated. A pseudo-terminal is allocated by <code>sudo</code> when it is running in a terminal and one or more of the <i>log_input</i> <i>log_output</i> or <i>use_pty</i> flags is enabled. By default, the new entry will be a copy of the user&#8217;s existing utmp entry (if any), with the tty, time, type, and pid fields updated. This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>setenv</code></dt>
<dd> <p> Allow the user to disable the <i>env_reset</i> option from the command line via the -<code>E</code> option. Additionally, environment variables set via the command line are not subject to the restrictions imposed by <i>env_check</i> <i>env_delete</i> or <i>env_keep</i> As such, only trusted users should be allowed to set variables in this manner. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>shell_noargs</code></dt>
<dd> <p> If set and <code>sudo</code> is invoked with no arguments it acts as if the -<code>s</code> option had been given. That is, it runs a shell as root (the shell is determined by the <code>SHELL</code> environment variable if it is set, falling back on the shell listed in the invoking user&#8217;s /etc/passwd entry if not). This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>stay_setuid</code></dt>
<dd> <p> Normally, when <code>sudo</code> executes a command the real and effective user-IDs are set to the target user (root by default). This option changes that behavior such that the real user-ID is left as the invoking user&#8217;s user-ID. In other words, this makes <code>sudo</code> act as a set-user-ID wrapper. This can be useful on systems that disable some potentially dangerous functionality when a program is run set-user-ID. This option is only effective on systems that support either the <a href="/docs/linux/man/2-setreuid/">setreuid</a>(2) or <a href="/docs/linux/man/2-setresuid/">setresuid</a>(2) system call. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>sudoedit_checkdir</code></dt>
<dd> <p> If set, <code>sudoedit</code> will check all directory components of the path to be edited for writability by the invoking user. Symbolic links will not be followed in writable directories and <code>sudoedit</code> will refuse to edit a file located in a writable directory. These restrictions are not enforced when <code>sudoedit</code> is run by root. On some systems, if all directory components of the path to be edited are not readable by the target user, <code>sudoedit</code> will be unable to edit the file. This flag is <i>on</i> by default. </p>
<p>This setting was first introduced in version 1.8.15 but initially suffered from a race condition. The check for symbolic links in writable intermediate directories was added in version 1.8.16. </p>
 </dd>
<dt><code>sudoedit_follow</code></dt>
<dd> <p> By default, <code>sudoedit</code> will not follow symbolic links when opening files. The <i>sudoedit_follow</i> option can be enabled to allow <code>sudoedit</code> to open symbolic links. It may be overridden on a per-command basis by the <i>FOLLOW</i> and <i>NOFOLLOW</i> tags. This flag is <i>off</i> by default. </p>
<p>This setting is only supported by version 1.8.15 or higher. </p>
 </dd>
<dt><code>syslog_pid</code></dt>
<dd> <p> When logging via <a href="/docs/linux/man/3-syslog/">syslog</a>(3), include the process ID in the log entry. This flag is <i>off</i> by default. </p>
<p>This setting is only supported by version 1.8.21 or higher. </p>
 </dd>
<dt><code>targetpw</code></dt>
<dd> <p> If set, <code>sudo</code> will prompt for the password of the user specified by the -<code>u</code> option (defaults to <code>root</code> instead of the password of the invoking user when running a command or editing a file. Note that this flag precludes the use of a user-ID not listed in the passwd database as an argument to the -<code>u</code> option. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>tty_tickets</code></dt>
<dd> <p> If set, users must authenticate on a per-tty basis. With this flag enabled, <code>sudo</code> will use a separate record in the time stamp file for each terminal. If disabled, a single record is used for all login sessions. </p>
<p>This option has been superseded by the <i>timestamp_type</i> option. </p>
 </dd>
<dt><code>umask_override</code></dt>
<dd> <p> If set, <code>sudo</code> will set the umask as specified in the <i>sudoers</i> file without modification. This makes it possible to specify a umask in the <i>sudoers</i> file that is more permissive than the user&#8217;s own umask and matches historical behavior. If <i>umask_override</i> is not set, <code>sudo</code> will set the umask to be the union of the user&#8217;s umask and what is specified in <i>sudoers</i> This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>use_netgroups</code></dt>
<dd> <p> If set, netgroups (prefixed with `+&#8216; ) , may be used in place of a user or host. For LDAP-based sudoers, netgroup support requires an expensive sub-string match on the server unless the <code>NETGROUP_BASE</code> directive is present in the /etc/ldap.conf file. If netgroups are not needed, this option can be disabled to reduce the load on the LDAP server. This flag is <i>on</i> by default. </p>
 </dd>
<dt><code>use_pty</code></dt>
<dd> <p> If set, and <code>sudo</code> is running in a terminal, the command will be run in a pseudo-terminal (even if no I/O logging is being done). If the <code>sudo</code> process is not attached to a terminal, <i>use_pty</i> has no effect. </p>
<p>A malicious program run under <code>sudo</code> may be capable of injecting commands into the user&#8217;s terminal or running a background process that retains access to the user&#8217;s terminal device even after the main program has finished executing. By running the command in a separate pseudo-terminal, this attack is no longer possible. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>user_command_timeouts</code></dt>
<dd> <p> If set, the user may specify a timeout on the command line. If the timeout expires before the command has exited, the command will be terminated. If a timeout is specified both in the sudoers file and on the command line, the smaller of the two timeouts will be used. See the <code>Timeout_Spec</code> section for a description of the timeout syntax. This flag is <i>off</i> by default. </p>
<p>This setting is only supported by version 1.8.20 or higher. </p>
 </dd>
<dt><code>utmp_runas</code></dt>
<dd> <p> If set, <code>sudo</code> will store the name of the runas user when updating the utmp (or utmpx) file. By default, <code>sudo</code> stores the name of the invoking user. This flag is <i>off</i> by default. </p>
 </dd>
<dt><code>visiblepw</code></dt>
<dd> <p> By default, <code>sudo</code> will refuse to run if the user must enter a password but it is not possible to disable echo on the terminal. If the <i>visiblepw</i> flag is set, <code>sudo</code> will prompt for a password even when it would be visible on the screen. This makes it possible to run things like ``<code>ssh somehost sudo ls</code> &#8216;&#8216; since by default, <a href="/docs/linux/man/1-ssh/">ssh</a>(1) does not allocate a tty when running a command. This flag is <i>off</i> by default. </p>
 </dd></dl>
<p> <code>Integers</code> </p>
<dl>
<dt><code>closefrom</code></dt>
<dd> <p> Before it executes a command, <code>sudo</code> will close all open file descriptors other than standard input, standard output, and standard error (file descriptors 0-2). The <i>closefrom</i> option can be used to specify a different file descriptor at which to start closing. The default is <code>3</code> </p>
 </dd>
<dt><code>command_timeout</code></dt>
<dd> <p> The maximum amount of time a command is allowed to run before it is terminated. See the <code>Timeout_Spec</code> section for a description of the timeout syntax. </p>
<p>This setting is only supported by version 1.8.20 or higher. </p>
 </dd>
<dt><code>log_server_timeout</code></dt>
<dd> <p> The maximum amount of time to wait when connecting to a log server or waiting for a server response. See the <code>Timeout_Spec</code> section for a description of the timeout syntax. The default value is 30 seconds. </p>
<p>This setting is only supported by version 1.9.0 or higher. </p>
 </dd>
<dt><code>maxseq</code></dt>
<dd> <p> The maximum sequence number that will be substituted for the ``<code>%{seq}</code> &#8216;&#8216; escape in the I/O log file (see the <i>iolog_dir</i> description below for more information). While the value substituted for ``<code>%{seq}</code> &#8216;&#8216; is in base 36, <i>maxseq</i> itself should be expressed in decimal. Values larger than 2176782336 (which corresponds to the base 36 sequence number ``ZZZZZZ&#8217;&#8216; will be silently truncated to 2176782336. The default value is 2176782336. </p>
<p>Once the local sequence number reaches the value of <i>maxseq</i> it will ``roll over&#8217;&#8216; to zero, after which <code>sudoers</code> will truncate and re-use any existing I/O log path names. </p>
<p>This setting is only supported by version 1.8.7 or higher. </p>
 </dd>
<dt><code>passwd_tries</code></dt>
<dd> <p> The number of tries a user gets to enter his/her password before <code>sudo</code> logs the failure and exits. The default is <code>3</code> </p>
 </dd>
<dt><code>syslog_maxlen</code></dt>
<dd> <p> On many systems, <a href="/docs/linux/man/3-syslog/">syslog</a>(3) has a relatively small log buffer. IETF RFC 5424 states that syslog servers must support messages of at least 480 bytes and should support messages up to 2048 bytes. By default, <code>sudoers</code> creates log messages up to 980 bytes which corresponds to the historic BSD syslog implementation which used a 1024 byte buffer to store the message, date, hostname, and program name. To prevent syslog messages from being truncated, <code>sudoers</code> will split up log messages that are larger than <i>syslog_maxlen</i> bytes. When a message is split, additional parts will include the string ``(command continued) &#8216;&#8216; after the user name and before the continued command line arguments. </p>
<p>This setting is only supported by version 1.8.19 or higher. </p>
 </dd></dl>
<p> <code>Integers that can be used in a boolean context</code> </p>
<dl>
<dt><code>loglinelen</code></dt>
<dd> <p> Number of characters per line for the file log. This value is used to decide when to wrap lines for nicer log files. This has no effect on the syslog log file, only the file log. The default is <code>80</code> (use 0 or negate the option to disable word wrap). </p>
 </dd>
<dt><code>passwd_timeout</code></dt>
<dd> <p> Number of minutes before the <code>sudo</code> password prompt times out, or <code>0</code> for no timeout. The timeout may include a fractional component if minute granularity is insufficient, for example <code>2.5</code> The default is <code>0</code> </p>
 </dd>
<dt><code>timestamp_timeout</code></dt>
<dd> <p> Number of minutes that can elapse before <code>sudo</code> will ask for a passwd again. The timeout may include a fractional component if minute granularity is insufficient, for example <code>2.5</code> The default is <code>15</code> Set this to <code>0</code> to always prompt for a password. If set to a value less than <code>0</code> the user&#8217;s time stamp will not expire until the system is rebooted. This can be used to allow users to create or delete their own time stamps via ``<code>sudo -v</code> &#8216;&#8216; and ``<code>sudo -k</code> &#8216;&#8216; respectively. </p>
 </dd>
<dt><code>umask</code></dt>
<dd> <p> File mode creation mask to use when running the command. Negate this option or set it to 0777 to prevent <code>sudoers</code> from changing the umask. Unless the <i>umask_override</i> flag is set, the actual umask will be the union of the user&#8217;s umask and the value of the <i>umask</i> setting, which defaults to <code>0022</code> This guarantees that <code>sudo</code> never lowers the umask when running a command. </p>
<p>If <i>umask</i> is explicitly set in <i>sudoers</i> it will override any umask setting in PAM or login.conf. If <i>umask</i> is not set in <i>sudoers</i> the umask specified by PAM or login.conf will take precedence. The umask setting in PAM is not used for <code>sudoedit</code> which does not create a new PAM session. </p>
 </dd></dl>
<p> <code>Strings</code> </p>
<dl>
<dt><code>authfail_message</code></dt>
<dd> <p> Message that is displayed after a user fails to authenticate. The message may include the `%d&#8217; escape which will expand to the number of failed password attempts. If set, it overrides the default message, <code>%d incorrect password attempt(s)</code> </p>
 </dd>
<dt><code>badpass_message</code></dt>
<dd> <p> Message that is displayed if a user enters an incorrect password. The default is <code>Sorry, try again.</code> unless insults are enabled. </p>
 </dd>
<dt><code>editor</code></dt>
<dd> <p> A colon (`:&#8216; ) separated list of editors path names used by <code>sudoedit</code> and <code>visudo</code> For <code>sudoedit</code> this list is used to find an editor when none of the <code>SUDO_EDITOR</code> <code>VISUAL</code> or <code>EDITOR</code> environment variables are set to an editor that exists and is executable. For <code>visudo</code> it is used as a white list of allowed editors; <code>visudo</code> will choose the editor that matches the user&#8217;s <code>SUDO_EDITOR</code> <code>VISUAL</code> or <code>EDITOR</code> environment variable if possible, or the first editor in the list that exists and is executable if not. Unless invoked as <code>sudoedit</code> <code>sudo</code> does not preserve the <code>SUDO_EDITOR</code> <code>VISUAL</code> or <code>EDITOR</code> environment variables unless they are present in the <i>env_keep</i> list or the <i>env_reset</i> option is disabled. The default is /usr/bin/editor </p>
 </dd>
<dt><code>iolog_dir</code></dt>
<dd> <p> The top-level directory to use when constructing the path name for the input/output log directory. Only used if the <i>log_input</i> or <i>log_output</i> options are enabled or when the <code>LOG_INPUT</code> or <code>LOG_OUTPUT</code> tags are present for a command. The session sequence number, if any, is stored in the directory. The default is /var/log/sudo-io </p>
<p>The following percent (`%&#8216; ) escape sequences are supported: </p>
 </dd>
<dl>
<dt><code>%{seq}</code></dt>
<dd> <p> expanded to a monotonically increasing base-36 sequence number, such as 0100A5, where every two digits are used to form a new directory, e.g., 01/00/A5 </p>
 </dd>
<dt><code>%{user}</code></dt>
<dd> <p> expanded to the invoking user&#8217;s login name </p>
 </dd>
<dt><code>%{group}</code></dt>
<dd> <p> expanded to the name of the invoking user&#8217;s real group-ID </p>
 </dd>
<dt><code>%{runas_user}</code></dt>
<dd> <p> expanded to the login name of the user the command will be run as (e.g., root) </p>
 </dd>
<dt><code>%{runas_group}</code></dt>
<dd> <p> expanded to the group name of the user the command will be run as (e.g., wheel) </p>
 </dd>
<dt><code>%{hostname}</code></dt>
<dd> <p> expanded to the local host name without the domain name </p>
 </dd>
<dt><code>%{command}</code></dt>
<dd> <p> expanded to the base name of the command being run </p>
 </dd></dl>
<p>In addition, any escape sequences supported by the system&#8217;s <a href="/docs/linux/man/3-strftime/">strftime</a>(3) function will be expanded. </p>
<p>To include a literal `%&#8216; character, the string `%%&#8216; should be used. </p>
<dt><code>iolog_file</code></dt>
<dd> <p> The path name, relative to <i>iolog_dir</i> in which to store input/output logs when the <i>log_input</i> or <i>log_output</i> options are enabled or when the <code>LOG_INPUT</code> or <code>LOG_OUTPUT</code> tags are present for a command. Note that <i>iolog_file</i> may contain directory components. The default is ``<code>%{seq}</code> &#8216;&#8216; </p>
<p>See the <i>iolog_dir</i> option above for a list of supported percent (`%&#8216; ) escape sequences. </p>
<p>In addition to the escape sequences, path names that end in six or more <code>X s</code> will have the <code>X s</code> replaced with a unique combination of digits and letters, similar to the <a href="/docs/linux/man/3-mktemp/">mktemp</a>(3) function. </p>
<p>If the path created by concatenating <i>iolog_dir</i> and <i>iolog_file</i> already exists, the existing I/O log file will be truncated and overwritten unless <i>iolog_file</i> ends in six or more <code>X s</code> </p>
 </dd>
<dt><code>iolog_flush</code></dt>
<dd> <p> If set, <code>sudo</code> will flush I/O log data to disk after each write instead of buffering it. This makes it possible to view the logs in real-time as the program is executing but may significantly reduce the effectiveness of I/O log compression. This flag is <i>off</i> by default. </p>
<p>This setting is only supported by version 1.8.20 or higher. </p>
 </dd>
<dt><code>iolog_group</code></dt>
<dd> <p> The group name to look up when setting the group-ID on new I/O log files and directories. If <i>iolog_group</i> is not set, the primary group-ID of the user specified by <i>iolog_user</i> is used. If neither <i>iolog_group</i> nor <i>iolog_user</i> are set, I/O log files and directories are created with group-ID 0. </p>
<p>This setting is only supported by version 1.8.19 or higher. </p>
 </dd>
<dt><code>iolog_mode</code></dt>
<dd> <p> The file mode to use when creating I/O log files. Mode bits for read and write permissions for owner, group, or other are honored, everything else is ignored. The file permissions will always include the owner read and write bits, even if they are not present in the specified mode. When creating I/O log directories, search (execute) bits are added to match the read and write bits specified by <i>iolog_mode</i> Defaults to 0600 (read and write by user only). </p>
<p>This setting is only supported by version 1.8.19 or higher. </p>
 </dd>
<dt><code>iolog_user</code></dt>
<dd> <p> The user name to look up when setting the user and group-IDs on new I/O log files and directories. If <i>iolog_group</i> is set, it will be used instead of the user&#8217;s primary group-ID. By default, I/O log files and directories are created with user and group-ID 0. </p>
<p>This setting can be useful when the I/O logs are stored on a Network File System (NFS) share. Having a dedicated user own the I/O log files means that <code>sudoers</code> does not write to the log files as user-ID 0, which is usually not permitted by NFS. </p>
<p>This setting is only supported by version 1.8.19 or higher. </p>
 </dd>
<dt><code>lecture_status_dir</code></dt>
<dd> <p> The directory in which <code>sudo</code> stores per-user lecture status files. Once a user has received the lecture, a zero-length file is created in this directory so that <code>sudo</code> will not lecture the user again. This directory should <i>not</i> be cleared when the system reboots. The default is /var/lib/sudo/lectured </p>
 </dd>
<dt><code>log_server_cabundle</code></dt>
<dd> <p> The path to a certificate authority bundle file, in PEM format, to use instead of the system&#8217;s default certificate authority database when authenticating the log server. The default is to use the system&#8217;s default certificate authority database. This setting has no effect unless <i>log_servers</i> is set and the remote log server is secured with TLS. </p>
<p>This setting is only supported by version 1.9.0 or higher. </p>
 </dd>
<dt><code>log_server_peer_cert</code></dt>
<dd> <p> The path to the <code>sudo</code> client&#8217;s certificate file, in PEM format. This setting is required when the remote log server is secured with TLS and client certificate validation is enabled. For <code>sudo_logsrvd</code> client certificate validation is controlled by the <i>tls_checkpeer</i> option, which defaults to <i>false</i> </p>
<p>This setting is only supported by version 1.9.0 or higher. </p>
 </dd>
<dt><code>log_server_peer_key</code></dt>
<dd> <p> The path to the <code>sudo</code> client&#8217;s private key file, in PEM format. This setting is required when the remote log server is secured with TLS and client certificate validation is enabled. For <code>sudo_logsrvd</code> client certificate validation is controlled by the <i>tls_checkpeer</i> option, which defaults to <i>false</i> </p>
<p>This setting is only supported by version 1.9.0 or higher. </p>
 </dd>
<dt><code>mailsub</code></dt>
<dd> <p> Subject of the mail sent to the <i>mailto</i> user. The escape <code>%h</code> will expand to the host name of the machine. Default is ``<code>*** SECURITY information for %h ***</code> &#8216;&#8216; </p>
 </dd>
<dt><code>noexec_file</code></dt>
<dd> <p> As of <code>sudo</code> version 1.8.1 this option is no longer supported. The path to the noexec file should now be set in the sudo.conf5 file. </p>
 </dd>
<dt><code>pam_askpass_service</code></dt>
<dd> <p> On systems that use PAM for authentication, this is the service name used when the -<code>A</code> option is specified. The default value is either ``<code>@pam_service@</code> &#8216;&#8216; or ``<code>sudo-i</code> &#8216;&#8216; depending on whether or not the -<code>i</code> option is also specified. See the description of <i>pam_service</i> for more information. </p>
<p>This setting is only supported by version 1.9.9 or higher. </p>
 </dd>
<dt><code>pam_login_service</code></dt>
<dd> <p> On systems that use PAM for authentication, this is the service name used when the -<code>i</code> option is specified. The default value is ``<code>sudo-i</code> &#8216;&#8216; See the description of <i>pam_service</i> for more information. </p>
<p>This setting is only supported by version 1.8.8 or higher. </p>
 </dd>
<dt><code>pam_service</code></dt>
<dd> <p> On systems that use PAM for authentication, the service name specifies the PAM policy to apply. This usually corresponds to an entry in the pam.conf file or a file in the /etc/pam.d directory. The default value is ``<code>sudo</code> &#8216;&#8216; </p>
<p>This setting is only supported by version 1.8.8 or higher. </p>
 </dd>
<dt><code>passprompt</code></dt>
<dd> <p> The default prompt to use when asking for a password; can be overridden via the -<code>p</code> option or the <code>SUDO_PROMPT</code> environment variable. The following percent (`%&#8216; ) escape sequences are supported: </p>
 </dd>
<dl>
<dt><code>%H</code></dt>
<dd> <p> expanded to the local host name including the domain name (only if the machine&#8217;s host name is fully qualified or the <i>fqdn</i> option is set) </p>
 </dd>
<dt><code>%h</code></dt>
<dd> <p> expanded to the local host name without the domain name </p>
 </dd>
<dt><code>%p</code></dt>
<dd> <p> expanded to the user whose password is being asked for (respects the <i>rootpw</i> <i>targetpw</i> and <i>runaspw</i> flags in <i>sudoers</i> </p>
 </dd>
<dt><code>%U</code></dt>
<dd> <p> expanded to the login name of the user the command will be run as (defaults to root) </p>
 </dd>
<dt><code>%u</code></dt>
<dd> <p> expanded to the invoking user&#8217;s login name </p>
 </dd>
<dt><code>%%</code></dt>
<dd> <p> two consecutive <code>%</code> characters are collapsed into a single <code>%</code> character </p>
 </dd></dl>
<p>On systems that use PAM for authentication, <i>passprompt</i> will only be used if the prompt provided by the PAM module matches the string ``Password: &#8216;&#8216; or ``username&#8217;s Password: &#8216;&#8216; This ensures that the <i>passprompt</i> setting does not interfere with challenge-response style authentication. The <i>passprompt_override</i> flag can be used to change this behavior. </p>
<p>The default value is ``<code>[sudo] password for %p: </code> &#8216;&#8216; </p>
<dt><code>role</code></dt>
<dd> <p> The default SELinux role to use when constructing a new security context to run the command. The default role may be overridden on a per-command basis in the <i>sudoers</i> file or via command line options. This option is only available when <code>sudo</code> is built with SELinux support. </p>
 </dd>
<dt><code>runas_default</code></dt>
<dd> <p> The default user to run commands as if the -<code>u</code> option is not specified on the command line. This defaults to <code>root</code> </p>
 </dd>
<dt><code>sudoers_locale</code></dt>
<dd> <p> Locale to use when parsing the sudoers file, logging commands, and sending email. Note that changing the locale may affect how sudoers is interpreted. Defaults to ``<code>C</code> &#8216;&#8216; </p>
 </dd>
<dt><code>timestamp_type</code></dt>
<dd> <p> <code>sudoers</code> uses per-user time stamp files for credential caching. The <i>timestamp_type</i> option can be used to specify the type of time stamp record used. It has the following possible values: </p>
 </dd>
<dl>
<dt><code>global</code></dt>
<dd> <p> A single time stamp record is used for all of a user&#8217;s login sessions, regardless of the terminal or parent process ID. An additional record is used to serialize password prompts when <code>sudo</code> is used multiple times in a pipeline, but this does not affect authentication. </p>
 </dd>
<dt><code>ppid</code></dt>
<dd> <p> A single time stamp record is used for all processes with the same parent process ID (usually the shell). Commands run from the same shell (or other common parent process) will not require a password for <i>timestamp_timeout</i> minutes Po <code>15</code> by default Pc . Commands run via <code>sudo</code> with a different parent process ID, for example from a shell script, will be authenticated separately. </p>
 </dd>
<dt><code>tty</code></dt>
<dd> <p> One time stamp record is used for each terminal, which means that a user&#8217;s login sessions are authenticated separately. If no terminal is present, the behavior is the same as <i>ppid</i> Commands run from the same terminal will not require a password for <i>timestamp_timeout</i> minutes Po <code>15</code> by default Pc . </p>
 </dd>
<dt><code>kernel</code></dt>
<dd> <p> The time stamp is stored in the kernel as an attribute of the terminal device. If no terminal is present, the behavior is the same as <i>ppid</i> Negative <i>timestamp_timeout</i> values are not supported and positive values are limited to a maximum of 60 minutes. This is currently only supported on Ox . </p>
 </dd></dl>
<p>The default value is <i>tty</i> </p>
<p>This setting is only supported by version 1.8.21 or higher. </p>
<dt><code>timestampdir</code></dt>
<dd> <p> The directory in which <code>sudo</code> stores its time stamp files. This directory should be cleared when the system reboots. The default is /run/sudo/ts </p>
 </dd>
<dt><code>timestampowner</code></dt>
<dd> <p> The owner of the lecture status directory, time stamp directory and all files stored therein. The default is <code>root</code> </p>
 </dd>
<dt><code>type</code></dt>
<dd> <p> The default SELinux type to use when constructing a new security context to run the command. The default type may be overridden on a per-command basis in the <i>sudoers</i> file or via command line options. This option is only available when <code>sudo</code> is built with SELinux support. </p>
 </dd></dl>
<p> <code>Strings that can be used in a boolean context</code> </p>
<dl>
<dt><code>admin_flag</code></dt>
<dd> <p> The <i>admin_flag</i> option specifies the path to a file that is created the first time a user that is a member of the <i>sudo</i> or <i>admin</i> groups runs <code>sudo</code> Only available if <code>sudo</code> is configured with the <code>--enable-admin-flag</code> option. The default value is <code>~/.sudo_as_admin_successful</code> </p>
 </dd>
<dt><code>env_file</code></dt>
<dd> <p> The <i>env_file</i> option specifies the fully qualified path to a file containing variables to be set in the environment of the program being run. Entries in this file should either be of the form ``<code>VARIABLE=value</code> &#8216;&#8216; or ``<code>export VARIABLE=value</code> &#8216;&#8216; The value may optionally be enclosed in single or double quotes. Variables in this file are only added if the variable does not already exist in the environment. This file is considered to be part of the security policy, its contents are not subject to other <code>sudo</code> environment restrictions such as <i>env_keep</i> and <i>env_check</i> </p>
 </dd>
<dt><code>exempt_group</code></dt>
<dd> <p> Users in this group are exempt from password and PATH requirements. The group name specified should not include a <code>%</code> prefix. This is not set by default. </p>
 </dd>
<dt><code>fdexec</code></dt>
<dd> <p> Determines whether <code>sudo</code> will execute a command by its path or by an open file descriptor. It has the following possible values: </p>
 </dd>
<dl>
<dt><code>always</code></dt>
<dd> <p> Always execute by file descriptor. </p>
 </dd>
<dt><code>never</code></dt>
<dd> <p> Never execute by file descriptor. </p>
 </dd>
<dt><code>digest_only</code></dt>
<dd> <p> Only execute by file descriptor if the command has an associated digest in the <i>sudoers</i> file. </p>
 </dd></dl>
<p>The default value is <i>digest_only</i> This avoids a time of check versus time of use race condition when the command is located in a directory writable by the invoking user. </p>
<p>Note that <i>fdexec</i> will change the first element of the argument vector for scripts ($0 in the shell) due to the way the kernel runs script interpreters. Instead of being a normal path, it will refer to a file descriptor. For example, /dev/fd/4 on Solaris and /proc/self/fd/4 on Linux. A workaround is to use the <code>SUDO_COMMAND</code> environment variable instead. </p>
<p>The <i>fdexec</i> setting is only used when the command is matched by path name. It has no effect if the command is matched by the built-in <code>ALL</code> alias. </p>
<p>This setting is only supported by version 1.8.20 or higher. If the operating system does not support the Fn fexecve system call, this setting has no effect. </p>
<dt><code>group_plugin</code></dt>
<dd> <p> A string containing a <code>sudoers</code> group plugin with optional arguments. The string should consist of the plugin path, either fully-qualified or relative to the /usr/libexec/sudo directory, followed by any configuration arguments the plugin requires. These arguments (if any) will be passed to the plugin&#8217;s initialization function. If arguments are present, the string must be enclosed in double quotes () </p>
<p>For more information see Sx GROUP PROVIDER PLUGINS . </p>
 </dd>
<dt><code>lecture</code></dt>
<dd> <p> This option controls when a short lecture will be printed along with the password prompt. It has the following possible values: </p>
 </dd>
<dl>
<dt><code>always</code></dt>
<dd> <p> Always lecture the user. </p>
 </dd>
<dt><code>never</code></dt>
<dd> <p> Never lecture the user. </p>
 </dd>
<dt><code>once</code></dt>
<dd> <p> Only lecture the user the first time they run <code>sudo</code> </p>
 </dd></dl>
<p>If no value is specified, a value of <i>once</i> is implied. Negating the option results in a value of <i>never</i> being used. The default value is <i>never</i> </p>
<dt><code>lecture_file</code></dt>
<dd> <p> Path to a file containing an alternate <code>sudo</code> lecture that will be used in place of the standard lecture if the named file exists. By default, <code>sudo</code> uses a built-in lecture. </p>
 </dd>
<dt><code>listpw</code></dt>
<dd> <p> This option controls when a password will be required when a user runs <code>sudo</code> with the -<code>l</code> option. It has the following possible values: </p>
 </dd>
<dl>
<dt><code>all</code></dt>
<dd> <p> All the user&#8217;s <i>sudoers</i> file entries for the current host must have the <code>NOPASSWD</code> flag set to avoid entering a password. </p>
 </dd>
<dt><code>always</code></dt>
<dd> <p> The user must always enter a password to use the -<code>l</code> option. </p>
 </dd>
<dt><code>any</code></dt>
<dd> <p> At least one of the user&#8217;s <i>sudoers</i> file entries for the current host must have the <code>NOPASSWD</code> flag set to avoid entering a password. </p>
 </dd>
<dt><code>never</code></dt>
<dd> <p> The user need never enter a password to use the -<code>l</code> option. </p>
 </dd></dl>
<p>If no value is specified, a value of <i>any</i> is implied. Negating the option results in a value of <i>never</i> being used. The default value is <i>any</i> </p>
<dt><code>log_format</code></dt>
<dd> <p> The event log format. Supported log formats are: </p>
 </dd>
<dl>
<dt><code>json</code></dt>
<dd> <p> Logs in JSON format. JSON log entries contain the full user details as well as the execution environment if the command was allowed. Due to limitations of the protocol, JSON events sent via <i>syslog</i> may be truncated. </p>
 </dd>
<dt><code>sudo</code></dt>
<dd> <p> Traditional sudo-style logs, see Sx LOG FORMAT for a description of the log file format. </p>
 </dd></dl>
<p>This setting affects logs sent via <a href="/docs/linux/man/3-syslog/">syslog</a>(3) as well as the file specified by the <i>logfile</i> setting, if any. The default value is <i>sudo</i> </p>
<dt><code>logfile</code></dt>
<dd> <p> Path to the <code>sudo</code> log file (not the syslog log file). Setting a path turns on logging to a file; negating this option turns it off. By default, <code>sudo</code> logs via syslog. </p>
 </dd>
<dt><code>mailerflags</code></dt>
<dd> <p> Flags to use when invoking mailer. Defaults to -<code>t</code> </p>
 </dd>
<dt><code>mailerpath</code></dt>
<dd> <p> Path to mail program used to send warning mail. Defaults to the path to sendmail found at configure time. </p>
 </dd>
<dt><code>mailfrom</code></dt>
<dd> <p> Address to use for the ``from&#8217;&#8216; address when sending warning and error mail. The address should be enclosed in double quotes () to protect against <code>sudo</code> interpreting the <code>@</code> sign. Defaults to the name of the user running <code>sudo</code> </p>
 </dd>
<dt><code>mailto</code></dt>
<dd> <p> Address to send warning and error mail to. The address should be enclosed in double quotes () to protect against <code>sudo</code> interpreting the <code>@</code> sign. Defaults to <code>root</code> </p>
 </dd>
<dt><code>rlimit_as</code></dt>
<dd> <p> The maximum size to which the process&#8217;s address space may grow (in bytes), if supported by the operating system. See Sx Resource limits for more information. </p>
 </dd>
<dt><code>rlimit_core</code></dt>
<dd> <p> The largest size core dump file that may be created (in bytes). See Sx Resource limits for more information. Defaults to 0 (no core dump created). </p>
 </dd>
<dt><code>rlimit_cpu</code></dt>
<dd> <p> The maximum amount of CPU time that the process may use (in seconds). See Sx Resource limits for more information. </p>
 </dd>
<dt><code>rlimit_data</code></dt>
<dd> <p> The maximum size of the data segment for the process (in bytes). See Sx Resource limits for more information. </p>
 </dd>
<dt><code>rlimit_fsize</code></dt>
<dd> <p> The largest size file that the process may create (in bytes). See Sx Resource limits for more information. </p>
 </dd>
<dt><code>rlimit_locks</code></dt>
<dd> <p> The maximum number of locks that the process may establish, if supported by the operating system. See Sx Resource limits for more information. </p>
 </dd>
<dt><code>rlimit_memlock</code></dt>
<dd> <p> The maximum size that the process may lock in memory (in bytes), if supported by the operating system. See Sx Resource limits for more information. </p>
 </dd>
<dt><code>rlimit_nofile</code></dt>
<dd> <p> The maximum number of files that the process may have open. See Sx Resource limits for more information. </p>
 </dd>
<dt><code>rlimit_nproc</code></dt>
<dd> <p> The maximum number of processes that the user may run simultaneously. See Sx Resource limits for more information. </p>
 </dd>
<dt><code>rlimit_rss</code></dt>
<dd> <p> The maximum size to which the process&#8217;s resident set size may grow (in bytes). See Sx Resource limits for more information. </p>
 </dd>
<dt><code>rlimit_stack</code></dt>
<dd> <p> The maximum size to which the process&#8217;s stack may grow (in bytes). See Sx Resource limits for more information. </p>
 </dd>
<dt><code>restricted_env_file</code></dt>
<dd> <p> The <i>restricted_env_file</i> option specifies the fully qualified path to a file containing variables to be set in the environment of the program being run. Entries in this file should either be of the form ``<code>VARIABLE=value</code> &#8216;&#8216; or ``<code>export VARIABLE=value</code> &#8216;&#8216; The value may optionally be enclosed in single or double quotes. Variables in this file are only added if the variable does not already exist in the environment. Unlike <i>env_file</i> the file&#8217;s contents are not trusted and are processed in a manner similar to that of the invoking user&#8217;s environment. If <i>env_reset</i> is enabled, variables in the file will only be added if they are matched by either the <i>env_check</i> or <i>env_keep</i> list. If <i>env_reset</i> is disabled, variables in the file are added as long as they are not matched by the <i>env_delete</i> list. In either case, the contents of <i>restricted_env_file</i> are processed before the contents of <i>env_file</i> </p>
 </dd>
<dt><code>runchroot</code></dt>
<dd> <p> If set, <code>sudo</code> will use this value for the root directory when running a command. The special value ``*&#8216;&#8216; will allow the user to specify the root directory via <code>sudo &#8216;s</code> -<code>R</code> option. See the Sx Chroot_Spec section for more details. </p>
<p>It is only possible to use <i>runchroot</i> as a command-specific Defaults setting if the command exists with the same path both inside and outside the chroot jail. This restriction does not apply to generic, host, or user-based Defaults settings or to a <i>Cmnd_Spec</i> that includes a <i>Chroot_Spec</i> </p>
<p>This setting is only supported by version 1.9.3 or higher. </p>
 </dd>
<dt><code>runcwd</code></dt>
<dd> <p> If set, <code>sudo</code> will use this value for the working directory when running a command. The special value ``*&#8216;&#8216; will allow the user to specify the working directory via <code>sudo &#8216;s</code> -<code>D</code> option. See the Sx Chdir_Spec section for more details. </p>
<p>This setting is only supported by version 1.9.3 or higher. </p>
 </dd>
<dt><code>secure_path</code></dt>
<dd> <p> If set, <code>sudo</code> will use this value in place of the user&#8217;s <code>PATH</code> environment variable. This option can be used to reset the <code>PATH</code> to a known good value that contains directories for system administrator commands such as /usr/sbin </p>
<p>Users in the group specified by the <i>exempt_group</i> option are not affected by <i>secure_path</i> This option is not set by default. </p>
 </dd>
<dt><code>syslog</code></dt>
<dd> <p> Syslog facility if syslog is being used for logging (negate to disable syslog logging). Defaults to <code>authpriv</code> </p>
<p>The following syslog facilities are supported: <code>authpriv</code> (if your OS supports it), <code>auth</code> <code>daemon</code> <code>user</code> <code>local0</code> <code>local1</code> <code>local2</code> <code>local3</code> <code>local4</code> <code>local5</code> <code>local6</code> and <code>local7</code> </p>
 </dd>
<dt><code>syslog_badpri</code></dt>
<dd> <p> Syslog priority to use when the user is not allowed to run a command or when authentication is unsuccessful. Defaults to <code>alert</code> </p>
<p>The following syslog priorities are supported: <code>alert</code> <code>crit</code> <code>debug</code> <code>emerg</code> <code>err</code> <code>info</code> <code>notice</code> <code>warning</code> and <code>none</code> Negating the option or setting it to a value of <code>none</code> will disable logging of unsuccessful commands. </p>
 </dd>
<dt><code>syslog_goodpri</code></dt>
<dd> <p> Syslog priority to use when the user is allowed to run a command and authentication is successful. Defaults to <code>notice</code> </p>
<p>See <i>syslog_badpri</i> for the list of supported syslog priorities. Negating the option or setting it to a value of <code>none</code> will disable logging of successful commands. </p>
 </dd>
<dt><code>verifypw</code></dt>
<dd> <p> This option controls when a password will be required when a user runs <code>sudo</code> with the -<code>v</code> option. It has the following possible values: </p>
 </dd>
<dl>
<dt><code>all</code></dt>
<dd> <p> All the user&#8217;s <i>sudoers</i> file entries for the current host must have the <code>NOPASSWD</code> flag set to avoid entering a password. </p>
 </dd>
<dt><code>always</code></dt>
<dd> <p> The user must always enter a password to use the -<code>v</code> option. </p>
 </dd>
<dt><code>any</code></dt>
<dd> <p> At least one of the user&#8217;s <i>sudoers</i> file entries for the current host must have the <code>NOPASSWD</code> flag set to avoid entering a password. </p>
 </dd>
<dt><code>never</code></dt>
<dd> <p> The user need never enter a password to use the -<code>v</code> option. </p>
 </dd></dl>
<p>If no value is specified, a value of <i>all</i> is implied. Negating the option results in a value of <i>never</i> being used. The default value is <i>all</i> </dl>
 </p>
<p> <code>Lists that can be used in a boolean context</code> </p>
<dl>
<dt><code>env_check</code></dt>
<dd> <p> Environment variables to be removed from the user&#8217;s environment unless they are considered ``safe&#8217;&#8216; For all variables except <code>TZ</code> ``safe&#8217;&#8216; means that the variable&#8217;s value does not contain any `%&#8216; or `/&#8216; characters. This can be used to guard against printf-style format vulnerabilities in poorly-written programs. The <code>TZ</code> variable is considered unsafe if any of the following are true: </p>
 </dd>
<ul>
<li> <p>It consists of a fully-qualified path name, optionally prefixed with a colon (`:&#8216; ) that does not match the location of the zoneinfo directory.  </li>
<li>  It contains a .. path element.  </li>
<li>  It contains white space or non-printable characters.  </li>
<li>  It is longer than the value of <code>PATH_MAX</code>  </li>
</ul>
 </p>
<p>The argument may be a double-quoted, space-separated list or a single value without double-quotes. The list can be replaced, added to, deleted from, or disabled by using the <code>=</code> <code>+=</code> <code>-=</code> and <code>!</code> operators respectively. Regardless of whether the <code>env_reset</code> option is enabled or disabled, variables specified by <code>env_check</code> will be preserved in the environment if they pass the aforementioned check. The global list of environment variables to check is displayed when <code>sudo</code> is run by root with the -<code>V</code> option. </p>
<dt><code>env_delete</code></dt>
<dd> <p> Environment variables to be removed from the user&#8217;s environment when the <i>env_reset</i> option is not in effect. The argument may be a double-quoted, space-separated list or a single value without double-quotes. The list can be replaced, added to, deleted from, or disabled by using the <code>=</code> <code>+=</code> <code>-=</code> and <code>!</code> operators respectively. The global list of environment variables to remove is displayed when <code>sudo</code> is run by root with the -<code>V</code> option. Note that many operating systems will remove potentially dangerous variables from the environment of any set-user-ID process (such as <code>sudo )</code> </p>
 </dd>
<dt><code>env_keep</code></dt>
<dd> <p> Environment variables to be preserved in the user&#8217;s environment when the <i>env_reset</i> option is in effect. This allows fine-grained control over the environment <code>sudo -spawned</code> processes will receive. The argument may be a double-quoted, space-separated list or a single value without double-quotes. The list can be replaced, added to, deleted from, or disabled by using the <code>=</code> <code>+=</code> <code>-=</code> and <code>!</code> operators respectively. The global list of variables to keep is displayed when <code>sudo</code> is run by root with the -<code>V</code> option. </p>
<p>Preserving the <code>HOME</code> environment variable has security implications since many programs use it when searching for configuration or data files. Adding <code>HOME</code> to <i>env_keep</i> may enable a user to run unrestricted commands via <code>sudo</code> and is strongly discouraged. Users wishing to edit files with <code>sudo</code> should run <code>sudoedit</code> (or <code>sudo -e</code> to get their accustomed editor configuration instead of invoking the editor directly. </p>
 </dd>
<dt><code>log_servers</code></dt>
<dd> <p> A list of one or more servers to use for remote event and I/O log storage, separated by white space. Log servers must be running <code>sudo_logsrvd</code> or another service that implements the protocol described by sudo_logsrv.proto5. </p>
<p>Server addresses should be of the form ``host [: <code>port </code>[(tls)] ] &#8216;&#8216; The host portion may be a host name, an IPv4 address, or an IPv6 address in square brackets. </p>
<p>If the optional <i>tls</i> flag is present, the connection will be secured with Transport Layer Security (TLS) version 1.2 or 1.3. Versions of TLS prior to 1.2 are not supported. </p>
<p>If a port is specified, it may either be a port number or a well-known service name as defined by the system service name database. If no port is specified, port 30343 will be used for plaintext connections and port 30344 will be used for TLS connections. </p>
<p>When <i>log_servers</i> is set, event log data will be logged both locally (see the <i>syslog</i> and <i>log_file</i> settings) as well as remotely, but I/O log data will only be logged remotely. If multiple hosts are specified, they will be attempted in reverse order. If no log servers are available, the user will not be able to run a command unless either the <i>ignore_iolog_errors</i> flag (I/O logging enabled) or the <i>ignore_log_errors</i> flag (I/O logging disabled) is set. Likewise, if the connection to the log server is interrupted while <code>sudo</code> is running, the command will be terminated unless the <i>ignore_iolog_errors</i> flag (I/O logging enabled) or the <i>ignore_log_errors</i> flag (I/O logging disabled) is set. </p>
<p>This setting is only supported by version 1.9.0 or higher. </p>
 </dd></dl>
<h2>GROUP PROVIDER PLUGINS</h2>
<p> The <code>sudoers</code> plugin supports its own plugin interface to allow non-Unix group lookups which can query a group source other than the standard Unix group database. This can be used to implement support for the <code>nonunix_group</code> syntax described earlier. </p>
<p>Group provider plugins are specified via the <i>group_plugin</i> setting. The argument to <i>group_plugin</i> should consist of the plugin path, either fully-qualified or relative to the /usr/libexec/sudo directory, followed by any configuration options the plugin requires. These options (if specified) will be passed to the plugin&#8217;s initialization function. If options are present, the string must be enclosed in double quotes () </p>
<p>The following group provider plugins are installed by default: </p>
<dl>
<dt><code>group_file</code></dt>
<dd> <p> The <i>group_file</i> plugin supports an alternate group file that uses the same syntax as the /etc/group file. The path to the group file should be specified as an option to the plugin. For example, if the group file to be used is /etc/sudo-group </p>
<pre><code>Defaults group_plugin=&quot;group_file.so /etc/sudo-group&quot;
</code></pre>
 </dd>
<dt><code>system_group</code></dt>
<dd> <p> The <i>system_group</i> plugin supports group lookups via the standard C library functions Fn getgrnam and Fn getgrid . This plugin can be used in instances where the user belongs to groups not present in the user&#8217;s supplemental group vector. This plugin takes no options: </p>
<pre><code>Defaults group_plugin=system_group.so
</code></pre>
 </dd></dl>
<p>The group provider plugin API is described in detail in sudo_plugin5.  </p>
<h2>LOG FORMAT</h2>
<p> <code>sudoers</code> can log events in either JSON or <i>sudo</i> format, this section describes the <i>sudo</i> log format. Depending on <i>sudoers</i> configuration, <code>sudoers</code> can log events via <a href="/docs/linux/man/3-syslog/">syslog</a>(3), to a local log file, or both. The log format is almost identical in both cases. Any control characters present in the log data are formatted in octal with a leading `#&#8216; character. For example, a horizontal tab is stored as `#011&#8217; and an embedded carriage return is stored as `#015&#8217; In addition, space characters in the command path are stored as `#040&#8217; Command line arguments that contain spaces are enclosed in single quotes (&#8216;&#8216;) This makes it possible to distinguish multiple command line arguments from a single argument that contains spaces. Literal single quotes and backslash characters (`\&#8216; ) in command line arguments are escaped with a backslash.  </p>
<h3>Accepted command log entries</h3>
<p> Commands that sudo runs are logged using the following format (split into multiple lines for readability): </p>
<pre><code>date hostname progname: username : TTY=ttyname ; CHROOT=chroot ; \
    PWD=cwd ; USER=runasuser ; GROUP=runasgroup ; TSID=logid ; \
    ENV=env_vars COMMAND=command
</code></pre>
<p>Where the fields are as follows: </p>
<dl>
<dt><code>date</code></dt>
<dd> <p> The date the command was run. Typically, this is in the format ``MMM, DD, HH:MM:SS&#8217;&#8216; If logging via <a href="/docs/linux/man/3-syslog/">syslog</a>(3), the actual date format is controlled by the syslog daemon. If logging to a file and the <i>log_year</i> option is enabled, the date will also include the year. </p>
 </dd>
<dt><code>hostname</code></dt>
<dd> <p> The name of the host <code>sudo</code> was run on. This field is only present when logging via <a href="/docs/linux/man/3-syslog/">syslog</a>(3). </p>
 </dd>
<dt><code>progname</code></dt>
<dd> <p> The name of the program, usually <i>sudo</i> or <i>sudoedit</i> This field is only present when logging via <a href="/docs/linux/man/3-syslog/">syslog</a>(3). </p>
 </dd>
<dt><code>username</code></dt>
<dd> <p> The login name of the user who ran <code>sudo</code> </p>
 </dd>
<dt><code>ttyname</code></dt>
<dd> <p> The short name of the terminal (e.g., ``console&#8217;&#8216; ``tty01&#8217;&#8216; or ``pts/0&#8217;&#8216; <code>sudo</code> was run on, or ``unknown&#8217;&#8216; if there was no terminal present. </p>
 </dd>
<dt><code>chroot</code></dt>
<dd> <p> The root directory that the command was run in, if one was specified. </p>
 </dd>
<dt><code>cwd</code></dt>
<dd> <p> The current working directory that <code>sudo</code> was run in. </p>
 </dd>
<dt><code>runasuser</code></dt>
<dd> <p> The user the command was run as. </p>
 </dd>
<dt><code>runasgroup</code></dt>
<dd> <p> The group the command was run as if one was specified on the command line. </p>
 </dd>
<dt><code>logid</code></dt>
<dd> <p> An I/O log identifier that can be used to replay the command&#8217;s output. This is only present when the <i>log_input</i> or <i>log_output</i> option is enabled. </p>
 </dd>
<dt><code>env_vars</code></dt>
<dd> <p> A list of environment variables specified on the command line, if specified. </p>
 </dd>
<dt><code>command</code></dt>
<dd> <p> The actual command that was executed, including any command line arguments. </p>
 </dd></dl>
<p>Messages are logged using the locale specified by <i>sudoers_locale</i> which defaults to the ``<code>C</code> &#8216;&#8216; locale.  </p>
<h3>Denied command log entries</h3>
<p> If the user is not allowed to run the command, the reason for the denial will follow the user name. Possible reasons include: </p>
<dl>
<dt><code>user NOT in sudoers</code></dt>
<dd> <p> The user is not listed in the <i>sudoers</i> file. </p>
 </dd>
<dt><code>user NOT authorized on host</code></dt>
<dd> <p> The user is listed in the <i>sudoers</i> file but is not allowed to run commands on the host. </p>
 </dd>
<dt><code>command not allowed</code></dt>
<dd> <p> The user is listed in the <i>sudoers</i> file for the host but they are not allowed to run the specified command. </p>
 </dd>
<dt><code>3 incorrect password attempts</code></dt>
<dd> <p> The user failed to enter their password after 3 tries. The actual number of tries will vary based on the number of failed attempts and the value of the <i>passwd_tries</i> option. </p>
 </dd>
<dt><code>a password is required</code></dt>
<dd> <p> The -<code>n</code> option was specified but a password was required. </p>
 </dd>
<dt><code>sorry, you are not allowed to set the following environment variables</code></dt>
<dd> <p> The user specified environment variables on the command line that were not allowed by <i>sudoers</i> </p>
 </dd></dl>
<h3>Error log entries</h3>
<p> If an error occurs, <code>sudoers</code> will log a message and, in most cases, send a message to the administrator via email. Possible errors include: </p>
<dl>
<dt><code>parse error in /etc/sudoers near line N</code></dt>
<dd> <p> <code>sudoers</code> encountered an error when parsing the specified file. In some cases, the actual error may be one line above or below the line number listed, depending on the type of error. </p>
 </dd>
<dt><code>problem with defaults entries</code></dt>
<dd> <p> The <i>sudoers</i> file contains one or more unknown Defaults settings. This does not prevent <code>sudo</code> from running, but the <i>sudoers</i> file should be checked using <code>visudo</code> </p>
 </dd>
<dt><code>timestamp owner (username): such user</code></dt>
<dd> <p> The time stamp directory owner, as specified by the <i>timestampowner</i> setting, could not be found in the password database. </p>
 </dd>
<dt><code>unable to open/read /etc/sudoers</code></dt>
<dd> <p> The <i>sudoers</i> file could not be opened for reading. This can happen when the <i>sudoers</i> file is located on a remote file system that maps user-ID 0 to a different value. Normally, <code>sudoers</code> tries to open the <i>sudoers</i> file using group permissions to avoid this problem. Consider either changing the ownership of /etc/sudoers or adding an argument like ``sudoers_uid=N&#8217;&#8216; (where `N&#8217; is the user-ID that owns the <i>sudoers</i> file) to the end of the <code>sudoers</code> <code>Plugin</code> line in the sudo.conf5 file. </p>
 </dd>
<dt><code>unable to stat /etc/sudoers</code></dt>
<dd> <p> The /etc/sudoers file is missing. </p>
 </dd>
<dt><code>/etc/sudoers is not a regular file</code></dt>
<dd> <p> The /etc/sudoers file exists but is not a regular file or symbolic link. </p>
 </dd>
<dt><code>/etc/sudoers is owned by uid N, should be 0</code></dt>
<dd> <p> The <i>sudoers</i> file has the wrong owner. If you wish to change the <i>sudoers</i> file owner, please add ``sudoers_uid=N&#8217;&#8216; (where `N&#8217; is the user-ID that owns the <i>sudoers</i> file) to the <code>sudoers</code> <code>Plugin</code> line in the sudo.conf5 file. </p>
 </dd>
<dt><code>/etc/sudoers is world writable</code></dt>
<dd> <p> The permissions on the <i>sudoers</i> file allow all users to write to it. The <i>sudoers</i> file must not be world-writable, the default file mode is 0440 (readable by owner and group, writable by none). The default mode may be changed via the ``sudoers_mode&#8217;&#8216; option to the <code>sudoers</code> <code>Plugin</code> line in the sudo.conf5 file. </p>
 </dd>
<dt><code>/etc/sudoers is owned by gid N, should be 1</code></dt>
<dd> <p> The <i>sudoers</i> file has the wrong group ownership. If you wish to change the <i>sudoers</i> file group ownership, please add ``sudoers_gid=N&#8217;&#8216; (where `N&#8217; is the group-ID that owns the <i>sudoers</i> file) to the <code>sudoers</code> <code>Plugin</code> line in the sudo.conf5 file. </p>
 </dd>
<dt><code>unable to open /run/sudo/ts/username</code></dt>
<dd> <p> <code>sudoers</code> was unable to read or create the user&#8217;s time stamp file. This can happen when <i>timestampowner</i> is set to a user other than root and the mode on /run/sudo is not searchable by group or other. The default mode for /run/sudo is 0711. </p>
 </dd>
<dt><code>unable to write to /run/sudo/ts/username</code></dt>
<dd> <p> <code>sudoers</code> was unable to write to the user&#8217;s time stamp file. </p>
 </dd>
<dt><code>/run/sudo/ts is owned by uid X, should be Y</code></dt>
<dd> <p> The time stamp directory is owned by a user other than <i>timestampowner</i> This can occur when the value of <i>timestampowner</i> has been changed. <code>sudoers</code> will ignore the time stamp directory until the owner is corrected. </p>
 </dd>
<dt><code>/run/sudo/ts is group writable</code></dt>
<dd> <p> The time stamp directory is group-writable; it should be writable only by <i>timestampowner</i> The default mode for the time stamp directory is 0700. <code>sudoers</code> will ignore the time stamp directory until the mode is corrected. </p>
 </dd></dl>
<h3>Notes on logging via syslog</h3>
<p> By default, <code>sudoers</code> logs messages via <a href="/docs/linux/man/3-syslog/">syslog</a>(3). The <i>date</i> <i>hostname</i> and <i>progname</i> fields are added by the system&#8217;s Fn syslog function, not <code>sudoers</code> itself. As such, they may vary in format on different systems. </p>
<p>The maximum size of syslog messages varies from system to system. The <i>syslog_maxlen</i> setting can be used to change the maximum syslog message size from the default value of 980 bytes. For more information, see the description of <i>syslog_maxlen</i>  </p>
<h3>Notes on logging to a file</h3>
<p> If the <i>logfile</i> option is set, <code>sudoers</code> will log to a local file, such as /var/log/sudo When logging to a file, <code>sudoers</code> uses a format similar to <a href="/docs/linux/man/3-syslog/">syslog</a>(3), with a few important differences: </p>
<ol>
<li> <p>The <i>progname</i> field is not present.  </li>
<li>  The <i>hostname</i> is only logged if the <i>log_host</i> option is enabled.  </li>
<li>  The date does not include the year unless the <i>log_year</i> option is enabled.  </li>
<li>  Lines that are longer than <i>loglinelen</i> characters (80 by default) are word-wrapped and continued on the next line with a four character indent. This makes entries easier to read for a human being, but makes it more difficult to use <a href="/docs/linux/man/1-grep/">grep</a>(1) on the log files. If the <i>loglinelen</i> option is set to 0 (or negated with a `!&#8216; ) , word wrap will be disabled.  </li>
</ol>
 </p>
<h2>I/O LOG FILES</h2>
<p> When I/O logging is enabled, <code>sudo</code> will run the command in a pseudo-terminal and log all user input and/or output, depending on which options are enabled. I/O can be logged either to the local machine or to a remote log server. For local logs, I/O is logged to the directory specified by the <i>iolog_dir</i> option Po /var/log/sudo-io by default Pc using a unique session ID that is included in the <code>sudo</code> log line, prefixed with ``<code>TSID=</code> &#8216;&#8216; The <i>iolog_file</i> option may be used to control the format of the session ID. For remote logs, the <i>log_servers</i> setting is used to specify one or more log servers running <code>sudo_logsrvd</code> or another server that implements the protocol described by sudo_logsrv.proto5. </p>
<p>For both local and remote I/O logs, each log is stored in a separate directory that contains the following files: </p>
<dl>
<dt><code>log </code></dt>
<dd> <p> A text file containing information about the command. The first line consists of the following colon-delimited fields: the time the command was run, the name of the user who ran <code>sudo</code> the name of the target user, the name of the target group (optional), the terminal that <code>sudo</code> was run from, and the number of lines and columns of the terminal. The second and third lines contain the working directory the command was run from and the path name of the command itself (with arguments if present). </p>
 </dd>
<dt><code>log.json </code></dt>
<dd> <p> A JSON-formatted file containing information about the command. This is similar to the log file but contains additional information and is easily extensible. The log.json file will be used by <a href="/docs/linux/man/8-sudoreplay/">sudoreplay</a>(8) in preference to the log file if it exists. The file may contain the following elements: </p>
 </dd>
<dl>
<dt><code>timestamp</code></dt>
<dd> <p> A JSON object containing time the command was run. It consists of two values, <i>seconds</i> and <i>nanoseconds</i> </p>
 </dd>
<dt><code>columns</code></dt>
<dd> <p> The number of columns of the terminal the command ran on, or zero if no terminal was present. </p>
 </dd>
<dt><code>command</code></dt>
<dd> <p> The fully-qualified path of the command that was run. </p>
 </dd>
<dt><code>lines</code></dt>
<dd> <p> The number of lines of the terminal the command ran on, or zero if no terminal was present. </p>
 </dd>
<dt><code>runargv</code></dt>
<dd> <p> A JSON array representing the command&#8217;s argument vector as passed to the Fn execve system call. </p>
 </dd>
<dt><code>runenv</code></dt>
<dd> <p> A JSON array representing the command&#8217;s environment as passed to the Fn execve system call. </p>
 </dd>
<dt><code>rungid</code></dt>
<dd> <p> The group ID the command ran as. This element is only present when the user specifies a group on the command line. </p>
 </dd>
<dt><code>rungroup</code></dt>
<dd> <p> The name of the group the command ran as. This element is only present when the user specifies a group on the command line. </p>
 </dd>
<dt><code>runuid</code></dt>
<dd> <p> The user ID the command ran as. </p>
 </dd>
<dt><code>runuser</code></dt>
<dd> <p> The name of the user the command ran as. </p>
 </dd>
<dt><code>submitcwd</code></dt>
<dd> <p> The current working directory at the time <code>sudo</code> was run. </p>
 </dd>
<dt><code>submithost</code></dt>
<dd> <p> The name of the host the command was run on. </p>
 </dd>
<dt><code>submituser</code></dt>
<dd> <p> The name of the user who ran the command via <code>sudo</code> </p>
 </dd>
<dt><code>ttyname</code></dt>
<dd> <p> The path name of the terminal the user invoked <code>sudo</code> from. If the command was run in a pseudo-terminal, <i>ttyname</i> will be different from the terminal the command actually ran in. </p>
 </dd></dl>
<dt><code>timing </code></dt>
<dd> <p> Timing information used to replay the session. Each line consists of the I/O log entry type and amount of time since the last entry, followed by type-specific data. The I/O log entry types and their corresponding type-specific data are: </p>
 </dd>
<dl>
<dt><code>0</code></dt>
<dd> <p> standard input, number of bytes in the entry </p>
 </dd>
<dt><code>1</code></dt>
<dd> <p> standard output, number of bytes in the entry </p>
 </dd>
<dt><code>2</code></dt>
<dd> <p> standard error, number of bytes in the entry </p>
 </dd>
<dt><code>3</code></dt>
<dd> <p> terminal input, number of bytes in the entry </p>
 </dd>
<dt><code>4</code></dt>
<dd> <p> terminal output, number of bytes in the entry </p>
 </dd>
<dt><code>5</code></dt>
<dd> <p> window change, new number lines and columns </p>
 </dd>
<dt><code>6</code></dt>
<dd> <p> bug compatibility for <code>sudo</code> 1.8.7 terminal output </p>
 </dd>
<dt><code>7</code></dt>
<dd> <p> command suspend or resume, signal received </p>
 </dd></dl>
<dt><code>ttyin </code></dt>
<dd> <p> Raw input from the user&#8217;s terminal, exactly as it was received. No post-processing is performed. For manual viewing, you may wish to convert carriage return characters in the log to line feeds. For example: `gunzip&#8217; -c ttyin | tr \r \n </p>
 </dd>
<dt><code>stdin </code></dt>
<dd> <p> The standard input when no terminal is present, or input redirected from a pipe or file. </p>
 </dd>
<dt><code>ttyout </code></dt>
<dd> <p> Output from the pseudo-terminal (what the command writes to the screen). Note that terminal-specific post-processing is performed before the data is logged. This means that, for example, line feeds are usually converted to line feed/carriage return pairs and tabs may be expanded to spaces. </p>
 </dd>
<dt><code>stdout </code></dt>
<dd> <p> The standard output when no terminal is present, or output redirected to a pipe or file. </p>
 </dd>
<dt><code>stderr </code></dt>
<dd> <p> The standard error redirected to a pipe or file. </p>
 </dd></dl>
<p>All files other than log are compressed in gzip format unless the <i>compress_io</i> flag has been disabled. Due to buffering, it is not normally possible to display the I/O logs in real-time as the program is executing. The I/O log data will not be complete until the program run by <code>sudo</code> has exited or has been terminated by a signal. The <i>iolog_flush</i> flag can be used to disable buffering, in which case I/O log data is written to disk as soon as it is available. The output portion of an I/O log file can be viewed with the <a href="/docs/linux/man/8-sudoreplay/">sudoreplay</a>(8) utility, which can also be used to list or search the available logs. </p>
<p>Note that user input may contain sensitive information such as passwords (even if they are not echoed to the screen), which will be stored in the log file unencrypted. In most cases, logging the command output via <i>log_output</i> or <code>LOG_OUTPUT</code> is all that is required. </p>
<p>Since each session&#8217;s I/O logs are stored in a separate directory, traditional log rotation utilities cannot be used to limit the number of I/O logs. The simplest way to limit the number of I/O is by setting the <i>maxseq</i> option to the maximum number of logs you wish to store. Once the I/O log sequence number reaches <i>maxseq</i> it will be reset to zero and <code>sudoers</code> will truncate and re-use any existing I/O logs.  </p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/sudo.conf </code></dt>
<dd> <p> Sudo front-end configuration </p>
 </dd>
<dt><code>/etc/sudoers </code></dt>
<dd> <p> List of who can run what </p>
 </dd>
<dt><code>/etc/group </code></dt>
<dd> <p> Local groups file </p>
 </dd>
<dt><code>/etc/netgroup </code></dt>
<dd> <p> List of network groups </p>
 </dd>
<dt><code>/var/log/sudo-io </code></dt>
<dd> <p> I/O log files </p>
 </dd>
<dt><code>/run/sudo/ts </code></dt>
<dd> <p> Directory containing time stamps for the <code>sudoers</code> security policy </p>
 </dd>
<dt><code>/var/lib/sudo/lectured </code></dt>
<dd> <p> Directory containing lecture status files for the <code>sudoers</code> security policy </p>
 </dd>
<dt><code>/etc/environment </code></dt>
<dd> <p> Initial environment for -<code>i</code> mode on AIX and Linux systems </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> Below are example <i>sudoers</i> file entries. Admittedly, some of these are a bit contrived. First, we allow a few environment variables to pass and then define our <i>aliases</i> </p>
<pre><code># Run X applications through sudo; HOME is used to find the
# .Xauthority file. Note that other programs use HOME to find
# configuration files and this may lead to privilege escalation!
Defaults env_keep += &quot;DISPLAY HOME&quot;
# User alias specification
User_Alias FULLTIMERS = millert, mikef, dowdy
User_Alias PARTTIMERS = bostley, jwfox, crawl
User_Alias WEBADMIN = will, wendy, wim
# Runas alias specification
Runas_Alias OP = root, operator
Runas_Alias DB = oracle, sybase
Runas_Alias ADMINGRP = adm, oper
# Host alias specification
Host_Alias SPARC = bigtime, eclipse, moet, anchor :\
                SGI = grolsch, dandelion, black :\
                ALPHA = widget, thalamus, foobar :\
                HPPA = boa, nag, python
Host_Alias CUNETS = 128.138.0.0/255.255.0.0
Host_Alias CSNETS = 128.138.243.0, 128.138.204.0/24, 128.138.242.0
Host_Alias SERVERS = primary, mail, www, ns
Host_Alias CDROM = orion, perseus, hercules
# Cmnd alias specification
Cmnd_Alias DUMPS = /usr/bin/mt, /usr/sbin/dump, /usr/sbin/rdump,\
                        /usr/sbin/restore, /usr/sbin/rrestore,\
                        sha224:0GomF8mNN3wlDt1HD9XldjJ3SNgpFdbjO1+NsQ== \
                        /home/operator/bin/start_backups
Cmnd_Alias KILL = /usr/bin/kill
Cmnd_Alias PRINTING = /usr/sbin/lpc, /usr/bin/lprm
Cmnd_Alias SHUTDOWN = /usr/sbin/shutdown
Cmnd_Alias HALT = /usr/sbin/halt
Cmnd_Alias REBOOT = /usr/sbin/reboot
Cmnd_Alias SHELLS = /usr/bin/sh, /usr/bin/csh, /usr/bin/ksh,\
                         /usr/local/bin/tcsh, /usr/bin/rsh,\
                         /usr/local/bin/zsh
Cmnd_Alias SU = /usr/bin/su
Cmnd_Alias PAGERS = /usr/bin/more, /usr/bin/pg, /usr/bin/less
</code></pre>
<p>Here we override some of the compiled in default values. We want <code>sudo</code> to log via <a href="/docs/linux/man/3-syslog/">syslog</a>(3) using the <i>auth</i> facility in all cases and for commands to be run with the target user&#8217;s home directory as the working directory. We don&#8217;t want to subject the full time staff to the <code>sudo</code> lecture and we want to allow them to run commands in a <a href="/docs/linux/man/2-chroot/">chroot</a>(2) ``sandbox&#8217;&#8216; via the -<code>R</code> option. User <code>millert</code> need not provide a password and we don&#8217;t want to reset the <code>LOGNAME</code> or <code>USER</code> environment variables when running commands as root. Additionally, on the machines in the <i>SERVERS</i> <code>Host_Alias</code> we keep an additional local log file and make sure we log the year in each log line since the log entries will be kept around for several years. Lastly, we disable shell escapes for the commands in the PAGERS <code>Cmnd_Alias</code> Po /usr/bin/more /usr/bin/pg and /usr/bin/less Pc . Note that this will not effectively constrain users with <code>sudo</code> <code>ALL</code> privileges. </p>
<pre><code># Override built-in defaults
Defaults syslog=auth,runcwd=~
Defaults&gt;root !set_logname
Defaults:FULLTIMERS !lecture,runchroot=*
Defaults:millert !authenticate
Defaults [at] SERVERS log_year, logfile=/var/log/sudo.log
Defaults!PAGERS noexec
</code></pre>
<p>The <i>User specification</i> is the part that actually determines who may run what. </p>
<pre><code>root ALL = (ALL) ALL
%wheel ALL = (ALL) ALL
</code></pre>
<p>We let <code>root</code> and any user in group <code>wheel</code> run any command on any host as any user. </p>
<pre><code>FULLTIMERS ALL = NOPASSWD: ALL
</code></pre>
<p>Full time sysadmins Po <code>millert</code> <code>mikef</code> and <code>dowdy</code> Pc may run any command on any host without authenticating themselves. </p>
<pre><code>PARTTIMERS ALL = ALL
</code></pre>
<p>Part time sysadmins <code>bostley</code> <code>jwfox</code> and <code>crawl</code> may run any command on any host but they must authenticate themselves first (since the entry lacks the <code>NOPASSWD</code> tag). </p>
<pre><code>jack CSNETS = ALL
</code></pre>
<p>The user <code>jack</code> may run any command on the machines in the <i>CSNETS</i> alias (the networks <code>128.138.243.0</code> <code>128.138.204.0</code> and <code>128.138.242.0 )</code> Of those networks, only <code>128.138.204.0</code> has an explicit netmask (in CIDR notation) indicating it is a class C network. For the other networks in <i>CSNETS</i> the local machine&#8217;s netmask will be used during matching. </p>
<pre><code>lisa CUNETS = ALL
</code></pre>
<p>The user <code>lisa</code> may run any command on any host in the <i>CUNETS</i> alias (the class B network <code>128.138.0.0 )</code> </p>
<pre><code>operator ALL = DUMPS, KILL, SHUTDOWN, HALT, REBOOT, PRINTING,\
                sudoedit /etc/printcap, /usr/oper/bin/
</code></pre>
<p>The <code>operator</code> user may run commands limited to simple maintenance. Here, those are commands related to backups, killing processes, the printing system, shutting down the system, and any commands in the directory /usr/oper/bin/ Note that one command in the <code>DUMPS</code> Cmnd_Alias includes a sha224 digest, /home/operator/bin/start_backups This is because the directory containing the script is writable by the operator user. If the script is modified (resulting in a digest mismatch) it will no longer be possible to run it via <code>sudo</code> </p>
<pre><code>joe ALL = /usr/bin/su operator
</code></pre>
<p>The user <code>joe</code> may only <a href="/docs/linux/man/1-su/">su</a>(1) to operator. </p>
<pre><code>pete HPPA = /usr/bin/passwd [A-Za-z]*, !/usr/bin/passwd *root*
%opers ALL = (: ADMINGRP) /usr/sbin/
</code></pre>
<p>Users in the <code>opers</code> group may run commands in /usr/sbin/ as themselves with any group in the <i>ADMINGRP</i> <code>Runas_Alias</code> (the <code>adm</code> and <code>oper</code> groups). </p>
<p>The user <code>pete</code> is allowed to change anyone&#8217;s password except for root on the <i>HPPA</i> machines. Because command line arguments are matched as a single, concatenated string, the `*&#8216; wildcard will match <i>multiple</i> words. This example assumes that <a href="/docs/linux/man/1-passwd/">passwd</a>(1) does not take multiple user names on the command line. Note that on GNU systems, options to <a href="/docs/linux/man/1-passwd/">passwd</a>(1) may be specified after the user argument. As a result, this rule will also allow: </p>
<pre><code>passwd username --expire
</code></pre>
<p>which may not be desirable. </p>
<pre><code>bob SPARC = (OP) ALL : SGI = (OP) ALL
</code></pre>
<p>The user <code>bob</code> may run anything on the <i>SPARC</i> and <i>SGI</i> machines as any user listed in the <i>OP</i> <code>Runas_Alias</code> Po <code>root</code> and <code>operator</code> Pc </p>
<pre><code>jim +biglab = ALL
</code></pre>
<p>The user <code>jim</code> may run any command on machines in the <i>biglab</i> netgroup. <code>sudo</code> knows that ``biglab&#8217;&#8216; is a netgroup due to the `+&#8216; prefix. </p>
<pre><code>+secretaries ALL = PRINTING, /usr/bin/adduser, /usr/bin/rmuser
</code></pre>
<p>Users in the <code>secretaries</code> netgroup need to help manage the printers as well as add and remove users, so they are allowed to run those commands on all machines. </p>
<pre><code>fred ALL = (DB) NOPASSWD: ALL
</code></pre>
<p>The user <code>fred</code> can run commands as any user in the <i>DB</i> <code>Runas_Alias</code> Po <code>oracle</code> or <code>sybase</code> Pc without giving a password. </p>
<pre><code>john ALPHA = /usr/bin/su [!-]*, !/usr/bin/su *root*
</code></pre>
<p>On the <i>ALPHA</i> machines, user <code>john</code> may su to anyone except root but he is not allowed to specify any options to the <a href="/docs/linux/man/1-su/">su</a>(1) command. </p>
<pre><code>jen ALL, !SERVERS = ALL
</code></pre>
<p>The user <code>jen</code> may run any command on any machine except for those in the <i>SERVERS</i> <code>Host_Alias</code> (primary, mail, www, and ns). </p>
<pre><code>jill SERVERS = /usr/bin/, !SU, !SHELLS
</code></pre>
<p>For any machine in the <i>SERVERS</i> <code>Host_Alias</code> <code>jill</code> may run any commands in the directory /usr/bin/ except for those commands belonging to the <i>SU</i> and <i>SHELLS</i> <code>Cmnd_Aliases</code> While not specifically mentioned in the rule, the commands in the <i>PAGERS</i> <code>Cmnd_Alias</code> all reside in /usr/bin and have the <i>noexec</i> option set. </p>
<pre><code>steve CSNETS = (operator) /usr/local/op_commands/
</code></pre>
<p>The user <code>steve</code> may run any command in the directory /usr/local/op_commands/ but only as user operator. </p>
<pre><code>matt valkyrie = KILL
</code></pre>
<p>On his personal workstation, valkyrie, <code>matt</code> needs to be able to kill hung processes. </p>
<pre><code>WEBADMIN www = (www) ALL, (root) /usr/bin/su www
</code></pre>
<p>On the host www, any user in the <i>WEBADMIN</i> <code>User_Alias</code> (will, wendy, and wim), may run any command as user www (which owns the web pages) or simply <a href="/docs/linux/man/1-su/">su</a>(1) to www. </p>
<pre><code>ALL CDROM = NOPASSWD: /sbin/umount /CDROM,\
                /sbin/mount -o nosuid\,nodev /dev/cd0a /CDROM
</code></pre>
<p>Any user may mount or unmount a CD-ROM on the machines in the CDROM <code>Host_Alias</code> (orion, perseus, hercules) without entering a password. This is a bit tedious for users to type, so it is a prime candidate for encapsulating in a shell script.  </p>
<h2>SECURITY NOTES</h2>
<h3>Limitations of the So ! Sc operator</h3>
<p> It is generally not effective to ``subtract&#8217;&#8216; commands from <code>ALL</code> using the `!&#8216; operator. A user can trivially circumvent this by copying the desired command to a different name and then executing that. For example: </p>
<pre><code>bill ALL = ALL, !SU, !SHELLS
</code></pre>
<p>Doesn&#8217;t really prevent <code>bill</code> from running the commands listed in <i>SU</i> or <i>SHELLS</i> since he can simply copy those commands to a different name, or use a shell escape from an editor or other program. Therefore, these kind of restrictions should be considered advisory at best (and reinforced by policy). </p>
<p>In general, if a user has sudo <code>ALL</code> there is nothing to prevent them from creating their own program that gives them a root shell (or making their own copy of a shell) regardless of any `!&#8216; elements in the user specification.  </p>
<i></i><h3>Security implications of fast_glob</h3>
<p> If the <i>fast_glob</i> option is in use, it is not possible to reliably negate commands where the path name includes globbing (aka wildcard) characters. This is because the C library&#8217;s <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) function cannot resolve relative paths. While this is typically only an inconvenience for rules that grant privileges, it can result in a security issue for rules that subtract or revoke privileges. </p>
<p>For example, given the following <i>sudoers</i> file entry: </p>
<pre><code>john ALL = /usr/bin/passwd [a-zA-Z0-9]*, /usr/bin/chsh [a-zA-Z0-9]*,\
              /usr/bin/chfn [a-zA-Z0-9]*, !/usr/bin/* root
</code></pre>
<p>User <code>john</code> can still run <code>/usr/bin/passwd root</code> if <i>fast_glob</i> is enabled by changing to /usr/bin and running <code>./passwd root</code> instead.  </p>
<h3>Preventing shell escapes</h3>
<p> Once <code>sudo</code> executes a program, that program is free to do whatever it pleases, including run other programs. This can be a security issue since it is not uncommon for a program to allow shell escapes, which lets a user bypass <code>sudo &#8216;s</code> access control and logging. Common programs that permit shell escapes include shells (obviously), editors, paginators, mail, and terminal programs. </p>
<p>There are four basic approaches to this problem: </p>
<dl>
<dt><code>restrict</code></dt>
<dd> <p> Avoid giving users access to commands that allow the user to run arbitrary commands. Many editors have a restricted mode where shell escapes are disabled, though <code>sudoedit</code> is a better solution to running editors via <code>sudo</code> Due to the large number of programs that offer shell escapes, restricting users to the set of programs that do not is often unworkable. </p>
 </dd>
<dt><code>intercept</code></dt>
<dd> <p> Many systems that support shared libraries have the ability to override default library functions by pointing an environment variable (usually <code>LD_PRELOAD</code> to an alternate shared library. On such systems, <code>sudo &#8216;s</code> <i>intercept</i> functionality can be used to transparently intercept an attempt to run a new command, allow or deny it based on <i>sudoers</i> rules, and log the result. For example, this can be used to restrict the commands run from within a privileged shell. Note, however, that this applies only to dynamically-linked executables. Statically-linked executables and executables running under binary emulation are not affected. Also, most shells support built-in commands and the ability to read or write sensitive files that cannot be intercepted by <code>sudo</code> </p>
<p>Currently, <code>sudo &#8216;s</code> <i>intercept</i> functionality only works for programs that use the Fn execl , Fn execle , Fn execlp , Fn execv , Fn execve , Fn execvp , or Fn execvpe library functions to run the new command. This may be expanded in a future release of <code>sudo</code> Because most dynamic loaders ignore <code>LD_PRELOAD</code> (or the equivalent) when running set-user-ID and set-group-ID programs, <code>sudoers</code> will not permit such programs to be run in <i>intercept</i> mode. </p>
<p>The <i>intercept</i> feature is known to work on Solaris, *BSD, Linux, macOS, HP-UX 11.x and AIX 5.3 and above. It should be supported on most operating systems that support the <code>LD_PRELOAD</code> environment variable. Check your operating system&#8217;s manual pages for the dynamic linker (usually ld.so, ld.so.1, dyld, dld.sl, rld, or loader) to see if <code>LD_PRELOAD</code> is supported. It is <i>not</i> supported when <code>sudo &#8216;s</code> SELinux RBAC support is in use due to a fundamental incompatibility. </p>
<p>To enable intercept mode on a per-command basis, use the <code>INTERCEPT</code> tag as documented in the User Specification section above. Here is that example again: </p>
<pre><code>chuck research = INTERCEPT: ALL
</code></pre>
<p>This allows user <code>chuck</code> to run any command on the machine ``research&#8217;&#8216; in intercept mode. Any commands run via shell escapes will be validated and logged by <code>sudo</code> If you are unsure whether or not your system is capable of supporting <i>intercept</i> you can always just try it out and check whether or not external commands run via a shell are logged when <i>intercept</i> is enabled. </p>
 </dd>
<dt><code>log</code></dt>
<dd> <p> There are two separate but related ways to log additional commands. The first is to enable I/O logging using the <i>log_output</i> flag. This will log the command&#8217;s output but will not create an event log entry when the additional command is run. The second is to enable the <i>log_subcmds</i> flag in <i>sudoers</i> which will create an event log entry every time a new command is run. If I/O logging is also enabled, the log entry will include a time offset into the I/O log to indicate when the command was run. This offset can be passed to the <a href="/docs/linux/man/8-sudoreplay/">sudoreplay</a>(8) utility to replay the I/O log at the exact moment when the command was run. The <i>log_subcmds</i> flag uses the same mechanism as <i>intercept</i> (see above) and has the same limitations. </p>
 </dd>
<dt><code>noexec</code></dt>
<dd> <p> <code>sudo &#8216;s</code> <i>noexec</i> functionality can be used to prevent a program run by <code>sudo</code> from executing any other programs. On most systems, it uses the same mechanism as <i>intercept</i> (see above) and thus the same caveats apply. The <i>noexec</i> functionality is capable of blocking execution of commands run via the Fn execl , Fn execle , Fn execlp , Fn exect , Fn execv , Fn execve , Fn execveat , Fn execvP , Fn execvp , Fn execvpe , Fn fexecve , Fn popen , Fn posix_spawn , Fn posix_spawnp , Fn system , and Fn wordexp functions. On Linux, a Fn seccomp filter is used to implement <i>noexec</i> On Solaris 10 and higher, <i>noexec</i> uses Solaris privileges instead of the <code>LD_PRELOAD</code> environment variable. </p>
<p>To enable <i>noexec</i> for a command, use the <code>NOEXEC</code> tag as documented in the User Specification section above. Here is that example again: </p>
<pre><code>aaron shanty = NOEXEC: /usr/bin/more, /usr/bin/vi
</code></pre>
<p>This allows user <code>aaron</code> to run /usr/bin/more and /usr/bin/vi with <i>noexec</i> enabled. This will prevent those two commands from executing other commands (such as a shell). If you are unsure whether or not your system is capable of supporting <i>noexec</i> you can always just try it out and check whether shell escapes work when <i>noexec</i> is enabled. </p>
 </dd></dl>
<p>Note that restricting shell escapes is not a panacea. Programs running as root are still capable of many potentially hazardous operations (such as changing or overwriting files) that could lead to unintended privilege escalation. In the specific case of an editor, a safer approach is to give the user permission to run <code>sudoedit</code> (see below).  </p>
<h3>Secure editing</h3>
<p> The <code>sudoers</code> plugin includes <code>sudoedit</code> support which allows users to securely edit files with the editor of their choice. As <code>sudoedit</code> is a built-in command, it must be specified in the <i>sudoers</i> file without a leading path. However, it may take command line arguments just as a normal command does. Wildcards used in <i>sudoedit</i> command line arguments are expected to be path names, so a forward slash (`/&#8216; ) will not be matched by a wildcard. </p>
<p>Unlike other <code>sudo</code> commands, the editor is run with the permissions of the invoking user and with the environment unmodified. More information may be found in the description of the -<code>e</code> option in <a href="/docs/linux/man/8-sudo/">sudo</a>(8). </p>
<p>For example, to allow user operator to edit the ``message of the day&#8217;&#8216; file: </p>
<blockquote><pre><code>operator sudoedit /etc/motd
</code></pre>
</blockquote>
<p>The operator user then runs <code>sudoedit</code> as follows: </p>
<blockquote><pre><code>$ sudoedit /etc/motd
</code></pre>
</blockquote>
<p>The editor will run as the operator user, not root, on a temporary copy of /etc/motd After the file has been edited, /etc/motd will be updated with the contents of the temporary copy. </p>
<p>Users should <i>never</i> be granted <code>sudoedit</code> permission to edit a file that resides in a directory the user has write access to, either directly or via a wildcard. If the user has write access to the directory it is possible to replace the legitimate file with a link to another file, allowing the editing of arbitrary files. To prevent this, starting with version 1.8.16, symbolic links will not be followed in writable directories and <code>sudoedit</code> will refuse to edit a file located in a writable directory unless the <i>sudoedit_checkdir</i> option has been disabled or the invoking user is root. Additionally, in version 1.8.15 and higher, <code>sudoedit</code> will refuse to open a symbolic link unless either the <i>sudoedit_follow</i> option is enabled or the <i>sudoedit</i> command is prefixed with the <code>FOLLOW</code> tag in the <i>sudoers</i> file.  </p>
<h3>Time stamp file checks</h3>
<p> <code>sudoers</code> will check the ownership of its time stamp directory Po /run/sudo/ts by default Pc and ignore the directory&#8217;s contents if it is not owned by root or if it is writable by a user other than root. Older versions of <code>sudo</code> stored time stamp files in /tmp this is no longer recommended as it may be possible for a user to create the time stamp themselves on systems that allow unprivileged users to change the ownership of files they create. </p>
<p>While the time stamp directory <i>should</i> be cleared at reboot time, not all systems contain a /run or /var/run directory. To avoid potential problems, <code>sudoers</code> will ignore time stamp files that date from before the machine booted on systems where the boot time is available. </p>
<p>Some systems with graphical desktop environments allow unprivileged users to change the system clock. Since <code>sudoers</code> relies on the system clock for time stamp validation, it may be possible on such systems for a user to run <code>sudo</code> for longer than <i>timestamp_timeout</i> by setting the clock back. To combat this, <code>sudoers</code> uses a monotonic clock (which never moves backwards) for its time stamps if the system supports it. </p>
<p> <code>sudoers</code> will not honor time stamps set far in the future. Time stamps with a date greater than current_time + 2 * <code>TIMEOUT</code> will be ignored and <code>sudoers</code> will log and complain. </p>
<p>If the <i>timestamp_type</i> option is set to ``tty&#8217;&#8216; the time stamp record includes the device number of the terminal the user authenticated with. This provides per-terminal granularity but time stamp records may still outlive the user&#8217;s session. </p>
<p>Unless the <i>timestamp_type</i> option is set to ``global&#8217;&#8216; the time stamp record also includes the session ID of the process that last authenticated. This prevents processes in different terminal sessions from using the same time stamp record. On systems where a process&#8217;s start time can be queried, the start time of the session leader is recorded in the time stamp record. If no terminal is present or the <i>timestamp_type</i> option is set to ``ppid&#8217;&#8216; the start time of the parent process is used instead. In most cases this will prevent a time stamp record from being re-used without the user entering a password when logging out and back in again.  </p>
<h2>DEBUGGING</h2>
<p> Versions 1.8.4 and higher of the <code>sudoers</code> plugin support a flexible debugging framework that can help track down what the plugin is doing internally if there is a problem. This can be configured in the sudo.conf5 file. </p>
<p>The <code>sudoers</code> plugin uses the same debug flag format as the <code>sudo</code> front-end: <i>subsystem </i><code>@ </code><i>priority</i> </p>
<p>The priorities used by <code>sudoers,</code> in order of decreasing severity, are: <i>crit , err , warn , notice , diag , info , trace</i> and <i>debug</i> Each priority, when specified, also includes all priorities higher than it. For example, a priority of <i>notice</i> would include debug messages logged at <i>notice</i> and higher. </p>
<p>The following subsystems are used by the <code>sudoers</code> plugin: </p>
<dl>
<dt><i>alias</i></dt>
<dd> <p> <code>User_Alias</code> <code>Runas_Alias</code> <code>Host_Alias</code> and <code>Cmnd_Alias</code> processing </p>
 </dd>
<dt><i>all</i></dt>
<dd> <p> matches every subsystem </p>
 </dd>
<dt><i>audit</i></dt>
<dd> <p> BSM and Linux audit code </p>
 </dd>
<dt><i>auth</i></dt>
<dd> <p> user authentication </p>
 </dd>
<dt><i>defaults</i></dt>
<dd> <p> <i>sudoers</i> file <i>Defaults</i> settings </p>
 </dd>
<dt><i>env</i></dt>
<dd> <p> environment handling </p>
 </dd>
<dt><i>ldap</i></dt>
<dd> <p> LDAP-based sudoers </p>
 </dd>
<dt><i>logging</i></dt>
<dd> <p> logging support </p>
 </dd>
<dt><i>match</i></dt>
<dd> <p> matching of users, groups, hosts, and netgroups in the <i>sudoers</i> file </p>
 </dd>
<dt><i>netif</i></dt>
<dd> <p> network interface handling </p>
 </dd>
<dt><i>nss</i></dt>
<dd> <p> network service switch handling in <code>sudoers</code> </p>
 </dd>
<dt><i>parser</i></dt>
<dd> <p> <i>sudoers</i> file parsing </p>
 </dd>
<dt><i>perms</i></dt>
<dd> <p> permission setting </p>
 </dd>
<dt><i>plugin</i></dt>
<dd> <p> The equivalent of <i>main</i> for the plugin. </p>
 </dd>
<dt><i>pty</i></dt>
<dd> <p> pseudo-terminal related code </p>
 </dd>
<dt><i>rbtree</i></dt>
<dd> <p> redblack tree internals </p>
 </dd>
<dt><i>sssd</i></dt>
<dd> <p> SSSD-based sudoers </p>
 </dd>
<dt><i>util</i></dt>
<dd> <p> utility functions </p>
 </dd></dl>
<p>For example: </p>
<pre><code>Debug sudoers.so /var/log/sudoers_debug match [at] info,nss [at] info
</code></pre>
<p>For more information, see the sudo.conf5 manual.  </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1), <a href="/docs/linux/man/1-su/">su</a>(1), <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3), <a href="/docs/linux/man/3-glob/">glob</a>(3), <a href="/docs/linux/man/3-mktemp/">mktemp</a>(3), <a href="/docs/linux/man/3-strftime/">strftime</a>(3), sudo.conf5, sudo_plugin5, sudoers.ldap5, sudoers_timestamp5, <a href="/docs/linux/man/8-sudo/">sudo</a>(8), <a href="/docs/linux/man/8-visudo/">visudo</a>(8)  </p>
<h2>AUTHORS</h2>
<p> Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<blockquote><p> An Todd C. Miller </p>
</blockquote>
<p>See the CONTRIBUTORS file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/contributors.html)">https://www.sudo.ws/contributors.html)</a> for an exhaustive list of people who have contributed to <code>sudo</code>  </p>
<h2>CAVEATS</h2>
<p> The <i>sudoers</i> file should <code>always</code> be edited by the <code>visudo</code> utility which locks the file and checks for syntax errors. If <i>sudoers</i> contains syntax errors, <code>sudo</code> may refuse to run, which is a serious problem if <code>sudo</code> is your only method of obtaining superuser privileges. Recent versions of <code>sudoers</code> will attempt to recover after a syntax error by ignoring the rest of the line after encountering an error. Older versions of <code>sudo</code> will not run if <i>sudoers</i> contains a syntax error. </p>
<p>When using netgroups of machines (as opposed to users), if you store fully qualified host name in the netgroup (as is usually the case), you either need to have the machine&#8217;s host name be fully qualified as returned by the <code>hostname</code> command or use the <i>fqdn</i> option in <i>sudoers</i>  </p>
<h2>BUGS</h2>
<p> If you feel you have found a bug in <code>sudo</code> please submit a bug report at <a rel="nofollow" href="https://bugzilla.sudo.ws/">https://bugzilla.sudo.ws/</a>  </p>
<h2>SUPPORT</h2>
<p> Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="https://www.sudo.ws/mailman/listinfo/sudo-users">https://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.  </p>
<h2>DISCLAIMER</h2>
<p> <code>sudo</code> is provided ``AS IS&#8217;&#8216; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the LICENSE file distributed with <code>sudo</code> or <a rel="nofollow" href="https://www.sudo.ws/license.html">https://www.sudo.ws/license.html</a> for complete details. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">DESCRIPTION</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAD">Configuring sudo.conf for sudoers</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">User Authentication</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">Logging</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">Command environment</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAH">SUDOERS FILE FORMAT</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAI">Resource limits</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">Quick guide to EBNF</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">Aliases</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">Defaults</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">User specification</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">Runas_Spec</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">Option_Spec</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">SELinux_Spec</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">Date_Spec</a></dt>
<dd>  </dd>
<dt><a href="#lbAR">Timeout_Spec</a></dt>
<dd>  </dd>
<dt><a href="#lbAS">Chdir_Spec</a></dt>
<dd>  </dd>
<dt><a href="#lbAT">Chroot_Spec</a></dt>
<dd>  </dd>
<dt><a href="#lbAU">Tag_Spec</a></dt>
<dd>  </dd>
<dt><a href="#lbAV">Wildcards</a></dt>
<dd>  </dd>
<dt><a href="#lbAW">Exceptions to wildcard rules</a></dt>
<dd>  </dd>
<dt><a href="#lbAX">Including other files from within sudoers</a></dt>
<dd>  </dd>
<dt><a href="#lbAY">Other special characters and reserved words</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAZ">SUDOERS OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbBA">GROUP PROVIDER PLUGINS</a></dt>
<dd>  </dd>
<dt><a href="#lbBB">LOG FORMAT</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbBC">Accepted command log entries</a></dt>
<dd>  </dd>
<dt><a href="#lbBD">Denied command log entries</a></dt>
<dd>  </dd>
<dt><a href="#lbBE">Error log entries</a></dt>
<dd>  </dd>
<dt><a href="#lbBF">Notes on logging via syslog</a></dt>
<dd>  </dd>
<dt><a href="#lbBG">Notes on logging to a file</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbBH">I/O LOG FILES</a></dt>
<dd>  </dd>
<dt><a href="#lbBI">FILES</a></dt>
<dd>  </dd>
<dt><a href="#lbBJ">EXAMPLES</a></dt>
<dd>  </dd>
<dt><a href="#lbBK">SECURITY NOTES</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbBL">Limitations of the So ! Sc operator</a></dt>
<dd>  </dd>
<dt><a href="#lbBM">Security implications of Em fast_glob</a></dt>
<dd>  </dd>
<dt><a href="#lbBN">Preventing shell escapes</a></dt>
<dd>  </dd>
<dt><a href="#lbBO">Secure editing</a></dt>
<dd>  </dd>
<dt><a href="#lbBP">Time stamp file checks</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbBQ">DEBUGGING</a></dt>
<dd>  </dd>
<dt><a href="#lbBR">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbBS">AUTHORS</a></dt>
<dd>  </dd>
<dt><a href="#lbBT">CAVEATS</a></dt>
<dd>  </dd>
<dt><a href="#lbBU">BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbBV">SUPPORT</a></dt>
<dd>  </dd>
<dt><a href="#lbBW">DISCLAIMER</a></dt>
<dd>  </dd></dl>
