---
title: "rsyncd(5)"
name: "rsyncd"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rsyncd/"
description: "rsyncd.conf – configuration file for rsync in daemon mode"
---

<p>rsyncd.conf &#8211; configuration file for rsync in daemon mode</p>
<h2>Synopsis</h2>
<p>rsyncd.conf </p>
<h2>Description</h2>
<p>The rsyncd.conf file is the runtime configuration file for rsync when run as an rsync daemon. The rsyncd.conf file controls authentication, access, logging and available modules. </p>
<h2>File Format</h2>
<p>The file consists of modules and parameters. A module begins with the name of the module in square brackets and continues until the next module begins. Modules contain parameters of the form &quot;name = value&quot;. </p>
<p> The file is line-based &#8212; that is, each newline-terminated line represents either a comment, a module name or a parameter. </p>
<p> Only the first equals sign in a parameter is significant. Whitespace before or after the first equals sign is discarded. Leading, trailing and internal whitespace in module and parameter names is irrelevant. Leading and trailing whitespace in a parameter value is discarded. Internal whitespace within a parameter value is retained verbatim. </p>
<p> Any line <code>beginning</code> with a hash (#) is ignored, as are lines containing only whitespace. (If a hash occurs after anything other than leading whitespace, it is considered a part of the line&#8217;s content.) </p>
<p> Any line ending in a \ is &quot;continued&quot; on the next line in the customary UNIX fashion. </p>
<p> The values following the equals sign in parameters are all either a string (no quotes needed) or a boolean, which may be given as yes/no, 0/1 or true/false. Case is not significant in boolean values, but is preserved in string values.</p>
<h2>Launching The Rsync Daemon</h2>
<p>The rsync daemon is launched by specifying the <code>&#8211;daemon</code> option to rsync. </p>
<p> The daemon must run with root privileges if you wish to use chroot, to bind to a port numbered under 1024 (as is the default 873), or to set file ownership. Otherwise, it must just have permission to read and write the appropriate data, log, and lock files. </p>
<p> You can launch it either via inetd, as a stand-alone daemon, or from an rsync client via a remote shell. If run as a stand-alone daemon then just run the command &quot;<code>rsync &#8211;daemon</code>&quot; from a suitable startup script. </p>
<p> When run via inetd you should add a line like this to /etc/services: </p>
<pre> rsync 873/tcp</pre>
<p>and a single line something like this to /etc/inetd.conf: </p>
<pre> rsync stream tcp nowait root /usr/bin/rsync rsyncd --daemon</pre>
<p>Replace &quot;/usr/bin/rsync&quot; with the path to where you have rsync installed on your system. You will then need to send inetd a HUP signal to tell it to reread its config file. </p>
<p> Note that you should <code>not</code> send the rsync daemon a HUP signal to force it to reread the <tt>rsyncd.conf</tt> file. The file is re-read on each client connection.</p>
<h2>Global Parameters</h2>
<p>The first parameters in the file (before a [module] header) are the global parameters. </p>
<p> You may also include any module parameters in the global part of the config file in which case the supplied value will override the default for that parameter. </p>
<p> You may use references to environment variables in the values of parameters. String parameters will have %VAR% references expanded as late as possible (when the string is used in the program), allowing for the use of variables that rsync sets at connection time, such as RSYNC_USER_NAME. Non-string parameters (such as true/false settings) are expanded when read from the config file. If a variable does not exist in the environment, or if a sequence of characters is not a valid reference (such as an un-paired percent sign), the raw characters are passed through unchanged. This helps with backward compatibility and safety (e.g. expanding a non-existent %VAR% to an empty string in a path could result in a very unsafe path). The safest way to insert a literal % into a value is to use %%. </p>
<dl>
<dt><code>motd file</code></p>
<dd>This parameter allows you to specify a &quot;message of the day&quot; to display to clients on each connect. This usually contains site information and any legal notices. The default is no motd file. This can be overridden by the <code>&#8211;dparam=motdfile=FILE</code> command-line option when starting the daemon.</p>
<dd>
<dt><code>pid file</code></p>
<dd>This parameter tells the rsync daemon to write its process ID to that file. If the file already exists, the rsync daemon will abort rather than overwrite the file. This can be overridden by the <code>&#8211;dparam=pidfile=FILE</code> command-line option when starting the daemon.</p>
<dd>
<dt><code>port</code></p>
<dd>You can override the default port the daemon will listen on by specifying this value (defaults to 873). This is ignored if the daemon is being run by inetd, and is superseded by the <code>&#8211;port</code> command-line option.</p>
<dd>
<dt><code>address</code></p>
<dd>You can override the default IP address the daemon will listen on by specifying this value. This is ignored if the daemon is being run by inetd, and is superseded by the <code>&#8211;address</code> command-line option.</p>
<dd>
<dt><code>socket options</code></p>
<dd>This parameter can provide endless fun for people who like to tune their systems to the utmost degree. You can set all sorts of socket options which may make transfers faster (or slower!). Read the man page for the <tt>setsockopt()</tt> system call for details on some of the options you may be able to set. By default no special socket options are set. These settings can also be specified via the <code>&#8211;sockopts</code> command-line option.</p>
<dd>
<dt><code>listen backlog</code></p>
<dd>You can override the default backlog value when the daemon listens for connections. It defaults to 5.</p>
<dd></dl>
<h2>Module Parameters</h2>
<p>After the global parameters you should define a number of modules, each module exports a directory tree as a symbolic name. Modules are exported by specifying a module name in square brackets [module] followed by the parameters for that module. The module name cannot contain a slash or a closing square bracket. If the name contains whitespace, each internal sequence of whitespace will be changed into a single space, while leading or trailing whitespace will be discarded. </p>
<p> As with GLOBAL PARAMETERS, you may use references to environment variables in the values of parameters. See the GLOBAL PARAMETERS section for more details. </p>
<dl>
<dt><code>comment</code></p>
<dd>This parameter specifies a description string that is displayed next to the module name when clients obtain a list of available modules. The default is no comment.</p>
<dd>
<dt><code>path</code></p>
<dd>This parameter specifies the directory in the daemon&#8217;s filesystem to make available in this module. You must specify this parameter for each module in <tt>rsyncd.conf</tt>.</p>
<dd>You may base the path&#8217;s value off of an environment variable by surrounding the variable name with percent signs. You can even reference a variable that is set by rsync when the user connects. For example, this would use the authorizing user&#8217;s name in the path:</p>
<dd>
<pre> path = /home/%RSYNC_USER_NAME% </pre>
<dd>It is fine if the path includes internal spaces &#8212; they will be retained verbatim (which means that you shouldn&#8217;t try to escape them). If your final directory has a trailing space (and this is somehow not something you wish to fix), append a trailing slash to the path to avoid losing the trailing whitespace.</p>
<dd>
<dt><code>use chroot</code></p>
<dd>If &quot;use chroot&quot; is true, the rsync daemon will chroot to the &quot;path&quot; before starting the file transfer with the client. This has the advantage of extra protection against possible implementation security holes, but it has the disadvantages of requiring super-user privileges, of not being able to follow symbolic links that are either absolute or outside of the new root path, and of complicating the preservation of users and groups by name (see below).</p>
<dd>As an additional safety feature, you can specify a dot-dir in the module&#8217;s &quot;path&quot; to indicate the point where the chroot should occur. This allows rsync to run in a chroot with a non-&quot;/&quot; path for the top of the transfer hierarchy. Doing this guards against unintended library loading (since those absolute paths will not be inside the transfer hierarchy unless you have used an unwise pathname), and lets you setup libraries for the chroot that are outside of the transfer. For example, specifying &quot;/var/rsync/./module1&quot; will chroot to the &quot;/var/rsync&quot; directory and set the inside-chroot path to &quot;/module1&quot;. If you had omitted the dot-dir, the chroot would have used the whole path, and the inside-chroot path would have been &quot;/&quot;.</p>
<dd>When &quot;use chroot&quot; is false or the inside-chroot path is not &quot;/&quot;, rsync will: (1) munge symlinks by default for security reasons (see &quot;munge symlinks&quot; for a way to turn this off, but only if you trust your users), (2) substitute leading slashes in absolute paths with the module&#8217;s path (so that options such as <code>&#8211;backup-dir</code>, <code>&#8211;compare-dest</code>, etc. interpret an absolute path as rooted in the module&#8217;s &quot;path&quot; dir), and (3) trim &quot;..&quot; path elements from args if rsync believes they would escape the module hierarchy. The default for &quot;use chroot&quot; is true, and is the safer choice (especially if the module is not read-only).</p>
<dd>When this parameter is enabled, rsync will not attempt to map users and groups by name (by default), but instead copy IDs as though <code>&#8211;numeric-ids</code> had been specified. In order to enable name-mapping, rsync needs to be able to use the standard library functions for looking up names and IDs (i.e. <tt>getpwuid()</tt> , <tt>getgrgid()</tt> , <tt>getpwname()</tt> , and <tt>getgrnam()</tt> ). This means the rsync process in the chroot hierarchy will need to have access to the resources used by these library functions (traditionally /etc/passwd and /etc/group, but perhaps additional dynamic libraries as well).</p>
<dd>If you copy the necessary resources into the module&#8217;s chroot area, you should protect them through your OS&#8217;s normal user/group or ACL settings (to prevent the rsync module&#8217;s user from being able to change them), and then hide them from the user&#8217;s view via &quot;exclude&quot; (see how in the discussion of that parameter). At that point it will be safe to enable the mapping of users and groups by name using the &quot;numeric ids&quot; daemon parameter (see below).</p>
<dd>Note also that you are free to setup custom user/group information in the chroot area that is different from your normal system. For example, you could abbreviate the list of users and groups.</p>
<dd>
<dt><code>numeric ids</code></p>
<dd>Enabling this parameter disables the mapping of users and groups by name for the current daemon module. This prevents the daemon from trying to load any user/group-related files or libraries. This enabling makes the transfer behave as if the client had passed the <code>&#8211;numeric-ids</code> command-line option. By default, this parameter is enabled for chroot modules and disabled for non-chroot modules.</p>
<dd>A chroot-enabled module should not have this parameter enabled unless you&#8217;ve taken steps to ensure that the module has the necessary resources it needs to translate names, and that it is not possible for a user to change those resources.</p>
<dd>
<dt><code>munge symlinks</code></p>
<dd>This parameter tells rsync to modify all symlinks in the same way as the (non-daemon-affecting) <code>&#8211;munge-links</code> command-line option (using a method described below). This should help protect your files from user trickery when your daemon module is writable. The default is disabled when &quot;use chroot&quot; is on and the inside-chroot path is &quot;/&quot;, otherwise it is enabled.</p>
<dd>If you disable this parameter on a daemon that is not read-only, there are tricks that a user can play with uploaded symlinks to access daemon-excluded items (if your module has any), and, if &quot;use chroot&quot; is off, rsync can even be tricked into showing or changing data that is outside the module&#8217;s path (as access-permissions allow).</p>
<dd>The way rsync disables the use of symlinks is to prefix each one with the string &quot;/rsyncd-munged/&quot;. This prevents the links from being used as long as that directory does not exist. When this parameter is enabled, rsync will refuse to run if that path is a directory or a symlink to a directory. When using the &quot;munge symlinks&quot; parameter in a chroot area that has an inside-chroot path of &quot;/&quot;, you should add &quot;/rsyncd-munged/&quot; to the exclude setting for the module so that a user can&#8217;t try to create it.</p>
<dd>Note: rsync makes no attempt to verify that any pre-existing symlinks in the module&#8217;s hierarchy are as safe as you want them to be (unless, of course, it just copied in the whole hierarchy). If you setup an rsync daemon on a new area or locally add symlinks, you can manually protect your symlinks from being abused by prefixing &quot;/rsyncd-munged/&quot; to the start of every symlink&#8217;s value. There is a perl script in the support directory of the source code named &quot;munge-symlinks&quot; that can be used to add or remove this prefix from your symlinks.</p>
<dd>When this parameter is disabled on a writable module and &quot;use chroot&quot; is off (or the inside-chroot path is not &quot;/&quot;), incoming symlinks will be modified to drop a leading slash and to remove &quot;..&quot; path elements that rsync believes will allow a symlink to escape the module&#8217;s hierarchy. There are tricky ways to work around this, though, so you had better trust your users if you choose this combination of parameters.</p>
<dd>
<dt><code>charset</code></p>
<dd>This specifies the name of the character set in which the module&#8217;s filenames are stored. If the client uses an <code>&#8211;iconv</code> option, the daemon will use the value of the &quot;charset&quot; parameter regardless of the character set the client actually passed. This allows the daemon to support charset conversion in a chroot module without extra files in the chroot area, and also ensures that name-translation is done in a consistent manner. If the &quot;charset&quot; parameter is not set, the <code>&#8211;iconv</code> option is refused, just as if &quot;iconv&quot; had been specified via &quot;refuse options&quot;.</p>
<dd>If you wish to force users to always use <code>&#8211;iconv</code> for a particular module, add &quot;no-iconv&quot; to the &quot;refuse options&quot; parameter. Keep in mind that this will restrict access to your module to very new rsync clients.</p>
<dd>
<dt><code>max connections</code></p>
<dd>This parameter allows you to specify the maximum number of simultaneous connections you will allow. Any clients connecting when the maximum has been reached will receive a message telling them to try later. The default is 0, which means no limit. A negative value disables the module. See also the &quot;lock file&quot; parameter.</p>
<dd>
<dt><code>log file</code></p>
<dd>When the &quot;log file&quot; parameter is set to a non-empty string, the rsync daemon will log messages to the indicated file rather than using syslog. This is particularly useful on systems (such as AIX) where <tt>syslog()</tt> doesn&#8217;t work for chrooted programs. The file is opened before <tt>chroot()</tt> is called, allowing it to be placed outside the transfer. If this value is set on a per-module basis instead of globally, the global log will still contain any authorization failures or config-file error messages.</p>
<dd>If the daemon fails to open the specified file, it will fall back to using syslog and output an error about the failure. (Note that the failure to open the specified log file used to be a fatal error.)</p>
<dd>This setting can be overridden by using the <code>&#8211;log-file=FILE</code> or <code>&#8211;dparam=logfile=FILE</code> command-line options. The former overrides all the log-file parameters of the daemon and all module settings. The latter sets the daemon&#8217;s log file and the default for all the modules, which still allows modules to override the default setting.</p>
<dd>
<dt><code>syslog facility</code></p>
<dd>This parameter allows you to specify the syslog facility name to use when logging messages from the rsync daemon. You may use any standard syslog facility name which is defined on your system. Common names are auth, authpriv, cron, daemon, ftp, kern, lpr, mail, news, security, syslog, user, uucp, local0, local1, local2, local3, local4, local5, local6 and local7. The default is daemon. This setting has no effect if the &quot;log file&quot; setting is a non-empty string (either set in the per-modules settings, or inherited from the global settings).</p>
<dd>
<dt><code>max verbosity</code></p>
<dd>This parameter allows you to control the maximum amount of verbose information that you&#8217;ll allow the daemon to generate (since the information goes into the log file). The default is 1, which allows the client to request one level of verbosity.</p>
<dd>This also affects the user&#8217;s ability to request higher levels of <code>&#8211;info</code> and <code>&#8211;debug</code> logging. If the max value is 2, then no info and/or debug value that is higher than what would be set by <code>-vv</code> will be honored by the daemon in its logging. To see how high of a verbosity level you need to accept for a particular info/debug level, refer to &quot;rsync &#8211;info=help&quot; and &quot;rsync &#8211;debug=help&quot;. For instance, it takes max-verbosity 4 to be able to output debug TIME2 and FLIST3.</p>
<dd>
<dt><code>lock file</code></p>
<dd>This parameter specifies the file to use to support the &quot;max connections&quot; parameter. The rsync daemon uses record locking on this file to ensure that the max connections limit is not exceeded for the modules sharing the lock file. The default is <tt>/var/run/rsyncd.lock</tt>.</p>
<dd>
<dt><code>read only</code></p>
<dd>This parameter determines whether clients will be able to upload files or not. If &quot;read only&quot; is true then any attempted uploads will fail. If &quot;read only&quot; is false then uploads will be possible if file permissions on the daemon side allow them. The default is for all modules to be read only.</p>
<dd>Note that &quot;auth users&quot; can override this setting on a per-user basis.</p>
<dd>
<dt><code>write only</code></p>
<dd>This parameter determines whether clients will be able to download files or not. If &quot;write only&quot; is true then any attempted downloads will fail. If &quot;write only&quot; is false then downloads will be possible if file permissions on the daemon side allow them. The default is for this parameter to be disabled.</p>
<dd>
<dt><code>list</code></p>
<dd>This parameter determines whether this module is listed when the client asks for a listing of available modules. In addition, if this is false, the daemon will pretend the module does not exist when a client denied by &quot;hosts allow&quot; or &quot;hosts deny&quot; attempts to access it. Realize that if &quot;reverse lookup&quot; is disabled globally but enabled for the module, the resulting reverse lookup to a potentially client-controlled DNS server may still reveal to the client that it hit an existing module. The default is for modules to be listable.</p>
<dd>
<dt><code>uid</code></p>
<dd>This parameter specifies the user name or user ID that file transfers to and from that module should take place as when the daemon was run as root. In combination with the &quot;gid&quot; parameter this determines what file permissions are available. The default when run by a super-user is to switch to the system&#8217;s &quot;nobody&quot; user. The default for a non-super-user is to not try to change the user. See also the &quot;gid&quot; parameter.</p>
<dd>The RSYNC_USER_NAME environment variable may be used to request that rsync run as the authorizing user. For example, if you want a rsync to run as the same user that was received for the rsync authentication, this setup is useful:</p>
<dd>
<pre> uid = %RSYNC_USER_NAME%
 gid = * </pre>
<dd>
<dt><code>gid</code></p>
<dd>This parameter specifies one or more group names/IDs that will be used when accessing the module. The first one will be the default group, and any extra ones be set as supplemental groups. You may also specify a &quot;*&quot; as the first gid in the list, which will be replaced by all the normal groups for the transfer&#8217;s user (see &quot;uid&quot;). The default when run by a super-user is to switch to your OS&#8217;s &quot;nobody&quot; (or perhaps &quot;nogroup&quot;) group with no other supplementary groups. The default for a non-super-user is to not change any group attributes (and indeed, your OS may not allow a non-super-user to try to change their group settings).</p>
<dd>
<dt><code>fake super</code></p>
<dd>Setting &quot;fake super = yes&quot; for a module causes the daemon side to behave as if the <code>&#8211;fake-super</code> command-line option had been specified. This allows the full attributes of a file to be stored without having to have the daemon actually running as root.</p>
<dd>
<dt><code>filter</code></p>
<dd>The daemon has its own filter chain that determines what files it will let the client access. This chain is not sent to the client and is independent of any filters the client may have specified. Files excluded by the daemon filter chain (<code>daemon-excluded</code> files) are treated as non-existent if the client tries to pull them, are skipped with an error message if the client tries to push them (triggering exit code 23), and are never deleted from the module. You can use daemon filters to prevent clients from downloading or tampering with private administrative files, such as files you may add to support uid/gid name translations.</p>
<dd>The daemon filter chain is built from the &quot;filter&quot;, &quot;include from&quot;, &quot;include&quot;, &quot;exclude from&quot;, and &quot;exclude&quot; parameters, in that order of priority. Anchored patterns are anchored at the root of the module. To prevent access to an entire subtree, for example, &quot;/secret&quot;, you <i>must</i> exclude everything in the subtree; the easiest way to do this is with a triple-star pattern like &quot;/secret/***&quot;.</p>
<dd>The &quot;filter&quot; parameter takes a space-separated list of daemon filter rules, though it is smart enough to know not to split a token at an internal space in a rule (e.g. &quot;- /foo &#8211; /bar&quot; is parsed as two rules). You may specify one or more merge-file rules using the normal syntax. Only one &quot;filter&quot; parameter can apply to a given module in the config file, so put all the rules you want in a single parameter. Note that per-directory merge-file rules do not provide as much protection as global rules, but they can be used to make <code>&#8211;delete</code> work better during a client download operation if the per-dir merge files are included in the transfer and the client requests that they be used.</p>
<dd>
<dt><code>exclude</code></p>
<dd>This parameter takes a space-separated list of daemon exclude patterns. As with the client <code>&#8211;exclude</code> option, patterns can be qualified with &quot;- &quot; or &quot;+ &quot; to explicitly indicate exclude/include. Only one &quot;exclude&quot; parameter can apply to a given module. See the &quot;filter&quot; parameter for a description of how excluded files affect the daemon.</p>
<dd>
<dt><code>include</code></p>
<dd>Use an &quot;include&quot; to override the effects of the &quot;exclude&quot; parameter. Only one &quot;include&quot; parameter can apply to a given module. See the &quot;filter&quot; parameter for a description of how excluded files affect the daemon.</p>
<dd>
<dt><code>exclude from</code></p>
<dd>This parameter specifies the name of a file on the daemon that contains daemon exclude patterns, one per line. Only one &quot;exclude from&quot; parameter can apply to a given module; if you have multiple exclude-from files, you can specify them as a merge file in the &quot;filter&quot; parameter. See the &quot;filter&quot; parameter for a description of how excluded files affect the daemon.</p>
<dd>
<dt><code>include from</code></p>
<dd>Analogue of &quot;exclude from&quot; for a file of daemon include patterns. Only one &quot;include from&quot; parameter can apply to a given module. See the &quot;filter&quot; parameter for a description of how excluded files affect the daemon.</p>
<dd>
<dt><code>incoming chmod</code></p>
<dd>This parameter allows you to specify a set of comma-separated chmod strings that will affect the permissions of all incoming files (files that are being received by the daemon). These changes happen after all other permission calculations, and this will even override destination-default and/or existing permissions when the client does not specify <code>&#8211;perms</code>. See the description of the <code>&#8211;chmod</code> rsync option and the <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) manpage for information on the format of this string.</p>
<dd>
<dt><code>outgoing chmod</code></p>
<dd>This parameter allows you to specify a set of comma-separated chmod strings that will affect the permissions of all outgoing files (files that are being sent out from the daemon). These changes happen first, making the sent permissions appear to be different than those stored in the filesystem itself. For instance, you could disable group write permissions on the server while having it appear to be on to the clients. See the description of the <code>&#8211;chmod</code> rsync option and the <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) manpage for information on the format of this string.</p>
<dd>
<dt><code>auth users</code></p>
<dd>This parameter specifies a comma and/or space-separated list of authorization rules. In its simplest form, you list the usernames that will be allowed to connect to this module. The usernames do not need to exist on the local system. The rules may contain shell wildcard characters that will be matched against the username provided by the client for authentication. If &quot;auth users&quot; is set then the client will be challenged to supply a username and password to connect to the module. A challenge response authentication protocol is used for this exchange. The plain text usernames and passwords are stored in the file specified by the &quot;secrets file&quot; parameter. The default is for all users to be able to connect without a password (this is called &quot;anonymous rsync&quot;).</p>
<dd>In addition to username matching, you can specify groupname matching via a &#8216;@&#8217; prefix. When using groupname matching, the authenticating username must be a real user on the system, or it will be assumed to be a member of no groups. For example, specifying &quot;@rsync&quot; will match the authenticating user if the named user is a member of the rsync group.</p>
<dd>Finally, options may be specified after a colon (:). The options allow you to &quot;deny&quot; a user or a group, set the access to &quot;ro&quot; (read-only), or set the access to &quot;rw&quot; (read/write). Setting an auth-rule-specific ro/rw setting overrides the module&#8217;s &quot;read only&quot; setting.</p>
<dd>Be sure to put the rules in the order you want them to be matched, because the checking stops at the first matching user or group, and that is the only auth that is checked. For example:</p>
<dd>
<pre> auth users = joe:deny @guest:deny admin:rw @rsync:ro susan joe sam </pre>
<dd>In the above rule, user joe will be denied access no matter what. Any user that is in the group &quot;guest&quot; is also denied access. The user &quot;admin&quot; gets access in read/write mode, but only if the admin user is not in group &quot;guest&quot; (because the admin user-matching rule would never be reached if the user is in group &quot;guest&quot;). Any other user who is in group &quot;rsync&quot; will get read-only access. Finally, users susan, joe, and sam get the ro/rw setting of the module, but only if the user didn&#8217;t match an earlier group-matching rule.</p>
<dd>See the description of the secrets file for how you can have per-user passwords as well as per-group passwords. It also explains how a user can authenticate using their user password or (when applicable) a group password, depending on what rule is being authenticated.</p>
<dd>See also the section entitled &quot;USING RSYNC-DAEMON FEATURES VIA A REMOTE SHELL CONNECTION&quot; in <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1) for information on how handle an rsyncd.conf-level username that differs from the remote-shell-level username when using a remote shell to connect to an rsync daemon.</p>
<dd>
<dt><code>secrets file</code></p>
<dd>This parameter specifies the name of a file that contains the username:password and/or @groupname:password pairs used for authenticating this module. This file is only consulted if the &quot;auth users&quot; parameter is specified. The file is line-based and contains one name:password pair per line. Any line has a hash (#) as the very first character on the line is considered a comment and is skipped. The passwords can contain any characters but be warned that many operating systems limit the length of passwords that can be typed at the client end, so you may find that passwords longer than 8 characters don&#8217;t work.</p>
<dd>The use of group-specific lines are only relevant when the module is being authorized using a matching &quot;@groupname&quot; rule. When that happens, the user can be authorized via either their &quot;username:password&quot; line or the &quot;@groupname:password&quot; line for the group that triggered the authentication.</p>
<dd>It is up to you what kind of password entries you want to include, either users, groups, or both. The use of group rules in &quot;auth users&quot; does not require that you specify a group password if you do not want to use shared passwords.</p>
<dd>There is no default for the &quot;secrets file&quot; parameter, you must choose a name (such as <tt>/etc/rsyncd.secrets</tt>). The file must normally not be readable by &quot;other&quot;; see &quot;strict modes&quot;. If the file is not found or is rejected, no logins for a &quot;user auth&quot; module will be possible.</p>
<dd>
<dt><code>strict modes</code></p>
<dd>This parameter determines whether or not the permissions on the secrets file will be checked. If &quot;strict modes&quot; is true, then the secrets file must not be readable by any user ID other than the one that the rsync daemon is running under. If &quot;strict modes&quot; is false, the check is not performed. The default is true. This parameter was added to accommodate rsync running on the Windows operating system.</p>
<dd>
<dt><code>hosts allow</code></p>
<dd>This parameter allows you to specify a list of patterns that are matched against a connecting clients hostname and IP address. If none of the patterns match then the connection is rejected.</p>
<dd>Each pattern can be in one of five forms:</p>
<dd>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>a dotted decimal IPv4 address of the form a.b.c.d, or an IPv6 address of the form a:b:c::d:e:f. In this case the incoming machine&#8217;s IP address must match exactly.</p>
<dt>o</p>
<dd>an address/mask in the form ipaddr/n where ipaddr is the IP address and n is the number of one bits in the netmask. All IP addresses which match the masked IP address will be allowed in.</p>
<dt>o</p>
<dd>an address/mask in the form ipaddr/maskaddr where ipaddr is the IP address and maskaddr is the netmask in dotted decimal notation for IPv4, or similar for IPv6, e.g. ffff:ffff:ffff:ffff:: instead of /64. All IP addresses which match the masked IP address will be allowed in.</p>
<dt>o</p>
<dd>a hostname pattern using wildcards. If the hostname of the connecting IP (as determined by a reverse lookup) matches the wildcarded name (using the same rules as normal unix filename matching), the client is allowed in. This only works if &quot;reverse lookup&quot; is enabled (the default).</p>
<dt>o</p>
<dd>a hostname. A plain hostname is matched against the reverse DNS of the connecting IP (if &quot;reverse lookup&quot; is enabled), and/or the IP of the given hostname is matched against the connecting IP (if &quot;forward lookup&quot; is enabled, as it is by default). Any match will be allowed in.</dl>
</dl>
<dd>Note IPv6 link-local addresses can have a scope in the address specification:</p>
<dd>
<dl>
<dd><tt> fe80::1%link1</tt><br />
 <tt> fe80::%link1/64</tt><br />
 <tt> fe80::%link1/ffff:ffff:ffff:ffff::</tt>
</dl>
<dd>You can also combine &quot;hosts allow&quot; with a separate &quot;hosts deny&quot; parameter. If both parameters are specified then the &quot;hosts allow&quot; parameter is checked first and a match results in the client being able to connect. The &quot;hosts deny&quot; parameter is then checked and a match means that the host is rejected. If the host does not match either the &quot;hosts allow&quot; or the &quot;hosts deny&quot; patterns then it is allowed to connect.</p>
<dd>The default is no &quot;hosts allow&quot; parameter, which means all hosts can connect.</p>
<dd>
<dt><code>hosts deny</code></p>
<dd>This parameter allows you to specify a list of patterns that are matched against a connecting clients hostname and IP address. If the pattern matches then the connection is rejected. See the &quot;hosts allow&quot; parameter for more information.</p>
<dd>The default is no &quot;hosts deny&quot; parameter, which means all hosts can connect.</p>
<dd>
<dt><code>reverse lookup</code></p>
<dd>Controls whether the daemon performs a reverse lookup on the client&#8217;s IP address to determine its hostname, which is used for &quot;hosts allow&quot;/&quot;hosts deny&quot; checks and the &quot;%h&quot; log escape. This is enabled by default, but you may wish to disable it to save time if you know the lookup will not return a useful result, in which case the daemon will use the name &quot;UNDETERMINED&quot; instead.</p>
<dd>If this parameter is enabled globally (even by default), rsync performs the lookup as soon as a client connects, so disabling it for a module will not avoid the lookup. Thus, you probably want to disable it globally and then enable it for modules that need the information.</p>
<dd>
<dt><code>forward lookup</code></p>
<dd>Controls whether the daemon performs a forward lookup on any hostname specified in an hosts allow/deny setting. By default this is enabled, allowing the use of an explicit hostname that would not be returned by reverse DNS of the connecting IP.</p>
<dd>
<dt><code>ignore errors</code></p>
<dd>This parameter tells rsyncd to ignore I/O errors on the daemon when deciding whether to run the delete phase of the transfer. Normally rsync skips the <code>&#8211;delete</code> step if any I/O errors have occurred in order to prevent disastrous deletion due to a temporary resource shortage or other I/O error. In some cases this test is counter productive so you can use this parameter to turn off this behavior.</p>
<dd>
<dt><code>ignore nonreadable</code></p>
<dd>This tells the rsync daemon to completely ignore files that are not readable by the user. This is useful for public archives that may have some non-readable files among the directories, and the sysadmin doesn&#8217;t want those files to be seen at all.</p>
<dd>
<dt><code>transfer logging</code></p>
<dd>This parameter enables per-file logging of downloads and uploads in a format somewhat similar to that used by ftp daemons. The daemon always logs the transfer at the end, so if a transfer is aborted, no mention will be made in the log file.</p>
<dd>If you want to customize the log lines, see the &quot;log format&quot; parameter.</p>
<dd>
<dt><code>log format</code></p>
<dd>This parameter allows you to specify the format used for logging file transfers when transfer logging is enabled. The format is a text string containing embedded single-character escape sequences prefixed with a percent (%) character. An optional numeric field width may also be specified between the percent and the escape letter (e.g. &quot;<code>%-50n %8l %07p</code>&quot;). In addition, one or more apostrophes may be specified prior to a numerical escape to indicate that the numerical value should be made more human-readable. The 3 supported levels are the same as for the <code>&#8211;human-readable</code> command-line option, though the default is for human-readability to be off. Each added apostrophe increases the level (e.g. &quot;<code>%&#8221;l %&#8217;b %f</code>&quot;).</p>
<dd>The default log format is &quot;%o %h [%a] %m (%u) %f %l&quot;, and a &quot;%t [%p] &quot; is always prefixed when using the &quot;log file&quot; parameter. (A perl script that will summarize this default log format is included in the rsync source code distribution in the &quot;support&quot; subdirectory: rsyncstats.)</p>
<dd>The single-character escapes that are understood are as follows:</p>
<dd>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>%a the remote IP address (only available for a daemon)</p>
<dt>o</p>
<dd>%b the number of bytes actually transferred</p>
<dt>o</p>
<dd>%B the permission bits of the file (e.g. rwxrwxrwt)</p>
<dt>o</p>
<dd>%c the total size of the block checksums received for the basis file (only when sending)</p>
<dt>o</p>
<dd>%C the full-file MD5 checksum if <code>&#8211;checksum</code> is enabled or a file was transferred (only for protocol 30 or above).</p>
<dt>o</p>
<dd>%f the filename (long form on sender; no trailing &quot;/&quot;)</p>
<dt>o</p>
<dd>%G the gid of the file (decimal) or &quot;DEFAULT&quot;</p>
<dt>o</p>
<dd>%h the remote host name (only available for a daemon)</p>
<dt>o</p>
<dd>%i an itemized list of what is being updated</p>
<dt>o</p>
<dd>%l the length of the file in bytes</p>
<dt>o</p>
<dd>%L the string &quot; -&gt; SYMLINK&quot;, &quot; =&gt; HARDLINK&quot;, or &quot;&quot; (where <code>SYMLINK</code> or <code>HARDLINK</code> is a filename)</p>
<dt>o</p>
<dd>%m the module name</p>
<dt>o</p>
<dd>%M the last-modified time of the file</p>
<dt>o</p>
<dd>%n the filename (short form; trailing &quot;/&quot; on dir)</p>
<dt>o</p>
<dd>%o the operation, which is &quot;send&quot;, &quot;recv&quot;, or &quot;del.&quot; (the latter includes the trailing period)</p>
<dt>o</p>
<dd>%p the process ID of this rsync session</p>
<dt>o</p>
<dd>%P the module path</p>
<dt>o</p>
<dd>%t the current date time</p>
<dt>o</p>
<dd>%u the authenticated username or an empty string</p>
<dt>o</p>
<dd>%U the uid of the file (decimal)</dl>
</dl>
<dd>For a list of what the characters mean that are output by &quot;%i&quot;, see the <code>&#8211;itemize-changes</code> option in the rsync manpage.</p>
<dd>Note that some of the logged output changes when talking with older rsync versions. For instance, deleted files were only output as verbose messages prior to rsync 2.6.4.</p>
<dd>
<dt><code>timeout</code></p>
<dd>This parameter allows you to override the clients choice for I/O timeout for this module. Using this parameter you can ensure that rsync won&#8217;t wait on a dead client forever. The timeout is specified in seconds. A value of zero means no timeout and is the default. A good choice for anonymous rsync daemons may be 600 (giving a 10 minute timeout).</p>
<dd>
<dt><code>refuse options</code></p>
<dd>This parameter allows you to specify a space-separated list of rsync command line options that will be refused by your rsync daemon. You may specify the full option name, its one-letter abbreviation, or a wild-card string that matches multiple options. For example, this would refuse <code>&#8211;checksum</code> (<code>-c</code>) and all the various delete options:</p>
<dd>
<dl>
<dd><tt> refuse options = c delete</tt></dl>
<dd>The reason the above refuses all delete options is that the options imply <code>&#8211;delete</code>, and implied options are refused just like explicit options. As an additional safety feature, the refusal of &quot;delete&quot; also refuses <code>remove-source-files</code> when the daemon is the sender; if you want the latter without the former, instead refuse &quot;delete-*&quot; &#8212; that refuses all the delete modes without affecting <code>&#8211;remove-source-files</code>.</p>
<dd>When an option is refused, the daemon prints an error message and exits. To prevent all compression when serving files, you can use &quot;dont compress = *&quot; (see below) instead of &quot;refuse options = compress&quot; to avoid returning an error to a client that requests compression.</p>
<dd>
<dt><code>dont compress</code></p>
<dd>This parameter allows you to select filenames based on wildcard patterns that should not be compressed when pulling files from the daemon (no analogous parameter exists to govern the pushing of files to a daemon). Compression is expensive in terms of CPU usage, so it is usually good to not try to compress files that won&#8217;t compress well, such as already compressed files.</p>
<dd>The &quot;dont compress&quot; parameter takes a space-separated list of case-insensitive wildcard patterns. Any source filename matching one of the patterns will not be compressed during transfer.</p>
<dd>See the <code>&#8211;skip-compress</code> parameter in the <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1) manpage for the list of file suffixes that are not compressed by default. Specifying a value for the &quot;dont compress&quot; parameter changes the default when the daemon is the sender.</p>
<dd>
<dt><code>pre-xfer exec</code>, <code>post-xfer exec</code></p>
<dd>You may specify a command to be run before and/or after the transfer. If the <code>pre-xfer exec</code> command fails, the transfer is aborted before it begins. Any output from the script on stdout (up to several KB) will be displayed to the user when aborting, but is NOT displayed if the script returns success. Any output from the script on stderr goes to the daemon&#8217;s stderr, which is typically discarded (though see &#8211;no-detatch option for a way to see the stderr output, which can assist with debugging).</p>
<dd>The following environment variables will be set, though some are specific to the pre-xfer or the post-xfer environment:</p>
<dd>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><code>RSYNC_MODULE_NAME</code>: The name of the module being accessed.</p>
<dt>o</p>
<dd><code>RSYNC_MODULE_PATH</code>: The path configured for the module.</p>
<dt>o</p>
<dd><code>RSYNC_HOST_ADDR</code>: The accessing host&#8217;s IP address.</p>
<dt>o</p>
<dd><code>RSYNC_HOST_NAME</code>: The accessing host&#8217;s name.</p>
<dt>o</p>
<dd><code>RSYNC_USER_NAME</code>: The accessing user&#8217;s name (empty if no user).</p>
<dt>o</p>
<dd><code>RSYNC_PID</code>: A unique number for this transfer.</p>
<dt>o</p>
<dd><code>RSYNC_REQUEST</code>: (pre-xfer only) The module/path info specified by the user. Note that the user can specify multiple source files, so the request can be something like &quot;mod/path1 mod/path2&quot;, etc.</p>
<dt>o</p>
<dd><code>RSYNC_ARG#</code>: (pre-xfer only) The pre-request arguments are set in these numbered values. RSYNC_ARG0 is always &quot;rsyncd&quot;, followed by the options that were used in RSYNC_ARG1, and so on. There will be a value of &quot;.&quot; indicating that the options are done and the path args are beginning &#8212; these contain similar information to RSYNC_REQUEST, but with values separated and the module name stripped off.</p>
<dt>o</p>
<dd><code>RSYNC_EXIT_STATUS</code>: (post-xfer only) the server side&#8217;s exit value. This will be 0 for a successful run, a positive value for an error that the server generated, or a -1 if rsync failed to exit properly. Note that an error that occurs on the client side does not currently get sent to the server side, so this is not the final exit status for the whole transfer.</p>
<dt>o</p>
<dd><code>RSYNC_RAW_STATUS</code>: (post-xfer only) the raw exit value from <tt>waitpid()</tt> .</dl>
</dl>
<dd>Even though the commands can be associated with a particular module, they are run using the permissions of the user that started the daemon (not the module&#8217;s uid/gid setting) without any chroot restrictions.</p>
<dd></dl>
<h2>Config Directives</h2>
<p>There are currently two config directives available that allow a config file to incorporate the contents of other files: <code>&amp;include</code> and <code>&amp;merge</code>. Both allow a reference to either a file or a directory. They differ in how segregated the file&#8217;s contents are considered to be. </p>
<p> The <code>&amp;include</code> directive treats each file as more distinct, with each one inheriting the defaults of the parent file, starting the parameter parsing as globals/defaults, and leaving the defaults unchanged for the parsing of the rest of the parent file. </p>
<p> The <code>&amp;merge</code> directive, on the other hand, treats the file&#8217;s contents as if it were simply inserted in place of the directive, and thus it can set parameters in a module started in another file, can affect the defaults for other files, etc. </p>
<p> When an <code>&amp;include</code> or <code>&amp;merge</code> directive refers to a directory, it will read in all the <code>*.conf</code> or <code>*.inc</code> files (respectively) that are contained inside that directory (without any recursive scanning), with the files sorted into alpha order. So, if you have a directory named &quot;rsyncd.d&quot; with the files &quot;foo.conf&quot;, &quot;bar.conf&quot;, and &quot;baz.conf&quot; inside it, this directive: </p>
<pre> &amp;include /path/rsyncd.d </pre>
<p>would be the same as this set of directives: </p>
<pre> &amp;include /path/rsyncd.d/bar.conf
 &amp;include /path/rsyncd.d/baz.conf
 &amp;include /path/rsyncd.d/foo.conf </pre>
<p>except that it adjusts as files are added and removed from the directory. </p>
<p> The advantage of the <code>&amp;include</code> directive is that you can define one or more modules in a separate file without worrying about unintended side-effects between the self-contained module files. </p>
<p> The advantage of the <code>&amp;merge</code> directive is that you can load config snippets that can be included into multiple module definitions, and you can also set global values that will affect connections (such as <code>motd file</code>), or globals that will affect other include files. </p>
<p> For example, this is a useful /etc/rsyncd.conf file: </p>
<pre> port = 873
 log file = /var/log/rsync.log
 pid file = /var/lock/rsync.lock
 &amp;merge /etc/rsyncd.d
 &amp;include /etc/rsyncd.d </pre>
<p>This would merge any /etc/rsyncd.d/*.inc files (for global values that should stay in effect), and then include any /etc/rsyncd.d/*.conf files (defining modules without any global-value cross-talk).</p>
<h2>Authentication Strength</h2>
<p>The authentication protocol used in rsync is a 128 bit MD4 based challenge response system. This is fairly weak protection, though (with at least one brute-force hash-finding algorithm publicly available), so if you want really top-quality security, then I recommend that you run rsync over ssh. (Yes, a future version of rsync will switch over to a stronger hashing method.) </p>
<p> Also note that the rsync daemon protocol does not currently provide any encryption of the data that is transferred over the connection. Only authentication is provided. Use ssh as the transport if you want encryption. </p>
<p> Future versions of rsync may support SSL for better authentication and encryption, but that is still being investigated.</p>
<h2>Examples</h2>
<p>A simple rsyncd.conf file that allow anonymous rsync to a ftp area at <tt>/home/ftp</tt> would be: </p>
<pre>[ftp]
 path = /home/ftp
 comment = ftp export area</pre>
<p>A more sophisticated example would be: </p>
<pre>uid = nobody
gid = nobody
use chroot = yes
max connections = 4
syslog facility = local5
pid file = /var/run/rsyncd.pid
[ftp]
 path = /var/ftp/./pub
 comment = whole ftp area (approx 6.1 GB)
[sambaftp]
 path = /var/ftp/./pub/samba
 comment = Samba ftp area (approx 300 MB)
[rsyncftp]
 path = /var/ftp/./pub/rsync
 comment = rsync ftp area (approx 6 MB)
[sambawww]
 path = /public_html/samba
 comment = Samba WWW pages (approx 240 MB)
[cvs]
 path = /data/cvs
 comment = CVS repository (requires authentication)
 auth users = tridge, susan
 secrets file = /etc/rsyncd.secrets</pre>
<p>The /etc/rsyncd.secrets file would look something like this:</p>
<dl>
<dd><tt>tridge:mypass</tt><br />
 <tt>susan:herpass</tt>
</dl>
<h2>Files</h2>
<p>/etc/rsyncd.conf or rsyncd.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1) </p>
<h2>Diagnostics</h2>
<h2>Bugs</h2>
<p>Please report bugs! The rsync bug tracking system is online at <a rel="nofollow" href="http://rsync.samba.org/">http://rsync.samba.org/</a> </p>
<h2>Version</h2>
<p>This man page is current for version 3.1.1 of rsync.</p>
<h2>Credits</h2>
<p>rsync is distributed under the GNU General Public License. See the file COPYING for details. </p>
<p> The primary ftp site for rsync is <a href="ftp://rsync.samba.org/pub/rsync.">ftp://rsync.samba.org/pub/rsync.</a> </p>
<p> A WEB site is available at <a rel="nofollow" href="http://rsync.samba.org/">http://rsync.samba.org/</a> </p>
<p> We would be delighted to hear from you if you like this program. </p>
<p> This program uses the zlib compression library written by Jean-loup Gailly and Mark Adler.</p>
<h2>Thanks</h2>
<p>Thanks to Warren Stanley for his original idea and patch for the rsync daemon. Thanks to Karsten Thygesen for his many suggestions and documentation!</p>
<h2>Author</h2>
<p>rsync was written by Andrew Tridgell and Paul Mackerras. Many people have later contributed to it. </p>
<p> Mailing lists for support and development are available at <a rel="nofollow" href="http://lists.samba.org">http://lists.samba.org</a></p>
